import math

print("Considerando 'a' e 'b' os catetos de um triangulo")
print("Digite o cateto 'A'")
a = float(input())
print("Digite o cateto 'B'")
b = float(input())
hip = math.sqrt(a ** 2 + b ** 2)

print(f"a hipotenusa é: {hip}")
