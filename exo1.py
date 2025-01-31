# Demander le nom complet de l'utilisateur
nom_utilisateur = input("Veuillez entrer votre nom complet :\n")

# Demander l'âge de l'utilisateur
age_utilisateur = int(input("Veuillez entrer votre âge :\n"))

# Définir l'année actuelle
annee_actuelle = 2025
# Calculer l'année de naissance
annee_naissance = annee_actuelle - age_utilisateur

# Afficher un message de bienvenue avec le nom complet
print("Bonjour", nom_utilisateur)

# Afficher l'année de naissance
print("Vous êtes né(e) en", annee_naissance)
