# Restaurant Order System

## Descripción

Restaurant Order System es una aplicación de consola desarrollada en Python que simula la gestión de pedidos de un local de comida.

El proyecto fue desarrollado con un enfoque incremental para practicar Programación Orientada a Objetos (POO) y un flujo de trabajo similar al utilizado en equipos de desarrollo profesionales.

Su alcance está limitado a una aplicación en memoria, sin persistencia de datos, permitiendo concentrarse en el diseño del dominio, la colaboración entre objetos y las buenas prácticas de desarrollo.

---

## Objetivos del proyecto

* Practicar Programación Orientada a Objetos en Python.
* Aplicar principios de encapsulamiento y responsabilidad única.
* Diseñar un dominio simple antes de implementar funcionalidades.
* Simular un flujo de trabajo profesional utilizando Git y GitHub.
* Desarrollar funcionalidades mediante pequeños incrementos revisados como Pull Requests.

---

## Funcionalidades

Actualmente el sistema permite:

* Crear productos.
* Administrar un menú de productos.
* Crear pedidos.
* Agregar productos a un pedido.
* Calcular el precio total.
* Confirmar pedidos.
* Cancelar pedidos.
* Consultar un pedido por su identificador.
* Administrar múltiples pedidos mediante `OrderManager`.
* Mostrar el detalle completo de un pedido.

---

## Estructura del proyecto

```text
.
├── .gitignore
├── README.md
├── main.py
└── src
    ├── menu.py
    ├── order.py
    ├── order_manager.py
    └── product.py
```

---

## Conceptos aplicados

Durante el desarrollo se practicaron los siguientes conceptos:

* Programación Orientada a Objetos.
* Encapsulamiento.
* Responsabilidad Única (SRP).
* Agregación entre objetos.
* Variables de instancia y de clase.
* Propiedades (`@property`).
* Métodos especiales (`__str__`).
* Validaciones mediante excepciones.
* Refactorización orientada al dominio.
* Diseño incremental basado en reglas de negocio.

---

## Tecnologías

* Python 3
* Git
* GitHub

No se utilizan frameworks ni librerías externas.

---

## Cómo ejecutar

Desde la raíz del proyecto:

```bash
python3 main.py
```

---

## Flujo de desarrollo

El proyecto fue construido mediante pequeños incrementos.

Cada funcionalidad fue desarrollada siguiendo un flujo similar al utilizado en equipos profesionales:

1. Análisis del requerimiento.
2. Definición del alcance.
3. Diseño de la solución.
4. Implementación.
5. Revisión del código.
6. Refactorización cuando fue necesaria.
7. Integración en la rama principal.

---

## Aprendizajes

Este proyecto permitió fortalecer habilidades en:

* Análisis de requerimientos.
* Diseño orientado a objetos.
* Modelado de entidades del dominio.
* Definición de responsabilidades.
* Evolución incremental de un proyecto.
* Uso de Git mediante ramas, commits y revisiones de código.
* Refactorización sin modificar el comportamiento del sistema.

---

## Estado del proyecto

Versión candidata a **v1.0.0**.
