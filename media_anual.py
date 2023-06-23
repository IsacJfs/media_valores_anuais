"""
Programa criado utilizando apenas funções built-in
"""

print("Programa para análise de valores por período de tempo\
retorna a média, maior e menor valor")
print("Digite ao menos 3 conjuntos de dados.\n")


def analise_anual(dados_coletados: dict) -> tuple:
    """
    :param dados_coletados: dicionário contendo ano como key e valor da média como value
    :return: tupla com os valores (maior, menor, média)
    """
    valores = dados_coletados.values()  # cria a variável valores para reduzir a quantidade de escrita
    maior_calculado = max(dados_coletados.values())
    menor_calculado = min(dados_coletados.values())
    media_calculado = round(sum(valores) / len(valores), 2)  # Calculo da média a partir dos valores da contagem
    resultado_analise = (maior_calculado, menor_calculado, media_calculado)
    return resultado_analise


def coleta_dados() -> dict:
    """
    Função que coleta uma quantidade > 3 de dados via input
    :return:  um dicionário contendo ano como key e valor da média como value
    """
    recebidos = {}  # Dicionário que vai receber os inputs key = ano e value = valor
    contagem = 0  # Contador criado para que a opção de sair só apareça após a terceira inserção

    while True:
        # Função que recebe os inputs
        finalizar = ''
        ano = int(input("Digite o ano: "))
        valor = int(input("Digite o valor médio nesse ano: "))
        recebidos[ano] = valor  # Inserção dos valores no dict recebidos
        if contagem > 1:  # implementação da contagem que começa a valer a partir da terceira inserção
            finalizar = input("Digite '1' para sair ou 'Enter' para continuar ")  # exibe comando de sair
        else:
            contagem += 1  # acresce o contador a cada repetição
        if finalizar == '1':  # finaliza o programa quando 1 é digitado na opção de sair ou continuar
            break

    return recebidos


maior, menor, media = analise_anual(coleta_dados())

print("\n", "=" * 30, "\n")
print(f"A média do período é de R$ {media}")
print(f"O maior valor foi de R$ {maior}")
print(f"O menor valor foi de R$ {menor}")
print("\n", "=" * 30, "\n")
