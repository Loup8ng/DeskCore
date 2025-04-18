import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class Calculatrice(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Calculatrice")
        self.geometry("300x400")
        self.resizable(False, False)

        # Frame principale
        self.main_frame = ctk.CTkFrame(self, fg_color="#2B2B2B")
        self.main_frame.pack(expand=True, fill="both", padx=10, pady=10)

        # Zone de saisie
        self.entry = ctk.CTkTextbox(self.main_frame, height=60, font=("Arial", 18))
        self.entry.pack(fill="x", padx=10, pady=(10, 5))
        self.entry.insert("end", "")  # zone vide au début
        self.entry.configure(state="normal")

        # Frame des boutons
        self.buttons_frame = ctk.CTkFrame(self.main_frame, fg_color="#1F1F1F")
        self.buttons_frame.pack(expand=True, fill="both", padx=10, pady=(5, 10))

        # Disposition des boutons
        self.create_buttons()

    def create_buttons(self):
        # Grille des boutons
        boutons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["0", ".", "=", "+"]
        ]

        for row_index, row in enumerate(boutons):
            for col_index, symbol in enumerate(row):
                bouton = ctk.CTkButton(self.buttons_frame, text=symbol,
                                       command=lambda s=symbol: self.bouton_click(s),
                                       width=60, height=50, font=("Arial", 16))
                bouton.grid(row=row_index, column=col_index, padx=5, pady=5, sticky="nsew")

        # Rendre la grille responsive
        for i in range(4):
            self.buttons_frame.grid_columnconfigure(i, weight=1)
        for i in range(4):
            self.buttons_frame.grid_rowconfigure(i, weight=1)

    def bouton_click(self, symbole):
        if symbole == "=":
            self.calculer()
        else:
            self.entry.insert("end", symbole)

    def calculer(self):
        expression = self.entry.get("0.0", "end").strip()
        try:
            résultat = eval(expression)
            self.entry.delete("0.0", "end")
            self.entry.insert("end", str(résultat))
        except:
            self.entry.delete("0.0", "end")
            self.entry.insert("end", "Erreur")

if __name__ == "__main__":
    app = Calculatrice()
    app.mainloop()
