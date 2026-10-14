# PT Perkebunan Asap Emas Nusantara

Company profile site for a fictional palm oil company, built as satire. The
company does not exist, and neither do the numbers, events, or claims on the
page. The site's subject is how such a company writes about itself.

Built with Nuxt 4 and bun, deployed to GitHub Pages by
`.github/workflows/deploy.yml`. Pushes to `main` build and publish; pull
requests build only.

## Local

```bash
bun install
bun run dev       # dev server
bun run generate  # static output in .output/public
```

`scripts/serve-static.py` serves `.output/public` with correct MIME types for
the click-through check. The npm `serve` package returns `text/html` for every
file on this machine, which stops the browser from running the Nuxt entry as a
module.

## Design

`DESIGN-NOTES.md` records every major decision and its reason. The site was
built without a `DESIGN.md`, so it is labelled a draft without direction and
runs the honest dials ENERGY 1 / RHYTHM 1 / MOTION 1.
