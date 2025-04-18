from dkce_extension import DKCE
import customtkinter as ctk
from customtkinter import filedialog


class NotesApp:
    def __init__(self, parent):
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

        self.content_frame = ctk.CTkFrame(self.frame,
                                          fg_color="#2B2B2B")
        
        self.content_frame.pack(fill="both",
                                expand=True,
                                padx=15,
                                pady=15)

        self.text_frame = ctk.CTkFrame(self.content_frame,
                                       fg_color="#2B2B2B")
        
        self.text_frame.pack(side="left",
                             fill="both",
                             expand=True,
                             padx=15,
                             pady=15)

        self.text_area = ctk.CTkTextbox(self.text_frame,
                                        width=600,
                                        height=300)
        
        self.text_area.pack(fill="both", expand=True)

        self.proprieties_button = ctk.CTkButton(self.text_frame,
                                                text="Propriétés",
                                                command=self.toggle_proprieties_frame,
                                                hover_color="#5A5A5A",
                                                fg_color="#444444")
        
        self.proprieties_button.pack(anchor="ne", padx=5, pady=5)

        self.proprieties_Frame = ctk.CTkFrame(self.content_frame,
                                              fg_color="#303030",
                                              corner_radius=10,
                                              width=300)
        
        self.proprieties_Frame.pack(side="right",
                                    padx=15,
                                    pady=15,
                                    fill="y")

        ctk.CTkLabel(self.proprieties_Frame,
                     text="Police d'écriture :",
                     fg_color="#303030").pack(pady=10, padx=10)

        self.font_choice = ctk.CTkComboBox(self.proprieties_Frame,
                                           values=["Arial", "Courier New", "Comic Sans MS", "Times New Roman", "Verdana"],
                                           command=self.change_font)
        
        self.font_choice.pack(pady=10, padx=10)

        save_button = ctk.CTkButton(self.frame,
                                    text="Sauvegarder",
                                    command=self.save_notes,
                                    hover_color="#5A5A5A",
                                    fg_color="#444444")
        
        save_button.pack(side="left", padx=10, pady=10)

        load_button = ctk.CTkButton(self.frame,
                                    text="Charger",
                                    command=self.load_notes,
                                    hover_color="#5A5A5A",
                                    fg_color="#444444")
        
        load_button.pack(side="left", padx=10, pady=10)

        self.is_proprieties_visible = True

    def toggle_proprieties_frame(self):
        """
        Affiche ou masque la frame des propriétés.
        """
        if self.is_proprieties_visible:
            self.proprieties_Frame.pack_forget()
        else:
            self.proprieties_Frame.pack(side="right",
                                        padx=15,
                                        pady=15,
                                        fill="y")
            
        self.is_proprieties_visible = not self.is_proprieties_visible

    def change_font(self, font_name):
        """
        Change la police d'écriture de la zone de texte.
        """
        self.text_area.configure(font=(font_name, 12))

    def save_notes(self):
        """
        Sauvegarde le contenu dans un fichier .dkceTXT avec la police cachée.
        """
        file_path = filedialog.asksaveasfilename(defaultextension=".dkceTXT",
                                        filetypes=[("DeskCore Text Files", "*.dkceTXT")])

        if file_path:
            # Récupérer le texte et la police
            text_content = self.text_area.get("1.0", "end-1c")
            current_font = self.font_choice.get()
            
            # Créer une ligne spéciale pour la police au début du fichier
            # Format: ##DKCE_FONT:NomDeLaPolice##
            font_marker = f"##DKCE_FONT:{current_font}##\n"
            
            # Combiner le marqueur et le contenu
            full_content = font_marker + text_content
            
            # Sauvegarder le contenu complet
            DKCE.save_dkceTXT(file_path, full_content)

    def load_notes(self):
        """
        Charge un fichier .dkceTXT et extrait la police si disponible.
        """
        file_path = filedialog.askopenfilename(filetypes=[("DeskCore Text Files", "*.dkceTXT")])

        if file_path:
            content = DKCE.load_dkceTXT(file_path)
            if content is not None:
                # Chercher le marqueur de police
                import re
                font_match = re.match(r"##DKCE_FONT:([^#]+)##\n(.*)", content, re.DOTALL)
                
                if font_match:
                    # Extraire la police et le contenu réel
                    font = font_match.group(1)
                    text = font_match.group(2)
                    
                    # Mettre à jour le texte sans le marqueur de police
                    self.text_area.delete("1.0", "end")
                    self.text_area.insert("1.0", text)
                    
                    # Mettre à jour la police si elle est valide
                    if font in ["Arial", "Courier New", "Comic Sans MS", "Times New Roman", "Verdana"]:
                        self.font_choice.set(font)
                        self.change_font(font)
                else:
                    # Pas de marqueur trouvé, charger tout le contenu tel quel
                    self.text_area.delete("1.0", "end")
                    self.text_area.insert("1.0", content)
