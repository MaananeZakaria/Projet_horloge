import pygame
import random
import sys  

# Initialisation de Pygame
pygame.init()

def enregistrer_score(score):
    with open("scores.txt", "a") as fichier:  # Mode "a" pour ajouter sans écraser
        fichier.write(f"Score : {score}\n")

# Dimensions de la fenêtre
LARGEUR, HAUTEUR = 1300, 800
écran = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Fruit Ninja")  

# Couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
ROUGE = (255, 0, 0)
VERT = (0, 255, 0)
BLEU = (0, 0, 255)
JAUNE = (255, 255, 0)

# Police
defaut_police = pygame.font.Font(None, 36)

# Variables globales
horloge = pygame.time.Clock()
FPS = 60
score = 0

# Six hauteurs distinctes où les fruits atteignent leur équilibre
hauteurs_niveaux = [HAUTEUR // 6, HAUTEUR // 3, HAUTEUR // 2, HAUTEUR * 2 // 3, HAUTEUR * 5 // 6, HAUTEUR]  # 6 niveaux distincts

# Classe Fruit
class Fruit:
    def __init__(self):
        self.couleur = random.choice([ROUGE, VERT, BLEU, JAUNE])
        
        if self.couleur == ROUGE:
            self.rayon = 40  
            self.vitesse_y = -11  # ici la vitesse a une influence sur la hauteur ( grosse vitesse(negative)= grande vitesse)
            self.vitesse_x = random.uniform(-2, 3)  
            self.acceleration = 0.2  
            self.position_cible = hauteurs_niveaux[0]  # Fruit rouge uniquement au niveau le plus bas
            self.atteint_équilibre = False
        elif self.couleur == JAUNE:
            self.rayon = 20  
            self.vitesse_y = -5
            self.vitesse_x = random.uniform(-2, 3)  
            self.acceleration = 0.2  
            self.position_cible = hauteurs_niveaux[0]  # Fruit jaune uniquement au premier niveau
            self.atteint_équilibre = False
        elif self.couleur == VERT:
            self.rayon = 40  
            self.vitesse_y = -8
            self.vitesse_x = random.uniform(-2, 3)  
            self.acceleration = 0.2  
            self.position_cible = random.choice(hauteurs_niveaux)  # Fruit vert va aux six niveaux, de manière aléatoire
            self.atteint_équilibre = False
        elif self.couleur == BLEU:
            self.rayon = 20  
            self.vitesse_y = -5
            self.vitesse_x = random.uniform(-2, 3)  
            self.acceleration = 0.2  
            self.position_cible = hauteurs_niveaux[0]  # Fruit bleu uniquement au premier niveau
            self.atteint_équilibre = False

        self.x = random.randint(self.rayon, LARGEUR - self.rayon)
        self.y = HAUTEUR + self.rayon  # Position initiale en bas de l'écran
        self.coupé = False

    def bouger(self):
        if not self.atteint_équilibre:
            # Phase de montée
            self.y += self.vitesse_y
            self.x += self.vitesse_x

            self.vitesse_y += 0.1  # Ralentissement de la montée

            if self.y <= self.position_cible:
                self.y = self.position_cible
                self.vitesse_y = 0
                self.atteint_équilibre = True  # Le fruit a atteint son sommet

        else:
            # Phase de descente
            self.vitesse_y += self.acceleration  # Applique la gravité
            self.y += self.vitesse_y
            self.x += self.vitesse_x  # Mouvement horizontal pour la descente

            # Si le fruit sort de l'écran par le bas, on le marque comme à supprimer
            if self.y >= HAUTEUR + self.rayon:
                self.coupé = True  # On marque le fruit comme coupé (disparaît)

    def dessiner(self):
        if not self.coupé:
            pygame.draw.circle(écran, self.couleur, (int(self.x), int(self.y)), self.rayon)

    def est_touché(self, pos):
        distance = ((self.x - pos[0])**2 + (self.y - pos[1])**2)**0.5
        return distance <= self.rayon

# Classe Lame
class Lame:
    def __init__(self):
        self.positions = []
        self.longueur_max = 10

    def mettre_à_jour(self, pos):
        self.positions.append(pos)
        if len(self.positions) > self.longueur_max:
            self.positions.pop(0)

    def dessiner(self):
        if len(self.positions) > 1:
            pygame.draw.lines(écran, BLANC, False, self.positions, 3)

# Classe principale du jeu
class JeuFruitNinja:
    def __init__(self):
        self.fruits = []
        self.lame = Lame()
        self.en_cours = True
        self.timer_ajout = 0

    def ajouter_fruit(self):
        self.fruits.append(Fruit())

    def gérer_événements(self):
        for événement in pygame.event.get():
            if événement.type == pygame.QUIT:
                self.en_cours = False

    def mettre_à_jour(self): 
        global score
        self.lame.mettre_à_jour(pygame.mouse.get_pos())

        fruits_a_supprimer = []

        for fruit in self.fruits:
            fruit.bouger()
            # Si le fruit sort de l'écran par le bas, on le marque comme à supprimer
            if fruit.y >= HAUTEUR + fruit.rayon:
                fruits_a_supprimer.append(fruit)

            if not fruit.coupé and fruit.est_touché(pygame.mouse.get_pos()):
                fruit.coupé = True

                if fruit.couleur == ROUGE:
                    self.en_cours = False  
                elif fruit.couleur == VERT:
                    score += 1  
                elif fruit.couleur == BLEU:
                    score += 2  
                elif fruit.couleur == JAUNE:
                    score += 3

                fruits_a_supprimer.append(fruit)  

        for fruit in fruits_a_supprimer:
            self.fruits.remove(fruit)

        self.timer_ajout += 1
        if self.timer_ajout > 30:  
            self.ajouter_fruit()
            self.timer_ajout = 0 

    def dessiner(self):
        écran.fill(NOIR)  # Changez ici pour modifier la couleur de fond
        self.lame.dessiner()

        for fruit in self.fruits:
            fruit.dessiner()

        texte_score = defaut_police.render(f"Score : {score}", True, BLANC)
        écran.blit(texte_score, (10, 10))

        pygame.display.flip()

    def exécuter(self):
        global score
        while self.en_cours:
            self.gérer_événements()
            self.mettre_à_jour()
            self.dessiner()
            horloge.tick(FPS)

        enregistrer_score(score)  # Enregistrer le score après la fin de la partie

if __name__ == "__main__":
    jeu = JeuFruitNinja()
    jeu.exécuter()
    pygame.quit()
    sys.exit()
