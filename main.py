class Prenda:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def mostrar_info(self):
        raise NotImplementedError("Este método debe ser sobrescrito en las clases hijas")

class RopaHombre(Prenda):
    def __init__(self, nombre, precio, cantidad, talla):
        super().__init__(nombre, precio, cantidad)
        self.talla = talla

    def mostrar_info(self):
        return f"Prenda: {self.nombre}, Precio: {self.precio}, Cantidad: {self.cantidad}, Talla: {self.talla}"

class RopaMujer(Prenda):
    def __init__(self, nombre, precio, cantidad, talla):
        super().__init__(nombre, precio, cantidad)
        self.talla = talla
        
    def mostrar_info(self):
        return f"Prenda: {self.nombre}, Precio: {self.precio}, Cantidad: {self.cantidad}, Talla: {self.talla}"

class Inventario:
    def __init__(self):
        self.prendas = []

    def agregar_prenda(self, prenda):
        self.prendas.append(prenda)

    def mostrar_inventario(self):
        for prenda in self.prendas:
            print(prenda.mostrar_info())

if __name__ == "__main__":
    camisa = RopaHombre("Camisa de Hombre", 25.00, 50, "M")
    falda = RopaMujer("Falda de Mujer", 28.00, 15, "S")
    inventario = Inventario()
    inventario.agregar_prenda(camisa)
    inventario.agregar_prenda(falda)
    inventario.mostrar_inventario()