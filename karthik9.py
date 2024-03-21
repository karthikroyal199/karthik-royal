''
s1 = "hello are you"
s2 = "hello how is"

s1 = s1.split("")
s2 = s2.split("")


for val in s1:
    if val not in s2:
        print(val)
for val in s2:
    if val not in s1:
        print(val)


num=5
n1=0
n2=1

for val in range(5):
    ans = n1+n2
    n1 = n2
    n2 = ans
print(ans)


# ! Constructors
# ? Eg:2
# * unparametaraised constructor
class profile
def _init_(self):
    print("hello world")
obj = profile()
obj._init_()
'''
# ? Eg:3
# * parametaraised Constructor
class profile:
    def _init_(self,id,name,age):
        print(id,name,age)
   
obj = profile(1,"hari",18)
   
# ? Eg:4
class c1:
    name = "sid"
    place = "cbe"


    def m1(self):
        name="sid"
        place="cbe"
        print(name,place)
     
object = c1()
object.m1()
   


# ? Eg:5
class c1:
    def m1(self):
        name = "sid"
        age = 28

    def display(self):
        print(self.name,self.age)


object = c1()
object.display()

'''






# hybrid Inheritance
 # The combination of above 4 inheritance is called Hybrid inheritance
class c1:
    def m1(self):
        print("Class1")
class c2:
    def m2(self):
        print("class2")
class c3:
    def m3(self):
        print("Class 3")
class c4:
    def m4(self):
        print("Class 4")
class c5:
    def m5(self):
        print("Class 5")
class c6:
    def m6(self):
        print("Class 6")






















i,.,
