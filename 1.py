
import time

def main():
    s = 0
    while True:
        s += 1 
        if s == 60:  
            print("\r1 m", end="", flush=True)  # Affiche "1 m" et reste sur la même ligne
            s = 0  
        else:
            print(f"\r{s}", end="", flush=True)  # Affiche les secondes en écrasant la précédente
        time.sleep(1) 

main()
