# Capítulo 2: Introdução ao Python - Variáveis, If/Else, Decisões Aninhadas e Laços de Repetição

# 1. Variáveis
# Criação de variáveis de diferentes tipos

nome = "Vitor"
idade = 25
saldo_bancario = 1500.50
estudante = True

print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Saldo bancário: R$ {saldo_bancario}")
print(f"É estudante? {estudante}")

# 2. Tomada de Decisão

# 2.1. Tomada de decisão aninhada (if/else dentro de if/else)
# Exemplo de checar múltiplas condições de forma encadeada

if idade >= 18:
    if saldo_bancario >= 1000:
        print(f"{nome} é maior de idade e tem um saldo bancário saudável.")
    else:
        print(f"{nome} é maior de idade, mas o saldo bancário está baixo.")
else:
    if saldo_bancario >= 1000:
        print(f"{nome} é menor de idade, mas tem um bom saldo bancário.")
    else:
        print(f"{nome} é menor de idade e tem um saldo bancário baixo.")

# 2.2. Tomada de decisão independente (else if, ou elif no Python)
# Aqui cada condição é verificada separadamente, sem dependência das outras

if saldo_bancario >= 5000:
    print(f"{nome} tem saldo excelente.")
elif saldo_bancario >= 1000:
    print(f"{nome} tem saldo bom.")
elif saldo_bancario >= 500:
    print(f"{nome} tem saldo mediano.")
else:
    print(f"{nome} tem saldo insuficiente.")

# 3. Laços de Repetição

# Exemplo simples de contagem regressiva com While
contador = 10
while contador > 0:
    if contador == 5:
        print("Chegamos à metade da contagem!")
    print(f"Contagem: {contador}")
    contador -= 1  # Decrementa o contador

print("Fim da contagem regressiva!")

# 4. Desafio While - Verificação de senha com número limitado de tentativas
# O usuário tem 3 tentativas para inserir a senha correta

senha_correta = "1234"
tentativas = 0
max_tentativas = 3

while tentativas < max_tentativas:
    senha = input("Digite sua senha: ")
    tentativas += 1

    if senha == senha_correta:
        print("Senha correta! Acesso concedido.")
        break
    else:
        print(f"Senha incorreta. Tentativas restantes: {max_tentativas - tentativas}")

    if tentativas == max_tentativas:
        print("Número máximo de tentativas atingido. Acesso bloqueado.")

# 5. Desafio While - Cálculo de fatorial
# Um exercício de cálculo de fatorial utilizando o laço while

numero = int(input("Digite um número para calcular o fatorial: "))
fatorial = 1
contador = numero

while contador > 0:
    fatorial *= contador
    contador -= 1

print(f"O fatorial de {numero} é {fatorial}.")
