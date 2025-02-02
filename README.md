# 🔄 Secure File Transfer

A **Python-based** encrypted file transfer system for **LAN** using **AES encryption**. Supports **GUI (Tkinter) & CLI**, with **Docker compatibility**.

---

## 🚀 Features
✔ **AES encryption** 🔒  
✔ **Tkinter GUI & CLI** 🖥  
✔ **Multi-threaded server** 🌐  
✔ **SHA-256 integrity check** ✅  
✔ **Docker support** 🐳 (maybe) 

---

## 📦 Installation
### **Prerequisites**
- Python **3.8+**, pip
- **Docker & Docker Compose** (if using containers)

### **Install Dependencies**
```bash
pip install -r requirements.txt
```

---

## ▶️ Usage
### **CLI Mode**
```bash
python server/server.py   # Start server
python client/client.py   # Run client
```
### **GUI Mode**
```bash
python server/server_gui.py  # Start GUI server
python client/client_gui.py  # Start GUI client
```

---

## 🐳 Docker Deployment
```bash
docker-compose up --build   # Start

docker-compose down        # Stop
```

---

## ⚙ Configuration
Edit `config.py` (server & client):
```python
SERVER_IP = "0.0.0.0"
SERVER_PORT = 5001
ENCRYPTION_KEY = b"key..."
CHUNK_SIZE = 4096
SAVE_DIRECTORY = "./uploads"
```

---

## 🔐 Security Features
- **AES-256 Encryption**
- **SHA-256 File Integrity Check**
- **Random IV for encryption**
- **Error Handling & Logging**

---

## 🛠 Future Improvements
✅ **Resumable Transfers**
✅ **RSA Key Encryption**
✅ **Tkinter GUI Enhancements**

---

## 🤝 Contributing
Fork & submit a pull request! 🚀



