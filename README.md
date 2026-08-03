# Restaurant Order System

## Description

Restaurant Order System is a Python console application that simulates the order management process of a small restaurant.

The project was developed using an incremental approach to practice Object-Oriented Programming (OOP) while following a workflow similar to that of a professional software development team.

The application intentionally stores all data in memory without persistence, allowing the focus to remain on domain modeling, object collaboration, and software design principles.

---

## Project Goals

* Practice Object-Oriented Programming in Python.
* Apply encapsulation and the Single Responsibility Principle.
* Design the domain before implementing features.
* Simulate a professional Git and GitHub workflow.
* Develop features through small, incremental changes reviewed as Pull Requests.

---

## Features

The current version allows you to:

* Create products.
* Manage a product menu.
* Create orders.
* Add products to an order.
* Calculate the total price of an order.
* Confirm orders.
* Cancel orders.
* Search for an order by its identifier.
* Manage multiple orders through `OrderManager`.
* Display detailed order information.

---

## Project Structure

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

## Concepts Applied

This project was built while practicing the following concepts:

* Object-Oriented Programming
* Encapsulation
* Single Responsibility Principle (SRP)
* Object Aggregation
* Instance and Class Attributes
* Properties (`@property`)
* Special Methods (`__str__`)
* Exception Handling
* Domain-Driven Refactoring
* Incremental Software Design

---

## Technologies

* Python 3
* Git
* GitHub

No external frameworks or third-party libraries were used.

---

## Running the Project

From the project root directory:

```bash
python3 main.py
```

---

## Development Workflow

The project was developed through small incremental iterations.

Each feature followed a workflow similar to a professional development process:

1. Analyze the requirement.
2. Define the scope.
3. Design the solution.
4. Implement the feature.
5. Perform a code review.
6. Refactor when necessary.
7. Merge into the main branch.

---

## What I Learned

This project helped strengthen my understanding of:

* Requirements analysis.
* Object-oriented design.
* Domain modeling.
* Defining class responsibilities.
* Incremental software development.
* Git workflows using branches, commits, and code reviews.
* Refactoring without changing system behavior.

---

## Project Status

**Version 1.0.0**

This project is considered complete within its original scope and serves as a learning project focused on Object-Oriented Programming and software design.
