from threading import Thread

def hello(n):
    for i in range(5):
        print ("Je suis le thread", n, "et ma valeur est", i)
    print ("------ Fin du Thread ", n)

for n in range(4):
    t = Thread(target=hello, args = (n,))
    t.start()