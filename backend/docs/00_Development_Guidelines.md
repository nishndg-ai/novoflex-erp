# NOVOFLEX Platform Development Guidelines

Version: 1.0

---

## Vision

NOVOFLEX is a configurable Manufacturing ERP Platform built for Plastic Injection Moulding industries.

The platform consists of:

* Platform
* Studio
* ERP
* AI

---

# Core Principles

## 1. Configuration over Coding

Every possible functionality should be configurable using metadata rather than hardcoded.

---

## 2. Excel First

All masters, checksheets, templates and configurations should support:

* Download Template
* Excel Upload
* Validation
* Version Control

---

## 3. Dynamic UI

No repetitive CRUD pages.

The Runtime Engine must generate:

* Forms
* Grids
* Reports
* Dashboards

from Metadata.

---

## 4. AI Ready

Every module should be understandable by AI.

---

## Folder Structure

backend/

* core
* platform
* studio
* erp
* integrations
* common

frontend/

* platform
* studio
* erp
* ai
* shared

---

## Backend Standards

* One model per file
* One schema per file
* One router per module
* One service per module
* Repository pattern
* Type hints mandatory
* Pydantic validation mandatory

---

## Frontend Standards

* Functional Components
* TypeScript only
* Material UI
* No inline styles
* Common reusable components

---

## Database Standards

* Alembic only
* No create_all()
* Soft Delete
* Audit Fields
* Version Number

---

## API Standards

Every module should support:

GET

GET BY ID

POST

PUT

DELETE

IMPORT

EXPORT

DOWNLOAD TEMPLATE

---

## Naming Convention

Database

snake_case

Python

snake_case

Class

PascalCase

React

PascalCase

Routes

lowercase

---

## Git Workflow

main

↓

develop

↓

feature branches

---

## Documentation First

Every major feature must be documented before implementation.

---

## Long Term Goal

Build a configurable manufacturing platform capable of generating ERP modules dynamically with minimal coding.
