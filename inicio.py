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

#iniciar programa
main()