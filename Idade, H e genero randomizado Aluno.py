#idade, altura, genero
import random

alunos = int(input("Quantidade de alunos: "))
listagenero = ['m','f']
idadeT = 0
alturaF = 0
est20 = 0
estudanteVe = 0
alturaVelho = 0
meninas = 0

for cont in range (alunos):
    genero = random.choice(['m','f'])


    idade = random.randint (15,29)



    altura = random.uniform (1.4,1.9)


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

print (f'média de idade dos alunos {mediaId:.1f}')
print (f'média de altura feminino {mediaHF:.2f}')
print (f'Percentual dos alunos com mais de 20 anos: {percentual:.1f}% e quantidade {est20}')
print (f"Altura do estudante mais velho {alturaVelho:.2f} e idade {estudanteVe}")

