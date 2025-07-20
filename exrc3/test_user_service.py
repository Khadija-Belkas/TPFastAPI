import pytest
from unittest.mock import patch
from user_service import create_user, hash_password

@pytest.fixture
def mock_generate_password():
    with patch("user_service.generate_password", return_value="passfixe1") as mock:
        yield mock  # on retourne le mock au test
        
def test_create_user(mock_generate_password):
    user = create_user("khadi", "khadi@example.com")

    # Vérifie que le mot de passe brut est celui de la fixture
    assert user["raw_password"] == "passfixe1"

    # Vérifie que le mot de passe hashé correspond bien
    assert user["password"] == hash_password("passfixe1")

    # Vérifie les autres champs
    assert user["username"] == "khadi"
    assert user["email"] == "khadi@example.com"

    # Vérifie que la fonction mockée a été appelée une fois
    mock_generate_password.assert_called_once()