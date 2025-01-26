from dkce_extension import DKCE
import customtkinter as ctk
from customtkinter import filedialog

class NotesApp:
    def __init__(self, parent:str):
        """
        Initialise l'application Notes dans la zone principale.
        """
        self.frame = ctk.CTkFrame(parent,
                                  fg_color="#2B2B2B",
                                  corner_radius=10)
        
        self.frame.pack(fill="both",
                        expand=True,
                        padx=15,
                        pady=10)

        self.text_area = ctk.CTkTextbox(self.frame,
                                        width=800,
                                        height=400)
        
        self.text_area.pack(padx=15,
                            pady=15,
                            expand=True)

        save_button = ctk.CTkButton(self.frame,
                                    text="Sauvegarder",
                                    command=self.save_notes,
                                    hover_color="#5A5A5A",
                                    fg_color="#444444")
        
        save_button.pack(side="left",
                         padx=10,
                         pady=10)

        load_button = ctk.CTkButton(self.frame,
                                    text="Charger",
                                    command=self.load_notes,
                                    hover_color="#5A5A5A",
                                    fg_color="#444444")
        
        load_button.pack(side="left",
                         padx=10,
                         pady=10)

    def save_notes(self):
        """
        Sauvegarde le contenu dans un fichier .dkceTXT.
        """
        file_path = filedialog.asksaveasfilename(defaultextension=".dkceTXT",
                                      filetypes=[("DeskCore Text Files", "*.dkceTXT")])
        
        if file_path:
            DKCE.save_dkceTXT(file_path, self.text_area.get("1.0", "end-1c")) #end-1c en gros ca fait comme "end" mais ca s'arrete avant d eretourner à la ligne (c'est mieux pour recuperer un texte)

    def load_notes(self):
        """
        Charge un fichier .dkceTXT.
        """
        file_path = filedialog.askopenfilename(filetypes=[("DeskCore Text Files", "*.dkceTXT")])
        
        if file_path:
            text = DKCE.load_dkceTXT(file_path)
            if text is not None:
                self.text_area.delete("1.0", "end")
                
                self.text_area.insert("1.0", text)
