# --------------------------
# URI: https://www.urionlinejudge.com.br/judge/en/problems/view/2189
# Problema 2189 | Quermesse
# --------------------------

i = 1
ingresso_ganhador = 0
while True:
    num_participantes = int(input())
    if num_participantes == 0:
        break
    num_ingresso = [int(x) for x in input().split()]
    j = 1
    for ingresso in num_ingresso:
        if ingresso == j:  # o vencedor é aquele que possui o número do ingresso igual à sua posição (j) de entrada na festa
            ingresso_ganhador = ingresso
        j += 1

    print("Teste %d" %i)
    print(ingresso_ganhador)

    i += 1
