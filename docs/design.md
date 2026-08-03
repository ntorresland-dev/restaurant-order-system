# Design Decisions

## Project Objective

The objective of this project was to solve a fictional restaurant order management problem aimed at reducing operational and financial errors during the ordering process.

The solution is a command-line application (CLI) written in Python that manages orders entirely in memory without using data persistence. This allowed the project to focus on domain modeling, Object-Oriented Programming, and software engineering best practices.

---

## Domain Model

The system is composed of the following domain entities:

* **Product**
* **Menu**
* **Order**
* **OrderManager**

Each entity has a single, well-defined responsibility to keep the design simple, maintainable, and easy to extend.

---

## Responsibilities

### Product

Represents a product available on the restaurant menu.

Each product stores its name and price and exposes them through read-only properties.

---

### Menu

Represents the restaurant's product catalog.

Its responsibility is to store the available products and provide product lookup by name, hiding its internal implementation from the rest of the system.

---

### Order

Represents a customer's order.

It is responsible for managing its products, calculating the total price, confirming or canceling the order, and enforcing all business rules throughout its lifecycle.

One of these rules is preventing any modification after an order has been confirmed.

---

### OrderManager

Represents the collection of orders managed by the system.

Its responsibility is to register, store, and retrieve orders by their identifier.

---

## Main Design Decisions

The following design decisions were made during development:

* `Menu` receives the collection of products from `main.py` instead of creating them internally.
* `Order` generates its own identifier using a class variable, ensuring every order has a unique ID.
* `OrderManager` returns `Order` objects instead of text representations, allowing the caller to decide how to use or display them.
* `main.py` acts exclusively as the application's orchestrator and contains no business logic.
* Business rules are enforced inside the domain entities rather than in the presentation layer.

---

## Principles Applied

The project was developed following these software design principles:

* Encapsulation
* Single Responsibility Principle (SRP)
* Separation of Responsibilities
* Incremental Development
* Domain-Driven Refactoring
* Exception-Based Business Rule Validation

---

## Future Improvements

The project intentionally keeps a limited scope to focus on Object-Oriented Programming. Possible future improvements include:

* Replace order states with an `Enum`.
* Add data persistence using files or a database.
* Implement unit tests.
* Expose the domain through a REST API.
* Build a graphical or web-based user interface.

---

## Conclusion

This project was designed to practice software development from a domain-oriented perspective, prioritizing design before implementation.

In addition to strengthening Object-Oriented Programming skills in Python, the project followed a workflow inspired by professional software development, including Git branching, descriptive commits, code reviews, and incremental refactoring.
