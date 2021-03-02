print("Digite o comprimento do terreno em metros")
comp = float(input())
print("Digite a largura do terreno em metros")
larg = float(input())
print("Digite o valor do preço do metro da tela para cercar o terreno")
prec = float(input())

tTela = comp * larg

tPrec = tTela * prec

print(f"O valor a ser gasto é de R$: {tPrec}")
