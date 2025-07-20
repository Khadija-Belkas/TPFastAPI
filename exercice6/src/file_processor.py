import os
import json
from pathlib import Path

def read_file(filepath):
    """Lit un fichier et retourne son contenu"""
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Le fichier {filepath} n'existe pas")
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()

def write_file(filepath, content):
    """Écrit du contenu dans un fichier"""
    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(content)

def process_config_file(config_path):
    """Traite un fichier de configuration JSON"""
    try:
        content = read_file(config_path)
        config = json.loads(content)
        # Valider la configuration
        if 'database' not in config:
            raise ValueError("Configuration 'database' manquante")
        return config
    except json.JSONDecodeError:
        raise ValueError("Format JSON invalide")

def backup_file(source_path, backup_path):
    """Sauvegarde un fichier"""
    content = read_file(source_path)
    write_file(backup_path, content)
    return f"Fichier sauvegardé de {source_path} vers {backup_path}"
