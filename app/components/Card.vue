<template>
  <!--
    THE CARD.

    Every raised surface on the site goes through this component, so the
    elevation, radius, border, and hover all change in one place. The reason it
    is a component and not a utility string repeated in markup: this site has
    five accent hues and two themes, and a card that is right in one pair of
    those was wrong in eight of the ten until the values were centralised.

    `tone` picks the accent used for the left rule and the number chip. The
    default (no hue) is the filing card.
  -->
  <div
    class="group relative overflow-hidden rounded-lg border-2 bg-card transition-all duration-300 ease-out"
    :class="[
      tone ? `border-${tone}-br` : 'border-hair',
      tone ? `harm-${tone}` : '',
      padded ? 'p-6 md:p-8' : '',
      interactive
        ? 'hover:-translate-y-1 hover:shadow-[var(--shadow-lift)]'
        : 'shadow-[var(--shadow-card)]',
    ]"
    :style="tone ? { backgroundColor: `var(--harm-${tone}-bg)` } : undefined"
  >
    <!-- The accent rule is the only place a hue is allowed to sit as a full
         block of colour, which is why it is 4px and runs the full height. -->
    <span
      v-if="tone"
      aria-hidden="true"
      class="absolute inset-y-0 left-0 w-1"
      :style="{ backgroundColor: `var(--harm-${tone}-br)` }"
    />

    <div :class="tone ? 'pl-4' : ''">
      <slot />
    </div>
  </div>
</template>

<script setup lang="ts">
// The five hues of damage, in the order the harm ledger presents them. Each one
// is a real CSS custom property pair in main.css, not a Tailwind colour, so
// that the numeral token can be specified separately from the border colour.
type Tone = 'fire' | 'water' | 'soil' | 'sick' | 'leaf'

defineProps<{
  tone?: Tone
  padded?: boolean
  /** Adds the lift-on-hover. Reserved for cards that are links or open. */
  interactive?: boolean
}>()
</script>
