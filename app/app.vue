<template>
  <div>
    <a class="skip-link" href="#konten">Lompat ke konten</a>

    <header class="masthead">
      <div class="wrap masthead__row">
        <!-- The mark is not a nav item, so it must not carry aria-current:
             NuxtLink to="/" matches the home route and would announce the logo
             as the current page to a screen reader. -->
        <NuxtLink class="masthead__brand" to="/" :aria-current="undefined">
          <!-- The engraved seal. Below ~96px its ring text and frond detail
               stop being legible, so the small mark is swapped in for mobile
               rather than shrinking the seal into a gold smear. -->
          <img
            class="masthead__seal masthead__seal--full"
            :src="'/company-sawit/logo.svg'"
          />
          <img
            class="masthead__seal masthead__seal--small"
            :src="'/company-sawit/logo-mark.svg'"
          />
          <span class="masthead__name">
            PT Perkebunan Asap Emas Nusantara
            <span>Tbk &middot; perusahaan rekaan</span>
          </span>
        </NuxtLink>

        <button
          class="nav-toggle"
          type="button"
          :aria-expanded="navOpen"
          aria-controls="nav-utama"
          @click="navOpen = !navOpen"
        >
          {{ navOpen ? 'Tutup' : 'Menu' }}
        </button>

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
          Dibangun dengan Nuxt 4. Kode sumber tersedia di repositori yang sama.
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
  window.addEventListener('keydown', onKeydown)
  window.addEventListener('click', onClickOutside)
})

onBeforeUnmount(() => {
  window.removeEventListener('keydown', onKeydown)
  window.removeEventListener('click', onClickOutside)
})

// The register follows the route, not a stored preference: the land is dark
// because of what it describes, the filing is light because the company is
// talking about itself.
//
// This touches `document`, so it must never run during SSR: a watchEffect
// alone fires synchronously inside setup, which is exactly what Nitro's
// prerenderer does, and it 500s the whole build. The guard is the fix.
const route = useRoute()

function syncRegister() {
  const onLand =
    route.path === '/'
  document.documentElement.classList.toggle('reg-lahan', onLand)
}

watch(route, syncRegister)
onMounted(syncRegister)
</script>
