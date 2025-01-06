import time

def main():
    s = 0  
    while True:
        s += 1 
        if s == 60: 
            print("1 m") 
            s = 0  # Réinitialise les secondes à 0
        else:
            print(s)  
        time.sleep(1)  # Pause de 1 seconde

main()


import time

def main():
    s = 0  # Initialisation des secondes
    while True:
        s += 1  # Incrémentation des secondes
        if s == 60:  # Vérifie si 60 secondes sont atteintes
            print("\r1 m", end="", flush=True)  # Affiche "1 m" et reste sur la même ligne
            s = 0  # Réinitialise les secondes à 0
        else:
            print(f"\r{s}", end="", flush=True)  # Affiche les secondes en écrasant la précédente
        time.sleep(1)  # Pause de 1 seconde

main()
