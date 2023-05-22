#Generamos un diccionario denominado Fruver y deberá permitirse
#realizar las siguientes opciones:
fruver={}
#Agregar
agregar=1
agregar=int(input("Desea agregar un articulo al FRUVER UNO para si, Dos para no\n"))
while agregar==1:
    articulo=str(input("Nombre Articulo\n"))
    valor=int(input("valor del Articulo\n"))
    for x in fruver:
        if articulo==x:
            print("Este articulo ya se encuentra registrado")
            articulo="0"
            valor=0
    fruver[articulo]=valor
    if articulo=="0":
        del fruver["0"]
    agregar=int(input("Desea agregar un articulo al FRUVER UNO para si, Dos para no\n")) 
for x, y in fruver.items():
    print(x, ":", y)
    agregar1=int(input("ingresar un texto de búsqueda\n"))  
       
#modificar
#Solicitar el nombre de la fruta.
#Si ésta ya se encuentra registrada, 
#deberá mostrar que ya se encuentra registrado
#y el precio de la fruta.
# Si el nombre no se encuentra,
# debe permitir ingresar los datos correspondientes.
#Buscar: 
# Nos pide ingresar un texto de búsqueda
# y nos muestra todas las frutas que comiencen con esa cadena.
#Borrar: 
# Nos pide ingresar el nombre del articulo a borrar,
# si existe nos preguntará si queremos borrarlo del fruver.
#Listar: 
# Nos muestra todos los artículos del fruver.
