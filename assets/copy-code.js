// Kopieren-Button fuer alle Codebloecke (Rouge: div.highlighter-rouge)
(function () {
  "use strict";

  function copyText(text) {
    if (navigator.clipboard && window.isSecureContext) {
      return navigator.clipboard.writeText(text);
    }
    return new Promise(function (resolve, reject) {
      var area = document.createElement("textarea");
      area.value = text;
      area.setAttribute("readonly", "");
      area.style.position = "fixed";
      area.style.opacity = "0";
      document.body.appendChild(area);
      area.select();
      try {
        document.execCommand("copy") ? resolve() : reject();
      } catch (e) {
        reject(e);
      } finally {
        document.body.removeChild(area);
      }
    });
  }

  var ICON_COPY =
    '<svg viewBox="0 0 16 16" width="16" height="16" fill="none" stroke="currentColor" ' +
    'stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">' +
    '<rect x="5.5" y="5.5" width="8" height="8" rx="1.5"/>' +
    '<path d="M10.5 3.5v-.5A1.5 1.5 0 0 0 9 1.5H3A1.5 1.5 0 0 0 1.5 3v6A1.5 1.5 0 0 0 3 10.5h.5"/>' +
    '</svg>';
  var ICON_DONE =
    '<svg viewBox="0 0 16 16" width="16" height="16" fill="none" stroke="currentColor" ' +
    'stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">' +
    '<path d="M3 8.5l3.2 3.2L13 4.8"/></svg>';

  function flash(button, title, cls) {
    button.innerHTML = cls === "is-done" ? ICON_DONE : ICON_COPY;
    button.title = title;
    button.classList.add(cls);
    setTimeout(function () {
      button.innerHTML = ICON_COPY;
      button.title = "Code kopieren";
      button.classList.remove(cls);
    }, 1500);
  }

  document.querySelectorAll("div.highlighter-rouge").forEach(function (block) {
    var pre = block.querySelector("pre");
    if (!pre) return;

    var button = document.createElement("button");
    button.type = "button";
    button.className = "copy-code-button";
    button.innerHTML = ICON_COPY;
    button.title = "Code kopieren";
    button.setAttribute("aria-label", "Code in die Zwischenablage kopieren");

    button.addEventListener("click", function () {
      copyText(pre.textContent.replace(/\n$/, ""))
        .then(function () { flash(button, "Kopiert", "is-done"); })
        .catch(function () { flash(button, "Kopieren fehlgeschlagen", "is-error"); });
    });

    block.appendChild(button);
  });
})();
