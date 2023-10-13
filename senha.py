import random
import string

def gerar_senha_forte(tamanho=24):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

senhas_geradas = []

for i in range(100):
    senha = gerar_senha_forte(8)
    senhas_geradas.append(senha)
    print(senhas_geradas)
    
with open('senhasGerada.txt', 'a') as arquivo:
    for senha in senhas_geradas:
        arquivo.write(senha + "\n")

print('Senhas geradas e armazenadas em senhasGerada.txt')