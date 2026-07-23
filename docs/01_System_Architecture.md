# NOVOFLEX ERP System Architecture

## Version

1.0

## Objective

NOVOFLEX ERP is a configurable manufacturing ERP platform designed specifically for Plastic Injection Moulding Industries.

Unlike traditional ERP systems where every master, transaction and check sheet is developed manually, NOVOFLEX uses a metadata-driven architecture.

The ERP automatically generates screens, validations, reports, dashboards and workflows from uploaded templates.

---

# Design Principles

## 1. Configuration Before Coding

Every business requirement should first be evaluated to determine whether it can be solved through configuration.

Coding should be the last option.

---

## 2. Excel Driven ERP

Masters

Check Sheets

Reports

Dashboards

Approval Workflows

Print Formats

should all be configurable through standardized Excel templates.

---

## 3. Generic Engines

Instead of developing individual modules, NOVOFLEX consists of reusable engines.

Examples:

• Master Engine

• Checksheet Engine

• Transaction Engine

• Workflow Engine

• Dashboard Engine

• Report Engine

• Notification Engine

---

## 4. Metadata Driven UI

The React frontend should render pages dynamically using metadata received from the backend.

Very few pages should be hardcoded.

---

## 5. API First

Every functionality must be available through REST APIs.

The frontend should never directly access the database.

---

## 6. Revision Control

Every template

Every master

Every check sheet

Every report

Every workflow

must maintain revision history.

No configuration should ever be permanently lost.

---

## 7. Guided User Experience

The ERP must guide users instead of simply showing errors.

Every upload should include:

• Instructions

• Validation

• Preview

• Error explanation

• Download latest template

---

## 8. Enterprise Standards

The ERP should support:

Multi Company

Multi Plant

Multi Department

Multi Warehouse

Multi User

Role Based Access

Audit Trail

Soft Delete

Version History

Approval Workflow

---

## 9. Future Ready

The architecture must support future modules without redesign.

Examples:

MES

SCADA

IoT

Barcode

QR Code

RFID

AI Assistant

Machine Vision

Predictive Maintenance

Business Intelligence

without changing the core architecture.

---

# Architecture Layers

Presentation Layer

↓

React

↓

API Layer

↓

FastAPI

↓

Business Layer

↓

Services

↓

Metadata Engine

↓

Database Layer

↓

SQLAlchemy

↓

SQLite (Development)

↓

PostgreSQL (Production)

---

# Long Term Vision

NOVOFLEX should evolve into a Manufacturing Platform where new modules are created through configuration rather than software development.
