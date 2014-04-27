import pygame
from pygame.locals import *

pygame.init()

def Somme(morpion):
	somme = 0
	for k in range(3):
		somme = 0
		for l in range(3):
			somme += morpion[k][l]
			if somme == 3:
				return 1
			if somme == -3:
				return -1

	for l in range(3):
		somme = 0
		for k in range(3):
			somme += morpion[k][l]
			if somme == 3:
				return 1
			if somme == -3:
				return -1

	somme = morpion[0][0] + morpion[1][1] + morpion[2][2]

	if somme == 3:
		return 1
	if somme == -3:
		return -1

	somme = morpion[0][2] + morpion[1][1] + morpion[2][0]

	if somme == 3:
		return 1
	if somme == -3:
		return -1



fenetre = pygame.display.set_mode((300, 400))

fond = pygame.image.load("background.jpg").convert()
fenetre.blit(fond, (0,0))

font = pygame.font.Font(None,90)

fenetre.blit(font.render("Menu", 1, (255,0,0)), (0,0))
fenetre.blit(font.render("1 joueur", 1, (255,0,0)), (0,100))
fenetre.blit(font.render("2 joueurs", 1, (255,0,0)), (0,200))
fenetre.blit(font.render("Quitter", 1, (255,0,0)), (0,300))

pygame.display.flip()

menu = 1

#Affichage du menu
while menu:
	for event in pygame.event.get():   #On parcours la liste de tous les événements reçus
		if event.type == QUIT:     #Si un de ces événements est de type QUIT
			menu = 0     #On arrête la boucle
		if event.type == MOUSEBUTTONDOWN and event.button == 1:
			if 100<event.pos[1]<200:
				continuer = 1
				joueurs = 1
				menu = 0
			if 200<event.pos[1]<300:
				continuer = 1
				joueurs = 2
				menu = 0
			if 300<event.pos[1]<400:
				continuer = 0
				menu = 0

#Chargement et collage du personnage
croix = pygame.image.load("croix.png").convert_alpha()
rond = pygame.image.load("rond.png").convert_alpha()


pygame.display.flip()

morpion = [[0,0,0],[0,0,0],[0,0,0]]

tour = 0

#Boucle infinie
while continuer:
	for event in pygame.event.get():   #On parcours la liste de tous les événements reçus
		if event.type == QUIT:     #Si un de ces événements est de type QUIT
			continuer = 0      #On arrête la boucle

		#Recheche de la cible du clic
		if event.type == MOUSEBUTTONDOWN and event.button == 1:
			#On recherche la collone k
			for k in range(3):
				if k*100 < event.pos[0] < (k+1)*100:
					#On recherche la ligne l
					for l in range(3):
						if l*100 < event.pos[1] < (l+1)*100:
							signe = morpion[k][l]
							#On met la croix ou le rond en fonction du tour
							if signe == 0:
								if tour % 2 == 0:
									morpion[k][l]=1
								else:
									morpion[k][l]=-1
								tour += 1

	if Somme(morpion) == 1:
		print "Cochon a gagné"
		morpion = [[0,0,0],[0,0,0],[0,0,0]]
		tour = 0
	if Somme(morpion) == -1:
		print "Vache a gagné"
		morpion = [[0,0,0],[0,0,0],[0,0,0]]
		tour = 0
	if tour == 9:
		print "egalité"
		tour = 0
		morpion = [[0,0,0],[0,0,0],[0,0,0]]

	#Affichage du tableau de jeu de morpion
	fenetre.blit(fond, (0,0))
	for i,col in enumerate(morpion):
		for j,ligne in enumerate(col):
			if ligne == 1:
				fenetre.blit(croix,(i*100,j*100))
			if ligne == -1:
				fenetre.blit(rond,(i*100,j*100) )
	pygame.display.flip()

