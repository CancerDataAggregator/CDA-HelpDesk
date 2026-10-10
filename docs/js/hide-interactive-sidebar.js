if (window.location.pathname.includes("/interactive/")) {
  document.addEventListener("DOMContentLoaded", function() {
    const left = document.querySelector(".md-sidebar--primary");
    if (left) left.style.display = "none";
  });
}
