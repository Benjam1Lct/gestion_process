#le programme peut afficher un nombre plus petit que 200000
from threading import Thread
from time import sleep

def incr():
    global compteur
    for _ in range(10**5):
        compteur += 1        

compteur = 0
thread_1 = Thread(target = incr, args = ())
thread_2 = Thread(target = incr, args = ())
thread_1.start()
thread_2.start()

"""while thread_1.is_alive() and thread_2.is_alive():
    sleep(1)"""

thread_1.join()
thread_2.join()



print("valeur finale", compteur)
