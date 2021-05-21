from Algoritmos import Algoritmos
from bokeh.plotting import figure, output_file, show


def graficar(lista1, lista2):
    output_file('vista.html')
    salida = figure()
    salida.square(lista1, lista2, size=100, color='#ff0000')
    show(salida)


# def centrar(lista):
#     print(lista)
#     for i in lista:
#         i = i + 0.5
#     return lista



if __name__ == "__main__":

    x = int(input('Ingresa el valor de x = '))
    y = int(input('Ingresa el valor de y = '))
    x2 = int(input('Ingresa el valor de x2 = '))
    y2 = int(input('Ingresa el valor de y2 = '))

    print("""Selecciona el algoritmo
    
        1)DDA
        2)Brezenham

    """)
    operacion = int(input(":: "))
    obj = Algoritmos(x, y,x2,y2)


    if (operacion == 1):
        obj.dda()
        lista_x = obj.varx
        lista_y = obj.vary
        graficar(lista_x, lista_y)

    else:
        obj.brezenham()
        lista_x = obj.varx
        lista_y = obj.vary
        graficar(lista_x, lista_y)