# Select Menu

A form input that presents a single-select dropdown of predefined options. For rich filtering or multi-select use cases, see Dropdown or Combobox.

**Figma variant properties:** Style=Filled/Outlined

---

## Preview

> Component preview image — to be added manually from Figma export.

---

## Variants

| Variant |
|---|
| Style: Filled / Outlined |
| Default |
| Focused |
| Open |
| Selected |
| Disabled |
| Error |

---

## Props

| Property | Type | Default | Description |
|---|---|---|---|
| `options` | Option[] | [] | Array of {value, label} objects |
| `value` | string | null | Selected value |
| `label` | string | "" | Field label |
| `placeholder` | string | "Select..." | Placeholder text |
| `style` | "filled" | "outlined" | "outlined" | Visual style |
| `disabled` | boolean | false | Disabled state |
| `error` | boolean | false | Error state |
| `errorMessage` | string | null | Error message |

---

## Usage

### Do
- Use for selecting one option from a defined list in a form.
- Always include a visible label.
- Include a neutral placeholder (not a valid option).

### Don't
- Don't use Select for more than 10 options without search — use Combobox.
- Don't use Select for non-form actions — use Dropdown.
- Don't pre-select an option when no default exists.


---

## Accessibility

- Associate `<label>` with `<select>` via `for`/`id`.
- `aria-invalid` on error.
- `aria-describedby` for error message.
- Keyboard: space to open, arrows to navigate, Enter to select.


---

## Tokens Used

- `color.semantic.Background.Primary`
- `color.semantic.Border.Primary`
- `color.semantic.Border.Focus`
- `borderRadius.S`
- `typography.text.M.regular`
- `spacing.M`

