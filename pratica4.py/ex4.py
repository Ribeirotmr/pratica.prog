import math as m

def combinacao(n, p):
    if n < 0 or p < 0:
        print("ERRO:")
    if n < p:
        print("ERRO:")
    else:
        print(m.factorial(n) // (m.factorial(n - p)) * m.factorial(p))
    
def main():
    x = int(input())
    y = int(input())
    combinacao(x, y)
    
main()   