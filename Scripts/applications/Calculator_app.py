import customtkinter as ctk
from customtkinter import filedialog

class Calculatrice:
    def __init__(self, parent):
        """
        Initialise l'application Calculatrice dans la zone principale.
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

        # Zone de texte pour afficher le résultat
        self.text_frame = ctk.CTkFrame(self.content_frame,
                                       fg_color="#2B2B2B")
        
        self.text_frame.pack(side="top",
                             fill="both",
                             expand=True,
                             padx=15,
                             pady=15)

        self.text_area = ctk.CTkTextbox(self.text_frame,
                                        width=600,
                                        height=100)
        
        self.text_area.pack(fill="both", expand=True)

        # Frame pour les propriétés (si on souhaite ajouter plus tard)
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

        # Zone des boutons pour la calculatrice (en bas)
        self.buttons_frame = ctk.CTkFrame(self.frame,
                                          fg_color="#2B2B2B")
        
        self.buttons_frame.pack(side="bottom",
                                fill="x",
                                padx=15,
                                pady=10)

        # Ajouter des boutons de calcul
        self.create_calculator_buttons()

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

    def create_calculator_buttons(self):
        """
        Crée les boutons de la calculatrice et les ajoute au layout.
        """
        buttons = [
            ('7', self.append_digit), ('8', self.append_digit), ('9', self.append_digit), ('/', self.append_operator),
            ('4', self.append_digit), ('5', self.append_digit), ('6', self.append_digit), ('*', self.append_operator),
            ('1', self.append_digit), ('2', self.append_digit), ('3', self.append_digit), ('-', self.append_operator),
            ('0', self.append_digit), ('.', self.append_digit), ('=', self.calculate_result), ('+', self.append_operator)
        ]

        for (text, command) in buttons:
            button = ctk.CTkButton(self.buttons_frame,
                                   text=text,
                                   command=lambda t=text: command(t),
                                   hover_color="#5A5A5A",
                                   fg_color="#444444")
            button.pack(side="left", padx=5, pady=5)

    def append_digit(self, digit):
        """
        Ajoute un chiffre ou un point à la zone de texte de la calculatrice.
        """
        current_text = self.text_area.get("1.0", "end-1c")
        self.text_area.delete("1.0", "end")
        self.text_area.insert("1.0", current_text + digit)

    def append_operator(self, operator):
        """
        Ajoute un opérateur à la zone de texte.
        """
        current_text = self.text_area.get("1.0", "end-1c")
        if current_text and current_text[-1] not in "+-*/":
            self.text_area.delete("1.0", "end")
            self.text_area.insert("1.0", current_text + operator)

    def calculate_result(self, _):
        """
        Calcule et affiche le résultat.
        """
        current_text = self.text_area.get("1.0", "end-1c")
        try:
            result = str(eval(current_text))  # Utilise eval pour évaluer l'expression
            self.text_area.delete("1.0", "end")
            self.text_area.insert("1.0", result)
        except Exception as e:
            self.text_area.delete("1.0", "end")
            self.text_area.insert("1.0", "Erreur")

