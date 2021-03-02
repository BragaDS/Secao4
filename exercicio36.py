import math

print("Digite a altura do cilindro")
alt = float(input())
print("Digite o raio do cilindro")
rai = float(input())
vol = math.pi * rai ** 2 * alt

print(f"O volume é: {vol}")
