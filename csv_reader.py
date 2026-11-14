
import os
import pandas as pd


# Exceptions personnalisees
class CsvException(Exception):
    pass


class FichierIntrouvableException(CsvException):
    pass


class LigneInvalideException(CsvException):
    pass


class PrixNegatifException(CsvException):
    pass


# Fonction pour charger le fichier CSV
def charger_csv(chemin):

    # Construire le chemin du fichier
    dossier = os.path.dirname(__file__)
    chemin = os.path.join(dossier, chemin)

    # Verifier l'existence du fichier
    if not os.path.exists(chemin):
        raise FichierIntrouvableException("Fichier introuvable")

    # Lire le fichier avec Pandas
    try:
        df = pd.read_csv(
            chemin,
            sep=";",
            dtype=str,
            skip_blank_lines=True
        )
    except pd.errors.EmptyDataError:
        return []

    # Verifier les colonnes
    if list(df.columns) != ["id", "nom", "prix"]:
        raise LigneInvalideException("Format des colonnes invalide")

    articles = []

    # Parcourir les lignes
    for index, ligne in df.iterrows():

        # Verifier le prix numerique
        try:
            prix = float(ligne["prix"])
        except (ValueError, TypeError):
            raise LigneInvalideException(
                f"Ligne {index + 2} : prix non numerique"
            )

        # Verifier le prix positif
        if prix <= 0:
            raise PrixNegatifException(
                f"Ligne {index + 2} : le prix doit etre positif"
            )

        # Creer le dictionnaire
        article = {
            "id": ligne["id"],
            "nom": ligne["nom"],
            "prix": prix
        }

        articles.append(article)

    return articles
