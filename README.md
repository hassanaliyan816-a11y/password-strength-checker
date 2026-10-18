# Password Strength Checker

A small Python program, written in VS Code with help from GitHub Copilot, that rates how strong a password is.

## How it works

The password gets one point for each of these:

- At least 8 characters
- At least 12 characters
- Contains lowercase letters
- Contains uppercase letters
- Contains numbers
- Contains symbols

| Score | Strength |
|-------|----------|
| 0–2   | Weak     |
| 3–4   | Medium   |
| 5–6   | Strong   |

Common passwords such as `password` or `123456` always score 0. The program also lists tips for anything that's missing.

## Run it

Requires Python 3.

```bash
python password_checker.py
```

The password you type is hidden and is never saved.
