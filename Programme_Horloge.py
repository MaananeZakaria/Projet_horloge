import time

def main():
    heures, minutes, secondes = saisie_de_heure()
    heure_alarme, minute_alarme, secondes_alarme, message_alarme = saisie_alarme()

    print(f"Heure actuelle réglée : {heures:02}:{minutes:02}:{secondes:02}")
    
    if heure_alarme is not None and minute_alarme is not None and secondes_alarme is not None:
        print(f"Alarme réglée à : {heure_alarme:02}:{minute_alarme:02}:{secondes_alarme:02} ; {message_alarme}") #ajout des s pour les chronos

    boucle_principale(heures, minutes, secondes, heure_alarme, minute_alarme , secondes_alarme , message_alarme)

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
    choix = input("Voulez-vous régler une alarme ? (oui/non) : ").strip().lower() #espaces et majuscules
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
                secondes_alarme = int(input("Entrez les secondes de l'alarme (0-59) : "))
                if 0 <= secondes_alarme < 60:
                    break
                print("Erreur : Les minutes doivent être entre 0 et 59.")
            except ValueError:
                print("Erreur : Veuillez entrer un nombre entier.")  
        
        #Possibilité de saisir un message pour l'alarme
        message_alarme = input("Entrez un message pour l'alarme (facultatif, appuyez sur Entrée pour passer) : ").strip()
        if not message_alarme:
                message_alarme = "Réveil ! RDV, Fin de la cuisson, etc."
        


        return heure_alarme, minute_alarme , secondes_alarme , message_alarme
    return None, None, None

def boucle_principale(heures, minutes, secondes, heure_alarme, minute_alarme , secondes_alarme, message_alarme):
    alarme_declenchee = False
    modification_alarme_possible = True
    modification_heure_possible = True

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

        # Affichage de l'heure , end="" permet de ne pas sauter de ligne et flush=True permet de forcer l'affichage
        print(f"\r{heures:02}h:{minutes:02}m:{secondes:02}s", end="", flush=True)

        # -------------Vérification de l'alarme-----------
        if not alarme_declenchee and heure_alarme is not None and minute_alarme is not None and secondes_alarme is not None:

            if heures == heure_alarme and minutes == minute_alarme and secondes == secondes_alarme: # Compare l'heure actuelle avec l'heure de l'alarme
                print(f"\n\aC'est l'heure ! {message_alarme}")    # \a pour le bip
                alarme_declenchee = True

        # ----permettre la modification de l'alarme ( version modifiée )--
        if modification_alarme_possible:
            choix_modif = input("Souhaitez-vous modifier l'alarme ? (oui/non) : ").strip().lower()
            if choix_modif == "oui":
                heure_alarme, minute_alarme , secondes_alarme = saisie_alarme() # Re-saisie de l'alarme

                alarme_declenchee = False  # Réinitialisation de l'état de l'alarme
                print(f"Nouvelle alarme réglée à : {heure_alarme:02}:{minute_alarme:02}:{secondes_alarme:02}")

            elif choix_modif == "non":
                modification_alarme_possible = False

         # =========  Modifications de l'heure ou suppressions de l'alarme ==========
        if modification_heure_possible:
            print("\n Souhaitez-vous modifier l'heure ou supprimer l'alarme ? Si oui tapez h/m/s/d, sinon tapez non.")
            choix = input("h/m/s pour changer l'heure, d pour supprimer l'alarme ").strip().lower()
            modification_heure_possible = False  # ----- Empêche la répétition du message

            if choix in ["h", "m", "s"]:
                try:
                    valeur = int(input("Entrez la nouvelle valeur : "))

                    if choix == "h" and 0 <= valeur < 24:
                        heures = valeur
                    elif choix == "m" and 0 <= valeur < 60:
                        minutes = valeur
                    elif choix == "s" and 0 <= valeur < 60: # on a mis les s pour les chronos
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
