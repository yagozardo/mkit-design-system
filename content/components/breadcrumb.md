# Breadcrumb

A navigational aid that shows a user's current location within the site hierarchy and provides links back to each parent level. Especially important in deep category trees.

**Figma variant properties:** Device=Desktop/Mobile, Clickable=Yes/No

---

## Preview

> Component preview image — to be added manually from Figma export.

---

## Variants

| Variant |
|---|
| Desktop |
| Mobile (truncated) |
| Clickable items |
| Current page (non-link) |

---

## Props

| Property | Type | Default | Description |
|---|---|---|---|
| `items` | BreadcrumbItem[] | [] | Array of {label, href} objects; last item has no href |
| `device` | "desktop" | "mobile" | "desktop" | Responsive variant |
| `separator` | string | "/" | Separator character between items |

---

## Usage

### Do
- Include breadcrumbs on all pages below the homepage.
- Mark the current page item as non-linked.
- Truncate long paths on mobile, showing at least one parent.

### Don't
- Don't use breadcrumbs on the homepage or single-level sites.
- Don't duplicate the page `<h1>` in the last breadcrumb item — keep them in sync.


---

## Accessibility

- Wrap in `<nav aria-label='Breadcrumb'>`.
- Use `<ol>` with `<li>` items.
- `aria-current='page'` on the last item.
- Separator characters are decorative — hide with `aria-hidden`.


---

## Tokens Used

- `color.semantic.Content.Link`
- `color.semantic.Content.Secondary`
- `typography.text.S.regular`
- `spacing.XS`

