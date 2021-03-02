import math

print("Digite a altura desejada do degrau")
degrau = int(input())
print("Digite a altura desejada da escada")
alt = int(input())

altd = math.ceil(alt / degrau)

print(f"A altura desejada é de: {altd}")
