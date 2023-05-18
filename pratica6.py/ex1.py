def fatorial(n):
    if type(n) == int and n >=0:
        return 1 if n == 0 or n == 1 else n*fatorial(n-1)
    else: 
        print("Numero invalido!!!!")
    
def main():
    n = 5
    print(f"{n}! = {fatorial(n)}")
    
    n = 2
    print(f"{n}! = {fatorial(n)}")
    
main()



#o problema esta no tipo de variavel e sua crecorrencia. Para a função funcionar o numero precisa ser inteiro e maior ou igual a 0.
#Implementei uma condição que verifica se o valor é inteiro ou não, caso ela não seja o programa imprime uma mensagem que o valor e invalido