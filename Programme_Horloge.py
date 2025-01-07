import time

def main():
    # Demander l'heure, les minutes et les secondes initiales
    try:
        heures = int(input("Entrez l'heure de départ (0-23) : "))
        minutes = int(input("Entrez les minutes de départ (0-59) : "))
        seconds = int(input("Entrez les secondes de départ (0-59) : "))
    except ValueError:
        print("Veuillez entrer des nombres valides.")
        return
    
    # Verification et Validation des valeurs entrées
    if not (0 <= heures < 24 and 0 <= minutes < 60 and 0 <= seconds < 60):
        print("Les valeurs doivent respecter les plages : heures (0-23), minutes (0-59), secondes (0-59).")
        return

    
    while True:
        seconds += 1  
        if seconds == 60:  
            minutes += 1  
            seconds = 0 
        if minutes == 60:  
            heures += 1  
            minutes = 0  
        if heures == 24:  # Vérifie si 24 heures sont atteintes
            heures = 0  # Réinitialise les heures à 0
        
        # Efface complètement la ligne(l31) et affiche l'heure actuelle (l32)
        print(f"\r{' ' * 20}", end="")
        print(f"\r{heures:02d}h : {minutes:02d}m : {seconds:02d}s", end="", flush=True)
        time.sleep(1)

main()
