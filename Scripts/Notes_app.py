import customtkinter as ctk


class NotesApp:
    """
    Application Notes pour DeskCore.
    """
    def __init__(self, master_zone:str):
        """
        Initialise l'application Notes dans la main_zone.
        """
        self.master_zone = master_zone
        self.notes_frame = None
        self.text_area = None

        self.setup()

    def setup(self):
        """
        Configure l'appli Notes.
        """
        
        for widget in self.master_zone.winfo_children():
            widget.destroy()

        self.notes_frame = ctk.CTkFrame(self.master_zone,
                                        fg_color="#333333",
                                        corner_radius=10)
        
        self.notes_frame.pack(fill="both",
                              expand=True,
                              padx=15,
                              pady=10)
        
        self.text_area = ctk.CTkTextbox(self.notes_frame,
                                        width=800,
                                        height=500,
                                        corner_radius=10,
                                        fg_color="#444444",
                                        text_color="white",
                                        font=("Arial", 14))
        
        self.text_area.pack(fill="both",
                            expand=True,
                            padx=15,
                            pady=15)

