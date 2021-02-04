# --------------------------
# URI: https://www.urionlinejudge.com.br/judge/en/problems/view/2373
# Problema 2373 | Garçom
# --------------------------

num_bandejas = int(input())

copos_quebrados = 0
for i in range(num_bandejas):
    num_latas, num_copos = [int(w) for w in input().split()]
    if num_latas > num_copos:
        copos_quebrados += num_copos

print(copos_quebrados)