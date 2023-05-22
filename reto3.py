
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
intructores2557861={
        "agenda":lunes,
        "agenda1":martes,
        "agenda2":miercoles,
        "agenda3":jueves,
        "agenda4":viernes,
        "agenda5":sabado
        
}
print("Ficha 2557861")
#Nos pide el nombre del instructor.
ingreso=(int(input("Uno para ingresar a la ficha\n")))
print(intructores2557861)
while ingreso==1:
    consulta=(str(input("Escribe el nombre o nombre del intructor\n")))
    consulta=consulta.lower()
    if consulta==lunes.get("nombre") or consulta==lunes.get("apellido"):
        print (lunes.get("materia"))
        print (lunes.get("telefono"))
        modificar=(int(input("UNO si Desea modificar, DOS para salir\n")))
        if modificar==1:
            print("Describe el dato que desea modificar\n")
            descripcion=(int(input("UNO nombre, DOS apellido, TRES materia, CUATRO telefono\n")))
            if descripcion==1:
                tipo=(str(input("Escribe Nombre\n")))
                lunes["nombre"] = tipo
            elif descripcion==2:
                tipo=(str(input("Escribe Apellido\n")))
                lunes["apellido"] = tipo
            elif descripcion==3:
                tipo=(str(input("Escribe Materia\n")))
                lunes["materia"] = tipo
            elif descripcion==4:
                tipo=(str(input("Escribe Telefono\n")))
                lunes["telefono"] = tipo 
            else:
                print("No es un caracter especifico")     
            descripcion=(int(input("UNO nombre, DOS apellido, TRES materia, CUATRO telefono\n")))
                
    elif consulta==martes.get("nombre") or consulta==martes.get("apellido"):
        print (martes.get("materia"))
        print (martes.get("telefono"))
        modificar=(int(input("UNO si Desea modificar, DOS para salir\n")))
        if modificar==1:
            print("Describe el dato que desea modificar\n")
            descripcion=(int(input("UNO nombre, DOS apellido, TRES materia, CUATRO telefono\n")))
            if descripcion==1:
                tipo=(str(input("Escribe Nombre\n")))
                martes["nombre"] = tipo
            elif descripcion==2:
                tipo=(str(input("Escribe Apellido\n")))
                martes["apellido"] = tipo
            elif descripcion==3:
                tipo=(str(input("Escribe Materia\n")))
                martes["materia"] = tipo
            elif descripcion==4:
                tipo=(str(input("Escribe Telefono\n")))
                martes["telefono"] = tipo 
            else:
                print("No es un caracter especifico")     
            descripcion=(int(input("UNO nombre, DOS apellido, TRES materia, CUATRO telefono\n")))
        
    elif consulta==miercoles.get("nombre") or consulta==miercoles.get("apellido"):
        print (miercoles.get("materia"))
        print (miercoles.get("telefono"))
        modificar=(int(input("UNO si Desea modificar, DOS para salir\n")))
        if modificar==1:
            print("Describe el dato que desea modificar\n")
            descripcion=(int(input("UNO nombre, DOS apellido, TRES materia, CUATRO telefono\n")))
            if descripcion==1:
                tipo=(str(input("Escribe Nombre\n")))
                miercoles["nombre"] = tipo
            elif descripcion==2:
                tipo=(str(input("Escribe Apellido\n")))
                miercoles["apellido"] = tipo
            elif descripcion==3:
                tipo=(str(input("Escribe Materia\n")))
                miercoles["materia"] = tipo
            elif descripcion==4:
                tipo=(str(input("Escribe Telefono\n")))
                miercoles["telefono"] = tipo 
            else:
                print("No es un caracter especifico")     
            descripcion=(int(input("UNO nombre, DOS apellido, TRES materia, CUATRO telefono\n")))
        
    elif consulta==jueves.get("nombre") or consulta==jueves.get("apellido"):
        print (jueves.get("materia"))
        print (jueves.get("telefono"))
        modificar=(int(input("UNO si Desea modificar, DOS para salir\n")))
        if modificar==1:
            print("Describe el dato que desea modificar\n")
            descripcion=(int(input("UNO nombre, DOS apellido, TRES materia, CUATRO telefono\n")))
            if descripcion==1:
                tipo=(str(input("Escribe Nombre\n")))
                jueves["nombre"] = tipo
            elif descripcion==2:
                tipo=(str(input("Escribe Apellido\n")))
                jueves["apellido"] = tipo
            elif descripcion==3:
                tipo=(str(input("Escribe Materia\n")))
                jueves["materia"] = tipo
            elif descripcion==4:
                tipo=(str(input("Escribe Telefono\n")))
                jueves["telefono"] = tipo 
            else:
                print("No es un caracter especifico")     
            descripcion=(int(input("UNO nombre, DOS apellido, TRES materia, CUATRO telefono\n")))
        
    elif consulta==viernes.get("nombre") or consulta==viernes.get("apellido"):
        print (viernes.get("materia"))
        print (viernes.get("telefono"))
        modificar=(int(input("UNO si Desea modificar, DOS para salir\n")))
        if modificar==1:
            print("Describe el dato que desea modificar\n")
            descripcion=(int(input("UNO nombre, DOS apellido, TRES materia, CUATRO telefono\n")))
            if descripcion==1:
                tipo=(str(input("Escribe Nombre\n")))
                viernes["nombre"] = tipo
            elif descripcion==2:
                tipo=(str(input("Escribe Apellido\n")))
                viernes["apellido"] = tipo
            elif descripcion==3:
                tipo=(str(input("Escribe Materia\n")))
                viernes["materia"] = tipo
            elif descripcion==4:
                tipo=(str(input("Escribe Telefono\n")))
                viernes["telefono"] = tipo 
            else:
                print("No es un caracter especifico")     
            descripcion=(int(input("UNO nombre, DOS apellido, TRES materia, CUATRO telefono\n")))
        
    elif consulta==sabado.get("nombre") or consulta==sabado.get("apellido"):
        print (sabado.get("materia"))
        print (sabado.get("telefono"))
        modificar=(int(input("UNO si Desea modificar, DOS para salir\n")))
        if modificar==1:
            print("Describe el dato que desea modificar\n")
            descripcion=(int(input("UNO nombre, DOS apellido, TRES materia, CUATRO telefono\n")))
            if descripcion==1:
                tipo=(str(input("Escribe Nombre\n")))
                sabado["nombre"] = tipo
            elif descripcion==2:
                tipo=(str(input("Escribe Apellido\n")))
                sabado["apellido"] = tipo
            elif descripcion==3:
                tipo=(str(input("Escribe Materia\n")))
                sabado["materia"] = tipo
            elif descripcion==4:
                tipo=(str(input("Escribe Telefono\n")))
                sabado["telefono"] = tipo 
            else:
                print("No es un caracter especifico")     
            descripcion=(int(input("UNO nombre, DOS apellido, TRES materia, CUATRO telefono\n")))
        
    else:
        print ("Instructor no esta asignado a esta ficha")
        dato=(int(input("UNO para registrar, DOS para salir\n")))
        if dato==1:
            print("Seleciona el dia de lunes a sabado")
            dato=(input("Ingresa día\n"))
            dato=dato.lower()
            if dato=="lunes":
                descripcion=(int(input("UNO para Nombre\n")))
                while descripcion>=1 or descripcion<=4:
                    if descripcion==1:
                        tipo=(str(input("Escribe Nombre\n")))
                        lunes["nombre"] = tipo
                        descripcion=(int(input("Marca DOS Apellido\n")))
                    elif descripcion==2:
                        tipo=(str(input("Escribe Apellido\n")))
                        lunes["apellido"] = tipo
                        descripcion=(int(input("Marca TRES Materia\n")))
                    elif descripcion==3:
                        tipo=(str(input("Escribe Materia\n")))
                        lunes["materia"] = tipo
                        descripcion=(int(input("Marca CUATRO Telefono\n")))
                    elif descripcion==4:
                        tipo=(str(input("Escribe Telefono\n")))
                        lunes["telefono"] = tipo
                        break 
                    else:
                        print("No es un caracter especifico")     
                        descripcion=(int(input("UNO nombre\n")))
                    
            elif dato=="martes":
                descripcion=(int(input("UNO para Nombre\n")))
                while descripcion>=1 or descripcion<=4:
                    if descripcion==1:
                        tipo=(str(input("Escribe Nombre\n")))
                        martes["nombre"] = tipo
                        descripcion=(int(input("DOS Apellido\n")))
                    elif descripcion==2:
                        tipo=(str(input("Escribe Apellido\n")))
                        martes["apellido"] = tipo
                        descripcion=(int(input("TRES Materia \n")))
                    elif descripcion==3:
                        tipo=(str(input("Escribe Materia\n")))
                        martes["materia"] = tipo
                        descripcion=(int(input("CUATRO Telefono\n")))
                    elif descripcion==4:
                        tipo=(str(input("Escribe Telefono\n")))
                        martes["telefono"] = tipo
                        break
                    else:
                        print("No es un caracter especifico")     
                        descripcion=(int(input("Escribe UNO nombre\n")))
            elif dato=="miercoles":
                descripcion=(int(input("UNO para Nombre\n")))
                while descripcion>=1 or descripcion<=4:
                    if descripcion==1:
                        tipo=(str(input("Escribe Nombre\n")))
                        miercoles["nombre"] = tipo
                        descripcion=(int(input("DOS Apellido\n")))
                    elif descripcion==2:
                        tipo=(str(input("Escribe Apellido\n")))
                        miercoles["apellido"] = tipo
                        descripcion=(int(input("TRES Materia\n")))
                    elif descripcion==3:
                        tipo=(str(input("Escribe Materia\n")))
                        miercoles["materia"] = tipo
                        descripcion=(int(input("CUATRO Telefono\n")))
                    elif descripcion==4:
                        tipo=(str(input("Escribe Telefono\n")))
                        miercoles["telefono"] = tipo 
                        break
                    else:
                        print("No es un caracter especifico")     
                        descripcion=(int(input("UNO nombre\n")))
            elif dato=="jueves":
                descripcion=(int(input("UNO para Nombre\n")))
                while descripcion>=1 or descripcion<=4:
                    if descripcion==1:
                        tipo=(str(input("Escribe Nombre\n")))
                        jueves["nombre"] = tipo
                        descripcion=(int(input("DOS Apellido\n")))
                    elif descripcion==2:
                        tipo=(str(input("Escribe Apellido\n")))
                        jueves["apellido"] = tipo
                        descripcion=(int(input("TRES Materia\n")))
                    elif descripcion==3:
                        tipo=(str(input("Escribe Materia\n")))
                        jueves["materia"] = tipo
                        descripcion=(int(input("CUATRO Telefono\n")))
                    elif descripcion==4:
                        tipo=(str(input("Escribe Telefono\n")))
                        jueves["telefono"] = tipo 
                        break
                    else:
                        print("No es un caracter especifico")     
                        descripcion=(int(input("UNO nombre\n")))
            elif dato=="viernes":
                descripcion=(int(input("UNO para Nombre\n")))
                while descripcion>=1 or descripcion<=4:
                    if descripcion==1:
                        tipo=(str(input("Escribe Nombre\n")))
                        viernes["nombre"] = tipo
                        descripcion=(int(input("DOS Apellido\n")))
                    elif descripcion==2:
                        tipo=(str(input("Escribe Apellido\n")))
                        viernes["apellido"] = tipo
                        descripcion=(int(input("TRES Materia\n")))
                    elif descripcion==3:
                        tipo=(str(input("Escribe Materia\n")))
                        viernes["materia"] = tipo
                        descripcion=(int(input("CUATRO Telefono\n")))
                    elif descripcion==4:
                        tipo=(str(input("Escribe Telefono\n")))
                        viernes["telefono"] = tipo
                    else:
                        print("No es un caracter especifico")     
                        descripcion=(int(input("UNO nombre\n")))
            elif dato=="sabado":
                descripcion=(int(input("UNO para Nombre\n")))
                while descripcion>=1 or descripcion<=4:
                    if descripcion==1:
                        tipo=(str(input("Escribe Nombre\n")))
                        sabado["nombre"] = tipo
                        descripcion=(int(input("DOS Apellido\n")))
                    elif descripcion==2:
                        tipo=(str(input("Escribe Apellido\n")))
                        sabado["apellido"] = tipo
                        descripcion=(int(input("TRES Materia\n")))
                    elif descripcion==3:
                        tipo=(str(input("Escribe Materia\n")))
                        sabado["materia"] = tipo
                        descripcion=(int(input("CUATRO Telefono\n")))
                    elif descripcion==4:
                        tipo=(str(input("Escribe Telefono\n")))
                        sabado["telefono"] = tipo 
                    else:
                        print("No es un caracter especifico") 
                        descripcion=(int(input("UNO nombre\n")))
            else:
                    print("No es un caracter especifico") 
        print("Ingresa Un Texto de Busqueda para el Nombre del Instructor")  
        buscar=(input("Texto\n"))
        buscar=buscar.lower()
'''Buscar: Nos pide ingresar un texto de búsqueda y nos muestra todos los contactos cuyos nombres comiencen por dicha cadena.
Borrar: Nos pide ingresar el nombre del instructor y si existe nos preguntará si queremos borrarlo de la agenda.
¿Cómo podría borrar un key dentro de un instructor en particular?
Listar: Nos muestra todos los instructores de la agenda.
'''  
                        
    ingreso=(int(input("UNO si Desea consultar nuevamente, DOS para salir\n")))   