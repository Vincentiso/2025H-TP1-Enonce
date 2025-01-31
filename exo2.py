# Demandez à l'utilisateur d'entrer le niveau de charge actuel de la batterie
niveau_charge_actuel = float(input("Entrez le niveau de charge actuel de la batterie :\n"))

# Vérifiez si le niveau de charge est valide
if 0 <= niveau_charge_actuel <= 100:
    

# Arrondir le pourcentage à la dizaine la plus proche
    niveau_charge_actuel_arrondie = round(niveau_charge_actuel)


# Calculer le nombre de barres
    nombre_barre = round(niveau_charge_actuel_arrondie/10) * "❚"
    nombre_barre_vide = (10 - round(niveau_charge_actuel_arrondie/10)) * " "

# Afficher la représentation graphique de la charge de la batterie
    print("[" + str(nombre_barre) + str(nombre_barre_vide) + "]")
    print(niveau_charge_actuel_arrondie, "%")

else:
    print("Erreur : niveau de charge invalide.")

# Exemple d'utilisation :
# Si l'utilisateur entre 76, la sortie sera :
# [❚❚❚❚❚❚❚❚     ]
# 76%