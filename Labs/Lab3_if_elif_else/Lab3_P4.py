# Name: Rachada Chairangsaris (Bay)
# Assignment: Lab 3, P4
# Date: February 20th, 2019

sum = 0
num = 0

while num != '000':
    num = input("Enter an integer, (to quit, please enter 000): ")

    if num == '000':
        break
    elif int(num) > 0 and int(num) <= 100:
        sum += int(num)
    else:
        continue
print(sum)
