import pytest

@pytest .fixture 
def mock_read_file(mocker):
    mocked = mocker.patch("exer6.le_processor.read_file")  # Remplace "your_module" par le nom réel du fichier (ex: "utils")
    return mocked

@pytest .fixture 
def mock_write_file(mocker):
    mocked =mocker.path("exer6.le_processor.write_file")
    return mocked
