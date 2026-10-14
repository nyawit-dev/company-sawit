<template>
  <article>
    <!-- Register A: the filing. This is the page where the corporate voice is
         least able to hide what it is saying, which is the point of putting it
         in the same clean register as the company's own history. -->
    <section class="opening">
      <div class="wrap">
        <p class="opening__meta">Visi, misi, dan komitmen &middot; 2025</p>
        <h1>
          Kami akan terus membuka lahan baru sampai tidak ada lahan yang tersisa
          untuk dibuka.
        </h1>
        <p class="lede">
          Pernyataan berikut disusun oleh bagian hubungan perusahaan, disetujui
          dewan direksi, dan diterbitkan tanpa perubahan oleh bagian
          keberlanjutan. Kami menuliskannya apa adanya, termasuk bagian yang
          paling jarang dibaca.
        </p>
        <FictionNotice label="Halaman fiksi" />
      </div>
    </section>

    <!-- The vision statement, set as the company wrote it. No paraphrase, no
         editorial gloss: the sentence carries the satire on its own. -->
    <section id="visi">
      <div class="wrap">
        <div class="section-head">
          <span class="section-head__num">01</span>
          <h2>Visi</h2>
        </div>
        <blockquote class="vision">
          <p>
            Menjadi perusahaan perkebunan kelapa sawit terdepan yang
            mengubah seluruh hutan tropis yang tersisa menjadi kebun
            produktif, dan menyebut proses perubahan itu pembangunan.
          </p>
          <footer>Bagian hubungan perusahaan, disetujui tanpa perubahan</footer>
        </blockquote>
        <p>
          Pernyataan di atas tidak disunting oleh bagian keberlanjutan. Kami
          menerbitkannya sebagaimana adanya karena versi yang sudah diperhalus
          tidak lagi mengatakan apa yang kami maksud.
        </p>
      </div>
    </section>

    <!-- Mission, as a numbered list of the company's own commitments. Each one
         is a real corporate mission genre, and each one states what it
         actually commits to. -->
    <section id="misi">
      <div class="wrap">
        <div class="section-head">
          <span class="section-head__num">02</span>
          <h2>Misi</h2>
        </div>
        <div class="register">
          <div class="register__row" v-for="(item, i) in missions" :key="i">
            <span class="register__label">Misi {{ i + 1 }}</span>
            <p class="register__claim">
              {{ item }}
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- Values, set as a definition list rather than a card grid: the content
         is short and the contrast between the value's name and what it means
         in practice is the whole point (R-14, R-05). -->
    <section id="nilai">
      <div class="wrap">
        <div class="section-head">
          <span class="section-head__num">03</span>
          <h2>Nilai perusahaan</h2>
        </div>
        <div class="values">
          <div class="values__row" v-for="v in values" :key="v.name">
            <h3>{{ v.name }}</h3>
            <p class="values__body">{{ v.body }}</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Commitments with dates, as the company states them. The scope column
         is where each commitment quietly excludes the thing it names. -->
    <section id="komitmen">
      <div class="wrap">
        <div class="section-head">
          <span class="section-head__num">04</span>
          <h2>Komitmen bertahun</h2>
        </div>
        <p>
          Komitmen berikut memiliki tahun target. Kami mencantumkan lingkup
          yang tidak dicakup di kolom terakhir, karena tanpa kolom itu tabel ini
          akan terbaca sebagai janji.
        </p>
        <div class="table-wrap" tabindex="0" role="region"
             aria-label="Tabel, geser ke samping untuk melihat kolom lain">
          <table>
            <caption>Komitmen perusahaan dan lingkup pengecualiannya</caption>
            <thead>
              <tr>
                <th scope="col">Komitmen</th>
                <th scope="col">Tahun target</th>
                <th scope="col">Yang tidak dicakup</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="c in commitments" :key="c.name">
                <th scope="row">{{ c.name }}</th>
                <td class="num">{{ c.year }}</td>
                <td>{{ c.excluded }}</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </section>

    <section id="tutup">
      <div class="wrap">
        <div class="section-head">
          <span class="section-head__num">05</span>
          <h2>Cara kami mengukur kemajuan</h2>
        </div>
        <p>
          Kemajuan diukur dari luas yang sudah ditanami, bukan dari luas hutan
          yang tersisa. Dua angka itu tidak saling melengkapi dalam laporan ini,
          karena yang kedua tidak pernah kami hitung.
        </p>
        <p>
          Latar belakang perusahaan dan riwayat konsesi ada di halaman
          <NuxtLink to="/tentang">tentang</NuxtLink>. Praktik
          operasional di lapangan ada di
          <NuxtLink to="/">halaman utama</NuxtLink>.
        </p>
      </div>
    </section>
  </article>
</template>

<script setup lang="ts">
const missions = [
  'Mengubah seluruh hutan tropis yang tersisa di wilayah konsesi menjadi kebun kelapa sawit produktif.',
  'Menggunakan pembakaran sebagai metode pembukaan lahan paling efisien, dan menerbitkan pernyataan resmi setiap kali kabut asap mencapai daratan.',
  'Memindahkan warga yang tinggal di dalam garis batas konsesi, dan menyebut perpindahan itu relokasi sukarela.',
  'Memperoleh sertifikasi keberlanjutan dari lembaga yang lingkup auditnya kami susun sendiri.',
  'Menerbitkan laporan keberlanjutan setiap tahun, dengan foto tanam bibit dan tanpa foto pembakaran.',
]

const values = [
  {
    name: 'Efisiensi',
    body: 'Kami membakar sisa tebangan karena mengangkutnya lebih mahal. Biaya yang hemat adalah biaya yang tidak muncul di laporan kami.',
  },
  {
    name: 'Kepatuhan',
    body: 'Kami mematuhi setiap peraturan yang berlaku di wilayah tempat kami beroperasi, dan mengubah wilayah operasi ketika peraturannya berubah.',
  },
  {
    name: 'Transparansi',
    body: 'Kami menerbitkan laporan tahunan setiap tahun. Laporan itu memuat seluruh angka yang mendukung perusahaan, dan tidak memuat angka yang tidak.',
  },
  {
    name: 'Keberlanjutan',
    body: 'Kami berkomitmen untuk tidak membuka lahan gambut baru setelah 2025. Lahan gambut yang sudah kami bakar sebelum tahun tersebut tetap produktif.',
  },
  {
    name: 'Kemitraan',
    body: 'Kami bermitra dengan masyarakat melalui program plasma. Masyarakat menanam di lahan kami, menjual hasilnya kepada kami, dengan harga yang kami tetapkan.',
  },
]

const commitments = [
  {
    name: 'Berhenti membuka lahan gambut baru',
    year: '2025',
    excluded: 'Lahan gambut yang sudah dibuka dan dibakar sebelum 2025',
  },
  {
    name: 'Nol kebakaran di wilayah konsesi',
    year: '2030',
    excluded: 'Kebakaran yang tidak dapat diatribusikan ke pihak mana pun',
  },
  {
    name: 'Serap emisi setara net zero',
    year: '2050',
    excluded: 'Emisi dari pembukaan lahan yang terjadi sebelum tahun dasar',
  },
  {
    name: 'Ganti rugi penuh bagi warga terdampak',
    year: 'Belum ada tahun',
    excluded: 'Warga yang menolak relokasi, dan warga di luar batas konsesi',
  },
]
</script>

<style scoped>
.vision {
  margin: 0 0 1.5rem;
  padding: 1.5rem 0 0;
  border-top: 1px solid var(--rule-strong);
  max-width: 44rem;
}

.vision p {
  font-size: clamp(1.25rem, 2.6vw, 1.625rem);
  line-height: 1.32;
  letter-spacing: -0.02em;
  margin: 0 0 1rem;
  font-style: italic;
  color: var(--ink);
}

.vision footer {
  padding: 0;
  font-family: var(--mono);
  font-size: 0.6875rem;
  letter-spacing: 0.04em;
  text-transform: uppercase;
  color: var(--muted);
}

.values {
  border-top: 1px solid var(--rule-strong);
  max-width: 62rem;
}

.values__row {
  padding-block: 1.375rem;
  border-bottom: 1px solid var(--rule);
  display: grid;
  gap: 0.35rem 2rem;
}

.values__row h3 {
  margin: 0;
}

.values__body {
  margin: 0;
  max-width: 46rem;
}

@media (min-width: 48rem) {
  .values__row {
    grid-template-columns: 14rem 1fr;
    align-items: baseline;
  }
}
</style>
