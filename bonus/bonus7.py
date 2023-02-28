def password_check(password_to_check):

    result_local = {}

    if len(password_to_check) < 8:
        result_local["length"] = False
    else:
        result_local["length"] = True

    digit_local = False
    for char in password_to_check:
        if char.isdigit():
            digit_local = True
    result_local["digits"] = digit_local

    uppercase_local = False
    for char in password_to_check:
        if char.isupper():
            uppercase_local = True
    result_local["uppercase"] = uppercase_local

    if all(result_local.values()):
        return "Strong Password"
    else:
        return "Weak Password"


password = input("Enter new password: ")

print(password_check(password))

