from persona import persona

miscontactos= [persona(123, "Luis", "Casa 1"), persona(321, "Juan", "Casa 2")]

def crearContacto(numero,nombre,direccion):
    miscontactos.append(persona(numero,nombre,direccion))
    print("\n\tContacto almacenado\n")

def buscarContacto(nombre):
    if len(miscontactos) ==0:
        print("La lista esta vacia, no hay contactos por buscar")
    else:
        encontrado=False
        for i in range(len(miscontactos)):
            if miscontactos[i].vernombre()== nombre:
                print("El telefono es", miscontactos[i].vernumero())
                print("La direccion es", miscontactos[i].verdireccion())
                encontrado= True
                break
            else:
                encontrado= False
        if encontrado== False:
            print("Dato no existente")

def mostrarcontactos():
    if len(miscontactos)==0:
        print("La lista esta vacia, no hay contactos por mostrar")
    else: 
        for i in range(len(miscontactos)):
            print("Nombre: ", miscontactos[i].vernombre(), " Direccion: ", miscontactos[i].verdireccion(), " Numero: ", miscontactos[i].vernumero())

def modificarcontacto(nombre):
    if len(miscontactos) ==0:
        print("La lista esta vacia, no hay contactos por buscar")
    else:
        encontrado=False
        posicion= None
        for i in range(len(miscontactos)):
            if miscontactos[i].vernombre()== nombre:
                posicion= i
                encontrado= True
                break
            else:
                encontrado= False
        if encontrado:
            print("Ingrese nuevo numero")
            nuevonumero=int(input())
            print("Ingrese nuevo nombre")
            nuevonombre=input()
            print("Ingrese nueva direccion")
            nuevodireccion= input()
            miscontactos[posicion].modificarnumero(nuevonumero)
            miscontactos[posicion].modificarnombre(nuevonombre)
            miscontactos[posicion].modificardireccion(nuevodireccion)
            print("Datos actualizados")
        else: 
            print("Dato no encontrado")

def eliminarcontacto(nombre):
    if len(miscontactos) ==0:
        print("La lista esta vacia, no hay contactos por buscar")
    else:
        encontrado=False
        posicion= None
        for i in range(len(miscontactos)):
            if miscontactos[i].vernombre()== nombre:
                posicion= i
                encontrado= True
                break
            else:
                encontrado= False
        if encontrado:
            miscontactos.pop(posicion)
            print("Datos eliminados")
        else: 
            print("Dato no encontrado")

def crearrepote():
    documento = open("reporte contactos.html","w")
    documento.write("<!doctype html>\n")
    documento.write("<html>\n")
    documento.write("<head>\n")
    documento.write("\t<title>Agenda 2022</title>\n")
    documento.write("</head>\n")
    documento.write("<body>\n")
    documento.write("\t<center>\n")
    documento.write("\t<h1>Mis contactos</h1>\n")
    documento.write('\t<table border="1">\n')
    documento.write("\t\t<tr>\n")
    documento.write("\t\t\t<td>Número de teléfono</td><td>Nombre</td><td>Dirección</td>\n")
    for i in range(len(miscontactos)):
        documento.write("\t\t<tr>\n")
        documento.write("\t\t\t<td>" + str(miscontactos[i].vernumero()) + "</td><td>" + miscontactos[i].vernombre() + "</td><td>" + miscontactos[i].verdireccion() + "</td>")
        documento.write("\t\t</tr>\n")

    documento.write("\t\t</tr>\n")
    documento.write("\t</table>\n")
    documento.write("\t</center>\n")
    documento.write("</body>\n")
    documento.write("</html>")
    documento.close()
    print("Reporte HTML creado con éxito...")

    print("Creando reporte HTML")

def main():
    op=0    
    while op != 7:
        print("------Agenda 2022-----")
        print("1. Crear contacto")
        print("2. Buscar contacto")
        print("3. Ver contacto")
        print("4. Modificar contacto")
        print("5. Eliminar contacto")
        print("6. Reporte HTML")
        print("7. Salir\n")  
        print("\tIngrese numero de opcion")
        op=int(input())
        if op == 1:
            print("Ingrese numero")
            numero=int(input())
            print("Ingrese nombre")
            nombre=input()
            print("Ingrese direccion")
            direccion=input()
            crearContacto(numero, nombre, direccion)
        elif op==2:
            print("Ingrese nombre del contacto a buscar")
            nombre=input()
            buscarContacto(nombre)
        elif op==3:
            mostrarcontactos()
        elif op==4:
            print("Ingrese nombre del contacto: ")
            nombre=input()
            modificarcontacto(nombre)
        elif op==5:
            print("Ingrese nombre del contacto: ")
            nombre=input()
            eliminarcontacto(nombre)
        elif op==6:
            crearrepote()
        elif op==7:
            print("\tPrograma Finalizado")
        else:   
            print("Opcion incorrecta")

#iniciar programa
main()