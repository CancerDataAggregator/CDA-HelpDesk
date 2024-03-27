---
title:  For Developers
status: wip
---

<link rel="stylesheet" type="text/css" href="swagger-ui.css">

This page is actively under construction, if you can't find the information you need please contact us at our helpdesk.


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

## Swagger definitions

<div id="swagger-ui"></div>

<script src="swagger-ui-bundle.js"></script>
<script src="swagger-ui-standalone-preset.js"></script>

<script>
window.onload = function() {
  const ui = SwaggerUIBundle({
    url: "./service_openapi.yaml",
    dom_id: '#swagger-ui',
    presets: [
      SwaggerUIBundle.presets.apis,
      SwaggerUIStandalonePreset
    ]
  })

  window.ui = ui
}
</script>