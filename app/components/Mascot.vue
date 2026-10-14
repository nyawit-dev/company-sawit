<template>
  <!--
    The mascot. A chibi palm spirit: big head, small body, the proportions that
    read as "cute" before anything else about it registers. She is holding a
    fruit bunch, which is what the company sells, and standing on a stump,
    which is what it took to get there.

    Drawn as SVG rather than an image so it scales cleanly and so the eyes and
    frond can animate independently. Every fill is a token, so she changes
    with the theme.
  -->
  <svg
    class="mascot"
    :class="`mascot--${size}`"
    viewBox="0 0 160 200"
    role="img"
    aria-label="Maskot perusahaan: roh kelapa sawit chibi menahan tandan buah, berdiri di atas tunggul pohon"
    xmlns="http://www.w3.org/2000/svg"
  >
    <title>Maskot PT Perkebunan Asap Emas Nusantara</title>

    <defs>
      <!-- A soft vertical gradient for the dress, so the flat pastel reads as
           fabric rather than as a coloured shape. -->
      <linearGradient id="dress" x1="0" y1="0" x2="0" y2="1">
        <stop offset="0%" stop-color="var(--mint)" />
        <stop offset="100%" stop-color="var(--sky)" />
      </linearGradient>
      <radialGradient id="cheek" cx="0.5" cy="0.5" r="0.5">
        <stop offset="0%" stop-color="var(--sakura)" stop-opacity="0.9" />
        <stop offset="100%" stop-color="var(--sakura)" stop-opacity="0" />
      </radialGradient>
    </defs>

    <!-- sparkles, because nothing this shape is allowed to be plain -->
    <g class="sparkles" fill="var(--sun)">
      <path class="sparkle" d="M22 26 l3 7 7 3 -7 3 -3 7 -3 -7 -7 -3 7 -3 z" />
      <path class="sparkle" d="M140 40 l2.4 5.6 5.6 2.4 -5.6 2.4 -2.4 5.6 -2.4 -5.6 -5.6 -2.4 5.6 -2.4 z" />
      <path class="sparkle" d="M132 148 l2 4.6 4.6 2 -4.6 2 -2 4.6 -2 -4.6 -4.6 -2 4.6 -2 z" />
    </g>

    <!-- the stump she is standing on: the part of the picture the corporate
         voice would leave out of its own mascot -->
    <g>
      <ellipse cx="80" cy="188" rx="46" ry="9" fill="var(--border)" />
      <path d="M42 186 q38 -14 76 0 l-4 8 q-34 -12 -68 0 z" fill="var(--muted)" opacity="0.5" />
      <ellipse cx="80" cy="184" rx="38" ry="7" fill="var(--sunken)" />
      <ellipse cx="80" cy="183" rx="38" ry="7" fill="none" stroke="var(--control)" stroke-width="1.5" />
      <!-- growth rings: the age of the tree that used to be here -->
      <ellipse cx="80" cy="183" rx="24" ry="4.5" fill="none" stroke="var(--control)" stroke-width="1" opacity="0.6" />
      <ellipse cx="80" cy="183" rx="12" ry="2.4" fill="none" stroke="var(--control)" stroke-width="1" opacity="0.5" />
    </g>

    <!-- body -->
    <g>
      <!-- legs -->
      <path d="M70 150 q-3 18 -1 30" stroke="var(--ink)" stroke-width="7" stroke-linecap="round" fill="none" opacity="0.85" />
      <path d="M90 150 q3 18 1 30" stroke="var(--ink)" stroke-width="7" stroke-linecap="round" fill="none" opacity="0.85" />
      <!-- shoes -->
      <ellipse cx="68" cy="181" rx="8" ry="4.5" fill="var(--sakura-ink)" />
      <ellipse cx="92" cy="181" rx="8" ry="4.5" fill="var(--sakura-ink)" />

      <!-- dress: a tapered trapezoid, the simplest silhouette that still
           reads as clothing rather than as a coloured blob -->
      <path
        d="M80 96
           C 66 96 58 106 54 122
           L 48 152 q 32 10 64 0
           L 102 122 C 98 106 94 96 80 96 Z"
        fill="url(#dress)"
        stroke="var(--ink)"
        stroke-width="2.5"
        stroke-linejoin="round"
      />
      <!-- collar -->
      <path d="M68 99 q12 8 24 0" stroke="var(--ink)" stroke-width="2.5" fill="none" stroke-linecap="round" />
      <!-- the company emblem, worn as a badge: the same seal as the header,
           shrunk. She works for them. -->
      <circle cx="80" cy="126" r="8" fill="var(--card)" stroke="var(--sun-ink)" stroke-width="2" />
      <path d="M80 130 v-5 M77 128 q3 -5 6 0" stroke="var(--sun-ink)" stroke-width="1.6" fill="none" stroke-linecap="round" />

      <!-- arms -->
      <path d="M56 112 q-12 6 -14 20" stroke="var(--ink)" stroke-width="6" stroke-linecap="round" fill="none" opacity="0.85" />
      <path d="M104 112 q12 6 14 20" stroke="var(--ink)" stroke-width="6" stroke-linecap="round" fill="none" opacity="0.85" />

      <!-- the fruit bunch she is holding out, like a tray. This is the
           product, presented the way a mascot presents a product. -->
      <g>
        <path d="M118 132 q10 -3 14 4" stroke="var(--ink)" stroke-width="4" fill="none" stroke-linecap="round" />
        <g fill="var(--sakura-ink)">
          <ellipse cx="128" cy="140" rx="6" ry="7.5" />
          <ellipse cx="138" cy="140" rx="6" ry="7.5" />
          <ellipse cx="133" cy="146" rx="6.5" ry="7" />
        </g>
        <g fill="var(--sakura)" opacity="0.85">
          <circle cx="127" cy="138" r="2" />
          <circle cx="139" cy="138" r="2" />
          <circle cx="133" cy="144.5" r="2.2" />
        </g>
      </g>
    </g>

    <!-- head: the chibi proportion. Roughly half the total height, which is
         what makes the shape read as cute before any detail is noticed. -->
    <g>
      <!-- hair back -->
      <path
        d="M80 30
           C 56 30 46 46 46 66
           C 46 78 42 92 46 104
           C 50 112 58 114 60 106
           C 56 96 58 82 62 74
           L 98 74
           C 102 82 104 96 100 106
           C 102 114 110 112 114 104
           C 118 92 114 78 114 66
           C 114 46 104 30 80 30 Z"
        fill="var(--lavender)"
        stroke="var(--ink)"
        stroke-width="2.5"
        stroke-linejoin="round"
      />

      <!-- face -->
      <ellipse cx="80" cy="64" rx="32" ry="29" fill="#FFF4F6" stroke="var(--ink)" stroke-width="2.5" />

      <!-- fronds worn as a hairpiece, animated -->
      <g class="mascot__frond" style="transform-origin: 80px 40px">
        <path d="M80 38 C 70 24 56 20 46 22" stroke="var(--mint-ink)" stroke-width="4" fill="none" stroke-linecap="round" />
        <path d="M80 38 C 90 24 104 20 114 22" stroke="var(--mint-ink)" stroke-width="4" fill="none" stroke-linecap="round" />
        <path d="M80 36 C 79 22 80 14 82 8" stroke="var(--mint-ink)" stroke-width="4" fill="none" stroke-linecap="round" />
        <!-- leaflets -->
        <g stroke="var(--mint-ink)" stroke-width="2.4" stroke-linecap="round">
          <path d="M68 30 l-4 -5" /><path d="M58 25 l-4 -4" />
          <path d="M92 30 l4 -5" /><path d="M102 25 l4 -4" />
          <path d="M81 24 l-5 -3" /><path d="M81 14 l5 -3" />
        </g>
      </g>

      <!-- fringe -->
      <path
        d="M48 58 q6 -22 32 -22 q26 0 32 22 q-10 -12 -20 -10 q-6 -8 -14 -6 q-8 -2 -12 6 q-10 -2 -18 10 z"
        fill="var(--lavender)"
        stroke="var(--ink)"
        stroke-width="2.5"
        stroke-linejoin="round"
      />

      <!-- eyes: two large ellipses with a highlight each. The highlight is
           what separates "anime eye" from "a dot", and it is drawn as a
           separate shape so the blink can scale it. -->
      <g class="mascot__eye">
        <ellipse cx="68" cy="66" rx="6.5" ry="8.5" fill="var(--ink)" />
        <ellipse cx="92" cy="66" rx="6.5" ry="8.5" fill="var(--ink)" />
        <circle cx="70.5" cy="62.5" r="2.6" fill="#FFFFFF" />
        <circle cx="94.5" cy="62.5" r="2.6" fill="#FFFFFF" />
        <circle cx="66" cy="70" r="1.4" fill="#FFFFFF" opacity="0.8" />
        <circle cx="90" cy="70" r="1.4" fill="#FFFFFF" opacity="0.8" />
      </g>

      <!-- brows, slightly worried: the only hint that she knows -->
      <path d="M61 54 q7 -3 13 0" stroke="var(--ink)" stroke-width="2" fill="none" stroke-linecap="round" opacity="0.7" />
      <path d="M86 54 q7 -3 13 0" stroke="var(--ink)" stroke-width="2" fill="none" stroke-linecap="round" opacity="0.7" />

      <!-- blush -->
      <ellipse cx="58" cy="74" rx="7" ry="4.5" fill="url(#cheek)" />
      <ellipse cx="102" cy="74" rx="7" ry="4.5" fill="url(#cheek)" />

      <!-- mouth: a small open smile -->
      <path d="M75 80 q5 5 10 0 q-5 3 -10 0 z" fill="var(--ink)" opacity="0.8" />
    </g>
  </svg>
</template>

<script setup lang="ts">
withDefaults(defineProps<{ size?: 'sm' | 'md' | 'lg' }>(), { size: 'md' })
</script>

<style scoped>
.mascot {
  display: block;
  overflow: visible;
}

.mascot--sm { width: 64px; }
.mascot--md { width: 120px; }
.mascot--lg { width: 200px; }
</style>
