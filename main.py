from connexion import main_connexion
from inscription import main_inscription

def accueil():
    print("Bienvenue sur notre application !")
    print("Veuillez choisir une option :")
    print("1. Connexion")
    print("2. Inscription")
    print("3. Quitter")

    choix = input("Entrez le numéro correspondant à votre choix : ")
    return choix

def main():
    while True:
        choix = accueil()

        if choix == '1':
            print("Vous avez choisi Connexion.")
            main_connexion()

        elif choix == '2':
            print("Vous avez choisi Inscription.")
            main_inscription()

        elif choix == '3':
            print("Vous avez choisi de quitter. Au revoir !")
            break

        else:
            print("Choix invalide. Veuillez entrer un numéro valide.")

if __name__ == "__main__":
    main()
