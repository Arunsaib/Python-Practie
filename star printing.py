##for i in range(4):
##    for j in range(4):
##        print("#",end="")
##
##    print()    


##for i in range(4):
##     for j in range(i):
##         print("#", end="")
##     print()

##for i in range(4):
##     for j in range(4-i):
##         print("#", end="")
##     print()

##nums=[12,15,18,21,25]
##for num in nums:
##    if num%5==0:
##        print(num)

##num=10
##for i in range(2,num):
##    if num % i ==0:
##        print("Not Prime" ,i)
##        break
##else:
##       print("prime Number" ,i)


##num = int(input("Enter a number to check prime or not"))
##for i in range(2,num):
##    if num % i ==0:
##        print("Not Prime -" , num)
##        break
##else:
##       print("prime Number -" ,num)

#------Python Examples-----------#

##1-Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,	between 2000 and 3200 (both included).
##The numbers obtained should be printed in a comma-separated sequence on a single line.

Result=""
count=0
for i in range(1999, 3201,1):
    if i%7==0 and i%5!=0 :
        Result+= str(i)+","
        count+=1
print(Result, "Total Numbers Divisble by 7 But not Multiple by 5 is",count)




#------factorial function----#
##2 Write a program which can compute the factorial of a given numbers.
##The results should be printed in a comma-separated sequence on a single line.
##Suppose the following input is supplied to the program:
##8
##Then, the output should be:
##40320

#code starts from here
factorial=1
number=int(input("Enter the Number:-"))
for i in range(1,number+1):
    factorial*=i
print("The Factorial of Number ",number,"is",factorial)    

#----3rd Question--#
##3 With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
##Suppose the following input is supplied to the program:
##8
##Then, the output should be:
##{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
dict={}
number=int(input("Enter the Number:-"))
for i in range(1,number+1):
     dict[i]=i*i
print(dict)

#---4th Question--#
##4 Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
##Suppose the following input is supplied to the program:
##34,67,55,33,12,98
##Then, the output should be:
##['34', '67', '55', '33', '12', '98']
##('34', '67', '55', '33', '12', '98')
listNum=[]
tupleNum=()
Input = input("Enter the Numbers seperated By commma")
numbers= Input.split(",")
for i in numbers:
    listNum.append(i)
    tupleNum+=(i,)
print(listNum)
print(tupleNum)
    

