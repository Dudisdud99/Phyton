x = input("Digite dd/mm/aaaa: ")

z = x.split("/")

if z[1] == '01': 
    z[1] = 'janeiro'
elif z[1] == '02': 
    z[1] = 'feverero'
elif z[1] == '03': 
    z[1] = 'março'
elif z[1] == '04': 
    z[1] = 'abril'
elif z[1] == '05': 
    z[1] = 'maio'
elif z[1] == '06': 
    z[1] = 'julho'
elif z[1] == '07': 
    z[1] = 'junho'
elif z[1] == '08': 
    z[1] = 'agosto'
elif z[1] == '09': 
    z[1] = 'setembro'
elif z[1] == '10': 
    z[1] = 'outubro'
elif z[1] == '11': 
    z[1] = 'novembro'
elif z[1] == '12': 
    z[1] = 'dezembro'
    
print(f"Vc nasceu em {z[0]} de {z[1]} de {z[2]}")