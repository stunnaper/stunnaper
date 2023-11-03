user_name = input('enter a name:')
counter = 0
vowels = ('a', 'e', 'i' ,'o' ,'u')
while any (vowel in user_name for vowel in vowels):
  print('True')
  break
else:
    print('False')