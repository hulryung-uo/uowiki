# UO Tavern — Design System

One product, three sites, one tone. The landing **hub** (`www.uotavern.com`, static
HTML), the **wiki** (`/wiki`, Astro + Starlight) and the **forum** (`/forum`,
Next.js + Tailwind) must look and feel like a single site. This document is the
**single source of truth** for that consistency.

> **Golden rule:** never hand-pick a colour, font, or spacing value in a component.
> Use a token from `uo-design.css`. If a value is missing, add it to the token file
> (and this doc) first, then use it.

## The canonical token file

`uo-design.css` defines every design token as a CSS custom property, plus the
shared `.uo-globalbar` component. It is **byte-identical** in all three repos:

| Repo | Path |
| --- | --- |
| hub | `uohub/uo-design.css` |
| wiki | `uowiki/src/styles/uo-design.css` |
| forum | `uotavern/src/app/uo-design.css` |

When you change tokens, change them in **one** repo, then copy the file verbatim to
the other two (`cp`), and rebuild all three. Do not let them drift.

## Tokens

### Colour — dark parchment-on-ink with gold

| Token | Value | Use |
| --- | --- | --- |
| `--uo-bg` | `#0b0a12` | page background (ink) |
| `--uo-bg-elev` | `#131120` | elevated band / alt section |
| `--uo-panel` | `#16131f` | card / panel surface |
| `--uo-panel-translucent` | `rgba(22,19,34,.72)` | panel over imagery |
| `--uo-line` | `rgba(217,179,92,.22)` | **gold hairline border** (default) |
| `--uo-line-soft` / `--uo-line-strong` | `.12` / `.40` | softer / stronger hairline |
| `--uo-gold` | `#d9b35c` | links, accents |
| `--uo-gold-bright` | `#f0cd7a` | hover / active |
| `--uo-gold-dim` | `#c7a46b` | secondary gold |
| `--uo-ink` | `#ece3cf` | primary text (parchment) |
| `--uo-ink-dim` | `#b9ad92` | muted text |
| `--uo-parch` | `#efe3c4` | warm highlight |
| `--uo-white` | `#f6efdc` | headings / strongest text |

Borders are **gold hairlines**, never grey. Surfaces are dark; there is **no light
mode** — the wiki forces dark to match.

### Type

| Token | Stack | Use |
| --- | --- | --- |
| `--uo-font-display` | `Cinzel, 'EB Garamond', Georgia, serif` | all headings, brand, site title |
| `--uo-font-body` | `'EB Garamond', Georgia, serif` | body copy (all three sites) |
| `--uo-font-rune` | `'Britannian', serif` | runic flourishes ("Britannia", mantras) |
| `--uo-font-mono` | system mono | code, IDs, item numbers |

`Cinzel` + `EB Garamond` load from Google Fonts via the `@import` at the top of
`uo-design.css`. **`Britannian` is a local font** (`/fonts/britannian-runic.ttf`),
so its `@font-face` is declared **per-site** (the URL differs: `/fonts/…` on the hub
and forum, `/wiki/fonts/…` on the wiki).

Headings use `--uo-font-display`; body text uses `--uo-font-body`. Both are serif —
the look is a classical illuminated book, not a modern sans UI.

### Geometry

`--uo-radius` 12px · `--uo-radius-sm` 7px · `--uo-shadow` `0 10px 30px rgba(0,0,0,.4)`
· `--uo-maxw` 1140px · `--uo-gutter` 24px · `--uo-navh` 56px · `--uo-bp-sm` 640px.

## The global bar (`.uo-globalbar`)

Every page on every site starts with the same bar so navigation between the three
feels like one app. Markup contract (render this structure in each stack — JSX,
Astro, or HTML — the styling lives in `uo-design.css`):

```html
<div class="uo-globalbar">
  <div class="uo-globalbar__inner">
    <a class="uo-globalbar__brand" href="https://www.uotavern.com/">
      UO Tavern <span class="uo-globalbar__rune">Britannia</span>
    </a>
    <nav class="uo-globalbar__nav">
      <a href="https://www.uotavern.com/">Home</a>
      <a class="is-active" href="https://www.uotavern.com/wiki/">Wiki</a>
      <a href="https://www.uotavern.com/forum/">Forum</a>
    </nav>
  </div>
</div>
```

Set `is-active` on the link for the current site. Links are **absolute** hub URLs
(so they work behind the path proxy). On mobile (`≤640px`) the rune hides and the
nav tightens — handled by `uo-design.css`, no per-site work needed.

## Responsive rules

- Mobile-first; the only hard breakpoint is `--uo-bp-sm` (640px).
- **Never allow horizontal overflow.** Every site sets
  `html, body { overflow-x: hidden; max-width: 100%; }` and wide elements
  (tables, code blocks, image rows) get `overflow-x: auto` on a wrapping container,
  not on the page.
- Content max-width is `--uo-maxw` (1140px), centred, with `--uo-gutter` side
  padding that shrinks to 16px on mobile.
- Tap targets ≥ 40px tall.

## Per-stack wiring

### Hub (static HTML) — `uohub/`
`<link rel="stylesheet" href="/uo-design.css">` in `<head>`. Local styles use
`var(--uo-*)` tokens. Declare the `Britannian` / `UOAscii` `@font-face` locally
(`/fonts/…`). Render `.uo-globalbar` markup directly.

### Wiki (Astro + Starlight) — `uowiki/`
Add both stylesheets to `astro.config.mjs` `customCss`:
`['./src/styles/uo-design.css', './src/styles/theme.css', './src/styles/sprites.css']`.
`theme.css` **maps tokens → Starlight variables** (`--sl-color-*` ← `--uo-*`),
forces dark, applies `--uo-font-display` to headings and `--uo-font-body` to text,
and hides the theme toggle. The global bar lives in the `Header.astro` component
override and uses the shared `.uo-globalbar` classes. `Britannian` `@font-face`
points at `/wiki/fonts/…`.

### Forum (Next.js + Tailwind) — `uotavern/`
`@import './uo-design.css';` at the top of `globals.css`. Tailwind's `uo-*` colour
and font utilities are mapped to the tokens in `tailwind.config` (e.g.
`colors['uo-bg'] = 'var(--uo-bg)'`), so existing `bg-uo-bg` / `text-uo-gold`
utilities resolve to the shared tokens. The `GlobalBar` component emits the shared
`.uo-globalbar` markup. Body font is `--uo-font-body`.

## Checklist when touching design

1. Change values in `uo-design.css` only; copy to all three repos.
2. Update this file if you add/rename a token.
3. Rebuild and screenshot **all three** sites at desktop (1280) **and** mobile (390).
4. Confirm: no horizontal scroll, gold hairlines (not grey), Cinzel headings,
   parchment text on `#0b0a12`, the global bar identical everywhere.
