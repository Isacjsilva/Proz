def calculadora(n1, n2, operacao):
    if operacao == 1:
        return n1 + n2  # Soma
    elif operacao == 2:
        return n1 - n2  # Subtração
    elif operacao == 3:
        return n1 * n2  # Multiplicação
    elif operacao == 4:
        return n1 / n2 if n2 != 0 else 'Erro: Divisão por zero'  # Divisão
    else:
        return 0  # Operação inválida

# Chamada da função e impressão do resultado fora da definição da função
resultado = calculadora(10, 2, 1)
print(resultado)
