x = 0
i = 2
while x<10:
    ii = 2
    while True:
        if i%ii!=0:
            ii+=1
        else:
            print(i)
            x+=1
            break
    i+=1