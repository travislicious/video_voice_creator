import threading
from traceback import print_tb
import requests
import tkinter as tk
from tkinter import messagebox

def fetch_data():
    user_list.delete(0, tk.END)
    try:
        print("Fetching data...")
        response = requests.get('https://jsonplaceholder.typicode.com/users')
        data = response.json()
        root.after(0, update_gui, data)
    except Exception as e:
        root.after(0, lambda: messagebox.showerror("Error", str(e)))
    finally:
        print("Data fetched.")

def start_fetching():
    threading.Thread(target=fetch_data).start()

def update_gui(data):
    user_list.delete(0, tk.END)
    for user in data:
        user_list.insert(tk.END, f"{user['name']} ({user['email']})")

root = tk.Tk()
root.title("User List")

fetch_button = tk.Button(root, text="Fetch Users", command=start_fetching)
fetch_button.pack(pady=20)

user_list = tk.Listbox(root, width=50, height=10)
user_list.pack(pady=20)

root.mainloop()
