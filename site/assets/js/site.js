(function () {
  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => [...r.querySelectorAll(s)];
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const S = window.SCHOOL;
  const PHONE = '8275204302';

  /* ---------- Icons ---------- */
  const ICONS = {
    book: 'M4 5c3-1 6-1 8 1 2-2 5-2 8-1v13c-3-1-6-1-8 1-2-2-5-2-8-1zM12 6v13',
    flask: 'M9 3h6M10 3v6l-5 9a2 2 0 002 3h10a2 2 0 002-3l-5-9V3M7 15h10',
    chip: 'M7 7h10v10H7zM10 10h4v4h-4zM9 3v4M15 3v4M9 17v4M15 17v4M3 9h4M3 15h4M17 9h4M17 15h4',
    bed: 'M3 19V6M3 15h18v4M21 15v-3a3 3 0 00-3-3h-7v6',
    fork: 'M7 3v8a2 2 0 002 2v8M5 3v6M9 3v6M17 21V3c-3 2-3 7-3 9h3',
    dome: 'M4 20v-7a8 8 0 0116 0v7M2 20h20M12 2v3M9 20v-4a3 3 0 016 0v4',
    ball: 'M12 3a9 9 0 100 18 9 9 0 000-18zM12 3v18M3 12h18',
    cross: 'M9 3h6v6h6v6h-6v6H9v-6H3V9h6z',
    plane: 'M3 12l18-8-6 16-3-7z',
    leaf: 'M5 20c0-9 5-15 15-16 0 10-6 15-14 15M5 20l7-7',
    target: 'M12 3a9 9 0 100 18 9 9 0 000-18zM12 7a5 5 0 100 10 5 5 0 000-10zM12 11a1 1 0 100 2 1 1 0 000-2z',
    palette: 'M12 3a9 9 0 100 18c1.5 0 2-1 1.5-2-.6-1.2.2-2.5 1.6-2.5H17a4 4 0 004-4c0-5-4-9.5-9-9.5zM7.5 11a1 1 0 100-2 1 1 0 000 2zM11 7.5a1 1 0 100-2 1 1 0 000 2zM15.5 9a1 1 0 100-2 1 1 0 000 2z',
    mic: 'M12 3a3 3 0 00-3 3v5a3 3 0 006 0V6a3 3 0 00-3-3zM5 11a7 7 0 0014 0M12 18v3',
    trophy: 'M8 4h8v6a4 4 0 01-8 0zM8 6H4v2a3 3 0 003 3M16 6h4v2a3 3 0 01-3 3M12 14v4M8 21h8M10 18h4',
    users: 'M9 11a3 3 0 100-6 3 3 0 000 6zM3 20v-1a5 5 0 0110 0v1M17 11a2.5 2.5 0 100-5M16 14a4 4 0 015 4v2',
    shield: 'M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6zM9 12l2 2 4-4',
    cap: 'M2 9l10-5 10 5-10 5zM6 11.5V16c0 1.5 3 3 6 3s6-1.5 6-3v-4.5M22 9v6',
    cal: 'M4 6h16v14H4zM4 10h16M8 3v4M16 3v4',
    phone: 'M5 4h4l2 5-2.5 1.5a11 11 0 005 5L15 13l5 2v4a2 2 0 01-2 2A16 16 0 013 6a2 2 0 012-2z',
    mail: 'M3 5h18v14H3zM3 6l9 7 9-7',
    pin: 'M12 21s7-6 7-11a7 7 0 10-14 0c0 5 7 11 7 11zM12 12a2 2 0 100-4 2 2 0 000 4z',
    chat: 'M4 5h16v11H9l-5 4z',
    play: 'M8 5v14l11-7z',
    camera: 'M3 8h4l2-3h6l2 3h4v12H3zM12 17a4 4 0 100-8 4 4 0 000 8z',
    arrow: 'M5 12h14M13 6l6 6-6 6',
    check: 'M5 12l5 5 9-10',
    sun: 'M12 8a4 4 0 100 8 4 4 0 000-8zM12 2v3M12 19v3M2 12h3M19 12h3M5 5l2 2M17 17l2 2M19 5l-2 2M7 17l-2 2',
    music: 'M9 18V6l10-2v12M9 18a3 3 0 11-6 0 3 3 0 016 0zM19 16a3 3 0 11-6 0 3 3 0 016 0z',
    heart: 'M12 20s-8-5-8-11a4.5 4.5 0 018-2.5A4.5 4.5 0 0120 9c0 6-8 11-8 11z',
    globe: 'M12 3a9 9 0 100 18 9 9 0 000-18zM3 12h18M12 3c3 3 3 15 0 18M12 3c-3 3-3 15 0 18',
    star: 'M12 3l2.7 5.8 6.3.8-4.6 4.4 1.2 6.3L12 17.2 6.4 20.3l1.2-6.3L3 9.6l6.3-.8z',
    menu: 'M4 7h16M4 12h16M4 17h16',
    x: 'M6 6l12 12M18 6L6 18',
    down: 'M6 9l6 6 6-6',
    clock: 'M12 3a9 9 0 100 18 9 9 0 000-18zM12 7v5l3 2',
    moon: 'M20 14a8 8 0 11-10-10 6 6 0 0010 10z',
    download: 'M12 4v11M7 11l5 5 5-5M5 20h14',
    info: 'M12 3a9 9 0 100 18 9 9 0 000-18zM12 11v6M12 7.5v.5',
    palette2: 'M4 4h16v16H4zM4 12h16M12 4v16'
  };
  const FILLED = ['play'];
  const sprite = '<svg width="0" height="0" style="position:absolute" aria-hidden="true">' +
    Object.entries(ICONS).map(([k, d]) => `<symbol id="i-${k}" viewBox="0 0 24 24"><path d="${d}"${FILLED.includes(k) ? ' fill="currentColor"' : ''}/></symbol>`).join('') + '</svg>';
  document.body.insertAdjacentHTML('afterbegin', sprite);
  const ic = (n, c = '') => `<svg class="ic ${c}" aria-hidden="true"><use href="#i-${n}"/></svg>`;
  window.aiicon = ic;

  /* ---------- Header / footer ---------- */
  const NAV = [
    { t: 'About', h: 'about.html', c: [['Vision & Mission', 'about.html#vision'], ['Our Story & Heritage', 'about.html#history'], ['Leadership', 'about.html#leadership'], ['Chairman’s Message', 'about.html#message'], ['Anjuman-I-Islam Network', 'about.html#network']] },
    { t: 'Academics', h: 'academics.html', c: [['Overview', 'academics.html'], ['School & Jr. College', 'academics.html#programmes'], ['Competitive Coaching', 'academics.html#coaching'], ['Labs & Digital Learning', 'academics.html#facilities'], ['Faculty & Staff', 'academics.html#faculty']] },
    { t: 'Boarding Life', h: 'boarding.html', c: [['Boarding & Care', 'boarding.html'], ['A Day at Panchgani', 'boarding.html#day'], ['Extracurricular Activities', 'activities.html'], ['Student Journey', 'student-journey.html'], ['Photo Gallery', 'gallery.html']] },
    { t: 'Results', h: 'results.html', c: [['Exam Results & Rankings', 'results.html'], ['Achievements & Awards', 'achievements.html']] },
    { t: 'Admissions', h: 'admissions.html', c: [['Enrolment Process', 'admissions.html#process'], ['Fees Policy', 'admissions.html#fees'], ['FAQs', 'admissions.html#faq'], ['Enquire Now', 'admissions.html#enquire'], ['School Calendar', 'calendar.html']] },
    { t: 'Contact', h: 'contact.html', c: [['Contact Us', 'contact.html'], ['Careers', 'contact.html#careers']] }
  ];
  const page = location.pathname.split('/').pop() || 'index.html';
  const isCur = (n) => n.h === page || n.c.some(([, u]) => u.split('#')[0] === page);

  const hdr = $('#site-header');
  if (hdr) hdr.innerHTML = `
    <a class="skip" href="#main">Skip to content</a>
    <div class="util"><div class="container">
      <div><span class="tag">ADMISSIONS OPEN</span>Boarding school &amp; Jr. College · Panchgani</div>
      <div class="r"><a href="#">Parent Login</a><a href="calendar.html">Calendar</a><a href="contact.html#careers">Careers</a><a href="#">Download Prospectus</a><a href="tel:${PHONE}">${PHONE} / 8275205404</a></div>
    </div></div>
    <header class="hdr"><div class="container">
      <a class="brand" href="index.html"><span class="logo-ph">LOGO<br>HERE</span><span><b>Anjuman-I-Islam</b><small>Public School &amp; Jr. College · Panchgani</small></span></a>
      <button class="menu-btn" aria-label="Menu" aria-expanded="false">${ic('menu')}</button>
      <ul class="nav">${NAV.map(n => `<li class="${isCur(n) ? 'cur' : ''}"><a href="${n.h}">${n.t}${ic('down')}</a><div class="dd">${n.c.map(([t, u]) => `<a href="${u}">${t}</a>`).join('')}</div></li>`).join('')}</ul>
      <a class="btn accent" href="admissions.html#enquire">Apply Now</a>
    </div></header>`;
  const mb = $('.menu-btn');
  if (mb) mb.addEventListener('click', () => {
    const o = document.body.classList.toggle('nav-open');
    mb.setAttribute('aria-expanded', o);
    mb.innerHTML = ic(o ? 'x' : 'menu');
  });

  const ftr = $('#site-footer');
  if (ftr) ftr.innerHTML = `
    <footer class="ftr"><div class="container">
      <div class="grid">
        <div>
          <a class="brand" href="index.html"><span class="logo-ph" style="color:#fff;border-color:var(--accent-l)">LOGO<br>HERE</span><span><b>Anjuman-I-Islam</b><small>Public School &amp; Jr. College · Panchgani</small></span></a>
          <p style="margin-top:18px;max-width:320px">A residential school and junior college on 174 acres in Panchgani — over a century of academic excellence, character development and global citizenship.</p>
          <div class="affil"><span class="logo-ph">AFFIL.<br>LOGO</span><span class="logo-ph">BOARD<br>LOGO</span><span class="logo-ph">ANJUMAN<br>LOGO</span></div>
        </div>
        <div><h5>School</h5><ul><li><a href="about.html">About Us</a></li><li><a href="about.html#vision">Vision &amp; Mission</a></li><li><a href="academics.html">Academics</a></li><li><a href="boarding.html">Boarding Life</a></li><li><a href="activities.html">Activities</a></li></ul></div>
        <div><h5>Results</h5><ul><li><a href="results.html">Exam Rankings</a></li><li><a href="achievements.html">Achievements</a></li><li><a href="student-journey.html">Student Journey</a></li><li><a href="gallery.html">Gallery</a></li><li><a href="calendar.html">Calendar</a></li></ul></div>
        <div><h5>Admissions</h5><ul><li><a href="admissions.html#process">Process</a></li><li><a href="admissions.html#fees">Fees Policy</a></li><li><a href="admissions.html#faq">FAQs</a></li><li><a href="contact.html#careers">Careers</a></li><li><a href="#">Parent Login</a></li></ul></div>
        <div class="contact"><h5>Contact</h5><ul>
          <li>${ic('pin')}<span>Panchgani, Maharashtra<br>(full address to be added)</span></li>
          <li>${ic('phone')}<span>${PHONE} / 8275205404</span></li>
          <li>${ic('mail')}<span>info@anjumanislampublicschoolpanchgani.in</span></li></ul></div>
      </div>
      <div class="legal"><span>© 2026 Anjuman-I-Islam Public School &amp; Jr. College, Panchgani. All rights reserved.</span><span>Design mockup · placeholder logos, photos and figures</span></div>
    </div></footer>
    <div class="fab"><a class="wa" href="https://wa.me/91${PHONE}" aria-label="WhatsApp">${ic('chat')}<span>WhatsApp</span></a><a class="en" href="admissions.html#enquire" aria-label="Enquire now">${ic('mail')}<span>Enquire Now</span></a></div>
    <div class="themer"><button aria-expanded="false">${ic('palette')} Theme</button><div class="panel"><b>Preview design theme</b>
      ${[['heritage', 'Heritage', ['#0f4c3a', '#c9a24b']], ['modern', 'Modern Global', ['#1d4ed8', '#0d9488']], ['vibrant', 'Vibrant Explorer', ['#0e7a5f', '#ffc933']], ['hillstation', 'Hill Station', ['#1f3a2e', '#b5651d']]].map(([k, n, c]) => `<button data-th="${k}"><span class="sw"><i style="background:${c[0]}"></i><i style="background:${c[1]}"></i></span>${n}</button>`).join('')}
    </div></div>`;

  /* ---------- Theme switcher ---------- */
  const qt = new URLSearchParams(location.search).get('theme');
  if (qt) document.documentElement.dataset.theme = qt;
  const themer = $('.themer');
  if (themer) {
    const mark = () => $$('[data-th]', themer).forEach(b => b.classList.toggle('on', b.dataset.th === document.documentElement.dataset.theme));
    mark();
    $('button', themer).addEventListener('click', e => { themer.classList.toggle('open'); e.currentTarget.setAttribute('aria-expanded', themer.classList.contains('open')); });
    $$('[data-th]', themer).forEach(b => b.addEventListener('click', () => {
      document.documentElement.dataset.theme = b.dataset.th;
      try { localStorage.setItem('aiips-theme', b.dataset.th); } catch (e) {}
      mark();
    }));
  }

  /* ---------- Photo placeholders ---------- */
  $$('[data-ph]').forEach(el => {
    if (el.classList.contains('bgph')) { el.insertAdjacentHTML('beforeend', `<span>Photo placeholder · ${el.dataset.ph}</span>`); return; }
    el.classList.add('ph');
    el.innerHTML = `<figcaption>${ic('camera')}<span>Photo placeholder</span><b>${el.dataset.ph}</b></figcaption>`;
  });

  /* ---------- Sliders ---------- */
  $$('[data-slider]').forEach(root => {
    const items = $$('[data-slide]', root);
    const dots = $('[data-dots]', root);
    let i = 0, timer;
    if (dots) dots.innerHTML = items.map((_, k) => `<button aria-label="Go to slide ${k + 1}"></button>`).join('');
    const go = n => {
      i = (n + items.length) % items.length;
      items.forEach((s, k) => s.classList.toggle('active', k === i));
      if (dots) $$('button', dots).forEach((d, k) => d.classList.toggle('on', k === i));
    };
    const play = () => { const ms = +root.dataset.slider; if (ms && !reduce) { clearInterval(timer); timer = setInterval(() => go(i + 1), ms); } };
    if (dots) $$('button', dots).forEach((d, k) => d.addEventListener('click', () => { go(k); play(); }));
    const p = $('[data-prev]', root), n = $('[data-next]', root);
    if (p) p.addEventListener('click', () => { go(i - 1); play(); });
    if (n) n.addEventListener('click', () => { go(i + 1); play(); });
    root.addEventListener('mouseenter', () => clearInterval(timer));
    root.addEventListener('mouseleave', play);
    go(0); play();
  });

  /* ---------- Tabs ---------- */
  function initTabs(root) {
    const btns = $$('[data-tab-btn]', root), panels = $$('[data-tab-panel]', root);
    const show = id => {
      btns.forEach(b => b.setAttribute('aria-selected', b.dataset.tabBtn === id));
      panels.forEach(p => { p.hidden = p.dataset.tabPanel !== id; });
    };
    btns.forEach(b => b.addEventListener('click', () => show(b.dataset.tabBtn)));
    const first = (location.hash && btns.find(b => '#' + b.dataset.tabBtn === location.hash)) || btns[0];
    if (first) show(first.dataset.tabBtn);
  }

  /* ---------- Exam data renderers ---------- */
  const val = '<span class="val">00</span>';
  const tiles = $('#exam-tiles');
  if (tiles) tiles.innerHTML = S.exams.slice(0, 5).map(e => `<a class="card exam-tile reveal" href="results.html#${e.id}"><b>${e.n}</b><span>${e.full}</span>${val}<small style="display:block;margin-top:6px;font-size:.7rem;letter-spacing:.1em;text-transform:uppercase;color:var(--muted)">Selections</small></a>`).join('');

  const res = $('#results-root');
  if (res) {
    res.setAttribute('data-tabs', '');
    res.innerHTML = `<div class="tabbar" role="tablist">${S.exams.map(e => `<button role="tab" data-tab-btn="${e.id}">${e.n}</button>`).join('')}</div>` +
      S.exams.map(e => `<div data-tab-panel="${e.id}">
        <div class="split wide-l" style="align-items:start"><div><h3>${e.n} — ${e.full}</h3><p style="color:var(--muted);margin-top:8px">${e.desc}</p></div></div>
        <div class="kpis"><div class="kpi"><b>${val}</b><span>Appeared</span></div><div class="kpi"><b>${val}</b><span>Qualified</span></div><div class="kpi"><b>${val}</b><span>${e.metric}</span></div><div class="kpi"><b>${val}%</b><span>75%+ scorers</span></div></div>
        <div class="tbl-wrap"><table class="tbl"><thead><tr><th>Year</th><th>Appeared</th><th>Qualified</th><th>${e.metric}</th><th>Distinctions</th></tr></thead><tbody>
          ${S.years.map(y => `<tr><td><b>${y}</b></td><td>${val}</td><td>${val}</td><td>${val}</td><td>${val}</td></tr>`).join('')}</tbody></table></div>
        <h4 style="margin:40px 0 18px">Top performers — ${e.n}</h4>
        <div class="grid g4">${[1, 2, 3, 4].map(k => `<div class="card topper flat"><div class="ph p${k + 1}" data-ph="Student photo"></div><b>Student name</b><p style="font-size:.85rem">${e.n} · ${e.metric.split(' / ')[0]} ${val}</p></div>`).join('')}</div>
      </div>`).join('');
    initTabs(res);
  }

  /* ---------- Calendar ---------- */
  const cal = $('#calendar-root');
  if (cal) {
    const T = S.types;
    cal.innerHTML = `<div class="legend" data-filters data-target="#calendar-root .month li"><div class="tabbar"><button class="on" data-filter="all">All</button>${Object.entries(T).map(([k, v]) => `<button data-filter="${k}">${v}</button>`).join('')}</div></div>
      <div class="cal-grid">${S.calendar.map(([m, ev]) => `<div class="month reveal"><h3>${m}</h3><ul>${ev.map(([d, t, k]) => `<li data-cat="${k}" data-t="${k}"><b>${d}</b><span>${t}</span></li>`).join('')}</ul></div>`).join('')}</div>`;
  }

  /* ---------- Filters ---------- */
  $$('[data-filters]').forEach(g => {
    const target = g.dataset.target;
    $$('[data-filter]', g).forEach(b => b.addEventListener('click', () => {
      $$('[data-filter]', g).forEach(x => x.classList.toggle('on', x === b));
      $$(target).forEach(it => { it.hidden = !(b.dataset.filter === 'all' || it.dataset.cat.split(' ').includes(b.dataset.filter)); });
    }));
  });

  /* ---------- Generic tabs ---------- */
  $$('[data-tabs]').forEach(r => { if (r.id !== 'results-root') initTabs(r); });

  /* ---------- Forms ---------- */
  $$('form[data-demo]').forEach(f => f.addEventListener('submit', e => {
    e.preventDefault();
    if (!f.checkValidity()) { f.reportValidity(); return; }
    f.outerHTML = `<div class="form-ok" role="status"><h3>Thank you</h3><p>Demo only — no data was sent. In the live site this enquiry will reach the admissions office.</p></div>`;
  }));

  /* ---------- Counters & reveal ---------- */
  const io = new IntersectionObserver(es => es.forEach(en => {
    if (!en.isIntersecting) return;
    const el = en.target; io.unobserve(el);
    el.classList.add('in');
    if (el.dataset.count) {
      const end = +el.dataset.count, suf = el.dataset.suffix || '';
      if (reduce) { el.textContent = end + suf; return; }
      const t0 = performance.now();
      (function tick(t) { const p = Math.min((t - t0) / 1400, 1); el.textContent = Math.round(end * (1 - Math.pow(1 - p, 3))) + suf; if (p < 1) requestAnimationFrame(tick); })(t0);
    }
  }), { threshold: .2 });
  $$('.reveal,[data-count],.bars').forEach(el => io.observe(el));
})();
