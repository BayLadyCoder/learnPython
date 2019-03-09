# Name: Rachada Chairangsaris (Bay)
# Assignment: Lab 3, P5
# Date: February 20th, 2019

positiveNum = 0
negativeNum = 0

while True:
    num = int(input('Enter an integer, (to quit, please enter 0): '))

    if num == 0:
        break
    elif num > 0:
        positiveNum += 1
    else:
        negativeNum += 1

print('Total Positive Numbers:', positiveNum,
      '\nTotal Negative Numbers:', negativeNum)
