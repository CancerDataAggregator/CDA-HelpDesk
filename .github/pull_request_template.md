---
name: Release Checklist
about: Ensure everything is updated properly
title: ''
labels: ''
assignees: 'ACharbonneau'

---

body:
- type: input
  id: prevalence
  attributes:
    label: Bug prevalence
    description: "How often do you or others encounter this bug?"
    placeholder: "Whenever I visit the user account page (1-2 times a week)"
  validations:
    required: true
