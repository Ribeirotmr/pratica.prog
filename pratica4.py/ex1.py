import math as m 

x = float(input())

if x <= 1:
    res = m.log(abs(x))
    print(res) 
elif x < 1 and x >= 2:
    res = (m.log10(x) + m.sqrt(x))
    print(res)
elif x > 2 and x <=5:
    res = (x **2 + m.log(x))
    print(res)
else:
    res = ((x **x/2) + m.log2(x))
    print(res)