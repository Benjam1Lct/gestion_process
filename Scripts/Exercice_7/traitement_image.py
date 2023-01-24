from PIL import Image
# coding: utf-8

def couleur_moyenne(img):
    """
    précondiitons : img est une image non vide
    psot conditions : couleur moyenne tuple de trois entiers entre 0 et 255
    calcule et renvoie la couleur moyenne de l'image img passée en paramètres
    """
    largeur, hauteur = img.size # largeur et hauteur en pixels de l’image
    somme_composante = [0, 0, 0] # initialisation de la somme des composantes de chaque couleur
    # parcours de chaque pixel de l'image
    for x in range(largeur):
        for y in range(hauteur):
            pixel = img.getpixel((x, y))
            # ajout de chaque composante du pixel à la composante correspondante de somme_composante
            for i in range(3):
                somme_composante[i] += pixel[i]
    #calcul de la couleur moyenne
    couleur_moyenne = (int(somme_composante[0]/(hauteur * largeur)), \
                       int(somme_composante[1]/(hauteur * largeur)), \
                       int(somme_composante[2]/(hauteur * largeur)))
    return couleur_moyenne

def cadre(img):
    bord = 50 # épaisseur de la future bordure

    # couleur RVB des pixels de la future bordure
    # appel à la fonction couleur_moyenne
    
    pixelbord = couleur_moyenne(img) 
    
    largeur, hauteur = img.size # largeur et hauteur en pixels de l’image

    lf = largeur + 2 * bord # largeur de l’image avec bordure
    hf = hauteur + 2 * bord # hauteur de l’image avec bordure

    imageBut = Image.new( "RGB", (lf, hf)) # ouverture d’une nouvelle image

    # on commence d’abord par recopier l’image dans le nouveau fichier
    # en tenant compte des décalages dus aux bords que l’on va ajouter :
    for y in range (hauteur) : # pour chaque ligne du fichier source
        for x in range (largeur) : #pour chaque colonne du fichier source
            p = img.getpixel((x, y)) # code du pixel source
            imageBut.putpixel((x + bord, y + bord), p) # création du pixel correspondant dans la nv

    # les boucles qui suivent correspondent aux bordures haute, basse, droite, gauche.
    for y in range (bord) :
        for x in range (lf) :
            imageBut.putpixel((x, y), pixelbord)

    for y in range (hauteur + bord, hf):
        for x in range (lf) :
            imageBut.putpixel((x ,y), pixelbord)

    for x in range (bord) :
        for y in range (hf) :
            imageBut.putpixel((x, y), pixelbord)

    for x in range (largeur+bord, lf) :
        for y in range (hf) :
            imageBut.putpixel((x, y), pixelbord)
    return imageBut

def traitement(nom_img):
    imageSource=Image.open(nom_img) # ouverture de l’image
    return cadre(imageSource)
    
if __name__ == '__main__':
    imageBut = traitement('U:/github/gestion_process-1/Scripts/Exercice_7/1.jpg')
    imageBut.show() # affichage de l’image

