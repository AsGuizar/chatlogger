# 💬 Real-Time WebSocket Chat System

A lightweight, real-time chat application built with Python WebSockets, featuring a web-based client interface and live administrative dashboard. Perfect for classroom demonstrations and small group communications.

![Status](https://img.shields.io/badge/status-active-success.svg)
![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![WebSocket](https://img.shields.io/badge/websocket-supported-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

## ✨ Features

- 🚀 **Real-time Communication** - Instant message delivery using WebSocket protocol
- 🌐 **Web-Based Client** - No installation required, runs in any modern browser
- 📊 **Live Dashboard** - Monitor all connections and messages in real-time
- ☁️ **Cloud Ready** - Deployed on Render with automatic scaling
- 👥 **Multi-Client Support** - Up to 100 using render free tier
- 🎨 **Modern UI** - Clean, responsive interface with gradient designs
- 🔔 **System Notifications** - Real-time alerts for user joins/leaves

## 🎯 Demo

```bash
# Quick start in 3 steps:
1. Deploy server to Render
2. Share web_client.html with users
3. Open dashboard.html to monitor activity
```

**Live Example:**
- Server: `wss://chatlogger-1.onrender.com`
- Users connect via browser, no downloads needed!

## 📋 Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Architecture](#architecture)
- [Deployment](#deployment)
- [API Reference](#api-reference)

## 🛠️ Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager
- Modern web browser (Chrome, Firefox, Safari, Edge)

### Local Setup

1. **Clone the repository**
```bash
git clone https://github.com/AsGuizar/chatlogger.git
cd websocket-chat
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the server**
```bash
python server.py
```

4. **Open the client**
- Double-click `web_client.html` in your browser
- Or open `dashboard.html` for monitoring

## 🚀 Usage

### For End Users

1. **Open `web_client.html`** in your browser
2. **Enter your name** (e.g., "Alice")
3. **Enter server address**:
   - Local: `localhost`
   - Cloud: `your-app.onrender.com`
4. **Click "Conectar"** and start chatting!

### For Administrators

1. **Open `dashboard.html`** in your browser
2. **Monitor live activity**:
   - Active connections count
   - Total messages sent
   - Real-time activity log
   - Connected users list
```

## 🏗️ Architecture

### System Overview

```
┌─────────────────────────────────────┐
│         Render Cloud ☁️             │
│                                     │
│  ┌───────────────────────────────┐ │
│  │   WebSocket Server (Python)   │ │
│  │   • Authentication            │ │
│  │   • Message Broadcasting      │ │
│  │   • Connection Management     │ │
│  └───────────────────────────────┘ │
└─────────────────┬───────────────────┘
                  │
        ┌─────────┼─────────┐
        │         │         │
        ▼         ▼         ▼
    Client1   Client2   Dashboard
```

### Tech Stack

- **Backend**: Python 3.8+ with `websockets` library
- **Frontend**: Vanilla JavaScript (ES6+), HTML5, CSS3
- **Protocol**: WebSocket (WS/WSS)
- **Deployment**: Render.com
- **No Frameworks**: Zero dependencies on frontend

## ☁️ Deployment

### Deploy to Render (Recommended)

1. **Create `requirements.txt`**:
```txt
websockets
```

2. **Configure Render**:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python server.py`
   - **Plan**: Free
   - **Environment**: Python 3

3. **Get your URL**: `https://your-app.onrender.com`

4. **Update clients**: Share the URL (without `https://`)

## 📡 API Reference

### WebSocket Messages

#### Client → Server

**Authentication**
```json
{
  "accion": "auth",
  "nombre": "Alice"
}
```

**Send Message**
```json
{
  "texto": "Hello, world!",
  "timestamp": "2025-09-30T12:00:00.000Z"
}
```

#### Server → Client

**Authentication Success**
```json
{
  "tipo": "auth_ok",
  "mensaje": "Bienvenido Alice",
  "total_nodos": 5
}
```

**User Joined**
```json
{
  "tipo": "nodo_conectado",
  "nodo": "Bob",
  "total_nodos": 6
}
```

**User Left**
```json
{
  "tipo": "nodo_desconectado",
  "nodo": "Charlie",
  "total_nodos": 5
}
```

**Broadcast Message**
```json
{
  "tipo": "mensaje",
  "remitente": "Alice",
  "contenido": {
    "texto": "Hello, world!",
    "timestamp": "2025-09-30T12:00:00.000Z"
  },
  "timestamp": "2025-09-30T12:00:01.234Z"
}
```

## 🐛 Troubleshooting

### Connection Issues

**Problem**: Can't connect to server

**Solutions**:
- ✅ Check server is running (Render dashboard shows "Active")
- ✅ Wait 30-60 seconds for Render to wake from sleep
- ✅ Verify URL is correct (no `https://` prefix)
- ✅ Check browser console (F12) for errors
- ✅ Use `wss://` for cloud, `ws://` for localhost

### Message Not Appearing

**Problem**: Messages sent but not received

**Solutions**:
- ✅ Check browser console for JavaScript errors
- ✅ Verify WebSocket connection is open (readyState === 1)
- ✅ Ensure server broadcast function is working
- ✅ Check server logs in Render dashboard

### Render Free Tier Sleep

**Problem**: Server sleeps after 15 minutes

**Solutions**:
- ✅ Use [UptimeRobot](https://uptimerobot.com/) to ping every 14 minutes
- ✅ Warn users about 30-second wake-up time
- ✅ Consider upgrading to paid tier for always-on

## 📁 Project Structure

```
websocket-chat/
├── server.py              # WebSocket server (Python)
├── web_client.html        # User chat interface
├── dashboard.html         # Admin monitoring panel
├── requirements.txt       # Python dependencies
├── README.md             # This file
```

## 🎓 Educational Use

This project was created for educational purposes to demonstrate:
- WebSocket protocol implementation
- Real-time bidirectional communication
- Async/await patterns in Python
- Event-driven architecture
- Cloud deployment workflows


## 📝 License

This project is licensed under the MIT License.

## 👥 Authors

- (https://github.com/AsGuizar)

## 🙏 Acknowledgments

- Python `websockets` library by Aymeric Augustin
- Render.com for free hosting

## 🌟 Star History

If you find this project useful, please consider giving it a star! ⭐

## 📚 Learn More

- [WebSocket Protocol (RFC 6455)](https://tools.ietf.org/html/rfc6455)
- [Python websockets Documentation](https://websockets.readthedocs.io/)
- [Render Guide](https://render.com/docs)

---

**Made with ❤️ for educational purposes**

*Last Updated: September 30, 2025*