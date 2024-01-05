import re


class Converter:
    @staticmethod
    def extract_number_from_string(string: str | int) -> int:
        extracted_int = re.search(r'\d+', str(string)).group()
        return int(extracted_int)
