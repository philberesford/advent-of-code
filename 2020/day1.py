fs = open("day1.data",'r')  
contents = fs.readlines()

def toNumber(str):
    return int(str.strip())

def adder(num1, num2, desiredTotal):
    total = num1 + num2
    return total == desiredTotal

def adder2(num1, num2, num3, desiredTotal):
    total = num1 + num2 + num3
    return total == desiredTotal

def list_adder(numbers, targetTotal):
    # Outer loop for traverse the entire list  
    for i in range(0,len(numbers)-1):  
        for j in range(len(numbers)-1):
            if (i!=j):
                number1 = numbers[i]
                number2 = numbers[j]
                if (adder(number1, number2, targetTotal)):
                    print(str(number1) + "," + str(number2))   

def list_adder2(numbers, targetTotal):
    # Outer loop for traverse the entire list  
    for i in range(0,len(numbers)-1):  
        for j in range(len(numbers)-1):
            for k in range(len(numbers)-1):
                if (i!=j!=k):
                    number1 = numbers[i]
                    number2 = numbers[j]
                    number3 = numbers[k]
                    if (adder2(number1, number2, number3, targetTotal)):
                        print(str(number1) + "," + str(number2) + "," + str(number3))   


numbers=list(map(toNumber, contents))
#list_adder(numbers, 2020)
list_adder2(numbers, 2020)