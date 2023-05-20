import pygame
import os
import sys

pygame.init()

fond = pygame.image.load("circuit.png")
couleur_de_la_bordure = (0, 0, 0, 0)
class Voiture :
    def __init__(self):
        largeur_voiture = 50
        longueur_voiture = 50
        self.corps = pygame.image.load("voiture.png")
        self.corps = pygame.transform.scale(self.corps, (largeur_voiture, longueur_voiture))
        self.centre = [self.position[0] + largeur_voiture / 2, self.position[1] + longueur_voiture / 2]
                                            
        self.position = (0,0)
        self.angle = 0
        self.vitesse = 0
    
    def affichage(self , ecran):
        pygame.ecran.blit(self.corps,self.position)
    
    def collision(self, fond):
        self.alive = True
        for point in self.coins:
            # If Any Corner Touches Border Color -> Crash
            # Assumes Rectangle
            if fond.get_at((int(point[0]), int(point[1]))) == couleur_de_la_bordure:
                self.alive = False
                break

    def update(self):
        self.position[0] += math.cos(math.radians(360 - self.angle)) * self.vitesse
        self.position[1] += math.sin(math.radians(360 - self.angle)) * self.vitesse
        self.centre = [int(self.position[0]) + longueur / 2, int(self.position[1]) + largeur / 2]
        self.check_collision(fond)
        # coin a calculer pour ensuite gérer les collisions
    
def main():
    largeur = 1920
    hauteur = 1080
    ecran = pygame.display.set_mode((largeur, hauteur))
    pygame.transform.scale(fond, (largeur, hauteur))
    while True:
        for evenement in pygame.event.get():
            if evenement.type == pygame.QUIT:
                pygame.quit()
                exit()

        ecran.blit(fond,(0,0))

        pygame.display.flip()
                                            
                    
    

'''         if :
                car.angle += 10 
            elif :
                car.angle -= 10 
            elif choice :
                if(car.vitesse - 2 >= 12):
                    car.vitesse -= 2 
            else:
                car.vitesse += 2 '''
# condition a choisir avec neat à priori

