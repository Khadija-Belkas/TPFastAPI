
import pytest
from src.file_processor import process_config_file
from tests.units.mocks.file_content_mock import file_content, unvalide_content_with_no_database,unvalide_json_content_file

def test_process_config_file_valide_content(mock_read_file):
    
    expected = {"database": "mydb", "k": "v"}
    got = process_config_file("/1")
    mock_read_file.assert_called_once_with("/1")
    assert got == expected

def test_process_config_file_no_database(mock_read_file):
   
    with pytest.raises(ValueError, match="Configuration 'database' manquante"):
        process_config_file("/2")
    mock_read_file.assert_called_once_with("/2")
def test_process_config_file_unvalid_f_json(mock_read_file):
    with pytest.raises(ValueError,match="Format JSON invalide"):
        process_config_file("/3")

def test_process_config_file_not_found(mock_read_file):

    with pytest.raises(FileNotFoundError, match=f"Le fichier /not_found n'existe pas"):
        
        process_config_file("/not_found")
    mock_read_file.assert_called_once_with("/not_found")
