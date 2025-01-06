
import time 

def main():

    s=0
    try: #try-except : pour ameliorée l'affichage lorsqu'on interumpt le programme
        while True :
            s+=1 
            print (s)
            time.sleep(1)
    except KeyboardInterrupt:
        print("You pressed Ctrl+C!")
        print("-- Exiting--")        
    
main()
