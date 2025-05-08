import re

def check_strength(password):
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    symbol_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    score = 5 - sum([length_error, digit_error, uppercase_error, lowercase_error, symbol_error])

    if score == 5:
        strength = "Strong ✅"
    elif 3 <= score < 5:
        strength = "Medium ⚠️"
    else:
        strength = "Weak ❌"

    # Suggestions
    suggestions = []
    if length_error:
        suggestions.append("Use at least 8 characters")
    if digit_error:
        suggestions.append("Include at least one digit")
    if uppercase_error:
        suggestions.append("Include at least one uppercase letter")
    if lowercase_error:
        suggestions.append("Include at least one lowercase letter")
    if symbol_error:
        suggestions.append("Include at least one special character (!@#$...)")

    return strength, suggestions

# Main Program
if __name__ == "__main__":
    print("🔐 Password Strength Checker")
    user_password = input("Enter your password: ")

    strength, tips = check_strength(user_password)
    print(f"Strength: {strength}")
    if tips:
        print("Suggestions to improve:")
        for tip in tips:
            print(f"- {tip}")
