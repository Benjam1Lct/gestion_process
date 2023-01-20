from random import randint
from sys import stdout
from time import sleep

# Repete 20 fois
i = 0
while i < 20:
    stdout.write("1") #afficher le chiffre sur la sortie standard (l'écran, par défaut)
    stdout.flush()  #pour demander à Python d'afficher le chiffre tout de suite, sinon c'est à la fin d'exécution
    attente = 0.2
    attente += randint(1, 60) / 100 # on crée une variable attente et on la fait varier, grâce à random, entre 0.2 et 0.8
    # attente est à présent entre 0.2 et 0.8
    sleep(attente)
    i += 1
