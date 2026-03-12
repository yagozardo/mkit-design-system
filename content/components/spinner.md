# Spinner

A visual loading indicator that communicates an ongoing background process. Appears while content is loading or an action is in progress.

**Figma variant properties:** Size=S/M/L

---

## Preview

> Component preview image — to be added manually from Figma export.

---

## Variants

| Variant |
|---|
| Size: S / M / L |

---

## Props

| Property | Type | Default | Description |
|---|---|---|---|
| `size` | "S" | "M" | "L" | "M" | Spinner diameter |
| `label` | string | "Loading..." | Accessible label (visually hidden) |
| `overlay` | boolean | false | Renders as a full-area blocking overlay |

---

## Usage

### Do
- Always include an accessible label.
- Use S for inline/button loading, M for content sections, L for full-page loads.
- Pair with disabled interactive elements during loading.

### Don't
- Don't leave spinner visible indefinitely without an error state fallback.
- Don't use multiple spinners on the same view.
- Don't rely solely on animation — provide text too.

---

## Accessibility

- `role='status'` with `aria-live='polite'`.
- Visible label as visually-hidden text.
- Respect `prefers-reduced-motion`.

---

## Tokens Used

- `color.semantic.Content.Brand`
- `color.semantic.Background.Tonal`
