import pytest
from tests.unit.mocks.file_content_mock import user_not_found,error_user,user_inactive,user_valid 
from unittest.mock import patch

def test_login_user_not_found(mock_login_user):
    expected = {"status": "fail", "reason": "user_not_found"}
    got = login_user("/1")
    mock_login_user.assert_called_once_with("/1")
    assert got == expected 
def test_login_user_error_user(mock_login_user):
    expected = {"status": "error", "reason": "db_error"}
    got = login_user("/2")
    mock_login_user.assert_called_once_with("/2")
    assert got == expected 
