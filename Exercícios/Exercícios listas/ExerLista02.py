R = set([1,2,3,4,5])
S = set()
    
for i in range (10):
    S.add(int(input("Digite um valor inteiro pra S: ")))
    
X = R & S
    
print(f"vc tirou {len(X)} pontos")