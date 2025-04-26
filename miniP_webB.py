import tkinter as tk
from tkinter import messagebox

hosts_path = r"C:\Windows\System32\drivers\etc\hosts"  # Modify for Linux/Mac
redirect = "127.0.0.1"
website_list = ["www.facebook.com", "facebook.com", "www.youtube.com", "youtube.com", "instagram.com", "www.instagram.com"]

def block_websites():
    with open(hosts_path, 'r+') as file:
        content = file.read()
        for website in website_list:
            if website not in content:
                file.write(f"{redirect} {website}\n")
    messagebox.showinfo("Website Blocker", "Websites are blocked!")

def unblock_websites():
    with open(hosts_path, 'r+') as file:
        content = file.readlines()
        file.seek(0)
        for line in content:
            if not any(website in line for website in website_list):
                file.write(line)
        file.truncate()
    messagebox.showinfo("Website Blocker", "Websites are unblocked!")

# Create the GUI
window = tk.Tk()
window.title("Website Blocker")
window.geometry("300x200")

label = tk.Label(window, text="Website Blocker", font=("Arial", 14))
label.pack(pady=20)

block_button = tk.Button(window, text="Block Websites", command=block_websites, width=20)
block_button.pack(pady=10)

unblock_button = tk.Button(window, text="Unblock Websites", command=unblock_websites, width=20)
unblock_button.pack(pady=10)

window.mainloop()
