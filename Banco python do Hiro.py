#esse projeto tem como objetivo de utilizar aprendizado obtido na aula 1 - 3 da lógica e programação.

#-------simulador de banco---------

print ('Bem-vindo ao Banco do Hiro.py')
print ('Por favor, escolha uma opção: ')
print ('1 - Ver o saldo')
print ('2 - Realizar depósito')
print ('3 - Realizar saque')
print ('4 - Sair')

#Saldo fixo para teste: R$500.00
saldo = 500.00

escolha = int(input('Digite o número da opção desejada: '))

if escolha == 1:
    print (f'seu saldo atual é: R${saldo:.2f}')

elif escolha == 2:
    valor_depositado = float(input('Digite o valor a ser depositado: R$'))
    saldo = saldo + valor_depositado
    print (f'você depositou R${valor_depositado:.2f}. Seu novo saldo é: R${saldo:.2f}')

elif escolha == 3:
    valor_saque = float(input('Digite o valor desejado para o saque: R$'))
    if valor_saque > saldo:
        print ('Por favor, insira um valor válido para o saque.')
    else:
        saldo = saldo - valor_saque
        print (f'você sacou R${valor_saque:.2f}. Seu novo saldo é: R${saldo:.2f}')
elif escolha == 4:
    print ('Obrigado por usar o Banco do Hiro.py. Tenha um ótimo dia!')

else:
    print ('Opção inválida. Por favor, escolha uma opção válida.')
        
