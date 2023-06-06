print("########## QUESTÃO 1 ##########")


def soma_pares(n):
    if n == 2:
        return 2
    elif n % 2 == 0:
        return n + soma_pares(n - 2)
    else:
        return soma_pares(n - 1)


print(soma_pares(6))

print("########## QUESTÃO 2 ##########")


def quantidade_digitos(n):
    if n < 10:
        return 1
    else:
        return n % 10 + quantidade_digitos(n // 10)


print(quantidade_digitos(123))


print("########## QUESTÃO 3 ##########")


def soma_quadrados(n):
    if n == 1:
        return 1
    return n**2 + soma_quadrados(n - 1)


print(soma_quadrados(3))


print("########## QUESTÃO 4 ##########")


def mdc(a, b):
    if b == 0:
        return a
    return mdc(b, a % b)


print(mdc(24, 20))


print("########## QUESTÃO 5 ##########")


def divisores(n, i=1):
    if i == n:
        return n
    if n % i == 0:
        return i + divisores(n, i + 1)
    else:
        return divisores(n, i + 1)


print(divisores(4))


print("########## QUESTÃO 6 ##########")


def div(a, b, i=0):
    if a == 0:
        return i
    else:
        return div(a - b, b, i + 1)


print(div(220, 2))


print("########## QUESTÃO 7 ##########")


def div2(a, b, i=0):
    if a - b < 0:
        return a
    else:
        return div2(a - b, b, i + 1)


print(div2(55, 6))


print("########## QUESTÃO 8 ##########")


def e_perfeito(n, i=1, s=0):
    if n == i:
        return s == n
    if n % i == 0:
        return e_perfeito(n, i + 1, s + i)
    return e_perfeito(n, i + 1, s)


def som_num_pefeito(n, m):
    if type(n) != int and type(m) != int:
        return None
    if n > m:
        return 0
    else:
        quantidade = e_perfeito(n) + som_num_pefeito(n + 1, m)
    return quantidade


def main():
    n = int(input())
    x = int(input())
    y = int(input())
    print(e_perfeito(n))
    print(som_num_pefeito(x, y))


main()
