day = input('day:')
result = ('monday','tuesday','wednesday','Thursday')
if day in result:
  print(' weekday')
elif day == 'friday':
  print('TGIF')
elif day in ('saturday', 'sunday'):
  print('weekend')
else:
  print('invalid input')