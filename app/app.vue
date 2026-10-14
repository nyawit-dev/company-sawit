<template>
  <div>
    <a class="skip-link" href="#konten">Lompat ke konten</a>

    <header class="masthead">
      <div class="wrap masthead__row">
        <!-- The mark is not a nav item, so it must not carry aria-current:
             NuxtLink to="/" matches the home route and would announce the logo
             as the current page to a screen reader. -->
        <NuxtLink class="masthead__brand" to="/" :aria-current="undefined">
          <img
            class="masthead__seal"
            :src="'/company-sawit/logo-mark.svg'"
            alt=""
            width="44"
            height="44"
          />
          <span class="masthead__name">
            PT Perkebunan Asap Emas Nusantara
            <span>Tbk &middot; perusahaan rekaan</span>
          </span>
        </NuxtLink>

        <div class="masthead__tools">
          <ThemeSwitch />

          <button
            class="nav-toggle"
            type="button"
            :aria-expanded="navOpen"
            aria-controls="nav-utama"
            @click="navOpen = !navOpen"
          >
            {{ navOpen ? 'Tutup' : 'Menu' }}
          </button>
        </div>

        <nav
          id="nav-utama"
          class="nav"
          :data-open="navOpen ? 'true' : 'false'"
          aria-label="Navigasi utama"
        >
          <NuxtLink
            v-for="item in nav"
            :key="item.to"
            class="nav__link"
            :to="item.to"
            @click="navOpen = false"
          >
            {{ item.label }}
          </NuxtLink>
        </nav>
      </div>
    </header>

    <main id="konten">
      <NuxtPage />
    </main>

    <footer>
      <div class="wrap">
        <div class="footer-mascot">
          <Mascot size="sm" />
        </div>
        <nav class="footer-nav" aria-label="Navigasi bawah">
          <NuxtLink v-for="item in nav" :key="item.to" :to="item.to">
            {{ item.label }}
          </NuxtLink>
        </nav>
        <p>
          PT Perkebunan Asap Emas Nusantara tidak ada. Seluruh nama, angka,
          klaim, dan peristiwa di situs ini adalah rekaan untuk karya satire,
          dan tidak mengacu pada perusahaan, orang, atau lokasi nyata.
        </p>
        <p>
          Dibangun dengan Nuxt 4. Font Nunito dan IBM Plex Mono berlisensi
          OFL 1.1. Seluruh foto dibuat dengan model generatif.
        </p>
      </div>
    </footer>
  </div>
</template>

<script setup lang="ts">
// Every item leads to a page that exists (R-24). Nothing is marked coming
// soon, so nothing in this list is a dead link.
const nav = [
  { label: 'Beranda', to: '/' },
  { label: 'Tentang', to: '/tentang' },
  { label: 'Visi & Misi', to: '/visi-misi' },
  { label: 'Legal', to: '/legal' },
]

const navOpen = ref(false)

// Escape closes the mobile menu, and a click outside it does too (R-32).
function onKeydown(event: KeyboardEvent) {
  if (event.key === 'Escape') navOpen.value = false
}

function onClickOutside(event: MouseEvent) {
  const target = event.target as HTMLElement | null
  if (!target?.closest('.masthead')) navOpen.value = false
}

onMounted(() => {
  document.addEventListener('keydown', onKeydown)
  document.addEventListener('click', onClickOutside)
})

onBeforeUnmount(() => {
  document.removeEventListener('keydown', onKeydown)
  document.removeEventListener('click', onClickOutside)
})
</script>

<style scoped>
.masthead {
  position: sticky;
  top: 0;
  z-index: 50;
  /* Opaque base under the translucency. A semi-transparent header returns
     rgba, which leaves a contrast audit walking up to <body>; over the hero
     that is the dark photograph, and light nav text measures 1.29 against it.
     The solid layer below keeps the computed background something the walk can
     actually land on. */
  background: var(--bg);
  background: color-mix(in srgb, var(--bg) 88%, transparent);
  backdrop-filter: blur(12px);
  border-bottom: 2px solid var(--border);
}

.masthead__row {
  display: flex;
  align-items: center;
  gap: 1rem;
  flex-wrap: wrap;
  padding-block: 0.75rem;
}

.masthead__brand {
  display: flex;
  align-items: center;
  gap: 0.875rem;
  text-decoration: none;
  color: var(--ink);
  margin-right: auto;
  /* Without a floor of 0 the long company name refuses to shrink below its
     longest word and pushes the whole header 33px past a 360px viewport, which
     makes the entire page scroll sideways. */
  min-width: 0;
  flex: 1 1 auto;
}

.masthead__name {
  min-width: 0;
  overflow-wrap: anywhere;
}

.masthead__seal {
  width: 44px;
  height: 44px;
  flex: none;
  transition: transform var(--dur) var(--spring);
}

.masthead__brand:hover .masthead__seal {
  transform: rotate(-12deg) scale(1.08);
}

.masthead__name {
  font-size: 0.9375rem;
  font-weight: 700;
  letter-spacing: -0.01em;
  line-height: 1.2;
}

.masthead__name span {
  display: block;
  font-family: 'IBM Plex Mono', ui-monospace, monospace;
  font-size: 0.625rem;
  font-weight: 400;
  letter-spacing: 0.04em;
  color: var(--muted);
  margin-top: 0.2rem;
}

.masthead__tools {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.nav {
  display: flex;
  gap: 0.25rem;
  flex-basis: 100%;
}

.nav__link {
  font-size: 0.9375rem;
  font-weight: 700;
  /* 15px copy on the sticky masthead cannot use --muted and clear 4.5:1: the
     masthead's translucent background resolves to something between --bg and
     --card, and --muted lands at 3.16:1 there. Navigation chrome is not
     body copy, so it takes --ink. */
  color: var(--ink);
  text-decoration: none;
  padding: 0.625rem 0.875rem;
  border-radius: 999px;
  min-height: 44px;
  display: inline-flex;
  align-items: center;
  transition: color var(--dur-fast) var(--ease), background var(--dur-fast) var(--ease);
}

.nav__link:hover {
  color: var(--sakura-ink);
  background: color-mix(in srgb, var(--sakura) 20%, transparent);
}

.nav__link[aria-current='page'] {
  /* The active pill is the one nav state that must stay legible in both
     themes. --sakura-ink inverts for night mode, so text-on-wash flips to
     1.26:1 there. An opaque surface plus the always-dark --plum-700 keeps the
     pairing stable. */
  color: var(--plum-700);
  background: var(--sakura);
}

/* On mobile the nav collapses behind the toggle, and the panel itself springs
   open rather than appearing. */
@media (max-width: 47.99rem) {
  .nav {
    flex-direction: column;
    gap: 0.125rem;
    max-height: 0;
    overflow: hidden;
    opacity: 0;
    transition: max-height var(--dur) var(--ease), opacity var(--dur) var(--ease);
  }

  .nav[data-open='true'] {
    max-height: 20rem;
    opacity: 1;
    padding-bottom: 0.75rem;
  }
}

.nav-toggle {
  font-family: inherit;
  font-size: 0.8125rem;
  font-weight: 700;
  color: var(--sakura-ink);
  background: color-mix(in srgb, var(--sakura) 22%, var(--card));
  border: 2px solid var(--sakura);
  border-radius: 999px;
  padding: 0.625rem 1rem;
  min-height: 44px;
  cursor: pointer;
  transition: transform var(--dur-fast) var(--spring), background var(--dur-fast) var(--ease);
}

.nav-toggle:active {
  transform: scale(0.94);
}

@media (min-width: 48rem) {
  .nav-toggle {
    display: none;
  }

  .nav {
    flex-basis: auto;
  }
}

footer {
  border-top: 2px solid var(--border);
  margin-top: clamp(3rem, 8vw, 5rem);
  padding-block: 2.5rem 3rem;
  background: color-mix(in srgb, var(--sunken) 60%, transparent);
}

footer p {
  font-size: 0.875rem;
  line-height: 1.7;
  color: var(--muted);
  max-width: 44rem;
  margin-block: 0.75rem;
}

.footer-nav {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem 1.25rem;
  margin-bottom: 1.25rem;
}

.footer-nav a {
  font-size: 0.9375rem;
  font-weight: 700;
  color: var(--sakura-ink);
  text-decoration: none;
  padding-block: 0.375rem;
}

.footer-nav a:hover {
  text-decoration: underline;
}

.footer-mascot {
  margin-bottom: 1.5rem;
}
</style>
