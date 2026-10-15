<template>
  <!-- The fiction notice is on every page (R-38), because a satirical corporate
       register is exactly the shape a reader could mistake for the real thing.
       It is also the last thing on every page, which is where a disclaimer
       belongs and where nobody reads it. -->
  <aside
    role="note"
    class="border-t-2 border-hair bg-[var(--harm-leaf-bg)]"
  >
    <div class="mx-auto max-w-6xl px-6 py-10">
      <div class="flex flex-wrap items-start gap-4">
        <span
          class="grid size-10 shrink-0 place-items-center rounded-lg border-2 border-leaf-400 bg-leaf-100 text-leaf-800 dark:border-leaf-500 dark:bg-leaf-900 dark:text-leaf-200"
          aria-hidden="true"
        >
          <svg viewBox="0 0 24 24" class="size-5" fill="currentColor">
            <path
              d="M12 2a10 10 0 1 0 0 20 10 10 0 0 0 0-20zm1 15h-2v-2h2zm0-4h-2V7h2z"
            />
          </svg>
        </span>
        <div class="min-w-0 flex-1">
          <h4
            class="m-0 text-[0.9375rem] font-semibold tracking-tight text-body"
          >
            {{ label }}
          </h4>
          <p
            class="m-0 mt-2 max-w-3xl text-sm leading-relaxed text-quiet"
          >
            PT Perkebunan Asap Emas Nusantara tidak ada. Seluruh nama, angka,
            klaim, dan peristiwa di halaman ini adalah rekaan untuk karya
            satire, dan tidak mengacu pada perusahaan, lembaga, orang, atau
            lokasi nyata di mana pun. Tidak ada lembaga sertifikasi, wilayah,
            atau badan pengawas sungguhan yang disebut atau dituduh. Seluruh
            foto di situs ini dibuat dengan model generatif.
          </p>
          <p v-if="link" class="m-0 mt-3 text-sm">
            <NuxtLink
              :to="link"
              class="font-semibold text-leaf-700 underline decoration-2 underline-offset-2 transition-colors duration-150 ease-out hover:text-leaf-800 dark:text-leaf-300 dark:hover:text-leaf-200"
              >{{ linkLabel }}</NuxtLink
            >
          </p>
          <p v-else class="m-0 mt-3 text-sm">
            <NuxtLink
              to="/legal"
              class="font-semibold text-leaf-700 underline decoration-2 underline-offset-2 transition-colors duration-150 ease-out hover:text-leaf-800 dark:text-leaf-300 dark:hover:text-leaf-200"
              >Baca penafian lengkap dan daftar kredit</NuxtLink
            >
          </p>
        </div>
      </div>
    </div>
  </aside>
</template>

<script setup lang="ts">
withDefaults(
  defineProps<{
    label?: string
    link?: string
    linkLabel?: string
  }>(),
  { label: 'Situs fiksi' },
)
</script>
