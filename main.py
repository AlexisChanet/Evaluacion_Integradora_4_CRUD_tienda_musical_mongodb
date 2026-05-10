from datetime import datetime
from db import coleccion
from producto_musical import ProductoMusical


# Funciones de apoyo

def pausar():
    input("\nPresione Enter para continuar...")


def pedir_texto(mensaje):
    while True:
        dato = input(mensaje).strip()

        if dato != "":
            return dato

        print("Error: el campo no puede quedar vacío.")


def pedir_rut(mensaje):
    while True:
        rut = input(mensaje).strip()

        if "." in rut and "-" in rut:
            return rut

        print("Error: ingrese el RUT con puntos y guion. Ejemplo: 20.497.593-0")


def pedir_entero(mensaje, minimo=0, maximo=100000000):
    while True:
        try:
            numero = int(input(mensaje))

            if numero < minimo:
                print(f"Error: el número debe ser mayor o igual a {minimo}.")
            elif numero > maximo:
                print(f"Error: el número debe ser menor o igual a {maximo}.")
            else:
                return numero

        except ValueError:
            print("Error: debe ingresar un número válido.")


def pedir_fecha(mensaje):
    while True:
        texto = input(mensaje).strip()

        try:
            return datetime.strptime(texto, "%Y-%m-%d")

        except ValueError:
            print("Error: fecha inválida. Use el formato YYYY-MM-DD. Ejemplo: 2026-05-12")


def pedir_si_no(mensaje):
    while True:
        respuesta = input(mensaje).strip().lower()

        if respuesta == "s" or respuesta == "n":
            return respuesta

        print("Debe ingresar 's' para sí o 'n' para no.")


def mostrar_fecha(fecha):
    if isinstance(fecha, datetime):
        return fecha.strftime("%Y-%m-%d")

    return "Sin fecha"


def elegir_metodo_pago():
    while True:
        print("\nSeleccione método de pago:")
        print("1. Débito")
        print("2. Crédito")
        print("3. Efectivo")
        print("4. Transferencia")
        print("0. Volver")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            return "Débito"
        elif opcion == "2":
            return "Crédito"
        elif opcion == "3":
            return "Efectivo"
        elif opcion == "4":
            return "Transferencia"
        elif opcion == "0":
            return None
        else:
            print("Opción no válida.")


def pedir_cliente():
    print("\nDatos del cliente")

    nombre = pedir_texto("Nombre del cliente: ")
    apellido = pedir_texto("Apellido del cliente: ")
    rut = pedir_rut("RUT del cliente, ejemplo 20.497.593-0: ")

    return {
        "nombre": nombre,
        "apellido": apellido,
        "rut": rut
    }


# Busca un producto por título exacto, sin importar mayúsculas o minúsculas.

def buscar_producto_por_titulo(titulo_album):
    return coleccion.find_one({
        "titulo_album": {
            "$regex": f"^{titulo_album}$",
            "$options": "i"
        }
    })


# Muestra solo información principal del producto.

def mostrar_producto_resumen(producto):
    print("\n----------------------------------------")
    print(f"Álbum: {producto.get('titulo_album')}")
    print(f"Artista: {producto.get('artista')}")
    print(f"Género: {producto.get('genero')}")
    print(f"Formato: {producto.get('formato')}")
    print(f"Precio: ${producto.get('precio')}")
    print(f"Stock: {producto.get('stock')}")

    sello = producto.get("sello_discografico", {})
    print(f"Sello discográfico: {sello.get('nombre')} - {sello.get('pais')}")

    ventas = producto.get("ventas", [])
    print(f"Ventas registradas: {len(ventas)}")
    print("----------------------------------------")


# Muestra el detalle del producto, sin mostrar el detalle de ventas.

def mostrar_detalle_producto(producto):
    print("\n----------------------------------------")
    print(f"Álbum: {producto.get('titulo_album')}")
    print(f"Artista: {producto.get('artista')}")
    print(f"Género: {producto.get('genero')}")
    print(f"Formato: {producto.get('formato')}")
    print(f"Precio: ${producto.get('precio')}")
    print(f"Stock: {producto.get('stock')}")
    print(f"Fecha lanzamiento: {mostrar_fecha(producto.get('fecha_lanzamiento'))}")

    sello = producto.get("sello_discografico", {})
    print(f"Sello discográfico: {sello.get('nombre')} - {sello.get('pais')}")

    ventas = producto.get("ventas", [])
    print(f"Ventas registradas: {len(ventas)}")
    print("----------------------------------------")


# Muestra solo el historial de ventas de un producto.

def mostrar_ventas_producto(producto):
    print("\n----------------------------------------")
    print(f"Álbum: {producto.get('titulo_album')}")
    print(f"Artista: {producto.get('artista')}")
    print("----------------------------------------")

    ventas = producto.get("ventas", [])

    if len(ventas) == 0:
        print("Este producto no tiene ventas registradas.")
    else:
        print("Historial de ventas:")

        for venta in ventas:
            cliente = venta.get("cliente", {})

            print("----------------------------------------")
            print(f"Cliente: {cliente.get('nombre')} {cliente.get('apellido')}")
            print(f"RUT: {cliente.get('rut')}")
            print(f"Cantidad: {venta.get('cantidad')}")
            print(f"Fecha venta: {mostrar_fecha(venta.get('fecha_venta'))}")
            print(f"Método de pago: {venta.get('metodo_pago')}")
            print(f"Total: ${venta.get('total')}")

    print("----------------------------------------")


# Crea un nuevo producto musical.

def crear_producto():
    print("\n===== CREAR PRODUCTO MUSICAL =====")

    titulo_album = pedir_texto("Título del álbum: ")

    producto_existente = buscar_producto_por_titulo(titulo_album)

    if producto_existente is not None:
        print("No se puede crear. Ya existe un producto con ese título.")
        pausar()
        return

    artista = pedir_texto("Artista: ")
    genero = pedir_texto("Género: ")
    formato = pedir_texto("Formato (CD/Vinilo/Digital/Cassette): ")

    precio = pedir_entero("Precio: ", 1)
    stock = pedir_entero("Stock inicial: ", 0)

    fecha_lanzamiento = pedir_fecha("Fecha de lanzamiento (YYYY-MM-DD): ")

    nombre_sello = pedir_texto("Nombre del sello discográfico: ")
    pais_sello = pedir_texto("País del sello discográfico: ")

    ventas = []
    stock_disponible = stock

    respuesta = pedir_si_no("¿Desea registrar una venta inicial? (s/n): ")

    if respuesta == "s":
        cantidad = pedir_entero("Cantidad vendida: ", 1)

        if cantidad > stock:
            print("No se puede registrar la venta inicial.")
            print("Motivo: la cantidad vendida supera el stock disponible.")
            pausar()
            return

        cliente = pedir_cliente()
        fecha_venta = pedir_fecha("Fecha de venta (YYYY-MM-DD): ")

        metodo_pago = elegir_metodo_pago()

        if metodo_pago is None:
            print("Registro cancelado.")
            pausar()
            return

        total = precio * cantidad
        stock_disponible = stock - cantidad

        ventas.append({
            "cliente": cliente,
            "cantidad": cantidad,
            "fecha_venta": fecha_venta,
            "metodo_pago": metodo_pago,
            "total": total
        })

    sello_discografico = {
        "nombre": nombre_sello,
        "pais": pais_sello
    }

    producto = ProductoMusical(
        titulo_album,
        artista,
        genero,
        formato,
        precio,
        stock_disponible,
        fecha_lanzamiento,
        sello_discografico,
        ventas
    )

    coleccion.insert_one(producto.crear_documento())

    print("\nProducto creado correctamente.")
    pausar()


# Lista los productos registrados.

def listar_productos():
    print("\n===== LISTAR PRODUCTOS =====")

    cantidad = coleccion.count_documents({})
    print(f"Cantidad de productos registrados: {cantidad}")

    if cantidad == 0:
        print("No hay productos registrados.")
        print("Debe ejecutar primero: python cargar_datos.py")
        pausar()
        return

    # Proyección: se solicitan solo los campos necesarios para este listado.
    productos = coleccion.find(
        {},
        {
            "titulo_album": 1,
            "artista": 1,
            "formato": 1,
            "precio": 1,
            "stock": 1,
            "_id": 0
        }
    ).sort("artista", 1)

    for producto in productos:
        print("----------------------------------------")
        print(f"Álbum: {producto.get('titulo_album')}")
        print(f"Artista: {producto.get('artista')}")
        print(f"Formato: {producto.get('formato')}")
        print(f"Precio: ${producto.get('precio')}")
        print(f"Stock: {producto.get('stock')}")

    print("----------------------------------------")
    pausar()


# Muestra el detalle del producto.

def ver_detalle_producto():
    while True:
        print("\n===== VER DETALLE DE PRODUCTO =====")

        texto = pedir_texto("Ingrese título del álbum: ")

        resultados = list(coleccion.find({
            "titulo_album": {
                "$regex": texto,
                "$options": "i"
            }
        }))

        if len(resultados) == 0:
            print("No se encontraron productos con ese título.")
        else:
            print(f"Coincidencias encontradas: {len(resultados)}")

            for producto in resultados:
                mostrar_detalle_producto(producto)

        repetir = input("¿Desea buscar otro álbum? (s/n): ").strip().lower()

        if repetir != "s":
            break


# Muestra las ventas de un producto.

def ver_ventas_producto():
    while True:
        print("\n===== VER VENTAS DE UN PRODUCTO =====")

        titulo_album = pedir_texto("Ingrese título del álbum: ")
        producto = buscar_producto_por_titulo(titulo_album)

        if producto is None:
            print("Producto no encontrado.")
            print("Revise que el título esté escrito correctamente.")
        else:
            mostrar_ventas_producto(producto)

        repetir = input("¿Desea consultar ventas de otro producto? (s/n): ").strip().lower()

        if repetir != "s":
            break


# Busca productos por precio.

def buscar_por_precio():
    while True:
        print("\n===== BUSCAR POR PRECIO =====")
        print("1. Buscar productos con precio mayor que")
        print("2. Buscar productos con precio menor que")
        print("0. Volver al menú")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "0":
            break

        if opcion != "1" and opcion != "2":
            print("Opción no válida.")
            continue

        precio = pedir_entero("Ingrese precio de referencia: ", 0)

        # Proyección: se solicitan solo los campos usados en el resumen.
        if opcion == "1":
            resultados = coleccion.find(
                {"precio": {"$gt": precio}},
                {
                    "titulo_album": 1,
                    "artista": 1,
                    "genero": 1,
                    "formato": 1,
                    "precio": 1,
                    "stock": 1,
                    "sello_discografico": 1,
                    "ventas": 1,
                    "_id": 0
                }
            )
        else:
            resultados = coleccion.find(
                {"precio": {"$lt": precio}},
                {
                    "titulo_album": 1,
                    "artista": 1,
                    "genero": 1,
                    "formato": 1,
                    "precio": 1,
                    "stock": 1,
                    "sello_discografico": 1,
                    "ventas": 1,
                    "_id": 0
                }
            )

        encontrados = 0

        for producto in resultados:
            mostrar_producto_resumen(producto)
            encontrados += 1

        if encontrados == 0:
            print("No se encontraron productos con ese precio.")

        repetir = input("¿Desea buscar otro precio? (s/n): ").strip().lower()

        if repetir != "s":
            break


# Busca productos por título o artista.

def buscar_por_titulo_o_artista():
    while True:
        print("\n===== BUSCAR POR TÍTULO O ARTISTA =====")

        texto = pedir_texto("Ingrese texto a buscar: ")

        resultados = coleccion.find({
            "$or": [
                {"titulo_album": {"$regex": texto, "$options": "i"}},
                {"artista": {"$regex": texto, "$options": "i"}}
            ]
        })

        encontrados = 0

        for producto in resultados:
            mostrar_producto_resumen(producto)
            encontrados += 1

        if encontrados == 0:
            print("No se encontraron coincidencias.")

        repetir = input("¿Desea buscar nuevamente? (s/n): ").strip().lower()

        if repetir != "s":
            break


# Busca productos por rango de fecha de lanzamiento.

def buscar_por_fecha_lanzamiento():
    while True:
        print("\n===== BUSCAR POR RANGO DE FECHAS =====")

        fecha_inicio = pedir_fecha("Fecha inicio (YYYY-MM-DD): ")
        fecha_fin = pedir_fecha("Fecha fin (YYYY-MM-DD): ")

        if fecha_inicio > fecha_fin:
            print("Error: la fecha de inicio no puede ser mayor a la fecha de fin.")
        else:
            resultados = coleccion.find({
                "fecha_lanzamiento": {
                    "$gte": fecha_inicio,
                    "$lte": fecha_fin
                }
            })

            encontrados = 0

            for producto in resultados:
                mostrar_producto_resumen(producto)
                encontrados += 1

            if encontrados == 0:
                print("No se encontraron productos en ese rango de fechas.")

        repetir = input("¿Desea buscar otro rango de fechas? (s/n): ").strip().lower()

        if repetir != "s":
            break


# Busca productos dentro del subdocumento sello_discografico.

def buscar_por_pais_sello():
    while True:
        print("\n===== BUSCAR POR PAÍS DEL SELLO =====")

        pais = pedir_texto("Ingrese país del sello discográfico: ")

        resultados = coleccion.find({
            "sello_discografico.pais": {
                "$regex": pais,
                "$options": "i"
            }
        })

        encontrados = 0

        for producto in resultados:
            mostrar_producto_resumen(producto)
            encontrados += 1

        if encontrados == 0:
            print("No se encontraron productos con ese país de sello.")

        repetir = input("¿Desea buscar otro país? (s/n): ").strip().lower()

        if repetir != "s":
            break


# Busca ventas dentro del array ventas.

def buscar_por_metodo_pago():
    while True:
        print("\n===== BUSCAR VENTAS POR MÉTODO DE PAGO =====")

        metodo = elegir_metodo_pago()

        if metodo is None:
            break

        # Se usa $elemMatch para buscar dentro del array de subdocumentos ventas.
        resultados = coleccion.find({
            "ventas": {
                "$elemMatch": {
                    "metodo_pago": metodo
                }
            }
        })

        encontrados = 0

        for producto in resultados:
            mostrar_producto_resumen(producto)

            ventas = producto.get("ventas", [])
            print("Ventas encontradas con este método:")

            for venta in ventas:
                if venta.get("metodo_pago") == metodo:
                    cliente = venta.get("cliente", {})

                    print("----------------------------------------")
                    print(f"Cliente: {cliente.get('nombre')} {cliente.get('apellido')}")
                    print(f"RUT: {cliente.get('rut')}")
                    print(f"Cantidad: {venta.get('cantidad')}")
                    print(f"Fecha venta: {mostrar_fecha(venta.get('fecha_venta'))}")
                    print(f"Total: ${venta.get('total')}")

            encontrados += 1

        if encontrados == 0:
            print("No se encontraron ventas con ese método de pago.")

        repetir = input("¿Desea buscar otro método de pago? (s/n): ").strip().lower()

        if repetir != "s":
            break


# Actualiza el precio de un producto.

def actualizar_precio():
    print("\n===== ACTUALIZAR PRECIO =====")

    titulo_album = pedir_texto("Ingrese título exacto del álbum: ")
    producto = buscar_producto_por_titulo(titulo_album)

    if producto is None:
        print("Producto no encontrado. No se puede actualizar.")
        pausar()
        return

    print("\nProducto antes de actualizar:")
    mostrar_producto_resumen(producto)

    nuevo_precio = pedir_entero("Ingrese nuevo precio: ", 1)

    coleccion.update_one(
        {"_id": producto["_id"]},
        {"$set": {"precio": nuevo_precio}}
    )

    producto_actualizado = coleccion.find_one({"_id": producto["_id"]})

    print("\nProducto después de actualizar:")
    mostrar_producto_resumen(producto_actualizado)

    pausar()


# Actualiza el país del sello discográfico.

def actualizar_pais_sello():
    print("\n===== ACTUALIZAR PAÍS DEL SELLO =====")

    titulo_album = pedir_texto("Ingrese título exacto del álbum: ")
    producto = buscar_producto_por_titulo(titulo_album)

    if producto is None:
        print("Producto no encontrado. No se puede actualizar.")
        pausar()
        return

    print("\nProducto antes de actualizar:")
    mostrar_producto_resumen(producto)

    nuevo_pais = pedir_texto("Ingrese nuevo país del sello: ")

    coleccion.update_one(
        {"_id": producto["_id"]},
        {"$set": {"sello_discografico.pais": nuevo_pais}}
    )

    producto_actualizado = coleccion.find_one({"_id": producto["_id"]})

    print("\nProducto después de actualizar:")
    mostrar_producto_resumen(producto_actualizado)

    pausar()


# Registra una nueva venta.

def registrar_venta():
    print("\n===== REGISTRAR NUEVA VENTA =====")

    titulo_album = pedir_texto("Ingrese título del álbum: ")
    producto = buscar_producto_por_titulo(titulo_album)

    if producto is None:
        print("Producto no encontrado. No se puede registrar la venta.")
        pausar()
        return

    print("\nProducto seleccionado:")
    mostrar_producto_resumen(producto)

    cantidad = pedir_entero("Cantidad vendida: ", 1)

    stock_actual = producto.get("stock", 0)

    if cantidad > stock_actual:
        print("No hay stock suficiente.")
        print(f"Stock disponible: {stock_actual}")
        pausar()
        return

    cliente = pedir_cliente()
    fecha_venta = pedir_fecha("Fecha de venta (YYYY-MM-DD): ")

    metodo_pago = elegir_metodo_pago()

    if metodo_pago is None:
        print("Venta cancelada.")
        pausar()
        return

    total = producto.get("precio", 0) * cantidad

    nueva_venta = {
        "cliente": cliente,
        "cantidad": cantidad,
        "fecha_venta": fecha_venta,
        "metodo_pago": metodo_pago,
        "total": total
    }

    coleccion.update_one(
        {"_id": producto["_id"]},
        {
            "$push": {"ventas": nueva_venta},
            "$inc": {"stock": -cantidad}
        }
    )

    producto_actualizado = coleccion.find_one({"_id": producto["_id"]})

    print("\nVenta registrada correctamente.")
    print("Resumen actualizado del producto:")
    mostrar_producto_resumen(producto_actualizado)

    pausar()


# Elimina un producto después de confirmar.

def eliminar_producto():
    print("\n===== ELIMINAR PRODUCTO =====")

    titulo_album = pedir_texto("Ingrese título exacto del álbum: ")
    producto = buscar_producto_por_titulo(titulo_album)

    if producto is None:
        print("Producto no encontrado. No se puede eliminar.")
        pausar()
        return

    print("\nProducto encontrado:")
    mostrar_producto_resumen(producto)

    confirmar = input("¿Está seguro de eliminar este producto? (s/n): ").strip().lower()

    if confirmar == "s":
        coleccion.delete_one({"_id": producto["_id"]})
        print("Producto eliminado correctamente.")
    else:
        print("Eliminación cancelada.")

    pausar()


# Muestra información básica de la base de datos.

def verificar_datos():
    print("\n===== VERIFICAR CONEXIÓN Y DATOS =====")

    cantidad = coleccion.count_documents({})

    print("Base de datos: tienda_musical_db")
    print("Colección: productos_musicales")
    print(f"Cantidad de documentos: {cantidad}")

    if cantidad == 0:
        print("La colección está vacía. Debe ejecutar python cargar_datos.py")
    else:
        print("La base de datos tiene información cargada.")

    pausar()


# Menú principal del sistema.

def mostrar_menu():
    print("\n========================================")
    print("     SISTEMA CRUD - TIENDA MUSICAL")
    print("========================================")
    print("1. Crear producto musical")
    print("2. Listar productos")
    print("3. Ver detalle de producto")
    print("4. Ver ventas de un producto")
    print("5. Buscar por precio")
    print("6. Buscar por título o artista")
    print("7. Buscar por rango de fechas")
    print("8. Buscar por país del sello")
    print("9. Buscar ventas por método de pago")
    print("10. Actualizar precio")
    print("11. Actualizar país del sello")
    print("12. Registrar venta")
    print("13. Eliminar producto")
    print("14. Verificar conexión y datos")
    print("0. Salir")
    print("========================================")


def main():
    while True:
        mostrar_menu()

        opcion = input("Seleccione una opción: ").strip()

        try:
            if opcion == "1":
                crear_producto()
            elif opcion == "2":
                listar_productos()
            elif opcion == "3":
                ver_detalle_producto()
            elif opcion == "4":
                ver_ventas_producto()
            elif opcion == "5":
                buscar_por_precio()
            elif opcion == "6":
                buscar_por_titulo_o_artista()
            elif opcion == "7":
                buscar_por_fecha_lanzamiento()
            elif opcion == "8":
                buscar_por_pais_sello()
            elif opcion == "9":
                buscar_por_metodo_pago()
            elif opcion == "10":
                actualizar_precio()
            elif opcion == "11":
                actualizar_pais_sello()
            elif opcion == "12":
                registrar_venta()
            elif opcion == "13":
                eliminar_producto()
            elif opcion == "14":
                verificar_datos()
            elif opcion == "0":
                print("Saliendo del sistema...")
                break
            else:
                print("Opción no válida.")

        except Exception as error:
            print("\nOcurrió un problema al ejecutar esta opción.")
            print("El sistema no se cerró, pero revise los datos ingresados.")
            print(f"Detalle: {error}")
            pausar()


main()
