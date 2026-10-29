# 7. Password Strength Checker
# Intermediate
# Concepts: Conditions, loops, functions, strings
# Requirements
#     • Accept a password from the user.
#     • Check its length.
#     • Check for uppercase and lowercase letters.
#     • Check for digits and special characters.
#     • Classify it as weak, medium, or strong according to your defined rules.
# Bonus: Display suggestions to improve a weak password.


def strength(password,upper,lower,digit,special):
    if len(password) >= 8 and upper and lower and digit and special:
        return "Strong"
    elif len(password) >= 8 and (upper or lower) and digit:
        return "Medium"
    else:
        return "Weak"

def suggestion(p,s,upper,lower,digit,special):
    if s.lower()=="weak" or s.lower()=="medium":
         print("Suggestion")
         if len(p)<8:
              return print("add more charatcer ")
         if not upper:
              print("add upper case character")
         if not lower:
              print("add lower case character")
         if not digit:
              print("add digit")
         if not special:
              print("add special char")
    else:
         print("All Ready Strong")


def password_strenghh():
        password = input("Enter Your Password : ")
        upper = any(c.isupper() for c in password)
        lower = any(c.islower() for c in password)
        digit = any(c.isdigit() for c in password)
        special = any(not c.isalnum() for c in password)
        score = strength(password,upper,lower,digit,special)
        print(score)
        suggestion(password,score,upper,lower,digit,special)


password_strenghh()