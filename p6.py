s,v=map(str,input().split())
if(len(s)!=len(v)):
 print("no")
else:
 s21=[s.count(i) for i in s]
 s31=[v.count(i) for i in v]
if(s21==s31):
 print("yes")
else:
 print("no")
