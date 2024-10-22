###
# Calculates the final grade for a test based
# on the number of points obtained
#
def pts_to_grade(points):
    grade = ''
    if points >= 18:
        grade = 'Excellent'
    if 18>points>=14:
        grade = 'Good'
    if 14>points>=10:
        grade = 'Satisfactory'
    if points<10:
        grade = 'Fail'
    return grade



test_result = int(input('insert the points you got: '))
final_grade = pts_to_grade(test_result)
print(f'You scored {test_result} points on the test. Your final grade is {final_grade}')