<template>
  <div>
    <a
      href="#konten"
      class="sr-only focus:not-sr-only focus:fixed focus:top-3 focus:left-3 focus:z-100 focus:rounded-full focus:bg-leaf-700 focus:px-5 focus:py-2.5 focus:text-sm focus:font-bold focus:text-white focus:no-underline"
      >Lompat ke konten</a
    >

    <header
      class="sticky top-0 z-50 border-b-2 border-hair bg-paper/90 backdrop-blur-md"
    >
      <div
        class="mx-auto flex max-w-6xl flex-wrap items-center gap-4 px-6 py-3 md:gap-6"
      >
        <!-- The mark is not a nav item, so it must not carry aria-current:
             NuxtLink to="/" matches the home route and would announce the logo
             as the current page to a screen reader. -->
        <NuxtLink
          to="/"
          :aria-current="undefined"
          class="flex min-w-0 flex-1 items-center gap-3.5 text-body no-underline"
        >
          <img
            :src="asset_company_sawit_logo_mark_svg"
            alt=""
            width="44"
            height="44"
            class="w-11 shrink-0 transition-transform duration-300 ease-out hover:-rotate-12 hover:scale-108"
          />
          <span class="min-w-0 text-[0.9375rem] leading-tight font-bold">
            PT Perkebunan Asap Emas Nusantara
            <span
              class="mt-0.5 block font-mono text-[0.625rem] font-normal tracking-wide text-quiet"
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
            class="min-h-11 cursor-pointer rounded-full border-2 border-leaf-400 bg-leaf-100 px-4 py-2.5 text-[0.8125rem] font-bold text-leaf-700 transition-transform duration-150 ease-out hover:-translate-y-0.5 active:scale-94 dark:border-leaf-500 dark:bg-leaf-900 dark:text-leaf-200 lg:hidden"
            @click="navOpen = !navOpen"
          >
            {{ navOpen ? 'Tutup' : 'Menu' }}
          </button>
        </div>

        <nav
          id="nav-utama"
          aria-label="Navigasi utama"
          :data-open="navOpen ? 'true' : 'false'"
          class="flex basis-full flex-col gap-0.5 overflow-hidden opacity-0 transition-[max-height,opacity] duration-300 ease-out data-[open=false]:max-h-0 data-[open=true]:max-h-80 data-[open=true]:opacity-100 lg:basis-auto lg:flex-row lg:gap-1 lg:max-h-none lg:opacity-100"
        >
          <NuxtLink
            v-for="item in nav"
            :key="item.to"
            :to="item.to"
            class="inline-flex min-h-11 items-center rounded-full px-3.5 py-2.5 text-[0.9375rem] font-bold text-body no-underline transition-colors duration-150 ease-out hover:bg-leaf-100 hover:text-leaf-700 aria-[current=page]:bg-leaf-600 aria-[current=page]:text-white dark:hover:bg-leaf-800 dark:hover:text-leaf-200"
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
              class="inline-flex min-h-11 items-center rounded-full px-4 py-2.5 text-sm font-bold text-quiet no-underline transition-colors duration-150 ease-out hover:bg-leaf-100 hover:text-leaf-700 dark:hover:bg-leaf-800 dark:hover:text-leaf-200"
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
})

onBeforeUnmount(() => {
  document.removeEventListener('keydown', onKeydown)
  document.removeEventListener('click', onClickOutside)
})
</script>
