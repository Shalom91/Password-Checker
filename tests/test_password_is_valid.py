from password_checker import password_is_valid
import pytest

# Testing for each condition of password_is_valid
def test_password_is_valid():
    with pytest.raises(Exception) as e:
        assert password_is_valid("")
    assert str(e.value) == "password should exist"

    with pytest.raises(Exception):
        assert password_is_valid("molash") == Exception("password must be longer than 8 characters")
        assert password_is_valid("MOLASH") == Exception("password must have at least one lowercase letter")
        assert password_is_valid("molash") == Exception("password must have at least one uppercase letter")
        assert password_is_valid("Molashxyz!") == Exception("password must have at least one digit")
        assert password_is_valid("Molashxyz4") == Exception("password must have at least one special character")
        
    assert password_is_valid("Molash@91") == True