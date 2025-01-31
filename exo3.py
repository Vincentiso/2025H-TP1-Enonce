import math

a = int(input("Entrez a, non nul: "))
b = int(input("Entrez b: "))
c = int(input("Entrez c: "))

# Calculer le discriminant et assigner la valeur dans la variable "delta"
delta = (b**2) - (4*a*c)

# Déterminer la condition (bool) qui correspond à aucune solution de l'équation et mettre la valeur dans la variable "naPasDeSolution"
if delta < 0:
    naPasDeSolution = True

    if naPasDeSolution:
        # ces ligne de code seront executé si il y'a aucune racine
        # afficher sur l'écran "Aucune racine"
        print("Aucune racine")
    
else:
    # Déterminer la condition (bool) qui correspond à une unique solution de l'équation et mettre la valeur dans "aUneSeuleSolution"
    if delta == 0:
        aUneSeuleSolution = True

        if aUneSeuleSolution:
            # ces ligne de code seront executé si il y'a une seule racine
            # afficher sur l'écran "Une seule racine"
            print("Une seule racine")
            # assigner a la variable x1 la valeur de la racine
            x1 = ((-1*b)-(delta**(1/2)))/(2*a)
            print(x1)
        
    else:
        # Déterminer la condition (bool) qui correspond à deux solutions de l'équation et mettre la valeur dans "aDeuxSolutions"
        if delta > 0:
            aDeuxSolutions = True

            if aDeuxSolutions:
                # afficher sur l'écran "Deux racines"
                print("Deux racines")
                # calculer la prmiere racine, assigner la a "x1"
                x1 = ((-1*b)-(delta**(1/2)))/(2*a)
                # calculer la deuxieme racine, assigner la a "x2"
                x2 = ((-1*b)+(delta**(1/2)))/(2*a)
                print(x1, x2)
            

# Exemple d'utilisation:
# Pour a = 1, b = -3, c = 2
# delta = 1
# Deux racines
# x1 = 1.0, x2 = 2.0
