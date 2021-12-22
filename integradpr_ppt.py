from os import write
import random
import csv
import os


def input_datos(name, lista_jugadores):
    if name in lista_jugadores:
        opcion = str(input(f'''Bienvenido {name} escribre la
            opción piedra, papel, tijera o fin para salir:''')).lower()

    else:
        name = str(input('Escriba su nombre para jugar:')).upper()
        opcion = str(input(f'''Bienvenido {name} escribre la
                opción piedra, papel, tijera o fin para salir:''')).lower()
        lista_jugadores.append(name)

    return name, opcion

def eleccion_pc(lista):
    opcion_pc = random.choice(lista)
    return opcion_pc

def test_jugada(opcion_pc, opcion_jugador):
    if opcion_pc == opcion_jugador:
        return 'Empate'
    
    elif opcion_jugador == 'papel' and opcion_pc == 'piedra':
        return 'Gana'
    
    elif opcion_jugador == 'piedra' and opcion_pc == 'tijera':
        return 'Gana'
    
    elif opcion_jugador == 'tijera' and opcion_pc == 'papel':
        return 'Gana'
    
    else:
        return 'Pierde'

def registro(name, contador_gana, contador_pierde, contador_empata, contador_jugadas):
    file_name = 'resultados_ppt.csv'
    if os.path.exists(file_name):
        csvfile = open('resultados_ppt.csv', 'a')
        header = ['name', 'gana', 'pierde', 'empate', 'total_jugadas']
        writer = csv.DictWriter(csvfile, fieldnames=header) #Escribir los registros por header
        
        fila = {}
        fila['name'] = name
        fila['gana'] = contador_gana
        fila['pierde'] = contador_pierde
        fila['empate'] = contador_empata
        fila['total_jugadas'] = contador_jugadas
        
        writer.writerow(fila)
        csvfile.close()
    
    else: 
    
        with open('resultados_ppt.csv', 'w', newline='') as csvfile:
            header = ['name', 'gana', 'pierde', 'empate', 'total_jugadas']
            writer = csv.DictWriter(csvfile, fieldnames=header)
            writer.writeheader()

            fila = {}
            fila['name'] = name
            fila['gana'] = contador_gana
            fila['pierde'] = contador_pierde
            fila['empate'] = contador_empata
            fila['total_jugadas'] = contador_jugadas

            writer.writerow(fila)


if __name__=='__main__':
    print('Bienvenido a nuestro juego piedra, papel o tijera')

    lista_jugadores = []
    name = None
    posibilidades = ['piedra', 'papel', 'tijera']
    contador_gana = 0
    contador_pierde = 0
    contador_empata = 0
    contador_jugadas = 0

    while True:
        name, opcion_jugador = input_datos(name, lista_jugadores)
        print(f'Hola {name} la opcion elegida es: {opcion_jugador}')

        if opcion_jugador == 'fin':
            registro(name, contador_gana, contador_pierde, contador_empata, contador_jugadas)
            break

        elif opcion_jugador in posibilidades:
            opcion_pc = eleccion_pc(posibilidades)
            print(f'Opcion elegida por la pc: {opcion_pc}')

            resultado = test_jugada(opcion_pc, opcion_jugador)
            
            if resultado == 'Gana':
                print(f'El jugador {name} gana')
                contador_gana += 1
            
            elif resultado == 'Empate':
                print(f'El jugador {name} empata con la pc')
                contador_empata += 1

            else:
                print(f'El jugador {name} pierde')
                contador_pierde += 1

            contador_jugadas += 1

        else:
            print('Hubo un error, intente nuevamente')

        print(f'''El jugador {name}, empata: {contador_empata}, 
                gana:{contador_gana}, pierde: {contador_pierde}, jugo: {contador_jugadas}''')
