# Spacing

The spacing system is built on an **8px base grid**. All spacing values are multiples of this base unit, ensuring visual consistency and alignment across the entire UI.

| Token | Value | Multiplier |
|---|---|---|
| `spacing.2XS` | 2px | 0.25x |
| `spacing.XS` | 4px | 0.5x |
| `spacing.S` | 8px | 1x |
| `spacing.M` | 12px | 1.5x |
| `spacing.L` | 16px | 2x |
| `spacing.XL` | 24px | 3x |
| `spacing.2XL` | 32px | 4x |
| `spacing.3XL` | 40px | 5x |
| `spacing.4XL` | 48px | 6x |
| `spacing.5XL` | 56px | 7x |
| `spacing.6XL` | 64px | 8x |
| `spacing.7XL` | 72px | 9x |
| `spacing.8XL` | 80px | 10x |
| `spacing.9XL` | 88px | 11x |
| `spacing.10XL` | 96px | 12x |
| `spacing.11XL` | 104px | 13x |
| `spacing.12XL` | 112px | 14x |

---

## Usage Guidelines

- Use spacing tokens for margins, padding, gaps, and component internal spacing.
- The most common spacing values are `S` (8px), `M` (12px), and `L` (16px).
- Use `2XS` (2px) and `XS` (4px) only for tight intra-component spacing (e.g., icon-to-label gap).
- Values above `4XL` (48px) are reserved for page-level layout and section separation.

## Do

- Apply spacing consistently — don't mix token-based and hard-coded values.
- Use `S` (8px) as the default internal padding unit for compact components.
- Use `XL` (24px) as the default gap between form fields.

## Don't

- Don't use arbitrary pixel values — always pick the nearest token.
- Don't use spacing tokens for border widths or border radius — use those specific tokens.
