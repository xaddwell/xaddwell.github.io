---
layout: default
title: "Privacy Iceberg: Protected Demo Materials"
date: 2026-11-12
tags: [protected, demo]
permalink: /posts/privacy-iceberg-demos/
excerpt: "Password-protected experimental materials."
sitemap: false
noindex: true
author_profile: true
---

<script src="{{ '/assets/js/pid-demo-payload.js' | relative_url }}"></script>

<div class="pid-lock" id="pid-lock">
  <h2 class="pid-lock__title"><i class="fas fa-lock"></i> Protected materials</h2>
  <p class="pid-lock__lede">This page contains research materials from a controlled experiment, shared with a specific person. Everything on it &mdash; the text, the instruction, and both demos &mdash; is encrypted, and can only be read with the password you were given.</p>
  <form id="pid-form" autocomplete="off">
    <input type="password" id="pid-password" placeholder="Password" aria-label="Password" required>
    <button type="submit">Unlock</button>
  </form>
  <p class="pid-lock__error" id="pid-error" role="alert"></p>
</div>

<div id="pid-content" hidden></div>

<script>
(function () {
  var P = window.__PID;
  var lock = document.getElementById('pid-lock');
  var content = document.getElementById('pid-content');
  var form = document.getElementById('pid-form');
  var input = document.getElementById('pid-password');
  var errorEl = document.getElementById('pid-error');
  var busy = false;

  function b64(s) {
    var bin = atob(s);
    var arr = new Uint8Array(bin.length);
    for (var i = 0; i < bin.length; i++) arr[i] = bin.charCodeAt(i);
    return arr;
  }

  function decrypt(password) {
    var enc = new TextEncoder();
    return crypto.subtle.importKey('raw', enc.encode(password), 'PBKDF2', false, ['deriveKey'])
      .then(function (baseKey) {
        return crypto.subtle.deriveKey(
          { name: 'PBKDF2', salt: b64(P.salt), iterations: P.iter, hash: 'SHA-256' },
          baseKey, { name: 'AES-GCM', length: 256 }, false, ['decrypt']);
      })
      .then(function (key) {
        return crypto.subtle.decrypt({ name: 'AES-GCM', iv: b64(P.iv) }, key, b64(P.ct));
      })
      .then(function (buf) {
        return JSON.parse(new TextDecoder().decode(buf));
      });
  }

  function mount(data) {
    content.innerHTML = data.html;
    var urlA = URL.createObjectURL(new Blob([data.a], { type: 'text/html' }));
    var urlB = URL.createObjectURL(new Blob([data.b], { type: 'text/html' }));
    document.getElementById('pid-demo-a').src = urlA;
    document.getElementById('pid-demo-b').src = urlB;
    document.getElementById('pid-open-a').href = urlA;
    document.getElementById('pid-open-b').href = urlB;
    lock.hidden = true;
    content.hidden = false;
  }

  form.addEventListener('submit', function (event) {
    event.preventDefault();
    if (busy) return;
    var password = input.value.trim();
    if (!password) return;
    busy = true;
    errorEl.textContent = 'Decrypting...';
    decrypt(password).then(function (data) {
      busy = false;
      errorEl.textContent = '';
      try { sessionStorage.setItem('pid-ok', password); } catch (e) {}
      mount(data);
    }).catch(function () {
      busy = false;
      errorEl.textContent = 'That password did not work. Check for stray spaces and try again.';
      input.value = '';
      input.focus();
    });
  });

  try {
    var saved = sessionStorage.getItem('pid-ok');
    if (saved) {
      decrypt(saved).then(mount).catch(function () {
        try { sessionStorage.removeItem('pid-ok'); } catch (e) {}
      });
    }
  } catch (e) {}
})();
</script>
