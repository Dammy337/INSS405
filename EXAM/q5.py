users = 4
def grades_result(users):
    grades = []
    for i in range(users):
        score = int(input("enter grades {}: ".format(i+1)))
        grades.append(score)
    return grades
def mean_grade(grades):
    sum_grade = sum(grades)
    grade_mean = sum_grade /4
    return grade_mean
def grade_level(grade_mean):
    if grade_mean >=90:
        print("grade level is A")
    elif grade_mean >=80:
        print("grade level is B")
    elif grade_mean >=70:
        print("grade level is C")
    elif grade_mean >=60:
        print("grade level is D")
    elif grade_mean >=50:
        print("grade level is E")
    else:
        print("grade level is E")

grades = grades_result(users)
grade_mean = mean_grade(grades)
grade_level = grade_level(grade_mean)

print("mean grade: ", grade_mean)
print("grade level", grade_level)



