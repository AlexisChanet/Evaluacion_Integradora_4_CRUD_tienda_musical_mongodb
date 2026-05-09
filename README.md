# Evaluacion_Integradora_4_CRUD_tienda_musical_mongodb
Desarrollo de sistema CRUD de tienda musical con MongoDB y Python. 

# Sistema CRUD Tienda Musical

Proyecto desarrollado en Python con PyMongo y MongoDB local.

## Caso de estudio

El sistema permite administrar productos musicales de una tienda, como CDs y vinilos. Cada producto tiene información del álbum, artista, género, formato, precio, stock, fecha de lanzamiento, sello discográfico y ventas asociadas.

## Base de datos

- Base de datos: `tienda_musical_db`
- Colección: `productos_musicales`

## Estructura del proyecto

- `db.py`: conexión con MongoDB.
- `producto_musical.py`: clase ProductoMusical.
- `cargar_datos.py`: carga los 8 productos iniciales.
- `main.py`: menú principal del CRUD.
- `requirements.txt`: librerías necesarias.
- `datos_entrega.txt`: URL del repositorio y rama utilizada.

## Cómo ejecutar

1. Instalar dependencias:

```bash
pip install -r requirements.txt
