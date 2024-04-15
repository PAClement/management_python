import pandas as pd

def update_user_info(email, field_to_update, new_value, csv_file):
    # Charger le fichier CSV des utilisateurs
    df = pd.read_csv(csv_file)

    # Vérifier si l'utilisateur existe dans le fichier
    if email in df['email'].values:
        # Mettre à jour le champ spécifié de l'utilisateur
        df.loc[df['email'] == email, field_to_update] = new_value
        
        # Enregistrer les modifications dans le fichier CSV
        df.to_csv(csv_file, index=False)
        print("Informations de l'utilisateur mises à jour avec succès.")
    else:
        print("Utilisateur non trouvé.")

def main_menu(email):
    # Charger le fichier CSV des utilisateurs
    df = pd.read_csv('users.csv')

    # Afficher les informations de l'utilisateur
    user_info = df[df['email'] == email]
    print("Informations de l'utilisateur :")
    print(user_info)

    while True:
        print("\nMenu principal :")
        print("1. Modifier le mot de passe")
        print("2. Modifier le nom de famille")
        print("3. Modifier le prénom")
        print("4. Modifier le numéro de téléphone")
        print("5. Se déconnecter")

        choice = input("Choisissez une option (1/2/3/4/5) : ")

        if choice in ['1', '2', '3', '4']:
            new_value = input(f"Entrez la nouvelle valeur pour le champ {choice} : ")
            fields = ['password', 'lastname', 'firstname', 'phone']
            field_to_update = fields[int(choice) - 1]
            update_user_info(email, field_to_update, new_value, 'users.csv')
        elif choice == '5':
            print("Vous avez été déconnecté.")
            break
        else:
            print("Option invalide. Veuillez réessayer.")

# Exemple d'utilisation de la fonction main_menu
if __name__ == "__main__":
    email = input("Entrez l'adresse e-mail de l'utilisateur : ")
    main_menu(email)