<template>
  <article>
    <!-- Register A: the filing. The company talking about itself, in the
         institutional register, with the emblem it would use to do it. -->
    <header class="border-b-2 border-hair bg-sunken">
      <div class="mx-auto max-w-6xl px-6 py-16 md:py-20">
        <img
          :src="logoUrl"
          alt=""
          width="72"
          height="72"
          class="mb-6 w-18 transition-transform duration-500 ease-out hover:rotate-12"
        />
        <p
          class="m-0 mb-3 font-mono text-[0.6875rem] tracking-wider uppercase text-quiet"
        >
          Identitas perusahaan &middot; Nomor Registrasi Desa 812.000.XXX
          &middot; Konoha
        </p>
        <h1
          class="m-0 max-w-3xl text-[clamp(1.75rem,4.5vw,2.75rem)] leading-[1.1] font-extrabold tracking-tight text-body"
        >
          Perusahaan yang kami tulis untuk diri kami sendiri.
        </h1>
        <p
          class="m-0 mt-4 max-w-2xl text-[clamp(1rem,1.9vw,1.125rem)] leading-relaxed text-quiet"
        >
          Halaman ini memuat apa yang PT Perkebunan Asap Emas Nusantara katakan
          tentang dirinya: sejarahnya, sertifikat yang dikantungnya, dan susunan
          dewan komisarisnya. Tidak ada bagian dari halaman ini yang ditulis
          oleh pihak yang dirugikan.
        </p>
      </div>
    </header>

    <!-- 01. HISTORY -->
    <section class="border-b-2 border-hair">
      <div class="mx-auto max-w-6xl px-6 py-12 md:py-16">
        <SectionHead num="01" title="Sejarah">
          Berikut riwayat perusahaan sebagaimana dicatat dalam prospektus
          penawaran umum saham kami tahun 2019. Riwayat yang sama, dibaca dari
          sisi yang berbeda, adalah catatan penggusuran.
        </SectionHead>

        <div class="grid items-start gap-8 lg:grid-cols-5 lg:gap-12">
          <div
            class="overflow-hidden rounded-2xl border-2 border-hair bg-card lg:col-span-3"
          >
            <div class="overflow-x-auto">
              <table class="w-full border-collapse text-left text-sm">
                <caption
                  class="border-b border-hair px-5 py-4 text-left font-mono text-[0.625rem] leading-relaxed tracking-wider text-quiet uppercase"
                >
                  Tonggak perusahaan 1998&ndash;2024, menurut dokumen resmi
                  perusahaan.
                </caption>
                <thead>
                  <tr class="border-b border-hair">
                    <th
                      scope="col"
                      class="px-5 py-3 font-mono text-[0.625rem] tracking-wider text-quiet uppercase"
                    >
                      Tahun
                    </th>
                    <th
                      scope="col"
                      class="px-5 py-3 font-mono text-[0.625rem] tracking-wider text-quiet uppercase"
                    >
                      Peristiwa menurut perusahaan
                    </th>
                    <th
                      scope="col"
                      class="px-5 py-3 font-mono text-[0.625rem] tracking-wider text-quiet uppercase"
                    >
                      Yang tidak dicakup
                    </th>
                  </tr>
                </thead>
                <tbody>
                  <tr
                    v-for="row in history"
                    :key="row.year"
                    class="border-b border-hair transition-colors duration-150 ease-out last:border-b-0 hover:bg-sunken"
                  >
                    <th
                      scope="row"
                      class="px-5 py-3 font-mono text-sm font-bold whitespace-nowrap text-body"
                    >
                      {{ row.year }}
                    </th>
                    <td class="px-5 py-3 text-sm text-quiet">
                      {{ row.event }}
                    </td>
                    <td class="px-5 py-3 text-sm text-quiet">
                      {{ row.omitted }}
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>

          <figure class="m-0 lg:col-span-2">
            <img
              :src="asset_company_sawit_img_mill_jpg"
              alt="Pabrik pengolahan kelapa sawit pada senja, dengan cerobong boiler tinggi, struktur konveyor, dan lampu kerja yang mulai menyala"
              width="1600"
              height="1067"
              loading="lazy"
              class="block w-full rounded-2xl border-2 border-hair object-cover transition-transform duration-500 ease-out hover:scale-102"
            />
            <figcaption
              class="mt-3 font-mono text-[0.625rem] leading-relaxed text-quiet"
            >
              Pabrik blok tengah, beroperasi sejak 2009. Gambar dibuat dengan
              model generatif untuk laman ini; bukan foto bangunan yang ada.
            </figcaption>
          </figure>
        </div>
      </div>
    </section>

    <!-- 02. CERTIFICATIONS -->
    <section class="border-b-2 border-hair">
      <div class="mx-auto max-w-6xl px-6 py-12 md:py-16">
        <SectionHead num="02" title="Sertifikasi">
          Kami tidak menyebut nama lembaga penerbit, karena tidak ada lembaga
          yang menerbitkannya. Nama sertifikat di bawah adalah nama yang kami
          pakai sendiri.
        </SectionHead>

        <!-- Three seals. Each one rotates a little on hover, because a seal
             that does not move is a picture of a seal. -->
        <div class="grid gap-5 md:grid-cols-3">
          <div
            v-for="seal in seals"
            :key="seal.name"
            class="flex items-center gap-4 rounded-2xl border-2 border-hair bg-card p-5 transition-transform duration-300 ease-out hover:-translate-y-1"
          >
            <img
              :src="asset_company_sawit_logo_mark_svg"
              alt=""
              width="40"
              height="40"
              class="w-10 shrink-0 transition-transform duration-500 ease-out group-hover:rotate-12"
            />
            <div class="min-w-0">
              <p
                class="m-0 font-mono text-xs font-bold tracking-wide text-body"
              >
                {{ seal.name }}
              </p>
              <p class="m-0 mt-1 text-sm text-quiet">{{ seal.scope }}</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- 03. THE BOARD -->
    <section class="border-b-2 border-hair">
      <div class="mx-auto max-w-6xl px-6 py-12 md:py-16">
        <!-- The board: the table every listed company publishes. Rows carry no
             names, because naming fictional people is the one thing a satire
             cannot do honestly. -->
        <SectionHead num="03" title="Dewan komisaris dan direksi">
          Susunan pengurus sesuai anggaran dasar. Nama tidak dicantumkan: orang
          dalam rekaan ini tidak punya nama, dan menamai mereka akan membuatnya
          tampak nyata.
        </SectionHead>

        <div
          class="overflow-hidden rounded-2xl border-2 border-hair bg-card"
        >
          <div class="overflow-x-auto">
            <table class="w-full border-collapse text-left text-sm">
              <caption
                class="border-b border-hair px-5 py-4 text-left font-mono text-[0.625rem] leading-relaxed tracking-wider text-quiet uppercase"
              >
                Susunan pengurus dan masa jabatan, menurut anggaran dasar.
              </caption>
              <thead>
                <tr class="border-b border-hair">
                  <th
                    v-for="col in boardColumns"
                    :key="col"
                    scope="col"
                    class="px-5 py-3 font-mono text-[0.625rem] tracking-wider text-quiet uppercase"
                  >
                    {{ col }}
                  </th>
                </tr>
              </thead>
              <tbody>
                <tr
                  v-for="person in board"
                  :key="person.role"
                  class="border-b border-hair transition-colors duration-150 ease-out last:border-b-0 hover:bg-sunken"
                >
                  <th
                    scope="row"
                    class="px-5 py-3 text-sm font-bold whitespace-nowrap text-body"
                  >
                    {{ person.role }}
                  </th>
                  <td class="px-5 py-3 font-mono text-sm text-quiet">
                    {{ person.term }}
                  </td>
                  <td class="px-5 py-3 text-sm text-quiet">
                    {{ person.background }}
                  </td>
                  <td class="px-5 py-3 text-sm text-quiet">
                    {{ person.omitted }}
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </section>

    <!-- 04. LAND -->
    <section class="border-b-2 border-hair">
      <div class="mx-auto max-w-6xl px-6 py-12 md:py-16">
        <div class="grid items-start gap-8 lg:grid-cols-2 lg:gap-12">
          <figure class="m-0">
            <img
              :src="asset_company_sawit_img_clear_cut_jpg"
              alt="Foto udara area perkebunan yang baru ditanami dengan barisan geometris muda, dan pita hutan gelap yang belum tersentuh di tepi atas bingkai"
              width="1600"
              height="1200"
              loading="lazy"
              class="block w-full rounded-2xl border-2 border-hair object-cover transition-transform duration-500 ease-out hover:scale-102"
            />
            <figcaption
              class="mt-3 font-mono text-[0.625rem] leading-relaxed text-quiet"
            >
              Blok barat, tahun tanam 2023. Gambar dibuat dengan model generatif
              untuk laman ini.
            </figcaption>
          </figure>

          <div>
            <SectionHead num="04" title="Lahan">
              412.000 hektare konsesi kami membentang di tiga kabupaten.
              Sebanyak 391.000 hektare ditanami sebelum komitmen 2018 kami
              berlaku, sehingga tercatat sebagai lahan historis.
            </SectionHead>
            <p class="m-0 text-[1.0625rem] leading-relaxed text-quiet">
              Kami tidak memublikasikan peta konsesi. Kami menerbitkan peta
              lokasi pabrik, yang tidak membingungkan siapa pun.
            </p>
          </div>
        </div>
      </div>
    </section>

    <FictionNotice />
  </article>
</template>

<script setup lang="ts">
// Bound rather than literal: rolldown rewrites a literal public/
// path into a static import, and public/ is not an import root.
const asset_company_sawit_logo_mark_svg = '/company-sawit/logo-mark.svg'

// Bound rather than literal: rolldown rewrites a literal public/
// path into a static import, and public/ is not an import root.
const asset_company_sawit_img_mill_jpg = '/company-sawit/img/mill.jpg'

// Bound rather than literal: rolldown rewrites a literal public/
// path into a static import, and public/ is not an import root.
const asset_company_sawit_img_clear_cut_jpg = '/company-sawit/img/clear-cut.jpg'

// Bound, not literal: a literal public/ path gets rewritten into a static
// import by the bundler, and public/ is not an import root.
const logoUrl = '/company-sawit/logo.svg'

const history = [
  {
    year: '1998',
    event: 'Perusahaan didirikan dengan izin lokasi 12.000 ha',
    omitted: 'Izin diterbitkan 4 bulan setelah kebakaran besar meratakan lokasi',
  },
  {
    year: '2004',
    event: 'Ekspansi ke blok timur, tambahan 48.000 ha',
    omitted: '21 keluarga di blok timur belum menerima ganti rugi',
  },
  {
    year: '2009',
    event: 'Pabrik blok tengah beroperasi',
    omitted: 'Limbah cair dialirkan ke sungai tanpa IPAL',
  },
  {
    year: '2013',
    event: 'Terdaftar di bursa efek Negeri Api',
    omitted: 'Prospektus tidak memuat risiko kebakaran gambut',
  },
  {
    year: '2015',
    event: 'Kabut asap melintasi perbatasan negara',
    omitted: 'Tercatat sebagai bencana alam, tanpa penyelidikan internal',
  },
  {
    year: '2018',
    event: 'Komitmen tanpa pembalakan dan tanpa gambut baru',
    omitted: 'Tidak berlaku surut untuk 391.000 ha yang sudah ditanami',
  },
  {
    year: '2024',
    event: '412.000 ha konsesi, 1,4 juta ton TBS',
    omitted: 'Audit keberlanjutan ditunda ke 2026',
  },
]

const seals = [
  { name: 'Keberlanjutan perkebunan', scope: 'Diklaim sejak 2019 · belum diaudit' },
  { name: 'Pratik kebun terbaik', scope: 'Diberikan oleh asosiasi yang kami ketuai' },
  { name: 'Perusahaan hijau', scope: 'Kriteria kelayakan tidak dipublikasikan' },
]

const boardColumns = [
  'Jabatan',
  'Masa jabatan',
  'Latar belakang',
  'Yang tidak dicakup',
]

const board = [
  {
    role: 'Komisaris utama',
    term: '2013–sekarang',
    background: 'Kehutanan industri',
    omitted: 'Mantan penerbit izin lokasi 1998',
  },
  {
    role: 'Direktur utama',
    term: '2018–sekarang',
    background: 'Keuangan korporasi',
    omitted: 'Menandatangani komitmen tanpa pembakaran 2018',
  },
  {
    role: 'Direktur operasional',
    term: '2015–sekarang',
    background: 'Teknik perkebunan',
    omitted: 'Bertanggung jawab atas pembukaan lahan',
  },
  {
    role: 'Direktur keberlanjutan',
    term: '2021–sekarang',
    background: 'Hubungan perusahaan',
    omitted: 'Jabatan dibentuk setelah kabut asap 2015',
  },
]
</script>
