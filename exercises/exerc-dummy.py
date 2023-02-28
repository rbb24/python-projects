def get_max():
    grades = [9.6, 9.2, 9.7]
    best_grade = max(grades)
    worst_grade = min(grades)
    grade_overview = f"Max: {best_grade}, Min: {worst_grade}"
    return grade_overview


print(get_max())
