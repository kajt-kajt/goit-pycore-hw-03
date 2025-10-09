import re

def normalize_phone(phone_number:str) -> str:
    """
    Normalize phone number, output format is +380NNNNNNNNN

    If country code is not provided, number is assumed to be from Ukraine.

    Parameters:
        phone_number (str): string containing digits of phone number with any separators

    Returns:
        str: normalized phone number in format +380NNNNNNNNN
    """

    # 1. Let's remove all non-digit characters
    result = re.sub(r"[^\d]", "", phone_number)
    # 2. Let's process country code
    if len(result) == 9:
         result = "380" + result
    if len(result) == 10:
         result = "38" + result
    return ("+" + result)


