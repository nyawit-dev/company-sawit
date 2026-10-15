<script setup lang="ts">
// The pair of numbers: what the company published, and what it did not.
// Extracted from the page because seven different layouts now render it, and
// duplicating the markup seven times is how the two sides drift apart.
//
// The solid border and the dashed border are the only visual difference between
// the two cells. That is deliberate: the difference between the two numbers is
// the entire argument, so nothing else is allowed to compete with it.
defineProps<{
  harm: {
    hue: string
    claim: { value: string; label: string }
    unprinted: { value: string; label: string }
  }
}>()
</script>

<template>
  <dl class="m-0 grid grid-cols-2 gap-4">
    <div
      class="rounded-lg border-2 bg-card p-5"
      :style="{ borderColor: `var(--harm-${harm.hue}-br)` }"
    >
      <dd
        class="m-0 font-mono text-figure leading-none font-semibold"
        :style="{ color: `var(--harm-${harm.hue}-fg)` }"
      >
        {{ harm.claim.value }}
      </dd>
      <dt
        class="mt-2 font-mono text-[0.625rem] leading-snug tracking-wider uppercase text-quiet"
      >
        {{ harm.claim.label }}
      </dt>
    </div>
    <div
      class="rounded-lg border-2 border-dashed bg-card/60 p-5"
      :style="{ borderColor: `var(--harm-${harm.hue}-br)` }"
    >
      <dd
        class="m-0 font-mono text-figure leading-none font-semibold text-body"
      >
        {{ harm.unprinted.value }}
      </dd>
      <dt
        class="mt-2 font-mono text-[0.625rem] leading-snug tracking-wider uppercase text-quiet"
      >
        {{ harm.unprinted.label }}
      </dt>
    </div>
  </dl>
</template>
