#--->swappng of variables
#eg-1
#a=8
#b=5
     #c=a         #c=8
     #a=b         #a=5
     #b=c         #b=8
     #print(a,b)
#eg-2
'''a=a+b
b=b-a
a=a-b
a,b=b,a
(a,b)
'''

#eg-3
'''a=a*b #40
b=a/b #8
a=a/b #5
print(int(a),int(b))
'''

'''print(a)
print(id(a)) ''' #id function which is used to find the memory address of the variable

#-----> keywords('False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield]

#keywords are reserved words which provides special meaning to compiler or interpreter
#
'''import keyword
print(keyword.kwlist)
print(len(keyword.kwlist))'''

#to check if the sring is keyword or not
#print(keyword.iskeyword("else"))


#!-----> literals
#iteral is the constant value assigned to the variable
#a variable is considered to be a constant it is defines in capitals

 #a=78   #a is variable
# A=78   #A is constant


#hash()---> it creates a hash value for constnat data type and
 # provides error for non constant data types
'''n1=89+7j
print(hash(n1))

f1=[7,8,9]
print(hash(f1)) #it givess error
'''
 #!--> operators
''' -->opearators are symbols which is used to perform various operations between two or more operation'''

 #arithematic
 #assignment
 #logical
 #relational or compariona
 #bitwise
 #identity
 #membership

 #*--to do -> arithematic___>+,-,*,/,%,
 
''''a=8
b=9
c=5
print(a+b*c-b)
 #  input is used to get the runtime input
'''
#n1=input("enter the value:")
#print(n1)
'''
#  eval is used to get the runtime input for all datatypes
//n1=eval(input("enter the value:"))
//print(type(n1))


a=4
b=2
print(a/b)  # is used to get the quotient value
print(a%b)  # is used to get the remainder value

'''

#1--> **__. used for ower of number
#print(2**4)--->16

#assignment operators--->+-=,-=, /=, *=
'''
a=8
a+=2
print(a)
b=10
b-=2
print(b)
'''

#!---> comparision oprators


'''
a=8
b=7
print(a>b)  #----> true

print(a==b)  #---> false
'''


#!----> bitwise oprators ---> & | ^, <<, >>
a=7
b=4
print(a&b)



# name, age, nationality
# 18 above, Indian

a=str (input("enter the name of candidate"))
age=int(input("enter the age"))
nationality=str(input("enter nationality"))
if (nationality==indian):
   
    age>=18:
    print("eligible  for voting")
    }
   
else:
        print("not eligible")























