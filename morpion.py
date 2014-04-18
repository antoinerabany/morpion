import pygame
from pygame.locals import *

pygame.init()

fenetre = pygame.display.set_mode((300, 300))

fond = pygame.image.load("background.jpg").convert()
fenetre.blit(fond, (0,0))

#Chargement et collage du personnage
croix = pygame.image.load("croix.png").convert_alpha()
rond = pygame.image.load("rond.png").convert_alpha()


pygame.display.flip()

morpion = [[0,0,0],[0,0,0],[0,0,0]]

continuer = 1

#Boucle infinie
while continuer:
	for event in pygame.event.get():   #On parcours la liste de tous les événements reçus
		if event.type == QUIT:     #Si un de ces événements est de type QUIT
			continuer = 0      #On arrête la boucle

		if event.type == MOUSEBUTTONDOWN and event.button == 1:
			print event.pos
			for k in range(3):
				if k*100<event.pos[0]<(k+1)*100:
					#colonne = morpion.pop(k)
					print k
					for l in range(3):
						if l*100<event.pos[1]<(l+1)*100:
							#colonne = morpion.pop(k)
							#signe=colonne.pop(l)
							signe = morpion[k][l]
							print k,l
							if signe == 0:
								morpion[k][l]=1





			# if 0<event.pos[0]<100:
			# 	col = morpion.pop(0)
			# 	if 0<event.pos[1]<100:
			# 		i=col.pop(0)
			# 		if i!=0:
			# 			morpion = morpionSave
			# 		else:
			# 			col.insert(0,1)
			# 			morpion.insert(0,col)



	#Affichage du tableau de jeu de morpion
	fenetre.blit(fond, (0,0))
	for i,col in enumerate(morpion):
		for j,ligne in enumerate(col):
			if ligne == 1:
				fenetre.blit(croix,(i*100,j*100))
			if ligne == -1:
				fenetre.blit(rond,(i*100,j*100) )
	pygame.display.flip()