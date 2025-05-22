import time

print('I can add 5 to any number you give me yes yes i can do it!')

time.sleep(1)

a = float(input('what number do you want me to add 5 to\n>'))

if a.is_integer():
    a = int(a)

b = 5
c = a + b

print(f'ok ez adding {b} to your number {a} it would be...')

time.sleep(1)

print(f'{c}!!')