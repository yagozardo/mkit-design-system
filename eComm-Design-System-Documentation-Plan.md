# eCommerce Design System Documentation Site — Step-by-Step Plan

> **Goal:** Use Claude Code with Figma MCP to scan 4 Figma files, extract tokens/variables/components, and generate a brand new design system documentation site.

---

## Phase 0 — Prerequisites & Environment Setup

### 0.1 — Set up Figma MCP in Claude Code
Claude Code supports MCP (Model Context Protocol) servers. Configure the Figma MCP server so that Claude Code can talk directly to your Figma files. The most reliable option today is the community-maintained `figma-mcp` server (or Figma's own official MCP, if you have access to the beta). Add it to your Claude Code `settings.json` under `mcpServers`, passing your Figma personal access token.

### 0.2 — Gather your Figma file IDs
Collect the exact file keys (the string in the Figma URL after `/file/`) for each of your 4 Figma files. Label them clearly — e.g., `tokens-file`, `components-file`, `icons-file`, `patterns-file` — so the scanning prompts can target each one precisely.

### 0.3 — Create a personal access token in Figma
If you don't already have one, generate a token in Figma's account settings with read access to those files. Store it securely (not hardcoded into any committed file).

### 0.4 — Decide on the output format early
Before scanning anything, agree on your target output. The most likely candidates are:

- A **static HTML/CSS/JS site** — easiest to host anywhere, no build pipeline needed
- A **Next.js or Astro site** — more scalable, better for a living system
- A **Notion or Confluence page** — lower effort, less custom

> **Recommendation:** Static HTML with Tailwind is the lowest-friction path that still looks professional, unless your team already uses a JS framework.

---

## Phase 1 — Figma File Scanning & Data Extraction

### 1.1 — Extract design tokens (variables)
For each of the 4 files, use the MCP to call the Figma Variables API endpoints. This returns:

- Color tokens (primitives and semantic aliases)
- Typography tokens (font family, size, weight, line height, letter spacing)
- Spacing tokens
- Border radius tokens
- Shadow/elevation tokens
- Opacity tokens
- Motion/animation tokens (if present)

Output: a raw JSON dump per file, then merged into a single canonical token map.

> ⚠️ *Note: Figma's Variables API has access constraints depending on your plan tier — verify that your account can read variables programmatically before starting.*

### 1.2 — Extract component inventory
Use the MCP to call the Figma components/component sets API for each file. For every component, capture:

- Component name and key
- Description (if written in Figma, even partial)
- Containing page
- Variant properties and their values
- Documented props/states (from component properties panel)
- Whether it belongs to a component set (i.e., has variants)

Output: a structured JSON inventory of all components across all 4 files.

### 1.3 — Extract color styles & text styles
Even if you're using variables, Figma separates "styles" from "variables." Pull both, since many components may reference styles rather than variables. Merge duplicates intelligently.

### 1.4 — Capture component previews (images)
Use the Figma Images API (also accessible via MCP) to render a PNG or SVG export of each component at a standard resolution (e.g., 2x). Store these as assets — they'll be used as visual swatches in the docs site.

> ⚠️ *This step can be time-consuming and API-quota-heavy for large component libraries — plan for batching.*

### 1.5 — Validate and clean the raw data
After extraction, Claude Code runs a pass to:

- Identify orphaned tokens (defined but not used by any component)
- Flag components with empty descriptions
- Detect naming inconsistencies (e.g., mixed casing conventions)
- Surface duplicate or near-duplicate components

Output: a cleaned JSON dataset + a short audit report highlighting gaps in the current state of the system.

---

## Phase 2 — Research & Design System Inspiration

### 2.1 — Audit reference design systems
Before writing a single line of docs, Claude Code browses and analyzes established design system sites to extract structural patterns. Good references:

- [Shopify Polaris](https://polaris.shopify.com) — especially relevant for eCommerce
- [Google Material Design 3](https://m3.material.io)
- [Atlassian Design System](https://atlassian.design)
- [Carbon Design System (IBM)](https://carbondesignsystem.com)
- [Base Web (Uber)](https://baseweb.design)

What to extract from each: page structure, token documentation format, component page anatomy (usage, anatomy, specs, do/don't), navigation patterns, and code snippet conventions.

### 2.2 — Define your documentation information architecture
Based on the audit and extracted data, map out the site structure. A typical eCommerce design system might look like:

```
Home / Overview
├── Foundations
│   ├── Color
│   ├── Typography
│   ├── Spacing
│   ├── Elevation / Shadows
│   ├── Border Radius
│   └── Motion
├── Components
│   ├── [Each component — auto-generated pages]
├── Patterns (if applicable)
├── Icons
└── Resources / Getting Started
```

This IA drives the auto-generation logic in Phase 3.

---

## Phase 3 — Content Generation

### 3.1 — Generate token documentation pages
Using the cleaned token data from Phase 1, generate the content for each Foundations section:

- **Colors:** visual swatch grid, token name, raw value, and semantic alias chain (e.g., `color.action.primary` → `color.blue.500` → `#1D4ED8`)
- **Typography:** live text specimen at each scale level
- **Spacing:** visual ruler showing each step

### 3.2 — Auto-generate component pages
For each component in the inventory, generate a documentation page with:

- **Overview:** component name, description (from Figma, or AI-drafted if missing)
- **Visual preview:** the exported image from step 1.4
- **Variants:** a grid or tabs showing each variant state
- **Props/API table:** component properties extracted from Figma
- **Usage guidelines:** do/don't examples (Claude Code generates sensible defaults — flagged as *draft, needs review*)
- **Token usage:** which design tokens this component consumes
- **Accessibility notes:** baseline notes based on component type

> ⚠️ *Anything in "Usage guidelines" and "Accessibility notes" should be reviewed and approved by your team before publishing.*

### 3.3 — Write the Overview / Getting Started page
Draft a landing page for the design system covering: what it is, who it's for, how to use the Figma libraries, and any team conventions.

---

## Phase 4 — Site Build

### 4.1 — Choose and scaffold the site template
Based on the format decision in Phase 0.4, scaffold the site. For a static HTML approach: a clean, minimal layout with a left-rail navigation, main content area, and a right-rail token/property inspector. The site should use your actual color and typography tokens — the docs site should eat its own cooking.

### 4.2 — Build the token visualization components
Create reusable HTML/CSS/JS snippets (or React components) for:

- Color swatch card
- Typography specimen block
- Spacing ruler
- Shadow card
- Component preview card with variant switcher

### 4.3 — Auto-generate all pages from the JSON data
Write a script (Node.js or Python) that takes the cleaned JSON from Phase 1 and the content from Phase 3 and renders all pages. This is the key automation step — the goal is that if you update a token in Figma and re-run the scan, the docs regenerate automatically.

### 4.4 — Integrate component images
Place the exported component previews (from step 1.4) into the correct component pages and ensure they load correctly in all contexts.

### 4.5 — Style the site using your actual design tokens
Apply your own color, typography, spacing, and radius tokens to the documentation site itself. This both validates the tokens work and makes the site a living demonstration of the system.

---

## Phase 5 — Review, QA & Iteration

### 5.1 — Internal review pass
Share a preview of the generated site with your team. Specifically flag:

- Pages where component descriptions were AI-generated and need human review
- Token pages where the semantic naming might be confusing
- Any components that were missing from the Figma scan

### 5.2 — Accessibility audit
Run the site through an automated accessibility checker (e.g., axe, Lighthouse) and fix flagged issues. Ensure the documentation site itself meets at least WCAG 2.1 AA.

### 5.3 — Establish a sync/update workflow
Define how the docs stay in sync with Figma going forward:

- **Manual re-scan:** run the MCP scan + regeneration script on a cadence (e.g., monthly)
- **Webhook-triggered:** Figma webhooks can notify a CI/CD pipeline when files change, triggering an automated re-scan and redeploy

---

## Phase 6 — Publishing

### 6.1 — Choose a hosting target
Options range from GitHub Pages (free, easy) to Netlify/Vercel (fast CI/CD) to an internal server behind your company's VPN. Since this is an internal design system for a marketing IT team, a VPN-gated internal host or a password-protected Netlify site are both reasonable.

### 6.2 — Set up the deployment pipeline
Wire up the generation script to deploy automatically on merge to main, or on a scheduled run.

### 6.3 — Announce and onboard the team
Write a short launch doc and walk the team through how to use and contribute to the system documentation.

---

## Risk Register & Honest Uncertainties

| Risk | Likelihood | Notes |
|---|---|---|
| Figma API plan limits | Medium | Variables API and image export may require a paid Figma Organization plan. Verify before committing to this approach. |
| Low component description coverage | High | If Figma files have little or no written descriptions, the auto-generated docs will need significant human review. |
| MCP server stability | Medium | The Figma MCP ecosystem is relatively young. Run a proof-of-concept scan on one file before committing to the full pipeline. |
| Image export volume | Medium | Hundreds of components across 4 files could be slow and rate-limited. Batching and caching will be important. |

---

*Plan created: February 2026 — Winsupply Marketing IT UX Design Team*
