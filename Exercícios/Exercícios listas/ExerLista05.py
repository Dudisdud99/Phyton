R = set()
S = set()

for i in range (10):
    R.add(int(input("Digite um valor inteiro pra R: ")))
    
print("\n")
    
for i in range (10):
    S.add(int(input("Digite um valor inteiro pra S: ")))
    
X = R -S
    
print(f"R sem S e : {X}")