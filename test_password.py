from password_checker import password_is_valid, password_is_ok
import pytest

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
#======================================= password_is_ok ==============================================

def test_password_is_ok():
    with pytest.raises(Exception):
        assert password_is_ok("") == Exception("Password is not OK if it is empty")

    with pytest.raises(Exception):
        assert password_is_ok("molash") == Exception("Password is not OK if its less than 8 characters")

    with pytest.raises(Exception):
        assert password_is_ok("jjjjjjjjjjj") == Exception
        assert password_is_ok("JJJJJJJJJJJ") == Exception
        assert password_is_ok("99999999999") == Exception
        assert password_is_ok("!@#$$%^&*()") == Exception
        assert password_is_ok("jjjjjjjjjjj") == Exception
        assert password_is_ok("jJjjjjjjjjj") == Exception
        assert password_is_ok("jjjJjjjjjj@1") == Exception

    assert password_is_ok("madk@kdfj") == True

