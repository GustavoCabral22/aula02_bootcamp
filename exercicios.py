import math

# #### Inteiros (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.

# numero1 = int(input("Digite um número: "))
# numero2 = int(input("Digite outro número: "))
# resultado = numero1 + numero2
# print(resultado)

# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.

# numeroParaDividir = 5
# numeroUsuario = int(input("Digite um número: "))
# resultado = numeroUsuario % numeroParaDividir
# print(resultado)

# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.

# numero1 = int(input("Digite um número: "))
# numero2 = int(input("Digite outro número: "))
# resultado = numero1 + numero2
# print(resultado)

# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.

# numero_01 = int(input("Inserir um numero inteiro: "))
# numero_02 = int(input("Inserir outro numero inteiro: "))
# resultado = numero_01 // numero_02
# print(resultado)

# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
# numero1 = int(input("Digite um número: "))
# numeroQuadrado = numero1 * numero1
# print(numeroQuadrado)

# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.

# numero_01 = float(input("Inserir um numero decimal: "))
# numero_02 = float(input("Inserir outro numero decimal: "))
# resultado = numero_01 + numero_02
# print(resultado)

# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.

# numero_01 = float(input("Inserir um numero decimal: "))
# numero_02 = float(input("Inserir outro numero decimal: "))
# media = (numero_01 + numero_02) / 2
# print(media) 

# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).

# base = int(input("Insira a base: "))
# expoente = int(input("Insira o expoente: "))
# potencia = base ** expoente
# print(potencia)

# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.

# temperatura_celcius = float(input("Digite a temperatura em Celcius: "))
# conversao = (temperatura_celcius * 1.8) + 32
# print(conversao)

# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.

# raio_do_circulo = float(input("Digite o raio: "))
# area_do_circulo = math.pi * raio_do_circulo ** 2
# print(round(area_do_circulo,2))

#raio_do_circulo = float(input("Digite o raio: "))
#area_do_circulo = math.pi * raio_do_circulo ** 2
#area_do_circulo_formatada = "{:.2f}".format(area_do_circulo)
#print(f"{area_do_circulo:.2f}")

# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.

# texto = input("Digite um texto: ").upper()
# print(texto)

# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.

# texto = input("Digite um texto: ").lower()
# print(texto)

# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.

# texto = input("Digite um texto: ")
# print(texto.strip())

# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.

# data = input("Digite uma data no formato dd/mm/yyyy: ")
# dia = data.split('/')
# print(dia[0])

# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.

# texto1 = input("Digite o primeiro texto: ")
# texto2 = input("Digite o segundo texto: ")
# print(texto1 + " " +  texto2)

# data_do_usuario = input("Insira uma data no formato dd/mm/aaaa: ")
# lista_de_dia_mes_ano = data_do_usuario.split("/")
# print(f"O elemento 1 e o: {lista_de_dia_mes_ano[0]}")
# print(f"O elemento 2 e o: {lista_de_dia_mes_ano[1]}")
# print(f"O elemento 3 e o: {lista_de_dia_mes_ano[2]}")

# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.

# expressao1 = bool(input("Digite o seu primeiro input: "))
# expressao2 = bool(input("Digite o seu segundo input: "))
# comparacao = expressao1 and expressao1
# print(comparacao)

# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.

# expressao1 = bool(input("Digite o seu primeiro input: "))
# expressao2 = bool(input("Digite o seu segundo input: "))
# comparacao = expressao1 or expressao1
# print(comparacao)

# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.

# expressao1 = input("Digite o seu primeiro input: ").lower()
# def inversao(expressao):
#     if(expressao == "false"):
#         return "True"
#     else: 
#         return "False"

# print(inversao(expressao1))

# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.

# numero1 = int(input("Digite um número: "))
# numero2 = int(input("Digite outro número: "))

# if(numero1 == numero2):
#     print("São iguais.")
# else:
#     print("São diferentes.")

# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.

numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite outro número: "))

if(numero1 != numero2):
    print("São diferentes.")
else:
    print("São iguais")

# #### try-except e if

# 21: Conversor de Temperatura


# 22: Verificador de Palíndromo
# 23: Calculadora Simples
# 24: Classificador de Números
# 25: Conversão de Tipo com Validação