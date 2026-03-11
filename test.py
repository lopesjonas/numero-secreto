# Gerador de tabuada e operações matemáticas simples

def gerar_tabuada_multiplicacao(numero, inicio=1, fim=10):
    print(f"Tabuada de Multiplicação do {numero} (de {inicio} a {fim}):")
    for i in range(inicio, fim + 1):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

def gerar_tabuada_adicao(numero, inicio=1, fim=10):
    print(f"Tabuada de Adição do {numero} (de {inicio} a {fim}):")
    for i in range(inicio, fim + 1):
        resultado = numero + i
        print(f"{numero} + {i} = {resultado}")

def gerar_tabuada_subtracao(numero, inicio=1, fim=10):
    print(f"Tabuada de Subtração do {numero} (de {inicio} a {fim}):")
    for i in range(inicio, fim + 1):
        resultado = numero - i
        print(f"{numero} - {i} = {resultado}")

def gerar_tabuada_divisao(numero, inicio=1, fim=10):
    print(f"Tabuada de Divisão do {numero} (de {inicio} a {fim}):")
    for i in range(inicio, fim + 1):
        if i == 0:
            print(f"{numero} / {i} = Indefinido (divisão por zero)")
        else:
            resultado = numero / i
            print(f"{numero} / {i} = {resultado:.2f}")

def main():
    print("=== Programa de Operações Matemáticas ===")
    while True:
        print("\nEscolha uma operação:")
        print("1. Multiplicação")
        print("2. Adição")
        print("3. Subtração")
        print("4. Divisão")
        print("5. Sair")
        
        try:
            opcao = int(input("Digite a opção (1-5): "))
            if opcao == 5:
                print("Saindo do programa. Até logo!")
                break
            if opcao not in [1, 2, 3, 4]:
                print("Opção inválida. Tente novamente.")
                continue
            
            num = int(input("Digite um número: "))
            inicio = int(input("Digite o início do intervalo (padrão 1): ") or 1)
            fim = int(input("Digite o fim do intervalo (padrão 10): ") or 10)
            
            if opcao == 1:
                gerar_tabuada_multiplicacao(num, inicio, fim)
            elif opcao == 2:
                gerar_tabuada_adicao(num, inicio, fim)
            elif opcao == 3:
                gerar_tabuada_subtracao(num, inicio, fim)
            elif opcao == 4:
                gerar_tabuada_divisao(num, inicio, fim)
                
        except ValueError:
            print("Por favor, digite um número válido.")
        except KeyboardInterrupt:
            print("\nPrograma interrompido pelo usuário.")
            break

if __name__ == "__main__":
    main()


