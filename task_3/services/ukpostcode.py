from typing import Optional
import re


class UKPostcode:
    def __init__(self, input_postcode: str):
        self.input_postcode = input_postcode

    def postcode_formatter(self) -> Optional[dict]:
        """
        Formats input UK postcode. Follows formatting convention as outlined:
        https://en.wikipedia.org/wiki/Postcodes_in_the_United_Kingdom#Formatting
        :param self.input_postcode: str - Between 6 and 9 characters including whitespace
        :return: dict - formatted postcode and outward/inward code segments.
        """
        if not 6 <= len(self.input_postcode) <= 9:
            return None

        else:
            postcode = self.input_postcode.upper()

            outward_code = postcode.replace(" ", "")[:-3]
            inward_code = postcode.replace(" ", "")[-3:]
            postcode = '{} {}'.format(outward_code, inward_code)

            return {'Postcode': postcode,
                    'Outward Code': outward_code,
                    'Inward Code': inward_code}

    def postcode_validator(self) -> bool:
        """
        Performs validation check of input UK postcode utilising regular expression check (including special cases)
        as defined: https://en.wikipedia.org/wiki/Postcodes_in_the_United_Kingdom#Validation
        :param self.input_postcode: str - Between 6 and 9 characters including whitespace
        :return: bool - indicating if formatted postcode is valid
        """
        formatted = self.postcode_formatter()

        if formatted is None:
            return False

        elif re.match(
                "^(([A-Z]{1,2}[0-9][A-Z0-9]?|ASCN|STHL|TDCU|BBND|[BFS]IQQ|PCRN|TKCA) ?[0-9][A-Z]{2}|BFPO ?[0-9]{1,"
                "4}|(KY[0-9]|MSR|VG|AI)[ -]?[0-9]{4}|[A-Z]{2} ?[0-9]{2}|GE ?CX|GIR ?0A{2}|SAN ?TA1)$",
                formatted['Postcode']) is None:
            return False

        else:
            return True
