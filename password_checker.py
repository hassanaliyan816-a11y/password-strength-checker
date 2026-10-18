"""Password strength checker.

Scores a password on length and character variety, then reports
its strength along with tips for making it stronger.
"""

import re
import getpass

COMMON_PASSWORDS = {"password", "123456", "qwerty", "letmein", "admin", "welcome"}


def check_password(password):
    """Return (score, tips) for the given password. Score ranges from 0 to 6."""
    score = 0
    tips = []

    if password.lower() in COMMON_PASSWORDS:
        return 0, ["This is a very common password. Choose something unique."]

    if len(password) >= 8:
        score += 1
    else:
        tips.append("Use at least 8 characters.")
    if len(password) >= 12:
        score += 1
    else:
        tips.append("12 or more characters is even better.")

    checks = [
        (r"[a-z]", "Add lowercase letters."),
        (r"[A-Z]", "Add uppercase letters."),
        (r"\d", "Add numbers."),
        (r"[^A-Za-z0-9]", "Add symbols such as ! @ # $."),
    ]
    for pattern, tip in checks:
        if re.search(pattern, password):
            score += 1
        else:
            tips.append(tip)

    return score, tips


def strength_label(score):
    if score <= 2:
        return "Weak"
    if score <= 4:
        return "Medium"
    return "Strong"


def main():
    print("=== Password Strength Checker ===")
    password = getpass.getpass("Enter a password to check (input hidden): ")
    score, tips = check_password(password)
    print(f"Score: {score}/6 -> {strength_label(score)}")
    for tip in tips:
        print(f"  - {tip}")


if __name__ == "__main__":
    main()
