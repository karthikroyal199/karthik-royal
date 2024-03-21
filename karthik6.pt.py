# to  print the first and last letters are capitalize
'''
s1="hello world"
fst=s1[0].upper()
lst=s1[-1].upper()
print(fst+s1[1:len(s1)-1]+lst)

n=128
i=0
while n!=0:
    rem=n%10
    print(rem)
    n=n/10

#add both l1 and l2 ---> ans[6,8,10,12]
l1=[1,2,3,4]
l2=[5,6,7,8]

'''
#############################################


'''
n=128
temp=n
f1=0
while n!=0:
    rem=n%10
    check=temp%rem
    if check!=0:
        f1=1
    n=n//10
if f1==0:
    print("yes")
else:
     print("no")
'''


#add both l1 and l2 ---> ans[6,8,10,12]
l1=[1,2,3,4]
l2=[5,6,7,8]
l3=[]
#print(l1[0]+l2[0],l1[1]+l2[1],l1[2]+l2[2],l1[3]+l2[3])
for val in range(len(l1)):
    ans=l1[val]+l2[val]
    l3.append(ans)
print(l3)






































