print("Digite o valor da hora de trabalho em reais, incluindo os centavos")
ht = float(input())
print("Digite o numero de horas trabalhadas no mês")
hm = int(input())

sal = (ht * hm) * 1.10

print(f"O valor é de {sal:.2f}")
