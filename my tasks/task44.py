user_name = input('enter your name:')
vowels = ('aeiou')
vowels_count = 0
index = 0

while index < len(user_name):
        if user_name[index]in vowels:
            vowels_count += 1
        index += 1    
print(vowels_count)
    
