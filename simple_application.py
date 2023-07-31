import tkinter as tk
from tkinter import messagebox

class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def display_info(self):
        info = f"Name: {self.name}\nPhone: {self.phone}\nEmail: {self.email}"
        return info

def display_contact_info():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    contact = Contact(name, phone, email)
    info = contact.display_info()
    messagebox.showinfo("Contact Information", info)

# Creating a GUI window
window = tk.Tk()
window.title("Address Book")

# Creating labels and entry fields
name_label = tk.Label(window, text="Name:")
name_label.pack()
name_entry = tk.Entry(window)
name_entry.pack()

phone_label = tk.Label(window, text="Phone:")
phone_label.pack()
phone_entry = tk.Entry(window)
phone_entry.pack()

email_label = tk.Label(window, text="Email:")
email_label.pack()
email_entry = tk.Entry(window)
email_entry.pack()

# Creating a button to display contact info
display_button = tk.Button(window, text="Display Info", command=display_contact_info)
display_button.pack()

# Starting the GUI event loop
window.mainloop()
