import re

phoneNumberRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

matchingObject = phoneNumberRegex.search("Hello I am User 123A. My contact details are 123-789-4562 and 9874-562-2586")

print(matchingObject.group())