import re


def validiraj_email(email):
    
    regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    
   
    if re.match(regex, email):
        return True
    else:
        return False


email_adrese = [
    "test@example.com",
    "user.name+tag+sorting@example.com",
    "user_name@sub.example.co.uk",
    "invalid-email@",
    "another.invalid@.com"
]

for email in email_adrese:
    if validiraj_email(email):
        print(f"{email} je validna email adresa.")
    else:
        print(f"{email} nije validna email adresa.")