# --------------------------
# URI: https://www.urionlinejudge.com.br/judge/en/problems/view/2456
# Problema 2456 | Cartas
# --------------------------

# Valores das cartas
cartas = [int(x) for x in input().split()]

count = 0
for i in range(len(cartas)-1):
    if cartas[i] < cartas[i+1]:
        count += 1
    i += 1

if count < 1:
    ordem = "D"  # sequência ordenada de forma decrescente
elif count == i:
    ordem = "C"  # sequência ordenada de forma crescente
else:
    ordem = "N"  # sequência desordenada

print(ordem)