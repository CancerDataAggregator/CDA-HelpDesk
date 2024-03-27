---
title:  For Developers
status: wip
---





link to swagger: https://cancerdata.dsde-prod.broadinstitute.org/api/swagger-ui.html


## mock node structure

```
{ 
    "MATCH_ALL": [
        {
            "operator": "=",
            "column": "column_name",
            "match": {
                "type": "(un)quoted",
                "value": "filter_value"
            }
        },
        {
            "operator": "=",
            "column": "column_name",
            "match": {
                "type": "(un)quoted",
                "value": "filter_value"
            }
        }
    ],
    "MATCH_SOME": [
        {
            "operator": "=",
            "column": "column_name",
            "match": {
                "type": "(un)quoted",
                "value": "filter_value"
            }
        }
    ],
    "SELECT": [
        "col1",
        "col2",
        "col3",
        "...",
        "coln"

    ]
}
```