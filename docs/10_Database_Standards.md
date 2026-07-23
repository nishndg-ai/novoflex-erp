# NOVOFLEX Database Standards

## Version

1.0

---

# Objective

Define database standards for the NOVOFLEX platform.

---

# Naming

snake_case

Singular model names

Plural table names

Meaningful column names

---

# Primary Keys

Integer

Auto Increment

Future UUID support

---

# Standard Audit Fields

created_at

updated_at

created_by

updated_by

deleted_at

deleted_by

version

is_active

---

# Soft Delete

Every table shall support soft delete.

---

# Relationships

Foreign Keys

Indexes

Cascade Rules

Lookup Integrity

---

# Performance

Indexes

Pagination

Lazy Loading

Caching Ready

---

# Security

Audit Trail

Role Security

Encrypted Sensitive Data

---

# Migration

Alembic

Version Controlled

Rollback Supported

---

# Backup

Scheduled Backup

Point-in-Time Recovery

Cloud Backup Ready

---

# Production Database

Development

SQLite

Testing

PostgreSQL

Production

PostgreSQL

Future

MS SQL Server

Oracle

MySQL
