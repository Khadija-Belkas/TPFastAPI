import pytest
from exer6 import backup_file
from exer6.le_processor import backup_file,process_config_file

def test_process_config_file_valid(mock_read_file):
    # Simule un fichier JSON valide avec la clé 'database'
    mock_read_file.return_value = '{"database": "sqlite", "user": "admin"}'
    
    config = process_config_file("dummy_path.json")
    
    assert isinstance(config, dict)
    assert config["database"] == "sqlite"
def test_process_config_file_invalid_json(mock_read_file):
    # Simule un contenu non JSON (provoque JSONDecodeError)
    mock_read_file.return_value = "ceci n'est pas un JSON"
    
    with pytest.raises(ValueError, match="Format JSON invalide"):
        process_config_file("dummy_path.json")
    

# Test : JSON valide mais sans la clé 'database'
def test_process_config_file_missing_database(mock_read_file):
    mock_read_file.return_value = '{"user": "admin"}'  # pas de clé "database"

    with pytest.raises(ValueError, match="Configuration 'database' manquante"):
        process_config_file("fake_config.json")


#  Test : JSON invalide
def test_process_config_file_invalid_json(mock_read_file):
    mock_read_file.return_value = "pas un json"  # contenu non JSON

    with pytest.raises(ValueError, match="Format JSON invalide"):
        process_config_file("fake_config.json")

