from PIL import Image
from traitement_image import cadre, couleur_moyenne
from time import time
from multiprocessing import Process

def charger_images():
    liste_images = []
    for i in range(1, 21):
        liste_images.append(Image.open('U:/github/gestion_process-1/Scripts/Exercice_7/'+str(i)+'.jpg'))
    return liste_images
    
def traiter_les_images(debut, fin):
    liste_images = charger_images()
    liste_images_retravaillees = []
    
    for img in liste_images[debut : fin]:
        imageRetravaille = cadre(img)
        imageRetravaille.show() 
        liste_images_retravaillees.append(imageRetravaille)
    return liste_images_retravaillees
 
if __name__ == '__main__':
    Début = time()
    p1 = Process(target=traiter_les_images, args=(1,10,))
    p2 = Process(target=traiter_les_images, args=(11,21,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print(time()- Début)