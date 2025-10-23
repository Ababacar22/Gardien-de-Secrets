import os
from dotenv import load_dotenv # On aura besoin de cette bibliothèque

# Cette ligne est magique :
# Elle va chercher un fichier .env et charger ses valeurs
# dans les variables d'environnement (os.environ)
# MAIS elle ne va PAS écraser les variables déjà existantes !
load_dotenv()

def get_config(key_name):
    """
    Récupère une valeur de configuration en priorité depuis :
    1. Les variables d'environnement système
    2. Le fichier .env
    """
    # C'est ici qu'on va écrire notre logique
    value = os.environ.get(key_name)
    return value


# ma Zone de test 
print("-Test de notre Gardien de Secrets")

print(f"User (depuis .env): {get_config('DB_USER')}")
print(f"Password (depuis .env): {get_config('DB_PASSWORD')}")
print(f"Cle non existante (devrait etre 'None'): {get_config('CLE_INCONNUE')}")

print("Fin :)")