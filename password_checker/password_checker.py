# Define special symbols
special_symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")",
"-", "_", "=", "+", " ", "`", "~", ",", "<", ".", ">", "?", "/", ";",
":", "'", '"', "|", "{", "}", "[", " \ ", "]"]

def password_is_valid(password):
    if password != "":
        #password length
        if len(password) >8:
            # password lowercase
            if any(i.islower() for i in password):
                # password uppercase
                if any(i.isupper() for i in password):
                    # password digit
                    if any(i.isdigit() for i in password):
                        # password special character
                        if any(i in special_symbols for i in password):
                            return True
                        
                        else:
                            raise Exception("password should have at least one special character")
                    else:
                        raise Exception("password should have at least one digit")
                else:
                    raise Exception("password should have at least one uppercase letter")
            else:
                raise Exception("password should have at least one lowercase letter")
        else:
            raise Exception("password should be longer than 8 characters")
    else:
        raise Exception("password should exist")

print(password_is_valid("111111111q1!S"))

#======================================= Password_is_ok ==============================================
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
