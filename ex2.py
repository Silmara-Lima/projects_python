#Exibir a multiplicação de dois números inteiros informados pelo usuário
x = int(input('Digite o 1º número -> '))
y = int(input('Digite o 2º número -> '))
z = x * y

print('O 1º número multiplicado pelo 2º número é igual a ', z)

#Ler um número inteiro e informar o seu dobro
a = x * 2

print('O dobro do 1º número digitado é ', a)

#Ler 3 números reais e exibir a soma do 1º número com o 2º, multiplicada pela soma do 2º pelo 3º.
number_1 = int(input('Digite um número -> '))
number_2 = int(input('Digite um segundo número -> '))
number_3 = int(input('Digite um terceiro número -> '))

print((number_1 + number_2) * (number_2 + number_3))

#Ler um número e exibir sua raiz quadrada
number_4 = int(input('Digite um número para saber a sua raiz quadrada -> '))

print(number_4 * number_4)

#Entrar com um número de 3 casas e imprimir o algarismo das dezenas
while True:
    number_5 = int(input('Digite um número de 3 dígitos: '))

    if numero.isdigit() and len(number_5) == 3:
        print(f'Você digitou o número: {number_5}')
        break
    else:
        print("Erro: O número digitado precisa ter 3 dígitos.")

#Ler e Imprimir seu nome E Imprimir o nome informado pelo usuário
name = str(input('Qual o seu nome?'))

print('Meu nome é ', name)

#Ler dois números reais e informar a média dos dois
number_6 = int(input('Digite um número -> '))
number_7 = int(input('Digite um segundo número -> '))

print('A media desses dois números é ', ((number_6 + number_7)/2))

#Ler dois números e informar o dividendo, o divisor, o quociente e o resto
dividendo = int(input('Digite um número -> '))
divisor = int(input('Digite um segundo número -> '))

#verificar se o divisor é 0 pra evitar erro
if divisor == 0:
    print('Erro: Não como realizar essa divisão.')
else: 
quociente = dividendo // divisor # o // faz divisão de números inteiros
resto = dividendo % divisor #o % vê o resto

print('O dividendo é {}, o dividor é {}, o quociente é {} e o resto é {}'.format(dividendo, divisor, quociente, resto))

#Entrar com um número e mostrar o número, o quadrado do número e a raiz quadrada deste número
number_8 = int(input('Digite um número -> '))

print(f"O número digitado foi: {number_8}")
print(f"O quadrado do número digitado é: {number_8 ** 2}")
print(f"A raiz quadrada do número digitado é: {number_8 ** 0,5}")
## se importar a lib math poderia fazer usar o math.sqtr(number_8)

#Entrar com a base e a altura de um triângulo e exibir a área
base = int(input('Digite o valor da base do triângulo -> '))
altura = int(input('Digite o valor da altura do triângulo -> '))

print('A área do triângulo equivale a ', {base * altura})

#Entrar com a base a altura de um retângulo e exibir o perímetro, a área e a diagonal (perímetro = 2*(base + altura);
#área = base * altura;
#diagonal = sqrt(base ^2 + altura ^ 2) – pitágoras

perimetro = 2 * (base + altura)
diagonal = (base ** 2 + altura ** 2) ** 0.5 #ou pela lib math ficaria 'math.sqrt(a**2 + b**2)'

print(f"O perímetro do triângulo é: {perimetro}")
print(f"A área do triângulo é: {base * altura}")
print(f"A diagonal do triângulo é: {diagonal}")