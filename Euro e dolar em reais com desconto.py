moeda = input('Digite a moeda (euro ou dolar): ').lower().strip()
valor = float(input('Digite o valor da moeda: '))


if moeda == 'euro':
    valor_em_reais = valor * 6.1
    taxa_iof = (valor_em_reais * 6.83) * 0.01
    valor_em_reais = valor_em_reais + taxa_iof
    print(f'O valor em reais com desconto é: R${valor_em_reais:.2f}')

elif moeda == 'dolar':
    valor_em_reais = valor * 5.2
    taxa_iof = (valor_em_reais * 6.83) * 0.01
    valor_em_reais = valor_em_reais + taxa_iof
    print(f'O valor em reais com desconto é: R${valor_em_reais:.2f}')