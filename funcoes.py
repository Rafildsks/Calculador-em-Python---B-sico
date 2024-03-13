def somar(n1, n2):
    return n1 + n2

def subtrair(n1, n2):
    return n1 - n2

def multiplicar(n1, n2):
    return n1 * n2

def dividir(n1, n2):
    if n2 == 0:
        print("Não é possivel dividir um numero por 0")
    else:
        resultado = n1/n2
        #print(f'{n1} / {n2} = {resultado}')
        return resultado
    
def calcular(n1, n2, operador):
    match operador:
        case '+': return somar(n1, n2)
        case '-': return subtrair(n1, n2)
        case '*': return multiplicar(n1, n2)
        case '/': return dividir(n1, n2)
        case other: return 'Operador não encontrado'

print(calcular(5, 10, '+'))
print(calcular(5, 10, '-'))
print(calcular(5, 10, '*'))
print(calcular(5, 0, '/'))
print(calcular(5, 10, 'o'))




'''

divisao = dividir(80, 5)
print('O resultado da divisão é', divisao)

print('Resultado', dividir(20, 0))

resultado = dividir(30, 5)  
soma = 20  + resultado 
print("A soma é", soma)

dividir(1250, 2)

'''

'''
n1 = 10
n2 = '0'

dividir()

try:
    resultado = n1 / n2

except ZeroDivisionError:
    print("Não é possivel divir um numero por zero")

except Exception:
    print("Ocorreu um erro!")
'''