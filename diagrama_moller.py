def diagrama_moller(z):
    subniveles = []  #Lista que almacenara la distribucion de lectrones de 'Z'
    moller = {'1s': 2, '2s': 2, '2p': 6, '3s': 2, '3p': 6, '4s': 2, '3d': 10, '4p': 6, '5s': 2, '4d': 10, '5p': 6,
              '6s': 2, '4f': 14, '5d': 10, '6p': 6, '7s': 2, '5f': 14, '6d': 10, '7p': 6}
    #For que recorre el diccionario moller como si fuera el diagrama de moller
    for k,v  in moller.items():
        tem = z
        z = z - v #Se resta a Z el valor que corresponde el subnivel de cada orbital
        if z <= 0:
            subniveles.append(k + str(tem))
            break
        else:
            subniveles.append(k + str(v))

    return subniveles


def distribucion_electrones():
    elementos = {} #diccionario que almacenara el nombre y numero atomico de los elementos
    print('Ingrese el nombre  y su numero atómico(z) de los elementos quimicos.\n'
          'La longitud del nombre debe ser menor de 50 y el numero atomico debe\n'
          'estar entre 0 y 118 incluido el 0 y el 118, ingrese exit para dejar\n '
          'de ingresar mas elementos.')
    while True:
        nombre = input('Nombre: ')
        #Si la longitud del nombre es mayor a 50, seguira pidiendo hasta que se ingrese uno correcto
        while len(nombre)>50:
            nombre = input('Nombre: ')

        #Condicion que verifica para salir de while
        if nombre == 'exit':
            break

        z = int(input('z: '))
        #si el z ingresado esta fuera de rango seguira pidiendo que se ingrese el z correcto
        while (z<0 or z>118):
            z = int(input('z: '))

        elementos[nombre] = z

    #For que recorre los valores(z) de los elementos quimicos ingresados
    for val in elementos.values():
        #se llama a la funcion diagrama_moller y se le pasa como parametro el z de cada elemento
        # devuelve una lista con la distribucion de los electrones de z
        electrones = diagrama_moller(val)
        print('')
        #se imprime por pantalla la distribucion de electrones de z para cada elemento
        for e in electrones: print(e, end=' ')


if __name__ == '__main__':
    distribucion_electrones()