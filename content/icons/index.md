# Icons

The eComm Design System uses the **Lucide** open-source icon library. Lucide provides consistent, clean line icons in SVG format and is available as an npm package.

- **Source:** [lucide.dev/icons](https://lucide.dev/icons/)
- **Style:** Outlined, 24×24px grid, 2px stroke
- **License:** ISC (open source)

---

## Usage

### In Figma
Icons are available directly through the Lucide plugin in Figma. Search by name and insert at 16px, 20px, or 24px.

### In Code
```bash
npm install lucide-react  # React
npm install lucide        # Vanilla JS / SVG sprites
```

```jsx
import { ShoppingCart, Search, ChevronDown } from 'lucide-react'

<ShoppingCart size={24} strokeWidth={2} />
```

### Token Pairing
Always use the appropriate semantic color token for icons:
- Default icons: `color.semantic.Content.Primary`
- Interactive icons: `color.semantic.Content.Link`
- Disabled icons: `color.semantic.Content.Disabled`
- Brand icons: `color.semantic.Content.Brand`

---

## Sizing

| Size | px | Use |
|---|---|---|
| XS | 16px | Inline with text (inside buttons, tags, inputs) |
| S  | 20px | UI controls and navigation items |
| M  | 24px | Default standalone icons |
| L  | 32px | Empty states and hero illustrations |

---

## Common Icons

| Name | Usage |
|---|---|
| `shopping-cart` | Cart / add-to-cart actions |
| `search` | Search bar trigger |
| `user` | Account/profile |
| `menu` | Mobile hamburger |
| `x` | Close / dismiss |
| `chevron-down` | Dropdowns, accordions |
| `chevron-right` | Breadcrumbs, nested navigation |
| `check` | Success states, checkboxes |
| `alert-circle` | Error / warning states |
| `info` | Info tips and tooltips |
| `plus` | Add actions |
| `minus` | Remove / decrement |
| `map-pin` | Location / branch finder |
| `phone` | Contact |
| `truck` | Shipping / delivery |
| `package` | Orders / products |

---

> Full interactive icon browser — to be generated in Phase 4 from the Lucide npm package.
