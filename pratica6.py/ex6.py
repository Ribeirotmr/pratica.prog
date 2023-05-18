def leInteiro():
    try:  # Tenta fazer a conversão do valor digitado para int
        return int(input("Digite um valor inteiro: "))
    except:  # Se não for possível fazer a conversão, uma exceção é lançada
        print("ERRO: Valor inválido")
        return leInteiro()

#Exercício 6a: Complete a função abaixo
def leFloat():
    try:
        return float(input("Digite um valor float: ")) 
    except:
        print("Erro: Valor invalido")
        return leFloat()
    

#Exercício 6b: Complete a função abaixo 
def leValor(n, mensagem = "Digite um valro: "):
    n = input("Digite um valro: ")
    try:
        return mensagem
    except:
        print("Erro: Valor invalido")
        return leValor(n)

def main():
    valorInt = leInteiro()
    print(f"Valor inteiro lido: {valorInt}")

    """"
    Após a implementação da função 'leFloat', descomente o código abaixo
    e teste o seu programa. Se sua implementação estiver correta, o programa
    irá funcionar.
    """

    valorFloat = leFloat()
    print(f"Valor real lido: {valorFloat}")

    """"
    Após a implementação da função 'leValor', descomente o código abaixo
    e teste o seu programa. Se sua implementação estiver correta, o programa
    irá funcionar.
    """

    valor = leValor(int, "Digite um valor inteiro: ")
    print(f"Valor digitado: {valor}")
    valor = leValor(int, "Digite um inteiro: ")
    print(f"Valor digitado: {valor}")
    valor = leValor(int)
    print(f"Valor digitado: {valor}")
    valor = leValor(float, "Digite um float: ")
    print(f"Valor digitado: {valor}")
    valor = leValor(str, "Digite um string: ")
    print(f"Valor digitado: {valor}")


main()
