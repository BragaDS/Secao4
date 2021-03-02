print("Digite o valor da mercadoria")
merc = float(input())
merc10 = merc * 0.90
merc3x = merc / 3
comiv = merc10 * 0.05
comip = merc * 0.05

print(f"Com 10% de desconto o valor da mercadoria será de: {merc10:.2f}")
print(f"O valor de cada parcela em 3x sem juros é de: {merc3x:.2f}")
print(f"O valor da comissão do vendedor sobre a venda a vista no valor de 5% é de: {comiv:.2f}")
print(f"O valor da comissão do vendedor sobre a venda parcelada no valor de 5% é de: {comip:.2f}")
