from __future__ import absolute_import
from __future__ import print_function
from unittest.mock import patch
from voipms.api import Client
from unittest.mock import MagicMock

import credentials


def test_instantiation():
    username = credentials.username
    password = credentials.password

    client = Client(username, password)
    return client


@patch('voipms.api.general.balance')
def test_make_get_request(mock_requests):
    mock_response_obj = MagicMock()
    mock_response_obj.json = {"test": "test"}
    mock_response_obj.status_code = 200
    mock_requests.get.return_value = mock_response_obj

    username = credentials.username
    password = credentials.password

    client = Client(username, password)

    res = client.registration_status.fetch()
    assert res == {"test": "test"}
