'''
25	2	3	4	21	
6	19	8	17	10	
11	12	13	14	15	
16	9	18	7	20	
5	22	23	24	1	
'''

n= int(input())
n_list=[[0 for x in range(n)] for y in range(n)]
num=1
for i in range(n):
 for j in range(n):
  n_list[i][j]=num
  num+=1

i=0
j=n
while i<j:
 n_list[i][i],n_list[j-1][j-1]=n_list[j-1][j-1],n_list[i][i]
 n_list[i][j-1],n_list[j-1][i]=n_list[j-1][i],n_list[i][j-1]
 i=i+1
 j=j-1

for i in range(n):
 for j in range(n):
  print(n_list[i][j],end="\t")
 print("\r")
