"""
Programa criado utilizando apenas funções built-in
"""

print("Programa para análise de valores por período de tempo\
retorna a média, maior e menor valor")
print("Digite ao menos 3 conjuntos de dados.\n")

recebidos = {}  # Dicionário que vai receber os inputs key = ano e value = valor
contagem = 0    # Contador criado para que a opção de sair só apareça após a terceira inserção

while True:
    # Função que recebe os inputs
    finalizar = ''
    ano = int(input("Digite o ano: "))
    valor = int(input("Digite o valor médio nesse ano: "))
    recebidos[ano] = valor  # Inserção dos valores no dict recebidos
    if contagem > 1:    # implementação da contagem que começa a valer a partir da terceira inserção
        finalizar = input("Digite '1' para sair ou 'Enter' para continuar ") # exibe comando de sair
    else:
        contagem += 1   # acresce o contador a cada repetição
    if finalizar == '1':    # finaliza o programa quando 1 é digitado na opção de sair ou continuar
        break

valores = recebidos.values()    # cria a variável valores para reduzir a quantidade de escrita
maior = {}
menor = {}
media = sum(valores) / len(valores)     # Calculo da média a partir dos valores da contagem

print("\n", "=" * 30, "\n")
print(f"Foram analisados valores coletados em {len(valores)} anos")

for ano, valor in recebidos.items():
    # Função que separa e imprime os maiores e menores valores e seus respectivos anos
    if valor == max(valores):
        maior[ano] = valor
        print(f"O maior valor foi de R$ {valor:4.2f} no ano de {ano}")
    if valor == min(valores):
        menor[ano] = valor
        print(f"O menor valor foi de R$ {valor:4.2f} no ano de {ano}")

print(f"A média do período é de R${media:4.2f}")
print("\n", "=" * 30, "\n")

