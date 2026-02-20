# Estatísticas de Altura e Gênero

Este projeto é uma aplicação em **Python** desenvolvida para coletar dados de altura e gênero de um grupo de pessoas e gerar estatísticas descritivas sobre o grupo.

## 📋 Funcionalidades

O script realiza as seguintes operações:

1.  **Coleta de Dados:** Solicita a altura e o gênero de 15 pessoas.
2.  **Validação de Entrada:** Garante que o gênero informado seja apenas 'M' (Masculino) ou 'F' (Feminino).
3.  **Cálculos Estatísticos:**
    *   Identifica a **maior altura** do grupo.
    *   Identifica a **menor altura** do grupo.
    *   Calcula a **média de altura** das pessoas do gênero Masculino.
    *   Conta o **número total de pessoas** do gênero Feminino.
4.  **Relatório:** Exibe todos os resultados formatados no console ao final da coleta.

## 🛠️ Pré-requisitos

Para executar este script, você precisa ter o **Python 3** instalado em sua máquina.

*   Verifique a instalação executando no terminal:
    ```bash
    python --version
    ```
    ou
    ```bash
    python3 --version
    ```

## 🚀 Como Executar

1.  **Salve o arquivo:**
    Certifique-se de que o código Python está salvo em um arquivo chamado `main.py`.

2.  **Abra o terminal:**
    Navegue até a pasta onde o arquivo está salvo.

3.  **Execute o script:**
    ```bash
    python main.py
    ```
    *Ou, dependendo da sua configuração:*
    ```bash
    python3 main.py
    ```

4.  **Siga as instruções:**
    Digite a altura e o gênero conforme solicitado pelo prompt para cada uma das 15 pessoas.

## 💻 Exemplo de Uso

```text
Informe a altura da pessoa número: 1
1.75
Informe o gênero (M/F) da pessoa: 1
M
Informe a altura da pessoa número: 2
1.60
Informe o gênero (M/F) da pessoa: 2
F
... (repete até 15 pessoas)

----- RESULTADOS -----
A maior altura do grupo é: 1.85
A menor altura do grupo é: 1.55
A média de altura das pessoas do gênero Masculino é: 1.78
O número de pessoas do gênero Feminino é: 7
```

## 📝 Estrutura do Código

*   **Variáveis de Controle:** Utiliza `float('-inf')` e `float('inf')` para inicializar as variáveis de maior e menor altura, garantindo que qualquer valor informado substitua o inicial.
*   **Loop Principal:** Um loop `for` executa exatamente 15 vezes para coletar os dados.
*   **Validação de Gênero:** Um loop `while True` garante que o usuário não prossiga sem digitar 'M' ou 'F'.
*   **Entrada de Dados:** Utiliza `input()` para leitura de teclado e `float()` para conversão numérica.
*   **Boas Práticas:** O código está encapsulado na função `main()` e protegido pelo bloco `if __name__ == "__main__":`, seguindo os padrões da comunidade Python.

## 🔧 Melhorias Sugeridas

Para expandir as funcionalidades deste projeto, considere:

*   Tornar a quantidade de pessoas (atualmente fixa em 15) dinâmica ou configurável via argumento.
*   Adicionar tratamento de exceções mais robusto para a entrada da altura (caso o usuário digite letras).
*   Permitir que o usuário encerre a coleta antecipadamente (ex: digitando '0' na altura).
*   Salvar os resultados em um arquivo de texto ou CSV para histórico.

## 📄 Licença

Este projeto é open source e está disponível para uso e modificação.