import time
from datetime import datetime

def main():
    choix = input("Souhaitez-vous régler l'heure manuellement ou utiliser l'heure locale de votre PC ? (manuel/local) : ").strip().lower()

    if choix == "local":
        heures, minutes, secondes = heure_locale()
    elif choix == "manuel":
        heures, minutes, secondes = saisie_de_heure()
    else:
        print("Choix invalide. Utilisation de l'heure locale par défaut.")
        heures, minutes, secondes = heure_locale()

    heure_alarme, minute_alarme, seconde_alarme, message_alarme = saisie_alarme()

    print(f"Heure actuelle réglée : {heures:02}:{minutes:02}:{secondes:02}")
    if heure_alarme is not None:
        print(f"Alarme réglée à : {heure_alarme:02}:{minute_alarme:02}:{seconde_alarme}")

    # Afficher les options une seule fois au début
    afficher_options()
    
    # Démarrer la boucle principale
    boucle_principale(heures, minutes, secondes, heure_alarme, minute_alarme, seconde_alarme, message_alarme)


def heure_locale():
    heures = int(time.strftime('%H'))
    minutes = int(time.strftime('%M'))
    secondes = int(time.strftime('%S'))
    return heures, minutes, secondes


def saisie_de_heure():
    while True:
        try:
            heures = int(input("Entrez l'heure actuelle (0-23) : "))
            if 0 <= heures < 24:
                break
            print("Erreur : Les heures doivent être entre 0 et 23.")
        except ValueError:
            print("Erreur : Veuillez entrer un nombre entier.")

    while True:
        try:
            minutes = int(input("Entrez les minutes actuelles (0-59) : "))
            if 0 <= minutes < 60:
                break
            print("Erreur : Les minutes doivent être entre 0 et 59.")
        except ValueError:
            print("Erreur : Veuillez entrer un nombre entier.")

    while True:
        try:
            secondes = int(input("Entrez les secondes actuelles (0-59) : "))
            if 0 <= secondes < 60:
                break
            print("Erreur : Les secondes doivent être entre 0 et 59.")
        except ValueError:
            print("Erreur : Veuillez entrer un nombre entier.")

    return heures, minutes, secondes


def saisie_alarme():
    choix = input("Voulez-vous régler une alarme ? (oui/non) : ").strip().lower()
    if choix == "oui":
        while True:
            try:
                heure_alarme = int(input("Entrez l'heure de l'alarme (0-23) : "))
                if 0 <= heure_alarme < 24:
                    break
                print("Erreur : L'heure doit être entre 0 et 23.")
            except ValueError:
                print("Erreur : Veuillez entrer un nombre entier.")

        while True:
            try:
                minute_alarme = int(input("Entrez les minutes de l'alarme (0-59) : "))
                if 0 <= minute_alarme < 60:
                    break
                print("Erreur : Les minutes doivent être entre 0 et 59.")
            except ValueError:
                print("Erreur : Veuillez entrer un nombre entier.")

        while True:
            try:
                seconde_alarme = int(input("Entrez les secondes de l'alarme (0-59) : "))
                if 0 <= seconde_alarme < 60:
                    break
                print("Erreur : Les secondes doivent être entre 0 et 59.")
            except ValueError:
                print("Erreur : Veuillez entrer un nombre entier.")

        message_alarme = input("Entrez un message pour l'alarme (facultatif, appuyez sur Entrée pour passer) : ").strip()
        if not message_alarme:
            message_alarme = "Réveil ! RDV, Fin de la cuisson, etc."

        return heure_alarme, minute_alarme, seconde_alarme, message_alarme
    return None, None, None, None


def afficher_options():
    print("\nOptions disponibles :")
    print("1. Modifier l'alarme")
    print("2. Modifier l'heure")
    print("3. Supprimer l'alarme")
    print("4. Continuer")


def boucle_principale(heures, minutes, secondes, heure_alarme, minute_alarme, seconde_alarme, message_alarme):
    alarme_declenchee = False
    afficher_menu = True

    while True:
        secondes += 1
        if secondes == 60:
            secondes = 0
            minutes += 1
        if minutes == 60:
            minutes = 0
            heures += 1
        if heures == 24:
            heures = 0

        # Afficher l'heure
        print(f"\r{heures:02}:{minutes:02}:{secondes:02}", end="", flush=True)

        # Vérifier si l'alarme doit se déclencher
        if not alarme_declenchee and heure_alarme is not None:
            if heures == heure_alarme and minutes == minute_alarme and secondes == seconde_alarme:
                print(f"\n\aC'est l'heure ! {message_alarme}")
                alarme_declenchee = True

        # Proposer les choix une seule fois au début
        if afficher_menu:
            choix = input("\nEntrez votre choix (1-4) : ").strip()
            afficher_menu = False  # Ne plus afficher le menu après la première fois

            if choix == "1":
                heure_alarme, minute_alarme, seconde_alarme, message_alarme = saisie_alarme()
                alarme_declenchee = False
                afficher_menu = True  # Réafficher le menu si nécessaire
            elif choix == "2":
                try:
                    heures = int(input("Entrez la nouvelle heure (0-23) : "))
                    minutes = int(input("Entrez les nouvelles minutes (0-59) : "))
                    secondes = int(input("Entrez les nouvelles secondes (0-59) : "))
                except ValueError:
                    print("Erreur : Veuillez entrer des nombres valides.")
                afficher_menu = True
            elif choix == "3":
                heure_alarme, minute_alarme, seconde_alarme, message_alarme = None, None, None, None
                print("Alarme supprimée.")
                afficher_menu = True
            elif choix == "4":
                print("Reprise du décompte sans modification.")
            else:
                print("Choix invalide.")
                afficher_menu = True

        time.sleep(1)


if __name__ == "__main__":
    main()
