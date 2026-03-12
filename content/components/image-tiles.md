# Image Tiles

A grid of linked image tiles used for category navigation, promotional campaigns, or visual browsing. Each tile contains an image with an overlaid label.

**Figma variant properties:** Type=2col/3col/4col/Mixed

---

## Preview

> Component preview image — to be added manually from Figma export.

---

## Variants

| Variant |
|---|
| Type: 2-col / 3-col / 4-col / Mixed |
| With label |
| Without label |
| Promotional overlay |

---

## Props

| Property | Type | Default | Description |
|---|---|---|---|
| `type` | "2-col" | "3-col" | "4-col" | "mixed" | "3-col" | Grid layout variant |
| `tiles` | ImageTile[] | [] | Array of {image, label, href} objects |
| `showLabel` | boolean | true | Show overlaid label on tile |

---

## Usage

### Do
- Use for category navigation on home page and landing pages.
- Keep tile images consistent in aspect ratio.
- Provide meaningful alt text for every tile image.

### Don't
- Don't use more than 6 tiles in a single row on desktop.
- Don't use decorative-only tiles without a clear destination.
- Don't overlay light text on light images.


---

## Accessibility

- Every tile is a link — use `<a>` with descriptive text.
- Image alt text describes the destination category.
- Decorative overlays use `aria-hidden`.


---

## Tokens Used

- `borderRadius.S`
- `typography.heading.XS`
- `spacing.S`
- `spacing.M`

