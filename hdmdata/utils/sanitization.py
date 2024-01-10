import re
import string
from unidecode import unidecode


def sanitize_string(value: int | str | float) -> str:
    """Remove accents and special characters from a string."""
    new_value = unidecode(str(value))
    return re.sub(rf"[{string.punctuation}]", "", new_value).strip()
