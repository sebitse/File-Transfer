import tkinter as tk
from tkinter import filedialog, messagebox
import threading
import client
import config

# Function to handle file selection
def select_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        file_entry.delete(0, tk.END)
        file_entry.insert(0, file_path)

# Function to send file when button is clicked
def send_file():
    file_path = file_entry.get()
    if not file_path:
        messagebox.showerror("Error", "Please select a file first!")
        return

    # Run the sending function in a separate thread
    threading.Thread(target=client.send_file, args=(file_path, config.SERVER_IP, config.SERVER_PORT), daemon=True).start()
    messagebox.showinfo("Success", f"File '{file_path}' is being sent!")

# Create GUI window
root = tk.Tk()
root.title("File Transfer - Client")
root.geometry("400x200")

# Create UI elements
tk.Label(root, text="Select a file to send:", font=("Arial", 12)).pack(pady=5)
file_entry = tk.Entry(root, width=40)
file_entry.pack(pady=5)
tk.Button(root, text="Browse", command=select_file).pack(pady=5)
tk.Button(root, text="Send File", command=send_file, bg="green", fg="white").pack(pady=10)

root.mainloop()
