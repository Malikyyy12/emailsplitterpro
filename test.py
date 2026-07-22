import customtkinter as ctk

ctk.set_appearance_mode("dark")

app = ctk.CTk()
app.geometry("300x200")
app.title("Test")

label = ctk.CTkLabel(app, text="Hello World")
label.pack(pady=40)

app.mainloop()