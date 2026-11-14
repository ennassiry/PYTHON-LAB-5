
from csv_reader import (
    charger_csv,
    FichierIntrouvableException,
    LigneInvalideException,
    PrixNegatifException
)


def main():

    try:
        articles = charger_csv("article.csv")
        

        print("Liste des articles :")

        for article in articles:
            print(article)

    except FichierIntrouvableException as e:
        print("Erreur :", e)

    except LigneInvalideException as e:
        print("Erreur :", e)

    except PrixNegatifException as e:
        print("Erreur :", e)


if __name__ == "__main__":
    main()
