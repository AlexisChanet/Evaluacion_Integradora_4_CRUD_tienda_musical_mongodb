class ProductoMusical:
    # Constructor de la clase.
    # Recibe los datos principales de un producto musical.
    def __init__(self, titulo_album, artista, genero, formato, precio,
                 stock, fecha_lanzamiento, sello_discografico, ventas):

        self.titulo_album = titulo_album
        self.artista = artista
        self.genero = genero
        self.formato = formato
        self.precio = precio
        self.stock = stock
        self.fecha_lanzamiento = fecha_lanzamiento
        self.sello_discografico = sello_discografico
        self.ventas = ventas

    # Método que transforma el objeto en un diccionario.
    # Este diccionario será insertado como documento en MongoDB.
    def crear_documento(self):
        return {
            "titulo_album": self.titulo_album,
            "artista": self.artista,
            "genero": self.genero,
            "formato": self.formato,
            "precio": self.precio,
            "stock": self.stock,
            "fecha_lanzamiento": self.fecha_lanzamiento,
            "sello_discografico": self.sello_discografico,
            "ventas": self.ventas
        }