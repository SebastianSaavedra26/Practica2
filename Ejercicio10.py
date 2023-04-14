#10. Dada una lista de nombres de estudiantes y dos listas con sus notas en un curso, escriba un
#programa que manipule dichas estructuras de datos para poder resolver los siguientes puntos:
#A. Generar una estructura con todas las notas relacionando el nombre del estudiante con las
#notas. Utilizar esta estructura para la resolución de los siguientes items.
#B. Calcular el promedio de notas de cada estudiante.
#C. Calcular el promedio general del curso.
#D. Identificar al estudiante con la nota promedio más alta.
#E. Identificar al estudiante con la nota más baja.
#Nota:
#• Las 3 estructuras están ordenadas de forma que los elementos en la misma posición corresponden
#a un mismo alumno.
 #• Realizar funciones con cada item
nombres = ''' 'Agustin', 'Alan', 'Andrés', 'Ariadna', 'Bautista', 'CAROLINA', 'CESAR',
'David','Diego', 'Dolores', 'DYLAN', 'ELIANA', 'Emanuel', 'Fabián', 'Facundo',
'Francsica', 'FEDERICO', 'Fernanda', 'GONZALO', 'Gregorio', 'Ignacio', 'Jonathan',
'Joaquina', 'Jorge','JOSE', 'Javier', 'Joaquín' , 'Julian', 'Julieta', 'Luciana',
'LAUTARO', 'Leonel', 'Luisa', 'Luis', 'Marcos', 'María', 'MATEO', 'Matias',
'Nicolás', 'Nancy', 'Noelia', 'Pablo', 'Priscila', 'Sabrina', 'Tomás', 'Ulises',
'Yanina' '''
notas_1 = [81, 60, 72, 24, 15, 91, 12, 70, 29, 42, 16, 3, 35, 67, 10, 57, 11, 69,
12, 77, 13, 86, 48, 65, 51, 41, 87, 43, 10, 87, 91, 15, 44,
85, 73, 37, 42, 95, 18, 7, 74, 60, 9, 65, 93, 63, 74]
notas_2 = [30, 95, 28, 84, 84, 43, 66, 51, 4, 11, 58, 10, 13, 34, 96, 71, 86, 37,
64, 13, 8, 87, 14, 14, 49, 27, 55, 69, 77, 59, 57, 40, 96, 24, 30, 73,
95, 19, 47, 15, 31, 39, 15, 74, 33, 57, 10]

diccionario = {}
diccionario_todo={}
lista_notas=zip(notas_1,notas_2)
diccionario_todo={k:v for(k,v) in zip(nombres.split(","),lista_notas)}

#inciso A
print('inciso a')
print(diccionario_todo)

#inciso B
i=0
print('inciso b')
promedios=map(lambda a,b:(a+b)/2, notas_1, notas_2)
diccionario={k:v for(k,v) in zip(nombres.split(","),promedios)}
print(diccionario)
#inciso C
print('inciso c')
prom_notas= (sum(diccionario.values())/len(notas_2))
print(round(prom_notas, 2))
#inciso D
print('inciso d')
clave_max=max(diccionario, key=diccionario.get)
print(clave_max)
print(diccionario[clave_max])
#inciso E
print('inciso e')
alumno_min=min(diccionario_todo, key=lambda key: diccionario_todo[key][0] if diccionario_todo[key][0]<diccionario_todo[key][1] else diccionario_todo[key][1])
print(f"nombre:{alumno_min} notas: {min(diccionario_todo[alumno_min])} ")
