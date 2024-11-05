# Nom du fichier à lire
file_path = "hello.txt"

# Lit et affiche le contenu du fichier
with open(file_path, "r") as file:
    content = file.read()
    print(content)
