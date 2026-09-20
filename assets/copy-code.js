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

  function flash(button, label, cls) {
    button.textContent = label;
    button.classList.add(cls);
    setTimeout(function () {
      button.textContent = "Kopieren";
      button.classList.remove(cls);
    }, 1800);
  }

  document.querySelectorAll("div.highlighter-rouge").forEach(function (block) {
    var pre = block.querySelector("pre");
    if (!pre) return;

    var button = document.createElement("button");
    button.type = "button";
    button.className = "copy-code-button";
    button.textContent = "Kopieren";
    button.setAttribute("aria-label", "Code in die Zwischenablage kopieren");

    button.addEventListener("click", function () {
      copyText(pre.textContent.replace(/\n$/, ""))
        .then(function () { flash(button, "Kopiert!", "is-done"); })
        .catch(function () { flash(button, "Fehler", "is-error"); });
    });

    block.appendChild(button);
  });
})();
