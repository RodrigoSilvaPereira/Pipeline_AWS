import random
import time
import names

random.seed(40)

qtd_nomes_unicos = 3000
qtd_nomes_aleatorios = 10000000

aux = []

for i in range(0, qtd_nomes_unicos):
    aux.append(names.get_full_name())

print("Gerando {} nomes aleatórios".format(qtd_nomes_aleatorios))

dados = []

for i in range(0, qtd_nomes_aleatorios):
    dados.append(random.choice(aux))

nome_arquivo = "nomes_aleatorios.txt"

with open(nome_arquivo, "w") as arquivo:

    for nome in dados:
        arquivo.write(nome + "\n")

print("Arquivo '{}' gerado com sucesso!".format(nome_arquivo))

with open(nome_arquivo, "r") as arquivo:
    conteudo = arquivo.read()

print("Conteúdo do arquivo:")
print(conteudo)
