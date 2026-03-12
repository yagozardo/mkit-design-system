# Country Badge

A flag-and-label badge indicating country/locale context. Used in international eCommerce contexts to denote language, shipping region, or store locale.

**Figma variant properties:** Language=ENG-USA/ESP-Mexico/PT-Brazil

---

## Preview

> Component preview image — to be added manually from Figma export.

---

## Variants

| Variant |
|---|
| ENG-USA |
| ESP-Mexico |
| PT-Brazil |

---

## Props

| Property | Type | Default | Description |
|---|---|---|---|
| `locale` | string | "ENG-USA" | Locale code (e.g., ENG-USA, ESP-MX) |
| `showLabel` | boolean | true | Show locale label alongside flag |

---

## Usage

### Do
- Use in header/account areas to show the active locale.
- Always show flag + label for clarity.

### Don't
- Don't use Country Badge as a standalone language switcher — pair with a Select.
- Don't use flag alone to represent language.

---

## Accessibility

- Include accessible label with country name for screen readers.
- Don't use flag emoji alone — not reliably supported.

---

## Tokens Used

- `borderRadius.XS`
- `typography.text.XS.semibold`
- `spacing.XS`
