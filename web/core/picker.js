/* Colour + font picker. Reads window.PAL (written by the inline script in <head>); the choice is remembered per design. */
(() => {
  const PAL = window.PAL, root = document.documentElement;
  if ('serviceWorker' in navigator && location.protocol !== 'file:') navigator.serviceWorker.register(new URL('../sw.js', location.href).href).catch(() => { });
  if (!PAL || !(PAL.list.length > 1 || PAL.f.length > 1)) return;
  const box = document.createElement('div'); box.className = 'pal';
  const btn = document.createElement('button'); btn.type = 'button'; btn.className = 'pal-btn'; btn.setAttribute('aria-expanded', 'false');
  const pop = document.createElement('div'); pop.className = 'pal-pop'; pop.hidden = true;
  const dots = c => '<span class="pal-sw">' + c.map(x => `<i style="background:${x}"></i>`).join('') + '</span>';
  const curP = () => PAL.list.find(p => p.id === root.dataset.palette) || PAL.list[0];
  const curF = () => PAL.f.find(f => f.id === root.dataset.font) || PAL.f[0];
  const paint = () => { btn.innerHTML = dots(curP().c) + '<b>Style</b>'; pop.querySelectorAll('button').forEach(b => b.classList.toggle('on', b.dataset.k === 'p' ? b.dataset.id === curP().id : b.dataset.id === curF().id)); };
  const group = (title, items, kind) => {
    const h = document.createElement('h6'); h.textContent = title; pop.appendChild(h);
    items.forEach(it => {
      const b = document.createElement('button'); b.type = 'button'; b.dataset.id = it.id; b.dataset.k = kind;
      b.innerHTML = (kind === 'p' ? dots(it.c) : '<span class="pal-aa">Aa</span>') + '<em>' + it.n + '</em>';
      b.addEventListener('click', () => {
        if (kind === 'p') { root.dataset.palette = it.id; try { localStorage.setItem('pal-' + PAL.k, it.id); } catch (e) { } }
        else {
          if (it.u && !document.querySelector('link[href="' + it.u + '"]')) { const l = document.createElement('link'); l.rel = 'stylesheet'; l.href = it.u; document.head.appendChild(l); }
          root.dataset.font = it.id; try { localStorage.setItem('fnt-' + PAL.k, it.id); } catch (e) { }
        }
        paint();
      });
      pop.appendChild(b);
    });
  };
  if (PAL.list.length > 1) group('Colours', PAL.list, 'p');
  if (PAL.f.length > 1) group('Fonts', PAL.f, 'f');
  /* app mode: full screen where the browser allows it, install to the home screen otherwise */
  const standalone = matchMedia('(display-mode: standalone)').matches || navigator.standalone;
  if (!standalone) {
    const ios = /iPad|iPhone|iPod/.test(navigator.userAgent) || (navigator.platform === 'MacIntel' && navigator.maxTouchPoints > 1);
    const app = document.createElement('div'); pop.appendChild(app);
    let installEvt = null;
    const fsOn = () => !!(document.fullscreenElement || document.webkitFullscreenElement);
    const renderApp = () => {
      app.innerHTML = '<h6>App</h6>';
      const row = (label, fn) => { const b = document.createElement('button'); b.type = 'button'; b.innerHTML = '<span class="pal-aa">\u2197</span><em>' + label + '</em>'; b.addEventListener('click', fn); app.appendChild(b); };
      if (document.fullscreenEnabled || document.webkitFullscreenEnabled) row(fsOn() ? 'Exit full screen' : 'Full screen', () => { (fsOn() ? (document.exitFullscreen || document.webkitExitFullscreen).call(document) : (root.requestFullscreen || root.webkitRequestFullscreen).call(root)); });
      if (installEvt) row('Install app', () => { installEvt.prompt(); installEvt = null; renderApp(); });
      if (!installEvt) { const p = document.createElement('p'); p.className = 'pal-hint'; p.textContent = ios ? 'For a full-screen app: tap Share, then Add to Home Screen.' : 'For a full-screen app: browser menu, then Install app or Add to Home screen.'; app.appendChild(p); }
    };
    addEventListener('beforeinstallprompt', e => { e.preventDefault(); installEvt = e; renderApp(); });
    document.addEventListener('fullscreenchange', renderApp); document.addEventListener('webkitfullscreenchange', renderApp);
    renderApp();
  }
  const shut = () => { pop.hidden = true; btn.setAttribute('aria-expanded', 'false'); };
  btn.addEventListener('click', e => { e.stopPropagation(); pop.hidden = !pop.hidden; btn.setAttribute('aria-expanded', String(!pop.hidden)); });
  document.addEventListener('click', e => { if (!box.contains(e.target)) shut(); });
  document.addEventListener('keydown', e => { if (e.key === 'Escape') shut(); });
  box.append(pop, btn); document.body.appendChild(box); paint();
})();
