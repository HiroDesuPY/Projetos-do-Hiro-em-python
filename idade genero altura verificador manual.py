#idade, altura, genero

alunos = int(input("Quantidade de alunos: "))
listagenero = ['m','f']
idadeT = 0
alturaF = 0
est20 = 0
estudanteVe = 0
alturaVelho = 0
meninas = 0

for cont in range (alunos):
    genero = input ('m ou f? ').lower().strip()

    while genero not in listagenero:
        print ('digite genero válido!')
        genero = input ('m ou f? ').lower().strip()

    idade = int(input('Digite a sua idade: '))

    while idade <= 0 or idade >= 30:
        print ("Digite um idade válida de um aluno!")
        idade = int(input('Digite a sua idade: '))

    altura = float(input("Qual a sua altura?? "))

    while altura <= 1.10 or altura >= 2.00:
        print ("Digite uma altura válida de uma pessoa normal!")
        altura = float(input("Qual a sua altura?? "))

    idadeT += idade

    if genero == 'f':
        alturaF += altura
        meninas += 1


    if idade > 20:
        est20 += 1

    
    if idade > estudanteVe:
        estudanteVe = idade
        alturaVelho = altura


mediaId = idadeT / alunos
mediaHF = alturaF / meninas
percentual = (est20 / alunos) * 100

print (f'média de idade dos alunos {mediaId}')
print (f'média de altura feminino {mediaHF}')
print (f'Percentual dos alunos com mais de 20 anos: {percentual}% e quantidade {est20}')
print (f"Altura do estudante mais velho {alturaVelho} e idade {estudanteVe}")



    

    


    



        






        

    







