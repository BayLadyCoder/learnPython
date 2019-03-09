# Name: Rachada Chairangsaris (Bay)
# Assignment: Lab 5, P1-P8
# Date: March 6th, 2019

# ---------------------------------------------------------------------------------
# P1 - zeroCheck
def zeroCheck(n1, n2, n3):
    print('n1 =', n1, ', n2 =', n2, ' ,n3 =', n3)
    return (n1 == 0 or n2 == 0 or n3 == 0)

# Test P1
print('zeroCheck:', zeroCheck(1, 0, 3))
print('----------------------------------')

# ---------------------------------------------------------------------------------
# P2 - ordered3
def ordered3(n1, n2, n3):
    print('n1 =', n1, ', n2 =', n2, ' ,n3 =', n3)
    return (n1 < n2 and n2 < n3)


# Test P2
print('ordered3:', ordered3(1, 4, 3))
print('----------------------------------')

# ---------------------------------------------------------------------------------
# P3 - modCount
def modCount(n, m):
    if m > n:
        print('Wrong input (m is greater than n)')
    else:
        print('n =', n, ', m =', m)
        print("Numbers from 1 -", n, "that are evenly divisible by", m, "are")

        numsWork = 0
        for num in range(1, n):
            if num % m == 0:
                print(num)
                numsWork += 1
        return numsWork

# Test P3
print('modCount:', modCount(40, 7))
print('----------------------------------')

# ---------------------------------------------------------------------------------
# P4 - HelloWorld
def helloWorld(name):
    print('name =', name)
    return ("Hello World, my name is " + name)

# Test P4
print('HelloWorld:', helloWorld("Bay"))
print('----------------------------------')

# ---------------------------------------------------------------------------------
# P5 - printAsterisks
def printAsterisks(n):
    asterisks = ""
    if n > 75:
        for x in range(75):
            asterisks += "*"
    else:
        for x in range(n):
            asterisks += "*"
    print('n =', n)
    return (asterisks)

# Test P5
print('printAsterisks:', printAsterisks(150))
print('----------------------------------')

# ---------------------------------------------------------------------------------
# P6 - getContinue
def getContinue():
    answer = ""
    while(answer != 'y' and answer != 'n' ):
        answer = input("Do you want to continue (y/n): ").lower()
    return answer

# Test P6
print('getContinue:', getContinue())
print('--------------------------------------------------------------------------')

# ---------------------------------------------------------------------------------
# P7 - listSideEffect
def listSideEffect(listNum, threshold=0):
    print('List 1 = ', listNum, ', Threshold =', threshold)
    i = 0
    while i < len(listNum):
        if listNum[i] <= threshold:
            del listNum[i]
        else:
            i += 1

# Test P7
numbers1 = [1, 2, 23, 44, 55, 100, 3, 9, 0, 88, 199]
listSideEffect(numbers1, 50)
print('List 1 after function called (altered):', numbers1)
print('--------------------------------------------------------------------------')

# ---------------------------------------------------------------------------------
# P8 - listFunctionValue
def listFunctionValue(listNum, threshold=0):
    print('List 2 = ', listNum, ', Threshold =', threshold)
    greaterNums = []
    for n in listNum:
        if n > threshold:
            greaterNums.append(n)
    return greaterNums

# Test P8
numbers2 = [1, 2, 23, 44, 55, 100, 3, 9, 0, 88, 199]
print('listFunctionValue (return):', listFunctionValue(numbers2, 40))
print('List 2 after function called:', numbers2)
print('--------------------------------------------------------------------------')
# ---------------------------------------------------------------------------------
