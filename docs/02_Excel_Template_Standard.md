# NOVOFLEX Excel Template Standard

## Version

1.0

---

# Objective

This document defines the standard Excel format used throughout NOVOFLEX ERP.

Every master, transaction, check sheet, report, dashboard, workflow and configuration must follow this standard.

The objective is to eliminate custom programming and allow ERP configuration through Excel.

---

# Supported Template Types

* Master
* Transaction
* Check Sheet
* Dashboard
* Workflow
* Report
* Print Format
* Lookup
* Settings

---

# Standard Workbook Structure

Every template shall contain the following sheets.

## Sheet 1

Metadata

Mandatory

---

## Sheet 2

Structure

Mandatory

---

## Sheet 3

Data

Optional

---

## Sheet 4

Instructions

Mandatory

---

## Sheet 5

Lookup

Optional

---

# Metadata Sheet

Example

| Property      | Value          |
| ------------- | -------------- |
| Module        | Company Master |
| Template Type | Master         |
| Version       | 1.0            |
| ERP Version   | 1.0            |
| Primary Key   | Code           |
| Update Mode   | UPSERT         |
| Created By    | Administrator  |
| Created On    | Auto           |
| Description   | Company Master |

---

# Structure Sheet

Every field should contain metadata.

| Field | Caption | Data Type | Length | Mandatory | Unique | Lookup | Default | Editable |
| ----- | ------- | --------- | ------ | --------- | ------ | ------ | ------- | -------- |

Example

| Code | Company Code | Text | 20 | Yes | Yes | | | Yes |
| Name | Company Name | Text | 200 | Yes | No | | | Yes |
| GSTIN | GST Number | Text | 15 | No | No | | | Yes |
| Active | Active | Boolean | | Yes | No | YesNo | True | Yes |

---

# Data Sheet

Contains actual records.

The ERP must support

Insert

Update

Upsert

Ignore Duplicate

Archive Missing

based on template configuration.

---

# Instructions Sheet

Every template must explain

Purpose

Mandatory Fields

Optional Fields

Data Formats

Common Errors

Examples

Import Rules

Revision Notes

Users should never need separate documentation.

---

# Lookup Sheet

Contains allowed values.

Examples

Department

State

Country

Machine Type

Shift

UOM

Status

These values shall automatically become dropdown lists inside Excel.

---

# Excel Formatting Standards

Green

Mandatory fields

Yellow

Optional fields

Blue

Lookup fields

Grey

Read Only fields

Red

System Controlled fields

---

# Data Validation

Every template must contain

Dropdown Lists

Date Validation

Number Validation

Text Length Validation

Duplicate Detection

Mandatory Field Validation

Email Validation

GST Validation

PAN Validation

Phone Validation

where applicable.

---

# Import Process

Step 1

Download Latest Template

↓

Step 2

Fill Data

↓

Step 3

Upload

↓

Step 4

Validation

↓

Step 5

Preview

↓

Step 6

Import

↓

Step 7

Audit Log

---

# Template Versioning

Every template shall have

Major Version

Minor Version

Revision Date

Revision Remarks

Backward Compatibility Status

---

# User Guidance

Every upload screen shall provide

Download Template

Template Instructions

Sample Data

Validation Report

Preview

Import Summary

Error Report

Rollback Option

---

# Future Extensions

The standard must support future enhancements including

AI Mapping

OCR

Barcode

QR Code

Digital Signature

Image Upload

File Attachments

Formula Engine

without requiring redesign.
