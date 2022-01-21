d='Goodbye'
w=input()
t=0
for i in w:
    if i==d[t]:
        t+=1
        if t==7:
            break
if t==7:
    print("Yes")
else:
    print("No")
