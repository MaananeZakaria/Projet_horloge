import time

def main():
      
    try:
        heures = int(input("Entrez les heures (0-23) : "))
        if not 0 <= heures < 24:
            print("Erreur : Les heures doivent être entre 0 et 23.")
            return

        minutes = int(input("Entrez les minutes (0-59) : "))
        if not 0 <= minutes < 60:
            print("Erreur : Les minutes doivent être entre 0 et 59.")
            return

        secondes = int(input("Entrez les secondes (0-59) : "))
        if not 0 <= secondes < 60:
            print("Erreur : Les secondes doivent être entre 0 et 59.")
            return

        print(f"Heure valide : {heures:02}:{minutes:02}:{secondes:02}")
    except ValueError:
        print("Erreur : Veuillez entrer un nombre entier.")


    
    while True:
        seconds += 1  
        if seconds == 60:  
            minutes += 1  
            seconds = 0 
        if minutes == 60:  
            heures += 1  
            minutes = 0  
        if heures == 24:  
            heures = 0  
        
        #[Affichage]= ":"(pour le format) , "02" (pour le nombre de chiffres) et 
        # "d" pour signifier que c'est un nombre entier (decimal)
        print(f"\r{heures:02d}h : {minutes:02d}m : {seconds:02d}s", end="", flush=True)
        time.sleep(1)

main()
