import time

print('hello i am adder man 123')
time.sleep(2)
print('give me 2 numbers you want to add up!!!')
time.sleep(1)

num_1 = float(input('your first number?\n>'))

if num_1.is_integer():
    num_1 = int(num_1)

print(f'awesome number {num_1}!!')
time.sleep(1)

num_2 = float(input('your second number?\n>'))

if num_2.is_integer():
    num_2 = int(num_2)

print(f'ok ok number {num_1} and {num_2} ez ez')
time.sleep(1)

total = num_1 + num_2

print(f'your number is {total}')