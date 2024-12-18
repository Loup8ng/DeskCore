import customtkinter as ctk

ctk.set_appearance_mode("Dark")
a = 1
app = ctk.CTk()
app.title("DeskCore")
app.geometry("800x600")import customtkinter as ctk

app = ctk.CTk()
app.title("DeskCore")
app.geometry("800x600")

class Workspace:
    def __init__(self, app):
        self.app = app
        self.frame_count = 0

    def creation_frame(self):
        self.frame_count += 1 
        frame = ctk.CTkFrame(self.app)
        frame.pack(side="top", fill="both",padx=10, pady=10)

ctk.set_appearance_mode("light")

deskcore = workspace(app)

frame_1 = ctk.CTkFrame(app, width=100)
frame_1.pack(side="left", fill="y", padx=10, pady=10)

button_create = ctk.CTkButton(frame_1, text="Créer une Frame", command=deskcore.create_frame)
button_create.pack(padx=10, pady=10)


app.mainloop()


frame_1 = ctk.CTkFrame(app, width=200)
frame_1.pack(side="left", fill="y", padx=10, pady=10)

frame_2 = ctk.CTkFrame(app)
frame_2.pack(side="right", fill="both", expand=True, padx=10, pady=10)

app.mainloop()
