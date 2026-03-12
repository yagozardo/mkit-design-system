# Motion

> **Note:** Motion tokens are not currently defined in the Figma Tokens file. This page documents the intended motion system for future implementation.

Motion reinforces spatial relationships, communicates state changes, and guides user attention. All animations must respect the user's `prefers-reduced-motion` setting.

---

## Principles

1. **Purposeful** — Every animation communicates something (state change, hierarchy, causality).
2. **Subtle** — Motion supports the UI; it never competes for attention.
3. **Accessible** — All animated elements provide a no-motion fallback.

---

## Intended Token Structure (Pending)

| Token | Intended Value | Usage |
|---|---|---|
| `motion.duration.instant` | 0ms | No-motion fallback |
| `motion.duration.fast` | 100ms | Micro-interactions (button press, checkbox) |
| `motion.duration.default` | 200ms | Component transitions (dropdown open, tooltip appear) |
| `motion.duration.slow` | 300ms | Page-level transitions, modals |
| `motion.duration.slower` | 500ms | Complex animations (onboarding, loading sequences) |
| `motion.easing.standard` | cubic-bezier(0.4, 0, 0.2, 1) | General UI transitions |
| `motion.easing.decelerate` | cubic-bezier(0, 0, 0.2, 1) | Elements entering the screen |
| `motion.easing.accelerate` | cubic-bezier(0.4, 0, 1, 1) | Elements leaving the screen |

---

## Accessibility

Always include:
```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }
}
```
