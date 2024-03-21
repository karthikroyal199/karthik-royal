#---> common functions for list

'''
l1=[8,9,6,22,5]
print(len(l1))
print (max(l1))
print(min(l1))


l1=[8,9,6,22,5,"p","o"]
print (max(l1)) ------> error coz its combination of int and string
'''

#l1=[6,7,8,9,0,8.89,-5,0.78]
#print(min(l1))  #-5


#l1=[6,7,8,9,0,8.89,-5,0.78]
# index() ---> to get index value of specific element
#print(l1.index(9))

#l1=[6,7,8,9,0,8.89,-5,0.78]
# count()--->how many num of times an element is repeated
#print(l1.count(6))


# Some functions which is specifically used for list

# To add element inside list
# insert() ---> to add element at specific index position
'''
l1 = [6,6,6,7,8,9,0,8.89,-5,0.78]
l1.insert(2,"cars")
print(l1)

'''

# To delete element from list
'''
l1 = [6,6,6,7,8,9,0,8.89,-5,0.78]
# pop() ---> last element will be deleted
l1.pop()
print(l1)


l1=[6,7,8,9,0,8.89,-5,0.78]
l1.pop(4)---> pop(index_value) is used to delete the specific element
print(l1)

l1=[6,7,8,9,0,8.89,-5,0.78]
l1.clear()---_> used to clear the specific element
print(l1)
'''

#---> join two list
'''
l1=[5,89,26,5]
l2=[89,65,325,89]
print(l1+l2)

#or
l1.extend(l2)
print(l1)
'''

#----> copy()
# l1 = [6, 7, 8,9, 3]
# l2 = l1.copy()
# print(l2)
# print(l1)

# print(id(l1))
# print(id(l2))

# Diff between shallow copy and deep copy
# shallow copy
'''
import copy
l1=[8,9,0,[5,6],[3,2,1]]
l2=copy.copy(l1)
print(l1)
print(l2)
'''

# deep copy
'''
import copy
l1=[8,9,0,[5,6],[3,2,1]]
l2=copy.copy(l1)
l2.append(890)
print(l1)
print(l2)


import copy
l1=[8,9,0,[5,6],[3,2,1]]
print(l1[-1[1]])
l2=copy.deepcopy(l1)
l1[-1].append('cars')
print(l1)
print(l2)

'''


# arranging elements in ascending and descending order (sort)
'''
l1=[5,33,6,9,4,50,60]
l1.sort() # for ascending order
print(l1)

l1=[5,33,6,9,4,50,60]
l1.sort(reverse=True) # for descending  order
print(l1)
'''

#--> list constructor
'''list() is used to cover other collection data types to list


l1=[8,9,[0,8,7],["p","o","y"],[8,"t"]]
print(l1[-2][1])  --> o only printed

'''

# delete t form l1
'''
l1=[8,9,[0,8,7],["p","o","y"],[8,"t"]]
l1[-1].remove("t")
print(l1)
'''
# Combine these ["p","o",'y'],[8,'t'] lists in l1['p', 'o', 'y', 8, 't']

'''
l1=["p","o","y"]
l2=[8,"t"]
l1.extend(l2)
print(l1)
'''
#---> touples
'''
1--;touple has to be sorrounded by ()
2--;the element inside touple are not chargeble
3--;the element inside topule are indexed
4--;the element will execute in order
5--;it is hetrogenious
6--;it allow duplicable elemets

'''
# Eg:
'''
t1=(8,8,9,6,5.78,[9,0],(6,8),"hey",9+6j)
print(t1)
print(type(t1))

'''

# indexing,slicing are all same as list


#l1=(8)
#print(type(l1)) # int


#l1=(8,)
#print(type(l1))

#t=8,
#print(type(t))

# len(),min(),max(),index(),count() --> all same as list

# to add element inside tuple --> cannot add
#cannot delete any element from tuple

# join 2 tuples

'''
t1=(8,9,0)
t2=(6,7,8)
print(t1+t2)

# To add all element inside list and tuple
#sum()
#l1 = (8, 9, 7, 6)
#print(sum(l1))



# * sort tuple
#t1 = (8, 9,0, 89, 12)
#print(tuple(sorted(t1)))
#print(tuple(sorted(t1, reverse=True)))

# * Iterate list and tuples

l1 = [9, 8, 0, 6, 5]
for i in l1:
    print(i)
 
'''

# ---> Strings

#s1='o'
#print(type(s1))
'''

s1="hello world"

# To access string
#print(s1)

# indexing and slicing ---> same as list and tuple

#print(s1[0:5])

# len(),min(),max(),index(),count()

s1="hello world"

# print(len(s1))
# print(max(s1))
# print(min(s1))

# ord() ---> used to find the ASCII value of a character
s1='u'
print(ord(s1))


# functions of string
s1 = "hello world"
# To convert all characters to upper case
print(s1.upper())


# To convert all characters to lower case

s1="HYIDUJIKWady"
print(s1.lower())


# Strip()---> To eliminate the space in beginning and end of string
s1="  Where are you?"
print(s1.lstrip())



# Split() --> To split the words in string based on character

s1 = "where are you?"
print(s1.split("r"))


# Replace() ---> to replace a specific char in the string
s1="where are you?"
print(s1.replace('r','&&'))


# Swapcase()---> to convert capital to small and small to capital

s1="HEY there"
print(s1.swapcase())


# Title() --> to write the string in format of title
s1='never giveUP'
print(s1.title())  # --> Never Giveup


# Capitalize() ---> 1st char of string will be converted to capital

s1='never giveUP'
print(s1.capitalize())

# Join the strings
s1 = "hello"
s2 = 'world'
print(s1+s2)


s1 =
how are you
iam fine
hey there


# splilines() ---> used to split the string based on lines
s1 ='''
#how are you
#iam fine
#hey there
'''
print(s1.splitlines())


# Find () --> To find the index based on a character
s1="hello world"
print(s1.index('z'))

# Join() --->
l1=["hey", "there"]
#print(" ".join(l1))
print("$".join(l1))


s1="Welcome to all"
print(s1.endswith('L')) ---> we get either true or false


s1="67"
print(type(s1)) --> we get datatype like str or int etc...
print(s1.isdigit())--> we get whether it is true or false


# Print the string in reverse manner

s1 = "Welcome to all"
print(s1[::-1]) --> we get the output in reverse manner



# Eg:1
# wap to find the number of lower case letters
s1 = "HEY there you aRE"
count=0
#print(s1.swapcase())
#print(len(s1))
for i in s1:
    if i.islower():
        count+=1
print("The total num of lower case lettes: ",count)
       
'''

# --> Eg:2 r --> "$"

#s1 = 'restarter'
s1 =  "IMAGIN"
fst=s1[0]
bal=s1[1:]
txt=bal.replace(fst, "$")
print=(fst+txt)
#print(s1ice.replace('r',"$"))



Lorem Ipsum is simply dummy text of the printing and typesetting industry.
Lorem Ipsum has been the industrys standard dummy text ever since the 1500s,
when an unknown printer took a galley of type and scrambled it to make a type specimen book.
It has survived not only five centuries,
but also the leap into electronic typesetting,
remaining essentially unchanged.
It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages,
and more recently with desktop p
desktop p"
char=len(s1)
print(char)
words=s1.split()
print(len(words))
sentenses=s1.split(".")
print(len(sentenses))






