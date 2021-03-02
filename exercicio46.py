print("Digite um numero de 100 a 999")
num = int(input())


while num < 100 or num > 999:
    print("Digite um numero de 100 a 999")
    num = int(input())


num = str(num)
reverse = num[::-1]

print(f" O numero digitado ao contrário é: {reverse}")
