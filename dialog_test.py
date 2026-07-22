import customtkinter as ctk

app = ctk.CTk()
app.geometry("300x200")

button = ctk.CTkButton(
    app,
    text="TEST BUTTON",
    command=lambda: print("Button Clicked")
)

button.pack(pady=20)

app.mainloop()