document.addEventListener("DOMContentLoaded", function () {
  const table = document.querySelector("#cdaaug2025");
  if (table) {
    $('#cdaaug2025').DataTable({
      layout: {
        topStart: {
          buttons: [
            { extend: 'searchBuilder', text: 'Search / Filter' }
          ]
        }
      }
    });
  }
});
