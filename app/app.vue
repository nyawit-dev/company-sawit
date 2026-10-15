<template>
  <div>
    <a
      href="#konten"
      class="sr-only focus:not-sr-only focus:fixed focus:top-3 focus:left-3 focus:z-100 focus:rounded-full focus:bg-leaf-700 focus:px-5 focus:py-2.5 focus:text-sm focus:font-semibold focus:text-white focus:no-underline"
      >Lompat ke konten</a
    >

    <header
      ref="headerEl"
      class="sticky top-0 z-50 border-b-2 border-hair bg-paper/90 backdrop-blur-md"
    >
      <!-- No `flex-wrap` here. With it, the nav dropping to a second line pushed
           the theme switch into the middle of the header instead of leaving it
           at the right edge, which is where a reader looks for it.

           The header measured 168px tall at 320px — 28% of a 600px viewport —
           because the logo's two-line wordmark, the theme switch and the menu
           button all wrapped onto separate rows. It is 66px at 1280px, which is
           the intended height. On phones the wordmark drops its second line and
           the mark shrinks, bringing the bar back to ~76px. A sticky header
           taller than the fold it is meant to leave room for defeats itself. -->
      <div
        class="mx-auto flex max-w-6xl items-center gap-3 px-4 py-2 md:gap-6 md:px-6 md:py-2.5"
      >
        <!-- The mark is not a nav item, so it must not carry aria-current:
             NuxtLink to="/" matches the home route and would announce the logo
             as the current page to a screen reader. -->
        <NuxtLink
          to="/"
          :aria-current="undefined"
          class="flex min-w-0 flex-1 items-center gap-2 text-body no-underline md:gap-3.5"
        >
          <img
            :src="asset_company_sawit_logo_mark_svg"
            alt=""
            width="44"
            height="44"
            class="w-8 shrink-0 transition-transform duration-300 ease-out hover:-rotate-12 hover:scale-108 md:w-11"
          />
          <!-- The second line is desktop-only. At 320px it is what pushed the
               header to 168px; dropping it keeps the company name on one line
               without truncating it.

               `truncate` is what keeps this honest at 320px: `min-w-0` lets the
               flex item shrink, and without a truncation strategy the text
               overflows its own zero-width box instead of ellipsising. Measured
               at 320px before this was added: the link was 0px wide and 94px
               tall, so the company name was simply not painted. -->
          <span
            class="min-w-0 truncate text-[0.8125rem] leading-tight font-semibold md:text-[0.9375rem]"
          >
            PT Perkebunan Asap Emas Nusantara
            <span
              class="mt-0.5 hidden font-mono text-[0.625rem] font-normal tracking-wide text-quiet md:block"
              >Tbk &middot; perusahaan rekaan</span
            >
          </span>
        </NuxtLink>

        <div class="flex items-center gap-3">
          <ThemeSwitch />

          <button
            type="button"
            :aria-expanded="navOpen"
            aria-controls="nav-utama"
            class="min-h-11 cursor-pointer rounded-full border-2 border-leaf-400 bg-leaf-100 px-4 py-2.5 text-[0.8125rem] font-semibold text-leaf-700 transition-transform duration-150 ease-out hover:-translate-y-0.5 active:scale-94 dark:border-leaf-500 dark:bg-leaf-900 dark:text-leaf-200 lg:hidden"
            @click="navOpen = !navOpen"
          >
            {{ navOpen ? 'Tutup' : 'Menu' }}
          </button>
        </div>

        <!-- `basis-0` when closed, `basis-full` when open.

             This was `basis-full` unconditionally, which means flex-basis:100%
             even while `max-h-0` collapses the height. A closed nav therefore
             still claimed the entire row width: measured at 320/375/768px the
             company-name link came out 0px wide, so the name was not painted at
             all — the header looked like a lone logo mark and two controls. The
             theme switch and menu button are `lg:hidden` / always-visible in a
             fixed 133px block, and everything they displaced came out of the
             wordmark, because that is the only item left with `flex-1`.

             Going through 0 on the way open is also what makes the transition
             smooth: the basis animates rather than snapping. -->
        <nav
          id="nav-utama"
          aria-label="Navigasi utama"
          :data-open="navOpen ? 'true' : 'false'"
          class="flex basis-0 flex-col gap-0.5 overflow-hidden opacity-0 transition-[flex-basis,max-height,opacity] duration-300 ease-out data-[open=false]:max-h-0 data-[open=true]:basis-full data-[open=true]:max-h-80 data-[open=true]:opacity-100 lg:basis-auto lg:flex-row lg:gap-1 lg:max-h-none lg:opacity-100"
        >
          <NuxtLink
            v-for="item in nav"
            :key="item.to"
            :to="item.to"
            class="inline-flex min-h-11 items-center rounded-full px-3.5 py-2.5 text-[0.9375rem] font-semibold text-body no-underline transition-colors duration-150 ease-out hover:bg-leaf-100 hover:text-leaf-700 aria-[current=page]:bg-leaf-600 aria-[current=page]:text-white dark:hover:bg-leaf-800 dark:hover:text-leaf-200"
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

    <footer class="mt-20 border-t-2 border-hair bg-sunken">
      <div class="mx-auto max-w-6xl px-6 py-12">
        <div class="flex flex-col gap-8 md:flex-row md:items-start md:justify-between">
          <div class="flex items-start gap-4">
            <Mascot size="sm" />
            <p class="m-0 max-w-md text-sm leading-relaxed text-quiet">
              PT Perkebunan Asap Emas Nusantara tidak ada. Seluruh nama, angka,
              klaim, dan peristiwa di situs ini adalah rekaan untuk karya satire,
              dan tidak mengacu pada perusahaan, orang, atau lokasi nyata.
            </p>
          </div>

          <nav aria-label="Navigasi bawah" class="flex flex-wrap gap-1">
            <NuxtLink
              v-for="item in nav"
              :key="item.to"
              :to="item.to"
              class="inline-flex min-h-11 items-center rounded-full px-4 py-2.5 text-sm font-semibold text-quiet no-underline transition-colors duration-150 ease-out hover:bg-leaf-100 hover:text-leaf-700 dark:hover:bg-leaf-800 dark:hover:text-leaf-200"
            >
              {{ item.label }}
            </NuxtLink>
          </nav>
        </div>

        <p
          class="mt-8 mb-0 border-t border-hair pt-6 text-xs leading-relaxed text-quiet"
        >
          Dibangun dengan Nuxt 4 dan Tailwind CSS. Font Nunito dan IBM Plex Mono
          berlisensi OFL 1.1. Seluruh foto dibuat dengan model generatif.
        </p>
      </div>
    </footer>
  </div>
</template>

<script setup lang="ts">
// Bound rather than literal: rolldown rewrites a literal public/
// path into a static import, and public/ is not an import root.
const asset_company_sawit_logo_mark_svg = '/company-sawit/logo-mark.svg'

// Every item leads to a page that exists (R-24). Nothing is marked coming
// soon, so nothing in this list is a dead link.
const nav = [
  { label: 'Beranda', to: '/' },
  { label: 'Tentang', to: '/tentang' },
  { label: 'Visi & Misi', to: '/visi-misi' },
  { label: 'Legal', to: '/legal' },
]

const navOpen = ref(false)

// Template ref for the <header>. Vue 3.5 binds a ref by variable name, so this
// declaration is what makes `headerEl` in the template resolve; without it the
// build fails on an unresolved identifier.
const headerEl = useTemplateRef<HTMLElement>('headerEl')

// Escape closes the mobile menu, and a click outside it does too (R-32).
function onKeydown(event: KeyboardEvent) {
  if (event.key === 'Escape') navOpen.value = false
}

function onClickOutside(event: MouseEvent) {
  const target = event.target as HTMLElement | null
  if (!target?.closest('header')) navOpen.value = false
}

onMounted(() => {
  document.addEventListener('keydown', onKeydown)
  document.addEventListener('click', onClickOutside)

  // Publish the header's real height as --header-h.
  //
  // SectionNav is sticky directly beneath the header and used to offset itself
  // with a hardcoded `top-[4.125rem]`. That value only matched the desktop
  // header; at 320px the header measured 168px, so the nav either overlapped it
  // or left a gap depending on which one was taller. Measuring beats guessing,
  // and a ResizeObserver keeps it correct when the mobile menu opens — which
  // changes the header's height on purpose.
  const publish = () => {
    const h = headerEl.value?.getBoundingClientRect().height
    if (h) document.documentElement.style.setProperty('--header-h', `${h}px`)
  }
  publish()

  const observer = new ResizeObserver(publish)
  if (headerEl.value) observer.observe(headerEl.value)
  window.addEventListener('resize', publish)

  onBeforeUnmount(() => {
    observer.disconnect()
    window.removeEventListener('resize', publish)
  })
})

onBeforeUnmount(() => {
  document.removeEventListener('keydown', onKeydown)
  document.removeEventListener('click', onClickOutside)
})
</script>
