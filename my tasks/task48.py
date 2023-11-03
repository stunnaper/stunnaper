import random
secret_number = random.randint(1, 100)
user_number = int(input('guess the number'))
while user_number != secret_number:
   if user_number < secret_number:
     print('too low')
   elif user_number > secret_number:
      print('too high')
   elif user_number == secret_number:
      print('wow that rigth:',secret_number)
   user_number = int(input('guess the number'))

print('it guess it right')
    

 