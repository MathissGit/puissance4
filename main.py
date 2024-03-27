from Joueur import *
from Game import *
import pyfiglet
import os

class Main():

    def __init__(self):
        self.titre = "PUISSANCE 4"
        self.regles = "REGLES DU JEU : \n- Pour commencer une partie de puissance 4, on désigne le premier joueur.\n- Celui-ci met un de ses jetons de couleur dans l’une des colonnes de son choix. Le jeton tombe alors en bas de la colonne. \n- Le deuxième joueur insère à son tour son jeton, de l’autre couleur dans la colonne de son choix.\n- Ansi de suite jusqu’à obtenir une rangée de 4 jetons de même couleur. \n\nCOMMENT GAGNER : \n- Pour gagner une partie de puissance 4, il suffit d’être le premier à aligner 4 jetons de sa couleur horizontalement, verticalement et diagonalement."

    # Getteur pour le titre du jeu
    def getTitre(self): return self.titre

    # Getteur pour les regles du jeu
    def getRegles(self): return self.regles

    def start_game(self):

        #nettoyage du terminal
        os.system('cls' if os.name == 'nt' else 'clear')

        # Afficher le titre du jeu en ASCII art
        ascii_art = pyfiglet.figlet_format(self.getTitre(), font="doom")
        print(ascii_art)

        # Afficher les regles du jeu
        print(self.getRegles())

        # Debut, choix des couleurs
        print("\nChoix entre le rouge et le jaune : ")
        game = Game(Joueur(input("\nPLAYER 1 / \nChoisir une couleur ( R ou Y ) : ")), Joueur(input("\nPLAYER 2 / \nCouleur restante  ( R ou Y ): ")))
        game.TourParTour_ASCII()

        # Choix pour recommencer une partie 
        reponse = input('Recommencer une partie ? [ Y:yes | N:no ] : ')
        if reponse == "Y" or reponse == "y": 
            main.start_game()

if __name__ == "__main__":
    main = Main()
    main.start_game()