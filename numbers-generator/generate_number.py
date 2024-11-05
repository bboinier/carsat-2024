import random
import os

# Crée le répertoire "output" s'il n'existe pas
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)

# Génère un nombre aléatoire entre 1 et 10 000
random_number = random.randint(1, 10000)

# Écrit le nombre aléatoire dans le fichier "number.txt"
with open(f"{output_dir}/number.txt", "w") as file:
    file.write(str(random_number))

print(f"Le nombre {random_number} a été écrit dans {output_dir}/number.txt")
