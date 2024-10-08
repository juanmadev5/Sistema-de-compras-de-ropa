class Producto:
    def __init__(self, nombre, precio):
        self._nombre = nombre
        self._precio = precio

    def get_nombre(self):
        return self._nombre

    def get_precio(self):
        return self._precio

    def mostrar_info(self):
        raise NotImplementedError("Este método debe ser sobrescrito en las clases hijas")

class Ropa(Producto):
    def __init__(self, nombre, precio, talla, tipo_tela):
        super().__init__(nombre, precio)
        self._talla = talla
        self._tipo_tela = tipo_tela

    def get_talla(self):
        return self._talla

    def get_tipo_tela(self):
        return self._tipo_tela

    def mostrar_info(self):
        return f"{self.get_nombre()} - Precio: {self.get_precio()}, Talla: {self._talla}, Tela: {self._tipo_tela}"

class Camisa(Ropa):
    def __init__(self, nombre, precio, talla, tipo_tela, tipo_cuello):
        super().__init__(nombre, precio, talla, tipo_tela)
        self._tipo_cuello = tipo_cuello

    def mostrar_info(self):
        return f"Camisa: {self.get_nombre()} - Precio: {self.get_precio()}, Talla: {self._talla}, Tela: {self._tipo_tela}, Cuello: {self._tipo_cuello}"

class Pantalon(Ropa):
    def __init__(self, nombre, precio, talla, tipo_tela, tipo_corte):
        super().__init__(nombre, precio, talla, tipo_tela)
        self._tipo_corte = tipo_corte

    def mostrar_info(self):
        return f"Pantalón: {self.get_nombre()} - Precio: {self.get_precio()}, Talla: {self._talla}, Tela: {self._tipo_tela}, Corte: {self._tipo_corte}"

class Zapato(Ropa):
    def __init__(self, nombre, precio, talla, tipo_material):
        super().__init__(nombre, precio, talla, tipo_material)
        self._tipo_material = tipo_material

    def mostrar_info(self):
        return f"Zapato: {self.get_nombre()} - Precio: {self.get_precio()}, Talla: {self._talla}, Material: {self._tipo_material}"

class Carrito:
    def __init__(self):
        self._productos = []

    def agregar_producto(self, producto):
        self._productos.append(producto)

    def mostrar_carrito(self):
        if not self._productos:
            print("El carrito está vacío.")
        else:
            print("\n--- Carrito de Compras ---")
            for producto in self._productos:
                print(producto.mostrar_info())

    def calcular_total(self):
        return sum(producto.get_precio() for producto in self._productos)

class Tienda:
    def __init__(self):
        self._productos_disponibles = []
        self._carrito = Carrito()

    def agregar_producto_disponible(self, producto):
        self._productos_disponibles.append(producto)

    def mostrar_productos_disponibles(self):
        print("\n--- Productos Disponibles ---")
        for idx, producto in enumerate(self._productos_disponibles, start=1):
            print(f"{idx}. {producto.mostrar_info()}")

    def seleccionar_producto(self, indice):
        if 0 <= indice < len(self._productos_disponibles):
            producto = self._productos_disponibles[indice]
            self._carrito.agregar_producto(producto)
            print(f"{producto.get_nombre()} ha sido agregado al carrito.")
        else:
            print("Selección inválida.")

    def mostrar_carrito(self):
        self._carrito.mostrar_carrito()

    def procesar_compra(self):
        total = self._carrito.calcular_total()
        print(f"\nEl total de la compra es: {total:.2f}")
        print("Compra procesada. ¡Gracias por su compra!")
        self._carrito = Carrito()

if __name__ == "__main__":
    tienda = Tienda()
    tienda.agregar_producto_disponible(Camisa("Camisa Casual", 25.00, "M", "Algodón", "Cuello Redondo"))
    tienda.agregar_producto_disponible(Pantalon("Pantalón Jeans", 40.00, "L", "Denim", "Slim Fit"))
    tienda.agregar_producto_disponible(Zapato("Zapatos de Cuero", 60.00, "42", "Cuero"))
    tienda.agregar_producto_disponible(Camisa("Camisa de Rayas", 30.00, "L", "Poliéster", "Cuello Mao"))
    tienda.agregar_producto_disponible(Camisa("Camisa Formal", 50.00, "S", "Algodón", "Cuello Clásico"))
    tienda.agregar_producto_disponible(Pantalon("Pantalón Corto", 35.00, "M", "Lino", "Regular Fit"))
    tienda.agregar_producto_disponible(Pantalon("Pantalón Chino", 45.00, "M", "Algodón", "Regular Fit"))
    tienda.agregar_producto_disponible(Zapato("Zapatos Deportivos", 55.00, "41", "Sintético"))
    tienda.agregar_producto_disponible(Zapato("Botas de Invierno", 80.00, "43", "Cuero"))
    tienda.agregar_producto_disponible(Zapato("Sandalias", 25.00, "40", "Plástico"))

    while True:
        print("\n--- Menú Principal ---")
        print("1. Ver Productos Disponibles")
        print("2. Agregar Producto al Carrito")
        print("3. Ver Carrito")
        print("4. Procesar Compra")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            tienda.mostrar_productos_disponibles()

        elif opcion == "2":
            tienda.mostrar_productos_disponibles()
            indice = int(input("Seleccione el número del producto que desea agregar al carrito: ")) - 1
            tienda.seleccionar_producto(indice)

        elif opcion == "3":
            tienda.mostrar_carrito()

        elif opcion == "4":
            tienda.procesar_compra()

        elif opcion == "5":
            print("Gracias por visitar la tienda. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Por favor, elija nuevamente.")
