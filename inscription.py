import csv
from update import main_menu

def add_user_to_csv(email, password, lastname, firstname, phone):
    with open("users.csv", mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([email, password, lastname, firstname, phone])

def main_inscription():
    print("Bienvenue Inscrivez vous !")
    print("Veuillez saisir vos informations :")

    email = input("Email : ")
    password = input("Mot de passe : ")
    confirm_password = input("Confirmez votre mot de passe : ")
    lastname = input("Nom : ")
    firstname = input("Prénom : ")
    phone = input("Téléphone : ")

    print("\nVous avez saisi les informations suivantes :")
    print("Email :", email)
    print("Mot de passe :", '*' * len(password))  # Affiche des * pour le mot de passe
    print("Nom :", lastname)
    print("Prénom :", firstname)
    print("Téléphone :", phone)

    confirmation = input("\nConfirmez-vous l'inscription ? (O/N) : ")
    if confirmation.lower() == 'o':
        add_user_to_csv(email, password, lastname, firstname, phone)
        print("Inscription réussie ! Les informations ont été ajoutées au fichier users.csv.")
        main_menu(email)
    else:
        print("Inscription annulée.")

if __name__ == "__main__":
    main()
