# 🔒 Gardien de Secrets (Secure Config Loader)

Ce projet est un petit utilitaire Python pour charger des configurations et des secrets d'application de manière sécurisée.

Il respecte les bonnes pratiques de développement (notamment la [Méthodologie 12-Factor](https://12factor.net/fr/config)) en séparant la configuration (qui varie) du code (qui ne varie pas).

##  Fonctionnalités

- Charge les variables depuis l'environnement système en priorité (standard pour le Cloud, Docker, K8s).
- Charge les variables depuis un fichier `.env` en second (pour le développement local).
- Permet de définir des variables comme "obligatoires" et arrête proprement le script si elles manquent ("Fail-Fast").
- Empêche les secrets (le fichier `.env`) d'être "commités" sur Git grâce au `.gitignore`.

## 🛠️ Comment l'utiliser

1.  **Inclure le module** :
    Copiez `config_loader.py` dans votre projet.

2.  **Créer votre `.env` local** (Ne *jamais* le mettre sur Git !) :
    ```
    # Fichier .env
    DB_USER=votre_user
    DB_PASSWORD=votre_pass
    API_KEY=votre_cle_secrete_locale
    ```

3.  **Utiliser dans votre code** :
    Importez la fonction `get_config` au tout début de votre script principal.

    ```python
    # main.py
    from config_loader import get_config

    # Charger une clé obligatoire (le script plantera si elle manque)
    api_key = get_config('API_KEY', is_required=True)
    db_pass = get_config('DB_PASSWORD', is_required=True)

    # Charger une clé optionnelle (vaudra None si elle manque)
    debug_mode = get_config('DEBUG_MODE') # is_required=False par défaut

    print(f"Connexion avec l'API Key : {api_key[:4]}...")
    print(f"Connexion avec le mot de passe : {'*' * len(db_pass)}")

    if debug_mode:
        print("Mode debug activé.")
    ```

##  Principes de Sécurité

1.  **Priorité** : Variables d'Environnement Système > Fichier `.env`.
2.  **Sécurité Git** : Le fichier `.gitignore` doit *impérativement* contenir la ligne `.env`.

---

## ✍️ Auteur

Fait par Khalifa Ababacar DIALLO