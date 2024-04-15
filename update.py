import pandas as pd

def update_user_info(username, new_info):
    # Charger le fichier CSV des utilisateurs
    df = pd.read_csv('users.csv')

    # Vérifier si l'utilisateur existe dans le fichier
    if username in df['username'].values:
        # Mettre à jour les informations de l'utilisateur
        df.loc[df['username'] == username, ['info_column']] = new_info
        
        # Enregistrer les modifications dans le fichier CSV
        df.to_csv('users.csv', index=False)
        print("Informations de l'utilisateur mises à jour avec succès.")
    else:
        print("Utilisateur non trouvé.")

# Exemple d'utilisation de la fonction update_user_info
if __name__ == "__main__":
    username = input("Entrez le nom d'utilisateur à mettre à jour : ")
    new_info = input("Entrez les nouvelles informations de l'utilisateur : ")
    update_user_info(username, new_info)
