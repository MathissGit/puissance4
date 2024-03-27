import os

class Game():

    # Constructeur
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.ligne = 6
        self.colone = 7
        self.plateau = [[" " for _ in range(self.colone)] for _ in range(self.ligne)]
        self.coupJoue = 0
        self.jetonJaune = 1
        self.jetonRouge = -1
        self.player = None

    # Getteur pour les regles du jeu
    def getRegles(self): return self.regles

    # Getteur plateau 
    def getPlateau(self): return self.plateau
    
    # Afficher le gagnant de la partie 
    def displayWinner(self): 
        if self.player == "" or self.player is None:
            return "personne n'a gagné"
        else: 
            return self.player + "a gagné"

    # Affichage de la grille du jeu
    def affichePlateau(self):
        for ligne in self.plateau:
            print("+---+---+---+---+---+---+---+")
            for case in ligne : 
                print("|",format(case), end=" ")
            print("|") 
        print("+---+---+---+---+---+---+---+")

    # Fonction pour placer un jeton dans le jeu. prend en parametre le jeton du joueur
    def placerJeton(self, jeton):
        while True:
            colone = input("Choisir une colonne (intervalle 0 à 6) : ")

            # Vérifie si la colonne est dans l'intervalle 0 à 6
            if colone.isdigit() and 0 <= int(colone) <= 6:
                colone = int(colone)
                # Parcourir le plateau de bas en haut pour trouver la première case vide dans la colonne choisie
                for i in range(len(self.plateau)-1, -1, -1):
                    if self.plateau[i][colone] == " ":
                        self.plateau[i][colone] = jeton
                        return True
                print("La colonne est pleine. Choisissez une autre colonne.")
            else:
                print("La colonne choisie n'est pas dans l'intervalle 0 à 6 ou n'est pas un nombre entier.")
            
    # Fonction qui verfie les coups gagnants
    def VerificationCoupGagnant(self, symbole): 
        
        # Vérification des alignements horizontaux
        for ligne in self.plateau:
            for i in range(len(ligne) - 3):
                if symbole * 4 in ''.join(ligne[i:i+4]):
                    return True

        # Vérification des alignements verticaux
        for col in range(len(self.plateau[0])):
            for i in range(len(self.plateau) - 3):
                if symbole * 4 in ''.join([self.plateau[j][col] for j in range(i, i+4)]):
                    return True

        # Vérification des alignements diagonaux (montants et descendants)
        for i in range(len(self.plateau) - 3):
            for j in range(len(self.plateau[0]) - 3):
                if symbole * 4 in ''.join([self.plateau[i+k][j+k] for k in range(4)]) or \
                        symbole * 4 in ''.join([self.plateau[i+3-k][j+k] for k in range(4)]):
                    return True

        return False
    
    # Fonction qui gère les tours des joueurs
    def TourParTour_ASCII(self):

        # Choix du joueur pour la fonction TourPartour
        en_cours = True
        joueur_actuel = self.player1

        while en_cours:
            #nettoyage du terminal
            os.system('cls' if os.name == 'nt' else 'clear')

            # Affichage du plateau et demande de placement du jeton
            self.affichePlateau()
            print(f"C'est au tour du joueur {joueur_actuel.getSymbole()}")
            if self.placerJeton(joueur_actuel.getSymbole()):
                self.coupJoue += 1

                # Vérification si le joueur actuel a gagné
                if self.VerificationCoupGagnant(joueur_actuel.getSymbole()):
                    os.system('cls' if os.name == 'nt' else 'clear')
                    self.affichePlateau()
                    print(f"--------------------- \nLe joueur {joueur_actuel.getSymbole()} a gagné ! \n---------------------")
                    en_cours = False
                    break

                # Vérification de l'égalité
                if self.coupJoue == self.ligne * self.colone:
                    self.affichePlateau()
                    print("Match nul")
                    en_cours = False
                    break

                # Passage au joueur suivant
                joueur_actuel = self.player2 if joueur_actuel == self.player1 else self.player1