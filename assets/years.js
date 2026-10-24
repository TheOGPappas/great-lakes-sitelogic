// Self-updating year figures for greatlakessitelogic.com.
// Elements carry an anchor year in a data attribute; this script recomputes
// the displayed value from the visitor's current year, so the numbers roll
// over every January 1 with no rebuild and no manual edit. The text inside
// each element is the correct value as of the last build and is shown as-is
// if this script fails to load.
// Anchors: combined experience = years since 1990 (36 in 2026, +1/yr);
// firsthand field experience = years since 2010 (16 in 2026, +1/yr).
(function () {
  function yearsSince(anchor) { return new Date().getFullYear() - anchor; }
  function numberWord(n) {
    var ones = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"];
    var tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"];
    if (n < 20) return ones[n];
    var t = Math.floor(n / 10), r = n % 10;
    return tens[t] + (r ? "-" + ones[r].toLowerCase() : "");
  }
  function fillTemplate(tpl) {
    return tpl.replace(/\{\{yrs:(\d{4})\}\}/g, function (m, a) { return yearsSince(+a); });
  }
  function run() {
    var y = new Date().getFullYear();
    document.querySelectorAll("[data-copyright-year]").forEach(function (el) { el.textContent = y; });
    document.querySelectorAll("[data-years-since]").forEach(function (el) { el.textContent = yearsSince(+el.getAttribute("data-years-since")); });
    document.querySelectorAll("[data-years-word]").forEach(function (el) { el.textContent = numberWord(yearsSince(+el.getAttribute("data-years-word"))); });
    document.querySelectorAll("meta[data-desc-template]").forEach(function (el) { el.setAttribute("content", fillTemplate(el.getAttribute("data-desc-template"))); });
  }
  if (document.readyState === "loading") { document.addEventListener("DOMContentLoaded", run); } else { run(); }
})();
