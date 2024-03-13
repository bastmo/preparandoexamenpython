bandas=[]


#Construyendo la interfaz 
print("***ALTAVOZ ES TU VOZ***")
print("***********************")

opcion=100
while(opcion!=5):

    print("1. Registrar Banda")
    print("2. Buscar informacion de una Banda")
    print("3. Agenda del evento")
    print("4. Modificar una Banda")
    print("5. SALIR")

    opcion=int(input("Digita una opcion: "))

    if opcion==1:
        banda={}
        #creando los datos del diccionario
        banda["id"]=int(input("Digita el id: "))
        banda["nombre"]=input("Nombre de la banda: ")
        banda["genero"]=input("Genero: ")
        banda["clasificacion"]=input("Clasificacion: ")
        banda["tiempo"]=int(input("Tiempo: "))
        banda["costo"]=int(input("Digita el costo: $"))
        
        #Agregando un diccionario a una lista 
        bandas.append(banda)

    elif opcion==2:
        
        bandaBuscada=input("digita el nombre de la banda que esta buscando: ")
        for bandaAuxiliar in bandas:
            if bandaAuxiliar["nombre"]==bandaBuscada:
                #Como lo encontre muestro los datos de bandaAuxiliar 
                print(f"id: {bandaAuxiliar["id"]} --- nombre: {bandaAuxiliar["nombre"]} ") 
            else:
                print("Parce siga buscando....")

    elif opcion==3:
        print(bandas)
    elif opcion==4:
        pass
    elif opcion==5:
        pass
    else:
        pass