# Tree View

A hierarchical list that displays nested data structures. Nodes can be expanded or collapsed to reveal children. Used for category navigation, file structures, and org charts.

**Figma variant properties:** Open/Closed=Open/Closed

---

## Preview

> Component preview image — to be added manually from Figma export.

---

## Variants

| Variant |
|---|
| Open (expanded) |
| Closed (collapsed) |
| With icons |
| With checkboxes (multi-select) |
| Single-select |

---

## Props

| Property | Type | Default | Description |
|---|---|---|---|
| `nodes` | TreeNode[] | [] | Nested data: {id, label, icon?, children?} |
| `expanded` | string[] | [] | IDs of currently expanded nodes |
| `selected` | string | null | ID of selected node |
| `multiSelect` | boolean | false | Allow multiple selections via checkboxes |

---

## Usage

### Do
- Use only for genuinely nested hierarchical data.
- Add a filter/search for large trees (>20 nodes).
- Show expand/collapse state with a chevron icon.

### Don't
- Don't use for flat lists — use a standard list or Table.
- Don't default all nodes to expanded if the tree is large.
- Don't use trees where a simpler nested list would suffice.


---

## Accessibility

- `role='tree'` on root `<ul>`.
- `role='group'` on nested lists.
- `role='treeitem'` on each `<li>`.
- `aria-expanded` on parent nodes.
- Arrow keys: right = expand, left = collapse, up/down = navigate.


---

## Tokens Used

- `color.semantic.Content.Primary`
- `color.semantic.Content.Link`
- `color.semantic.Background.Tonal`
- `typography.text.M.regular`
- `spacing.S`
- `spacing.M`

