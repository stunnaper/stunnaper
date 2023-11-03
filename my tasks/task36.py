score = input('enter your score:')
score_int = int(score)
if score_int >= 90:
    print('A')
elif 80 <= score_int <= 89:
    print('B')
elif 70 <= score_int <= 79:
    print('C')
elif 60 <= score_int <= 69:
    print('D')
elif score_int < 60:
    print('F')
else:
    ('invalid score')
    



