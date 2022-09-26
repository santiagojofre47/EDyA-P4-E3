from claseArbolBinario import ArbolBinario

if __name__ == '__main__':
    objArbol = ArbolBinario()
    detener = False
    while not detener:
        clave = int(input('Ingrese la clave del nodo (-1 para salir): '))
        if clave == -1:
            detener = True
        else:
            objArbol.insertar(objArbol.getRaiz(), clave)
    clave = int(input('Ingrese la clave de un nodo: '))
    objArbol.mostrarParientes(objArbol.getRaiz(), clave)
    cant_nodos = objArbol.getCantidadNodos(objArbol.getRaiz())
    print('Cantidad de nodos del arbol: {}'. format(cant_nodos))
    altura = objArbol.Altura(objArbol.getRaiz())
    print('Altura del arbol: {}' .format(altura))
    clave = int(input('Ingrese la clave de un nodo: '))
    print('Sucesores del nodo {}:'.format(clave))
    objArbol.getSucesores(clave)


