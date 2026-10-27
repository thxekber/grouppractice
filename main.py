print("hi")
for i in range (1,100):
    for j in range(1,i+1):
        s=0
        if i%j==0:
            s+=1
    if s==2:
        print(i)
