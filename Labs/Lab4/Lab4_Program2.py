# Name: Rachada Chairangsaris (Bay)
# Assignment: Lab 4, Program 2 (For Loop)
# Date: February 26th, 2019


# Get User Input and append into a list
num = ''
listNum = []

while num != '000':
    num = input("Enter an integer, (to see the result, please enter 000): ")

    if num == '000':
        break
    else:
        num = int(num)
        listNum.append(num)

# Calculate Sum, Product, and Subtracting (with For Loop)
sum = 0
average = 0
product = 1
for k in listNum:
    sum += k
    product *= k
    subtracting = listNum[len(listNum)-1] - listNum[0]

# Calculate Average
average = sum/len(listNum)

# Format the Results
sum = "{:,}".format(sum)
average = "{:,}".format(average)
product = "{:,}".format(product)

# Print All the Results
print('-------------------------------------------------------')
print('Sum:', sum, '\nAverage:', average, '\nProduct:',
      product, '\nSubtract (first from last):', subtracting)
print('-------------------------------------------------------')
