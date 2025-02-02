import tkinter as tk
import threading
import server
import config

# Function to start the server in a separate thread
def start_server():
    threading.Thread(target=server.start_server, args=(config.SERVER_IP, config.SERVER_PORT), daemon=True).start()
    status_label.config(text="Server is Running...", fg="green")

# Create GUI window
root = tk.Tk()
root.title("File Transfer - Server")
root.geometry("300x150")

# UI Elements
status_label = tk.Label(root, text="Server not started", font=("Arial", 12), fg="red")
status_label.pack(pady=10)
tk.Button(root, text="Start Server", command=start_server, bg="blue", fg="white").pack(pady=10)

root.mainloop()
