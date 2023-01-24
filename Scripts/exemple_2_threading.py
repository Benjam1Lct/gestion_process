from random import randint
from sys import stdout
from time import sleep
from threading import Thread, Lock

verrou = Lock()

class Afficheur(Thread):

    """Thread chargé simplement d'afficher une lettre dans la console."""

    def __init__(self, mot):
        Thread.__init__(self)
        self.mot = mot

    def run(self):
        """Code à exécuter pendant l'exécution du thread."""
        global verrou
        i = 0
        while i < 5:
            verrou.acquire()
            for lettre in self.mot:
                stdout.write(lettre)
                stdout.flush()
                attente = 0.2
                attente += randint(1, 60) / 100
                sleep(attente)
            verrou.release()
            i += 1
        

# Création des threads
thread_1 = Afficheur("canard")
thread_2 = Afficheur("TORTUE")

# Lancement des threads
thread_1.start()
thread_2.start()

# Attend que les threads se terminent
thread_1.join()
thread_2.join()
