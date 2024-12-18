import customtkinter as ctk
# j'utilise principalement la doc https://customtkinter.tomschimansky.com/documentation/ pour le code.

class DeskCoreApp:
    def __init__(self):
        self.app = ctk.CTk()
        self.app.title("DeskCore")
        self.app.geometry("1400x800")
        self.app.iconbitmap("Ressources\images\iconDC.ico")
        self.initialisation()

    def initialisation(self):
        self.menu = ctk.CTkFrame(self.app, width=200)
        self.menu.pack(side="left", fill="both", padx=10, pady=10)
        
        self.create_button = ctk.CTkButton(self.menu, width=70, height=70, text="+Zone", corner_radius=15, command=self.creation_zone)
        self.create_button.pack(padx=10, pady=10)

        self.delete_button = ctk.CTkButton(self.menu, width=70, height=70, text="-Zone", corner_radius=15, command=self.suppression_zone)
        self.delete_button.pack(padx=10, pady=10)
        
        self.new_frame = ctk.CTkFrame(self.app)
        self.new_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)
        self.frames = []
        self.frame_count = 0

    def creation_zone(self):
        if self.frame_count < 5:
            self.frame_count += 1
            new_frame = ctk.CTkFrame(self.new_frame, corner_radius=10)
            new_frame.pack(side="left", fill="both", padx=10, pady=10)
            self.frames.append(new_frame)
        else:
            self.pop_up("Nombre de zones maximum atteint !")

    def suppression_zone(self):
        if self.frames:
            frame_to_remove = self.frames.pop()
            frame_to_remove.destroy()
            self.frame_count -= 1
        else:
            self.pop_up("Aucune zone à supprimer !")

    def pop_up(self, message):
        popup = ctk.CTkToplevel(self.app)
        popup.title("Erreur")
        popup.geometry("300x150")
        popup.resizable(False, False)
        popup.grab_set()
        
        label = ctk.CTkLabel(popup, text=message, justify="center")
        label.pack(padx=20, pady=20)

        ok_button = ctk.CTkButton(popup, text="OK", command=popup.destroy)
        ok_button.pack(pady=10)
        popup.focus_force()

    def run(self):
        self.app.mainloop()


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")
app = DeskCoreApp()
app.run()
