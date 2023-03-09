def main():  
    numero =  int(input("Informe um numero: "))

    if (pertenceSerieFibonacci(numero)):
        print(numero, " pertence a sequencia de Fibonacci")
    else:
        print(numero, " nao pertence a sequencia de Fibonacci")
 
def pertenceSerieFibonacci(numero):
    a = 0
    b = 1
    while a <= numero:
        if numero == a:
            return True
        a, b = b, a + b
    return False

main()