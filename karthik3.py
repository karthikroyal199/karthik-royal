#eg:3--> take the values of length and breadth of from a user check is it suatre or not
'''
l=int(input("enter the length:"))
b=int(input("enter the breadth:"))
if l==b:
    print("it is a suare")
else:
     print("it is not suare")

'''

#eg4--> program to chech wheather it is both multiple of 5 and 7

'''n=int(input("enter the number"))
if n%5==0 and n%7==0:
    print("yes")
else:
        print("no")


 

'''

#eg:5---> accept the age of 4 people and display oldest one

'''
a=int(input("enter the age1: "))
b=int(input("enter the age2: "))
c=int(input("enter the age3: "))
d=int(input("enter the age4: "))
if a>b and a>c and a>d:
    print("a is greater")
elif b>a and b>c and b>d:
     print("b is greater")
elif c>a and c>b and c>d:
         print("c is greater")
else:
     print("d is greater")

'''

#--->#Eg6: write a program to accept the price of the bike and display the road tax to be paid
   #according to the following criteria :
   
   #Cost price(in Rs)                   Tax
  #>100000                              15 % + discount 6%
  #>50000 and <=100000                  10%
  #<=50000                              5%
'''

t=int(input("enter the cost:"))
if t>100000:
    discount=t*(6/100)
    value=price-discount
    amount=value*(15/100)
    print(amount+value)
else:
    amount=t*(5/100)
    print(amount)
   
'''

#A school has following rules for grading system:
# a. Below 25 - F
# b. 25 to 45 - E
# c. 45 to 50 - D
# d. 50 to 60 - C
# e. 60 to 80 - B
# f. Above 80 - A
# Ask user to enter marks and print the corresponding grade.
'''
m=int(input("enter the marks:"))

if m>25 and m<=45:
    print("grade if e")
elif m>45 and m<=50:
    print("grade is d")
elif m>50 and m<=60:
    print("grade is c")
elif m>60 and m<=80:
    print("grade is b")
elif m>80:
    print("grade is a")
else:
print("fail")
'''


#(rules---->*statement inside the if condition have to be present at first
            #*elif cannot be used in short hand if else
            #*always it have to end with else)


# code to chesck the given char owel or consonent
'''
char=input("enter thr char:")
if char=="a" or char=="e" or char=="i" or char=="o" or char=="u":
     print("it is a owel")
else:
    print("it is a consonent")

'''


#short hand if else
'''
char=input("enter thr char:")
str="aeiouAEIIOU"
if char in str:
   print("vowels")
else:
    print("consonent")

'''

#elif ladder using short hand if else

#find graetest os 3 variables

'''
a=10
b=12
c=20
print("a is greater") if a>b and a>c else print("b is greater") if b>a and b>c else print("c is greater")

'''


#!--------> looping

#looping can be implemented using for loop and while loop
#---> for loop is used for iteration,if we know the number of timesthe loop have to run
#----> it is used to iterate the iterables eg(string,list,tuple,etc...)

#todo---- syntax for loop
'''
for i in range(0,10):
    print(i)
'''
#eg-2

'''
for val in range(45,96,4):    #(start,end,step)
    print(val)
   
'''

#eg-3---> to decrement the value
'''
for val in range (10,0,-1):
  print(val)

'''
# to print the output of 7th multiplication table from 21 to 43

'''
for i in range(1,10):
    print('7','*',i,'=',i*7)
'''

#---> using break statement

'''
for val in range(15,85):
    if val==30:
     break
    print(val)

'''
##2
'''
for val in range(15,85):
    if val==30:
        print(val)
        break
     
 '''

#----- continue statement
#eg-1
'''
for val in range(15,30):
    if val==18:
        continue
    print(val)
 '''

# practice problems
#1--> print even number b/w 20-40

for i in range (20,41):
    if val %2==0:
        print(val

#!------------->  while loop
#






