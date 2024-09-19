K = []

for i in range (2,11):
    K.append(i)
    
print(K,"\n")

for i in range (len(K)):
    cont = 0
    for x in range (1,K[i]):
        if K[i]/x == 0:
            cont+=1
    if cont == 2:
        print(K[i])
        
    