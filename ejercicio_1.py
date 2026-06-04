
lista_productos = []

print("***** Sistema Fruna *****");
print("** Vers - 0.0.1 **");

pedido = input("Desea agregar productos al listado?: ").upper()

if pedido == "SI":
        productos = input("Nombre del producto: ")
        precios = int(input("Precio del producto: "))

        nuevo_prod = {
                "Producto": productos,
                "Precio": precios
        }

        lista_productos.append(nuevo_prod)
        print("n\Producto añadido correctamente")

        confirmacion = input("Desea agregar otro producto?: ").upper()


        while confirmacion == "APARTE":
            productos = input("Nombre del producto: ")
            precios = int(input("Precio del producto: "))

            nuevo_prod = {
                  "Producto": productos,
                  "Precio": precios
            }

            lista_productos.append(nuevo_prod)
            print("n\Producto añadido correctamente")


        if confirmacion == "AHINOMAS":
                print("Ha dejado de agregar productos.")
                break

print("*** Lista de productos ***")
for i in lista_productos:
    print("Producto:", i["Producto"]) 
    print("Precio:", i["Precio"])
    print("---")

    

        


