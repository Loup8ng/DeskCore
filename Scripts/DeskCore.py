import customtkinter as ctk
from Notes_app import NotesApp


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
                                             text="Paramètre",
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


        self.show_settings()

    def clear_main_zone(self):
        """
        Supprime tous les widgets de la Main Zone. ( Main Zone c'est le nom de la grande Frame qui contient les applications et les paramètres)
        """
        for widget in self.main_zone.winfo_children():
            widget.destroy()
        
        self.settings_frame = None

    def toggle_apps_menu(self):
        """
        Affiche ou cache le menu des applications sous le menu.
        """
        if self.apps_menu:
            self.apps_menu.destroy()
            self.apps_menu = None
        else:
            self.apps_menu = ctk.CTkFrame(self.app,
                                          height=80,
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
                
                app_button.pack(side="left",
                                padx=15,
                                pady=10)

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
        
        options = ["Désactiver la sauvegarde auto"]
        
        for option in options:
            checkbox = ctk.CTkCheckBox(self.settings_frame,
                                        text=option,
                                        command=self.action)
            
            checkbox.pack(anchor="w",
                          padx=15,
                          pady=10)

    def action(self):
        pass

    def open_Notes_app(self):
        """
        Ouvre l'application Notes_app.
        """
        NotesApp(self.main_zone)

    def run(self):
        """
        Lance la boucle.
        """
        self.app.mainloop()

app = DeskCoreApp()
app.run()
