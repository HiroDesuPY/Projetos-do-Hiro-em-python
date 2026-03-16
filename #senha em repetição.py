#senha em repetição

import string

senha = input ("digite a sua senha: ")

while True:
    if len(senha) < 8:
        print('*'*5, "ERRO!", '*' *5)
        print ('tamanho deve ser maior que 8 letras!')
        print ("="*30)
        senha = input ("digite novamente a sua senha! ")

    elif not any(l in string.ascii_uppercase for l in senha):
        print('*'*5, "ERRO!", '*' *5)
        print ("A senha deve ter pelo menos um carater maiuscula!")
        print ("="*30)
        senha = input ("digite novamente a sua senha! ")

    elif not any(l in string.digits for l in senha):
        print('*'*5, "ERRO!", '*' *5)
        print ('A senha deve ter pelo menos um ou mais digito!')
        print ('='*30)
        senha = input ("digite novamente a sua senha! ")

    elif not any(l in string.punctuation for l in senha):
        print('*'*5, "ERRO!", '*' *5)
        print (f'A senha deve ter pelo menos um carater especial: {string.punctuation}')
        print ('='*30)
        senha = input ("digite novamente a sua senha! ")

    else:
        print ("Senha forte criada!!")
        break