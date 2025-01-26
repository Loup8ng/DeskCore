class DKCE:
    """
    Class pour gérer les fichiers dkce (DesKCorE).
    """

    def save_dkceTXT(file_path:str, text:str):
        """
        Enregistre un texte dans un fichier .dkceTXT.
        """
        if not file_path.endswith(".dkceTXT"):
            file_path += ".dkceTXT"

        file = open(file_path, "w", encoding="utf-8") #w = write
        file.write(text)
        file.close()



    def load_dkceTXT(file_path):
        """
        Charge un texte à partir d'un fichier .dkceTXT.
        """
        file = open(file_path, "r", encoding="utf-8") #r = read
        text = file.read()
        file.close()
        return text

