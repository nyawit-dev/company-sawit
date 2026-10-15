<template>
  <article>
    <!-- Register A: the filing. This is the page where the corporate voice is
         least able to hide what it is saying, which is the point of putting it
         in the same clean register as the company's own history. -->
    <header class="border-b-2 border-hair bg-sunken">
      <div class="mx-auto max-w-6xl px-6 py-16 md:py-20">
        <p
          class="m-0 mb-3 font-mono text-[0.6875rem] tracking-wider uppercase text-quiet"
        >
          Visi, misi, dan komitmen &middot; 2025
        </p>
        <h1
          class="m-0 max-w-3xl text-hero font-semibold tracking-tight text-body"
        >
          Kami akan terus membuka lahan baru sampai tidak ada lahan yang tersisa
          untuk dibuka.
        </h1>
        <p
          class="m-0 mt-4 max-w-2xl text-[1.0625rem] leading-relaxed text-quiet"
        >
          Pernyataan berikut disusun oleh bagian hubungan perusahaan, disetujui
          dewan direksi, dan diterbitkan tanpa perubahan oleh bagian
          keberlanjutan. Kami menuliskannya apa adanya, termasuk bagian yang
          paling jarang dibaca.
        </p>
      </div>
    </header>

    <!-- The vision statement, set as the company wrote it. No paraphrase, no
         editorial gloss: the sentence carries the satire on its own. -->
    <section id="visi" class="border-b-2 border-hair">
      <div class="mx-auto max-w-6xl px-6 py-12 md:py-16">
        <SectionHead num="01" title="Visi" />

        <blockquote
          class="m-0 mt-8 max-w-3xl border-t-2 border-leaf-400 pt-6"
        >
          <p
            class="m-0 mb-4 text-title font-semibold tracking-tight text-body italic"
          >
            Menjadi perusahaan perkebunan kelapa sawit terdepan yang mengubah
            seluruh hutan tropis yang tersisa menjadi kebun produktif, dan
            menyebut proses perubahan itu pembangunan.
          </p>
          <footer
            class="p-0 font-mono text-[0.6875rem] tracking-wider text-quiet uppercase"
          >
            Bagian hubungan perusahaan, disetujui tanpa perubahan
          </footer>
        </blockquote>

        <p class="m-0 mt-6 max-w-3xl text-[1.0625rem] leading-relaxed text-quiet">
          Pernyataan di atas tidak disunting oleh bagian keberlanjutan. Kami
          menerbitkannya sebagaimana adanya karena versi yang sudah diperhalus
          tidak lagi mengatakan apa yang kami maksud.
        </p>
      </div>
    </section>

    <!-- Mission, as a numbered list of the company's own commitments. Each one
         is a real corporate mission genre, and each one states what it
         actually commits to. -->
    <section id="misi" class="border-b-2 border-hair">
      <div class="mx-auto max-w-6xl px-6 py-12 md:py-16">
        <SectionHead num="02" title="Misi" />

        <ol class="m-0 mt-8 grid list-none gap-4 p-0">
          <li
            v-for="(item, i) in missions"
            :key="i"
            class="flex flex-wrap items-start gap-4 rounded-lg border-2 border-hair bg-card p-5 transition-transform duration-300 ease-out hover:-translate-y-0.5"
          >
            <span
              class="grid size-8 shrink-0 place-items-center rounded-lg bg-leaf-600 font-mono text-xs font-semibold text-white"
              >{{ i + 1 }}</span
            >
            <p class="m-0 min-w-0 flex-1 text-[1.0625rem] leading-relaxed text-body">
              {{ item }}
            </p>
          </li>
        </ol>
      </div>
    </section>

    <!-- Values, set as a definition list rather than a card grid: the content
         is short and the contrast between the value's name and what it means
         in practice is the whole point (R-14, R-05). -->
    <section id="nilai" class="border-b-2 border-hair">
      <div class="mx-auto max-w-6xl px-6 py-12 md:py-16">
        <SectionHead num="03" title="Nilai perusahaan" />

        <dl class="m-0 mt-8 border-t-2 border-leaf-400">
          <div
            v-for="v in values"
            :key="v.name"
            class="grid gap-1 border-b border-hair py-5 md:grid-cols-[14rem_1fr] md:gap-8"
          >
            <dt
              class="m-0 text-[1.0625rem] font-semibold tracking-tight text-body"
            >
              {{ v.name }}
            </dt>
            <dd class="m-0 max-w-3xl text-[1.0625rem] leading-relaxed text-quiet">
              {{ v.body }}
            </dd>
          </div>
        </dl>
      </div>
    </section>

    <!-- Commitments with dates, as the company states them. The scope column
         is where each commitment quietly excludes the thing it names. -->
    <section id="komitmen" class="border-b-2 border-hair">
      <div class="mx-auto max-w-6xl px-6 py-12 md:py-16">
        <SectionHead num="04" title="Komitmen bertahun">
          Komitmen berikut memiliki tahun target. Kami mencantumkan lingkup yang
          tidak dicakup di kolom terakhir, karena tanpa kolom itu tabel ini
          akan terbaca sebagai janji.
        </SectionHead>

        <DataTable
                  caption="Komitmen perusahaan dan lingkup pengecualiannya."
                  :columns="commitmentColumns.map((label) => ({ label }))"
                  :rows="commitments.map((c) => [c.name, c.year, c.excluded])"
                />
      </div>
    </section>

    <section id="tutup" class="border-b-2 border-hair">
      <div class="mx-auto max-w-6xl px-6 py-12 md:py-16">
        <SectionHead num="05" title="Cara kami mengukur kemajuan" />
        <p class="m-0 mt-6 max-w-3xl text-[1.0625rem] leading-relaxed text-quiet">
          Kemajuan diukur dari luas yang sudah ditanami, bukan dari luas hutan
          yang tersisa. Dua angka itu tidak saling melengkapi dalam laporan ini,
          karena yang kedua tidak pernah kami hitung.
        </p>
        <p class="m-0 mt-4 max-w-3xl text-[1.0625rem] leading-relaxed text-quiet">
          Latar belakang perusahaan dan riwayat konsesi ada di halaman
          <NuxtLink
            to="/tentang"
            class="font-semibold text-leaf-700 underline decoration-2 underline-offset-2 transition-colors duration-150 ease-out hover:text-leaf-800 dark:text-leaf-300 dark:hover:text-leaf-200"
            >tentang</NuxtLink
          >. Praktik operasional di lapangan ada di
          <NuxtLink
            to="/"
            class="font-semibold text-leaf-700 underline decoration-2 underline-offset-2 transition-colors duration-150 ease-out hover:text-leaf-800 dark:text-leaf-300 dark:hover:text-leaf-200"
            >halaman utama</NuxtLink
          >.
        </p>
      </div>
    </section>

    <FictionNotice label="Halaman fiksi" />
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

const commitmentColumns = ['Komitmen', 'Tahun target', 'Yang tidak dicakup']

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
