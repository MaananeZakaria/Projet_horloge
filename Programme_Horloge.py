import time

def main():
    seconds = 0  
    minutes = 0  # Initialisation des minutes
    while True:
        seconds += 1  
        if seconds == 60:  
            minutes += 1  # Incrémente les minutes
            seconds = 0  
        print(f"\r{' ' * 10}", end="")  # Efface complètement la ligne(fin du 1m:9ss)
        print(f"\r{minutes}m : {seconds}s", end="", flush=True)
        time.sleep(1)  # Pause de 1 seconde

main()
