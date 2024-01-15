import re


class Converter:
    @staticmethod
    def extract_number_from_string(string: str | int) -> int:
        extracted_int = "".join(re.findall(r"\d+", str(string)))
        if not extracted_int:
            extracted_int = 0
        return int(extracted_int)
