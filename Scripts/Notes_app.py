import customtkinter as ctk

class NotesApp:
    def __init__(self, parent:str):
        """
        initialise l'applications Notes
        """
        self.text_area = ctk.CTkTextbox(parent, width=100, height=800)
        self.text_area.pack(fill="both", expand=True, padx=5, pady=5)