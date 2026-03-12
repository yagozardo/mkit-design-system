#!/usr/bin/env python3
"""
MKIT Design System — Static Site Generator
Phase 4 build script. Run: python3 build.py
Reads: assets/tokens.json, assets/ia.json, content/**/*.md
Writes: index.html, foundations/*.html, components/*.html, icons/*.html,
        resources/*.html, assets/tokens.css
"""

import json, os, re, html as html_mod
from pathlib import Path
import markdown as md_lib

# ─── Paths ────────────────────────────────────────────────────────────────────
SITE = Path(__file__).parent
CONTENT = SITE / "content"
ASSETS  = SITE / "assets"

tokens = json.loads((ASSETS / "tokens.json").read_text())
ia     = json.loads((ASSETS / "ia.json").read_text())

# ─── 1. GENERATE tokens.css ───────────────────────────────────────────────────
def build_tokens_css():
    lines = [":root {"]

    # Primitive colors
    for group, shades in tokens["color"]["primitive"].items():
        g = group.lower().replace(" ", "-")
        for step, val in shades.items():
            lines.append(f"  --color-{g}-{step}: {val};")

    # Semantic colors
    for cat, toks in tokens["color"]["semantic"].items():
        c = cat.lower()
        for name, val in toks.items():
            n = re.sub(r'(?<!^)(?=[A-Z])', '-', name).lower()
            lines.append(f"  --color-{c}-{n}: {val};")

    # Typography
    lines.append(f"  --font-heading: '{tokens['typography']['fontFamily']['heading']}', sans-serif;")
    lines.append(f"  --font-body: '{tokens['typography']['fontFamily']['body']}', sans-serif;")
    for name, p in tokens["typography"]["heading"].items():
        n = name.lower()
        lines.append(f"  --heading-{n}-size: {p['fontSize']}px;")
        lines.append(f"  --heading-{n}-lh: {p['lineHeight']}px;")
        lines.append(f"  --heading-{n}-ls: {p['letterSpacing']}px;")
    for size, variants in tokens["typography"]["text"].items():
        s = size.lower()
        for weight, p in variants.items():
            w = "400" if weight == "regular" else "600"
            lines.append(f"  --text-{s}-{weight}-size: {p['fontSize']}px;")
            lines.append(f"  --text-{s}-{weight}-lh: {p['lineHeight']}px;")

    # Spacing
    for name, val in tokens["spacing"].items():
        if name.startswith("_"): continue
        lines.append(f"  --spacing-{name.lower()}: {val}px;")

    # Border radius
    for name, p in tokens["borderRadius"].items():
        lines.append(f"  --radius-{name.lower()}: {p['value']}{p['unit']};")

    # Border width
    for name, p in tokens["borderWidth"].items():
        lines.append(f"  --border-{name}: {p['value']}{p['unit']};")

    # Docs shell (light mode)
    docs = {
        "--docs-bg":             "#F5F5F5",
        "--docs-bg-surface":     "#FFFFFF",
        "--docs-bg-sidebar":     "#FFFFFF",
        "--docs-bg-active":      "#E3EEF7",
        "--docs-text":           "#191C1E",
        "--docs-text-secondary": "#454748",
        "--docs-text-muted":     "#6F7071",
        "--docs-border":         "#E2E2E2",
        "--docs-accent":         "#0072CF",
        "--docs-accent-hover":   "#0B62A9",
        "--docs-code-bg":        "#F1F1F1",
        "--docs-table-head":     "#F5F5F5",
    }
    for k, v in docs.items():
        lines.append(f"  {k}: {v};")

    lines.append("}")

    # Base styles
    lines += [
        "",
        "*, *::before, *::after { box-sizing: border-box; }",
        "body { font-family: var(--font-body); color: var(--docs-text); background: var(--docs-bg); margin: 0; }",
        "code { font-family: 'JetBrains Mono', 'Fira Code', monospace; background: var(--docs-code-bg); "
        "padding: 2px 6px; border-radius: 4px; font-size: 0.875em; cursor: pointer; transition: background 0.15s; }",
        "code.copied { background: #dcfce7 !important; color: #166534 !important; }",
        "pre { background: #1e2937; color: #e5e7eb; padding: 1rem 1.25rem; border-radius: 8px; overflow-x: auto; }",
        "pre code { background: transparent; color: inherit; padding: 0; font-size: 0.85rem; cursor: default; }",
        "a { color: var(--docs-accent); text-decoration: none; }",
        "a:hover { text-decoration: underline; }",
        "h1,h2,h3,h4 { font-family: var(--font-heading); font-weight: 700; color: var(--docs-text); margin-top: 2rem; margin-bottom: 0.5rem; }",
        "h1 { font-size: 2.25rem; line-height: 1.2; letter-spacing: -0.5px; margin-top: 0; }",
        "h2 { font-size: 1.375rem; line-height: 1.3; border-bottom: 1px solid var(--docs-border); padding-bottom: 0.4rem; }",
        "h3 { font-size: 1rem; line-height: 1.4; }",
        "p  { line-height: 1.6; color: var(--docs-text); margin: 0.75rem 0; }",
        "ul, ol { padding-left: 1.4rem; line-height: 1.7; }",
        "li { margin-bottom: 0.25rem; }",
        "hr { border: none; border-top: 1px solid var(--docs-border); margin: 2rem 0; }",
        "blockquote, aside.callout { background: #EFF6FF; border-left: 3px solid var(--docs-accent); "
        "margin: 1rem 0; padding: 0.75rem 1rem; border-radius: 0 6px 6px 0; }",
        "blockquote p, aside.callout p { margin: 0; font-size: 0.9rem; }",
        "table { width: 100%; border-collapse: collapse; font-size: 0.875rem; margin: 1rem 0; }",
        "th { background: var(--docs-table-head); text-align: left; padding: 0.6rem 0.75rem; "
        "font-weight: 600; border-bottom: 2px solid var(--docs-border); white-space: nowrap; }",
        "td { padding: 0.55rem 0.75rem; border-bottom: 1px solid var(--docs-border); vertical-align: top; }",
        "tr:last-child td { border-bottom: none; }",
        "tr:hover td { background: #fafafa; }",
        "@media (prefers-reduced-motion: reduce) { *, *::before, *::after { animation-duration: 0.01ms !important; transition-duration: 0.01ms !important; } }",
    ]

    css = "\n".join(lines)
    (ASSETS / "tokens.css").write_text(css)
    print("  ✓ assets/tokens.css")

# ─── 2. NAVIGATION ────────────────────────────────────────────────────────────
def _nav_path_for_md(md_path: Path) -> str:
    rel = md_path.relative_to(CONTENT)
    parts = list(rel.parts)
    parts[-1] = parts[-1].replace(".md", ".html")
    if parts[0] == "index.html":
        return "/index.html"
    return "/" + "/".join(parts)

def build_sidebar(active_path: str) -> str:
    """Build the full sidebar HTML."""
    # Collect component files for the Components group
    comp_files = sorted((CONTENT / "components").glob("*.md"))
    comp_items = [{"label": f.stem.replace("-", " ").title(), "path": f"/components/{f.stem}.html"}
                  for f in comp_files]

    nav_groups = [
        {
            "label": "Overview",
            "items": [
                {"label": "Introduction",    "path": "/index.html"},
                {"label": "Getting Started", "path": "/resources/getting-started.html"},
            ]
        },
        {
            "label": "Foundations",
            "items": [
                {"label": "Color",           "path": "/foundations/color.html"},
                {"label": "Typography",      "path": "/foundations/typography.html"},
                {"label": "Spacing",         "path": "/foundations/spacing.html"},
                {"label": "Elevation",       "path": "/foundations/elevation.html"},
                {"label": "Borders",         "path": "/foundations/borders.html"},
                {"label": "Motion",          "path": "/foundations/motion.html"},
            ]
        },
        {
            "label": "Components",
            "items": comp_items
        },
        {
            "label": "Icons",
            "items": [
                {"label": "Icon Library", "path": "/icons/index.html"},
            ]
        },
    ]

    parts = []
    for group in nav_groups:
        parts.append(f'<div class="nav-group">')
        parts.append(f'  <div class="nav-group-label">{group["label"]}</div>')
        for item in group["items"]:
            is_active = item["path"] == active_path
            cls = "nav-item active" if is_active else "nav-item"
            parts.append(f'  <a href="{item["path"]}" class="{cls}">{item["label"]}</a>')
        parts.append('</div>')

    return "\n".join(parts)


# ─── 3. PAGE SHELL ────────────────────────────────────────────────────────────
def page_shell(title: str, content_html: str, active_path: str,
               breadcrumbs: list = None, depth: int = 0) -> str:
    root = "../" * depth if depth else ""
    sidebar_html = build_sidebar(active_path)

    bc_html = ""
    if breadcrumbs:
        items = []
        for i, (label, href) in enumerate(breadcrumbs):
            if i == len(breadcrumbs) - 1:
                items.append(f'<span class="bc-current">{label}</span>')
            else:
                items.append(f'<a href="{href}">{label}</a>')
        bc_html = '<nav class="breadcrumbs" aria-label="Breadcrumb">' + \
                  '<span class="bc-sep">›</span>'.join(items) + '</nav>'

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{html_mod.escape(title)} — MKIT Design System</title>
  <link rel="preconnect" href="https://fonts.bunny.net">
  <link href="https://fonts.bunny.net/css?family=inter:400,600&display=swap" rel="stylesheet">
  <link href="https://api.fontshare.com/v2/css?f[]=satoshi@700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="{root}assets/tokens.css">
  <style>
    /* Layout */
    .layout {{ display: flex; height: 100vh; overflow: hidden; }}
    .sidebar {{
      width: 240px; min-width: 240px; height: 100vh; overflow-y: auto;
      background: var(--docs-bg-sidebar); border-right: 1px solid var(--docs-border);
      display: flex; flex-direction: column;
    }}
    .sidebar-logo {{
      padding: 20px 16px 16px; border-bottom: 1px solid var(--docs-border);
      font-family: var(--font-heading); font-weight: 700; font-size: 1rem;
      color: var(--docs-text); line-height: 1.2;
    }}
    .sidebar-logo span {{ display: block; font-family: var(--font-body); font-weight: 400;
      font-size: 0.75rem; color: var(--docs-text-muted); margin-top: 2px; }}
    .sidebar-nav {{ padding: 8px 0 24px; flex: 1; }}
    .nav-group {{ margin-bottom: 4px; }}
    .nav-group-label {{
      padding: 12px 16px 4px; font-size: 0.7rem; font-weight: 600; letter-spacing: 0.08em;
      text-transform: uppercase; color: var(--docs-text-muted);
    }}
    .nav-item {{
      display: block; padding: 6px 16px; font-size: 0.8125rem; color: var(--docs-text-secondary);
      text-decoration: none; border-radius: 0; transition: background 0.1s, color 0.1s;
      line-height: 1.4;
    }}
    .nav-item:hover {{ background: var(--docs-bg); color: var(--docs-text); text-decoration: none; }}
    .nav-item.active {{
      background: var(--docs-bg-active); color: var(--docs-accent);
      font-weight: 600; border-right: 2px solid var(--docs-accent);
    }}
    .main {{ flex: 1; overflow-y: auto; display: flex; flex-direction: column; min-width: 0; }}
    .topbar {{
      padding: 12px 40px; border-bottom: 1px solid var(--docs-border);
      background: var(--docs-bg-surface); position: sticky; top: 0; z-index: 10;
    }}
    .content-area {{ padding: 40px; max-width: 900px; }}

    /* Breadcrumbs */
    .breadcrumbs {{ font-size: 0.8125rem; color: var(--docs-text-muted); display: flex; gap: 6px; align-items: center; }}
    .breadcrumbs a {{ color: var(--docs-text-muted); }}
    .breadcrumbs a:hover {{ color: var(--docs-accent); }}
    .bc-current {{ color: var(--docs-text-secondary); }}
    .bc-sep {{ color: var(--docs-border); }}

    /* Token cards */
    .swatch-group {{ margin-bottom: 2rem; }}
    .swatch-group h3 {{ margin-bottom: 0.75rem; font-size: 0.9375rem; }}
    .swatch-row {{ display: flex; gap: 4px; flex-wrap: wrap; }}
    .swatch {{
      position: relative; width: 56px; cursor: pointer;
      transition: transform 0.1s;
    }}
    .swatch:hover {{ transform: translateY(-2px); }}
    .swatch-chip {{
      height: 40px; border-radius: 6px; border: 1px solid rgba(0,0,0,0.08);
    }}
    .swatch-label {{ font-size: 0.65rem; color: var(--docs-text-muted); margin-top: 3px;
      text-align: center; line-height: 1.2; }}

    /* Semantic color table swatch */
    .sem-swatch {{ width: 20px; height: 20px; border-radius: 50%;
      border: 1px solid rgba(0,0,0,0.1); display: inline-block; flex-shrink: 0; }}

    /* Typography specimens */
    .type-specimen {{ margin: 2rem 0; }}
    .type-specimen-label {{ font-size: 0.75rem; font-weight: 600;
      color: var(--docs-text-muted); margin-bottom: 6px; letter-spacing: 0.04em; text-transform: uppercase; }}
    .type-specimen-text {{ color: var(--docs-text); }}

    /* Spacing ruler */
    .spacing-bar {{ background: var(--docs-accent); height: 8px; border-radius: 4px;
      display: inline-block; opacity: 0.7; }}

    /* Radius preview */
    .radius-preview {{ display: flex; gap: 20px; flex-wrap: wrap; margin: 1.5rem 0; }}
    .radius-swatch {{ text-align: center; }}
    .radius-box {{ width: 64px; height: 64px; background: var(--docs-bg-active);
      border: 2px solid var(--docs-accent); margin: 0 auto 8px; }}
    .radius-label {{ font-size: 0.75rem; color: var(--docs-text-muted); }}

    /* Component preview box */
    .component-preview {{
      background: var(--docs-table-head); border: 1px dashed var(--docs-border);
      border-radius: 8px; padding: 40px; text-align: center; margin-bottom: 2rem;
      color: var(--docs-text-muted); font-size: 0.875rem;
    }}
    .component-preview strong {{ display: block; font-size: 0.8125rem; margin-bottom: 6px; color: var(--docs-text-secondary); }}

    /* Do/Don't sections */
    .do-dont {{ display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin: 1rem 0; }}
    .do-block {{ border-left: 3px solid #16a34a; padding: 0.75rem 1rem; background: #f0fdf4; border-radius: 0 6px 6px 0; }}
    .dont-block {{ border-left: 3px solid #dc2626; padding: 0.75rem 1rem; background: #fef2f2; border-radius: 0 6px 6px 0; }}
    .do-block h4, .dont-block h4 {{ margin: 0 0 0.5rem; font-size: 0.8125rem; font-weight: 600; }}
    .do-block h4 {{ color: #15803d; }}
    .dont-block h4 {{ color: #b91c1c; }}
    .do-block ul, .dont-block ul {{ margin: 0; padding-left: 1.2rem; font-size: 0.85rem; }}

    /* Home quick links */
    .quick-links {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); gap: 16px; margin: 2rem 0; }}
    .quick-link-card {{
      border: 1px solid var(--docs-border); border-radius: 8px; padding: 20px;
      background: var(--docs-bg-surface); text-decoration: none; color: var(--docs-text);
      transition: border-color 0.15s, box-shadow 0.15s;
    }}
    .quick-link-card:hover {{ border-color: var(--docs-accent); box-shadow: 0 2px 8px rgba(0,114,207,0.12); text-decoration: none; }}
    .quick-link-card .card-icon {{ font-size: 1.5rem; margin-bottom: 10px; }}
    .quick-link-card .card-title {{ font-family: var(--font-heading); font-weight: 700; font-size: 1rem; margin-bottom: 4px; }}
    .quick-link-card .card-desc {{ font-size: 0.8125rem; color: var(--docs-text-secondary); }}

    /* Responsive */
    @media (max-width: 768px) {{
      .sidebar {{ display: none; }}
      .content-area {{ padding: 20px; }}
      .do-dont {{ grid-template-columns: 1fr; }}
    }}
  </style>
</head>
<body>
  <div class="layout">
    <aside class="sidebar" aria-label="Main navigation">
      <div class="sidebar-logo">
        MKIT DS
        <span>Design System</span>
      </div>
      <nav class="sidebar-nav">
        {sidebar_html}
      </nav>
    </aside>
    <div class="main">
      <div class="topbar">
        {bc_html if bc_html else '<span style="color:var(--docs-text-muted);font-size:0.8125rem;">Winsupply Marketing IT UX</span>'}
      </div>
      <div class="content-area">
        {content_html}
      </div>
    </div>
  </div>
  <script>
    // Token copy-on-click
    document.querySelectorAll('code').forEach(el => {{
      if (el.closest('pre')) return;
      el.title = 'Click to copy';
      el.addEventListener('click', () => {{
        navigator.clipboard.writeText(el.textContent).catch(() => {{}});
        el.classList.add('copied');
        setTimeout(() => el.classList.remove('copied'), 1200);
      }});
    }});
  </script>
</body>
</html>"""


# ─── 4. MARKDOWN CONVERTER ────────────────────────────────────────────────────
def md_to_html(text: str) -> str:
    result = md_lib.markdown(
        text,
        extensions=["tables", "fenced_code", "attr_list", "toc"],
        extension_configs={"toc": {"permalink": False}}
    )
    # Rewrite any .md hrefs to .html (handles cross-page links in source markdown)
    result = re.sub(r'href="([^"]+)\.md"', r'href="\1.html"', result)
    return result


# ─── 5. ENHANCED COLOR PAGE ───────────────────────────────────────────────────
def render_color_page(md_text: str) -> str:
    # Extract intro text (everything before "## Primitive Colors")
    intro_end = md_text.find("## Primitive Colors")
    intro_html = md_to_html(md_text[:intro_end].strip()) if intro_end > 0 else ""

    # Primitive color swatches
    prim_html = '<h2 id="primitive-colors">Primitive Colors</h2>'
    prim_html += '<p>Raw palette — 14 color groups, steps 0 (darkest) to 100 (lightest). Click any hex value to copy.</p>'
    for group, shades in tokens["color"]["primitive"].items():
        prim_html += f'<div class="swatch-group"><h3>{html_mod.escape(group)}</h3><div class="swatch-row">'
        for step, val in shades.items():
            prim_html += (
                f'<div class="swatch" title="{val}">'
                f'  <div class="swatch-chip" style="background:{val}"></div>'
                f'  <div class="swatch-label"><code>{val}</code><br>{step}</div>'
                f'</div>'
            )
        prim_html += '</div></div>'

    # Semantic color tables
    sem_html = '<h2 id="semantic-colors">Semantic Colors</h2>'
    sem_html += '<p>Role-based tokens mapped from the primitive palette.</p>'
    for cat, toks_dict in tokens["color"]["semantic"].items():
        sem_html += f'<h3>{cat}</h3>'
        sem_html += '<table><thead><tr><th>Token</th><th>Hex</th><th>Swatch</th></tr></thead><tbody>'
        for name, val in toks_dict.items():
            sem_html += (
                f'<tr><td><code>color.semantic.{cat}.{name}</code></td>'
                f'<td><code>{val}</code></td>'
                f'<td><span class="sem-swatch" style="background:{val}"></span></td></tr>'
            )
        sem_html += '</tbody></table>'

    # Usage section from markdown (after "## Semantic Colors" section)
    usage_start = md_text.find("## Usage Guidelines")
    usage_html = md_to_html(md_text[usage_start:]) if usage_start > 0 else ""

    return intro_html + prim_html + sem_html + usage_html


# ─── 6. ENHANCED TYPOGRAPHY PAGE ─────────────────────────────────────────────
def render_typography_page(md_text: str) -> str:
    base_html = md_to_html(md_text)

    specimens = '<h2 id="live-specimens">Live Specimens</h2>'
    specimens += '<p>Text rendered using the actual Satoshi and Inter fonts loaded via CDN.</p>'

    for name, p in tokens["typography"]["heading"].items():
        specimens += (
            f'<div class="type-specimen">'
            f'  <div class="type-specimen-label">Heading/{name} — {p["fontSize"]}px / {p["lineHeight"]}px lh / w{p["fontWeight"]}</div>'
            f'  <div class="type-specimen-text" style="font-family:Satoshi,sans-serif;font-size:{p["fontSize"]}px;'
            f'line-height:{p["lineHeight"]}px;font-weight:{p["fontWeight"]};letter-spacing:{p["letterSpacing"]}px;">'
            f'The quick brown fox</div>'
            f'</div>'
        )

    specimens += '<h3>Text Scale (Inter)</h3>'
    for size, variants in tokens["typography"]["text"].items():
        for weight, p in variants.items():
            specimens += (
                f'<div class="type-specimen">'
                f'  <div class="type-specimen-label">Text/{size}/{weight.capitalize()} — {p["fontSize"]}px / {p["lineHeight"]}px lh / w{p["fontWeight"]}</div>'
                f'  <div class="type-specimen-text" style="font-family:Inter,sans-serif;font-size:{p["fontSize"]}px;'
                f'line-height:{p["lineHeight"]}px;font-weight:{p["fontWeight"]};">'
                f'The quick brown fox jumps over the lazy dog</div>'
                f'</div>'
            )

    return base_html + specimens


# ─── 7. ENHANCED SPACING PAGE ─────────────────────────────────────────────────
def render_spacing_page(md_text: str) -> str:
    base_html = md_to_html(md_text)
    ruler = '<h2 id="visual-scale">Visual Scale</h2>'
    ruler += '<div style="display:flex;flex-direction:column;gap:10px;margin:1.5rem 0;">'
    for name, val in tokens["spacing"].items():
        if name.startswith("_"): continue
        bar_w = min(val, 600)
        ruler += (
            f'<div style="display:flex;align-items:center;gap:16px;">'
            f'  <div style="width:80px;font-size:0.8rem;color:var(--docs-text-muted);text-align:right;flex-shrink:0;">'
            f'    <strong>{name}</strong></div>'
            f'  <div class="spacing-bar" style="width:{bar_w}px;"></div>'
            f'  <code style="font-size:0.75rem;">{val}px</code>'
            f'</div>'
        )
    ruler += '</div>'
    return base_html + ruler


# ─── 8. ENHANCED BORDERS PAGE ────────────────────────────────────────────────
def render_borders_page(md_text: str) -> str:
    base_html = md_to_html(md_text)
    radius_items = {
        "XS": "4px", "S": "8px", "M": "12px", "L": "16px",
        "Pill": "999px", "Circle": "50%",
    }
    preview = '<h2 id="radius-preview">Radius Preview</h2>'
    preview += '<div class="radius-preview">'
    for name, val in radius_items.items():
        preview += (
            f'<div class="radius-swatch">'
            f'  <div class="radius-box" style="border-radius:{val};"></div>'
            f'  <div class="radius-label"><strong>{name}</strong><br>{val}</div>'
            f'</div>'
        )
    preview += '</div>'
    return base_html + preview


# ─── 9. HOME PAGE ─────────────────────────────────────────────────────────────
def render_home_page(md_text: str) -> str:
    intro_html = md_to_html(md_text)
    comp_count = len(list((CONTENT / "components").glob("*.md")))
    cards = [
        ("🎨", "Foundations", "Color, typography, spacing, elevation, and borders.", "/foundations/color.html"),
        ("🧩", "Components", f"{comp_count} reusable UI building blocks.", "/components/button.html"),
        ("✦",  "Icons",      "Lucide open-source icon library.", "/icons/index.html"),
        ("📖", "Getting Started", "How to use Figma libraries and tokens.", "/resources/getting-started.html"),
    ]
    cards_html = '<div class="quick-links">'
    for icon, title, desc, href in cards:
        cards_html += (
            f'<a class="quick-link-card" href="{href}">'
            f'  <div class="card-icon">{icon}</div>'
            f'  <div class="card-title">{title}</div>'
            f'  <div class="card-desc">{desc}</div>'
            f'</a>'
        )
    cards_html += '</div>'
    return intro_html + cards_html


# ─── 10. COMPONENT PAGE ───────────────────────────────────────────────────────
def render_component_page(md_text: str, name: str) -> str:
    # Insert component preview image (or placeholder if not found)
    img_path = SITE / "assets" / "images" / f"{name}.png"
    depth_prefix = "../" if "/" not in name else "../../"
    if img_path.exists():
        preview_box = (
            f'<div class="component-preview" style="background:#fff;padding:0;overflow:hidden;">'
            f'  <img src="{depth_prefix}assets/images/{name}.png" alt="{name} preview"'
            f'    style="width:100%;height:auto;display:block;">'
            f'</div>'
        )
    else:
        preview_box = (
            f'<div class="component-preview">'
            f'  <strong>Component Preview</strong>'
            f'  Image not found: <code>assets/images/{name}.png</code>'
            f'</div>'
        )

    # Parse and split the Do / Don't sections for styled rendering
    raw_html = md_to_html(md_text)

    # Wrap adjacent Do/Don't <h3> + <ul> into styled blocks
    raw_html = re.sub(
        r'<h3>Do</h3>\s*(<ul>.*?</ul>)\s*<h3>Don&#x27;t</h3>\s*(<ul>.*?</ul>)',
        lambda m: (
            '<div class="do-dont">'
            f'<div class="do-block"><h4>✓ Do</h4>{m.group(1)}</div>'
            f'<div class="dont-block"><h4>✕ Don\'t</h4>{m.group(2)}</div>'
            '</div>'
        ),
        raw_html, flags=re.DOTALL
    )

    # Skip the H1 (it's the page title) and insert preview after it
    h1_end = raw_html.find('</h1>')
    if h1_end != -1:
        insert_at = h1_end + len('</h1>')
        raw_html = raw_html[:insert_at] + preview_box + raw_html[insert_at:]

    return raw_html


# ─── 11. WRITE A PAGE ─────────────────────────────────────────────────────────
def write_page(out_path: Path, title: str, content_html: str,
               active_nav: str, breadcrumbs: list, depth: int):
    out_path.parent.mkdir(parents=True, exist_ok=True)
    html = page_shell(title, content_html, active_nav, breadcrumbs, depth)
    out_path.write_text(html)
    print(f"  ✓ {out_path.relative_to(SITE)}")


# ─── 12. MAIN BUILD ───────────────────────────────────────────────────────────
def main():
    print("Building MKIT Design System site...")

    # Step 1 — CSS
    print("\n[1/3] Generating tokens.css")
    build_tokens_css()

    print("\n[2/3] Generating HTML pages")

    # ── Home
    md = (CONTENT / "index.md").read_text()
    write_page(
        SITE / "index.html", "Introduction",
        render_home_page(md),
        "/index.html",
        [("Introduction", "/index.html")],
        depth=0
    )

    # ── Getting Started
    md = (CONTENT / "resources" / "getting-started.md").read_text()
    write_page(
        SITE / "resources" / "getting-started.html", "Getting Started",
        md_to_html(md),
        "/resources/getting-started.html",
        [("Introduction", "/index.html"), ("Getting Started", "/resources/getting-started.html")],
        depth=1
    )

    # ── Foundations
    foundation_map = {
        "color":      ("Color",           render_color_page),
        "typography": ("Typography",      render_typography_page),
        "spacing":    ("Spacing",         render_spacing_page),
        "elevation":  ("Elevation",       lambda t: md_to_html(t)),
        "borders":    ("Borders",         render_borders_page),
        "motion":     ("Motion",          lambda t: md_to_html(t)),
    }
    for slug, (label, renderer) in foundation_map.items():
        md = (CONTENT / "foundations" / f"{slug}.md").read_text()
        write_page(
            SITE / "foundations" / f"{slug}.html", label,
            renderer(md),
            f"/foundations/{slug}.html",
            [("Introduction", "/index.html"), ("Foundations", "/foundations/color.html"), (label, f"/foundations/{slug}.html")],
            depth=1
        )

    # ── Components
    for md_file in sorted((CONTENT / "components").glob("*.md")):
        slug  = md_file.stem
        label = slug.replace("-", " ").title()
        md    = md_file.read_text()
        write_page(
            SITE / "components" / f"{slug}.html", label,
            render_component_page(md, slug),
            f"/components/{slug}.html",
            [("Introduction", "/index.html"), ("Components", "/index.html"), (label, f"/components/{slug}.html")],
            depth=1
        )

    # ── Icons
    md = (CONTENT / "icons" / "index.md").read_text()
    write_page(
        SITE / "icons" / "index.html", "Icon Library",
        md_to_html(md),
        "/icons/index.html",
        [("Introduction", "/index.html"), ("Icons", "/icons/index.html")],
        depth=1
    )

    print("\n[3/3] Done.")
    total = sum(1 for _ in SITE.rglob("*.html"))
    print(f"\n  {total} HTML files in site root.")
    print("  Open index.html in a browser to preview.")


if __name__ == "__main__":
    main()
