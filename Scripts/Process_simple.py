"""Process : simple utilisation"""

from multiprocessing import Process
from os import getpid
from time import sleep

def ecriture():
    pid = str(getpid())
    with open("test.txt", "w") as fichier:
        for i in range(10**3):
            fichier.write("{} : {}\n".format(pid, i))
            fichier.flush()
            sleep(0.1)

if __name__ == '__main__':
    p1 = Process(target = ecriture, args = ())
    p2 = Process(target = ecriture, args = ())
    p3 = Process(target = ecriture, args = ())
    p1.start()
    p2.start()
    p3.start()
    p1.join()
    p2.join()
    p3.join()
    



