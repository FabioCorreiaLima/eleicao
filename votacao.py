import os

# Lista de candidatos com seus nomes e votos iniciais
lista_candidatos = [[0, 'Mateus'], [0, 'Hygor'], [0, 'Marcos'], [0, 'Jeanderson'], [0, 'Lucas']]
total = []
opc = 1

while opc != 0:
    print('''1- Mateus
2- Hygor
3- Marcos
4- Jeanderson
5- Lucas''')

    opc = int(input(':Vote aqui. '))
    while opc > 5 or opc < 0:
        opc = int(input('Digite 1 a 5 para votar ou 0 para finalizar: '))
    if opc != 0:
        total.append(opc)
        lista_candidatos[opc - 1][0] += 1
    os.system('cls')

print(f'{"Candidatos":<15} {"Votos":<8} {"%":<8}')
print(f'{"-" * 30}')
segundo_turno = []

# Ordenar a lista de candidatos com base nos votos em ordem decrescente
lista_candidatos.sort(key=lambda x: x[0], reverse=True)

for c in lista_candidatos:
    pecr = f'{(c[0] / len(total) * 100):.2f}'
    print(f'{c[1]:<15} {c[0]:<8} {pecr:<8}')

print(f'{"-" * 30}')
print(f'{"Total":<15} {len(total):<8}')

# Verificar se é necessário um segundo turno
if (lista_candidatos[0][0] / len(total)) < 0.5:
    v = lista_candidatos[:2]
    print(f'Haverá um segundo turno entre {v[0][1]} e {v[1][1]}')

    # Inicializar a lista para o segundo turno
    segundo_turno = [[0, v[0][1]], [0, v[1][1]]]

    while True:
        print(f'\nVotação do Segundo Turno:')
        print(f'1- {v[0][1]}')
        print(f'2- {v[1][1]}')

        opc = int(input(':Vote aqui (1 ou 2): '))
        while opc != 1 and opc != 2:
            opc = int(input('Digite 1 ou 2 para votar: '))

        # Atualizar a contagem de votos do segundo turno
        segundo_turno[opc - 1][0] += 1
        os.system('cls')

        # Verificar o fim do segundo turno
        if sum(voto[0] for voto in segundo_turno) == len(total):
            break

    print('A votação do segundo turno terminou.')

# Determinar o vencedor do segundo turno, se aplicável
if segundo_turno[0][0] > segundo_turno[1][0]:
    print(f'O vencedor do segundo turno é {segundo_turno[0][1]} com {segundo_turno[0][0]} votos.')
elif segundo_turno[1][0] > segundo_turno[0][0]:
    print(f'O vencedor do segundo turno é {segundo_turno[1][1]} com {segundo_turno[1][0]} votos.')
else:
    print('O segundo turno terminou em empate.')

