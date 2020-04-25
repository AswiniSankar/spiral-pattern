'''
17	16	15	14	13	
18	5	4	3	12	
19	6	1	2	11	
20	7	8	9	10	
21	22	23	24	25
'''



num=int(input("enter the number of rows..."))
n_list=[[0 for x in range(num)] for y in range(num)]
n=num*num
low=0
high=num-1
count=int((num+1)/2)
for i in range(count):
 for j in range(high,low-1,-1):
  n_list[high][j]=n
  n-=1
 for j in range(high-1,low-1,-1):
  n_list[j][low]=n
  n-=1
 for j in range(low+1,high+1):
  n_list[low][j]=n
  n-=1
 for j in range(low+1,high):
  n_list[j][high]=n
  n-=1
 low=low+1
 high=high-1



for i in range(num):
 for j in range(num):
  print(n_list[i][j],end="\t")
 print("\r")
