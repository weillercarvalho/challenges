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
altura = int(input('Digite o valor da altura:'))
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



























