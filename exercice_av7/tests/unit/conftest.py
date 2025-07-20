import pytest 
from tests.unit.mocks.side_effects.file_side_effects import file_side_effect

@pytest .fixture
def mock_login_user(mocker):
    return mocker.patch("src.user.login_user",side_effect=file_side_effect)
