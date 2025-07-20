import pytest 
from tests.units.mocks.side_effects.file_side_effect import file_side_effect


@pytest.fixture
def mock_read_file(mocker):
    return mocker.patch("src.file_processor.read_file", side_effect=file_side_effect)
