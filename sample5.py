'''
1	2	3	4	5	
11	12	13	14	15	
0	0	0	0	0	
16	17	18	19	20	
6	7	8	9	10	
'''
num=int(input())
n_list=[[0 for x in range(num)] for y in range(num)]
n=1
low=0
high=num-1
while low<high:
 for j in range(num):
  n_list[low][j]=n
  n+=1
 for j in range(num):
  n_list[high][j]=n
  n+=1
 low+=1
 high-=1

for i in range(num):
 for j in range(num):
  print(n_list[i][j],end='\t')
 print("\r")
