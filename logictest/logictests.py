#MATRIZ
'''
M = int(input('Digite o número de linhas:'))
N = int(input('Digite o número de colunas:'))
mat = [[0 for x in range(N)] for x in range(M)]
for i in range(0,M):
    for j in range(0,N):
        mat[i][j]=int(input(f"Elementos [{i},{j}]:"))
    print()
    print('Matriz:')

for i in range(0,M):
    for j in range(0,N):
        print(f"{mat[i][j]} ", end="")
    print()
'''
#VETOR
'''
V = int(input('Digite o número de elementos:'))
vet = [0 for x in range(V)]
for j in range(0,V):
    vet[j]=float(input('Digite os elementos:'))
    print()
    print('Vetor:')
for j in range(0,V):
    print(f"{vet[j]:.1f}")
'''
#FATORIAL
'''
numero = int(input('Digite o número:'))
if numero > 0:
    fatorial = 1
    for num in range(1,numero+1):
        fatorial = fatorial*num
        print('Valor final é:', fatorial)
else:
    print('Valor inválido')
'''
#RETANGULO


'''
import math

base = int(input('Digite o valor da base:'))
alturat(input('Digite o valor da altura:'))
area = base * altura
print('Área:', area)
perimetro = (base * 2 + altura * 2)
print('Perímetro:', perimetro)
diagonal = float(math.sqrt(base ** 2 + altura ** 2))
print('A Diagonal é: {:.1f}'.format(diagonal))
'''

#IDADES

'''
import math

print('Dados da primeira pessoa:')
dados1 = input('Digite o nome da primeira pessoa:')
dadosnumeros1 = int(input('Digite a idade da primeira pessoa:'))
print('Dados da segunda pessoa:')
dados2 = input('Digite o nome da segunda pessoa:')
dadosnumeros2 = int(input('Digite a idade da segunda pessoa:'))
média = float((dadosnumeros1 + dadosnumeros2) / 2)
print('O nome da primeira pessoa é {:s}, e o nome da segunda pessoa é {:s} e a média entre a idade de ambas é: {:.1f}'.format(dados1, dados2, média))
'''

#Menor de três (a<b, a<c) or (b<c) or c

'''

(print('Determine o menor entre os três valores:'))
primeiro_valor = int(input('Digite o primeiro valor:'))
segundo_valor = int(input('Digite o segundo valor:'))
terceiro_valor = int(input('Digite o terceiro valor:'))
if primeiro_valor < segundo_valor and primeiro_valor < terceiro_valor:
    print('O menor valor é:', primeiro_valor)
elif segundo_valor < terceiro_valor:
    print('O menor valor é:', segundo_valor)
else:
    print('O menor é:', terceiro_valor)
'''

#Crescente

'''
print('Digite dois números:')
X = int(input('Primeiro número:'))
Y = int(input('Segundo número:'))
acerto = False
while acerto == False:
    if X < Y:
        print('Crescente')
        print('Digite novamente outros dois números:')
        X = int(input('Primeiro número:'))
        Y = int(input('Segundo número:')) 
    elif X > Y:
        print('Decrescente')
        print('Digite novamente outros dois números:')
        X = int(input('Primeiro número:'))
        Y = int(input('Segundo número:')) 
    elif X == Y:
        acerto = True
        print('Valores iguais')
'''        
#Crescente forma diferente (mais simples porém desconsidera o print de valores iguais.)

'''
print('Digite dois números:')
X = int(input('Primeiro número:'))
Y = int(input('Segundo número:'))    
while X != Y:
    if X < Y:
        print('Crescente')
    else:
        print('Descrescente')
    print('Digite novamente dois números:')
    X = int(input('Primeiro número:'))
    Y = int(input('Segundo número:')) 
'''
#Soma de números impares

'''
import math

numero_a=int(input('Digite o primeiro número:'))
numero_b=int(input('Digite o segundo número:'))

if numero_a > numero_b:
    troca = numero_a
    numero_a = numero_b
    numero_b = troca

soma = 0
for x in range(numero_a+1,numero_b):
    if x % 2 == 1:
        soma = soma + x
        print(soma)
'''

#Soma de vetores

'''
N = int(input('Digite o número de elementos do vetor:'))
vet = [0 for x in range(N)]
for j in range(0,N):
    vet[j]=float(input("Digite os números:"))
print()
print('Valores:', end="")
for j in range(0,N):
    print()
    print(f"{vet[j]:.1f} ", end="")
a = 0
for j in range(0,N):
    a = a + vet[j]
print()
print('Soma dos elementos do vetor:', a)
media = a / N
print('Média dos elementos do vetor é: {:.2f} ' .format(media))
'''

#Matriz com valores negativos
'''
A = int(input('Qual a ordem da matriz?'))
if A <= 10:
    N = A
    M = A
    N = M
mat = [[0 for x in range(N)] for x in range(M)]
for i in range (0,M):
    for j in range (0,N):
        mat[i][j]=int(input(f"Elementos [{i},{j}]:"))
    print()
    
for i in range (0,M):
    print(f"{mat[i][i]} ", end="")
cont = 0
for i in range (0,M):
    for j in range (0,N):
        if mat[i][j] < 0:
            cont = cont + 1
print(f"Quantidade de negativos: {cont} ")
'''
#Matriz com valores negativos (forma de resolver padrão)

'''
N = int(input('Qual a ordem da matriz?'))
mat = [[0 for x in range(N)] for x in range(N)]
for i in range(N):
    for j in range(N):
        mat[i][j] = int(input(f"Elementos:[{i},{j}]:"))
    print()
for i in range(N):
    print(f"{mat[i][i]} ", end="")
cont = 0
for i in range(N):
    for j in range(N):
        if mat[i][j] < 0:
            cont = cont + 1
            print('Contagem de negativos é:', cont)
'''
#Altura
'''
n = int(input("Quantas pessoas serao digitadas? "))

nomes = [0 for x in range(n)]
idades = [0 for x in range(n)]
alturas = [0 for x in range(n)]

for i in range(n):
	print(f"Dados da {i+1}a pessoa:")
	nomes[i] = str(input("Nome: "))
	idades[i] = int(input("Idade: "))
	alturas[i] = float(input("Altura: "))

nmenores = 0
alturatotal = 0
for i in range(n):
	if idades[i] < 16:
		nmenores = nmenores + 1
for i in range(n):
	alturatotal = alturatotal + alturas[i]

alturamedia = alturatotal / n
percentualMenores = (float(nmenores) / n) * 100.0

print(f"\nAltura media = {alturamedia:.2f}")
print(f"Pessoas com menos de 16 anos: {percentualMenores:.1f}%")

for i in range(n):
	if idades[i] < 16:
		print(nomes[i])

'''
#Vetores pares (meu)

'''
A = int(input('Quantos números você vai digitar?'))
vet = [0 for x in range(A)]
for v in range (0,A):
    vet[v] = float(input('Digite um número:'))
print('Vetores pares:')
y = 0 
for v in range (0,A):
    if vet[v] % 2 == 0:
        y = y + 1
        print(f"{vet[v]} " , end="")
print()
print(f"Pares: {y} ")

'''
#Vetores pares (sistema)

'''

n = int(input("Quantos numeros voce vai digitar? "))

vetor = [0 for x in range(n)]

for i in range(n):
	vetor[i] = int(input("Digite um numero: "))

print("\nNUMEROS PARES:")

qtdpares = 0
for i in range(n):
	if vetor[i] % 2 == 0:
		print(f"{vetor[i]}  ", end="")
		qtdpares = qtdpares + 1

print(f"\n\nQUANTIDADE DE PARES = {qtdpares}")


'''

#Maior posição

'''

n = int(input('Quantos dígitos:'))
vet = [0 for x in range(n)]
for i in range (0,n):
    vet[i] = float(input('Digite os número:'))
maior = vet[0]
posmaior = 0
for i in range(0,n):
    if vet[i] > maior:
        maior = vet[i]
        posmaior = i
print(f"Maior valor = {maior:.1f}  ")
print(f"Posição = {posmaior} ")

'''
#Soma de vetores

'''
n = int(input('Quantos valores terão cada vetor?'))
a = [0 for x in range(n)]
b = [0 for x in range(n)]
c = [0 for x in range(n)]
for i in range (0,n):
    a[i] = float(input('Digite os valores do vetor A:'))
for i in range (0,n):
    b[i] = float(input('Digite os valores do vetor B:'))

for i in range(0,n):
    c[i] = a[i] + b[i]
    print(f"Valor de C = {c[i]}" , end="")
'''
#Abaixo da média

'''
n = int(input('Digite o número de elementos do vetor:'))
vet = [0 for x in range(n)]
for i in range (0,n):
    vet[i] = float(input('Digite os números:'))

print('Média dos vetores:')
c = 0
for i in range(0,n):
    c = c + vet[i]
media = c / n
print(f"\nMédia dos vetores: {media:.3f} ")
print()
print('Elementos abaixo da média:')
for i in range(0,n):
    if vet[i] < media:
        print(f"\n {vet[i]:.1f}", end="")
'''

#Média pares (interessante)

'''
n = int(input("Quantos elementos vai ter o vetor? "))

vetor: [int] = [0 for x in range(n)]

for i in range(n):
	vetor[i] = int(input("Digite um numero: "))

npares = 0
somapares = 0
for i in range(n):
	if vetor[i] % 2 == 0:
		somapares = somapares + vetor[i]
		npares = npares + 1

if npares == 0:
	print("NENHUM NUMERO PAR")
else:
	mediapares = float(somapares) / npares

	print(f"MEDIA DOS PARES = {mediapares:.1f}")
'''
# Mais velho
'''
n = int(input('Quantas pessoas você vai digitar:'))
nome = [0 for x in range(n)]
idade = [0 for x in range(n)]
for i in range(0,n):
    print(f"Dados da {i+1}a pessoa:")
    nome[i] = input('Nome:')
    idade[i] = int(input('Idade:'))
x = idade[0]
for i in range(n):
    if idade[i] > x:
        x = idade[i]
print(f"\n Pessoa mais velha: ", x)

'''

# Aprovados

'''
n = int(input('Quantos alunos serão digitados:'))
nome = [0 for x in range(n)]
nota_1 = [0 for x in range(n)]
nota_2 = [0 for x in range(n)]
for i in range(0,n):
    print(f"\n Digite nome, primeira e segunda nota do {i+1} aluno:")
    nome[i] = input()
    nota_1[i] = float(input())
    nota_2[i] = float(input())
print('Alunos aprovados:')
c = 0
y = 0
for i in range(0,n):
    c = (nota_1[i] + nota_2[i]) / 2
    if c >= 6:
        c = nome[i]
        print(f"\n  {c} ", end="")    
'''

# Dados pessoas

'''
n = int(input('Quantas pessoas serão digitadas:'))
altura = [0 for x in range(n)]
sexo = [0 for x in range(n)]
for i in range(0,n):
    altura[i] = float(input(f"Altura da {i+1}a pessoa: "))
    sexo[i] = input(f"Sexo da {i+1}a pessoa: ")
w = altura[0]
for i in range(0,n):
    if altura[i]>w:
        w = altura[i]
print(f"\n Altura máxima: ", w)
for i in range(0,n):
    if altura[i]<w:
        w = altura[i]
print(f"\n Altura mínima: ", w)
altfem = 0
a = 0
nm = 0
for i in range(0,n):
    if sexo[i] != 'F':
        a = a + 1
    else:
        nm = nm + 1
        altfem = altfem + altura[i]
altmed = altfem / nm
print(f"Número de homens: {a}")
print(f"Média dos valores femininos: {altmed:.2f} ")   
'''

# Comerciante

'''
n = int(input('Serão digitados dados de quantos produtos?'))
nome = [0 for x in range(n)]
compra = [0 for x in range(n)]
venda = [0 for x in range(n)]
for i in range(0,n):
    print(f"\n Produto {i+1}")
    nome[i] = input(f"Nome: ")
    compra[i] = float(input(f"Preço de compra: "))
    venda[i] = float(input(f"Preço de venda: "))
a = 0
b = 0
c = 0
for i in range(0,n):
    if venda[i] < compra[i] * 1.1:
        a = a + 1
    elif venda[i] >= compra[i] * 1.1 and venda[i] <= compra[i] * 1.2:
        b = b + 1
    elif venda[i] > compra[i] * 1.2:
        c = c + 1
print(f"Lucros abaixo de 10% ", a)
print(f"Lucros entre 10 e 20 %: ", b)
print(f"Lucro acima de 20%: ", c)
d = 0
e = 0
for i in range(0,n):
    d = compra[i] + d
    e = venda[i] + e
lucrototal = e - d
print(f"Valor total de compra: {d:.2f} ")
print(f"Valor total de venda: {e:.2f} ")
print(f"Lucro total: {lucrototal:.2f} ")
'''
# Soma linhas
'''
m = int(input("Qual a quantidade de linhas da matriz? "))
n = int(input("Qual a quantidade de colunas da matriz? "))

matriz = [[0 for x in range(n)] for x in range(m)]
vetor = [0 for x in range(m)]

for i in range(m):
	print(f"Digite os elementos da {i + 1} a. linha")
	for j in range(n):
		matriz[i][j] = float(input())

for i in range(m):
	somalinha = 0

	for j in range(n):
		somalinha = somalinha + matriz[i][j]
	vetor[i] = somalinha

print("VETOR GERADO:")

for i in range(m):
	print(f"{vetor[i]:.1f}")
'''
# Negativos matriz

'''

M = int(input('Qual a quantidade de linhas da matriz?'))
N = int(input('Qual a quantidade de colunas da matriz?'))
while M > 10 or N > 10:
    print(f"\n Não é possível aceitar números maiores que 10.")
    M = int(input('Qual a quantidade de linhas da matriz?'))
    N = int(input('Qual a quantidade de colunas da matriz?'))
matriz = [[0 for x in range(N)] for x in range(M)]
for i in range(0,M):
    for j in range(0,N):
        matriz[i][j] = int(input(f" Elemento [{i}][{j}]: "))
print('VALORES NEGATIVOS:')
for i in range(0,M):
    for j in range(0,N):
        if matriz[i][j] < 0:
            print(f" {matriz[i][j]} ")

'''
# Cada linha

n = int(input('Qual a ordem da matriz?'))
while n > 10:
    print(f"\n Não é possível aceitar números maiores que 10.")
    n = int(input('Qual a ordem da matriz?'))
matriz = [[0 for x ]]





















