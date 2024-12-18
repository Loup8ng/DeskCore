import customtkinter as ctk

ctk.set_appearance_mode("Dark")
a = 1
app = ctk.CTk()
app.title("DeskCore")
app.geometry("800x600")

frame_1 = ctk.CTkFrame(app, width=200)
frame_1.pack(side="left", fill="y", padx=10, pady=10)

frame_2 = ctk.CTkFrame(app)
frame_2.pack(side="right", fill="both", expand=True, padx=10, pady=10)

app.mainloop()
