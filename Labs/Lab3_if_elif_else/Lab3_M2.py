# Name: Rachada Chairangsaris (Bay)
# Assignment: Lab 3, M2
# Date: February 20th, 2019

# Temperature Conversion Program
print('This program will covert temperatures (Fahrenheit/Celsius/Kelvin')
print('Enter (FC) to convert Fahrenhiet to Celsius')
print('Enter (CF) to convert Celsius to Fahrenhiet')
print('Enter (CK) to convert Celsius to Kelvin')
print('Enter (KC) to convert Kelvin to Celsius')
print('Enter (FK) to convert Fahrenhiet to Kelvin')
print('Enter (KF) to convert Kelvin to Fahrenhiet')

# Get temperature to convert
which = input('Enter selection: ')

while which != 'FC' and which != 'CF' and which != 'CK' and which != 'KC' and which != 'FK' and which != 'KF':
    which = input('Please enter "FC", "CF", "CK", "KC", "FK", "KF ')

temp = int(input('Enter temperature to convert: '))

# Determine temperature conversion needed and display results
if which == 'FC':
    converted_temp = format((temp - 32) * 5/9, '.1f')
    print(temp, 'degrees Fahrenheit equals', converted_temp, 'degrees Celsius')
elif which == 'CF':
    converted_temp = format((9/5 * temp) + 32, '.1f')
    print(temp, 'degrees Celsius equals', converted_temp, 'degrees Fahrenheit')
elif which == 'CK':
    converted_temp = format(temp + 273.15, '.1f')
    print(temp, 'degrees Celsius equals', converted_temp, 'degrees Kelvin')
elif which == 'KC':
    converted_temp = format(temp - 273.15, '.1f')
    print(temp, 'degrees Kelvin equals', converted_temp, 'degrees Celsius')
elif which == 'FK':
    converted_temp = format(((temp - 32) * 5/9) + 273.15, '.1f')
    print(temp, 'degrees Fahrenhiet equals', converted_temp, 'degrees Kelvin')
else:
    converted_temp = format((9/5 * (temp - 273.15)) + 32, '.1f')
    print(temp, 'degrees Kelvin equals', converted_temp, 'degrees Fahrenheit')
