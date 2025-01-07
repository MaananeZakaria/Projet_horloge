import time

def main():
    seconds = 0  
    minutes = 0  
    heures = 0
    while True:
        seconds += 1  
        if seconds == 60:  
            minutes += 1 
            seconds = 0  
        if minutes == 60:  # Vérifie si 60 minutes sont atteintes 
            heures += 1  # Incrémente les heures
            minutes = 0  # Réinitialise les minutes à 0
    
        print(f"\r{' ' * 20}", end="") 
        # Efface complètement la ligne ( ligne de 20 ,on regle le probleme ss ou mm)
        print(f"\r{heures}h : {minutes}m : {seconds}s", end="", flush=True)
        time.sleep(1)       
main()