import math

# Constante de gravité
g = 9.8

# Demander la vitesse initiale de la boule
vitesse = float(input("Vitesse initiale (en m/s):\n"))

# Demander l'angle de lancement
angle_en_degre = float(input("Angle de lancer (en degrés):\n"))

# Convertir l'angle en radians
angle_en_radians = angle_en_degre * (math.pi/180)

# Calculer la distance maximale en x
distance_max_x = ((vitesse**2) * (math.sin(2*angle_en_radians)))/g

# Afficher la distance maximale arrondie à 2 chiffres après la virgule
print(str(round(distance_max_x, 2)) + "m")

# Exemple:
# Pour une vitesse initiale de 10 m/s et un angle de 45 degrés
# La distance parcourue serait de 10.20m
