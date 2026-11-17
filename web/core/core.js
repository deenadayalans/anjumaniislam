(() => {
  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => [...r.querySelectorAll(s)];
  const root = document.documentElement;
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const fine = matchMedia('(pointer:fine)').matches;

  /* ---- load + page transitions ---- */
  setTimeout(() => root.classList.add('loaded'), 60);
  if (/[?&]static/.test(location.search)) root.classList.add('loaded', 'is-static');
  if (/[?&]solo/.test(location.search)) root.classList.add('is-solo');
  addEventListener('pageshow', e => { if (e.persisted) { root.classList.remove('leaving'); root.classList.add('loaded'); } });
  document.addEventListener('click', e => {
    const a = e.target.closest('a[href]');
    if (!a || !$('.curtain') || e.metaKey || e.ctrlKey || e.shiftKey || a.target === '_blank' || a.hasAttribute('download')) return;
    const u = new URL(a.href, location.href);
    if (u.origin !== location.origin || (u.pathname === location.pathname && u.hash) || u.protocol === 'tel:' || u.protocol === 'mailto:') return;
    if (reduce) return;
    e.preventDefault();
    root.classList.add('leaving');
    setTimeout(() => { location.href = a.href; }, 520);
  });

  /* ---- header, progress ---- */
  const header = $('[data-header]');
  const prog = $('.progress i');
  let lastY = scrollY, hacc = 0;
  const onScroll = () => {
    const y = scrollY, h = document.documentElement.scrollHeight - innerHeight;
    if (prog) prog.style.transform = `scaleX(${h > 0 ? y / h : 0})`;
    if (header) {
      header.classList.toggle('scrolled', y > 40);
      if (header.hasAttribute('data-hide')) {
        const dy = y - lastY;
        if (Math.sign(dy) !== Math.sign(hacc)) hacc = 0;
        hacc += dy;
        if (y < 200 || hacc < -40) header.classList.remove('hide');
        else if (hacc > 60) header.classList.add('hide');
      }
    }
    lastY = y;
    parallax();
    lines();
  };

  /* ---- parallax + scroll-drawn lines ---- */
  const par = $$('[data-par]');
  function parallax() {
    if (reduce || root.classList.contains('is-static')) return;
    par.forEach(el => {
      const r = el.getBoundingClientRect();
      if (r.bottom < -200 || r.top > innerHeight + 200) return;
      const s = parseFloat(el.dataset.par) || .15;
      const y = (r.top + r.height / 2 - innerHeight / 2) * s * -1;
      el.style.transform = `translate3d(0,${y.toFixed(1)}px,0)${el.dataset.parScale ? ` scale(${el.dataset.parScale})` : ''}`;
    });
  }
  const lns = $$('[data-line]');
  function lines() {
    lns.forEach(l => {
      const r = l.getBoundingClientRect();
      const p = Math.min(1, Math.max(0, (innerHeight * .6 - r.top) / r.height));
      l.style.setProperty('--p', p.toFixed(3));
    });
  }
  addEventListener('scroll', onScroll, { passive: true });
  addEventListener('resize', onScroll);

  /* ---- split text ---- */
  $$('[data-split]').forEach(el => {
    const walk = n => {
      [...n.childNodes].forEach(c => {
        if (c.nodeType === 3) {
          const frag = document.createDocumentFragment();
          c.textContent.split(/(\s+)/).forEach(t => {
            if (!t) return;
            if (/^\s+$/.test(t)) { frag.append(' '); return; }
            const w = document.createElement('span'); w.className = 'w';
            const i = document.createElement('span'); i.textContent = t; w.append(i); frag.append(w);
          });
          c.replaceWith(frag);
        } else if (c.nodeType === 1) walk(c);
      });
    };
    walk(el);
    $$('.w', el).forEach((w, i) => w.style.setProperty('--i', i));
  });

  /* ---- stagger + intersection observer ---- */
  $$('[data-stagger]').forEach(p => [...p.children].forEach((c, i) => { if (!c.hasAttribute('data-i')) c.dataset.i = i % 8; }));
  $$('[data-r]').forEach(el => { el.style.setProperty('--i', el.dataset.i || 0); });
  const counted = new WeakSet();
  const count = el => {
    if (counted.has(el)) return; counted.add(el);
    const end = parseFloat(el.dataset.count), dec = (el.dataset.count.split('.')[1] || '').length;
    if (reduce || root.classList.contains('is-static')) { el.textContent = end.toLocaleString('en-IN', { minimumFractionDigits: dec }); return; }
    const t0 = performance.now(), d = 1600;
    (function tick(t) {
      const p = Math.min((t - t0) / d, 1), e = 1 - Math.pow(1 - p, 4);
      el.textContent = (end * e).toLocaleString('en-IN', { minimumFractionDigits: dec, maximumFractionDigits: dec });
      if (p < 1) requestAnimationFrame(tick);
    })(t0);
  };
  const io = new IntersectionObserver(es => es.forEach(en => {
    if (!en.isIntersecting) return;
    const el = en.target; io.unobserve(el);
    el.classList.add('is-in');
    $$('[data-count]', el).forEach(count);
    if (el.dataset.count) count(el);
  }), { threshold: .14, rootMargin: '0px 0px -4% 0px' });
  $$('[data-r],[data-split],.bar,[data-count],[data-in]').forEach(el => io.observe(el));

  /* ---- hover effects ---- */
  if (fine && !reduce) {
    document.addEventListener('mousemove', e => {
      const s = e.target.closest('[data-spot]');
      if (s) { const r = s.getBoundingClientRect(); s.style.setProperty('--mx', (e.clientX - r.left) + 'px'); s.style.setProperty('--my', (e.clientY - r.top) + 'px'); }
      const t = e.target.closest('[data-tilt]');
      if (t) { const r = t.getBoundingClientRect(); const x = (e.clientX - r.left) / r.width - .5, y = (e.clientY - r.top) / r.height - .5; t.style.transform = `perspective(900px) rotateY(${x * 8}deg) rotateX(${-y * 8}deg) translateZ(0)`; }
    });
    document.addEventListener('mouseout', e => { const t = e.target.closest('[data-tilt]'); if (t && !t.contains(e.relatedTarget)) t.style.transform = ''; });
    $$('[data-mag]').forEach(b => {
      b.addEventListener('mousemove', e => { const r = b.getBoundingClientRect(); b.style.transform = `translate(${(e.clientX - r.left - r.width / 2) * .25}px,${(e.clientY - r.top - r.height / 2) * .35}px)`; });
      b.addEventListener('mouseleave', () => { b.style.transform = ''; });
    });
    if (document.body.hasAttribute('data-cursor')) {
      const c = document.createElement('div'); c.className = 'cursor'; document.body.append(c);
      let x = 0, y = 0, tx = 0, ty = 0;
      addEventListener('mousemove', e => { tx = e.clientX; ty = e.clientY; });
      (function loop() { x += (tx - x) * .2; y += (ty - y) * .2; c.style.left = x + 'px'; c.style.top = y + 'px'; requestAnimationFrame(loop); })();
      document.addEventListener('mouseover', e => c.classList.toggle('is-hover', !!e.target.closest('a,button,[data-hover],summary,input,select,textarea')));
    }
  }

  /* ---- nav toggle ---- */
  const nt = $('[data-nav-toggle]');
  if (nt) nt.addEventListener('click', () => { const o = document.body.classList.toggle('nav-open'); nt.setAttribute('aria-expanded', o); });
  $$('.nav a').forEach(a => a.addEventListener('click', () => setTimeout(() => {
    // Keep the menu open while the page wipe covers it; closing it first exposes the old page.
    if (!root.classList.contains('leaving')) document.body.classList.remove('nav-open');
  })));

  /* ---- sliders ---- */
  $$('[data-slider]').forEach(r => {
    const items = $$('[data-slide]', r), dots = $('[data-dots]', r);
    let i = 0, timer;
    if (dots) dots.innerHTML = items.map((_, k) => `<button aria-label="Slide ${k + 1}"></button>`).join('');
    const go = n => { i = (n + items.length) % items.length; items.forEach((s, k) => s.classList.toggle('active', k === i)); if (dots) $$('button', dots).forEach((d, k) => d.classList.toggle('on', k === i)); r.style.setProperty('--slide', i); };
    const play = () => { clearInterval(timer); const ms = +r.dataset.slider; if (ms && !reduce) timer = setInterval(() => go(i + 1), ms); };
    if (dots) $$('button', dots).forEach((d, k) => d.addEventListener('click', () => { go(k); play(); }));
    const p = $('[data-prev]', r), n = $('[data-next]', r);
    if (p) p.addEventListener('click', () => { go(i - 1); play(); });
    if (n) n.addEventListener('click', () => { go(i + 1); play(); });
    r.addEventListener('mouseenter', () => clearInterval(timer)); r.addEventListener('mouseleave', play);
    go(0); play();
  });

  /* ---- tabs ---- */
  $$('[data-tabs]').forEach(t => {
    const btns = $$('[data-tab]', t), panes = $$('[data-pane]', t);
    const show = id => { btns.forEach(b => { const on = b.dataset.tab === id; b.classList.toggle('on', on); b.setAttribute('aria-selected', on); }); panes.forEach(p => { p.hidden = p.dataset.pane !== id; if (!p.hidden) $$('[data-r]', p).forEach(e => e.classList.add('is-in')); }); };
    btns.forEach(b => b.addEventListener('click', () => show(b.dataset.tab)));
    show(btns[0].dataset.tab);
  });

  /* ---- filters (activities, calendar, gallery) ---- */
  $$('[data-filter-group]').forEach(g => {
    const ex = g.closest('[data-explorer]');
    if (ex) return;
    const sel = g.dataset.target || g.dataset.items;
    if (!sel) return;
    const scope = g.closest('section') || document;
    $$('[data-filter]', g).forEach(b => b.addEventListener('click', () => {
      $$('[data-filter]', g).forEach(x => x.classList.toggle('on', x === b));
      $$(sel, scope).forEach(it => {
        const show = b.dataset.filter === 'all' || (it.dataset.cat || '').split(' ').includes(b.dataset.filter);
        it.hidden = !show;
        if (show) it.classList.add('is-in');
      });
    }));
  });
  /* institutions explorer: category + search */
  $$('[data-explorer]').forEach(ex => {
    const rows = $$('tbody tr', ex), out = $('[data-out]', ex), q = $('[data-search]', ex);
    let cat = 'all';
    const apply = () => {
      const t = (q.value || '').trim().toLowerCase(); let n = 0;
      rows.forEach(r => { const s = (cat === 'all' || r.dataset.cat === cat) && (!t || r.dataset.text.includes(t)); r.hidden = !s; if (s) n++; });
      out.textContent = n;
    };
    $$('[data-filter]', ex).forEach(b => b.addEventListener('click', () => { cat = b.dataset.filter; $$('[data-filter]', ex).forEach(x => x.classList.toggle('on', x === b)); apply(); }));
    q.addEventListener('input', apply);
  });

  /* ---- rails (drag to scroll) ---- */
  $$('.rail').forEach(r => {
    let down = false, sx = 0, sl = 0, moved = false;
    r.addEventListener('pointerdown', e => { if (e.pointerType !== 'mouse') return; down = true; moved = false; sx = e.clientX; sl = r.scrollLeft; r.classList.add('drag'); });
    addEventListener('pointerup', () => { down = false; r.classList.remove('drag'); });
    addEventListener('pointermove', e => { if (!down) return; const dx = e.clientX - sx; if (Math.abs(dx) > 4) moved = true; r.scrollLeft = sl - dx; });
    r.addEventListener('click', e => { if (moved) e.preventDefault(); }, true);
  });

  /* ---- forms ---- */
  $$('form[data-demo]').forEach(f => f.addEventListener('submit', e => {
    e.preventDefault();
    if (!f.checkValidity()) { f.reportValidity(); return; }
    const ok = document.createElement('div'); ok.className = 'form-ok'; ok.setAttribute('role', 'status');
    ok.innerHTML = '<h3>Thank you</h3><p>This is a design demo, so nothing was sent. On the live site this enquiry goes to the admissions office.</p>';
    if (f.hasAttribute('data-confetti') && !reduce) {
      const cols = getComputedStyle(root).getPropertyValue('--confetti').split(',').map(s => s.trim()).filter(Boolean);
      for (let i = 0; i < 70; i++) { const c = document.createElement('i'); c.className = 'confetti'; c.style.left = (Math.random() * 100) + 'vw'; c.style.background = cols[i % cols.length] || '#fc3'; c.style.setProperty('--dx', (Math.random() * 200 - 100) + 'px'); c.style.animationDelay = (Math.random() * .5) + 's'; document.body.append(c); setTimeout(() => c.remove(), 2600); }
    }
    f.replaceWith(ok);
  }));

  /* ---- aerial: scroll-driven zoom in / zoom out over a label-free satellite map (Leaflet + Esri World Imagery) ---- */
  const cl = (v, lo = 0, hi = 1) => Math.min(hi, Math.max(lo, v));
  const es = t => t * t * (3 - 2 * t);
  $$('[data-aerial]').forEach(a => {
    const el = $('[data-leaflet]', a);
    if (!el || !window.L) return;
    const ll = L.latLng(+el.dataset.lat, +el.dataset.lng);
    const map = L.map(el, { zoomControl: false, dragging: false, scrollWheelZoom: false, doubleClickZoom: false, boxZoom: false, keyboard: false, touchZoom: false, tap: false, minZoom: 11, maxZoom: 19, zoomSnap: 0, zoomAnimation: false, fadeAnimation: false, markerZoomAnimation: false });
    map.attributionControl.setPrefix(false);
    const TILES = 'https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}';
    /* the map is never empty mid-zoom: stitched coarse "posters" sit under the detailed tiles and scale with the map */
    map.createPane('under').style.zIndex = 150;
    const POSTERS = [[13, 12.4, 11], [15, 14.4, 14.4]];
    const fallback = ([n, , lo]) => L.tileLayer(TILES, { minNativeZoom: n, maxNativeZoom: n, minZoom: lo, maxZoom: 19, keepBuffer: 2 }).addTo(map);
    L.tileLayer(TILES, { minNativeZoom: 17, maxNativeZoom: 17, minZoom: 16.4, maxZoom: 19, keepBuffer: 2 }).addTo(map);
    L.tileLayer(TILES, { maxZoom: 19, maxNativeZoom: 18, keepBuffer: 6, attribution: 'Imagery © Esri, Maxar, Earthstar Geographics' }).addTo(map);
    const pin = `<span class="lp-wrap"><i class="lp-radar"><b></b><b></b><b></b></i><i class="lp-dot"></i><span class="lp-tag"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 21s7-6 7-11a7 7 0 10-14 0c0 5 7 11 7 11zM12 12a2 2 0 100-4 2 2 0 000 4z"/></svg>${el.dataset.label}</span></span>`;
    L.marker(ll, { icon: L.divIcon({ className: 'lp', html: pin, iconSize: [0, 0] }), interactive: false, keyboard: false }).addTo(map);
    el._map = map;
    const title = $('.aerial-in', a), caps = $$('.aerial-cap', a), cue = $('.aerial-cue', a), lv = $$('[data-lv]', a), toggle = $('[data-map-toggle]', a);
    /* campus (17) -> in to street level (18) -> hold -> out to the whole hill station (12.6) */
    const zoomAt = p => p < .1 ? 17 : p < .36 ? 17 + es((p - .1) / .26) : p < .5 ? 18 : p < .88 ? 18 - 5.4 * es((p - .5) / .38) : 12.6;
    const offAt = p => 1 - es(cl((p - .08) / .24));
    let live = false, lastKey = '', W = el.clientWidth, H = el.clientHeight;
    function render(p) {
      const z = zoomAt(p), f = offAt(p), w = W, h = H;
      const key = z.toFixed(3) + '|' + f.toFixed(3);
      if (key === lastKey) { overlays(p, z); return; }
      lastKey = key;
      const c = map.project(ll, z).add([w > 900 ? -w * .16 * f : 0, h * .1 * f]);
      map.setView(map.unproject(c, z), z, { animate: false });
      overlays(p, z);
    }
    function overlays(p, z) {
      title.style.opacity = 1 - cl((p - .08) / .14); title.style.transform = `translateY(${(-cl(p / .25) * 50).toFixed(0)}px)`;
      caps.forEach(cp => { const v = cl((p - +cp.dataset.in) / .06) * (1 - cl((p - +cp.dataset.out) / .06)); cp.style.opacity = v.toFixed(3); cp.style.transform = `translateY(${((1 - v) * 24).toFixed(0)}px)`; });
      cue.style.opacity = 1 - cl(p / .04);
      const k = z > 16 ? 0 : z > 14.2 ? 1 : 2; lv.forEach((s, i) => s.classList.toggle('on', i === k));
    }
    const prog = () => { const r = a.getBoundingClientRect(); return cl(-r.top / Math.max(1, r.height - innerHeight)); };
    const fixed = new URLSearchParams(location.search).get('a');
    if (fixed !== null) { render(cl(parseFloat(fixed))); return; }
    let cur = prog(), tgt = cur, raf = 0;
    const loop = () => { cur += (tgt - cur) * (reduce ? 1 : .22); if (Math.abs(tgt - cur) < .0004) cur = tgt; if (!live) render(cur); raf = cur !== tgt ? requestAnimationFrame(loop) : 0; };
    const kick = () => { tgt = prog(); if (!raf) raf = requestAnimationFrame(loop); };
    addEventListener('scroll', kick, { passive: true });
    addEventListener('resize', () => { W = el.clientWidth; H = el.clientHeight; map.invalidateSize(); lastKey = ''; kick(); if (!live) render(cur); });
    render(cur);
    /* stitch each poster from a grid of tiles covering what the scroll will reveal, then show it as an image under the map */
    const buildPoster = ([n, ez]) => new Promise(done => {
      const c = map.project(ll, n), k = Math.pow(2, n - ez), hw = W * k / 2 + 256, hh = H * k / 2 + 256, max = Math.pow(2, n);
      const x0 = Math.max(0, Math.floor((c.x - hw) / 256)), x1 = Math.min(max - 1, Math.floor((c.x + hw) / 256));
      const y0 = Math.max(0, Math.floor((c.y - hh) / 256)), y1 = Math.min(max - 1, Math.floor((c.y + hh) / 256));
      const cv = document.createElement('canvas'); cv.width = (x1 - x0 + 1) * 256; cv.height = (y1 - y0 + 1) * 256;
      const g = cv.getContext('2d'), jobs = [];
      for (let x = x0; x <= x1; x++) for (let y = y0; y <= y1; y++) jobs.push([x, y]);
      let ok = 0, left = jobs.length;
      const finish = () => {
        if (ok < jobs.length * .9) return done(false);
        try {
          cv.toBlob(b => {
            if (!b) return done(false);
            const sw = map.unproject([x0 * 256, (y1 + 1) * 256], n), ne = map.unproject([(x1 + 1) * 256, y0 * 256], n);
            L.imageOverlay(URL.createObjectURL(b), L.latLngBounds(sw, ne), { pane: 'under', interactive: false }).addTo(map);
            done(true);
          });
        } catch (e) { done(false); }
      };
      const load = ([x, y]) => { const im = new Image(); im.crossOrigin = 'anonymous'; im.onload = () => { g.drawImage(im, (x - x0) * 256, (y - y0) * 256); ok++; step(); }; im.onerror = step; im.src = TILES.replace('{z}', n).replace('{y}', y).replace('{x}', x); };
      let next = 0;
      const step = () => { if (--left === 0) return finish(); if (next < jobs.length) load(jobs[next++]); };
      for (let i = 0; i < 6 && next < jobs.length; i++) load(jobs[next++]);
    });
    const warm = async () => {
      if (navigator.connection && navigator.connection.saveData) { POSTERS.forEach(fallback); return; }
      for (const p of POSTERS) if (!(await buildPoster(p))) fallback(p);
    };
    if (document.readyState === 'complete') setTimeout(warm, 600); else addEventListener('load', () => setTimeout(warm, 600));
    toggle.addEventListener('click', () => {
      live = a.classList.toggle('is-live');
      toggle.textContent = live ? 'Back to the scroll story' : 'Explore the map';
      ['dragging', 'scrollWheelZoom', 'doubleClickZoom', 'touchZoom', 'boxZoom', 'keyboard'].forEach(k => map[k][live ? 'enable' : 'disable']());
      if (live) { el._zc = L.control.zoom({ position: 'bottomleft' }).addTo(map); } else { if (el._zc) el._zc.remove(); render(cur); }
    });
  });

  /* ---- scroll-driven day clock ---- */
  const hx = h => { h = h.replace('#', ''); return [0, 2, 4].map(i => parseInt(h.slice(i, i + 2), 16)); };
  const mix = (a, b, t) => a.map((v, i) => Math.round(v + (b[i] - v) * t));
  const rgb = a => `rgb(${a[0]},${a[1]},${a[2]})`;
  const lum = a => (.2126 * a[0] + .7152 * a[1] + .0722 * a[2]) / 255;
  const ease = t => t * t * (3 - 2 * t);
  const clamp = (v, a = 0, b = 1) => Math.min(b, Math.max(a, v));
  $$('[data-dayclock]').forEach(rootEl => {
    const st = JSON.parse(rootEl.dataset.stages);
    const sky = JSON.parse(rootEl.dataset.sky).map(k => ({ t: k[0], a1: hx(k[1]), a2: hx(k[2]) }));
    /* one scroll segment per stage, or per sub-step when a stage has them (school hours) */
    const segs = []; st.forEach((S, i) => { if (S.subs) S.subs.forEach((b, j) => segs.push({ ...b, i, j })); else segs.push({ s: S.s, e: S.e, w: S.w, i, j: -1 }); });
    const total = segs.reduce((a, s) => a + s.w, 0), cum = []; let acc = 0; segs.forEach(s => { cum.push(acc); acc += s.w; });
    const stage = $('.dc-stage', rootEl), panels = $$('.dc-panel', rootEl), bars = $$('.seg', rootEl), mark = $('[data-mark]', rootEl);
    const hh = $('[data-hand-h]', rootEl), mm = $('[data-hand-m]', rootEl), ring = $('[data-ring]', rootEl), orb = $('[data-orb]', rootEl);
    const tEl = $('[data-dc-time]', rootEl), apEl = $('[data-dc-ampm]', rootEl), lab = $('[data-dc-label]', rootEl);
    const kick = panels.map(p => $('.dc-kicker', p).textContent), subLis = panels.map(p => $$('.dc-sub li', p)), subTxt = panels.map(p => $('.dc-subtext', p));
    const sunEl = $('.dc-orb.sun', rootEl), moonEl = $('.dc-orb.moon', rootEl);
    const T0 = st[0].s, fixed = new URLSearchParams(location.search).get('p');
    let last = -1, lastJ = -2, SW = stage.clientWidth, SH = stage.clientHeight;
    addEventListener('resize', () => { SW = stage.clientWidth; SH = stage.clientHeight; });
    if (fixed === null) rootEl.style.height = (total * 46 + 100) + 'vh';
    const progress = () => { const r = rootEl.getBoundingClientRect(); return clamp(-r.top / Math.max(1, r.height - innerHeight)); };
    const skyAt = T => { let k = 0; while (k < sky.length - 2 && T >= sky[k + 1].t) k++; const u = ease(clamp((T - sky[k].t) / (sky[k + 1].t - sky[k].t))); return [mix(sky[k].a1, sky[k + 1].a1, u), mix(sky[k].a2, sky[k + 1].a2, u)]; };
    const arc = (T, a, b) => { const u = (T - a) / (b - a); return u < 0 || u > 1 ? null : { x: u * 100, y: 86 - Math.sin(Math.PI * u) * 64, o: Math.pow(Math.sin(Math.PI * u), .45) }; };
    function render(p) {
      const x = p * total; let k = 0; while (k < segs.length - 1 && x >= cum[k] + segs[k].w) k++;
      const sg = segs[k], t = clamp((x - cum[k]) / sg.w), T = sg.s + (sg.e - sg.s) * t, i = sg.i, j = sg.j;
      const [c1, c2] = skyAt(T), L = lum(mix(c1, c2, .5)), night = clamp((.46 - L) / .3), S = stage.style, dark = [4, 8, 16];
      S.setProperty('--sky1', rgb(c1)); S.setProperty('--sky2', rgb(c2)); S.setProperty('--night', night.toFixed(3));
      S.setProperty('--hill1', rgb(mix(mix(c2, [60, 86, 70], .45), dark, night * .55)));
      S.setProperty('--hill2', rgb(mix(mix(c2, [34, 62, 50], .6), dark, night * .6)));
      S.setProperty('--hill3', rgb(mix(mix(c2, [20, 40, 32], .78), dark, night * .65)));
      rootEl.dataset.mode = L < .5 ? 'dark' : 'light';
      const sun = arc(T, 5.5, 18.5), moon = arc(T < 12 ? T + 24 : T, 17.5, 30.5);
      sunEl.style.transform = `translate3d(${((sun ? sun.x : 50) / 100 * SW).toFixed(1)}px,${((sun ? sun.y : 110) / 100 * SH).toFixed(1)}px,0) translate(-50%,-50%)`; sunEl.style.opacity = sun ? sun.o.toFixed(3) : 0;
      moonEl.style.transform = `translate3d(${((moon ? moon.x : 50) / 100 * SW).toFixed(1)}px,${((moon ? moon.y : 110) / 100 * SH).toFixed(1)}px,0) translate(-50%,-50%)`; moonEl.style.opacity = moon ? moon.o.toFixed(3) : 0;
      const h24 = T % 24, H = Math.floor(h24), M = (h24 - H) * 60;
      hh.setAttribute('transform', `rotate(${((H % 12) + M / 60) * 30} 110 110)`);
      mm.setAttribute('transform', `rotate(${M * 6} 110 110)`);
      tEl.textContent = `${H % 12 || 12}:${String(Math.floor(M)).padStart(2, '0')}`; apEl.textContent = H < 12 ? 'AM' : 'PM';
      const f = (T - T0) / 24; ring.style.strokeDashoffset = (666 * (1 - f)).toFixed(1);
      const ang = f * Math.PI * 2 - Math.PI / 2; orb.setAttribute('transform', `translate(${(110 + 106 * Math.cos(ang)).toFixed(1)} ${(110 + 106 * Math.sin(ang)).toFixed(1)})`);
      rootEl.classList.toggle('night', night > .5);
      if (i !== last) { panels.forEach((pn, n) => pn.classList.toggle('on', n === i)); bars.forEach((b, n) => b.classList.toggle('on', n === i)); last = i; lastJ = -2; }
      if (j !== lastJ) {
        lastJ = j; const li = subLis[i];
        if (li.length) { li.forEach((l, n) => l.classList.toggle('on', n === j)); if (j >= 0) { subTxt[i].textContent = li[j].dataset.text; lab.textContent = $('span', li[j]).textContent; } }
        else lab.textContent = kick[i];
      }
      const S2 = st[i], b = bars[i]; mark.style.transform = `translateX(${(b.offsetLeft + b.offsetWidth * clamp((T - S2.s) / (S2.e - S2.s))).toFixed(1)}px)`;
    }
    bars.forEach((b, n) => b.addEventListener('click', () => {
      const idx = segs.findIndex(q => q.i === n), r = rootEl.getBoundingClientRect(), span = r.height - innerHeight;
      scrollTo({ top: scrollY + r.top + (cum[idx] / total) * span + 4, behavior: reduce ? 'auto' : 'smooth' });
    }));
    if (fixed !== null) { render(clamp(parseFloat(fixed))); if (!root.classList.contains('is-solo')) setTimeout(() => rootEl.scrollIntoView({ block: 'start', behavior: 'instant' }), 50); return; }
    let cur = progress(), tgt = cur, raf = 0;
    const loop = () => { cur += (tgt - cur) * (reduce ? 1 : .22); if (Math.abs(tgt - cur) < .0003) cur = tgt; render(cur); raf = cur !== tgt ? requestAnimationFrame(loop) : 0; };
    addEventListener('scroll', () => { tgt = progress(); if (!raf) raf = requestAnimationFrame(loop); }, { passive: true });
    addEventListener('resize', () => { tgt = progress(); if (!raf) raf = requestAnimationFrame(loop); });
    render(cur);
  });

  /* ---- collage: shuffled, jittered 2x2 so the cards sit differently on every visit; overlaps stay thin so labels are never covered ---- */
  $$('[data-collage]').forEach(c => {
    const tiles = $$('.tile', c); if (tiles.length !== 4) return;
    const r = (a, b) => a + Math.random() * (b - a), h = 1.1;
    const sx = r(45, 55), ly = r(50, 62), ry = r(46, 58), off = r(1, 7), a = r(0, 4), b = r(0, 3);
    const slots = [
      { l: 0, t: 0, w: sx + h, ht: ly + h, s: 'l' },
      { l: sx - h, t: off, w: 100 - sx + h, ht: ry - off + h, s: 'r' },
      { l: a, t: ly - h, w: sx + h - a, ht: 100 - ly + h - r(0, 3), s: 'l' },
      { l: sx - h + b, t: ry - h, w: 100 - sx + h - b, ht: 100 - ry + h, s: 'r' }
    ];
    const order = [0, 1, 2, 3].sort(() => Math.random() - .5);
    slots.forEach((s, k) => {
      const t = tiles[order[k]], st = t.style, sign = k === 0 || k === 3 ? -1 : 1;
      st.left = s.l + '%'; st.top = s.t + '%'; st.width = s.w + '%'; st.height = s.ht + '%'; st.right = 'auto'; st.bottom = 'auto';
      st.transform = `rotate(${(sign * r(1.5, 4.5)).toFixed(1)}deg)`; t.dataset.side = s.s;
    });
    const spin = $('.spin', c);
    if (spin) { spin.style.left = `calc(${sx}% - ${spin.offsetWidth / 2}px)`; spin.style.top = `calc(${(ly + ry) / 2}% - ${spin.offsetHeight / 2}px)`; }
  });

  /* ---- rotating words ---- */
  $$('[data-rotate]').forEach(el => {
    const words = el.dataset.rotate.split('|'); let i = 0;
    el.textContent = '';
    const s = document.createElement('span'); s.className = 'rot'; s.textContent = words[0]; el.append(s);
    if (reduce) return;
    setInterval(() => {
      s.classList.add('out');
      setTimeout(() => { i = (i + 1) % words.length; s.textContent = words[i]; s.classList.remove('out'); s.classList.add('in'); requestAnimationFrame(() => requestAnimationFrame(() => s.classList.remove('in'))); }, 380);
    }, 2600);
  });

  $$('[data-year]').forEach(e => { e.textContent = new Date().getFullYear(); });
  onScroll();
})();
