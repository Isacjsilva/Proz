def calcular_idade(ano_atual, ano_nascimento):
    return ano_atual - ano_nascimento

def main():
    while True:
        nome_completo = input("Digite seu nome completo: ")
        ano_nascimento_str = input("Digite seu ano de nascimento (entre 1922 e 2021): ")
        
        try:
            ano_nascimento = int(ano_nascimento_str)
            if ano_nascimento < 1922 or ano_nascimento > 2021:
                raise ValueError("Ano de nascimento fora do intervalo permitido.")
            
            idade = calcular_idade(2022, ano_nascimento)
            print(f"Nome: {nome_completo}")
            print(f"Idade: {idade} anos (completou ou completará em 2022)")

            break
        except ValueError as e:
            print(f"Erro: {e}")
            print("Por favor, insira um ano válido.")

if __name__ == "__main__":
    main()
