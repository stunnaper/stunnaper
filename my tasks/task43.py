user_name = input('Enter a name: ')
counter = 0
vowels = ('a', 'e', 'i', 'o', 'u')
for vowel in vowels:
  if vowel in user_name:
    counter += 1
    break

if counter > 0:
  print('True')
else:
  print('False')
