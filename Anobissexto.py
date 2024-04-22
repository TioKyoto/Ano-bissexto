def verificar_bissexto(ano):
    # Verifica se o ano é divisível por 4 e não por 100, ou se é divisível por 400
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        return True
    else:
        return False

def explicar_bissexto(ano):
    if verificar_bissexto(ano):
        return f"O ano {ano} é bissexto, pois possui 366 dias."
    else:
        return f"O ano {ano} não é bissexto, pois possui 365 dias."

# Solicita ao usuário que insira o ano desejado
ano_desejado = int(input("Digite o ano que deseja verificar: "))

# Verifica se o ano é bissexto e fornece a explicação correspondente
resultado = explicar_bissexto(ano_desejado)
print(resultado)
