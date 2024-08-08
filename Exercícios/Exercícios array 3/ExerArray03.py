x = input("Digite dia/mes/ano: ")

x.split("/")

if x[1] == '01': 
    x[1] = 'janeiro'
elif x[1] == '02': 
    x[1] = 'feverero'
elif x[1] == '03': 
    x[1] = 'março'
elif x[1] == '04': 
    x[1] = 'abril'
elif x[1] == '05': 
    x[1] = 'maio'
elif x[1] == '06': 
    x[1] = 'julho'
elif x[1] == '07': 
    x[1] = 'junho'
elif x[1] == '08': 
    x[1] = 'agosto'
elif x[1] == '09': 
    x[1] = 'setembro'
elif x[1] == '10': 
    x[1] = 'outubro'
elif x[1] == '11': 
    x[1] = 'novembro'
elif x[1] == '12': 
    x[1] = 'dezembro'  
    
print(f"Vc nasceu em {x[0]} de {x[1]} de {x[2]}")