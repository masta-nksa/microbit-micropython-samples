// Easter Egg: Snake (1 oder 2 Spieler an einer Tastatur).
// Freischalten: Konami-Code (Pfeile hoch hoch runter runter links rechts links rechts, B, A)
// oder auf dem Handy 5x schnell auf das Copyright-Zeichen im Footer tippen.
(function () {
  "use strict";

  var COLS = 28;
  var ROWS = 20;
  var CELL = 20;
  var TICK_MS = 110;
  var BEST_KEY = "snake-best";

  var KONAMI = ["arrowup", "arrowup", "arrowdown", "arrowdown", "arrowleft", "arrowright",
                "arrowleft", "arrowright", "b", "a"];
  var konamiPos = 0;

  var DIRS = {
    up: { x: 0, y: -1 },
    down: { x: 0, y: 1 },
    left: { x: -1, y: 0 },
    right: { x: 1, y: 0 }
  };
  var KEYS_P1 = { w: DIRS.up, s: DIRS.down, a: DIRS.left, d: DIRS.right };
  var KEYS_ARROWS = {
    arrowup: DIRS.up, arrowdown: DIRS.down, arrowleft: DIRS.left, arrowright: DIRS.right
  };

  var COLOR_P1 = "#3ddc84";
  var COLOR_P2 = "#ffb020";
  var COLOR_DEAD = "#5a5a55";
  var COLOR_FOOD = "#ff4d4d";

  var overlay, canvas, ctx, hud, msg, closeBtn;
  var players = [];
  var foods = [];
  var mode = 0;            // 0 = Menue, 1 oder 2 Spieler
  var running = false;
  var timer = null;
  var best = readBest();

  // ---------- Freischalten ----------

  document.addEventListener("keydown", function (e) {
    if (overlay && !overlay.hidden) {
      onGameKey(e);
      return;
    }
    var key = e.key.toLowerCase();
    if (key === KONAMI[konamiPos]) {
      konamiPos++;
      if (konamiPos === KONAMI.length) {
        konamiPos = 0;
        openGame();
      }
    } else {
      konamiPos = key === KONAMI[0] ? 1 : 0;
    }
  });

  var taps = 0;
  var tapTimer = null;
  document.addEventListener("click", function (e) {
    if (!e.target.closest || !e.target.closest("#egg-trigger")) return;
    taps++;
    clearTimeout(tapTimer);
    tapTimer = setTimeout(function () { taps = 0; }, 3000);
    if (taps >= 5) {
      taps = 0;
      openGame();
    }
  });

  if (window.console) {
    console.log("psst: ↑↑↓↓←→←→ B A");
  }

  // ---------- Overlay ----------

  function buildOverlay() {
    overlay = document.createElement("div");
    overlay.className = "snake-overlay";
    overlay.hidden = true;
    overlay.setAttribute("role", "dialog");
    overlay.setAttribute("aria-modal", "true");
    overlay.setAttribute("aria-label", "Snake");
    overlay.innerHTML =
      '<div class="snake-box" tabindex="-1">' +
      '<div class="snake-top"><span class="snake-title">Snake</span>' +
      '<button type="button" class="snake-close" aria-label="Schliessen">&times;</button></div>' +
      '<div class="snake-hud"></div>' +
      '<canvas class="snake-canvas" width="' + COLS * CELL + '" height="' + ROWS * CELL + '"></canvas>' +
      '<div class="snake-msg"></div>' +
      '<div class="snake-buttons">' +
      '<button type="button" data-players="1">1 Spieler</button>' +
      '<button type="button" data-players="2">2 Spieler</button></div>' +
      '<div class="snake-help">1 Spieler: Pfeile oder WASD (auf dem Handy wischen). ' +
      '2 Spieler: <span style="color:' + COLOR_P1 + '">Grün = WASD</span>, ' +
      '<span style="color:' + COLOR_P2 + '">Orange = Pfeile</span>. ' +
      'Leertaste = nochmal, Esc = schliessen.</div>' +
      '</div>';
    document.body.appendChild(overlay);

    canvas = overlay.querySelector(".snake-canvas");
    ctx = canvas.getContext("2d");
    hud = overlay.querySelector(".snake-hud");
    msg = overlay.querySelector(".snake-msg");
    closeBtn = overlay.querySelector(".snake-close");

    closeBtn.addEventListener("click", closeGame);
    overlay.addEventListener("click", function (e) {
      if (e.target === overlay) closeGame();
    });
    Array.prototype.forEach.call(overlay.querySelectorAll("[data-players]"), function (b) {
      b.addEventListener("click", function () {
        b.blur();
        start(parseInt(b.getAttribute("data-players"), 10));
      });
    });

    var touchStart = null;
    canvas.addEventListener("touchstart", function (e) {
      var t = e.changedTouches[0];
      touchStart = { x: t.clientX, y: t.clientY };
    }, { passive: true });
    canvas.addEventListener("touchmove", function (e) { e.preventDefault(); }, { passive: false });
    canvas.addEventListener("touchend", function (e) {
      if (!touchStart || !running || !players.length) return;
      var t = e.changedTouches[0];
      var dx = t.clientX - touchStart.x;
      var dy = t.clientY - touchStart.y;
      touchStart = null;
      if (Math.max(Math.abs(dx), Math.abs(dy)) < 20) return;
      var d = Math.abs(dx) > Math.abs(dy) ? (dx > 0 ? DIRS.right : DIRS.left)
                                          : (dy > 0 ? DIRS.down : DIRS.up);
      setDir(players[0], d);
    });
  }

  function openGame() {
    if (!overlay) buildOverlay();
    overlay.hidden = false;
    document.body.classList.add("snake-open");
    mode = 0;
    running = false;
    players = [];
    foods = [];
    updateHud();
    setMessage("Wähle einen Modus (Taste 1 oder 2)");
    draw();
    overlay.querySelector(".snake-box").focus();
  }

  function closeGame() {
    stop();
    overlay.hidden = true;
    document.body.classList.remove("snake-open");
  }

  // ---------- Steuerung ----------

  function onGameKey(e) {
    var key = e.key.toLowerCase();
    if (key === "escape") {
      closeGame();
      e.preventDefault();
      return;
    }
    if (key === "1" || key === "2") {
      start(parseInt(key, 10));
      e.preventDefault();
      return;
    }
    if ((key === " " || e.code === "Space" || key === "enter") && e.target.tagName !== "BUTTON") {
      if (!running && mode) start(mode);
      e.preventDefault();
      return;
    }
    if (!running) {
      if (KEYS_ARROWS[key]) e.preventDefault();
      return;
    }
    if (mode === 1) {
      var d1 = KEYS_ARROWS[key] || KEYS_P1[key];
      if (d1) { setDir(players[0], d1); e.preventDefault(); }
    } else {
      if (KEYS_P1[key]) { setDir(players[0], KEYS_P1[key]); e.preventDefault(); }
      if (KEYS_ARROWS[key]) { setDir(players[1], KEYS_ARROWS[key]); e.preventDefault(); }
    }
  }

  function setDir(p, d) {
    if (!p.alive) return;
    if (d.x === -p.dir.x && d.y === -p.dir.y) return;
    p.next = d;
  }

  // ---------- Spiel ----------

  function newPlayer(x, y, dir, color) {
    var body = [];
    for (var i = 0; i < 3; i++) body.push({ x: x - dir.x * i, y: y - dir.y * i });
    return { body: body, dir: dir, next: dir, alive: true, color: color, score: 0 };
  }

  function start(n) {
    stop();
    mode = n;
    players = [newPlayer(6, Math.floor(ROWS / 2), DIRS.right, COLOR_P1)];
    if (n === 2) {
      players[0].body = shiftBody(players[0], 0, -3);
      players.push(newPlayer(COLS - 7, Math.floor(ROWS / 2) + 3, DIRS.left, COLOR_P2));
    }
    foods = [];
    for (var i = 0; i < n; i++) placeFood();
    running = true;
    setMessage("");
    updateHud();
    draw();
    timer = setTimeout(tick, TICK_MS);
  }

  function shiftBody(p, dx, dy) {
    return p.body.map(function (c) { return { x: c.x + dx, y: c.y + dy }; });
  }

  function stop() {
    running = false;
    clearTimeout(timer);
    timer = null;
  }

  function isFree(x, y) {
    for (var i = 0; i < players.length; i++) {
      for (var j = 0; j < players[i].body.length; j++) {
        if (players[i].body[j].x === x && players[i].body[j].y === y) return false;
      }
    }
    for (var k = 0; k < foods.length; k++) {
      if (foods[k].x === x && foods[k].y === y) return false;
    }
    return true;
  }

  function placeFood() {
    for (var tries = 0; tries < 500; tries++) {
      var x = Math.floor(Math.random() * COLS);
      var y = Math.floor(Math.random() * ROWS);
      if (isFree(x, y)) {
        foods.push({ x: x, y: y });
        return;
      }
    }
  }

  function foodAt(x, y) {
    for (var i = 0; i < foods.length; i++) {
      if (foods[i].x === x && foods[i].y === y) return i;
    }
    return -1;
  }

  function tick() {
    if (!running) return;
    var heads = [];
    var eats = [];
    players.forEach(function (p, i) {
      if (!p.alive) { heads[i] = null; return; }
      p.dir = p.next;
      heads[i] = { x: p.body[0].x + p.dir.x, y: p.body[0].y + p.dir.y };
      eats[i] = foodAt(heads[i].x, heads[i].y) >= 0;
    });

    // Belegte Felder: alle Koerper, das Schwanzende zaehlt frei, wenn die Schlange nicht waechst
    var occupied = {};
    players.forEach(function (p, i) {
      var len = p.body.length;
      if (p.alive && !eats[i]) len--;
      for (var j = 0; j < len; j++) occupied[p.body[j].x + "," + p.body[j].y] = true;
    });

    var dies = players.map(function (p, i) {
      if (!p.alive) return false;
      var h = heads[i];
      if (h.x < 0 || h.y < 0 || h.x >= COLS || h.y >= ROWS) return true;
      if (occupied[h.x + "," + h.y]) return true;
      for (var o = 0; o < players.length; o++) {
        if (o !== i && heads[o] && heads[o].x === h.x && heads[o].y === h.y) return true;
      }
      return false;
    });

    players.forEach(function (p, i) {
      if (!p.alive) return;
      if (dies[i]) { p.alive = false; return; }
      p.body.unshift(heads[i]);
      if (eats[i]) {
        p.score++;
        foods.splice(foodAt(heads[i].x, heads[i].y), 1);
        placeFood();
      } else {
        p.body.pop();
      }
    });

    updateHud();
    draw();

    var alive = players.filter(function (p) { return p.alive; });
    if (mode === 1 ? alive.length === 0 : alive.length <= 1) {
      finish();
      return;
    }
    timer = setTimeout(tick, TICK_MS);
  }

  function finish() {
    running = false;
    var text;
    if (mode === 1) {
      var score = players[0].score;
      if (score > best) {
        best = score;
        writeBest(best);
        text = "Game Over: " + score + " Punkte, neuer Rekord!";
      } else {
        text = "Game Over: " + score + " Punkte";
      }
    } else if (players[0].alive) {
      text = "Grün gewinnt!";
    } else if (players[1].alive) {
      text = "Orange gewinnt!";
    } else {
      text = "Unentschieden!";
    }
    setMessage(text + " Leertaste = nochmal");
    updateHud();
    draw();
  }

  // ---------- Anzeige ----------

  function setMessage(text) {
    msg.textContent = text;
  }

  function updateHud() {
    if (!hud) return;
    if (mode === 2 && players.length === 2) {
      hud.innerHTML = '<span style="color:' + COLOR_P1 + '">Grün: ' + players[0].score + '</span>' +
                      '<span style="color:' + COLOR_P2 + '">Orange: ' + players[1].score + '</span>';
    } else {
      hud.innerHTML = "<span>Punkte: " + (players[0] ? players[0].score : 0) + "</span>" +
                      "<span>Rekord: " + best + "</span>";
    }
  }

  function cell(x, y, color) {
    ctx.fillStyle = color;
    ctx.beginPath();
    var r = 5;
    var px = x * CELL + 1;
    var py = y * CELL + 1;
    var s = CELL - 2;
    if (ctx.roundRect) {
      ctx.roundRect(px, py, s, s, r);
    } else {
      ctx.rect(px, py, s, s);
    }
    ctx.fill();
  }

  function draw() {
    ctx.fillStyle = "#14161a";
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    ctx.fillStyle = "#23262d";
    for (var x = 0; x < COLS; x++) {
      for (var y = 0; y < ROWS; y++) {
        ctx.fillRect(x * CELL + CELL / 2 - 1, y * CELL + CELL / 2 - 1, 2, 2);
      }
    }

    foods.forEach(function (f) {
      ctx.fillStyle = COLOR_FOOD;
      ctx.beginPath();
      ctx.arc(f.x * CELL + CELL / 2, f.y * CELL + CELL / 2, CELL / 2 - 3, 0, Math.PI * 2);
      ctx.fill();
    });

    players.forEach(function (p) {
      p.body.forEach(function (c, i) {
        var color = p.alive ? p.color : COLOR_DEAD;
        cell(c.x, c.y, i === 0 && p.alive ? "#ffffff" : color);
        if (i === 0 && p.alive) {
          ctx.fillStyle = p.color;
          ctx.fillRect(c.x * CELL + 6, c.y * CELL + 6, CELL - 12, CELL - 12);
        }
      });
    });
  }

  // ---------- Rekord ----------

  function readBest() {
    try {
      return parseInt(localStorage.getItem(BEST_KEY), 10) || 0;
    } catch (e) {
      return 0;
    }
  }

  function writeBest(n) {
    try {
      localStorage.setItem(BEST_KEY, String(n));
    } catch (e) { /* Speicher nicht verfuegbar */ }
  }
})();
