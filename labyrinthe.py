level_1 = [
    "+-------+------------+",
    "|       |            |",
    "+-----+ |   -----+   |",
    "|     |          |   |",
    "|  |  +------+   |   |",
    "|  |         | T |   |",
    "|  +----     +---+   |",
    "|      |             |",
    "+ ---  +-------------+",                           
    "|      |             |",
    "+ --+  |   |         |",
    "|  T|  |   |    -----+",
    "|   |      |         |",
    "|   +------+---+     |",
    "|              |     |",
    "|    +-------  |     |",
    "| T  |               |",
    "| ---+     ----------+",
    "|    |              P|",
    "+----+---------------+"
    ]
def affiche_labyrinthe(lab):
    for ligne in lab:
        print(ligne)

def affiche_bordure_labyrinthe(taille):
    print ("+{}+".format("-" * (taille - 2)))
    for i in range (taille - 2):
        print("|{}|".format("" * (taille - 2)))

    print ("+{}+".format("-" * (taille - 2)))

def choix_joueur():
    return input ("Votre déplacement (Haut/Bat/Droite/Gauche) ? ")

affiche_labyrinthe(level_1)
dep = choix_joueur()
print (dep)
perso = "G"
pos_perso = [1, 1]

def affiche_labyrinthe(lab, pos_perso):
    """
       Affichage d'un labyrinte

       lab : Variable contenant le labyrinte
    """
    n_ligne = 0
    for ligne in lab:
        if pos_perso[1, 1] == n_ligne :
            print (ligne, "<- ligne du personnage")
        else:
            print(ligne)
        n_ligne = n_ligne + 1
