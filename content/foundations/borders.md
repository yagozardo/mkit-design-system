# Borders

The border system covers two concerns: **border radius** (corner rounding) and **border width** (stroke thickness).

---

## Border Radius

| Token | Value |
|---|---|
| `borderRadius.XS` | 4px |
| `borderRadius.S` | 8px |
| `borderRadius.M` | 12px |
| `borderRadius.L` | 16px |
| `borderRadius.Pill` | 999px |
| `borderRadius.Circle` | 50%% |

### When to Use Each Radius

| Token | Usage |
|---|---|
| `XS` (4px) | Chips, tags, badges, small inputs |
| `S` (8px) | Buttons, cards, tooltips |
| `M` (12px) | Modals, panels, dropdowns |
| `L` (16px) | Large cards, image containers |
| `Pill` (999px) | Toggle switches, pill badges, search bars |
| `Circle` (50%) | Avatars, icon-only buttons, spinners |

---

## Border Width

| Token | Value |
|---|---|
| `borderWidth.default` | 1px |
| `borderWidth.focused` | 1.5px |

- **Default (1px)** — All standard borders: inputs, cards, dividers, tables.
- **Focused (1.5px)** — Interactive elements in focused state: inputs, selects, textareas.

---

## Usage Guidelines

- Always use border tokens — never set corner radii or widths directly.
- For focus rings, use `Border/Focus` color + `borderWidth.focused` (1.5px).
- Disabled components retain their shape but use `Border/Disabled` color.

## Don't

- Don't mix radius tokens on the same component (e.g., L on top, XS on bottom).
- Don't use `Circle` for anything other than circular/avatar-shaped elements.
