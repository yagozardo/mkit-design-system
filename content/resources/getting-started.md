# Getting Started

## For Designers

### 1. Enable the Figma Libraries
In any Figma file, open the Assets panel (⌥2) → click the book icon → search for:
- **Tokens** — color, typography, spacing, and border variables
- **Base Components** — core UI building blocks
- **Advanced Components** — eCommerce-specific patterns

### 2. Use Variables, Not Raw Values
Always apply tokens from the Variables panel rather than hard-coding hex values or pixel sizes. This ensures your work stays in sync with the system and adapts to future theme changes.

### 3. Naming Convention
Figma component variants follow the pattern: `Property=Value, Property=Value`  
Example: `State=Hover, Size=M, Type=Primary`

---

## For Developers

### Tokens
All design tokens are available as `assets/tokens.json`. This file is the single source of truth for all color, typography, spacing, and layout values.

```json
// Color example
tokens.color.primitive.Blue["50"]  // → "#0072CF"
tokens.color.semantic.Background.Primary  // → "#191C1E"

// Typography example
tokens.typography.heading["XL"]  // → { fontSize: 40, lineHeight: 48, fontWeight: 700 }

// Spacing example
tokens.spacing.L  // → 16 (px)
```

### Figma File Keys
| Library | File Key |
|---|---|
| Tokens | `6HCZSlgXsmODj59ldL9IkA` |
| Base Components | `cBzqjlyUoVJczHoLvQPXS9` |
| Advanced Components | `rF3f8JHhAXJ4wI8X3PMKpJ` |

---

## Contributing
All changes to the design system go through the Winsupply Marketing IT UX Design Team. Open a ticket or Slack the team before making additions or modifications.
