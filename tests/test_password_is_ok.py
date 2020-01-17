from password_checker import password_is_ok
import pytest

def password_is_ok(password):
    count = 0
# set conditions for the password
    if password != "":
        if len(password) > 8:
            if (any(i.islower() for i in password) or any(i.isupper() 
                for i in password) or any(i.isdigit() for i in password) 
                or any(i in special_symbols for i in password)):
                    count += 1
            else:
                pass
        else:
            raise Exception("Password is not OK if its less than 8 characters")
    else:
        raise Exception("Password is not OK if it is empty")
# when condtions are met, return true               
    if count == 1:
        return True
   
print(password_is_ok("ftttttttttttt"))