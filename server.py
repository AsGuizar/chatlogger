import asyncio
import websockets
import json
from datetime import datetime
from collections import defaultdict

# Storage for connected nodes
nodos = {}  # {websocket: {"nombre": str, "conectado_en": datetime}}
mensajes_log = []  # Lista de todos los mensajes para el historial

async def broadcast(mensaje, remitente_ws=None):
    """Envía un mensaje a todos los nodos conectados excepto al remitente"""
    if not nodos:
        return
    
    # Crear lista de tareas para enviar en paralelo
    tareas = []
    for websocket in nodos:
        if websocket != remitente_ws:
            tareas.append(asyncio.create_task(websocket.send(mensaje)))
    
    # Ejecutar todos los envíos en paralelo
    if tareas:
        await asyncio.gather(*tareas, return_exceptions=True)

async def manejar_conexion(websocket):
    nodo_info = None
    
    try:
        # Esperar autenticación
        mensaje_auth = await websocket.recv()
        data = json.loads(mensaje_auth)
        
        if data.get("accion") == "auth":
            nombre_nodo = data.get("nombre", "Anónimo")
            nodo_info = {
                "nombre": nombre_nodo,
                "conectado_en": datetime.now(),
                "address": websocket.remote_address
            }
            nodos[websocket] = nodo_info
            
            print(f"✨ Nodo '{nombre_nodo}' conectado desde {websocket.remote_address}. Total: {len(nodos)}")
            
            # Registrar en el log
            log_entry = {
                "tipo": "conexion",
                "nodo": nombre_nodo,
                "timestamp": datetime.now().isoformat(),
                "address": str(websocket.remote_address)
            }
            mensajes_log.append(log_entry)
            
            # Confirmar autenticación
            await websocket.send(json.dumps({
                "tipo": "auth_ok",
                "mensaje": f"Bienvenido {nombre_nodo}",
                "total_nodos": len(nodos)
            }))
            
            # Notificar a otros nodos
            notificacion = json.dumps({
                "tipo": "nodo_conectado",
                "nodo": nombre_nodo,
                "total_nodos": len(nodos)
            })
            await broadcast(notificacion, websocket)
            
            # Loop principal para recibir mensajes
            async for mensaje in websocket:
                try:
                    data = json.loads(mensaje)
                    print(f"📥 Mensaje de '{nombre_nodo}': {data}")
                    
                    # Registrar en el log
                    log_entry = {
                        "tipo": "mensaje",
                        "nodo": nombre_nodo,
                        "contenido": data,
                        "timestamp": datetime.now().isoformat()
                    }
                    mensajes_log.append(log_entry)
                    
                    # Reenviar a todos los demás nodos
                    mensaje_broadcast = json.dumps({
                        "tipo": "mensaje",
                        "remitente": nombre_nodo,
                        "contenido": data,
                        "timestamp": datetime.now().isoformat()
                    })
                    await broadcast(mensaje_broadcast, websocket)
                    
                except json.JSONDecodeError:
                    print(f"⚠️ Mensaje no JSON de '{nombre_nodo}': {mensaje}")
                    
    except websockets.exceptions.ConnectionClosed:
        print(f"🔌 Conexión cerrada normalmente")
    except Exception as e:
        print(f"❌ Error en la conexión: {e}")
    finally:
        # Limpiar al desconectar
        if websocket in nodos:
            nombre = nodos[websocket]["nombre"]
            del nodos[websocket]
            print(f"👋 Nodo '{nombre}' desconectado. Total: {len(nodos)}")
            
            # Registrar desconexión
            log_entry = {
                "tipo": "desconexion",
                "nodo": nombre,
                "timestamp": datetime.now().isoformat()
            }
            mensajes_log.append(log_entry)
            
            # Notificar desconexión
            notificacion = json.dumps({
                "tipo": "nodo_desconectado",
                "nodo": nombre,
                "total_nodos": len(nodos)
            })
            await broadcast(notificacion)

async def main():
    # Iniciar servidor WebSocket
    async with websockets.serve(
        manejar_conexion,
        "0.0.0.0",
        8765
    ):
        print("🚀 Servidor WebSocket iniciado en ws://0.0.0.0:8765")
        print("📊 Para ver el dashboard, abre dashboard.html en tu navegador")
        print("   (El dashboard se conectará automáticamente al servidor)")
        await asyncio.Future()  # Mantener corriendo indefinidamente

if __name__ == "__main__":
    asyncio.run(main())