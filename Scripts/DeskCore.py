import customtkinter as ctk

class DeskCoreApp:
    """
    Classe principale pour l'application DeskCore. 
    Permet de gérer une interface avec des zones dynamiques, un menu, et d'autres fonctionnalités.
    """

    def __init__(self):
        """
        Initialise l'application DeskCore et les variables de base.
        """
        self.app = ctk.CTk()
        self.app.title("DeskCore")
        self.app.geometry("1000x600")
        self.frames = []
        self.frame_states = {}
        self.initialisation()

    def initialisation(self):
        """
        Initialise les éléments de l'interface graphique y compris le menu, 
        les zones dynamiques et la barre de scroll horizontale.
        """
        self.menu = ctk.CTkFrame(self.app, width=200)
        self.menu.pack(side="left", fill="both", padx=10, pady=10)
        
        self.create_button = ctk.CTkButton(self.menu, width=70, height=70, text="+Zone", corner_radius=15, command=self.creation_zone)
        self.create_button.pack(padx=10, pady=10)

        self.delete_button = ctk.CTkButton(self.menu, width=70, height=70, text="-Zone", corner_radius=15, command=self.suppression_zone)
        self.delete_button.pack(padx=10, pady=10)

        self.Notes_app = ctk.CTkButton(self.menu, width=70, height=70, text="Notes", corner_radius=15, command=self.ouvrir_notes)
        self.Notes_app.pack(padx=10, pady=10)
  
        self.container_frame = ctk.CTkFrame(self.app)
        self.container_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)

        self.canvas = ctk.CTkCanvas(self.container_frame, highlightthickness=0)
        self.scrollbar = ctk.CTkScrollbar(self.container_frame, orientation="horizontal", command=self.canvas.xview)
        self.canvas.configure(xscrollcommand=self.scrollbar.set)

        self.canvas.pack(side="top", fill="both", expand=True)
        self.scrollbar.pack(side="bottom", fill="x")

        self.new_frame = ctk.CTkFrame(self.canvas, width=0)
        self.canvas.create_window((0, 0), window=self.new_frame, anchor="nw")

        self.new_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        # Cela permet de crée un slider pour defiler les Zones/Frames

        self.frame_count = 0

    def creation_zone(self):
        """
        Crée une nouvelle zone dynamique avec un scrool de largeur ajustable.
        Affiche un message d'erreur si le nombre maximum de zones est atteint.
        """
        if self.frame_count < 5:
            self.frame_count += 1

            new_frame = ctk.CTkFrame(self.new_frame, corner_radius=10, width=100, height=800)
            new_frame.pack(side="left", padx=10, pady=10)
            new_frame.pack_propagate(False)

            slider = ctk.CTkSlider(master=new_frame, from_=100, to=600, command=lambda value, frame=new_frame: self.adjust_frame_width(value, frame))
            slider.pack(padx=5, pady=5, anchor="nw")

            self.frames.append(new_frame)
            self.frame_states[new_frame] = None
        else:
            self.pop_up("Nombre de zones maximum atteint !")

    def suppression_zone(self):
        """
        Supprime la dernière zone créée.
        Affiche un message d'erreur si aucune zone n'existe.
        """
        if self.frames:
            frame_to_remove = self.frames.pop()
            self.frame_states.pop(frame_to_remove, None)
            frame_to_remove.destroy()
            self.frame_count -= 1
        else:
            self.pop_up("Aucune zone à supprimer !")

    def adjust_frame_width(self, value:int, frame:int):
        """
        Ajuste la largeur d'une frame en fonction de la valeur du scroll.
        """
        new_width = int(value)
        frame.configure(width=new_width)

    def pop_up(self, message:str):
        """
        Affiche une fenêtre avec un message.
        """
        popup = ctk.CTkToplevel(self.app)
        popup.title("Erreur")
        popup.geometry("300x150")
        popup.resizable(False, False)
        popup.grab_set()
        
        label = ctk.CTkLabel(popup, text=message, justify="center")
        label.pack(padx=20, pady=20)

        ok_button = ctk.CTkButton(popup, text="OK", command=popup.destroy)
        ok_button.pack(pady=10)
        popup.focus()

        # Pour l'instant ça deconne sur Linux et non sur Windows
        # problème : grab_set() et focus() qui se casse sur Linux

    def ouvrir_notes(self):
        """
        Ouvre l'application notes dans une zone libre. 
        Affiche un message d'erreur si aucune zone libre n'est disponible.
        """
        for frame, app in self.frame_states.items():
            if app is None:
                from Notes_app import NotesApp
                NotesApp(frame)
                self.frame_states[frame] = "Notes"
                return
        self.pop_up("Aucune frame disponible pour ouvrir Notes !")

    def run(self):
        """
        Lance la boucle principale de l'application pour démarrer DeskCore.
        """
        self.app.mainloop()


ctk.set_appearance_mode("light") 
ctk.set_default_color_theme("dark-blue")

# les deux lignes du dessus sont là pour mettre le thème en attendant que Houssemand fasse la fonction

app = DeskCoreApp()
app.run()
