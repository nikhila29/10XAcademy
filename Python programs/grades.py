n=int(input())
grade=[]
for _ in range(n):
    grade.append(int(input()))
for x,i in enumerate(grade):
    if(i>=38) and (i%5)>=3:
        grade[x]=i+5-(i%5)
for i in grade:
    print(i)
