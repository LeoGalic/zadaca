import re


def validiraj_email(email):
    email_regex = r'^[a-zA-Z]+\.[a-zA-Z]+@fpmoz\.sum\.ba$'
    return re.match(email_regex, email) is not None


def validiraj_eduid(eduid):
    eduid_regex = r'^[a-zA-Z][a-zA-Z]+[0-9]*@sum\.ba$'
    return re.match(eduid_regex, eduid) is not None

email = input("Unesite e-mail adresu (ime.prezime@fpmoz.sum.ba): ")
eduid = input("Unesite eduId (iprezimeX@sum.ba): ")


if validiraj_email(email):
    print(f"E-mail adresa '{email}' je validna.")
else:
    print(f"E-mail adresa '{email}' nije validna.")

if validiraj_eduid(eduid):
    print(f"eduId '{eduid}' je validan.")
else:
    print(f"eduId '{eduid}' nije validan.")