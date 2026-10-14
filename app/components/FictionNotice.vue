<template>
  <aside class="notice" role="note">
    <h4>{{ label }}</h4>
    <p>
      PT Perkebunan Asap Emas Nusantara adalah rekaan. Seluruh nama, angka,
      klaim, dan peristiwa di halaman ini bagian dari karya satire, dan tidak
      mengacu pada perusahaan, orang, atau lokasi nyata.
    </p>
  </aside>
</template>

<script setup lang="ts">
// The fiction notice is on every page (R-38), because a satirical corporate
// register is exactly the shape a reader could mistake for the real thing.
withDefaults(defineProps<{ label?: string }>(), { label: 'Situs fiksi' })
</script>
