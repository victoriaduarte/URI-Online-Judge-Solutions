# --------------------------
# URI: https://www.urionlinejudge.com.br/judge/en/problems/view/1114
# Problema 1114 | Senha fixa
# --------------------------

chave_certa = 2002
while True:
    senha = int(input())
    if senha == chave_certa:
        print("Acesso Permitido")
        break
    print("Senha Invalida")

