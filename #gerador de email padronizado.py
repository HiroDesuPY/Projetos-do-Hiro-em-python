#gerador de email padronizado
#.lower().strip()
#variavel = ''.join()


nome = input("Digite o nome completo do funcionário: ").lower().strip()

nome_separado = nome.split()

primeiro_nome = nome_separado[0]
sobrenome = nome_separado[-1]

if nome_separado[1:-1]:
    nome_meio = nome_separado[1:-1]
    iniciais = ''.join([separa[0] for separa in nome_meio])
    email = f"{primeiro_nome}.{iniciais}.{sobrenome}@empresa.com"
else:
    email = f"{primeiro_nome}.{sobrenome}@empresa.com"

print(email)

