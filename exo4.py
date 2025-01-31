secondes = int(input("Entrez un nombre de secondes : "))

# Ne pas modifier.
annees = semaines = jours = heures = minutes = 0

# TODO: Assigner à la variable "annees" le nombre d'années
annees, reste_annees_en_secondes = divmod(secondes, 31536000)

# TODO: Assigner à la variable "semaines" le nombre de semaines restantes
semaines, reste_semaines_en_secondes = divmod(reste_annees_en_secondes, 604800)

# TODO: Assigner à la variable "jours" le nombre de jours restants
jours, reste_jours_en_secondes = divmod(reste_semaines_en_secondes, 86400)

# TODO: Assigner à la variable "heures" le nombre d'heures restantes
heures, reste_heures_en_secondes = divmod(reste_jours_en_secondes, 3600)

# TODO: Assigner à la variable "minutes" le nombre de minutes restantes
minutes, reste_minutes_en_secondes = divmod(reste_heures_en_secondes, 60)

# TODO: Assigner à la variable "secondes" le nombre de secondes restantes
secondes = reste_minutes_en_secondes

# TODO: Afficher le nombres d'années, semaines, jours, heures, minutes et secondes
print(annees, "années,", semaines, "semaines,", jours, "jours,", heures, "heures,", minutes, "minutes et", secondes, "secondes")
