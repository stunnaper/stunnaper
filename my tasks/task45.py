user_name = input('name:')
vowels = ('aeiou')
vowels_count = 0

for x in user_name:
   if x in vowels:
     vowels_count += 1
print(vowels_count)