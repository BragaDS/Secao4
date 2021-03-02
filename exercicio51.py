x1 = int(input(f'Informe x1 => '))
y1 = int(input(f'Informe y1 => '))

# elevar à uma fracão corresponde a tirar a raiz tendo como com indice
#  número indicado no denominador
distancia = int((((0 - x1) ** 2) + ((0 - y1) ** 2)) ** (1 / 2))

print(f'A distância entre a origem (0,0) e o ponto de'
      f' coordenadas ({x1},{y1})é: {distancia}')
#
# Demonstrando o cálculo

print(f'x2 - x1 = {0 - x1}, \n'
      f'y2 - y1 = {0 - y1}')
print(f'(x2 - x1) ** 2 = {(0 - x1) ** 2}, \n'
      f'(y2 - y1) ** 2 = {(0 - y1) ** 2}')

print(f'Distância da origem = {distancia}')
