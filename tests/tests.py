from __future__ import absolute_import
from __future__ import print_function
from unittest.mock import patch
from voipms.api import Client
import credentials

try:
    from unittest.mock import MagicMock
except:
    from mock import MagicMock


def test_instantiation():
    """Test instantiation of NOAA class.
    """
    username = credentials.username
    password = credentials.password

    client = Client(username, password)
    return client

@patch('voipms.api.general.balance')
def test_make_get_request(mock_requests):
    mock_response_obj = MagicMock()
    mock_response_obj.json = {"test":"test"}
    mock_response_obj.status_code = 200
    mock_requests.get.return_value = mock_response_obj

    username = credentials.username
    password = credentials.password

    client = Client(username, password)

    res = client.registration_status.fetch()
    assert res == {"test": "test"}

# @patch('noaa_sdk.util.requests')
# def test_make_get_request_failed(mock_requests):
#     mock_response_obj = MagicMock()
#     mock_response_obj.text = 'mock text'
#     mock_response_obj.status_code = 500
#     mock_response_obj.json = lambda: {"test":"test"}
#     mock_requests.get.return_value = mock_response_obj

#     with pytest.raises(Exception) as err:
#         n = noaa.NOAA(user_agent='test_agent')
#         n.make_get_request('http://test')
#         assert err == 'Error: end_point is None.'


# @patch('noaa_sdk.noaa.NOAA.make_get_request')
# def test_points(mock_make_get_request):
#     mock_make_get_request.return_value = None
#     n = noaa.NOAA(user_agent='test_agent')
#     n.points('23.44,34.55')
#     mock_make_get_request.assert_called_with(
#         '/points/23.44,34.55', end_point=n.DEFAULT_END_POINT)


# @patch('noaa_sdk.noaa.NOAA.make_get_request')
# def test_points_with_stations(mock_make_get_request):
#     mock_make_get_request.return_value = None
#     n = noaa.NOAA(user_agent='test_agent')
#     n.points('23.44,34.55', stations=True)
#     mock_make_get_request.assert_called_with(
#         '/points/23.44,34.55/stations', end_point=n.DEFAULT_END_POINT)


# @patch('noaa_sdk.noaa.NOAA.make_get_request')
# def test_points_forecast(mock_make_get_request):
#     mock_make_get_request.return_value = {
#         'properties': {
#             'forecast': 'forecast_uri',
#             'forecastHourly': 'forecast_hourly_uri'
#         }
#     }
#     n = noaa.NOAA(user_agent='test_agent')
#     n.points_forecast(23.44, 34.55, hourly=False)
#     mock_make_get_request.assert_any_call(
#         uri='forecast_uri', end_point=n.DEFAULT_END_POINT)