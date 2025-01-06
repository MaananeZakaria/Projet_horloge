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
