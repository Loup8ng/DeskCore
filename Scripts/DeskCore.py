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
        self.app.resizable(True, True)
        self.enroute = False

        self.font = "white"        
        self.menu_bar = ctk.CTkFrame(self.app,
                                     height=100,
                                     corner_radius=5,
                                     fg_color=self.font)
        
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

        self.jeux_button = ctk.CTkButton(self.menu_bar,
                                        text="Jeux",
                                        corner_radius=10,
                                        width=100,
                                        height=30,
                                        command=self.toggle_jeux_menu,
                                        hover_color="#5A5A5A",
                                        fg_color="#444444")
        
        self.jeux_button.pack(side="left",
                            padx=15,
                            pady=5)        

        self.main_zone = ctk.CTkFrame(self.app,
                                      fg_color=self.font)
        
        self.main_zone.pack(fill="both",
                            side="bottom",
                            expand=True,
                            padx=15,
                            pady=10)
        

        self.apps_menu = None
        self.jeux_menu = None
        self.settings_frame = None

    fond = ["white", "dark"]
    def fond_color(self, value): 
       
        if value == "white":
            self.font = "white"
            return self.font 
        elif value == "dark":
            self.font = "dark" 
            return self.font
        else: 
            pass


    def action(self):
        """
        histoire de dire que ya quelque chose.
        """
        pass

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
                                        fg_color=self.font,
                                        corner_radius=10)
            
            self.apps_menu.pack(side="top",
                                fill="x",
                                pady=10,
                                padx=15)

            apps = [("Notes_app", self.open_Notes_app),
                    ("Calculatrice", self.open_calculatrice_app),
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

    def toggle_jeux_menu(self):
        """
        Affiche ou cache le menu des jeux sous le menu principal.
        """
        if self.jeux_menu:
            self.jeux_menu.destroy()
            self.jeux_menu = None
        else:
            self.jeux_menu = ctk.CTkFrame(self.app,
                                        height=100,
                                        fg_color=self.font,
                                        corner_radius=10)
            
            self.jeux_menu.pack(side="top",
                                fill="x",
                                pady=10,
                                padx=15)

            jeux = [("Morpion à deux", self.open_morpion_a_deux_app),
                    ("...", self.action)]
            
            for jeux_name, command in jeux:
                jeux_button = ctk.CTkButton(self.jeux_menu,
                                        text=jeux_name,
                                        corner_radius=10,
                                        width=120,
                                        height=50,
                                        hover_color="#5A5A5A",
                                        fg_color="#444444",
                                        command=command)
                
                jeux_button.pack(side="left", padx=15, pady=10)

    def show_settings(self):
        """
        Affiche les paramètres dans la Main Zone.
        """
        self.clear_main_zone()
        
        self.settings_frame = ctk.CTkFrame(self.main_zone,
                                        fg_color=self.font,
                                        corner_radius=10)
        
        self.settings_frame.pack(fill="both",
                                expand=True,
                                padx=15,
                                pady=10)

        # Titre ou label
        label = ctk.CTkLabel(self.settings_frame, text="Choisissez un thème :", font=("Arial", 14), text_color="white")
        label.pack(pady=10, padx=10, anchor="w")

        # Options du menu déroulant
        options = ["système", "clair", "sombre"]

        # Créer le menu
        self.theme_menu = ctk.CTkOptionMenu(self.settings_frame,
                                            values=options,
                                            command=self.theme)  # Appelle une fonction quand on change d'option
        
        self.theme_menu.pack(pady=5, padx=5, anchor="w")

    def theme (self, value):
        self.change_theme(value)
        self.fond_color(value)

    def change_theme(self, value):
        """
        Change le thème selon la sélection du menu.
        """
        if value == "sombre" : 
            ctk.set_appearance_mode("dark")
        elif value == "clair" : 
            ctk.set_appearance_mode("light")
        elif value == "système" : 
            ctk.set_appearance_mode("système")


    def open_Notes_app(self):
        """
        Ouvre l'application Notes.
        """
        from applications.Notes_app import NotesApp
        
        self.clear_main_zone()
        NotesApp(self.main_zone)

    def open_calculatrice_app(self):
        """
        Ouvre l'application Notes.
        """
        from applications.Calculator_app import Calculatrice
        
        self.clear_main_zone()
        Calculatrice(self.main_zone)

    def open_morpion_a_deux_app(self):
        from jeux.morpion_a_deux_app import MorpionApp

        if not self.enroute:
            self.morpion_window = MorpionApp()
            self.morpion_window.mainloop()
            self.enroute = True

    def run(self):
        """
        Lance la boucle principale.
        """
        self.app.mainloop()

app = DeskCoreApp()
app.run()