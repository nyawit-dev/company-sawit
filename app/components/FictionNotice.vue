<template>
  <aside class="notice" role="note">
    <h4>{{ label }}</h4>
    <p>
      PT Perkebunan Asap Emas Nusantara tidak ada. Seluruh nama, angka, klaim,
      dan peristiwa di halaman ini adalah rekaan untuk karya satire, dan tidak
      mengacu pada perusahaan, lembaga, orang, atau lokasi nyata di mana pun.
      Tidak ada lembaga sertifikasi, wilayah, atau badan pengawas sungguhan yang
      disebut atau dituduh. Seluruh foto di situs ini dibuat dengan model
      generatif.
    </p>
    <p class="notice__link">
      <NuxtLink to="/legal">Baca penafian lengkap dan daftar kredit</NuxtLink>
    </p>
  </aside>
</template>

<script setup lang="ts">
// The fiction notice is on every page (R-38), because a satirical corporate
// register is exactly the shape a reader could mistake for the real thing.
withDefaults(defineProps<{ label?: string }>(), { label: 'Situs fiksi' })
</script>
