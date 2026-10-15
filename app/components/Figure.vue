<template>
  <!--
    THE FIGURE.

    Every photograph on the site goes through this. The frame, the hover, and
    the caption treatment are shared so that a reader who has seen one caption
    knows where to look on the next one.

    The caption is deliberately in two registers: the plain description, then
    the attribution line in mono that says the image was generated. That second
    line is on every figure without exception (R-38), because a satirical
    corporate register with photorealistic evidence needs the disclosure inside
    the frame, not only on the legal page.
  -->
  <figure
    class="group/figure m-0 overflow-hidden rounded-lg border-2 border-hair bg-card shadow-[var(--shadow-card)]"
  >
    <div class="overflow-hidden">
      <img
        :src="src"
        :alt="alt"
        loading="lazy"
        decoding="async"
        :style="{ aspectRatio: ratio }"
        class="block w-full object-cover transition-transform duration-700 ease-out group-hover/figure:scale-105"
      />
    </div>
    <figcaption class="border-t-2 border-hair px-5 py-4">
      <p class="m-0 text-[0.9375rem] leading-relaxed text-body">{{ caption }}</p>
      <p
        class="m-0 mt-2 font-mono text-[0.625rem] tracking-wider text-quiet uppercase"
      >
        {{ attribution }}
      </p>
    </figcaption>
  </figure>
</template>

<script setup lang="ts">
withDefaults(
  defineProps<{
    src: string
    alt: string
    caption: string
    attribution?: string
    // The frame ratio. Every figure was locked to 3/2, which made nine
    // photographs the same height whatever the block needed: a 0.406 overlay,
    // a 0.563 landscape and a card thumbnail all resolved to the same band.
    // The layout now chooses per use, so the page rhythm carries through to the
    // photographs instead of flattening back to one repeated shape.
    ratio?: string
  }>(),
  {
    attribution: 'Gambar dibuat dengan model generatif untuk laman ini.',
    ratio: '3/2',
  },
)
</script>
