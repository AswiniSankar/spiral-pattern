'''n=int(input("enter the value..\n"))
for i in range(n):
 for j in range(n):
  if i==0 or i==n-1 or j==0 or j==n-1 or i==j or j==n-1-i:
   print("* ",end=" ")
  else:
   if j>=i+1 and j<=n-i-1:
     print("# ",end=" ")
   elif j<i+1 and j>n-i-1:
     print("@ ",end=" ")
   elif j<=i-1:
     print("% ",end=" ")
   elif j>=n-i-1:
     print("$ ",end=" ")
   else:
     print("  ",end=" ")
 print("\r")'''
'''

0 0 2 0 4 

0 1 2 1 4 

0 2 2 2 4 

0 3 2 3 4 

0 4 2 4 4 

'''

n=int(input())
for i in range(n):
 for j in range(n):
  if j%2==0:
   print(j,end=' ')
  else:
   print(i,end=' ')
 print("\n")
