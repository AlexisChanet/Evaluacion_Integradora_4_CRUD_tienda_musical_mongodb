# Sistema CRUD Tienda Musical

Proyecto desarrollado en Python con PyMongo y MongoDB local para la Evaluación Integradora N°4 de Bases de Datos No Estructuradas.

## Caso de estudio

El sistema corresponde a una tienda musical que administra productos como CDs y vinilos.

Cada producto musical permite registrar información como:

- título del álbum;
- artista;
- género;
- formato;
- precio;
- stock;
- fecha de lanzamiento;
- sello discográfico;
- ventas asociadas.

## Tecnologías utilizadas

- Python 3
- PyMongo
- MongoDB Community Server
- MongoDB Compass
- GitHub

## Base de datos

- Base de datos: `tienda_musical_db`
- Colección: `productos_musicales`

## Modelo de datos

Cada documento representa un producto musical.

El documento contiene:

- campos simples: `titulo_album`, `artista`, `genero`, `formato`, `precio`, `stock`;
- campo fecha: `fecha_lanzamiento`;
- subdocumento: `sello_discografico`;
- array de subdocumentos: `ventas`;
- subdocumento dentro del array: `cliente`;
- fecha dentro del array: `fecha_venta`.

## Cumplimiento de funcionalidades requeridas

El sistema cumple las funcionalidades solicitadas en la evaluación mediante el menú de consola en Python.

### 1. Crear documento

**Requisito:** Crear un documento nuevo con todos los campos, incluyendo subdocumento, array de subdocumentos y fecha.

**Cómo se cumple:**  
La opción **1. Crear producto musical** permite registrar un producto con datos principales, fecha de lanzamiento, sello discográfico y ventas.

Campos utilizados:

- Datos principales: `titulo_album`, `artista`, `genero`, `formato`, `precio`, `stock`
- Fecha: `fecha_lanzamiento`
- Subdocumento: `sello_discografico`
- Array de subdocumentos: `ventas`
- Subdocumento dentro del array: `cliente`

---

### 2. Listar documentos

**Requisito:** Listar todos los documentos de la colección.

**Cómo se cumple:**  
La opción **2. Listar productos** muestra los productos registrados en la colección `productos_musicales`.

Además, se aplica proyección para mostrar solo campos relevantes:

- `titulo_album`
- `artista`
- `formato`
- `precio`
- `stock`

---

### 3. Buscar con operador de comparación

**Requisito:** Buscar por campo simple usando operadores como `$gt`, `$lt`, `$gte` o `$lte`.

**Cómo se cumple:**  
La opción **5. Buscar por precio** permite buscar productos usando:

- `$gt`: productos con precio mayor que un valor ingresado.
- `$lt`: productos con precio menor que un valor ingresado.

---

### 4. Buscar con expresión regular

**Requisito:** Buscar usando `$regex` sobre un campo de texto.

**Cómo se cumple:**  
La opción **6. Buscar por título o artista** permite buscar coincidencias de texto en:

- `titulo_album`
- `artista`

Se utiliza `$regex` con búsqueda sin distinguir mayúsculas y minúsculas.

---

### 5. Buscar por rango de fechas

**Requisito:** Buscar documentos dentro de un rango de fechas.

**Cómo se cumple:**  
La opción **7. Buscar por rango de fechas** permite buscar productos según `fecha_lanzamiento`.

Se usan los operadores:

- `$gte`: fecha mayor o igual.
- `$lte`: fecha menor o igual.

---

### 6. Buscar dentro de subdocumentos y arrays

**Requisito:** Buscar dentro de un subdocumento o dentro de un array de subdocumentos.

**Cómo se cumple:**

- La opción **8. Buscar por país del sello** busca dentro del subdocumento `sello_discografico`.
- La opción **9. Buscar ventas por método de pago** busca dentro del array `ventas` usando `$elemMatch`.

---

### 7. Actualizar campo raíz

**Requisito:** Actualizar un campo del documento principal.

**Cómo se cumple:**  
La opción **10. Actualizar precio** modifica el campo `precio` del producto musical usando `$set`.

---

### 8. Actualizar subdocumento o array

**Requisito:** Actualizar un campo dentro de un subdocumento o array de subdocumentos.

**Cómo se cumple:**

- La opción **11. Actualizar país del sello** modifica `sello_discografico.pais`.
- La opción **12. Registrar venta** agrega una nueva venta al array `ventas` usando `$push`.

---

### 9. Eliminar documento

**Requisito:** Eliminar un documento usando una condición específica.

**Cómo se cumple:**  
La opción **13. Eliminar producto** elimina un producto musical según el título ingresado y solicita confirmación antes de borrar.

## Archivos del proyecto

- `db.py`: contiene la conexión con MongoDB local.
- `producto_musical.py`: contiene la clase `ProductoMusical`.
- `cargar_datos.py`: carga los 8 productos iniciales en MongoDB.
- `main.py`: contiene el menú principal y las operaciones CRUD.
- `requirements.txt`: contiene la dependencia `pymongo`.
- `datos_entrega.txt`: contiene la URL del repositorio y la rama utilizada.

## Instalación y ejecución

Para ejecutar el proyecto se deben tener instalados Python, MongoDB Community Server y MongoDB Compass.

### 1. Clonar el repositorio

```bash
git clone URL_DEL_REPOSITORIO
```

### 2. Entrar a la carpeta del proyecto

```bash
cd Evaluacion_Integradora_4_CRUD_tienda_musical_mongodb
```

### 3. Instalar PyMongo

```bash
pip install -r requirements.txt
```

### 4. Abrir MongoDB

Abrir MongoDB Compass y conectarse a:

```txt
mongodb://localhost:27017
```

### 5. Cargar los datos iniciales

```bash
python cargar_datos.py
```

Este comando carga los 8 productos musicales iniciales en la base de datos.

### 6. Ejecutar el sistema

```bash
python main.py
```

Al ejecutar este archivo se muestra el menú principal del CRUD en la consola.

Si el comando `python` no funciona, se puede probar usando:

```bash
py cargar_datos.py
py main.py
```

## Funcionalidades del menú

El menú del sistema permite:

1. Crear producto musical.
2. Listar productos.
3. Ver detalle de producto.
4. Ver ventas de un producto.
5. Buscar por precio.
6. Buscar por título o artista.
7. Buscar por rango de fechas.
8. Buscar por país del sello.
9. Buscar ventas por método de pago.
10. Actualizar precio.
11. Actualizar país del sello.
12. Registrar venta.
13. Eliminar producto.
14. Verificar conexión y datos.

## Consultas implementadas

El sistema incluye:

- listado de productos usando proyección;
- búsqueda por precio usando `$gt` y `$lt`;
- búsqueda por título o artista usando `$regex`;
- búsqueda por rango de fechas usando `$gte` y `$lte`;
- búsqueda dentro del subdocumento `sello_discografico`;
- búsqueda dentro del array `ventas` usando `$elemMatch`;
- actualización de campo raíz con `$set`;
- actualización de subdocumento con `$set`;
- inserción en array con `$push`;
- eliminación con condición usando `delete_one()`.

## Consideraciones

Antes de ejecutar `main.py`, se recomienda ejecutar:

```bash
python cargar_datos.py
```

Esto asegura que la base de datos tenga los 8 productos iniciales.

Para verificar que la conexión y los datos estén correctos, usar la opción:

```txt
14. Verificar conexión y datos
```

## Entrega

El archivo `datos_entrega.txt` debe contener:

```txt
URL del repositorio:
https://github.com/TU-USUARIO/Evaluacion_Integradora_4_CRUD_tienda_musical_mongodb

Rama utilizada:
main
```