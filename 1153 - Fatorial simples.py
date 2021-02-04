# --------------------------
# URI: https://www.urionlinejudge.com.br/judge/en/problems/view/1153
# Problema 1153 | Fatorial simples
# --------------------------

n = int(input())

i = 1
fatorial = 1
while i <= n:
    fatorial *= i  # ex: se n = 3, fatorial = (1 * 1) + (1 * 2) + (1 * 3) = 6
    i += 1

print(fatorial)