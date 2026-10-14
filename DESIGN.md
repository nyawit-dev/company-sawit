# DESIGN.md

Design direction for PT Perkebunan Asap Emas Nusantara. The company and every
image on this site are fiction, and the pages say so.

## The form

A listed plantation company's annual report site. This is deliberately the
most conventional corporate form there is: full-bleed hero photograph with a
headline over it, an emblem seal, a stat strip, a certification badge row,
photo-led sections, a board table, a contact block with an address.

The satire is in the copy, not in the form. The more convincing the shape,
the harder the sentences land. Nothing here is designed to look like a
concept piece.

## Identity

**Emblem.** An engraved circular seal: forest field, gold ring, curved text
reading `PERKEBUNAN ASAP EMAS` over `SEJAK 1998`, and a charge of a palm
trunk with a fruit bunch and five swept fronds. Drawn as SVG so it stays
crisp at any size. Below ~96px the seal's ring text and frond detail stop
being legible, so the site swaps in `logo-mark.svg`: the same trunk, bunch,
and fronds on the same field, with the ring text dropped rather than shrunk
into a gold smear.

**Palette.** Two core colours and one accent, plus neutrals.

| Token | Light (the filing) | Dark (the land) |
|---|---|---|
| page | `#F4F1EA` paper | `#12110D` char |
| raised | `#FBF9F3` | `#1B1A14` |
| ink | `#1C1A17` | `#EDE9DC` |
| muted | `#5C5A52` | `#9A9689` |
| accent | `#2C4A34` forest | `#E07A4A` ember |
| seal gold | `#C9A227` | `#C9A227` |
| control border | `#7D7867` | `#6E6B57` |

Gold is reserved for the emblem and the certification badges, where a
company seal would use it. It is never a text colour.

**Typography.** Self-hosted, no third-party request at runtime:

- **Newsreader** (optical-size serif) for the corporate voice and every
  headline. An old-style book face in the register of a filed document.
- **IBM Plex Mono** for the ledger, stat strip, tables, labels, and nav.

Latin subset only, ~300KB across four files.

## Two registers

The whole design rests on one idea: the company writes about itself in a
clean corporate voice, and the land it is describing is on fire.

**Register A, Berkas (the filing).** Light, paper, ruled lines. For the
company talking about itself: the stat strip, identity, history,
certifications, vision, mission, commitments, contact.

**Register B, Lahan (the land).** Char and ember with heavier rules. For the
land and what happened to it: the hero, the numbers register, the clearing
process, the fire photograph.

The reader crosses between them by scrolling, which is the same motion as
reading down a filing. Nothing animates to mark the crossing.

## Photography

Five generated photographs, each captioned as generated on the page where it
appears:

- `hero-aerial.jpg` the hero: aerial plantation grid with a band of
  remaining forest at the top edge.
- `clear-cut.jpg` freshly cleared rows with charred stumps, for the clearing
  process.
- `fire.jpg` peatland fire on the concession horizon, for the section that
  names it.
- `mill.jpg` the mill at dusk, for the operations section.
- `ffb.jpg` a fruit bunch on a harvesting truck, for the product section.

Every photograph carries `width` and `height` so the page does not reflow
while loading.

## Dials

ENERGY 2 / RHYTHM 2 / MOTION 1.

ENERGY 2 because the design is layered and confident: full-bleed imagery, a
real emblem, a stat strip, badge row, tabular data. RHYTHM 2 because
compositions vary between the two registers while staying consistent inside
each. MOTION 1 because a filed document does not move: hover and focus
states only, no scroll animation, no loops, no reveal.

## Structure

Navigation splits the site the way the company splits its own paperwork:

- **Beranda**: the hero claim, the stat strip, the numbers, the clearing
  process, the fire, the product, contact.
- **Tentang**: who the company says it is. Identity, history, the mill,
  certifications, the board.
- **Visi & Misi**: the vision statement, the missions, the values, the
  commitments.

Every navigation item leads to a page that exists. Nothing is marked coming
soon.

## Honesty

Every figure is presented as the company's own self-reported claim and is
labelled as such where it appears. No named people, no testimonials, no
invented sources, no certification bodies named. Photographs are generated
and say so in their captions. The fiction notice appears on every page and
in the footer.
