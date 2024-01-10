import re


class Converter:
    @staticmethod
    def extract_number_from_string(string: str | int) -> int:
        extracted_int = "".join(re.findall(r"\d+", str(string)))
        return int(extracted_int)
