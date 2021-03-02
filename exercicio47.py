print("Digite um numero de 1000 a 9999")
num = int(input())


while num < 1000 or num > 9999:
    print("Digite um numero de 1000 a 9999")
    num = int(input())


print(f"primeiro digito é {str(num)[0]}")
print(f"segundo digito é {str(num)[1]}")
print(f"terceiro digito é {str(num)[2]}")
print(f"quarto digito é {str(num)[3]}")
