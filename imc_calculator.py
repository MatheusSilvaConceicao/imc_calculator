# Função para calcular o Índice de Massa Corporal (IMC)
def imc_calculator():
    try:
        # Solicita a altura do usuário e converte para float
        height = float(input("Digite sua altura: "))
        if height <= 0:  # Verifica se a altura é válida
            print("Altura inválida! Digite um valor maior que zero.")
            return  # Sai da função se o valor for inválido

        # Solicita o peso do usuário e converte para float
        weight = float(input("Digite seu peso: "))
        if weight <= 0:  # Verifica se o peso é válido
            print("Peso inválido! Digite um valor maior que zero.")
            return  # Sai da função se o valor for inválido
    
        # Calcula o IMC (peso dividido pelo quadrado da altura)
        imc = weight / (height ** 2)

        # Classifica o IMC de acordo com a tabela oficial da OMS
        if imc < 18.5:
            classification = "Magreza"
        elif imc <= 24.9:
            classification = "Normal"
        elif imc <= 29.9:
            classification = "Sobrepeso"
        elif imc <= 34.9:
            classification = "Obesidade grau I"
        elif imc <= 39.9:
            classification = "Obesidade grau II"
        else:
            classification = "Obesidade grau III"

        # Exibe o resultado formatado com duas casas decimais
        print(f"Seu IMC é de {imc:.2f} e sua classificação é {classification}")
    
    except ValueError:
        # Captura erro caso o usuário digite algo que não seja um número
        print("Entrada inválida! Digite apenas números.")

# Loop principal para exibir o menu e interagir com o usuário
while True:
    print('''
    ======= IMC CALCULATOR =======   
    01 - Iniciar
    02 - Sair      
    ==============================
    ''')

    try:
        # Solicita a opção do usuário
        option = int(input("Digite a opção desejada: "))
    except ValueError:
        print("Digite uma opção válida")  # Mensagem de erro para entrada inválida
        continue  # Volta ao início do loop

    # Executa a função se o usuário escolher "1"
    if option == 1:
        imc_calculator()
    # Encerra o programa se o usuário escolher "2"
    elif option == 2:
        print("Encerramento do programa...")
        break
    # Mensagem de erro caso a opção seja inválida
    else:
        print("Digite uma opção válida!")
