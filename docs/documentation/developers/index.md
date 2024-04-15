---
title:  For Developers
status: wip
---

<link rel="stylesheet" type="text/css" href="swagger-ui.css">

This page is actively under construction, if you can't find the information you need please contact us at our helpdesk.

# API roadmap

Our API will be undergoing large structural changes in the spring/summer, and we highly recommend delaying any serious development against it until we release the new version. However, if you are interested in working with our API, we would love to hear from you, especially as we work out what capabilities we will offer. We would be happy to work with you during our development, and to bring your group on as a beta tester when we get closer to release.

## Swagger definitions

<div id="swagger-ui"></div>

<script src="swagger-ui-bundle.js"></script>
<script src="swagger-ui-standalone-preset.js"></script>

<script>
  const swaggerUrl = "https://raw.githubusercontent.com/CancerDataAggregator/cda-service/develop/src/main/resources/api/service_openapi.yaml"
  const apiUrl = "https://cancerdata.dsde-prod.broadinstitute.org/api/swagger-ui.html"
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