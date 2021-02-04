# --------------------------
# URI: https://www.urionlinejudge.com.br/judge/en/problems/view/2936
# Problema 2936 | Quanto Mandioca?
# --------------------------

# Porções de mandioca (em gramas)
curupira = 300
boitata = 1500
boto = 600
mapinguari =1000
iara = 150
dona_chica = 225  # Dona Chica sempre come 225 gramas

# Quantidade de porções (p)
p_curupira = int(input())
p_boitata = int(input())
p_boto = int(input())
p_mapinguari = int(input())
p_iara = int(input())

# Total de mandioca
total = ((curupira*p_curupira) + (boitata*p_boitata) + (boto*p_boto) + (mapinguari*p_mapinguari) + (iara*p_iara) + (dona_chica))

# Imprime a quantidade de mandioca que a Dona Chica deve preparar
print("\nDona Chica deve preparar", total, "gramas de mandioca.")