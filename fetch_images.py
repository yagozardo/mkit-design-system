#!/usr/bin/env python3
"""Phase 1.4 — Fetch component preview images from Figma."""

import json, os, urllib.request, urllib.error, time, sys

# ── Config ──────────────────────────────────────────────────────────────────
settings = json.load(open(os.path.expanduser("~/.claude/settings.json")))
API_KEY = settings["mcpServers"]["figma"]["args"][-1].split("=", 1)[1]
HEADERS = {"X-Figma-Token": API_KEY}
OUT_DIR = "assets/images"
os.makedirs(OUT_DIR, exist_ok=True)

BASE   = "cBzqjlyUoVJczHoLvQPXS9"
ADVANCED = "rF3f8JHhAXJ4wI8X3PMKpJ"

# ── Component → (fileKey, nodeId) map ───────────────────────────────────────
COMPONENTS = {
    # Base Components file
    "badge":          (BASE, "268:1398"),
    "button":         (BASE, "3:156"),
    "button-circle":  (BASE, "3:534"),
    "checkbox":       (BASE, "4:140"),
    "chip":           (BASE, "308:1591"),
    "country-badge":  (BASE, "531:1909"),
    "input":          (BASE, "261:2293"),
    "pill":           (BASE, "432:2439"),
    "radio":          (BASE, "22:1377"),
    "spinner":        (BASE, "1:219"),
    "tag":            (BASE, "308:906"),
    "toast":          (BASE, "168:783"),
    "toggle":         (BASE, "35:483"),
    "tooltip":        (BASE, "79:184"),
    # Advanced Components file
    "accordion":         (ADVANCED, "3248:685"),
    "add-to-cart-button":(ADVANCED, "2918:826"),
    "breadcrumb":        (ADVANCED, "3216:5513"),
    "drawer":            (ADVANCED, "2186:12247"),
    "dropdown":          (ADVANCED, "2291:406"),
    "footer":            (ADVANCED, "2696:2682"),
    "image-tiles":       (ADVANCED, "2004:449"),
    "location-card":     (ADVANCED, "2928:6338"),
    "maintenance-banner":(ADVANCED, "3314:2390"),
    "modal":             (ADVANCED, "2193:16365"),
    "navbar":            (ADVANCED, "2055:2862"),
    "product-carousel":  (ADVANCED, "2808:17254"),
    "products":          (ADVANCED, "3034:12235"),
    "segmented-control": (ADVANCED, "2813:19103"),
    "tabs":              (ADVANCED, "3192:531"),
    "tips":              (ADVANCED, "210:678"),
    "tree-view":         (ADVANCED, "2751:3675"),
}

def figma_get(path):
    req = urllib.request.Request(f"https://api.figma.com/v1{path}", headers=HEADERS)
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read())

def download(url, path):
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req, timeout=60) as r:
        with open(path, "wb") as f:
            f.write(r.read())

def batch_images(file_key, node_map, scale=2, fmt="png"):
    """node_map: {node_id: slug}. Returns {node_id: image_url}."""
    ids = ",".join(node_map.keys())
    # URL-encode colons
    ids_enc = ids.replace(":", "%3A")
    data = figma_get(f"/images/{file_key}?ids={ids_enc}&scale={scale}&format={fmt}")
    return data.get("images", {})

# ── Group by file ────────────────────────────────────────────────────────────
by_file = {}
for slug, (fkey, nid) in COMPONENTS.items():
    by_file.setdefault(fkey, {})[nid] = slug

# ── Fetch + download ─────────────────────────────────────────────────────────
errors = []
total = len(COMPONENTS)
done = 0

for fkey, node_map in by_file.items():
    label = "Base" if fkey == BASE else "Advanced"
    print(f"\n[{label}] Requesting {len(node_map)} image URLs…")
    try:
        images = batch_images(fkey, node_map)
    except Exception as e:
        print(f"  ERROR fetching image URLs: {e}")
        errors.append(("batch", fkey, str(e)))
        continue

    for nid, slug in node_map.items():
        url = images.get(nid)
        if not url:
            print(f"  SKIP  {slug} — no URL returned")
            errors.append(("no-url", slug, ""))
            continue
        out_path = os.path.join(OUT_DIR, f"{slug}.png")
        if os.path.exists(out_path) and os.path.getsize(out_path) > 0:
            print(f"  CACHED {slug}.png")
            done += 1
            continue
        try:
            download(url, out_path)
            size = os.path.getsize(out_path)
            print(f"  ✓  {slug}.png  ({size//1024}KB)")
            done += 1
        except Exception as e:
            print(f"  ERROR {slug}: {e}")
            errors.append(("download", slug, str(e)))
        time.sleep(0.1)  # gentle rate limiting

print(f"\n── Summary ──────────────────────────────")
print(f"  Downloaded: {done}/{total}")
if errors:
    print(f"  Errors ({len(errors)}):")
    for kind, name, msg in errors:
        print(f"    [{kind}] {name}: {msg}")

# ── Check for missing: popover, select-menu ──────────────────────────────────
missing = ["popover", "select-menu"]
print(f"\n  Note: {missing} have no component set in Figma — skipped (placeholders remain).")
print("\nDone. Images saved to assets/images/")
