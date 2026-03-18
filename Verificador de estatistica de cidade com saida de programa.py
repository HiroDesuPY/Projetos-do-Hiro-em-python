# estatistica de uma cidade com uma "escape", idade , salario

generolista = ['masculino','feminino']
escolha = ['sim','não']
programa = True


mulherescom3500 = 0
menor = float('inf')  # Inicializa com infinito para encontrar o mínimo
maior = float('-inf')  # Inicializa com -infinito para encontrar o máximo
salarioT = 0
f3500 = 0
pessoa = 0
def repeat(sim):
    while True:

    
        genero = input("Digite o seu genero: ").lower().strip()

        if genero in generolista:
            pessoa += 1

        if genero not in generolista:
            print ('x'*30)
            print ('Genero incorreto!')
            print ('='*30)
            genero = input("Digite genero novamento: ")

        idade = int(input("Digite a idade: "))
        if idade < 0 or idade > 100:
            print ('x'*30)
            print ('Idade incorreto!')
            print ('='*30)
            idade = input("Digite idade novamento: ")


        salario = float(input("Informe o salario: "))
        if salario < 0:
            print ('x'*30)
            print ('Salario incorreto!')
            print ('='*30)
            idade = input("Digite salario novamento: ")



        salarioT += salario

        if idade > maior:
            maior = idade

        if menor > idade:
            menor = idade


        if genero == "feminino" and salario >= 3500:
            f3500 += 1


        mediaSa = salarioT / pessoa


        escolha_usuario = input("Você quer sair? Sim ou não. ")

        if escolha_usuario not in escolha:
            escolha_usuario = input ("Sim ou não? ")

        if escolha_usuario == 'sim':
            break

        if escolha_usuario == 'não':
            repeat


    
    

while True:

    
    genero = input("Digite o seu genero: ").lower().strip()

    if genero in generolista:
        pessoa += 1

    if genero not in generolista:
        print ('x'*30)
        print ('Genero incorreto!')
        print ('='*30)
        genero = input("Digite genero novamento: ")

    idade = int(input("Digite a idade: "))
    if idade < 0 or idade > 100:
        print ('x'*30)
        print ('Idade incorreto!')
        print ('='*30)
        idade = input("Digite idade novamento: ")


    salario = float(input("Informe o salario: "))
    if salario < 0:
        print ('x'*30)
        print ('Salario incorreto!')
        print ('='*30)
        idade = input("Digite salario novamento: ")



    salarioT += salario

    if idade > maior:
        maior = idade

    if menor > idade:
        menor = idade


    if genero == "feminino" and salario >= 3500:
        f3500 += 1


    mediaSa = salarioT / pessoa


    escolha_usuario = input("Você quer sair? Sim ou não. ")

    if escolha_usuario not in escolha:
        escolha_usuario = input ("Sim ou não? ").lower().strip()

    if escolha_usuario == 'sim':
        break

    if escolha_usuario == 'não':
        repeat

print (f'maior {maior}')

print (f'menor {menor}')

print (f'media salarial: {mediaSa}')

print (f'mulher com 3500 > : {f3500} mulheres')

print (f'total de pessoas na estat. {pessoa}')




    

    



    

    


    



    



