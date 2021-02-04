# --------------------------
# URI: https://www.urionlinejudge.com.br/judge/en/problems/view/2423
# Problema 2423 | Receita de Bolo
# --------------------------

# Receita
# a = farinha (2*x)
# b = ovos (3*x)
# c = leite (5*x)

a, b, c = [int(w) for w in input().split()]

farinha = a//2
ovos = b//3
leite = c//5

# Imprime a quantidade máxima de bolos
print(min(farinha, ovos, leite))