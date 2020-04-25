'''
   1 1 1 1 1
   1 2 2 2 1
   1 2 3 2 1
   1 2 2 2 1
   1 1 1 1 1
'''
n=int(input("enter the value"))
t=(n*2)-1
c=t+1
n1=1
n2=1
for j in range(1,n):
  for k in range(1,j+1):
        print(n2,end=" ")
        n2=n2+1
  for i in range(1,(2*(n-j))):
       print(n1,end=" ")
  n1=n1+1
  n2= n
  n4=n-j
  for l in range(1,j+1):
       print(n4-1)
       n4=n4-1
  print("\r")
