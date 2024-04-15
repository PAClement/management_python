import click
import pandas as pd

@click.command()
@click.option('--email', prompt='Email', help='Adresse email de l\'utilisateur')
@click.password_option(prompt='Mot de passe', help='Mot de passe de l\'utilisateur')
@click.password_option(prompt='Confirmez le mot de passe', help='Confirmez le mot de passe')
@click.option('--nom', prompt='Nom', help='Nom de l\'utilisateur')
@click.option('--prenom', prompt='Prénom', help='Prénom de l\'utilisateur')
@click.option('--telephone', prompt='Téléphone', help='Numéro de téléphone de l\'utilisateur')
def inscription(email, password, confirm_password, nom, prenom, telephone):
    if password != confirm_password:
        click.echo("Les mots de passe ne correspondent pas. Veuillez réessayer.")
        return

    # Vérifier si l'utilisateur existe déjà dans le fichier Excel
    users_df = pd.read_excel('users.csv', engine='openpyxl', dtype=str)
    if email in users_df['Email'].values:
        click.echo("Cet email existe déjà. Veuillez utiliser un autre email.")
        return

    # Ajouter l'utilisateur au fichier Excel
    new_user = {'Email': email, 'Mot de passe': password, 'Nom': nom, 'Prénom': prenom, 'Téléphone': telephone}
    users_df = users_df.append(new_user, ignore_index=True)

    # Sauvegarder le DataFrame dans le fichier Excel
    users_df.to_excel('users.xlsx', index=False, engine='openpyxl')
    click.echo("Utilisateur inscrit avec succès !")

if __name__ == '__main__':
    inscription()
