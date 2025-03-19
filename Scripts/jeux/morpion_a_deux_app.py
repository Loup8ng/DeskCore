import customtkinter as ctk

class MorpionApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Morpion à deux")
        self.geometry("400x500")
        self.resizable(True, True)
        
        self.joueur = "X"
        self.grille = [[None for _ in range(3)] for _ in range(3)]
        
        self.label = ctk.CTkLabel(self, text=f"Tour du joueur {self.joueur}")
        self.label.pack(pady=10)
        
        self.cadre = ctk.CTkFrame(self)
        self.cadre.pack()
        
        self.boutons = [[None for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.boutons[i][j] = ctk.CTkButton(
                    self.cadre, text="", width=100, height=100,
                    command=lambda lig=i, col=j: self.jouer(lig, col)
                )
                self.boutons[i][j].grid(row=i, column=j, padx=5, pady=5)
        
        self.bouton_reset = ctk.CTkButton(self, text="Recommencer", command=self.reinitialiser)
        self.bouton_reset.pack(pady=10)

    def jouer(self, lig, col):
        if self.grille[lig][col] is None:
            self.grille[lig][col] = self.joueur
            self.boutons[lig][col].configure(text=self.joueur)

            if self.victoire(self.joueur):
                self.label.configure(text=f"Le joueur {self.joueur} gagne !")
                self.desactiver_boutons()
                return
            if self.match_nul():
                self.label.configure(text="Match nul !")
                return

            self.joueur = "O" if self.joueur == "X" else "X"
            self.label.configure(text=f"Tour du joueur {self.joueur}")

    def victoire(self, joueur):
        for ligne in self.grille:
            if all(cell == joueur for cell in ligne):
                return True
        for col in range(3):
            if all(self.grille[lig][col] == joueur for lig in range(3)):
                return True
        if all(self.grille[i][i] == joueur for i in range(3)) or all(self.grille[i][2 - i] == joueur for i in range(3)):
            return True
        return False

    def match_nul(self):
        return all(all(cell is not None for cell in ligne) for ligne in self.grille)

    def desactiver_boutons(self):
        for ligne in self.boutons:
            for bouton in ligne:
                bouton.configure(state="disabled")

    def reinitialiser(self):
        self.joueur = "X"
        self.grille = [[None for _ in range(3)] for _ in range(3)]
        self.label.configure(text=f"Tour du joueur {self.joueur}")
        for i in range(3):
            for j in range(3):
                self.boutons[i][j].configure(text="", state="normal")

if __name__ == "__main__":
    app = MorpionApp()
    app.mainloop()