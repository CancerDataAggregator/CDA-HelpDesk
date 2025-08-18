// script.js
$(document).ready(function () {
  $('#cdaaug2025').DataTable({
    layout: {
      topStart: {
        buttons: [
          {
            extend: 'searchBuilder',
            text: 'Advanced Search'
          }
        ]
      }
    }
  });
});
