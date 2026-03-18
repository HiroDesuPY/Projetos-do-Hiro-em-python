#Verificador da senha
import string

senha = input ('digite a senha: ')

maiuscula = any(letra in string.ascii_uppercase for letra in senha)
minuscula = any(letra in string.ascii_lowercase for letra in senha)
numeros = any(letra in string.digits for letra in senha)
caracteres_especiais = any(letra in string.punctuation for letra in senha)
tamanho_min = len(senha) >= 8

erros = []

if not maiuscula:
    erros.append("Ter pelo menos um carater maiuscula!")

if not minuscula:
    erros.append("ter pelo menos um carater minuscula!")

if not caracteres_especiais:
    erros.append (f"ter pelo menos um carater especial! Letras especias: {string.punctuation}")

if not numeros:
    erros.append ("A senha deve ter digitos!")

if not tamanho_min:
    erros.append ("Tamanho minimo igual ou maior a 8!")


#_----------------------------------------_

if not erros:
    print ('senha criada!')

else:
    print("senha invalida!")
    print(f"A senha deve ter: {erros}")
