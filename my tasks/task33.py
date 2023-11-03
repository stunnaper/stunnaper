grade = input('enter your grade:')
grade_int = int(grade)
if grade_int >= 90:
    print ('A')
elif 80 <= grade_int <= 89:
    print('B')
elif 70 <= grade_int <= 79:
    print('C')
else:
    if grade_int < 70:
        print('F')

