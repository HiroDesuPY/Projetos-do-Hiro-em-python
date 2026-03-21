#Registro do aluno,valor true ou false??
#podemos criar funções calculador de dias disponiveis para utilizar a academia

alunos = {
}
escolha_usu = ['sim','não','nao','s','n']
valor_mensal = 258.00

while True:
    nome = input("Digite o nome do aluno: ")
    valor = float(input("Digite o valor mensal do pagamento do aluno: "))

    if nome in alunos:
        alunos[nome]["pagamento"] += valor
    else:
        alunos[nome] = {"pagamento": valor}

    escolha_usu = input("Você quer sair? sim ou não? ").lower().strip()

    if escolha_usu == 'sim' or escolha_usu == 's':
        break

    elif escolha_usu == 'não' or escolha_usu == 'nao' or escolha_usu == 'n':
        continue

    else:
        print ('*'*30)
        escolha_usu = input("Faça escolha certa!")
        print ('='*30)

for val in alunos:
    if valor_mensal <= alunos[val]["pagamento"]:
        credito = alunos[val]["pagamento"] - valor_mensal
        print (f"{val} pagou o valor mínimo de R${valor_mensal:.2f}. Seu crédito é de R${credito:.2f}")

    else:
        print(f"{val} não pagou o valor mínimo de R${valor_mensal:.2}")

print (alunos)
    










