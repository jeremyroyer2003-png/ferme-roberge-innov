/* Ferme Roberge-Innov — catalogue (accueil) et galerie (pages produit).
   Les données viennent de data/products.js (window.PRODUCTS), généré à partir de
   data/products.json, pour que le site fonctionne aussi ouvert directement depuis le disque. */
(function () {
  "use strict";

  var fmt = new Intl.NumberFormat("fr-CA", { style: "currency", currency: "CAD" });
  function formatPrice(p) {
    if (p.price === null || p.price === undefined) return '<span class="price-ask">Prix sur demande</span>';
    var s = fmt.format(p.price);
    if (p.price_prefix) s = p.price_prefix + " " + s;
    if (p.price_unit) s += " / " + p.price_unit;
    return s;
  }
  function esc(s) {
    return String(s == null ? "" : s).replace(/[&<>"']/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
    });
  }
  function norm(s) {
    return String(s || "").toLowerCase().normalize("NFD").replace(/[̀-ͯ]/g, "");
  }

  /* ---------- Catalogue ---------- */
  function initCatalog() {
    var root = document.getElementById("catalog-grid");
    if (!root || !window.PRODUCTS) return;
    var products = window.PRODUCTS;
    var base = root.getAttribute("data-base") || "";
    var state = { cat: "all", q: "", min: null, max: null, sort: "newest" };

    var chipsEl = document.getElementById("chips");
    var cats = [];
    products.forEach(function (p) { if (cats.indexOf(p.category) === -1) cats.push(p.category); });
    cats.sort(function (a, b) { return a.localeCompare(b, "fr"); });
    var chipHtml = '<button type="button" class="chip" data-cat="all" aria-pressed="true">Tout (' + products.length + ")</button>";
    cats.forEach(function (c) {
      var n = products.filter(function (p) { return p.category === c; }).length;
      chipHtml += '<button type="button" class="chip" data-cat="' + esc(c) + '" aria-pressed="false">' + esc(c) + " (" + n + ")</button>";
    });
    chipsEl.innerHTML = chipHtml;
    chipsEl.addEventListener("click", function (e) {
      var b = e.target.closest(".chip");
      if (!b) return;
      state.cat = b.getAttribute("data-cat");
      chipsEl.querySelectorAll(".chip").forEach(function (x) { x.setAttribute("aria-pressed", x === b ? "true" : "false"); });
      render();
    });

    var q = document.getElementById("q");
    q.addEventListener("input", function () { state.q = norm(q.value.trim()); render(); });
    var minEl = document.getElementById("pmin"), maxEl = document.getElementById("pmax");
    function num(v) { var n = parseFloat(String(v).replace(",", ".")); return isNaN(n) ? null : n; }
    minEl.addEventListener("input", function () { state.min = num(minEl.value); render(); });
    maxEl.addEventListener("input", function () { state.max = num(maxEl.value); render(); });
    var sortEl = document.getElementById("sort");
    sortEl.addEventListener("change", function () { state.sort = sortEl.value; render(); });

    var countEl = document.getElementById("result-count");

    function render() {
      var list = products.filter(function (p) {
        if (state.cat !== "all" && p.category !== state.cat) return false;
        if (state.q && norm(p.name + " " + p.category + " " + p.description).indexOf(state.q) === -1) return false;
        if (state.min !== null || state.max !== null) {
          if (p.price === null) return false;
          if (state.min !== null && p.price < state.min) return false;
          if (state.max !== null && p.price > state.max) return false;
        }
        return true;
      });
      list.sort(function (a, b) {
        if (state.sort === "price-asc" || state.sort === "price-desc") {
          var dir = state.sort === "price-asc" ? 1 : -1;
          if (a.price === null && b.price === null) return 0;
          if (a.price === null) return 1;            // sans prix toujours à la fin
          if (b.price === null) return -1;
          return (a.price - b.price) * dir;
        }
        if (state.sort === "name") return a.name.localeCompare(b.name, "fr");
        return String(b.date || "").localeCompare(String(a.date || ""));
      });
      countEl.textContent = list.length + (list.length > 1 ? " produits" : " produit");
      if (!list.length) {
        root.innerHTML = '<li class="empty">Aucun produit ne correspond à ces filtres.</li>';
        return;
      }
      root.innerHTML = list.map(function (p, i) {
        var img = p.images[0] || "";
        return '<li><article class="card">' +
          '<img class="card-img" src="' + base + esc(p.thumb || img) + '" alt="' + esc(p.name) + '" width="600" height="450"' +
          (i > 3 ? ' loading="lazy"' : "") + ' decoding="async">' +
          '<div class="card-body"><span class="card-cat">' + esc(p.category) + "</span>" +
          '<h3><a href="' + base + "produits/" + esc(p.id) + '.html">' + esc(p.name) + "</a></h3>" +
          '<p class="card-price">' + formatPrice(p) + "</p>" +
          '<span class="card-more" aria-hidden="true">Voir les détails →</span></div></article></li>';
      }).join("");
    }
    render();
  }

  /* ---------- Galerie produit ---------- */
  function initGallery() {
    var main = document.getElementById("gallery-main-img");
    var thumbs = document.querySelectorAll(".thumbs button");
    if (!main || !thumbs.length) return;
    thumbs.forEach(function (b) {
      b.addEventListener("click", function () {
        main.src = b.getAttribute("data-full");
        main.alt = b.getAttribute("data-alt");
        thumbs.forEach(function (x) { x.setAttribute("aria-current", x === b ? "true" : "false"); });
      });
    });
  }

  document.addEventListener("DOMContentLoaded", function () { initCatalog(); initGallery(); });
})();
