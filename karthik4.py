# ---> Assesment
# 1.) cats and mouse:Hacker rank
# 2.) Print the factorial of 8 using for loop
# 3.) Write a program to display sum of odd numbers and even 
# numbers that fall between
# 12 and 37(including both numbers)
# 4.) Write code to print the sum of number using while loop
# n1 = 123 --> 1+2+3 = 6
# 5.) Prine th reverse of given number --> n1= 234 o/p --> 432
def catAndMouse(x, y, z):
    dist_cat_a = abs(z - x)
    dist_cat_b = abs(z - y)
    if dist_cat_a == dist_cat_b:
        return "Mouse C"
    elif dist_cat_a < dist_cat_b:
        return "Cat A"
    else:
        return "Cat B"
# Example usage
print(catAndMouse(1, 2, 3))  # Output: Cat B

#  2nd answer
num = 8
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print("Factorial of", num, "is:", factorial)

# 3rd answer
sum_even = 0
sum_odd = 0
for num in range(12, 38):
15:51
for num

# 4th answer
n1 = 123
total = 0
while n1 > 0:
    digit = n1 % 10
    total += digit
    n1 //= 10
print("Sum of digits of the number:", total)
#5th answer
n1 = 234
reverse = 0
while n1 > 0:
    digit = n1 % 10
    reverse = reverse * 10 + digit
    n1 //= 10
print("Reverse of the given number:", reverse)

#  2nd answer
num = 8
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print("Factorial of", num, "is:", factorial)
# 3rd answer
sum_even = 0
sum_odd = 0
for num in range(12, 38):
    if num % 2 == 0:
        sum_even += num
    else:
        sum_odd += num
print("Sum of even numbers:", sum_even)
print("Sum of odd numbers:", sum_odd)
ssv-hcbt-rgo






#---> while loop
#---> break using while loop
# Eg:1
#1.)iterate from 20 to 30 and break the loop in 27
'''
i=20
while i<31:
     if i==27:
         break
       
     print(i)             #upto 27
     i+=1
   '''      
#eg---------

'''
i=20
while i<31:
    if i==27:
        print(i)
        break
    i+=1                        #27 only
       
 '''


# -------> continue
'''
i=20
while i<31:
    if i==27:
        continue
    print(i)
    i=i+1  
   
   '''  

#eg
'''
i=19
while i<31:
    i=i+1  
    if i==27:
        continue
    print(i)
   
   '''

#--->dind the sum of all number b/w 12 to 22

'''i=12
sum=0
while i<22:
    sum=sum+i
    i+=1
print(sum)
  '''  
#---> find the average of value from 20 to 25    
'''  
i=20
sum=0
while i<26:
    sum=sum+i
    i+=1
avg=sum/6
print(avg)
       
   '''

#Eg:6
# find the average of value from 20 to 30
'''
i=20
sum=0
count=0
while i<=30:
    sum=sum+i
    count+=1
    i+=1
avg=sum/count
print(avg)
'''

# ! -----> Nested for loop

# Eg:1
'''
for row in range(1, 3+1):
    for col in range(1,4+1):
        print(row, col)
'''


'''
rows = int(input("enter the rows: "))
cols = int(input("enter the cols: "))

for row in range(rows):
    for col in range(cols):
        print(row,col,end=" ")
    print()


'''

# to print stars in right angle triangle
'''
for row in range(0,6):
    for col in range(0,row):
        print("*",end=" ")
    print()

#--->
row=6
col=5
for row in range(0,row):
    for col in range(0,col):
        print("&",end=" ")
    print()


'''
#---> print this
#* * * * *
#*       *
#*       *
#*       *
#* * * * *

'''
for row in range(0,5):
    for col in range(0,5):
        if col==0 or col==5-1 or row==0 or row==5-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
   

'''

'''
for row in range(0,5):
    for col in range(0,6):
        if ((row==0 and col==3)or (row==1 and(col>=2 and col<4) or (row==2 and (col>=1 and col<=5)))):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
  '''  



#*  (--- print this) * *  *  *  *  *  *  *  * * * * * *
'''
for row in range(0,6):
    for col in range(0,6):
        if (col==0 or (col==1 and row==1)or (col==2 and row==2) or(col==3 and row==3) or (col==4 and row==4) or (col==5 and row==5) or row==6-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

'''



 # ----> data types
# primary

# Number ----> int, float complex
# String
# Boolean
# None

# collection
# List
# tuple
# set
# dictionary  


#-------> list

#1--> if the collection of elements are surrounded by square brackets, it is considerd to be list
#eg
#k1=[4,85,6,95,23,5,"hellow"]



# Characteristics of list

'''
# 1.) List have to be surrounded []
# 2.) It is mutable (the elements in the list are changable)
# 3.) Every elements inside list is indexed
# 4.) The elements inside list will be ordered format
# 5.) It can hold duplicate values
# 6.) Its heterogenous

'''
# to acces the elements in list
'''
l1=[1,8,6,8,22,99,]
print(l1)
'''


#--> Indexing

'''
# In the collection datatypes like list, tuple, string, the elements will be alloted
# with predefined unique value called index value

#--> We have 2 types of indexing

# Positive indexing --> starts with @ from left hand side
# Negative indexing --> starts with -1 from right hand side

'''

### Positive indexing
#print(lst1[0])
#print(lst1[4])
#print(lst1[20])


# ---->Negative indexing
#lst1 = [1, 4, 1, 7, 89.7, 75, "p", "i"]
#print(lst1[-1])
#print(lst1[-5])


#---> slicing

lst1 = [1, 4, 1, 7, 89.7, 75, "p", "i"]
#lst1(start,end,step)
print(lst1[0:4])
print(lst1[6:8])
print(lst1[3:6])
print(1st1[ :5])
print(1st1[:3])
print(1st1[:])

print(1st1[0:7:1])   1st1[0:7]-----> both are same
print(1st1[0:7:2])

trail + int(input())



