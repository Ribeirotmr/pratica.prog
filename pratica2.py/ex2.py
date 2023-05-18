x = input("Digite um numero")

if x%2 == 0:
    print (f"{x} é par")
if x%2 == 1:
    print (f"{x} é impar ")
if x%2 == 0 or x%3 == 0:
    print ("...")
if x%2 == 0 and x%5 == 0:
    print ("...")