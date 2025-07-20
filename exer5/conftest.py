import pytest

from unittest.mock import AsyncMock

@pytest.fixture
def mock_asyncio_sleep(mocker):
 
    return mocker.patch("async_api_service.asyncio.sleep", return_value=AsyncMock())


@pytest.fixture
def user_data():
    return {
        'user_id': "user_id",
        'name': "name",
        'email': "email@gmail.com"
    }

@pytest.fixture
def mock_aiohttp_client_session(mocker, user_data):
    mock_response = AsyncMock()
    mock_response.json = AsyncMock(return_value=user_data)

    mock_get = mocker.MagicMock()
    mock_get.__aenter__.return_value = mock_response

    mock_session = mocker.MagicMock()
    mock_session.__aenter__.return_value = mock_session
    mock_session.get.return_value = mock_get

    with mocker.patch("async_api_service.aiohttp.ClientSession", return_value=mock_session):
        yield mock_session


@pytest.fixture
def mock_fetch_data(mocker, user_data):
    mock_fetch_data = mocker.patch("async_api_service.fetch_user_data", return_value=AsyncMock())
    mock_fetch_data.return_value = user_data
    return mock_fetch_data

@pytest.fixture
def mock_fetch_data(mocker, user_data):
    mock_fetch_data = mocker.patch("async_api_service.fetch_user_data", return_value=AsyncMock())
    mock_fetch_data.return_value = user_data
    return mock_fetch_data
@pytest.fixture
def user_name(mocker):
    return "name"

@pytest.fixture
def user_email(mocker):
    return "email@gmail.com"

@pytest.fixture
def mock_get_user_name(mocker,user_name):    
    mock_user_name= mocker.patch("async_api_service.get_user_name", return_value=AsyncMock())
    mock_user_name.return_value = user_name
    return mock_user_name

@pytest.fixture
def mock_get_user_email(mocker,user_email):    
    mock_user_email= mocker.patch("async_api_service.get_user_email", return_value=AsyncMock())
    mock_user_email.return_value = user_email
    return mock_user_email

