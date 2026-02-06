import string

def check_password_strength(password):
    has_upper = False
    has_lower = False
    has_digit = False
    has_symbol = False

    for ch in password:
        if ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch.isdigit():
            has_digit = True
        elif ch in string.punctuation:
            has_symbol = True

    missing = []
    if not has_upper:
        missing.append("Uppercase letter")
    if not has_lower:
        missing.append("Lowercase letter")
    if not has_digit:
        missing.append("Number")
    if not has_symbol:
        missing.append("Symbol")

    score = 0
    if has_upper: score += 1
    if has_lower: score += 1
    if has_digit: score += 1
    if has_symbol: score += 1

    if score <= 1:
        strength = "Weak"
    elif score == 2 or score == 3:
        strength = "Medium"
    else:
        strength = "Strong"

    return strength, missing
print("🔐 Password Strength Checker")
print("-----------------------------")

password = input("Enter your password: ")

strength, missing_conditions = check_password_strength(password)

print(f"\nPassword Strength: {strength}")

if missing_conditions:
    print("Missing conditions:")
    for item in missing_conditions:
        print(f"- {item}")
else:
    print("✔ Password meets all conditions")