import os
import sys  # On importe sys pour pouvoir arrêter le script proprement
from dotenv import load_dotenv

load_dotenv()

def get_config(key_name, is_required=False):
    """
    Récupère une valeur de configuration en priorité depuis :
    1. Les variables d'environnement système
    2. Le fichier .env

    Si is_required=True et que la clé n'est pas trouvée, 
    le programme s'arrête avec une erreur.
    """
    value = os.environ.get(key_name)

    # C'est ici que ma nouvelle logique intervient
    if value is None and is_required:
        print(f"Attention Critique: La variable d'environnement obligatoire '{key_name}' n'est pas définie.", file=sys.stderr)
        sys.exit(1) # Arrête mon script avec un code d'erreur

    return value


#  Zone de test (Maj)
print("-Test de notre Gardien de Secrets (v2)")

# Test 1 : Clé obligatoire qui existe (depuis .env)
print("Test 1 (Clé obligatoire OK):")
api_key = get_config('API_KEY', is_required=True)
print(f"   -> API Key trouvée: {api_key}\n")


# Test 2 : Clé optionnelle qui n'existe pas (comportement normal)
print("Test 2 (Clé optionnelle KO):")
optional_key = get_config('CLE_INCONNUE', is_required=False) 
print(f"   -> ma Clé optionnelle: {optional_key}\n")


# Test 3 : Clé obligatoire qui n'existe pas (cense planter mon script)
print("Test 3 (Clé obligatoire KO):")
print("   -> Le script va maintenant tenter de charger mon 'DB_TOKEN' (qui n'existe pas)...")
db_token = get_config('DB_TOKEN', is_required=True)

# Si le script arrive ici, c'est que le test 3 a échoué (ce qui ne devrait pas)
print(f"   -> Attention: Mon script n'a pas dû s'arrêter. {db_token}")
print("fin :)")