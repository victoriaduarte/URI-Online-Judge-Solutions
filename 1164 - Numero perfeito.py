# --------------------------
# URI: https://www.urionlinejudge.com.br/judge/en/problems/view/1164
# Problema 1164 | Número perfeito
# --------------------------

# Na matemática, um número perfeito é um inteiro para o qual a soma de todos os seus próprios divisores positivos (excluindo a si mesmo) é igual ao próprio número.
# Por exemplo o número 6 é perfeito, pois 1 + 2 + 3 é igual a 6.

# Quantidade de casos de teste
casos_teste = int(input())

i = 0
while i < casos_teste:
    num = int(input())
    i += 1

    soma = 0
    for x in range(1, num):
        if (num % x) == 0:
            soma = soma + x  # acumula todos os divisores de 'num' na variável 'soma'

    if soma == num:  # o número é perfeito se a soma de todos os seus divisores for igual ao próprio número
        print(num, "eh perfeito")
    else:
        print(num, "nao eh perfeito")