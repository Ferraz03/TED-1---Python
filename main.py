def main():
    # Inicialização das variáveis
    # Em Python, usamos float('inf') e float('-inf') para representar valores 
    # máximos e mínimos infinitos, equivalentes a Double.MAX_VALUE e MIN_VALUE neste contexto.
    maior_altura = float('-inf')
    menor_altura = float('inf')

    total_mulheres = 0
    qtd_homens = 0
    soma_homens = 0.0

    # Loop para 15 pessoas
    for i in range(15):
        print(f"Informe a altura da pessoa número: {i + 1}")
        try:
            altura = float(input())
        except ValueError:
            print("Erro: Digite um número válido para a altura.")
            # Em uma implementação robusta, você poderia decrementar i para repetir a iteração
            # Mas para manter a lógica idêntica ao Java, assumimos entrada válida ou encerramos.
            return 

        genero_valido = ' '

        while True:
            print(f"Informe o gênero (M/F) da pessoa: {i + 1}")
            genero = input().strip()

            if not genero:
                continue

            primeira_letra = genero.upper()[0]

            if primeira_letra == 'M' or primeira_letra == 'F':
                genero_valido = primeira_letra
                break
            else:
                print("Erro: Digite apenas M ou F.")

        if altura > maior_altura:
            maior_altura = altura
        if altura < menor_altura:
            menor_altura = altura
        
        if genero_valido == 'M':
            soma_homens += altura
            qtd_homens += 1
        else:
            total_mulheres += 1

    media_homens = 0.0
    if qtd_homens > 0:
        media_homens = soma_homens / qtd_homens

    print("\n----- RESULTADOS -----")
    print(f"A maior altura do grupo é: {maior_altura}")
    print(f"A menor altura do grupo é: {menor_altura}")
    print(f"A média de altura das pessoas do gênero Masculino é: {media_homens}")
    print(f"O número de pessoas do gênero Feminino é: {total_mulheres}")

if __name__ == "__main__":
    main()