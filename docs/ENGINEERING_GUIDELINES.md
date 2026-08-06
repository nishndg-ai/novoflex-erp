# BLUISH ERP Platform

# ENGINEERING_GUIDELINES.md

## Purpose

This document defines the engineering principles that govern the BLUISH platform.

Every feature, module, engine, API, UI component, and AI capability must follow these guidelines.

If any implementation conflicts with these principles, the implementation must be changed—not the principles—unless there is a compelling architectural reason.

---

# 1. Platform Philosophy

BLUISH is **not an ERP application**.

BLUISH is an **ERP Creation Platform**.

Developers build the platform.

Business users build ERP applications using metadata.

**Principle**

> Code builds the platform. Metadata builds the ERP.

---

# 2. Metadata First

Everything possible must be represented as metadata.

Examples include:

* Business Objects
* Fields
* Forms
* Grids
* Menus
* Validation Rules
* Workflows
* Dashboards
* Reports
* Permissions
* Notifications
* AI Prompts

Adding a new ERP feature should preferably require metadata changes rather than source code changes.

---

# 3. Runtime First

Nothing should be statically generated unless absolutely necessary.

The Runtime Engine is responsible for rendering:

* Forms
* Grids
* Menus
* Detail Views
* Dashboards
* Reports
* Workflows

The frontend renders metadata instead of containing business logic.

---

# 4. No Module-Specific Development

Avoid creating:

* CustomerForm.tsx
* SupplierGrid.tsx
* ItemMasterPage.tsx

Instead, build reusable runtime components:

* RuntimeForm
* RuntimeGrid
* RuntimeDetail
* RuntimeDashboard
* RuntimeWorkflow

One implementation should work for every Business Object.

---

# 5. Generic Before Custom

Every new capability should first be evaluated as a platform feature.

Ask:

"Can this solve the same problem for every module?"

If yes, build it into the platform rather than into a single ERP module.

---

# 6. Single Source of Truth

Metadata is the authoritative source for:

* Structure
* Behaviour
* Validation
* Navigation
* Security
* Presentation

No duplicate definitions should exist in frontend or backend code.

---

# 7. Separation of Responsibilities

Backend owns:

* Metadata
* Business Rules
* Validation
* Provisioning
* Runtime APIs
* Security

Frontend owns:

* Rendering
* User Interaction
* User Experience

Frontend should not contain business-specific logic.

---

# 8. Reusable Engines

Every engine must be reusable across the platform.

Examples:

* Form Engine
* Grid Engine
* Workflow Engine
* Report Engine
* Notification Engine
* AI Engine

No engine should depend on a specific ERP module.

---

# 9. Database Independence

Business logic must not depend on a specific database vendor.

Use:

* SQLAlchemy
* Repository Pattern
* Query Builder

Avoid vendor-specific SQL unless isolated.

---

# 10. API Standards

All APIs should be:

* RESTful
* Predictable
* Metadata-driven
* Versionable

Business Objects should expose a consistent runtime API.

---

# 11. Security First

Security is metadata-driven.

Support:

* Role-based access
* Object permissions
* Field permissions
* Workflow permissions
* Audit logging

Security rules must never be hardcoded inside UI components.

---

# 12. Auditability

Every important change should be traceable.

Track:

* Who
* When
* What
* Previous Value
* New Value

Audit capability must be platform-wide.

---

# 13. AI Integration

AI extends the platform.

AI must never bypass:

* Metadata
* Validation
* Permissions
* Workflow
* Security

AI should generate metadata rather than application code whenever possible.

---

# 14. User Experience

The platform should require minimal technical knowledge.

Business users should perform most configuration through visual designers.

Swagger and direct API interaction are development tools—not end-user tools.

---

# 15. Performance

Runtime flexibility must not compromise usability.

Guidelines:

* Lazy loading
* Server-side pagination
* Metadata caching
* Query optimization
* Efficient rendering

---

# 16. Extensibility

Every subsystem should be designed for extension without modification.

Examples:

* New field types
* New control types
* New workflow actions
* New report formats
* New AI providers

---

# 17. Consistency

Naming conventions, APIs, metadata, UI behaviour, and user experience should remain consistent across all modules.

Users should learn the platform once and apply that knowledge everywhere.

---

# 18. Engineering Decision Test

Before implementing any feature, ask:

1. Is it metadata-driven?
2. Is it reusable?
3. Can every Business Object use it?
4. Does it belong in the platform instead of a module?
5. Will it reduce future coding effort?
6. Does it support the long-term vision of an ERP Creation Platform?

If the answer to most questions is "No", reconsider the implementation.

---

# Engineering Motto

> Build the platform once. Build ERP systems forever.
