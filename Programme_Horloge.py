import time

def main():
    try:
        # =========  Saisie de l'heure actuelle , Possibilité de saisir directement après l'erreur  ==========
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

        print(f"Heure actuelle réglée : {heures:02}:{minutes:02}:{secondes:02}")

        # ===============  Réglage de l'alarme  , Possibilité de saisir directement après l'erreur =============
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
        
            print(f"Alarme réglée à {heure_alarme:02}:{minute_alarme:02}.")
        else:
            heure_alarme, minute_alarme = None, None
        #====================================================================================================

    except ValueError:
        print("Erreur : Veuillez entrer un nombre entier.")
        return

    # ===========  Boucle principale de gestion du temps  ===========
    alarme_declenchee = False  # Indicateur pour vérifier si l'alarme a été déclenchée
    modification_possible = True

    while True:
        secondes += 1
        if secondes == 60:
            minutes += 1
            secondes = 0
        if minutes == 60:
            heures += 1
            minutes = 0
        if heures == 24:
            heures = 0

        # ===========  Affichage de l'heure  ===========
        print(f"\r{heures:02d}h : {minutes:02d}m : {secondes:02d}s", end="", flush=True)

        # ==========  Vérification de l'alarme  ==========
        if not alarme_declenchee and heure_alarme is not None and minute_alarme is not None:
            if heures == heure_alarme and minutes == minute_alarme:
                print("\nRéveil ! 🚨")
                alarme_declenchee = True  # Marque l'alarme comme déclenchée

        # =========  Gestion des modifications ou suppressions de l'alarme ==========
        if modification_possible:
            print("\n Souhaitez-vous modifier l'heure ou supprimer l'alarme ? Si oui tapez h/m/s/d, sinon tapez non.")
            choix = input("h/m/s pour changer l'heure, d pour supprimer l'alarme ").strip().lower()
            modification_possible = False  # ----- Empêche la répétition du message

            if choix in ["h", "m", "s"]:
                try:
                    valeur = int(input("Entrez la nouvelle valeur : "))
                    if choix == "h" and 0 <= valeur < 24:
                        heures = valeur
                    elif choix == "m" and 0 <= valeur < 60:
                        minutes = valeur
                    elif choix == "s" and 0 <= valeur < 60:
                        secondes = valeur
                    else:
                        print("Erreur : Valeur hors limites.")
                except ValueError:
                    print("Erreur : Veuillez entrer un nombre entier.")
            elif choix == "d":
                heure_alarme, minute_alarme = None, None
                print("Alarme supprimée.")
                alarme_declenchee = False
            elif choix == "non":
                print("Aucune modification effectuée.")
            else:
                print("Option invalide.")

        time.sleep(1)

if __name__ == "__main__":
    main()
