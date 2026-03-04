import random
# ========= simulador de jogo pedra, papel e tesoura =================

print ('Bem-vindo ao jogo de Pedra, Papel e Tesoura!')
jogador = input ('Digite a sua escolha [pe]dra, [pa]pel ou [t]esoura: ')
computador = random.choice(['pe', 'pa', 't'])
print (f'Computador escolheu: {computador}')

if jogador == computador: print ('Empate!!!')

elif jogador == 'pe':
    if computador == 't':
        print ('Parabéns, você ganhou!!!')
    else:
        print ('Que pena, você perdeu!!!')
elif jogador == 'pa':
    if computador == 'pe':
        print ('Parabéns, você ganhou!!!')
    else:
        print ('Que pena, você perdeu!!!')

elif jogador == 't':
    if computador == 'pa':
        print ('Parabéns, você ganhou!!!')
    else:
        print ('Que pena, você perdeu!!!')
    




