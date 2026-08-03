# Design Decisions

## Objetivo del proyecto

El objetivo de este proyecto fue resolver un caso ficticio de gestión de pedidos para un local de comida, con el propósito de reducir errores logísticos y financieros durante el proceso de atención.

La solución consiste en una aplicación de consola (CLI) desarrollada en Python, que permite administrar pedidos completamente en memoria, sin utilizar persistencia de datos. Esto permitió enfocar el desarrollo en el diseño del dominio, la Programación Orientada a Objetos y las buenas prácticas de ingeniería de software.

---

## Modelo del dominio

El dominio del sistema está compuesto por las siguientes entidades:

* **Product**
* **Menu**
* **Order**
* **OrderManager**

Cada una posee una responsabilidad claramente definida para mantener un diseño simple, desacoplado y fácil de mantener.

---

## Responsabilidades

### Product

Representa un producto disponible en el menú del restaurante.

Cada producto posee un nombre y un precio, y es responsable de exponer únicamente la información necesaria mediante propiedades de solo lectura.

---

### Menu

Representa el catálogo de productos disponibles.

Su responsabilidad consiste en almacenar los productos del restaurante y permitir su consulta por nombre, evitando que otras clases conozcan cómo se gestionan internamente.

---

### Order

Representa un pedido realizado por un cliente.

Es responsable de administrar los productos que contiene, calcular el precio total, confirmar o cancelar el pedido y garantizar que las reglas de negocio se cumplan durante todo su ciclo de vida.

Entre dichas reglas se encuentra impedir cualquier modificación una vez que el pedido ha sido confirmado.

---

### OrderManager

Representa el conjunto de pedidos registrados por el sistema.

Su responsabilidad consiste en almacenar los pedidos, registrarlos y permitir su consulta mediante su identificador.

---

## Principales decisiones de diseño

Durante el desarrollo del proyecto se tomaron las siguientes decisiones:

* `Menu` recibe la colección de productos desde `main.py`, evitando que la clase sea responsable de crearlos.
* `Order` genera automáticamente su propio identificador mediante una variable de clase, garantizando que cada pedido posea un ID único.
* `OrderManager` devuelve objetos `Order` en lugar de representaciones en texto, permitiendo que otras partes del sistema decidan cómo utilizar cada pedido.
* `main.py` actúa únicamente como orquestador de la aplicación, coordinando la interacción entre las entidades sin contener lógica de negocio.
* Las reglas de negocio se implementan dentro de las entidades responsables y no en la capa de presentación.

---

## Principios aplicados

Durante el desarrollo se aplicaron los siguientes principios y buenas prácticas:

* Encapsulamiento.
* Responsabilidad Única (Single Responsibility Principle).
* Separación de responsabilidades.
* Desarrollo incremental mediante pequeños cambios.
* Refactorización guiada por las reglas del dominio.
* Uso de excepciones para comunicar errores de negocio.

---

## Posibles mejoras futuras

Este proyecto fue desarrollado con un alcance intencionalmente reducido para practicar Programación Orientada a Objetos. Algunas mejoras que podrían incorporarse en versiones futuras son:

* Reemplazar los estados del pedido por un `Enum`.
* Incorporar persistencia de datos mediante archivos o una base de datos.
* Agregar pruebas unitarias para validar el comportamiento de las entidades.
* Exponer la lógica del dominio mediante una API REST.
* Incorporar una interfaz gráfica o una interfaz web como capa de presentación.

---

## Conclusión

Este proyecto permitió practicar el desarrollo de software desde una perspectiva orientada al dominio, priorizando el diseño antes que la implementación.

Además de reforzar conceptos de Programación Orientada a Objetos en Python, el desarrollo se realizó siguiendo un flujo de trabajo similar al de un entorno profesional, utilizando Git, ramas por funcionalidad, commits descriptivos, revisiones de código y refactorizaciones incrementales.
