import base64, sys, html, pathlib

out = pathlib.Path(sys.argv[1])
mascot = base64.b64encode(pathlib.Path(sys.argv[2]).read_bytes()).decode()
FONT = "-apple-system,BlinkMacSystemFont,'Segoe UI','Apple SD Gothic Neo','Noto Sans KR','Malgun Gothic',Helvetica,Arial,sans-serif"
MONO = "'SF Mono','JetBrains Mono',Menlo,Consolas,monospace"

header = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="340" viewBox="0 0 1200 340">
<defs>
  <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="#0b1220"/><stop offset="0.55" stop-color="#0f2236"/><stop offset="1" stop-color="#1a1f3d"/>
  </linearGradient>
  <radialGradient id="o1"><stop offset="0" stop-color="#4A90B8" stop-opacity="0.55"/><stop offset="1" stop-color="#4A90B8" stop-opacity="0"/></radialGradient>
  <radialGradient id="o2"><stop offset="0" stop-color="#8B5CF6" stop-opacity="0.45"/><stop offset="1" stop-color="#8B5CF6" stop-opacity="0"/></radialGradient>
  <radialGradient id="o3"><stop offset="0" stop-color="#22d3ee" stop-opacity="0.35"/><stop offset="1" stop-color="#22d3ee" stop-opacity="0"/></radialGradient>
  <pattern id="grid" width="32" height="32" patternUnits="userSpaceOnUse">
    <path d="M32 0H0V32" fill="none" stroke="#ffffff" stroke-opacity="0.045"/>
  </pattern>
  <linearGradient id="name" x1="0" x2="1">
    <stop offset="0" stop-color="#e6f1ff"/><stop offset="0.5" stop-color="#8ecbf0"/><stop offset="1" stop-color="#b9a4ff"/>
  </linearGradient>
  <clipPath id="r"><rect width="1200" height="340" rx="22"/></clipPath>
  <style>
    .o1{{animation:f1 9s ease-in-out infinite}} .o2{{animation:f2 11s ease-in-out infinite}} .o3{{animation:f1 13s ease-in-out infinite reverse}}
    @keyframes f1{{0%,100%{{transform:translate(0,0)}}50%{{transform:translate(60px,-25px)}}}}
    @keyframes f2{{0%,100%{{transform:translate(0,0)}}50%{{transform:translate(-70px,30px)}}}}
    .m{{animation:bob 3.2s ease-in-out infinite}} @keyframes bob{{0%,100%{{transform:translateY(0)}}50%{{transform:translateY(-10px)}}}}
    .cur{{animation:blink 1s steps(1) infinite}} @keyframes blink{{50%{{opacity:0}}}}
    .in{{animation:in .8s ease-out backwards}} .d1{{animation-delay:.2s}} .d2{{animation-delay:.55s}} .d3{{animation-delay:.9s}} .d4{{animation-delay:1.25s}}
    @keyframes in{{from{{opacity:0;transform:translateY(10px)}}}}
    .tw{{animation:tw 2.4s ease-in-out infinite}} @keyframes tw{{0%,100%{{opacity:.15}}50%{{opacity:.9}}}}
  </style>
</defs>
<g clip-path="url(#r)">
  <rect width="1200" height="340" fill="url(#bg)"/>
  <rect width="1200" height="340" fill="url(#grid)"/>
  <circle class="o1" cx="180" cy="60" r="260" fill="url(#o1)"/>
  <circle class="o2" cx="1000" cy="300" r="280" fill="url(#o2)"/>
  <circle class="o3" cx="640" cy="20" r="200" fill="url(#o3)"/>
  <g fill="#cfe8ff">
    <circle class="tw" cx="560" cy="70" r="1.6"/><circle class="tw" style="animation-delay:.7s" cx="720" cy="270" r="1.4"/>
    <circle class="tw" style="animation-delay:1.3s" cx="1130" cy="60" r="1.8"/><circle class="tw" style="animation-delay:.4s" cx="820" cy="110" r="1.2"/>
    <circle class="tw" style="animation-delay:1.9s" cx="420" cy="300" r="1.5"/><circle class="tw" style="animation-delay:1s" cx="90" cy="280" r="1.3"/>
  </g>
  <rect x="0.5" y="0.5" width="1199" height="339" rx="22" fill="none" stroke="#ffffff" stroke-opacity="0.08"/>

  <g font-family="{MONO}">
    <text x="72" y="96" font-size="20" fill="#7ee0a1">$ <tspan fill="#9fb3c8">whoami</tspan></text>
  </g>
  <text x="70" y="168" font-family="{FONT}" font-size="64" font-weight="800" fill="url(#name)" letter-spacing="-1">Sangwook Park</text>
  <text x="72" y="214" font-family="{FONT}" font-size="22" fill="#c9d6e3">즉흥적으로 떠올린 아이디어를 바로 구현하는 걸 좋아합니다.</text>
  <g font-family="{MONO}" font-size="16">
    <rect x="72" y="244" width="210" height="34" rx="17" fill="#4A90B8" fill-opacity="0.18" stroke="#4A90B8" stroke-opacity="0.6"/>
    <text x="177" y="266" text-anchor="middle" fill="#9fd3f5">Fullstack Developer</text>
    <rect x="294" y="244" width="224" height="34" rx="17" fill="#8B5CF6" fill-opacity="0.18" stroke="#8B5CF6" stroke-opacity="0.6"/>
    <text x="406" y="266" text-anchor="middle" fill="#c9b8ff">Claude Code tooling</text>
    <rect x="530" y="244" width="140" height="34" rx="17" fill="#22d3ee" fill-opacity="0.14" stroke="#22d3ee" stroke-opacity="0.55"/>
    <text x="600" y="266" text-anchor="middle" fill="#a5f3fc">ai-ng.co.kr</text>
    <text x="686" y="267" fill="#7ee0a1">▍<animate attributeName="opacity" values="1;0;1" dur="1s" repeatCount="indefinite" calcMode="discrete"/></text>
  </g>

  <ellipse cx="985" cy="312" rx="110" ry="14" fill="#000" fill-opacity="0.28"/>
  <g class="m"><image href="data:image/png;base64,{mascot}" x="855" y="40" width="260" height="260"/></g>
</g>
</svg>
'''
(out / "header.svg").write_text(header)

LANG = {"TypeScript": "#3178c6", "JavaScript": "#f1e05a", "Python": "#3572A5", "Rust": "#dea584", "Skill": "#CC785C"}

def wrap(s, n):
    lines, cur = [], ""
    for w in s.split(" "):
        if len(cur) + len(w) + 1 > n and cur:
            lines.append(cur); cur = w
        else:
            cur = (cur + " " + w).strip()
    lines.append(cur)
    return lines

def card(fname, name, kind, desc, lang, accent, tag=None, w=580, h=204):
    lines = wrap(desc, 44)[:3]
    tspans = "".join(f'<tspan x="28" dy="{0 if i == 0 else 24}">{html.escape(l)}</tspan>' for i, l in enumerate(lines))
    tag_svg = ""
    if tag:
        tw = 14 + len(tag) * 8
        tag_svg = f'<rect x="{w-28-tw}" y="24" width="{tw}" height="24" rx="12" fill="{accent}" fill-opacity="0.15" stroke="{accent}" stroke-opacity="0.5"/><text x="{w-28-tw/2}" y="40.5" text-anchor="middle" font-family="{MONO}" font-size="12" fill="{accent}">{tag}</text>'
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">
<defs>
  <linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#0f1726"/><stop offset="1" stop-color="#141d30"/></linearGradient>
  <linearGradient id="bar" x1="0" x2="1"><stop offset="0" stop-color="{accent}"/><stop offset="1" stop-color="{accent}" stop-opacity="0"/></linearGradient>
  <radialGradient id="glow" cx="1" cy="0" r="0.9"><stop offset="0" stop-color="{accent}" stop-opacity="0.22"/><stop offset="1" stop-color="{accent}" stop-opacity="0"/></radialGradient>
  <clipPath id="c"><rect width="{w}" height="{h}" rx="16"/></clipPath>
  <style>.s{{animation:s 4s linear infinite}}@keyframes s{{from{{transform:translateX(-{w}px)}}to{{transform:translateX({w}px)}}}}</style>
</defs>
<g clip-path="url(#c)">
  <rect width="{w}" height="{h}" fill="url(#g)"/>
  <rect width="{w}" height="{h}" fill="url(#glow)"/>
  <rect class="s" y="0" width="{w}" height="3" fill="url(#bar)"/>
  <rect x="0.5" y="0.5" width="{w-1}" height="{h-1}" rx="16" fill="none" stroke="#ffffff" stroke-opacity="0.1"/>
  <text x="28" y="46" font-family="{FONT}" font-size="13" fill="#7d8da3" letter-spacing="1.5">{kind}</text>
  <text x="28" y="78" font-family="{MONO}" font-size="24" font-weight="700" fill="#e6edf3">{name}</text>
  {tag_svg}
  <text y="112" font-family="{FONT}" font-size="15.5" fill="#aab7c6">{tspans}</text>
  <circle cx="34" cy="{h-24}" r="6" fill="{LANG[lang]}"/>
  <text x="48" y="{h-19}" font-family="{FONT}" font-size="13" fill="#8b98a9">{lang}</text>
  <text x="{w-28}" y="{h-19}" text-anchor="end" font-family="{MONO}" font-size="13" fill="{accent}">view repo →</text>
</g>
</svg>
'''
    (out / f"card-{fname}.svg").write_text(svg)

card("korean-unslop", "korean-unslop", "CLAUDE CODE PLUGIN",
     "한국어 글의 어색한 AI 문체를 찾아 다듬습니다. 문장 교정은 물론 PPT·보고서의 흐름까지 검토하고 진행 상황을 세션 화면에 띄웁니다.",
     "TypeScript", "#4A90B8", "writing")
card("model-routing", "model-routing", "SKILL",
     "하네스·플랜·남은 사용량을 확인하고 작업 단계마다 모델과 effort를 배치합니다. 아낄 단계와 품질을 지킬 단계를 구분합니다.",
     "Skill", "#CC785C", "routing")
card("claude-code-mods", "claude-code-mods", "MOD COLLECTION",
     "Claude Code의 세션 화면과 동작을 바꾸는 mod 모음. 대시보드, 세션 기록기, API 테스트 도구, 새 mod 템플릿을 담았습니다.",
     "TypeScript", "#8B5CF6", "mods")
card("your-call", "your-call", "CLAUDE CODE PLUGIN",
     "AI와 작업하며 내린 결정과 변경 과정을 대화 밖에 기록합니다. 의도는 사람이 한 말로만 남기고, 확정한 케이스를 테스트와 대조합니다.",
     "JavaScript", "#22c55e", "decisions")
card("wasm-bottleneck", "wasm-bottleneck", "SKILL",
     "성능 병목을 측정하고, 필요성이 확인된 부분만 Rust/WASM으로 교체하도록 돕습니다.",
     "Python", "#f59e0b", "perf", h=186)
card("kaisa", "kaisa", "RUST TOOL · EARLY STAGE",
     "코딩 에이전트의 작업을 격리하고, 테스트와 독립 리뷰를 통과한 것만 보게 합니다.",
     "Rust", "#ef4444", "wip", h=186)

footer = '''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="120" viewBox="0 0 1200 120">
<defs>
  <linearGradient id="w" x1="0" x2="1"><stop offset="0" stop-color="#4A90B8"/><stop offset="0.5" stop-color="#8B5CF6"/><stop offset="1" stop-color="#22d3ee"/></linearGradient>
  <style>.a{animation:m 8s ease-in-out infinite}.b{animation:m 11s ease-in-out infinite reverse}@keyframes m{0%,100%{transform:translateX(0)}50%{transform:translateX(-200px)}}</style>
</defs>
<g class="b" opacity="0.35"><path fill="url(#w)" d="M0 70 C150 40 300 100 450 70 S750 40 900 70 S1200 100 1400 60 V120 H0Z"/></g>
<g class="a" opacity="0.6"><path fill="url(#w)" d="M0 85 C200 60 350 110 550 85 S850 60 1050 85 S1300 105 1400 80 V120 H0Z"/></g>
</svg>
'''
(out / "footer-wave.svg").write_text(footer)
