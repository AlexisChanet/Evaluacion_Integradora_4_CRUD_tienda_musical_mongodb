from datetime import datetime
from db import coleccion
from producto_musical import ProductoMusical


# Productos iniciales para cargar en MongoDB.
# Cada producto tiene un sello discográfico y una lista de ventas.
productos = [
    ProductoMusical(
        "Alta Suciedad",
        "Andrés Calamaro",
        "Rock en español",
        "CD",
        14990,
        10,
        datetime(1997, 9, 9),
        {
            "nombre": "Warner Music",
            "pais": "Argentina"
        },
        [
            {
                "cliente": {
                    "nombre": "Carlos",
                    "apellido": "Muñoz",
                    "rut": "12.345.678-9"
                },
                "cantidad": 1,
                "fecha_venta": datetime(2026, 5, 12),
                "metodo_pago": "Débito",
                "total": 14990
            }
        ]
    ),

    ProductoMusical(
        "Odio",
        "Planeta No",
        "Pop chileno",
        "Vinilo",
        19990,
        7,
        datetime(2015, 8, 28),
        {
            "nombre": "Sello Azul",
            "pais": "Chile"
        },
        [
            {
                "cliente": {
                    "nombre": "Javiera",
                    "apellido": "Soto",
                    "rut": "18.456.789-2"
                },
                "cantidad": 1,
                "fecha_venta": datetime(2026, 5, 10),
                "metodo_pago": "Transferencia",
                "total": 19990
            }
        ]
    ),

    ProductoMusical(
        "Songs from the Big Chair",
        "Tears for Fears",
        "New Wave",
        "CD",
        15990,
        12,
        datetime(1985, 2, 25),
        {
            "nombre": "Mercury Records",
            "pais": "Reino Unido"
        },
        [
            {
                "cliente": {
                    "nombre": "Felipe",
                    "apellido": "Rojas",
                    "rut": "16.222.333-4"
                },
                "cantidad": 2,
                "fecha_venta": datetime(2026, 5, 9),
                "metodo_pago": "Crédito",
                "total": 31980
            }
        ]
    ),

    ProductoMusical(
        "Bailar y Llorar",
        "Teleradio Donoso",
        "Indie rock",
        "CD",
        12990,
        8,
        datetime(2008, 1, 1),
        {
            "nombre": "Sello Independiente",
            "pais": "Chile"
        },
        [
            {
                "cliente": {
                    "nombre": "Camila",
                    "apellido": "Torres",
                    "rut": "19.333.444-5"
                },
                "cantidad": 1,
                "fecha_venta": datetime(2026, 5, 8),
                "metodo_pago": "Efectivo",
                "total": 12990
            }
        ]
    ),

    ProductoMusical(
        "Bad",
        "Michael Jackson",
        "Pop",
        "Vinilo",
        24990,
        15,
        datetime(1987, 8, 31),
        {
            "nombre": "Epic Records",
            "pais": "Estados Unidos"
        },
        [
            {
                "cliente": {
                    "nombre": "Diego",
                    "apellido": "Herrera",
                    "rut": "17.555.666-7"
                },
                "cantidad": 1,
                "fecha_venta": datetime(2026, 5, 6),
                "metodo_pago": "Débito",
                "total": 24990
            }
        ]
    ),

    ProductoMusical(
        "I Am",
        "Earth, Wind & Fire",
        "Funk",
        "Vinilo",
        22990,
        9,
        datetime(1979, 6, 9),
        {
            "nombre": "Columbia Records",
            "pais": "Estados Unidos"
        },
        [
            {
                "cliente": {
                    "nombre": "Sebastián",
                    "apellido": "Vega",
                    "rut": "15.777.888-9"
                },
                "cantidad": 1,
                "fecha_venta": datetime(2026, 5, 4),
                "metodo_pago": "Crédito",
                "total": 22990
            }
        ]
    ),

    ProductoMusical(
        "Something Special",
        "Kool & The Gang",
        "Funk",
        "CD",
        16990,
        11,
        datetime(1981, 9, 24),
        {
            "nombre": "De-Lite Records",
            "pais": "Estados Unidos"
        },
        [
            {
                "cliente": {
                    "nombre": "Valentina",
                    "apellido": "Pérez",
                    "rut": "20.111.222-3"
                },
                "cantidad": 2,
                "fecha_venta": datetime(2026, 5, 2),
                "metodo_pago": "Transferencia",
                "total": 33980
            }
        ]
    ),

    ProductoMusical(
        "Random Access Memories",
        "Daft Punk",
        "Electrónica",
        "Vinilo",
        29990,
        6,
        datetime(2013, 5, 17),
        {
            "nombre": "Columbia Records",
            "pais": "Estados Unidos"
        },
        [
            {
                "cliente": {
                    "nombre": "María",
                    "apellido": "González",
                    "rut": "21.333.444-5"
                },
                "cantidad": 1,
                "fecha_venta": datetime(2026, 4, 30),
                "metodo_pago": "Débito",
                "total": 29990
            }
        ]
    )
]


# Se convierten los objetos ProductoMusical en documentos para MongoDB.
documentos = []

for producto in productos:
    documentos.append(producto.crear_documento())


# Se limpia la colección para evitar duplicados al volver a ejecutar el archivo.
coleccion.delete_many({})

# Se insertan los 8 productos musicales iniciales.
coleccion.insert_many(documentos)

print("Datos iniciales cargados correctamente.")
print("Se insertaron 8 productos musicales en MongoDB.")