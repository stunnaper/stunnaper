user_number = (input('number:'))
user_number_int = int(user_number)
factorial = 1
while user_number_int > 0:
    factorial *= user_number_int
    user_number_int -= 1
print(factorial)
