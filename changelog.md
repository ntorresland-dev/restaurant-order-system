# Changelog

All notable changes to this project will be documented in this file.

The format is inspired by [Keep a Changelog](https://keepachangelog.com/) and follows Semantic Versioning.

---

## [1.0.0] - 2026-08-03

### Added

* Implemented the `Product` entity.
* Implemented the `Menu` entity.
* Implemented the `Order` entity.
* Implemented the `OrderManager` entity.
* Added product lookup by name.
* Added automatic order identifier generation.
* Added order registration.
* Added order retrieval.
* Added order lookup by identifier.
* Added order confirmation.
* Added order cancellation.
* Added detailed order visualization using `__str__()`.

### Changed

* Centralized order modification validation to eliminate duplicated business rules.
* Improved naming consistency throughout the project.
* Refined the object model by introducing automatic order identifiers.
* Improved project documentation.

### Documentation

* Added a comprehensive `README.md`.
* Added `design.md` documenting the main design decisions.
* Added project structure, development workflow, and learning objectives.

### Notes

This release marks the completion of the initial project scope.

The project was developed as a learning exercise focused on Object-Oriented Programming, software design, incremental development, and professional Git workflows.
