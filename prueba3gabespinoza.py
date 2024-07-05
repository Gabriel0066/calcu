import csv

def difinombre(numero):
    if numero=='1':
        return'principiante'
    elif numero=='2':
        return'avanzado'
    elif numero=='3':
        return'experto'
    else:
        return 'invalido'

try:
    with open('datos.csv','w') as archivo_csv:
        escritorcsv=csv.writer(archivo_csv)
        difi=(input('ingrese numero de dificultad 1. Principiante 2. avanzado 3. experto '))
        dificultad=difinombre(difi)
        id=input('ingrese Nickname(id) ')
        nombre=input('ingrese Nombre ')
        puntajev=int(input('ingrese puntaje de valorant '))
        puntajef=int(input('ingrese puntaje de Fortnite '))
        puntajefi=int(input('ingrese puntaje de fifa '))
        escritorcsv.writerow(['      Tabla csv puntajes y dificulad        '])
        escritorcsv.writerow([' ID de jugador',' Nombre ',' Valonrant ',' Fortnite ',' fifa ',' dificultad '])
        escritorcsv.writerow([
            [ id , nombre , puntajev , puntajef, puntajefi , dificultad ],
        ])
except ValueError:
    print('error!!! caracter no valido!!!!!!!!!!!!')
try:
    with open('datos.csv','r')as archivo_csv:
        escritorcsv=csv.reader(archivo_csv)
        for fila in archivo_csv:
            print(fila)
except FileNotFoundError:
 print('archivo no encontrado')