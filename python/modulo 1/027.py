# botando os nomes em maiusculas

nome = input(' qual o seu nome? ')
print(nome.upper())


# botando o sobrenome em minusculo

sobrenome = input(' qual seu sobrenome? ')
print(sobrenome.lower())


# removendo os espaços e vendo quantas letras tem

nom = input(' digita seu nome: ')
nom = nom.strip()
print(' seu nome tem {} letras'.format(len(nom)))

# quantas letras tem o primeiro nome

nomee = input(' qual o seu nome e sobrenome? ')
print(' seu primeiro nome tem {} letras'.format(nomee.find(' ')))