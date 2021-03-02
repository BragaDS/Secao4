print("Digite a hora os minutos e os segundos abaixo")
print("hora(s)")
hor = int(input())
print("minuto(s)")
mi = int(input())
print("segundos(s)")
seg = int(input())
print("Informe a duração em segundos: ")
dur = int(input())

hor = hor * 3600
mi = mi * 600
tSec = hor + mi + seg + dur

hFinal = int(tSec / 3600)
rest = tSec % 3600
miFinal = int(rest / 60)
rest = rest % 60

print(f"A experiência irá terminar as: {hFinal}:{miFinal}:{rest}")
