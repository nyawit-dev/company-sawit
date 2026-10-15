<template>
  <!--
    THE PAIRED FIGURE.

    The satire of this site is carried by one shape: the company's number next
    to the number it does not print, in the same type size, with no comment
    between them. The reader supplies the comment. This component exists so
    that shape is identical every time it appears, because the joke weakens the
    moment one pair is styled differently from another.

    `ours` is the company figure (quiet, because it is the one in the annual
    report). `theirs` is the other one (loud, because it is not).
  -->
  <div
    class="grid gap-3 sm:grid-cols-2 sm:gap-0"
    :class="[tone ? `harm-${tone}` : '']"
    :style="tone ? { backgroundColor: `var(--harm-${tone}-bg)` } : undefined"
  >
    <div
      v-for="(side, i) in sides"
      :key="i"
      class="relative px-5 py-4"
      :class="i === 1 ? 'sm:border-l-2 sm:border-current/15' : ''"
      :style="
        i === 1 && tone ? { borderLeftColor: `var(--harm-${tone}-br)` } : undefined
      "
    >
      <dt
        class="m-0 font-mono text-[0.625rem] font-semibold tracking-wider uppercase"
        :style="{ color: tone ? `var(--harm-${tone}-num)` : undefined }"
        :class="tone ? '' : 'text-quiet'"
      >
        {{ side.label }}
      </dt>
      <dd
        class="m-0 mt-1.5 text-figure leading-none font-semibold tracking-tight"
        :class="[tone ? 'text-body' : i === 0 ? 'text-body' : 'text-leaf-700 dark:text-leaf-300']"
      >
        {{ side.value }}
      </dd>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue'

type Tone = 'fire' | 'water' | 'soil' | 'sick' | 'leaf'

const props = defineProps<{
  tone?: Tone
  ours: string
  oursLabel: string
  theirs: string
  theirsLabel: string
}>()

// Order matters: the company's figure always reads first, so the reader meets
// the familiar claim before the correction.
const sides = computed(() => [
  { label: props.oursLabel, value: props.ours },
  { label: props.theirsLabel, value: props.theirs },
])
</script>
