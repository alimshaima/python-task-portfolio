# Email Validator
def validate_email(email):
    if "@" not in email:
        return False
    username, domain = email.split("@")
    if username == "" or domain == "":
        return False
    if "." not in domain or domain.startswith(".") or domain.endswith("."):
        return False
    return True

email = input("Enter email to validate: ")
if validate_email(email):
    print("Valid email address")
else:
    print("Invalid email address")
