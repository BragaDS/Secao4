print("Digite abaixo o salário base do funcionário")
sbase = float(input())
s1 = (sbase * 0.05)
s2 = (sbase * 0.93)
sfinal = s1 + s2

print(f"Salário final é de: {sfinal:.2f}")
