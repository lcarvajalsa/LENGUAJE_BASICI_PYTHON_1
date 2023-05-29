lunes={
    "nombre": "paula",
    "apellido":"romero",
    "materia": "director de grupo - comunicacion",
    "telefono":"3215342819"
}
martes={
    "nombre": "jonathan ",
    "apellido":"espitia",
    "materia": "sql extendido relacionales y no relacionales",
    "telefono": "3102465054"
}
miercoles={
    "nombre": "jonathan",
    "apellido":"espitia",
    "materia": "asesoria proyecto",
    "telefono": "3102465054"
}
jueves={
    "nombre": "paola",
    "apellido":"ballen",
    "materia": "arquitectura de software",
    "telefono": "3114325687"
}
viernes={
    "nombre": "henry",
    "apellido":"caicedo",
    "materia": "fron end 1 node.js",
    "telefono": "3149762032"
}
sabado={
    "nombre": "jennifer",
    "apellido":"fajardo",
    "materia": "lenguaje basico python",
    "telefono": "3014985481"
}
f2557861={
        "agenda":lunes,
        "agenda1":martes,
        "agenda2":miercoles,
        "agenda3":jueves,
        "agenda4":viernes,
        "agenda5":sabado 
}
print("Ficha 2557861")
#Nos pide el nombre del instructor.
ingreso=(int(input("UNO para buscar, DOS para ingresar \n")))
while ingreso>=1 or ingreso<=2:
    if ingreso==1:
        print(f2557861)
    #solicita al usuario ingresar el texto de la busqueda
        prefijo = input("Ingrese el prefijo a buscar: ")
        resultados = []
        
        #revisa todo el diccionario y compara todos los registros dentro, si coincide que comienzan con lo ingresado por el usuario, entonces los guarda en la variable resultados
        for key in f2557861:
            for key1 in f2557861[key]:
                if key1.startswith(prefijo):
                    resultados.append (key1)
        #siempre y cuando halla encontrado resultados imprimirá todos los resultados
            if len(resultados) > 0:
                for resultado in resultados:
                    print(resultado)
            else:
                print("No se encontraron registros con el prefijo especificado.")    
    elif ingreso==2:        
        consulta=(str(input("Escribe el nombre o apellido del instructor\n")))
        consulta=consulta.lower()
        if consulta==lunes.get("nombre") or consulta==lunes.get("apellido"):
            print (lunes.get("materia"))
            print (lunes.get("telefono"))
            modificar=(int(input("UNO si decea modifícar, DOS para salir\n")))
            if modificar==1:            
                descripcion=(int(input("UNO nombre, DOS apellido, TRES materia, CUATRO telefono\n")))
                while descripcion>=1 or descripcion<=4:
                    if descripcion==1:
                        tipo=(str(input("Escribe Nombre\n")))
                        tipo=tipo.lower()
                        lunes["nombre"] = tipo
                        print(lunes)
                    elif descripcion==2:
                        tipo=(str(input("Escribe Apellido\n")))
                        tipo=tipo.lower()
                        lunes["apellido"] = tipo
                    elif descripcion==3:
                        tipo=(str(input("Escribe Materia\n")))
                        tipo=tipo.lower()
                        lunes["materia"] = tipo
                    elif descripcion==4:
                        tipo=(str(input("Escribe Telefono\n")))
                        tipo=tipo.lower()
                        lunes["telefono"] = tipo
                    else:
                        break
                    descripcion=(int(input("UNO nombre, DOS apellido, TRES materia, CUATRO telefono, CINCO para salir\n")))
        elif consulta==martes.get("nombre") or consulta==martes.get("apellido"):
            print (martes.get("materia"))
            print (martes.get("telefono"))
            modificar=(int(input("UNO si decea modificar, DOS para salir\n")))
            if modificar==1:
                print("Describe el dato que decea modificar\n")
                descripcion=(int(input("UNO nombre, DOS apellido, TRES materia, CUATRO telefono\n")))
                while descripcion>=1 and descripcion<=4:
                    if descripcion==1:
                        tipo=(str(input("Escribe Nombre\n")))
                        tipo=tipo.lower()
                        martes["nombre"] = tipo
                    elif descripcion==2:
                        tipo=(str(input("Escribe Apellido\n")))
                        tipo=tipo.lower()
                        martes["apellido"] = tipo
                    elif descripcion==3:
                        tipo=(str(input("Escribe Materia\n")))
                        tipo=tipo.lower()
                        martes["materia"] = tipo
                    elif descripcion==4:
                        tipo=(str(input("Escribe Telefono\n")))
                        tipo=tipo.lower()
                        martes["telefono"] = tipo 
                    else:
                        break   
                    descripcion=(int(input("UNO nombre, DOS apellido, TRES materia, CUATRO telefono, CINCO para salir\n")))    
        elif consulta==miercoles.get("nombre") or consulta==miercoles.get("apellido"):
            print (miercoles.get("materia"))
            print (miercoles.get("telefono"))
            modificar=(int(input("UNO si Desea modificar, DOS para salir\n")))
            if modificar==1:
                print("Describe el dato que desea modificar\n")
                descripcion=(int(input("UNO nombre, DOS apellido, TRES materia, CUATRO telefono\n")))
                while descripcion>=1 or descripcion<=4:
                    if descripcion==1:
                        tipo=(str(input("Escribe Nombre\n")))
                        tipo=tipo.lower()
                        miercoles["nombre"] = tipo
                    elif descripcion==2:
                        tipo=(str(input("Escribe Apellido\n")))
                        tipo=tipo.lower()
                        miercoles["apellido"] = tipo
                    elif descripcion==3:
                        tipo=(str(input("Escribe Materia\n")))
                        tipo=tipo.lower()
                        miercoles["materia"] = tipo
                    elif descripcion==4:
                        tipo=(str(input("Escribe Telefono\n")))
                        tipo=tipo.lower()
                        miercoles["telefono"] = tipo 
                    else:
                        break    
                    descripcion=(int(input("UNO nombre, DOS apellido, TRES materia, CUATRO telefono,CINCO para salir\n")))
        elif consulta==jueves.get("nombre") or consulta==jueves.get("apellido"):
            print (jueves.get("materia"))
            print (jueves.get("telefono"))
            modificar=(int(input("UNO si Desea modificar, DOS para salir\n")))
            if modificar==1:
                print("Describe el dato que desea modificar\n")
                descripcion=(int(input("UNO nombre, DOS apellido, TRES materia, CUATRO telefono\n")))
                while descripcion>=1 or descripcion<=4:
                    if descripcion==1:
                        tipo=(str(input("Escribe Nombre\n")))
                        tipo=tipo.lower()
                        jueves["nombre"] = tipo
                    elif descripcion==2:
                        tipo=(str(input("Escribe Apellido\n")))
                        tipo=tipo.lower()
                        jueves["apellido"] = tipo
                    elif descripcion==3:
                        tipo=(str(input("Escribe Materia\n")))
                        tipo=tipo.lower()
                        jueves["materia"] = tipo
                    elif descripcion==4:
                        tipo=(str(input("Escribe Telefono\n")))
                        tipo=tipo.lower()
                        jueves["telefono"] = tipo 
                    else:
                        break    
                    descripcion=(int(input("UNO nombre, DOS apellido, TRES materia, CUATRO telefono, CINCO para salir\n")))
        elif consulta==viernes.get("nombre") or consulta==viernes.get("apellido"):
            print (viernes.get("materia"))
            print (viernes.get("telefono"))
            modificar=(int(input("UNO si Desea modificar, DOS para salir\n")))
            if modificar==1:
                print("Describe el dato que desea modificar\n")
                descripcion=(int(input("UNO nombre, DOS apellido, TRES materia, CUATRO telefono\n")))
                while descripcion>=1 or descripcion<=4:
                    if descripcion==1:
                        tipo=(str(input("Escribe Nombre\n")))
                        tipo=tipo.lower()
                        viernes["nombre"] = tipo
                    elif descripcion==2:
                        tipo=(str(input("Escribe Apellido\n")))
                        tipo=tipo.lower()
                        viernes["apellido"] = tipo
                    elif descripcion==3:
                        tipo=(str(input("Escribe Materia\n")))
                        tipo=tipo.lower()
                        viernes["materia"] = tipo
                    elif descripcion==4:
                        tipo=(str(input("Escribe Telefono\n")))
                        tipo=tipo.lower()
                        viernes["telefono"] = tipo 
                    else:
                        break     
                    descripcion=(int(input("UNO nombre, DOS apellido, TRES materia, CUATRO telefono, CINCO para salir\n")))
        elif consulta==sabado.get("nombre") or consulta==sabado.get("apellido"):
            print (sabado.get("materia"))
            print (sabado.get("telefono"))
            modificar=(int(input("UNO si Desea modificar, DOS para salir\n")))
            if modificar==1:
                print("Describe el dato que desea modificar\n")
                descripcion=(int(input("UNO nombre, DOS apellido, TRES materia, CUATRO telefono\n")))
                while descripcion>=1 or descripcion<=4:
                    if descripcion==1:
                        tipo=(str(input("Escribe Nombre\n")))
                        tipo=tipo.lower()
                        sabado["nombre"] = tipo
                    elif descripcion==2:
                        tipo=(str(input("Escribe Apellido\n")))
                        tipo=tipo.lower()
                        sabado["apellido"] = tipo
                    elif descripcion==3:
                        tipo=(str(input("Escribe Materia\n")))
                        tipo=tipo.lower()
                        sabado["materia"] = tipo
                    elif descripcion==4:
                        tipo=(str(input("Escribe Telefono\n")))
                        tipo=tipo.lower()
                        sabado["telefono"] = tipo 
                    break    
                descripcion=(int(input("UNO nombre, DOS apellido, TRES materia, CUATRO telefono, CINCO para salir\n")))
        else:
            print ("Instructor no esta asignado a esta ficha")
            dato=(int(input("UNO para registrar, DOS para salir\n")))
            while dato==1:
                print("Ingrese día de la semana que va a programar")
                dato1=(input("Día\n"))
                dato1=dato1.lower()
                if dato1=="lunes":
                    tipo=(str(input("Escribe Nombre\n")))
                    lunes["nombre"] = tipo
                    tipo=(str(input("Escribe Apellido\n")))
                    lunes["apellido"] = tipo
                    tipo=(str(input("Escribe Materia\n")))
                    lunes["materia"] = tipo
                    tipo=(str(input("Escribe Telefono\n")))
                    lunes["telefono"] = tipo  
                    print([lunes])  
                    
                elif dato1=="martes":
                    tipo=(str(input("Escribe Nombre\n")))
                    martes["nombre"] = tipo
                    tipo=(str(input("Escribe Apellido\n")))
                    martes["apellido"] = tipo
                    tipo=(str(input("Escribe Materia\n")))
                    martes["materia"] = tipo
                    tipo=(str(input("Escribe Telefono\n")))
                    martes["telefono"] = tipo   
                elif dato1=="miercoles":
                    tipo=(str(input("Escribe Nombre\n")))
                    miercoles["nombre"] = tipo
                    tipo=(str(input("Escribe Apellido\n")))
                    miercoles["apellido"] = tipo
                    tipo=(str(input("Escribe Materia\n")))
                    miercoles["materia"] = tipo
                    tipo=(str(input("Escribe Telefono\n")))
                    miercoles["telefono"] = tipo   
                elif dato1=="jueves":
                    tipo=(str(input("Escribe Nombre\n")))
                    jueves["nombre"] = tipo
                    tipo=(str(input("Escribe Apellido\n")))
                    jueves["apellido"] = tipo
                    tipo=(str(input("Escribe Materia\n")))
                    jueves["materia"] = tipo
                    tipo=(str(input("Escribe Telefono\n")))
                    jueves["telefono"] = tipo   
                elif dato1=="viernes":
                    tipo=(str(input("Escribe Nombre\n")))
                    viernes["nombre"] = tipo
                    tipo=(str(input("Escribe Apellido\n")))
                    viernes["apellido"] = tipo
                    tipo=(str(input("Escribe Materia\n")))
                    viernes["materia"] = tipo
                    tipo=(str(input("Escribe Telefono\n")))
                    viernes["telefono"] = tipo   
                elif dato1=="sabado":
                    tipo=(str(input("Escribe Nombre\n")))
                    sabado["nombre"] = tipo
                    tipo=(str(input("Escribe Apellido\n")))
                    sabado["apellido"] = tipo
                    tipo=(str(input("Escribe Materia\n")))
                    sabado["materia"] = tipo
                    tipo=(str(input("Escribe Telefono\n")))
                    sabado["telefono"] = tipo
                else:   
                    print("dato incorrepto")
                    

print("Que tenga un excelente día")   
                    
'''Buscar: Nos pide ingresar un texto de búsqueda y nos muestra todos los contactos cuyos nombres comiencen por dicha cadena.
Borrar: Nos pide ingresar el nombre del instructor y si existe nos preguntará si queremos borrarlo de la agenda.
¿Cómo podría borrar un key dentro de un instructor en particular?
Listar: Nos muestra todos los instructores de la agenda.
'''  
                        

