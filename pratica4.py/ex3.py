def converter(segundos):
        h = segundos // 3600
        m = (segundos % 3600) // 60 
        s = (segundos % 3600) % 60
        print(f"horas: {h} minutos: {m} segundos: {s}")
     
def main():
    s = int(input())
    converter(s)
    print(f"horas: {h} minutos: {m} segundos: {s}")

    
main()