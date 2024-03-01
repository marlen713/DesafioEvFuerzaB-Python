
# Esta librerias la voy a usar para poder mostrar l umbral especificado python mayor_a.py 40000
# lo cual esto se hace pasandole a sys el dato llamandolo con python mayor_a.py 40000 esto lo coloco abajo en la consola
import sys
resumen = int(sys.argv[1])

ventas = {
    "Enero": 15000,
    "Febrero": 22000,
    "Marzo": 12000,
    "Abril": 17000,
    "Mayo": 81000,
    "Junio": 13000,
    "Julio": 21000,
    "Agosto": 41200,
    "Septiembre": 25000,
    "Octubre": 21500,
    "Noviembre": 91000,
    "Diciembre": 21000
}

# creo mi diccionario luego le coloco la key y value 
diccionario = {k:v for k,v in ventas.items() if v > resumen}
print(diccionario)