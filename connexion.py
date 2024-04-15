import pandas as pd
from update import main_menu

def login(email, password, csv_file):
    # Lecture du fichier CSV
    df = pd.read_csv(csv_file)

    # Vérification des informations d'identification
    for index, row in df.iterrows():
        if row['email'] == email and row['password'] == password:
            return True

    return False

def main_connexion():
    csv_file = 'users.csv'  # Remplacez 'users.csv' par le nom de votre fichier CSV

    print("Bienvenue ! Veuillez vous connecter.")
    email = input("Adresse e-mail : ")
    password = input("Mot de passe : ")

    if login(email, password, csv_file):
        print("Connexion réussie. Vous êtes connecté.")
        main_menu(email)
    else:
        print("La connexion a échoué. Veuillez vérifier vos informations d'identification.")

if __name__ == "__main__":
    main()