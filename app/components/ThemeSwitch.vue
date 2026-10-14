<template>
  <!-- A theme switch as a physical toggle, because a select element would be
       the wrong object for something this decorative. The knob slides and the
       sun and moon swap, which is what tells you the choice took effect before
       the palette has finished changing. -->
  <button
    type="button"
    role="switch"
    :aria-checked="dark"
    :aria-label="dark ? 'Ganti ke mode terang' : 'Ganti ke mode gelap'"
    class="group relative flex h-11 w-[4.75rem] shrink-0 cursor-pointer items-center rounded-full border-2 border-hair bg-card transition-colors duration-300 ease-out"
    @click="toggle"
  >
    <!-- The sun: day mode. Scales away in dark, where the moon takes over. -->
    <span
      class="absolute left-1.5 grid size-7 place-items-center rounded-full bg-leaf-200 text-leaf-800 transition-all duration-300 ease-out group-aria-checked:scale-0 group-aria-checked:opacity-0"
    >
      <svg viewBox="0 0 24 24" class="size-4" fill="none" aria-hidden="true">
        <circle cx="12" cy="12" r="4.5" fill="currentColor" />
        <g stroke="currentColor" stroke-width="2" stroke-linecap="round">
          <path
            d="M12 2.5v2.5M12 19v2.5M2.5 12H5M19 12h2.5M5.3 5.3l1.8 1.8M16.9 16.9l1.8 1.8M18.7 5.3l-1.8 1.8M7.1 16.9l-1.8 1.8"
          />
        </g>
      </svg>
    </span>

    <!-- The moon: night mode. Scales in over the sun's position. -->
    <span
      class="absolute right-1.5 grid size-7 scale-0 place-items-center rounded-full bg-leaf-800 text-leaf-100 opacity-0 transition-all duration-300 ease-out group-aria-checked:scale-100 group-aria-checked:opacity-100"
    >
      <svg viewBox="0 0 24 24" class="size-4" fill="currentColor" aria-hidden="true">
        <path d="M20 14.5A8.5 8.5 0 0 1 9.5 4a8.5 8.5 0 1 0 10.5 10.5z" />
      </svg>
    </span>

    <!-- The knob. It is the one thing that physically moves, so it carries the
         whole affordance: without motion this control reads as decoration. -->
    <span
      class="absolute top-1 left-1 size-7 rounded-full bg-leaf-600 shadow-[0_2px_6px_rgb(14_39_25/0.35)] transition-transform duration-300 ease-out group-aria-checked:translate-x-[2.25rem]"
    ></span>
  </button>
</template>

<script setup lang="ts">
// The theme lives in localStorage so the choice survives a reload, and the
// initial value is read before paint to avoid a flash of the wrong mode.
const LIGHT = 'hijau'
const DARK = 'malam'
const KEY = 'sawit-theme'

const dark = ref(false)

function apply(value: boolean) {
  dark.value = value
  document.documentElement.dataset.theme = value ? DARK : LIGHT
  try {
    localStorage.setItem(KEY, value ? DARK : LIGHT)
  } catch {
    // Private browsing with storage blocked. The theme still applies for this
    // page view; it just will not persist, which is not worth an error.
  }
}

function toggle() {
  apply(!dark.value)
}

onMounted(() => {
  // Read the stored choice here rather than in setup: this runs after Nuxt has
  // hydrated, and touching localStorage during SSR throws.
  let stored: string | null = null
  try {
    stored = localStorage.getItem(KEY)
  } catch {
    stored = null
  }
  if (stored === DARK || stored === LIGHT) {
    apply(stored === DARK)
    return
  }
  // No stored choice: follow the system. A reader who has asked their OS for
  // dark mode should not be handed a bright page.
  apply(window.matchMedia('(prefers-color-scheme: dark)').matches)
})
</script>
