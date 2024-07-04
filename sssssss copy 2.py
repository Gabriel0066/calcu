import csv

def difinombre(numero):
    if numero=='1':
        return'principiante'
    elif numero=='2':
        return'experimentado'
    elif numero==3:
        return'experto'
    else:
        return'desconocido'
try:
    with open('datosva.csv','w')as archivo_csv:
            juegos_csv=csv.writer(archivo_csv)
            juegos_csv.writerow(['ID','Nombre','Valorant','Fortnite','fifa','dificultad'])
            dificultadnivel=input('elija dificultad 1.princiante 2.experimentado 3. experto ')
            dificultad=difinombre(dificultadnivel)
            id=input('ingrese ID jugador ')
            nombre=input('ingrese nombre ')
            puntaje1=int(input('puntaje valorant '))
            puntaje2=int(input('puntaje fortnite '))
            puntaje3=int(input('puntaje fifa '))
            juegos_csv.writerow([
            [id, nombre, puntaje1, puntaje2, puntaje3, dificultad],
            ])
except ValueError:
    print('errorrrrrrrr!!!!!!! debe ser un caracter valido')
    
with open('datosva.csv','r',newline='') as archivo_csv:
    juegos_csv=csv.reader(archivo_csv)
    for fila in juegos_csv:
        print(fila)
