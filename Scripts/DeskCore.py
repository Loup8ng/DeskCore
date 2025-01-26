import customtkinter as ctk

class DeskCoreApp:
    """
    Class principale pour DeskCore.
    """
    def __init__(self):
        """
        Initialise DeskCore.
        """
        self.app = ctk.CTk()
        self.app.title("DeskCore")
        self.app.geometry("1200x800")
        self.app.resizable(False, False)

        self.menu_bar = ctk.CTkFrame(self.app,
                                     height=100,
                                     corner_radius=5,
                                     fg_color="#2B2B2B")
        
        self.menu_bar.pack(side="top",
                           pady=10,
                           padx=15,
                           fill="x")
        
        self.app_button = ctk.CTkButton(self.menu_bar,
                                        text="Applications",
                                        corner_radius=10,
                                        width=100,
                                        height=30,
                                        command=self.toggle_apps_menu,
                                        hover_color="#5A5A5A",
                                        fg_color="#444444")
        
        self.app_button.pack(side="left",
                             padx=15,
                             pady=5)
        
        self.settings_button = ctk.CTkButton(self.menu_bar,
                                             text="Paramètres",
                                             corner_radius=10,
                                             width=100,
                                             height=30,
                                             command=self.show_settings,
                                             hover_color="#5A5A5A",
                                             fg_color="#444444")
        
        self.settings_button.pack(side="left",
                                  padx=15,
                                  pady=5)
        

        self.main_zone = ctk.CTkFrame(self.app,
                                      fg_color="#2B2B2B")
        
        self.main_zone.pack(fill="both",
                            side="bottom",
                            expand=True,
                            padx=15,
                            pady=10)
        

        self.apps_menu = None
        self.settings_frame = None

    def clear_main_zone(self):
        """
        Supprime tous les widgets de la zone principale.
        """
        for widget in self.main_zone.winfo_children():
            widget.destroy()


    def toggle_apps_menu(self):
        """
        Affiche ou cache le menu des applications sous le menu principal.
        """
        if self.apps_menu:
            self.apps_menu.destroy()
            self.apps_menu = None
        else:
            self.apps_menu = ctk.CTkFrame(self.app,
                                        height=100,
                                        fg_color="#333333",
                                        corner_radius=10)
            self.apps_menu.pack(side="top",
                                fill="x",
                                pady=10,
                                padx=15)

            apps = [("Notes_app", self.open_Notes_app),
                    ("Calculatrice", self.action),
                    ("Musique", self.action),
                    ("...", self.action),
                    ("...", self.action)]

            for app_name, command in apps:
                app_button = ctk.CTkButton(self.apps_menu,
                                        text=app_name,
                                        corner_radius=10,
                                        width=120,
                                        height=50,
                                        hover_color="#5A5A5A",
                                        fg_color="#444444",
                                        command=command)
                app_button.pack(side="left", padx=15, pady=10)


    def show_settings(self):
        """
        Affiche les paramètres dans la Main Zone.
        """
        self.clear_main_zone()
        
        self.settings_frame = ctk.CTkFrame(self.main_zone,
                                           fg_color="#333333",
                                           corner_radius=10)
        
        self.settings_frame.pack(fill="both",
                                 expand=True,
                                 padx=15,
                                 pady=10)
        
        options = ["reglage 1",
                   "reglage 2",
                   "reglage 3",
                   "reglage 4,"]
        
        for option in options:
            switch = ctk.CTkSwitch(self.settings_frame,
                                   text=option,
                                   command=self.action)
            
            switch.pack(anchor="w",
                        padx=15,
                        pady=10)

    def action(self):
        """
        histoire de dire que ya quelque chose.
        """
        pass

    def open_Notes_app(self):
        """
        Ouvre l'application Notes.
        """
        from Notes_app import NotesApp
        
        self.clear_main_zone()
        NotesApp(self.main_zone)


    def run(self):
        """
        Lance la boucle principale.
        """
        self.app.mainloop()


app = DeskCoreApp()
app.run()
