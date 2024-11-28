from Stock import stock as  st
from Producto import producto as pr
nombre= "cliente1"
nombre1="cliente2"







def mostrar_menu():
    print("Menú Principal")
    print("1. Pedir Producto")
    print("2.Ver stock")
    print("3. Salir")

def iniciar_sesion(nombre,contrasena):
    
    if nombre == "cliente1"or contrasena=="1" or nombre== "cliente2" or contrasena == "2":
        print(f"Bienvenido, {nombre}!")
        while True:
            mostrar_menu()
            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                st.pedir_producto()
            elif opcion == "2":
                pr.mostrar_stock()
            elif opcion == "3":
                print("Muchas gracias por la compra...")
                break
            
            else:
                print("Opción no válida, por favor intente de nuevo.")
    else:
        print("Nombre o contraseña incorrectos.")

        
nombre_usuario = str( input("Ingrese su nombre: "))
contrasena_usuario = int(input("Ingrese su contraseña: "))
                         

iniciar_sesion(nombre_usuario,contrasena_usuario)
