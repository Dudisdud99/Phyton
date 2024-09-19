K = []
par = []
impar = []
contImpar = 0
contPar = 0
    
for i in range (20):
    K.append(int(input("Digite um valor inteiro pra K: ")))
    
for i in range (20):
    if K[i]%2 == 0:
        par.append(K[i])
    else:
        impar.append(K[i])
        
for i in range (20):
    if i%2 == 0:
        K[i] = par[contPar]
        contPar+=1
    else:
        K[i] = impar[contImpar]
        contImpar+=1
    
print(K)