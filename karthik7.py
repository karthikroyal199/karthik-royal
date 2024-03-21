# ----> Assesment
# ----> Assesment
# 1.) dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
# Merge two python dictionary
# o/p --> {'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

'''
d1={'Ten':10,'Twenty':20,'Thirty':30}
d2={'Thirty':30,'fourty':40,'fifty':50}
d1.update(d2)
print(d1)


# 2.)Python Program to determine if
# the given Sets Are Disjoint
# or Not without Using Inbuilt-in Functions

# set1 = {'Python', 'Java', 'Data Science'}
# set2 = {'ML', 'AI', 'R Language', 'Python'}
# set3 = {'Data Analytics', 'Robotics', 'Deep L
# 3.)list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"]

# O/P --> ['My', 'name', 'is', 'Kelly']

set1 = {'Python', 'Java', 'Data Science'}
set2 = {'ML', 'AI', 'R Language', 'Python'}
set3 = {'Data Analytics', 'Robotics', 'Deep Learning'}
c = 0
flag = 0
for val in range(3):
    c=c+1
    if c==1:
        for val in set1:
            if val in set2 or val in set3:
                flag=1
                break
    if c==2:
        for val in set2:
            if val in set1 or val in set3:
                flag=1
                break

    if c==3:
        for val in set3:
            if val in set2 or val in set1:
               flag=1
               break
if flag==0:
    print("Disjoint")
else:
    print("joint")




# 3.)list1 = ["M", "na", "i", "Ke"]
#    list2 = ["y", "me", "s", "lly"]
#    O/P --> ['My', 'name', 'is', 'Kelly']


list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
l3=[]
for i in range(len(list1)):
    result=list1[i]+list2[i]
    l3.append(result)
print(l3)


       

list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

result = [list1[i]+list2[i]
for i in range(len(list1))]

print(result)




list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
result = []
i = 0
while i < len(list1):
    combined_string = list1[i] + list2[i]
    result.append(combined_string)
    i += 1
print(result)



list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
result = []
i = 0
while i < len(list1):
    l3.append(list1[i]+list2[i])
    i+=1
print(l3)



# ---> Functions

# Defintion:

# Function is a block of code which is used to perform a specific functionality.
# Function can be created using def keyword.

# Function has 3 parts

1) Function declaration
2) Function definition
3) Function call



# Eg:1
def greet():  # function definition
    print("Greeting User!!")



# Eg:2
# Function with parameter
def greeting(name):
    print("Welcome",name)
   
for val in range(3):
       username=input("Enter the name: ")
       greeting(username)  # username is argument


'''


#Eg:3


