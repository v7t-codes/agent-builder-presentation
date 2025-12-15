# Final Presentation: Agent OS & Agent Builder Market Map

This folder is the canonical, reader-friendly narrative and market map in one place.

## Presentation

- Deck order (dynamic): `deck.md`
- React presentation: `presentation.html`
- Slide index (derived from deck): `INDEX.md`

## Run locally

Recommended (works from anywhere):

```bash
cd agent-builder-tools/final-presentation
./serve.sh
```

It prints (and auto-opens) the exact URL, e.g.:

- `http://localhost:8001/agent-builder-tools/final-presentation/presentation.html`

Manual option (from the repo root):

- `python -m http.server 8001`
- Then open `http://localhost:8001/agent-builder-tools/final-presentation/presentation.html`

## Structure

- **One slide = one `*.md` file.**
- **One part = one folder**: `part-0-framing/`, `part-1-market-segments/`, `part-2-summary/` (older parts/slides moved to `../Archive/`).
- `deck.md` is the only source of truth for presentation order (the presentation reads it at runtime).
- Tables that include a `Company` column auto-render logos from `assets/logos/<slug>.(svg|png|jpg|jpeg)` (fallback: `assets/logos/_placeholder.svg`).
