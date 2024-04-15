import pandas as pd
import matplotlib.pyplot as plt

def import_data(file_path, num_rows=None):
    # Importation des données à partir du fichier plat (Excel dans ce cas)
    try:
        if num_rows is None:
            data = pd.read_excel(file_path)
        else:
            data = pd.read_excel(file_path, nrows=num_rows)

        # Vérifier s'il existe une colonne qui contient les noms des données
        data_columns = data.columns.tolist()
        name_column = None
        value_column = None

        print("Colonnes disponibles dans le fichier Excel :")
        for i, column in enumerate(data_columns):
            print(f"{i+1}. {column}")

        name_column_num = int(input("Entrez le numéro de la colonne contenant les noms des données (ou 0 si aucune) : ")) - 1
        if name_column_num >= 0:
            name_column = data_columns[name_column_num]

        value_column_num = int(input("Entrez le numéro de la colonne contenant les valeurs des données : ")) - 1
        value_column = data_columns[value_column_num]

        return data, name_column, value_column

    except FileNotFoundError:
        print("Le fichier spécifié est introuvable.")
        return None, None, None
    except Exception as e:
        print("Une erreur s'est produite lors de l'importation des données :", e)
        return None, None, None

def plot_graph(data, name_column, value_column, title, plot_type):
    # Créer le graphique en fonction du type de graphique choisi
    if plot_type == 'scatter':
        data.plot.scatter(x=name_column, y=value_column)
        plt.title(title)
        plt.xlabel("Nom des données")
        plt.ylabel("Valeurs des données")
        plt.show()
    elif plot_type == 'line':
        data.plot(x=name_column, y=value_column)
        plt.title(title)
        plt.xlabel("Nom des données")
        plt.ylabel("Valeurs des données")
        plt.show()
    elif plot_type == 'histogram':
        data[value_column].plot.hist()
        plt.title(title)
        plt.xlabel("Valeurs des données")
        plt.ylabel("Fréquence")
        plt.show()
    else:
        print("Choix de graphique invalide. Veuillez choisir parmi scatter, line ou histogram.")

def main_graph():
    # Demander à l'utilisateur le chemin du fichier
    file_path = input("Veuillez entrer le chemin du fichier Excel contenant les données : ")

    # Demander à l'utilisateur s'il veut importer tout le fichier ou seulement un nombre spécifique de lignes
    num_rows_str = input("Voulez-vous importer tout le fichier ? (oui/non) : ")
    if num_rows_str.lower() == 'non':
        num_rows = int(input("Entrez le nombre de lignes à importer : "))
    else:
        num_rows = None

    # Importer les données
    data, name_column, value_column = import_data(file_path, num_rows)
    if data is None:
        return

    # Demander le titre du graphique
    title = input("Entrez le titre du graphique : ")

    # Demander le type de graphique
    plot_type = input("Choisissez le type de graphique à créer (scatter/line/histogram) : ")

    # Créer le graphique
    plot_graph(data, name_column, value_column, title, plot_type)

if __name__ == "__main__":
    main_graph()