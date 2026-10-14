# DESIGN.md

Design direction for PT Perkebunan Asap Emas Nusantara. The site is fiction
and says so on every page.

## Identity

A palm oil company's own annual report, written by the people who cleared the
forest. The register is corporate and calm; the content is arson and eviction.
The gap between the two is the site.

## Two registers

The whole design rests on one idea: the company writes about itself in a clean
corporate voice, and the land it is describing is on fire. Two visual
registers, never mixed inside one block:

**Register A: Berkas (the filing).** Light, paper, ruled lines. Used for the
company talking about itself: identity, vision, mission, certifications, the
contact page. Palette: paper `#F4F1EA`, ink `#1C1A17`, forest `#2C4A34`,
control border `#7D7867`.

**Register B: Lahan (the land).** Dark, burnt, heavier rules, tighter
leading. Used for the land and what happened to it: the opening claim, the
numbers register, the clearing process. Palette: char `#12110D`, bone
`#EDE9DC`, ember `#E07A4A`, control border `#6E6B57`.

The reader crosses between them by scrolling, which is the same motion as
reading down a filing. Nothing animates to mark the crossing; the colour
change is the signal.

Accent is used in three places only: the company's own claim in the numbers
register, the primary button, and the focus ring.

## Typography

Two families, both self-hosted (no third-party request at runtime):

- **Newsreader** (optical-size serif) for everything the company says about
  itself, and every headline. An old-style book face in the register of a
  corporate filing: it reads as institutional and slightly dated, which is
  what a company writing its own history sounds like.
- **IBM Plex Mono** for the data, labels, section numbers, and the land
  register's sub-labels. It carries the ledger, the tables, and the filing's
  apparatus.

Weights shipped: Newsreader 400-700 variable (roman + italic), Plex Mono 400
and 500. Latin subset only, ~300KB total.

## Dials

ENERGY 2 / RHYTHM 2 / MOTION 1.

ENERGY 2 because the design is confident and layered (two registers, a real
grid, optical-size display type) but never shouts. RHYTHM 2 because section
compositions vary between the two registers while staying consistent inside
each. MOTION 1 because a corporate filing does not move: hover and focus
states only, no scroll animation, no loops, no reveal.

## Structure

Navigation splits the site the way the company splits its own paperwork:

- **Beranda**: the claim, the numbers, the clearing process, contact.
- **Tentang**: who the company says it is. History, certifications, the
  board. Register A.
- **Visi & Misi**: the mission statement, the values, the commitments.
  Register A, and the page where the corporate voice is least able to hide
  what it is saying.

Every navigation item leads to a page that exists. Nothing is marked coming
soon.

## Honesty

Every figure is presented as the company's own self-reported claim and is
labelled as such on the page. No named people, no testimonials, no invented
sources. The fiction notice appears on every page and in the footer.
