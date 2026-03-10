# Projeto Meteorologica Fase 1. L-P

#extensos:

meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", 
         "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

# Variáveis de controle ---------------------------------------------------------------------------
média_anual = 0
meses_escaldantes = 0
maior_temperatura = -61  
menor_temperatura = 51   
mes_quente = 0
mes_frio = 0
#----------------------------------------------------------------------------------------
for cont in range(1, 13):
    while True:
        temperatura_mês = float(input(f'Digite a temperatura máxima de {meses[cont-1]} em graus Celsius: '))
        
        
        if temperatura_mês > 50 or temperatura_mês < -60:
            print(f'{"!"*5} ERRO: Temperatura inválida! {"!"*5}')
            print('Por favor, digite um valor entre -60 e 50 graus Celsius.')
            print('=' * 50)
        else:    
            média_anual += temperatura_mês

            if temperatura_mês > 33:
                meses_escaldantes += 1

            if temperatura_mês >= maior_temperatura:
                maior_temperatura = temperatura_mês
                mes_quente = cont

            if temperatura_mês <= menor_temperatura:
                menor_temperatura = temperatura_mês
                mes_frio = cont
            
            break 
#----------------------------------------------------------------------------------------
# Cálculos finais
média_anual /= 12
#----------------------------------------------------------------------------------------
print('=' * 40)
print(f' A média anual de temperatura é: {média_anual:.2f}°C')
print(f' Quantidade de meses escaldantes (Temperatura maior que 33°C): {meses_escaldantes} meses')
print('-' * 40)
print(f' MAIOR temperatura: {maior_temperatura:.1f}°C em {meses[mes_quente - 1]}')
print(f' MENOR temperatura: {menor_temperatura:.1f}°C em {meses[mes_frio - 1]}')
print('=' * 40)