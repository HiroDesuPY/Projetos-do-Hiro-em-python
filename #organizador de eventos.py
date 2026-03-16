#organizador de eventos

num_adulto = int(input("insira o número de adultos: "))
num_crianca = int(input("insira o número de crianças: "))
carne_grama = 0
carne_crianca_grama = 0
bebida_litro = 0
bebida_crianca_litro = 0

for i in range(num_adulto):
    carne_grama += 150
    bebida_litro += 1



for i in range(num_crianca):
    idade_criança = int(input(f"{i + 1} - insira a idade da criança: "))

    if idade_criança <= 3:
        carne_crianca_grama += 40
        bebida_crianca_litro += 0.5
    
    elif idade_criança <= 8:
        carne_crianca_grama += 60
        bebida_crianca_litro += 0.75

    elif idade_criança <= 13:
        carne_crianca_grama += 90
        bebida_crianca_litro += 1

carne_total_grama = carne_grama + carne_crianca_grama
carne_total_kg = carne_total_grama / 1000
bebida_total_litro = bebida_litro + bebida_crianca_litro


print(f"Quantidade total de carne necessária: {carne_total_kg} kg")
print(f"Quantidade total de bebida necessária: {bebida_total_litro} litros")

