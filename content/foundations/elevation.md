# Elevation

Elevation communicates the relative depth of components using box shadows. The system defines 6 levels (L1–L6), from subtle surface lifts to prominent modal overlays.

> **Note:** Shadow CSS values (L1–L6) are pending extraction from the Base Components Figma file. This page will be updated when those values are available.

| Level | Usage |
|---|---|
| L1 | Cards, list items — subtle lift above background |
| L2 | Dropdowns, popovers — clearly elevated |
| L3 | Sticky headers, floating action buttons |
| L4 | Drawers, sidesheets — high elevation panels |
| L5 | Modals, dialogs — primary overlay layer |
| L6 | Tooltips, notification toasts — topmost layer |

---

## Usage Guidelines

- Choose elevation based on the **interaction level** of the component, not aesthetic preference.
- Higher elevation implies a stronger interruption of the user's flow — use sparingly.
- Combine elevation with `Background/Inverse` for surfaces that need to visually lift above the dark primary background.

## Do

- Use L1–L2 for inline elevated components (cards, panels).
- Use L4–L5 for overlays that block background interaction.
- Ensure elevated components have sufficient contrast with their backdrop.

## Don't

- Don't stack high-elevation components (e.g., a modal over a drawer over a popover).
- Don't use elevation as the only differentiator between component states.
