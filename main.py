class Prenda:
    def __init__(self, nombre, precio, cantidad):
        self._nombre = nombre
        self._precio = precio
        self._cantidad = cantidad

    def get_nombre(self):
        return self._nombre

    def get_precio(self):
        return self._precio

    def get_cantidad(self):
        return self._cantidad

    def set_precio(self, nuevo_precio):
        if nuevo_precio > 0:
            self._precio = nuevo_precio
        else:
            print("El precio debe ser mayor a 0")

    def mostrar_info(self):
        raise NotImplementedError("Este método debe ser sobrescrito en las clases hijas")

class RopaHombre(Prenda):
    def __init__(self, nombre, precio, cantidad, talla):
        super().__init__(nombre, precio, cantidad)
        self._talla = talla

    def mostrar_info(self):
        return f"Prenda: {self.get_nombre()}, Precio: {self.get_precio()}, Cantidad: {self.get_cantidad()}, Talla: {self._talla}"

class RopaMujer(Prenda):
    def __init__(self, nombre, precio, cantidad, talla):
        super().__init__(nombre, precio, cantidad)
        self._talla = talla

    def mostrar_info(self):
        return f"Prenda: {self.get_nombre()}, Precio: {self.get_precio()}, Cantidad: {self.get_cantidad()}, Talla: {self._talla}"

class Categoria:
    def __init__(self, nombre):
        self._nombre = nombre
        self._prendas = []

    def agregar_prenda(self, prenda):
        self._prendas.append(prenda)

    def mostrar_prendas(self):
        print(f"\n--- Categoría: {self._nombre} ---")
        for idx, prenda in enumerate(self._prendas, start=1):
            print(f"{idx}. {prenda.mostrar_info()}")

    def obtener_prenda(self, indice):
        if 0 <= indice < len(self._prendas):
            return self._prendas[indice]
        return None

    def get_nombre(self):
        return self._nombre

class Tienda:
    def __init__(self):
        self._categorias = []
        self._carrito = []

    def agregar_categoria(self, categoria):
        self._categorias.append(categoria)

    def mostrar_categorias(self):
        for idx, categoria in enumerate(self._categorias, start=1):
            print(f"{idx}. {categoria.get_nombre()}")

    def seleccionar_categoria(self, indice):
        if 0 <= indice < len(self._categorias):
            return self._categorias[indice]
        return None

    def agregar_al_carrito(self, prenda):
        self._carrito.append(prenda)

    def mostrar_carrito(self):
        if not self._carrito:
            print("El carrito está vacío.")
        else:
            for prenda in self._carrito:
                print(prenda.mostrar_info())

    def procesar_compra(self):
        if not self._carrito:
            print("El carrito está vacío. No hay nada para comprar.")
        else:
            total = sum(prenda.get_precio() for prenda in self._carrito)
            print(f"El total de la compra es: {total:.2f}")
            self._carrito.clear()
            print("Compra procesada. ¡Gracias por su compra!")

if __name__ == "__main__":
    ropa_hombre = Categoria("Ropa de Hombre")
    ropa_mujer = Categoria("Ropa de Mujer")

    ropa_hombre.agregar_prenda(RopaHombre("Camisa de Hombre", 25.00, 50, "M"))
    ropa_hombre.agregar_prenda(RopaHombre("Pantalón de Hombre", 35.00, 30, "L"))
    
    ropa_mujer.agregar_prenda(RopaMujer("Falda de Mujer", 28.00, 15, "S"))
    ropa_mujer.agregar_prenda(RopaMujer("Zapatos de Mujer", 50.00, 20, "38"))

    tienda = Tienda()
    tienda.agregar_categoria(ropa_hombre)
    tienda.agregar_categoria(ropa_mujer)

    while True:
        print("\n--- Sistema de Compra de Ropa ---")
        print("1. Ver Categorías")
        print("2. Agregar Prenda al Carrito")
        print("3. Ver Carrito")
        print("4. Procesar Compra")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("\n--- Categorías ---")
            tienda.mostrar_categorias()

        elif opcion == "2":
            print("\n--- Selección de Categoría ---")
            tienda.mostrar_categorias()
            cat_idx = int(input("Seleccione el número de la categoría: ")) - 1
            categoria = tienda.seleccionar_categoria(cat_idx)
            if categoria:
                categoria.mostrar_prendas()
                prenda_idx = int(input("Seleccione el número de la prenda para agregar al carrito: ")) - 1
                prenda = categoria.obtener_prenda(prenda_idx)
                if prenda:
                    tienda.agregar_al_carrito(prenda)
                    print(f"{prenda.get_nombre()} ha sido agregado al carrito.")
                else:
                    print("Selección de prenda inválida.")
            else:
                print("Selección de categoría inválida.")

        elif opcion == "3":
            print("\n--- Carrito de Compras ---")
            tienda.mostrar_carrito()

        elif opcion == "4":
            print("\n--- Procesar Compra ---")
            tienda.procesar_compra()

        elif opcion == "5":
            print("Gracias por visitar la tienda. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Por favor, elija nuevamente.")