<template>
  <!-- A theme switch as a physical toggle, because a select element would be
       the wrong object for something this decorative. The knob slides and the
       sky and sun swap, which is the whole point of having two modes. -->
  <button
    class="theme-switch"
    type="button"
    :aria-pressed="isNight"
    :aria-label="isNight ? 'Ganti ke mode siang (sakura)' : 'Ganti ke mode malam (yoru)'"
    @click="toggle"
  >
    <span class="theme-switch__track" aria-hidden="true">
      <span class="theme-switch__sky" />
      <span class="theme-switch__sun" />
      <span class="theme-switch__moon" />
      <span class="theme-switch__knob" />
    </span>
    <span class="theme-switch__label">{{ isNight ? 'Yoru' : 'Sakura' }}</span>
  </button>
</template>

<script setup lang="ts">
// The theme lives in localStorage so the choice survives a reload, and the
// initial value is read before paint to avoid a flash of the wrong mode.
type Mode = 'sakura' | 'yoru'

const KEY = 'sawit-theme'

const mode = ref<Mode>('sakura')
const isNight = computed(() => mode.value === 'yoru')

function apply(next: Mode) {
  mode.value = next
  document.documentElement.dataset.theme = next
  try {
    localStorage.setItem(KEY, next)
  } catch {
    // Private browsing with storage disabled. The theme still applies for this
    // page view; it just will not persist, which is not worth an error.
  }
}

function toggle() {
  apply(isNight.value ? 'sakura' : 'yoru')
}

onMounted(() => {
  // Read the stored choice here rather than in setup: this runs after Nuxt has
  // hydrated, and touching localStorage during SSR throws.
  let stored: Mode | null = null
  try {
    const raw = localStorage.getItem(KEY)
    if (raw === 'sakura' || raw === 'yoru') stored = raw
  } catch {
    stored = null
  }
  if (stored) {
    mode.value = stored
    document.documentElement.dataset.theme = stored
    return
  }
  // No stored choice: follow the system. A reader who has asked their OS for
  // dark mode should not be handed a bright pink page.
  const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches
  apply(prefersDark ? 'yoru' : 'sakura')
})
</script>

<style scoped>
.theme-switch {
  display: inline-flex;
  align-items: center;
  gap: 0.625rem;
  background: none;
  border: 0;
  padding: 0.375rem;
  cursor: pointer;
  border-radius: 999px;
  min-height: 44px;
}

.theme-switch__track {
  position: relative;
  display: block;
  width: 56px;
  height: 30px;
  border-radius: 999px;
  border: 2px solid var(--control);
  background: linear-gradient(180deg, var(--sky) 0%, var(--lavender) 100%);
  overflow: hidden;
  transition: background var(--dur) var(--ease);
}

.theme-switch[aria-pressed='true'] .theme-switch__track {
  background: linear-gradient(180deg, #3B2E52 0%, var(--lavender-ink) 100%);
}

.theme-switch__knob {
  position: absolute;
  top: 2px;
  left: 2px;
  width: 22px;
  height: 22px;
  border-radius: 999px;
  background: var(--sun);
  box-shadow: 0 0 0 2px rgb(255 255 255 / 0.7), 0 2px 6px rgb(0 0 0 / 0.25);
  transition: transform var(--dur) var(--spring), background var(--dur) var(--ease);
}

.theme-switch[aria-pressed='true'] .theme-switch__knob {
  transform: translateX(26px);
  background: var(--card);
}

/* Tiny stars, only visible in the night mode. */
.theme-switch__moon {
  position: absolute;
  inset: 0;
  opacity: 0;
  transition: opacity var(--dur) var(--ease);
  background-image:
    radial-gradient(1.5px 1.5px at 12px 9px, #fff, transparent),
    radial-gradient(1px 1px at 24px 18px, #fff, transparent),
    radial-gradient(1.5px 1.5px at 38px 11px, #fff, transparent);
}

.theme-switch[aria-pressed='true'] .theme-switch__moon {
  opacity: 0.9;
}

.theme-switch__label {
  font-family: 'IBM Plex Mono', ui-monospace, monospace;
  font-size: 0.6875rem;
  font-weight: 500;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: var(--muted);
}

.theme-switch:hover .theme-switch__label {
  color: var(--sakura-ink);
}
</style>
