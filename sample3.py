'''
5 5 5 5 5 5 5 5 5 
5 4 4 4 4 4 4 4 5 
5 4 3 3 3 3 3 4 5 
5 4 3 2 2 2 3 4 5 
5 4 3 2 1 2 3 4 5 
5 4 3 2 2 2 3 4 5 
5 4 3 3 3 3 3 4 5 
5 4 4 4 4 4 4 4 5 
5 5 5 5 5 5 5 5 5 
'''

num=int(input("enter the number..."))
n_list=[[0 for x in range((2*num)-1)] for y in range((2*num)-1)]

n=num
low=0
high=(2*num)-2

for i in range(n):
 for j in range(low,high+1):
   n_list[i][j]=n
 for j in range(low+1,high+1):
   n_list[j][high]=n
 for j in range(high-1,low-1,-1):
   n_list[high][j]=n
 for j in range(high-1,low,-1):
   n_list[j][low]=n
 n-=1
 low+=1
 high-=1




for i in range((2*num)-1):
 for j in range((2*num)-1):
  print(n_list[i][j],end=" ")
 print("\r")
