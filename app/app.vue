<template>
  <div>
    <a class="skip-link" href="#konten">Lompat ke konten</a>
    <header class="masthead">
      <div class="wrap masthead__row">
        <a class="mark" href="/company-sawit/">
          PT Perkebunan Asap Emas Nusantara
          <span class="mark__sub">Tbk &middot; fiksi, bukan perusahaan nyata</span>
        </a>
        <button
          class="theme-toggle"
          type="button"
          :aria-pressed="isDark"
          @click="toggleTheme"
        >
          {{ isDark ? 'Mode terang' : 'Mode gelap' }}
        </button>
      </div>
    </header>

    <main id="konten">
      <NuxtPage />
    </main>

    <footer>
      <div class="wrap">
        <p>
          PT Perkebunan Asap Emas Nusantara tidak ada. Seluruh nama, angka,
          klaim, dan peristiwa di situs ini adalah rekaan untuk karya satire,
          dan tidak mengacu pada perusahaan, orang, atau lokasi nyata.
        </p>
        <p>Dibangun dengan Nuxt 4. Kode sumber tersedia di repositori yang sama.</p>
      </div>
    </footer>
  </div>
</template>

<script setup lang="ts">
const isDark = ref(false)

function readTheme(): 'light' | 'dark' {
  const stored = localStorage.getItem('theme')
  if (stored === 'light' || stored === 'dark') return stored
  return window.matchMedia('(prefers-color-scheme: dark)').matches
    ? 'dark'
    : 'light'
}

function applyTheme(theme: 'light' | 'dark') {
  document.documentElement.dataset.theme = theme
  isDark.value = theme === 'dark'
}

function toggleTheme() {
  const next = isDark.value ? 'light' : 'dark'
  localStorage.setItem('theme', next)
  applyTheme(next)
}

onMounted(() => {
  applyTheme(readTheme())
})
</script>
