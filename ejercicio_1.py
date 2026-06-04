
lista_productos = []

print("***** Sistema Fruna *****");
print("** Vers - 0.0.1 **");

pedido = input("\nDesea crear lista de productos?: ").upper()

if pedido == "SI":
        print("\n*** Iniciando lista de productos ***")
        print("------------------------------------------")

        productos = input("Nombre del producto: ")
        precios = int(input("Precio del producto: "))

        nuevo_prod = {
                "Producto": productos,
                "Precio": precios
        }

        lista_productos.append(nuevo_prod)
        print("------------------------------------------")
        print("\nProducto añadido correctamente")
        
        while True:
            confirmacion = input("\nDesea agregar otro producto?: ").upper()

            if confirmacion == "APARTE":

                productos = input("Nombre del producto: ")
                precios = int(input("Precio del producto: "))

                nuevo_prod = {
                    "Producto": productos,
                    "Precio": precios
                }

                lista_productos.append(nuevo_prod)
                print("\nProducto añadido correctamente")


            elif confirmacion == "AHINOMAS":
                print("Ha dejado de agregar productos.")
                break
            else:
                print("Opciones no validas")

print("\n*** Lista de productos ***")
for i in lista_productos:
    print("---")
    print("Producto:", i["Producto"]) 
    print("Precio:", i["Precio"])
    print("---")

    

        


