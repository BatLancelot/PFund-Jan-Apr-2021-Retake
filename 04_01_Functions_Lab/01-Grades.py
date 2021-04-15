def grade_in_text(grade):
    if 2.00 <= grade < 3.00:
        return "Fail"
    if 3.00 <= grade < 3.50:
        return "Poor"
    if 3.50 <= grade < 4.50:
        return "Good"
    if 4.50 <= grade < 5.50:
        return "Very Good"
    if 5.50 <= grade < 6.00:
        return "Excellent"


grade = float(input())
print(grade_in_text(grade))
