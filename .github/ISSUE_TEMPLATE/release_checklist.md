---
name: Release Checklist
about: Ensure everything is updated properly
title: ''
labels: ''
assignees: 'ACharbonneau'

---

- type: checkboxes
  id: ToDos
  attributes:
    label: Have you checked all of these?
    description: Data Only release
    options:
      - label: Update data release notes
      - label: Add new vignettes
      - label: Edit hardcoded vignette counts
  
  - type: checkboxes
  id: ToDos
  attributes:
    label: Have you checked all of these?
    description: Code release
    options:
      - label: Update code release notes
      - label: Add new vignettes
      - label: Edit Man pages
      - label: Update API page
   
  - type: checkboxes
  id: ToDos
  attributes:
    label: Have you checked all of these?
    description: Other
    options:
      - label: Personnel list
      - label: ETL image
