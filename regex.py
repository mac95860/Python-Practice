#email address text scraper

import re

text = "A123 random string. mike123@email.com some more text. Your_Name.8-88@company.net"
pattern = re.compile("[a-zA-Z0-9\.\-\_\!\%]+@[a-zA-Z0-9]+\.+[a-zA-Z]+")
result = pattern.findall(text)
print(result)