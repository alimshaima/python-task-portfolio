# Password Strength Checker
def check_password(pwd):
    score = 0
    if len(pwd) >= 8: score += 1
    if any(c.isupper() for c in pwd): score += 1
    if any(c.islower() for c in pwd): score += 1
    if any(c.isdigit() for c in pwd): score += 1
    if any(c in "!@#$%^&*()" for c in pwd): score += 1
    
    if score == 5:
        return "STRONG"
    elif score >= 3:
        return "MEDIUM"
    else:
        return "WEAK"

pwd = input("Enter password: ")
print(f"Strength: {check_password(pwd)}")
