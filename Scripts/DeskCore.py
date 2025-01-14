import customtkinter as ctk

class DeskCoreApp:
    def __init__(self):
        self.app = ctk.CTk()
        self.app.title("DeskCore")
        self.app.geometry("1000x600")
        self.current_theme = "light"
        self.frames = []
        self.frame_states = {}
        self.initialisation()

    def initialisation(self):
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

        self.frame_count = 0

    def creation_zone(self):
        if self.frame_count < 5:
            self.frame_count += 1

            new_frame = ctk.CTkFrame(self.new_frame, corner_radius=10, width=100, height=800)
            new_frame.pack(side="left", padx=10, pady=10)
            new_frame.pack_propagate(False)

            slider = ctk.CTkSlider(
                master=new_frame, 
                from_=100, 
                to=600, 
                command=lambda value, frame=new_frame: self.adjust_frame_width(value, frame)
            )
            slider.pack(padx=5, pady=5, anchor="nw")

            self.frames.append(new_frame)
            self.frame_states[new_frame] = None
        else:
            self.pop_up("Nombre de zones maximum atteint !")

    def suppression_zone(self):
        if self.frames:
            frame_to_remove = self.frames.pop()
            self.frame_states.pop(frame_to_remove, None)
            frame_to_remove.destroy()
            self.frame_count -= 1
        else:
            self.pop_up("Aucune zone à supprimer !")

    def adjust_frame_width(self, value, frame):
        new_width = int(value)
        frame.configure(width=new_width)

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
        popup.focus()

    def ouvrir_notes(self):
        for frame, app in self.frame_states.items():
            if app is None:
                from Notes_app import NotesApp
                NotesApp(frame)
                self.frame_states[frame] = "Notes"
                return
        self.pop_up("Aucune frame disponible pour ouvrir Notes !")

    def run(self):
        self.app.mainloop()

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("dark-blue")
app = DeskCoreApp()
app.run()
