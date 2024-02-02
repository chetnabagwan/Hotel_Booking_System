import re

from .config_class import Config
class InputValidations:

    @staticmethod
    def password_validator(password):

        """Validates the password entered whether it meets the password requirements or not."""
        pat = re.compile(Config.PWD_REGEX)
        ans = re.search(pat,password)
        return bool(ans)


    @staticmethod
    def gen_validator(input):
        
        """Validates the input entered."""
        pat = re.compile(Config.GEN_REGEX)
        ans = re.match(pat,input)
        return bool(ans)
    
        
    @staticmethod
    def phone_number_validator(input):
        pattern = re.compile(Config.PHONE_NUMBER_REGEX)
        match = pattern.search(input)
        return bool(match)

       
