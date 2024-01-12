import re


def has_valid_link(url: str) -> bool:
    regex = r"http[s]?:\/{2}[wW]?\.?[\w-].+\.\w{2,}+"
    return bool(re.match(regex, url))
