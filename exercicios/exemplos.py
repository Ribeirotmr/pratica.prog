# Faça uma função que retorne a soma dos numeros pares menores que n.


# def menores(n):
#     if n == 2:
#         return 2
#     elif n % 2 == 0:
#         return n + menores(n - 2)
#     else:
#         return menores(n - 1)


# print(menores(5))


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#


# Faça uma função que retorne a quantidade de digitos de um numero.


# def quantidade_digitos(n):
#     if n < 10:
#         return 1
#     elif n < -10:
#         return -1
#     else:
#         return n % 10 + quantidade_digitos(n // 10)


# print(quantidade_digitos(123))


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#


# Faça uma função que retorne a soma do qadrado de n ate 1.


# def soma_quadrado(n):
#     if n == 1:
#         return 1
#     else:
#         return n**2 + soma_quadrado(n - 1)


# print(soma_quadrado(3))


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#


# Faça um que calcule o MDC de dois numeros.


# def mdc(a, b):
#     if b == 0:
#         return a
#     else:
#         return mdc(b, a % b)


# print(mdc(24, 20))


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#


# Faça uma função que calcule o logaritimo dos numeros.


# def misterio(n):
#     if n == 1:
#         return 0
#     else:
#         return 1 + misterio(n // 2)


# print(misterio(4))
# print(misterio(6))
# print(misterio(8))
# print(misterio(10))
# print(misterio(16))
# print(misterio(20))


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#


# Faça uma função que retorne a soma dos divisores de um numero natural.


# def soma_divisores(n, i=1):
#     if i == n:
#         return n
#     elif n % 1 == 0:
#         return 1 + soma_divisores(n, i + 1)
#     else:
#         return soma_divisores(n, i + 1)


# print(soma_divisores(2))
# print(soma_divisores(4))
# print(soma_divisores(6))
# print(soma_divisores(7))
# print(soma_divisores(5))
# print(soma_divisores(28))


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#


# Faça uma função que calcula um numero é perfeito, cujo a soma dos seus divisores é igual a ele excluindo ele mesmo


def e_perfeito(n, i=1, soma_divisores=0):
    if i == n:
        return n == soma_divisores
    elif n % i == 0:
        return e_perfeito(n, i + 1, soma_divisores + i)
    else:
        return e_perfeito(n, i + 1, soma_divisores)


print(e_perfeito(12))


# def e_perfeito(n, divisor=1, soma=0):
#     if divisor >= n:
#         return soma == n

#     if n % divisor == 0:
#         soma += divisor

#     return e_perfeito(n, divisor + 1, soma)


# print(e_perfeito(6))
# print(e_perfeito(28))
# print(e_perfeito(12))


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
