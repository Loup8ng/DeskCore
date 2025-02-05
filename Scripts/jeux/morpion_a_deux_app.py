import customtkinter as ctk
import random

class MorpionApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Morpion")
        self.geometry("400x500")
        
        self.current_player = "X"
        self.board = [[None for _ in range(3)] for _ in range(3)]
        
        self.label = ctk.CTkLabel(self, text=f"Tour du joueur {self.current_player}")
        self.label.pack(pady=10)
        
        self.frame = ctk.CTkFrame(self)
        self.frame.pack()
        
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = ctk.CTkButton(self.frame, text="", width=100, height=100, command=lambda row=i, col=j: self.play(row, col))
                self.buttons[i][j].grid(row=i, column=j, padx=5, pady=5)
        
        self.reset_button = ctk.CTkButton(self, text="Recommencer", command=self.reset_game)
        self.reset_button.pack(pady=10)
    
    def play(self, row, col):
        if self.board[row][col] is None:
            self.board[row][col] = self.current_player
            self.buttons[row][col].configure(text=self.current_player)
            
            if self.check_win(self.current_player):
                self.label.configure(text=f"Le joueur {self.current_player} gagne !")
                self.disable_buttons()
                return
            
            if self.is_draw():
                self.label.configure(text="Match nul !")
                return
            
            self.current_player = "O" if self.current_player == "X" else "X"
            self.label.configure(text=f"Tour du joueur {self.current_player}")
    
    def check_win(self, player):
        for row in self.board:
            if all(cell == player for cell in row):
                return True
        for col in range(3):
            if all(self.board[row][col] == player for row in range(3)):
                return True
        if all(self.board[i][i] == player for i in range(3)) or all(self.board[i][2 - i] == player for i in range(3)):
            return True
        return False
    
    def is_draw(self):
        return all(all(cell is not None for cell in row) for row in self.board)
    
    def disable_buttons(self):
        for row in self.buttons:
            for button in row:
                button.configure(state="disabled")
    
    def reset_game(self):
        self.current_player = "X"
        self.board = [[None for _ in range(3)] for _ in range(3)]
        self.label.configure(text=f"Tour du joueur {self.current_player}")
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].configure(text="", state="normal")

if __name__ == "__main__":
    app = Morpion()
    app.mainloop()
