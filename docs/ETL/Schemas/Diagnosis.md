---
title: diagnosis
---


<div id="test">
<script type="text/javascript" src="../../../javascripts/renderjson.js"></script>
<script>
renderjson.set_show_to_level(1);
var example = {
    "$id": "https://example.org/cda-data-model/Diagnosis#",
    "$schema": "http://json-schema.org/draft-07/schema#",
    "description": "",
    "definitions": {},
    "additionalProperties": true,
    "properties": {
        "describedBy": {
            "description": "The JSON Schema used for this object.",
            "type": "string"
        },
        "id": {
            "description": "The 'logical' identifier of the entity in the repository, e.g. a UUID.  This 'id' is unique within a given system. The identified entity may have a different 'id' in a different system.",
            "type": "string"
        },
        "identifier": {
            "description": "A 'business' identifier  or accession number for the entity, typically as provided by an external system or authority, that persists across implementing systems  (i.e. a  'logical' identifier). ",
            "items": {
                "$ref": "https://example.org/cda-data-model/definitions/Identifier"
            },
            "type": "array"
        },
        "age_at_diagnosis": {
            "description": "",
            "type": "integer"
        },
        "grade": {
            "description": "",
            "type": "string"
        },
        "harmonized_primary_diagnosis": {
            "description": "",
            "type": "string"
        },
        "morphology": {
            "description": "",
            "type": "string"
        },
        "primary_diagnosis": {
            "description": "",
            "$ref": "https://example.org/cda-data-model/definitions/CodeableConcept"
        },
        "stage": {
            "description": "",
            "type": "string"
        },
        "treatment": {
            "description": "",
            "type": "array",
            "items": {
                "$ref": "https://example.org/cda-data-model/Treatment"
            }
        },
        "research_subject": {
            "description": "Reference to the ResearchSubject UUID.",
            "type": "string"
        },
        "specimen": {
            "description": "Reference to the Specimen used for this diagnosis.",
            "type": "string"
        }
    },
    "required": [
        "id",
        "describedBy"
    ],
    "title": "Diagnosis",
    "type": "object"
};
    document.getElementById("test").appendChild(renderjson(example));
</script>
