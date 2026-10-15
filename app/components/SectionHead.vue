<template>
  <!-- A section heading with its number. The numbered block is the register of
       an annual report, and it is repeated on every page so the document reads
       as one filing rather than as a website. -->
  <div class="flex flex-wrap items-start gap-4">
    <span
      class="grid size-12 shrink-0 place-items-center rounded-lg border-2 border-leaf-400 bg-leaf-100 font-mono text-sm font-semibold text-leaf-800 dark:border-leaf-500 dark:bg-leaf-900 dark:text-leaf-200"
      >{{ num }}</span
    >
    <div class="min-w-0 flex-1">
      <h2
        class="m-0 text-display tracking-tight text-body"
      >
        {{ title }}
      </h2>
      <p
        v-if="subtitle"
        class="m-0 mt-2 font-mono text-[0.6875rem] tracking-wider text-leaf-700 uppercase dark:text-leaf-300"
      >
        {{ subtitle }}
      </p>
      <p
        v-if="$slots.default"
        class="m-0 mt-3 max-w-2xl text-[1.0625rem] leading-relaxed text-quiet"
      >
        <slot />
      </p>
    </div>
  </div>
</template>

<script setup lang="ts">
defineProps<{ num: string; title: string; subtitle?: string }>()
</script>
