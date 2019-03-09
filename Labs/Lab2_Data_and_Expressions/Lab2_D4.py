# Name: Rachada Chairangsaris (Bay)
# Assignment: Lab 2, D4 Life Signs
# Date: February 7th, 2019


# The estimate time for this program
# 1 day = 1,440 minutes (60 minutes * 24 hours)
# 1 month = 30 days and 1 year = 12 months
print('-----------------------------------------------------')
print('Please input your age in a whole number for years and months')
print()
print('For example, if you are 8 years and 10 months old')
print('You are going to input 8 for years, and 10 for months')
print('-----------------------------------------------------')

ageYear = int(input('How old are you? (YEARS only, input 0-100): '))
ageMonth = int(input('How old are you? (MONTHS only, input 0-11): '))

# minsMonth (total minutes in a month) = 30 days * 24 hours * 60 minutes
minsMonth = 30 * 24 * 60
# minsYear (total minutes in a year) = 12 months * 30 days * 24 hours * 60 minutes
minsYear = 12 * 30 * 24 * 60

heartRate = 67.5
minutes = (ageYear * minsYear) + (ageMonth * minsMonth)
heartbeats = int(minutes * heartRate)

if ageYear < 1:
    breathLow = minutes * 30
    breathHigh = minutes * 60
elif ageYear >= 1 and ageYear <= 4:
    breathLow = minutes * 20
    breathHigh = minutes * 30
elif ageYear >= 5 and ageYear <= 14:
    breathLow = minutes * 15
    breathHigh = minutes * 25
else:
    breathLow = minutes * 12
    breathHigh = minutes * 20

breathLow = "{:,}".format(breathLow)
breathHigh = "{:,}".format(breathHigh)
heartbeats = "{:,}".format(heartbeats)

print()
print('You have breathed about', breathLow, '-', breathHigh, 'times ')
print('and your total heartbeats since you were born is', heartbeats, 'times')
print('---------------------------------------------------')
print('Name: Rachada Chairangsaris (Bay)')
print('Assignment: Lab 2, D4 Life Signs')
print('Date: February 7th, 2019')
print()
