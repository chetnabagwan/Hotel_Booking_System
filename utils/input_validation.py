import re
import logging
from datetime import datetime 
from .config_class import Config

class InputValidations:

    @staticmethod
    def password_validator(password):

        """Validates the password entered whether it meets the password requirements or not."""

        pat = re.compile(Config.PWD_REGEX)
        answer = re.search(pat,password)
        
        if answer is not None:
            return True
        else:
            return False

    @staticmethod
    def gen_validator(input):
        
        """Validates the input entered."""
        pat = re.compile(Config.GEN_REGEX)
        ans = re.match(pat,input)
        if ans is not None:
            return True
        else:
            return False
def password_validation(password):
    reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
    pat = re.compile(reg)
    answer = re.search(reg,password)
    
    if answer is not None:
        return True
    else:
        return False
    
#print(password_validation("Cht1@"))
