# Name: Rachada Chairangsaris (Bay)
# Assignment: Lab 7, Text File I/O
# Date: March 18th, 2019

# read  data from the file 
file = open('account_information.txt', 'r')

# create lists to store data
list = []
usernames = []
passwords = []

# split username and password in line from file and add to a list
for line in file:
    line = line.split()
    list += line

# separate usernames and passwords into different lists
for i in range(0,len(list), 2):
    usernames.append(list[i])
    passwords.append(list[i+1])


# Get Username from user
username = input('Username: ').lower()

# check if username is matched with usernames in database
while username not in usernames:
    print('Username "'+ username + '" is not existed, please try again.')
    username = input('Username: ').lower()


# Get Password from user
password = input('Password: ')
attemps = 3

# check if password is matched with passwords in database
while password not in passwords:
    attemps -= 1
    # if enter incorrect password 3 times, program shuts down
    if attemps < 1:
        print("You've entered too many incorrect passwords, Program is quit")
        quit()
    print('Password is incorrect, you have ' + str(attemps) + ' more attemp(s)')
    password = input('Password: ')


# Succesfully Logged In
print("Logged in succesfully")




    
