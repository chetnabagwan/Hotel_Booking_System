import re

def is_valid_phone_number(phone_number):
    # Define the regular expression pattern for a 10-digit phone number
    pattern = re.compile(r'^\d{10}$')

    # Use the search function to check if the phone number matches the pattern
    match = pattern.search(phone_number)

    # If there is a match, the phone number is valid
    return bool(match)

# Example usage:
phone_number = "123457890"
if is_valid_phone_number(phone_number):
    print(f"{phone_number} is a valid phone number.")
else:
    print(f"{phone_number} is not a valid phone number.")
