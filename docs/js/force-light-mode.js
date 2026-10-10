// docs/js/force-light-mode.js
// DataTables (via itables) auto-detects system dark-mode preference using
// window.matchMedia('(prefers-color-scheme: dark)') and toggles a "dark" class
// onto <html> when it matches -- this is documented, built-in DataTables behavior,
// not something in this site's own code. Since this site doesn't support a dark
// theme at all, the most reliable fix is intercepting that one detection call so
// it always reports "no match," rather than patching each individual dark-reactive
// DataTables component (buttons, SearchBuilder, etc.) one at a time as each is
// discovered.
(function() {
  const originalMatchMedia = window.matchMedia;
  window.matchMedia = function(query) {
    if (query.includes("prefers-color-scheme: dark")) {
      return {
        matches: false,
        media: query,
        addListener: function() {},
        removeListener: function() {},
        addEventListener: function() {},
        removeEventListener: function() {},
      };
    }
    return originalMatchMedia.call(window, query);
  };
})();
