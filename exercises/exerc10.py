def calc_age(year_of_birth, current_year=2023):
    age_local = current_year - year_of_birth
    return age_local


birth_year_user = int(input("What is your year of birth? "))
age_user = calc_age(birth_year_user)
if age_user > 120:
    print("Wow, you're fucking old!")
else:
    print(age_user)
