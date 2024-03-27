---
title:  For Developers
status: wip
---

This page is actively under construction, if you can't find the information you need please contact us at our helpdesk.

<iframe src="https://cancerdata.dsde-prod.broadinstitute.org/api/swagger-ui.html" title="swagger documentation"></iframe>





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