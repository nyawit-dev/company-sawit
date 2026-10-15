<template>
  <!-- A corporate contact form. Every field is validated on the client and
       there is nowhere for the submission to go: the company is fiction, so
       the form says what it does instead of pretending to transmit. -->
  <form class="mt-8 grid gap-6 md:grid-cols-2" @submit.prevent="onSubmit">
    <label class="block">
      <span
        class="mb-2 block font-mono text-[0.6875rem] tracking-wider uppercase text-quiet"
        >Nama</span
      >
      <input
        v-model="form.name"
        type="text"
        name="nama"
        autocomplete="name"
        required
        class="min-h-11 w-full rounded-lg border-2 border-hair bg-card px-4 py-3 font-sans text-base text-body transition-colors duration-150 ease-out focus:border-leaf-500 focus:outline-none"
      />
    </label>

    <label class="block">
      <span
        class="mb-2 block font-mono text-[0.6875rem] tracking-wider uppercase text-quiet"
        >Surel</span
      >
      <input
        v-model="form.email"
        type="email"
        name="surel"
        autocomplete="email"
        required
        class="min-h-11 w-full rounded-lg border-2 border-hair bg-card px-4 py-3 font-sans text-base text-body transition-colors duration-150 ease-out focus:border-leaf-500 focus:outline-none"
      />
    </label>

    <label class="block md:col-span-2">
      <span
        class="mb-2 block font-mono text-[0.6875rem] tracking-wider uppercase text-quiet"
        >Keperluan</span
      >
      <select
        v-model="form.purpose"
        name="keperluan"
        required
        class="min-h-11 w-full rounded-lg border-2 border-hair bg-card px-4 py-3 font-sans text-base text-body transition-colors duration-150 ease-out focus:border-leaf-500 focus:outline-none"
      >
        <option value="">Pilih salah satu</option>
        <option value="media">Permintaan media</option>
        <option value="investor">Hubungan investor</option>
        <option value="mitra">Kemitraan plasma</option>
        <option value="ganti-rugi">Klaim ganti rugi lahan</option>
        <!-- The last option in the list is the one that matters, and it routes
             to the same inbox as the media request. -->
        <option value="pengaduan">Pengaduan warga</option>
      </select>
    </label>

    <label class="block md:col-span-2">
      <span
        class="mb-2 block font-mono text-[0.6875rem] tracking-wider uppercase text-quiet"
        >Pesan</span
      >
      <textarea
        v-model="form.message"
        name="pesan"
        rows="5"
        required
        class="w-full rounded-lg border-2 border-hair bg-card px-4 py-3 font-sans text-base text-body transition-colors duration-150 ease-out focus:border-leaf-500 focus:outline-none"
      ></textarea>
    </label>

    <div
      class="flex flex-wrap items-center gap-4 md:col-span-2"
    >
      <!-- NEFA's button geometry, same as the hero pair: pill radius, 32px
           padding, 14px at weight 400. It was still at 16px/600 after the sweep,
           which made this button visibly heavier than the two in the hero that
           it shares a page with. -->
      <button
        type="submit"
        :disabled="sent"
        class="inline-flex min-h-11 cursor-pointer items-center rounded-full border-2 border-leaf-600 bg-leaf-600 px-8 py-4 text-sm font-normal text-white shadow-[0_3px_0_var(--color-leaf-800)] transition-transform duration-150 ease-out hover:-translate-y-0.5 hover:shadow-[0_5px_0_var(--color-leaf-800)] active:translate-y-0.5 active:shadow-[0_1px_0_var(--color-leaf-800)] disabled:cursor-not-allowed disabled:opacity-70"
      >
        {{ sent ? 'Terkirim' : 'Kirim' }}
      </button>
      <p class="m-0 max-w-md text-sm leading-relaxed text-quiet">
        Pengaduan warga dan permintaan media diteruskan ke unit hubungan
        korporat yang sama.
      </p>
    </div>

    <p
      v-if="sent"
      role="status"
      class="m-0 rounded-lg border-2 border-dashed border-leaf-400 bg-sunken p-5 text-sm leading-relaxed text-body md:col-span-2"
    >
      Borang ini tidak mengirim data ke mana pun. PT Perkebunan Asap Emas
      Nusantara tidak ada, dan tidak ada kotak masuk yang menunggu pesan Anda.
    </p>
  </form>
</template>

<script setup lang="ts">
const form = reactive({
  name: '',
  email: '',
  purpose: '',
  message: '',
})

const sent = ref(false)

function onSubmit() {
  // Deliberately no network call. A form that posts to a dead endpoint is
  // worse than one that states plainly that nothing is listening.
  sent.value = true
}
</script>
