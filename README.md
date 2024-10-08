# Tienda_Ropa_POOBootcamp

## Descripción
Este proyecto es una simulación de un sistema de tienda de ropa en línea utilizando los pilares de la Programación Orientada a Objetos (POO). Los usuarios pueden seleccionar productos de diferentes categorías de ropa, agregarlos a un carrito de compras y finalizar la compra obteniendo un total.

## Requisitos del Proyecto
El proyecto fue diseñado para implementar los cuatro pilares de la POO:
- **Encapsulamiento:** Atributos de clase encapsulados usando métodos getter y setter.
- **Herencia:** La clase `Ropa` hereda de `Producto`, mientras que `Camisa`, `Pantalon` y `Zapato` heredan de `Ropa`.
- **Polimorfismo:** Método `mostrar_info` sobrescrito en cada clase hija para mostrar la información específica de cada producto.
- **Abstracción:** Oculta el proceso de compra interno para simplificar la interacción del usuario.

## Clases y Estructura

- **Producto:** Clase base para todos los productos en la tienda.
- **Ropa:** Clase que hereda de `Producto` y añade características comunes de ropa, como `talla` y `tipo de tela`.
- **Camisa, Pantalon, Zapato:** Clases específicas que heredan de `Ropa` y definen atributos adicionales según el tipo de prenda.
- **Carrito:** Clase para almacenar y gestionar los productos seleccionados por el usuario.
- **Tienda:** Clase principal que maneja la interacción del usuario, mostrando productos disponibles y procesando compras.

## Ejecución
Para ejecutar el programa:
```bash
python tienda_ropa.py
