import customtkinter as ctk

class Launcher:
    def __init__(self):
        self.app = ctk.CTk()
        self.app.title("DeskCore Launcher")
        self.app.geometry("600x300")
        self.initialisation()

    def initialisation(self):
        self.menu_a = ctk.CTkFrame(self.app, width=250)
        self.menu_a.pack(side="left", fill="both", padx=20, pady=20)

        self.menu_b = ctk.CTkFrame(self.app, width=400)
        self.menu_b.pack(side="right", fill="both", padx=20, pady=20)

        self.linux_button = ctk.CTkButton(self.menu_a, width=150, height=90, text="Launch Linux", corner_radius=20)
        self.linux_button.pack(side="top", padx=10, pady=10)

        self.windows_button = ctk.CTkButton(self.menu_a, width=150, height=90, text="Launch Windows", corner_radius=20)
        self.windows_button.pack(side="bottom", padx=10, pady=10)

    def LW(self):
        pass

    def LL(self):
        pass

    def run(self):
        self.app.mainloop()

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("dark-blue")
app = Launcher()
app.run()
