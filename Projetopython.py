def soma(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        print("Divisao por zero invalida!!")
    else:
        return a / b
    
print("___Calculadora Python___")

num1 = int(input("Informe o primeiro numero:"))
num2 = int(input("Informe o segundo numero:"))

####################################

op = input("Qual op voce deseja?")

if op == '1':
    print(soma(num1, num2))
elif op == '2':
    print(subtrair(num1, num2))
elif op == '3':
    print(multiplicacao(num1, num2))
elif op == '4':
    print(divisao(num1, num2))
elif op == '5':
    print("Saindo do programa...")
    
else:
    print("Escolha invalida, tente novamente")
