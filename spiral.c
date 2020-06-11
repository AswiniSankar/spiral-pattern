/*
ip::5
op::
   1   2   3   4   5
   6   7   8   9  10
  11  12  13  14  15
  16  17  18  19  20
  21  22  23  24  25
*/
#include<stdio.h>
int main()
{
  int n,i,j,k=1;
  scanf("%d",&n);
  for(i=0;i<n;i++)
  {for(j=0;j<n;j++)
   {
     printf("%4d",k);
     k++;
   }
   printf("\n");
  }
  printf("\n");
 return 0;
}
/*

ip::6
op::
   1   2   3   4   5   6
  12  11  10   9   8   7
  13  14  15  16  17  18
  24  23  22  21  20  19
  25  26  27  28  29  30
  36  35  34  33  32  31
*/
#include<stdio.h>
int main()
{
  int n,i,j,k=1,l,c=2;
  scanf("%d",&n);
 
  for(i=0;i<n;i++)
  {if(i%2==0)
  {
   for(j=0;j<n;j++)
   {
     printf("%4d",k);
     k++;
   }
   k=k+n;
   printf("\n");
  }
 else
   { l=n*c;
   for(j=0;j<n;j++)
   {
     printf("%4d",l);
    l--;
   }
   c=c+2;
   printf("\n");
  }
  
  }
  printf("\n");
 return 0;
}
