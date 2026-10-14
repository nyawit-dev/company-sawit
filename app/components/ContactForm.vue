<template>
  <form class="form" @submit.prevent="onSubmit">
    <!-- A corporate contact form. Every field is validated on the client and
         there is nowhere for the submission to go: the company is fiction, so
         the form says what it does instead of pretending to transmit. -->
    <div class="form__row">
      <label class="field">
        <span class="field__label">Nama</span>
        <input
          v-model="form.name"
          class="field__input"
          type="text"
          name="nama"
          autocomplete="name"
          required
        />
      </label>

      <label class="field">
        <span class="field__label">Surel</span>
        <input
          v-model="form.email"
          class="field__input"
          type="email"
          name="surel"
          autocomplete="email"
          required
        />
      </label>
    </div>

    <label class="field">
      <span class="field__label">Keperluan</span>
      <select v-model="form.purpose" class="field__input" name="keperluan" required>
        <option value="">Pilih salah satu</option>
        <option value="media">Permintaan media</option>
        <option value="investor">Hubungan investor</option>
        <option value="mitra">Kemitraan plasma</option>
        <option value="ganti-rugi">Klaim ganti rugi lahan</option>
        <option value="pengaduan">Pengaduan warga</option>
      </select>
    </label>

    <label class="field">
      <span class="field__label">Pesan</span>
      <textarea
        v-model="form.message"
        class="field__input field__input--area"
        name="pesan"
        rows="5"
        required
      />
    </label>

    <div class="form__foot">
      <button class="button" type="submit" :disabled="sent">
        {{ sent ? 'Terkirim' : 'Kirim' }}
      </button>
      <!-- The last option in the list is the one that matters, and it routes
           to the same inbox as the media request. -->
      <p class="form__note">
        Pengaduan warga dan permintaan media diteruskan ke unit hubungan
        korporat yang sama.
      </p>
    </div>

    <p v-if="sent" class="form__sent" role="status">
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
