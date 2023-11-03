month = input('enter a month:')
if month in ('january','February','March','April','May'):
    print('Spring')
elif month in ('June','July','august'):
    print('summer')
elif month in ('September','October','November',):
    print('fall')
elif month in 'December':
    print('Winter')
else:
    print('invalid month')