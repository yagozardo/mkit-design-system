# Typography

Two typefaces define the system's typographic voice:

| Role | Font | Weights Used |
|---|---|---|
| Headings | **Satoshi** | Bold (700) |
| Body / UI | **Inter** | Regular (400), Semibold (600) |

---

## Heading Scale

All headings use **Satoshi Bold**. Letter spacing tightens at larger sizes for optical correction.

| Token | Size | Line Height | Weight | Family | Letter Spacing |
|---|---|---|---|---|---|
| Heading/5XL | 72px | 80px | 700 | Satoshi | -1px |
| Heading/4XL | 64px | 72px | 700 | Satoshi | -1px |
| Heading/3XL | 56px | 64px | 700 | Satoshi | -1px |
| Heading/2XL | 48px | 56px | 700 | Satoshi | -1px |
| Heading/XL | 40px | 48px | 700 | Satoshi | -1px |
| Heading/L | 32px | 40px | 700 | Satoshi | -1px |
| Heading/M | 24px | 32px | 700 | Satoshi | -0.5px |
| Heading/S | 20px | 28px | 700 | Satoshi | -0.5px |
| Heading/XS | 16px | 24px | 700 | Satoshi | -0.5px |
| Heading/2XS | 14px | 20px | 700 | Satoshi | 0px |

---

## Text Scale

All body/UI text uses **Inter**. No letter spacing adjustments.

| Token | Size | Line Height | Weight | Family | Letter Spacing |
|---|---|---|---|---|---|
| Text/XL/Regular | 18px | 26px | 400 | Inter | 0px |
| Text/XL/Semibold | 18px | 26px | 600 | Inter | 0px |
| Text/L/Regular | 14px | 20px | 400 | Inter | 0px |
| Text/L/Semibold | 14px | 20px | 600 | Inter | 0px |
| Text/M/Regular | 12px | 16px | 400 | Inter | 0px |
| Text/M/Semibold | 12px | 16px | 600 | Inter | 0px |
| Text/S/Semibold | 12px | 16px | 600 | Inter | 0px |
| Text/XS/Regular | 10px | 14px | 400 | Inter | 0px |
| Text/XS/Semibold | 10px | 14px | 600 | Inter | 0px |

---

## Usage Guidelines

- Use heading tokens for page titles, section headers, and component labels.
- Use **Text/L** (14px) for standard body copy and default input text.
- Use **Text/M** (12px) for secondary labels, captions, and helper text.
- Use **Text/XS** (10px) for badges, tags, and meta information only.
- Never use heading styles below Heading/XS for UI elements — use Text styles instead.

## Do

- Maintain the defined line heights — don't override them.
- Use **Semibold** for labels, button text, and any emphasis within body copy.

## Don't

- Don't use Satoshi for body text or Inter for headings.
- Don't create intermediate sizes outside the scale.
