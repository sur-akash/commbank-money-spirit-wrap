"""
Phone-framed Money Spirit Wrap story renderer.

Renders the full 9-screen, Spotify-Wrapped-style experience for a single
customer as a self-contained HTML document, presented inside a realistic
phone mockup styled like the **CommBank retail app** (consistent with the
CommBiz "Business Spirit Wrap" layout):

  - white device "stage", iOS status bar, app header with the CommBank logo
  - story progress segments + tap-to-advance + explicit Back / Next controls
  - a retail-app bottom tab bar (Home · Pay · Wrap · Cards · More)
  - premium dark story cards: behaviour-based mascots, percentile badge,
    peak timeline, a celebratory confetti reveal, and the social share card

Used by both the Streamlit app (components.html) and the static exporter
(generate.py), so the two stay perfectly in sync.
"""
from branding import logo_img
from share_card import render_share_card

# CommBank palette
Y = "#FFCC00"
INK = "#141414"
CARD = "#FFFFFF"
LINE = "#E7E7EA"
MUTED = "#6B6B70"


# One consistent dark CommBank background across every story card.
DARK_BG = "linear-gradient(170deg, #202020 0%, #141414 46%, #0b0b0b 100%)"


DRIVER_ICON = {
    "travel": "✈️", "lifestyle": "🛍️", "food": "🍽️", "entertainment": "🎬",
    "fitness": "🏃", "saving": "🐷", "technology": "💡", "giving": "💛",
}


def _status_bar():
    c = "#FFFFFF"
    return f"""<div class="status">
      <span class="time">9:41</span>
      <span class="sicons">
        <svg width="17" height="11" viewBox="0 0 18 11"><rect x="0" y="6" width="3" height="5" rx="1" fill="{c}"/><rect x="5" y="4" width="3" height="7" rx="1" fill="{c}"/><rect x="10" y="2" width="3" height="9" rx="1" fill="{c}"/><rect x="15" y="0" width="3" height="11" rx="1" fill="{c}"/></svg>
        <svg width="16" height="11" viewBox="0 0 16 11"><path d="M8 2.5c2 0 3.8.8 5.1 2.1l1.3-1.4C13 1.6 10.6.7 8 .7S3 1.6 1.6 3.2L2.9 4.6C4.2 3.3 6 2.5 8 2.5z" fill="{c}"/><path d="M8 6c1 0 2 .4 2.7 1.1L8 10 5.3 7.1C6 6.4 7 6 8 6z" fill="{c}"/></svg>
        <svg width="25" height="12" viewBox="0 0 26 12"><rect x="1" y="1" width="21" height="10" rx="2.5" fill="none" stroke="{c}" opacity="0.5"/><rect x="3" y="3" width="15" height="6" rx="1" fill="{c}"/><rect x="23" y="4" width="2" height="4" rx="1" fill="{c}"/></svg>
      </span>
    </div>"""


def _tabbar():
    tabs = [
        ("Home", "M3 11l9-8 9 8v9a1 1 0 01-1 1h-5v-6h-6v6H4a1 1 0 01-1-1z"),
        ("Pay", "M3 6h18v12H3zM3 10h18"),
        ("Wrap", "M12 2l2.4 6.9H22l-6 4.4 2.3 7L12 16l-6.3 4.3 2.3-7-6-4.4h7.6z"),
        ("Cards", "M3 7h18v10H3zM3 11h18"),
        ("More", "M5 12h.01M12 12h.01M19 12h.01"),
    ]
    active = 2
    out = []
    for i, (label, path) in enumerate(tabs):
        on = i == active
        col = INK if on else MUTED
        fill = Y if on else "none"
        out.append(
            f"<div class='tab {'active' if on else ''}'>"
            f"<svg width='22' height='22' viewBox='0 0 24 24' fill='{fill}' stroke='{col}' "
            f"stroke-width='1.6' stroke-linejoin='round' stroke-linecap='round'><path d='{path}'/></svg>"
            f"<span style='color:{col}'>{label}</span></div>"
        )
    return f"<div class='tabbar'>{''.join(out)}</div>"


def _timeline_html(timeline, peak_month):
    peak3 = peak_month[:3]
    bars = []
    for m in timeline:
        is_peak = m["month"] == peak3
        h = max(6, m["value"] * 100)
        bars.append(
            f"<div class='bar {'peak' if is_peak else ''}'>"
            f"<span style='height:{h}%'></span><small>{m['month']}</small></div>"
        )
    return f"<div class='timeline'>{''.join(bars)}</div>"


def _cards(wrap):
    p = wrap["persona"]
    g = DARK_BG
    year = wrap["year"]
    name = wrap.get("customer_name", "there")
    traits = "".join(f"<span class='chip gold'>{t}</span>" for t in p["traits"])
    share_html = render_share_card(p, year=year, logo_html=logo_img(20))

    cards = []

    # 0 — Welcome
    cards.append(f"""
    <section class="card" data-dur="8" data-fx="particles">
      <div class="card-bg" style="background:linear-gradient(165deg,#101010,#1c1c1c 48%,#2a2a2a)"></div>
      <canvas class="fx-particles"></canvas>
      <div class="card-inner">
        <div class="spacer"></div>
        <div class="glyph float reveal-up d1" style="font-size:74px">✨</div>
        <div class="greeting reveal-up d2" style="text-align:center">Hi {name} 👋</div>
        <h1 class="reveal-up d2" style="text-align:center;margin-top:6px">Your {year}<br/>Money Spirit<br/>is ready</h1>
        <p class="sub reveal-up d3" style="text-align:center">A look back at your year through the choices, habits and moments that shaped your financial story.</p>
        <div class="spacer"></div>
        <button class="cta reveal-up d4" data-next>Start my story</button>
      </div>
    </section>""")

    # 1 — Driver
    cards.append(f"""
    <section class="card">
      <div class="card-bg" style="background:{g}"></div>
      <div class="card-inner">
        <span class="kicker reveal-up d1">Your driver</span>
        <div class="spacer"></div>
        <div class="glyph float reveal-up d2">{DRIVER_ICON.get(wrap['driver'], '✨')}</div>
        <div class="spacer"></div>
        <h2 class="reveal-up d3">{wrap['driver_label']} shaped your year</h2>
        <p class="lead reveal-up d4">{wrap['driver_copy']}</p>
      </div>
    </section>""")

    # 2 — Peak
    cards.append(f"""
    <section class="card" data-fx="timeline">
      <div class="card-bg" style="background:{g}"></div>
      <div class="card-inner">
        <span class="kicker reveal-up d1">Your peak moment</span>
        <h2 class="reveal-up d2" style="margin-top:8px">{wrap['peak_month']} was your<br/>biggest {wrap['driver_label'].lower()} month</h2>
        <div class="spacer"></div>
        <div class="reveal-up d3">{_timeline_html(wrap['timeline'], wrap['peak_month'])}</div>
        <div class="spacer"></div>
        <p class="sub reveal-up d4">That's when {wrap['driver_label'].lower()} became a major part of your year.</p>
      </div>
    </section>""")

    # 3 — Shine in the crowd
    cards.append(f"""
    <section class="card">
      <div class="card-bg" style="background:{g}"></div>
      <div class="card-inner">
        <span class="kicker reveal-up d1">Shine in the crowd</span>
        <div class="spacer"></div>
        <div class="badge reveal-up d2" style="--p:{100 - wrap['shine_band']}">
          <div class="pct">Top<br/>{wrap['shine_band']}<small>%</small></div>
          <div class="lab">of your crowd</div>
        </div>
        <div class="spacer"></div>
        <p class="lead reveal-up d3" style="text-align:center">{wrap['shine_copy']}</p>
      </div>
    </section>""")

    # 4 — Individually rewarding
    cards.append(f"""
    <section class="card">
      <div class="card-bg" style="background:{g}"></div>
      <div class="card-inner">
        <span class="kicker reveal-up d1">Rewarding you</span>
        <div class="spacer"></div>
        <div class="glyph reveal-up d2">🌱</div>
        <div class="spacer"></div>
        <h2 class="reveal-up d3">A year that paid you back</h2>
        <p class="lead reveal-up d4">{wrap['rewarding_copy']}</p>
      </div>
    </section>""")

    # 5 — Community impact
    cards.append(f"""
    <section class="card">
      <div class="card-bg" style="background:{g}"></div>
      <div class="card-inner">
        <span class="kicker reveal-up d1">Community impact</span>
        <div class="spacer"></div>
        <div class="glyph reveal-up d2">🤝</div>
        <div class="spacer"></div>
        <h2 class="reveal-up d3">Bigger than your balance</h2>
        <p class="lead reveal-up d4">{wrap['community_copy']}</p>
      </div>
    </section>""")

    # 6 — Reveal
    cards.append(f"""
    <section class="card" data-dur="11" data-fx="confetti">
      <div class="card-bg" style="background:{g}"></div>
      <canvas class="fx-confetti"></canvas>
      <div class="card-inner">
        <span class="kicker reveal-up d1" style="text-align:center">Your {year} Money Spirit is…</span>
        <div class="spacer"></div>
        <div class="mascot-stage reveal-up d2"><div class="halo"></div><div class="mascot lg float">{p['art']}</div></div>
        <div class="reveal-name reveal-up d3">{p['name']}</div>
        <div class="reveal-title reveal-up d3">{p['title']}</div>
        <div class="chips reveal-up d4" style="justify-content:center;margin-top:12px">{traits}</div>
        <p class="lead reveal-up d4" style="text-align:center;margin-top:12px;font-size:14.5px">{p['description']}</p>
        <div class="reveal-tag reveal-up d4">&ldquo;{p['tagline']}&rdquo;</div>
        <div class="spacer"></div>
      </div>
    </section>""")

    # 7 — Social share card
    cards.append(f"""
    <section class="card share">
      <div class="card-bg" style="background:{g}"></div>
      <div class="card-inner">
        <span class="kicker reveal-up d1">Share your spirit</span>
        <div class="spacer"></div>
        <div class="reveal-up d2">{share_html}</div>
        <div class="spacer"></div>
        <button class="cta reveal-up d3" data-share data-name="{p['name']}" data-tag="{p['tagline']}">Share my Money Spirit</button>
      </div>
    </section>""")

    # 8 — Next-year action plan (3 relevant actionables)
    cards.append(f"""
    <section class="card">
      <div class="card-bg" style="background:{g}"></div>
      <div class="card-inner">
        <div class="planhead reveal-up d1">
          <div class="mascot xs">{p['art']}</div>
          <div>
            <span class="kicker">Your next-year plan</span>
            <h2 style="margin:2px 0 0;font-size:21px">A head start on {year + 1}</h2>
          </div>
        </div>
        <div class="spacer"></div>
        <div class="actions">
          <div class="act reveal-up d2"><span class="actnum">1</span><p>{p['actions'][0]}</p></div>
          <div class="act reveal-up d3"><span class="actnum">2</span><p>{p['actions'][1]}</p></div>
          <div class="act reveal-up d4"><span class="actnum">3</span><p>{p['actions'][2]}</p></div>
        </div>
        <p class="sub reveal-up d4" style="margin-top:14px;text-align:center;font-size:13px">Made with care by CommBank 💛</p>
        <div class="spacer"></div>
        <button class="cta ghost reveal-up d4" data-restart>Replay my story</button>
      </div>
    </section>""")

    return cards


# --- static CSS (no f-string: keeps CSS braces literal) -------------------
_CSS = """
<style>
  :root { --cba-yellow:#FFCC00; --ink:#141414; }
  * { box-sizing:border-box; -webkit-tap-highlight-color:transparent; margin:0; }
  html, body { height:100%; }
  body { background:transparent; color:#fff; display:flex; align-items:flex-start; justify-content:center;
    font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif; }

  .stage { display:flex; justify-content:center; align-items:flex-start;
    background:#FFFFFF; max-width:460px; margin:0 auto; padding:22px 16px 26px;
    border-radius:30px; box-shadow:0 24px 70px rgba(0,0,0,.5); width:100%; }
  .fit { display:contents; }

  .phone { position:relative; width:390px; height:824px; background:#0B0B0B;
    border-radius:52px; border:12px solid #0c0c0c; overflow:hidden;
    box-shadow:0 18px 44px rgba(0,0,0,.45), inset 0 0 0 2px #2a2a2a;
    display:flex; flex-direction:column; }
  .notch { position:absolute; top:0; left:50%; transform:translateX(-50%);
    width:148px; height:28px; background:#0c0c0c; border-radius:0 0 18px 18px; z-index:50; }

  /* top app chrome */
  .topchrome { background:#0B0B0B; z-index:30; }
  .status { display:flex; justify-content:space-between; align-items:center;
    padding:13px 26px 3px; color:#fff; font-size:14px; font-weight:600; }
  .status .sicons { display:flex; gap:6px; align-items:center; }
  .appbar { display:flex; align-items:center; justify-content:space-between; padding:6px 18px 8px; }
  .appbar .brand { display:flex; align-items:center; gap:8px; color:#fff; font-weight:700; font-size:15px; }
  .appbar .brand img { border-radius:5px; }
  .appbar .close { color:#fff; opacity:.7; font-size:15px; }
  .segs { display:flex; gap:4px; padding:0 16px 9px; }
  .seg { flex:1; height:3px; border-radius:3px; background:rgba(255,255,255,.26); overflow:hidden; }
  .seg > i { display:block; height:100%; width:0; background:#fff; border-radius:3px; }
  .seg.done > i { width:100%; }
  .seg.active > i { animation:fill var(--dur,7s) linear forwards; }
  .seg.paused > i { animation-play-state:paused; }
  @keyframes fill { from {width:0} to {width:100%} }

  /* story viewport */
  .viewport { position:relative; flex:1; overflow:hidden; background:#000; }
  .tapzone { position:absolute; top:0; bottom:0; width:34%; z-index:20; cursor:pointer; }
  .tapzone.left { left:0; } .tapzone.right { right:0; width:66%; }

  .card { position:absolute; inset:0; display:flex; flex-direction:column;
    opacity:0; pointer-events:none; transform:scale(1.03);
    transition:opacity .5s ease, transform .5s ease; }
  .card.active { opacity:1; pointer-events:auto; transform:scale(1); }
  .card-bg { position:absolute; inset:0; z-index:0; }
  .card-bg::after { content:""; position:absolute; inset:0;
    background:radial-gradient(120% 75% at 50% -8%, rgba(255,204,0,.16), transparent 58%); }
  .card-inner { position:relative; z-index:2; display:flex; flex-direction:column;
    height:100%; padding:24px 24px 22px; overflow-y:auto; color:#fff; }

  h1 { font-size:29px; line-height:1.12; margin-bottom:14px; font-weight:800; letter-spacing:-.4px; color:#fff; }
  h2 { font-size:24px; line-height:1.18; margin-bottom:12px; font-weight:800; letter-spacing:-.3px; color:#fff; }
  h3 { color:#fff; }
  .greeting { color:var(--cba-yellow); font-weight:800; font-size:18px; letter-spacing:.2px; }
  .lead { font-size:16.5px; line-height:1.5; color:rgba(255,255,255,.94); }
  .sub { font-size:14.5px; line-height:1.5; color:rgba(255,255,255,.7); }
  .kicker { font-size:11px; color:var(--cba-yellow); font-weight:700; letter-spacing:.16em; text-transform:uppercase; }
  .spacer { flex:1 0 auto; min-height:6px; }
  .reveal-up { opacity:0; transform:translateY(16px); }
  .card.active .reveal-up { animation:up .7s cubic-bezier(.2,.7,.2,1) forwards; }
  .card.active .d1 { animation-delay:.12s; } .card.active .d2 { animation-delay:.28s; }
  .card.active .d3 { animation-delay:.44s; } .card.active .d4 { animation-delay:.6s; }
  @keyframes up { to { opacity:1; transform:translateY(0); } }

  .glyph { font-size:104px; line-height:1; text-align:center; filter:drop-shadow(0 14px 30px rgba(0,0,0,.45)); }
  .glyph.float, .mascot.float { animation:floaty 4s ease-in-out infinite; }
  @keyframes floaty { 0%,100% {transform:translateY(0)} 50% {transform:translateY(-10px)} }

  .mascot { margin:0 auto; filter:drop-shadow(0 16px 26px rgba(0,0,0,.4)); }
  .mascot svg, .mascot img { width:100%; height:100%; display:block; object-fit:contain; }
  .mascot.lg { width:172px; height:172px; }
  .mascot.xs { width:46px; height:46px; margin:0; filter:none; flex:0 0 auto; }

  /* reveal mascot with a soft golden spotlight halo */
  .mascot-stage { position:relative; width:200px; height:188px; margin:0 auto; display:flex; align-items:center; justify-content:center; }
  .mascot-stage .mascot.lg { position:relative; z-index:2; margin:0; }
  .halo { position:absolute; width:188px; height:188px; border-radius:50%; z-index:1;
    background:radial-gradient(circle, rgba(255,204,0,.34) 0%, rgba(255,204,0,.12) 45%, transparent 70%);
    animation:halo 3.5s ease-in-out infinite; }
  @keyframes halo { 0%,100% {transform:scale(1);opacity:.9} 50% {transform:scale(1.08);opacity:1} }

  .chips { display:flex; flex-wrap:wrap; gap:8px; }
  .chip { padding:7px 13px; border-radius:999px; font-size:13.5px; font-weight:700;
    background:rgba(255,255,255,.14); border:1px solid rgba(255,255,255,.22); }
  .chip.gold { background:var(--cba-yellow); color:#000; border-color:transparent; }

  .badge { align-self:center; width:176px; height:176px; border-radius:50%;
    display:flex; flex-direction:column; align-items:center; justify-content:center;
    background:conic-gradient(var(--cba-yellow) calc(var(--p,88)*1%), rgba(255,255,255,.14) 0); position:relative; }
  .badge::before { content:""; position:absolute; inset:11px; border-radius:50%; background:rgba(0,0,0,.55); }
  .badge .pct { position:relative; font-size:42px; font-weight:900; letter-spacing:-1px; text-align:center; line-height:1; }
  .badge .pct small { font-size:19px; font-weight:800; }
  .badge .lab { position:relative; font-size:11px; color:rgba(255,255,255,.66); text-transform:uppercase; letter-spacing:.12em; margin-top:6px; }

  .timeline { display:flex; align-items:flex-end; gap:6px; height:168px; padding:8px 2px 0; }
  .bar { flex:1; display:flex; flex-direction:column; align-items:center; gap:6px; height:100%; justify-content:flex-end; }
  .bar > span { display:block; width:100%; border-radius:6px 6px 3px 3px; background:rgba(255,255,255,.22);
    transition:height .8s cubic-bezier(.2,.7,.2,1); }
  .bar.peak > span { background:var(--cba-yellow); box-shadow:0 0 22px rgba(255,204,0,.6); }
  .bar small { font-size:9px; color:rgba(255,255,255,.66); }
  .bar.peak small { color:var(--cba-yellow); font-weight:800; }

  .reveal-name { font-size:31px; font-weight:900; letter-spacing:-.6px; text-align:center; margin:6px 0 2px; }
  .reveal-title { text-align:center; color:var(--cba-yellow); font-weight:800; font-size:13px; letter-spacing:.14em; text-transform:uppercase; }
  .reveal-tag { text-align:center; font-style:italic; font-size:15px; color:rgba(255,255,255,.9); margin-top:10px; }

  .planhead { display:flex; gap:12px; align-items:center; }
  .actions { display:flex; flex-direction:column; gap:10px; width:100%; }
  .act { display:flex; gap:12px; align-items:center; background:rgba(255,255,255,.07);
    border:1px solid rgba(255,204,0,.22); border-radius:14px; padding:13px 14px; }
  .act p { font-size:14px; color:#fff; line-height:1.35; font-weight:500; }
  .actnum { flex:0 0 auto; width:26px; height:26px; border-radius:50%;
    background:var(--cba-yellow); color:#000; font-weight:800; font-size:14px;
    display:flex; align-items:center; justify-content:center; }

  .cta { appearance:none; border:0; cursor:pointer; width:100%; padding:15px; border-radius:15px;
    font-size:15.5px; font-weight:800; background:var(--cba-yellow); color:#000;
    box-shadow:0 10px 26px rgba(255,204,0,.28); }
  .cta.ghost { background:rgba(255,255,255,.12); color:#fff; box-shadow:none; }
  .cta:active { transform:translateY(1px); }

  .fx-particles { position:absolute; inset:0; z-index:1; }
  .fx-confetti { position:absolute; inset:0; z-index:40; pointer-events:none; }

  /* share screen: fit the Instagram card inside the phone */
  .card.share .card-inner { padding:16px 14px 18px; }
  .card.share .igc-card { width:288px; padding:20px 18px 18px; }
  .card.share .igc-head { font-size:23px; }
  .card.share .igc-orbit { width:194px; height:194px; }
  .card.share .igc-circle { width:140px; height:140px; }
  .card.share .igc-mascot { width:114px; height:114px; }
  .card.share .igc-cta { padding:12px 16px; font-size:14px; margin-top:16px; }

  /* bottom controls + retail tab bar (CommBank app chrome) */
  .controls { display:flex; align-items:center; justify-content:space-between;
    padding:9px 16px; background:#fff; border-top:1px solid #E7E7EA; z-index:30; }
  .navp { border:1px solid #E7E7EA; background:#fff; color:#141414; border-radius:999px;
    padding:8px 16px; font-weight:700; font-size:13.5px; cursor:pointer; }
  .navp.primary { background:var(--cba-yellow); border-color:var(--cba-yellow); color:#000; }
  .navp:disabled { opacity:.4; cursor:default; }
  .counter { font-size:12px; color:#6B6B70; font-weight:700; letter-spacing:1px; }
  .tabbar { display:flex; justify-content:space-around; padding:8px 8px 20px;
    background:#fff; border-top:1px solid #E7E7EA; z-index:30; }
  .tab { display:flex; flex-direction:column; align-items:center; gap:3px; font-size:10px; font-weight:600; }
  .tab.active span { color:#141414; }
</style>
"""

_JS = """
<script>
(function(){
  const cards = Array.from(document.querySelectorAll('.card'));
  const N = cards.length;
  const prog = document.getElementById('progress');
  prog.innerHTML = cards.map(()=>'<div class="seg"><i></i></div>').join('');
  const segs = Array.from(document.querySelectorAll('.seg'));
  const counter = document.getElementById('counter');
  const prevBtn = document.getElementById('prev');
  const nextBtn = document.getElementById('next');
  let idx = 0, timer = null;

  function show(n){
    idx = Math.max(0, Math.min(N-1, n));
    cards.forEach((c,i)=> c.classList.toggle('active', i===idx));
    segs.forEach((s,i)=>{ s.classList.remove('active','done','paused');
      s.querySelector('i').style.animation='none'; if(i<idx) s.classList.add('done'); });
    const seg = segs[idx];
    const dur = parseFloat(cards[idx].dataset.dur||'7');
    requestAnimationFrame(()=>{ seg.style.setProperty('--dur', dur+'s');
      seg.querySelector('i').style.animation=''; seg.classList.add('active'); });
    clearTimeout(timer);
    timer = setTimeout(()=>{ if(idx<N-1) show(idx+1); }, dur*1000);
    counter.textContent = (idx+1)+' / '+N;
    prevBtn.disabled = idx===0; nextBtn.textContent = idx===N-1 ? 'Done' : 'Next ›';
    const fx = cards[idx].dataset.fx;
    if(fx==='particles') initParticles();
    if(fx==='timeline') animateTimeline();
    if(fx==='confetti'){ fireConfetti(); if(navigator.vibrate) navigator.vibrate([8,40,8]); }
  }
  function next(){ if(idx<N-1) show(idx+1); }
  function prev(){ if(idx>0) show(idx-1); }

  document.getElementById('tapL').addEventListener('click', prev);
  document.getElementById('tapR').addEventListener('click', next);
  prevBtn.addEventListener('click', prev);
  nextBtn.addEventListener('click', next);
  document.addEventListener('keydown', e=>{ if(e.key==='ArrowRight') next(); if(e.key==='ArrowLeft') prev(); });
  document.addEventListener('click', e=>{
    const t = e.target.closest('[data-next],[data-restart],[data-share]');
    if(!t) return; e.stopPropagation();
    if(t.hasAttribute('data-next')) next();
    else if(t.hasAttribute('data-restart')) show(0);
    else if(t.hasAttribute('data-share')) shareSpirit(t.dataset.name, t.dataset.tag);
  });
  document.querySelector('.viewport').addEventListener('pointerdown', ()=>{ const s=segs[idx]; if(s) s.classList.add('paused'); clearTimeout(timer); });
  document.querySelector('.viewport').addEventListener('pointerup', ()=>{ const s=segs[idx]; if(!s) return; s.classList.remove('paused');
    const dur=parseFloat(cards[idx].dataset.dur||'7'); clearTimeout(timer);
    timer=setTimeout(()=>{ if(idx<N-1) show(idx+1); }, dur*1000*0.5); });

  function shareSpirit(name, tag){
    const text = 'My CommBank Money Spirit is the '+name+' — "'+tag+'" ✨ #MoneySpiritWrap';
    if(navigator.share){ navigator.share({title:'My Money Spirit', text}).catch(()=>{}); }
    else { try{ navigator.clipboard.writeText(text); }catch(e){} alert('Copied to share:\\n\\n'+text); }
  }
  function animateTimeline(){
    document.querySelectorAll('.timeline .bar > span').forEach(s=>{
      const h=s.style.height; s.style.height='0'; requestAnimationFrame(()=> s.style.height=h); });
  }
  function initParticles(){
    const cv=document.querySelector('.card.active .fx-particles'); if(!cv) return;
    const ctx=cv.getContext('2d'); const r=cv.getBoundingClientRect();
    cv.width=r.width; cv.height=r.height; const pts=[];
    for(let i=0;i<70;i++) pts.push({x:Math.random()*cv.width,y:Math.random()*cv.height,
      r:Math.random()*2+0.6,s:Math.random()*0.5+0.15,o:Math.random()*0.5+0.3});
    cancelAnimationFrame(window._pf);
    (function loop(){ ctx.clearRect(0,0,cv.width,cv.height);
      pts.forEach(p=>{ p.y-=p.s; if(p.y<-4){p.y=cv.height+4;p.x=Math.random()*cv.width;}
        ctx.beginPath(); ctx.arc(p.x,p.y,p.r,0,7); ctx.fillStyle='rgba(255,204,0,'+p.o+')'; ctx.fill(); });
      window._pf=requestAnimationFrame(loop); })();
  }
  function fireConfetti(){
    const cv=document.querySelector('.card.active .fx-confetti'); if(!cv) return;
    const ctx=cv.getContext('2d'); const r=cv.getBoundingClientRect();
    cv.width=r.width; cv.height=r.height;
    const cols=['#FFCC00','#fff','#FFD84D','#F2B800']; const conf=[];
    for(let i=0;i<140;i++) conf.push({x:cv.width/2,y:cv.height*0.3,vx:(Math.random()-0.5)*8,
      vy:Math.random()*-9-3,g:0.22+Math.random()*0.12,s:Math.random()*7+3,c:cols[i%4],rot:Math.random()*6,vr:(Math.random()-0.5)*0.4});
    cancelAnimationFrame(window._cf);
    (function loop(){ ctx.clearRect(0,0,cv.width,cv.height); let alive=false;
      conf.forEach(p=>{ p.vy+=p.g; p.x+=p.vx; p.y+=p.vy; p.rot+=p.vr; if(p.y<cv.height+20) alive=true;
        ctx.save(); ctx.translate(p.x,p.y); ctx.rotate(p.rot); ctx.fillStyle=p.c;
        ctx.fillRect(-p.s/2,-p.s/2,p.s,p.s*0.6); ctx.restore(); });
      if(alive) window._cf=requestAnimationFrame(loop); })();
  }

  // scale the phone to fit the host container width (Streamlit column / mobile)
  function fit(){
    const stage=document.querySelector('.stage'); const phone=document.querySelector('.phone');
    if(!stage||!phone) return;
    const avail=Math.max(220, stage.clientWidth - 32);
    phone.style.zoom = Math.min(1, avail/390);
  }
  window.addEventListener('resize', fit); fit();
  show(0);
})();
</script>
"""


def render_story(wrap, *, full_document=True):
    """Return the full phone-framed story HTML for one customer's wrap."""
    cards_html = "".join(_cards(wrap))
    brand = logo_img(24)
    body = f"""
    <div class="stage"><div class="fit">
      <div class="phone">
        <div class="notch"></div>
        <div class="topchrome">
          {_status_bar()}
          <div class="appbar">
            <div class="brand">{brand}<span>Money Spirit Wrap</span></div>
            <div class="close">✕</div>
          </div>
          <div class="segs" id="progress"></div>
        </div>
        <div class="viewport">
          <div class="tapzone left" id="tapL"></div>
          <div class="tapzone right" id="tapR"></div>
          {cards_html}
        </div>
        <div class="controls">
          <button class="navp" id="prev">‹ Back</button>
          <div class="counter" id="counter">1 / 9</div>
          <button class="navp primary" id="next">Next ›</button>
        </div>
        {_tabbar()}
      </div>
    </div></div>
    {_JS}
    """
    if not full_document:
        return _CSS + body
    return f"""<!DOCTYPE html><html lang="en"><head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no"/>
<meta name="theme-color" content="#000000"/>
<title>CommBank · Money Spirit Wrap {wrap['year']}</title>
{_CSS}</head><body>{body}</body></html>"""
