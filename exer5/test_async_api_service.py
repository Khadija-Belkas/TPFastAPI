import pytest
from async_api_service import fetch_user_data, get_user_name, get_user_email,get_user_profile

@pytest.mark.asyncio
async def test_fetch_user_data(mock_asyncio_sleep, mock_aiohttp_client_session, user_data):
    latence_reseau = 0.5
    user_id = "user_id"
    url = f"https://api.example.com/users/{user_id}"

    expected = user_data

    got = await fetch_user_data(user_id)

    mock_asyncio_sleep.assert_called_once_with(latence_reseau)
    mock_aiohttp_client_session.get.assert_called_once_with(url)
    assert got == expected


@pytest.mark.asyncio
async def test_get_user_name(mock_fetch_data, user_data):
    user_id = "user_id"
    expected = user_data.get("name") # name

    got = await get_user_name(user_id=user_id)

    mock_fetch_data.assert_called_once_with(user_id)
    assert got == expected

@pytest.mark.asyncio
async def test_get_user_unfound_name(mock_fetch_data):
    user_id = "user_id"
    expected = "Unknown"
    mock_fetch_data.return_value = {}

    got = await get_user_name(user_id=user_id)

    mock_fetch_data.assert_called_once_with(user_id)
    assert got == expected

@pytest.mark.asyncio
async def test_get_user_email(mock_fetch_data, user_data):
   
    user_id = "user_id"
    expected = user_data.get("email") # email

    got = await get_user_email(user_id=user_id)

    mock_fetch_data.assert_called_once_with(user_id)
    assert got == expected

@pytest.mark.asyncio
async def test_get_user_unfound_email(mock_fetch_data, user_data):
    mock_fetch_data.return_value = {}
    user_id = "user_id"
    expected = "no-email@example.com" # email

    got = await get_user_email(user_id=user_id)

    mock_fetch_data.assert_called_once_with(user_id)
    assert got == expected
@pytest.mark.asyncio
async def test_get_user_profile(mock_get_user_name,mock_get_user_email,user_data):
    user_id = "user_id"
    got = await get_user_profile(user_id=user_id)
    mock_get_user_name.assert_called_once_with(user_id)
    mock_get_user_email.assert_called_once_with(user_id)
    assert got == user_data