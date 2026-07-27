# ERP Document Control + AI Form Generator Architecture

## Purpose

Future reference architecture for an ERP platform where QMS Document
Control manages controlled formats and departmental modules consume
approved runtime forms.

## Core Flow

Document Control → Document Change Request → Approval → Revision Release
→ Issue to Department Module → Runtime Form Execution

## Master Data Update Options

1.  Revise Format

-   Change structure/layout of master or form.
-   Updates metadata and creates revision.

2.  Revise Existing Data

-   Modify existing records.
-   Maintain revision history.

3.  Add New Data

-   Create new records.

All operations support: - Manual ERP entry - Excel upload - Word
upload - PDF upload - Image upload

## AI Document Processing

Upload File → OCR / Table Detection / Layout Detection → Data
Identification → Field Mapping → Validation → Runtime Metadata
Generation → ERP Form

## Examples

### Product Master

Upload Excel/PDF/Image. AI identifies: - Product Code - Product Name -
Material - Customer - Drawing Number - Revision

### Patrol Inspection

AI identifies: - Machine - Parameter - Specification - Actual Reading -
Result

### PM Checksheet

AI identifies: - Machine - Lubrication Check - Cleaning - Abnormality -
Technician

## Document Control Module

### Document Master

Stores: - Document Number - Document Name - Department - Module -
Owner - Current Revision - Status

### Document Revision

Stores: - Revision Number - Revision Reason - File - Metadata JSON -
Effective Date - Approval Details

### Document Change Request

Workflow:

Draft → Review → Approval → Release

### Document Issue Control

Controls distribution of approved formats to: - Production - Quality -
Purchase - Maintenance - Stores

## AI Mapping Engine

Example:

Source: Item No

ERP Field: product.code

Confidence: 98%

Mappings shall be reusable.

## Runtime Integration

Document Revision → Metadata → Runtime Form

Uses: - Runtime Grid Renderer - Runtime Form Renderer - Dynamic
Controls - Workflow Engine

## Database Modules

platform/

-   document_control/
-   document_ai/
-   workflow/
-   approval/

## Required Tables

-   document_master
-   document_revision
-   document_change_request
-   document_issue
-   document_upload
-   document_field_mapping

## IATF Alignment

Supports: - Documented Information Control - Revision Control -
Traceability - Approval History - Controlled Forms

## Development Roadmap

Completed: - Runtime CRUD Engine - Dynamic Grid - Dynamic Forms -
Create/Edit/Update/Delete

Next: 1. Runtime Layout Engine 2. Document Control Module 3. AI Document
Processing Engine 4. Master Data Lifecycle Engine 5. Department
Controlled Forms

## Vision

Existing company documents become ERP-controlled forms.

Approved formats control execution.

Revisions maintain audit history.

AI reduces manual data entry.
