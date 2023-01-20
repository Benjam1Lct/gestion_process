from PIL import Image
from traitement_image import cadre, couleur_moyenne
from time import time

def charger_images():
    liste_images = []
    for i in range(1, 21):
        liste_images.append(Image.open(str(i)+'.jpg'))
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
    traiter_les_images(1, 21)
    print(time()- Début)