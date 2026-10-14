<template>
  <article>
    <!-- Opening: one focal point, the claim itself. No pill above the H1 (R-09). -->
    <section class="opening">
      <div class="wrap">
        <p class="opening__meta">
          Laporan tahunan ke-27 &middot; tahun buku 2025
        </p>
        <h1>
          Kami menebang hutan, membakarnya, dan menyebutnya pembangunan.
        </h1>
        <p class="lede">
          Selama dua puluh tujuh tahun, Asap Emas mengubah hutan primer Kalimantan
          menjadi kebun kelapa sawit. Prosesnya melibatkan api, alat berat, dan
          warga yang menolak pindah. Laporan ini menyajikan ketiga hal itu sebagai
          capaian operasional.
        </p>
        <div class="notice" role="note">
          <strong>Situs fiksi</strong>
          PT Perkebunan Asap Emas Nusantara adalah rekaan. Seluruh angka,
          peristiwa, dan klaim di bawah ini bagian dari karya satire dan tidak
          mengacu pada perusahaan nyata. Tidak ada sumber di baliknya karena
          tidak ada yang terjadi.
        </div>
      </div>
    </section>

    <!-- The register: the company's own claims, labelled as its own. Numbers
         are presented as self-reported, never as sourced fact (R-17, R-36). -->
    <section id="register">
      <div class="wrap">
        <div class="section-head">
          <span class="section-no">01</span>
          <h2>Angka yang kami laporkan</h2>
        </div>
        <p>
          Semua angka di bawah berasal dari laporan internal kami sendiri. Tidak
          ada audit independen atas angka tersebut, dan tidak ada lembaga yang
          memverifikasinya. Kami memasukkannya ke laporan ini karena format
          laporan tahunan mewajibkan ada angka.
        </p>
        <div class="register">
          <div class="register__row">
            <span class="register__label">Luas konsesi</span>
            <p class="register__claim">
              Klaim kami: <mark>412.000 hektare</mark>. Angka ini diukur dari
              garis batas yang kami gambar sendiri, dan meliputi daerah yang
              masih dihuni warga hingga hari ini.
            </p>
          </div>
          <div class="register__row">
            <span class="register__label">Kejadian kabut asap</span>
            <p class="register__claim">
              Klaim kami: <mark>1.847 titik api terlacak</mark>. Kami
              mengklasifikasikan angka ini sebagai &ldquo;tidak dapat
              diatribusikan&rdquo;, sehingga tanggung jawab atasnya tidak jatuh
              pada pihak mana pun dalam dokumen ini.
            </p>
          </div>
          <div class="register__row">
            <span class="register__label">Kepindahan warga</span>
            <p class="register__claim">
              Klaim kami: <mark>6.200 keluarga direlokasi</mark>. Kami
              menggunakan kata &ldquo;relokasi&rdquo;. Warga yang terpengaruh
              menggunakan kata lain, dan perbedaan itu tidak tercatat di mana
              pun dalam laporan ini.
            </p>
          </div>
          <div class="register__row">
            <span class="register__label">Sertifikasi berkelanjutan</span>
            <p class="register__claim">
              Klaim kami: <mark>sertifikasi diperoleh</mark>. Kami tidak
              menyebutkan nama lembaga sertifikasi, tanggal audit, atau ruang
              lingkupnya, karena dokumen sertifikatnya dikeluarkan oleh
              konsultan yang kami bayar sendiri.
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- The ledger: how the clearing actually happened, as a sequence, not
         three rounded steps with icons (R-05). -->
    <section id="proses">
      <div class="wrap">
        <div class="section-head">
          <span class="section-no">02</span>
          <h2>Cara kami membersihkan lahan</h2>
        </div>
        <p>
          Urutan di bawah bukan diagram alur. Ini urutan kejadian yang sama
          berulang di setiap blok konsesi, disusun menurut apa yang terjadi
          lebih dahulu.
        </p>
        <div class="ledger">
          <div class="ledger__item">
            <h3>Pemetaan ulang</h3>
            <p class="ledger__where">Tahap 1, berlangsung sepanjang tahun</p>
            <p class="ledger__body">
              Tim survei kami menandai batas konsesi. Batas itu diperbarui
              berkala, dan setiap pembaruan menggeser garis keluar. Warga yang
              kemarin berada di luar garis hari ini berada di dalamnya.
            </p>
          </div>
          <div class="ledger__item">
            <h3>Pembakaran</h3>
            <p class="ledger__where">Tahap 2, musim kemarau</p>
            <p class="ledger__body">
              Sisa tebangan dibakar karena lebih murah daripada diangkut. Saat
              kabut asap mencapai daratan, kami menerbitkan pernyataan yang
              menyebutkan perubahan iklim, dan tidak menyebutkan kami.
            </p>
          </div>
          <div class="ledger__item">
            <h3>Penanaman</h3>
            <p class="ledger__where">Tahap 3, satu tahun setelah pembakaran</p>
            <p class="ledger__body">
              Bibit ditanam pada tanah yang kehilangan lapisan humusnya. Produksi
              tahap awal tinggi, lalu turun seiring tanah menipis. Blok berikutnya
              dibuka untuk menggantikannya, dan prosesnya dimulai lagi dari tahap
              satu.
            </p>
          </div>
          <div class="ledger__item">
            <h3>Pelaporan</h3>
            <p class="ledger__where">Berjalan terus, sepanjang tahun</p>
            <p class="ledger__body">
              Setiap tahap didokumentasikan, difoto, dan dimasukkan ke laporan
              keberlanjutan. Foto yang dipakai adalah foto tanam bibit. Foto
              pembakaran tidak dipakai karena kualitas gambarnya kurang baik.
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- Questions actually asked of this company, per R-28: no template FAQ. -->
    <section id="tanya">
      <div class="wrap">
        <div class="section-head">
          <span class="section-no">03</span>
          <h2>Pertanyaan yang benar-benar diajukan kepada kami</h2>
        </div>
        <div class="qa">
          <div class="qa__item" v-for="item in faq" :key="item.q">
            <button
              class="qa__q"
              type="button"
              :aria-expanded="open === item.q"
              :aria-controls="`a-${slug(item.q)}`"
              @click="toggle(item.q)"
            >
              <span>{{ item.q }}</span>
              <span class="qa__sign" aria-hidden="true">{{
                open === item.q ? '&minus;' : '+'
              }}</span>
            </button>
            <p class="qa__a" :id="`a-${slug(item.q)}`" :hidden="open !== item.q">
              {{ item.a }}
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- Contact: a form that actually submits and gives feedback (R-26, R-27). -->
    <section id="kontak">
      <div class="wrap">
        <div class="section-head">
          <span class="section-no">04</span>
          <h2>Hubungi bagian keberlanjutan kami</h2>
        </div>
        <p>
          Bagian ini menerima pertanyaan mengenai praktik lingkungan kami.
          Pertanyaan yang masuk akan diteruskan ke bagian yang sama yang
          menyusun laporan tahunan.
        </p>
        <form novalidate @submit.prevent="submit">
          <label class="field" for="nama">
            <span class="field__label">Nama</span>
            <input
              id="nama"
              v-model="form.nama"
              class="field__input"
              type="text"
              autocomplete="name"
              aria-describedby="nama-hint"
            />
            <span class="field__hint" id="nama-hint">Nama Anda, bukan nama perusahaan.</span>
          </label>

          <label class="field" for="surel">
            <span class="field__label">Surel</span>
            <input
              id="surel"
              v-model="form.surel"
              class="field__input"
              type="email"
              autocomplete="email"
              :aria-invalid="errors.surel ? 'true' : undefined"
              aria-describedby="surel-error"
            />
            <span class="field__error" id="surel-error" v-if="errors.surel">{{
              errors.surel
            }}</span>
          </label>

          <label class="field" for="pesan">
            <span class="field__label">Pertanyaan</span>
            <textarea
              id="pesan"
              v-model="form.pesan"
              class="field__area"
              aria-describedby="pesan-hint"
            ></textarea>
            <span class="field__hint" id="pesan-hint">
              Situs ini tidak mengirim ke mana pun. Tidak ada server, tidak ada
              basis data, tidak ada yang menerima.
            </span>
          </label>

          <button class="button" type="submit" :disabled="state === 'sending'">
            {{ state === 'sending' ? 'Mengirim' : 'Kirim pertanyaan' }}
          </button>

          <p class="form-status" :data-state="state" role="status">
            <template v-if="state === 'idle'">
              Belum ada yang dikirim.
            </template>
            <template v-else-if="state === 'sending'">Sedang memeriksa isian.</template>
            <template v-else-if="state === 'error'">
              {{ errors.form }}
            </template>
            <template v-else-if="state === 'sent'">
              Terkirim ke folder tempat surat tidak pernah dibalas. Pesan Anda
              tersimpan di peramban ini saja.
            </template>
          </p>
        </form>
      </div>
    </section>
  </article>
</template>

<script setup lang="ts">
const faq = [
  {
    q: 'Apakah kebakaran itu disengaja?',
    a: 'Kami tidak menjawab pertanyaan itu dengan ya atau tidak. Laporan tahunan kami menyebut peristiwa kebakaran pada bagian lampiran, tanpa kata ganti pelaku, dan bagian induk laporan tidak menyebutnya sama sekali.',
  },
  {
    q: 'Bagaimana nasib warga yang menolak direlokasi?',
    a: 'Mereka tetap tinggal. Tanah mereka berada di dalam garis batas yang kami gambar, dan garis itu tidak berubah karena mereka menolak. Yang berubah adalah akses mereka ke jalan yang kami kelola.',
  },
  {
    q: 'Berapa banyak hutan yang tersisa di konsesi Anda?',
    a: 'Kami tidak menyimpan angka itu. Dokumen yang kami miliki berisi luas yang sudah ditanami, bukan luas yang belum. Dua angka itu bukan saling melengkapi dalam laporan kami, karena yang kedua tidak pernah dihitung.',
  },
  {
    q: 'Apakah ada ganti rugi bagi warga terdampak kabut asap di luar konsesi?',
    a: 'Kabut asap melewati batas konsesi, dan pertanggungjawaban kami berhenti di batas itu. Kami menyebutkan hal tersebut di laporan keberlanjutan sebagai keterbatasan ruang lingkup, bukan sebagai konsekuensi.',
  },
]

const open = ref<string | null>(null)
function toggle(q: string) {
  open.value = open.value === q ? null : q
}
function slug(text: string) {
  return text
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, '-')
    .replace(/(^-|-$)/g, '')
}

const form = reactive({ nama: '', surel: '', pesan: '' })
const errors = reactive<Record<string, string>>({})
const state = ref<'idle' | 'sending' | 'sent' | 'error'>('idle')

function submit() {
  delete errors.form
  delete errors.surel

  if (!form.surel.trim()) {
    errors.surel = 'Surel diperlukan agar pertanyaan Anda tercatat.'
    state.value = 'error'
    return
  }
  if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(form.surel.trim())) {
    errors.surel = 'Format surel belum benar. Contoh: nama@domain.id'
    state.value = 'error'
    return
  }
  if (!form.pesan.trim()) {
    errors.form = 'Tulis pertanyaannya dulu. Kolom kosong tidak dikirim.'
    state.value = 'error'
    return
  }

  state.value = 'sending'
  window.setTimeout(() => {
    state.value = 'sent'
  }, 600)
}
</script>
