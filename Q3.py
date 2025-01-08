def calculadora():
    while True:
        print("\nEscolha a operação:")
        print("1: Soma")
        print("2: Subtração")
        print("3: Multiplicação")
        print("4: Divisão")
        print("0: Sair")

        opcao = input("Digite o número da operação: ")

        if opcao == '0':
            print("Encerrando o programa...")
            break
        elif opcao in ['1', '2', '3', '4']:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            if opcao == '1':
                resultado = num1 + num2
                operacao = "soma"
            elif opcao == '2':
                resultado = num1 - num2
                operacao = "subtração"
            elif opcao == '3':
                resultado = num1 * num2
                operacao = "multiplicação"
            elif opcao == '4':
                if num2 != 0:
                    resultado = num1 / num2
                    operacao = "divisão"
                else:
                    print("Erro: Divisão por zero não é permitida.")
                    continue

            print(f"Resultado da {operacao}: {resultado}")
        else:
            print("Essa opção não existe.")

if __name__ == "__main__":
    calculadora()
