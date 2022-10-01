from persona import persona

mis_contactos= []

def crearContacto():
    print("Creando Contacto")

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

#iniciar programa
main()