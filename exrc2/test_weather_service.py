import pytest
from weather_service import get_weather_data, get_temperature,is_sunny


def test_get_weather_data(mocker):
    mock_get = mocker.patch("weather_service.requests.get")
    mock_response = mock_get.return_value
    city = "paris"
    expected = {
        "city": "paris",
        "temperature": 25
    }
    mock_response.json.return_value = expected

    got = get_weather_data(city=city)
    mock_get.assert_called_once_with(f"http://api.weather.com/v1/weather?city={city}")
    assert got == expected

def test_get_temperature (mocker):
    mock_get_data = mocker.patch("weather_service.get_weather_data", return_value={
        "city": "paris",
        "temperature": 25
    })
    expected = 25

    got = get_temperature("paris")
    assert got ==expected
    
def test_is_sunny(mocker):
    mock_get_weaterdata = mocker.patch("weather_service.get_weather_data", return_value={"temperature": 25 ,"condition":"sunny"})
    
    result = is_sunny("paris")
    mock_get_weaterdata.assert_called_once_with("paris")
    assert result is True

def test_is_not_sunny(mocker):
    mocker.patch("weather_service.get_weather_data", return_value={"temperature": 4 ,"condition":"not_sunny"})
    
    result = is_sunny("nice")
    assert result is False