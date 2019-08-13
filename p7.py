n1=input()
n=list(n1)
for i in range(0,len(n)-1,2):
   c=n[i]
   n[i]=n[i+1]
   n[i+1]=c
for i in n:
   print(i,end="")
