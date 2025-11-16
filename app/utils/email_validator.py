import re
def validate_email(e):
    return bool(re.match(r"^[A-Za-z0-9._%-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$", e))