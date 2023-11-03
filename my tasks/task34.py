temperature = input('enter temperature:')
temperature_int = int(temperature)
if temperature_int >= 100:
    print('Boiling')
elif  32 <= temperature_int <= 99:
    print('liquid')
else:
    if temperature_int < 32:
        print('Freezing')