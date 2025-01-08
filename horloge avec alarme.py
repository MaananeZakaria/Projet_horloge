import time
import os  # Pour jouer un son (optionnel)


def main():
    try:
        # Saisie des heures
        heures = int(input("Entrez l'heure actuelle (0-23) : "))
        if not 0 <= heures < 24:
            print("Erreur : Les heures doivent être entre 0 et 23.")
            return

        # Saisie des minutes
        minutes = int(input("Entrez les minutes actuelles (0-59) : "))
        if not 0 <= minutes < 60:
            print("Erreur : Les minutes doivent être entre 0 et 59.")
            return

        # Saisie des secondes
        secondes = int(input("Entrez les secondes actuelles (0-59) : "))
        if not 0 <= secondes < 60:
            print("Erreur : Les secondes doivent être entre 0 et 59.")
            return

        print(f"Heure actuelle réglée : {heures:02}:{minutes:02}:{secondes:02}")

        # Demande de réglage de l'alarme
        choix = input("Voulez-vous régler une alarme ? (oui/non) : ").strip().lower()
        if choix == "oui":
            heure_alarme = int(input("Entrez l'heure de l'alarme (0-23) : "))
            if not 0 <= heure_alarme < 24:
                print("Erreur : L'heure doit être entre 0 et 23.")
                return

            minute_alarme = int(input("Entrez les minutes de l'alarme (0-59) : "))
            if not 0 <= minute_alarme < 60:
                print("Erreur : Les minutes doivent être entre 0 et 59.")
                return

            print(f"Alarme réglée à {heure_alarme:02}:{minute_alarme:02}.")
        else:
            heure_alarme, minute_alarme = None, None

    except ValueError:
        print("Erreur : Veuillez entrer un nombre entier.")
        return

    # Début du chronomètre
    while True:
        secondes += 1  # Incrémentation des secondes
        if secondes == 60:  # Réinitialisation des secondes
            minutes += 1
            secondes = 0
        if minutes == 60:  # Réinitialisation des minutes
            heures += 1
            minutes = 0
        if heures == 24:  # Réinitialisation des heures
            heures = 0

        # Affichage continu du temps formaté
        print(f"\r{heures:02d}h : {minutes:02d}m : {secondes:02d}s", end="", flush=True)

        # Vérification de l'alarme
        if heure_alarme is not None and minute_alarme is not None:
            if heures == heure_alarme and minutes == minute_alarme and secondes == 0:
                print("\n⏰ L'alarme sonne maintenant !")

                # Jouer un son (optionnel)
                try:
                    if os.name == 'nt':  # Pour Windows
                        os.system("echo \a")
                    else:  # Pour macOS et Linux
                        os.system("afplay /System/Library/Sounds/Ping.aiff")
                except Exception:
                    print("🔔 Son d'alarme joué (selon la configuration système).")
                
                break  # Arrête le programme après que l'alarme a sonné

        time.sleep(1)  # Pause d'une seconde


main()

























































































































































