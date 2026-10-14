# DESIGN-NOTES.md

Draft without direction. Dials: ENERGY 1 / RHYTHM 1 / MOTION 1 (antislop R-37).
The owner declined to supply a `DESIGN.md`, so this is not a shippable
deliverable, it is a draft.

## Content status

Fiction. Every company, person, figure, and statement on this site is invented
for satire. A notice to that effect is visible on the page itself.

## Decisions and their reasons

- **Serif headline stack, system only (Georgia, Iowan Old Style, Charter).**
  The site reads like a company filing or a newspaper report, so the headline
  voice is editorial and print-like. No webfont is downloaded: the site has no
  network dependency, no FOUT, and no render-blocking request, which is the
  honest choice for a static GitHub Pages build.
- **Palette: paper + forest green + burnt orange.**
  Paper (`#F4F1EA`) is the document. Forest green is the thing being cut.
  Burnt orange (`#AB3F19` light, `#E07A4A` dark) is the fire, and it is the
  only accent on the page: it marks the one thing the site is about, and
  nothing else. Both accents were darkened until every pairing passed 4.5:1
  on both the paper and the raised surface.
- **Ledger row structure instead of cards.**
  The subject is a company and its filings, so sections are ruled rows in a
  register with a number, not a grid of feature cards. It is the composition
  the content asks for.
- **Numbers presented as the company's own self-reported claims.**
  They are fictional by design and labelled as such on the page. No figure is
  presented as independently sourced, because none is.
- **No named people and no testimonial section.**
  Inventing people to quote would be fabrication dressed as evidence. The
  company's own voice carries the satire instead.
- **Bracketed greenwashing phrases, set apart and marked.**
  Corporate filler is the subject of the joke, so it appears as the company's
  own wording, set in a distinct style and attributed to the fictional
  company. The site's own copy stays plain.
- **Motion: hover and focus states only.**
  A corporate filing does not move. No scroll animation, no loops, no
  parallax, no reveal.
- **Both themes ship and both are tested.**
  The site is content-first with no brand reason for a fixed dark theme, so
  the light/dark toggle is built rather than deferred, and every pair of
  colours was contrast-checked in both modes.
