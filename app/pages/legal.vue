<template>
  <article>
    <!-- Register A: the filing. The legal page is deliberately the most boring
         page on the site, because a disclaimer that reads like marketing is a
         disclaimer nobody believes. -->
    <header class="border-b-2 border-hair bg-sunken">
      <div class="mx-auto max-w-6xl px-6 py-16 md:py-20">
        <img
          :src="logoUrl"
          alt="Segel PT Perkebunan Asap Emas Nusantara"
          width="72"
          height="72"
          class="mb-6 w-18"
        />
        <p
          class="m-0 mb-3 font-mono text-[0.6875rem] tracking-wider uppercase text-quiet"
        >
          Penafian &amp; kredit &middot; dokumen hukum
        </p>
        <h1
          class="m-0 max-w-3xl text-[clamp(1.75rem,4.5vw,2.75rem)] leading-[1.1] font-extrabold tracking-tight text-body"
        >
          Ini bukan perusahaan. Ini karya fiksi.
        </h1>
        <p
          class="m-0 mt-4 max-w-2xl text-[clamp(1rem,1.9vw,1.125rem)] leading-relaxed text-quiet"
        >
          Halaman ini menjelaskan apa yang nyata dan apa yang tidak di situs ini,
          siapa yang membuat gambar yang Anda lihat, dan mengapa tidak ada satu
          pun nama, tempat, atau lembaga sungguhan yang disebut di dalamnya.
        </p>
      </div>
    </header>

    <!-- 01. DISCLAIMER -->
    <section class="border-b-2 border-hair">
      <div class="mx-auto max-w-6xl px-6 py-12 md:py-16">
        <SectionHead num="01" title="Penafian">
          Bagian berikut berlaku untuk seluruh isi situs ini tanpa kecuali.
        </SectionHead>

        <div class="mt-8 grid max-w-3xl gap-4">
          <p
            v-for="clause in disclaimer"
            :key="clause.head"
            class="m-0 text-[1.0625rem] leading-relaxed text-quiet"
          >
            <strong class="font-extrabold text-body">{{ clause.head }}</strong>
            {{ clause.body }}
          </p>
        </div>
      </div>
    </section>

    <!-- 02 + 03. WHY NO REAL NAMES, AND THE ONE BORROWED NAME -->
    <section class="border-b-2 border-hair">
      <div class="mx-auto max-w-6xl px-6 py-12 md:py-16">
        <div class="grid items-start gap-12 lg:grid-cols-2">
          <div>
            <SectionHead num="02" title="Mengapa tidak ada nama nyata">
              Bukan karena hati-hati berlebihan. Satire yang menyebut nama
              lembaga atau wilayah sungguhan dalam tuduhan fiktif berubah menjadi
              tuduhan, dan itu bisa digugat.
            </SectionHead>
            <p class="m-0 mt-6 text-[1.0625rem] leading-relaxed text-quiet">
              Karena itu dunia situs ini dibangun dari nol: Desa Konoha sebagai
              lokasi, Ryo sebagai mata uang, Dewan Hijau sebagai badan audit
              rekaan, Negeri Api sebagai negara. Tidak ada satu pun rujukan ke
              dunia nyata, dan itu membuat karya ini murni fiksi dari ujung ke
              ujung.
            </p>
          </div>

          <div>
            <SectionHead
              num="03"
              title="Catatan soal nama Konoha"
              subtitle="Satu-satunya nama yang bukan rekaan sepenuhnya."
            />
            <p class="m-0 mt-6 text-[1.0625rem] leading-relaxed text-quiet">
              &ldquo;Konoha&rdquo; diambil dari dunia fiksi anime
              <em class="font-bold text-body not-italic">Naruto</em>, yang
              merupakan karya berhak cipta milik pemegang haknya. Nama itu
              dipakai di sini sebagai penghormatan dan penanda fiksi, bukan untuk
              mengklaim kepemilikan atas karya tersebut atau berafiliasi dengan
              pemegang haknya.
            </p>
            <p class="m-0 mt-4 text-[1.0625rem] leading-relaxed text-quiet">
              Jika Anda pemegang hak atas karya tersebut dan keberatan atas
              pemakaian namanya di laman ini, ganti namanya cukup satu kali edit
              di seluruh berkas situs ini, dan seluruh dunia situs akan berubah
              menjadi rekaan sepenuhnya tanpa nama pinjaman.
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- 04. CREDITS -->
    <section class="border-b-2 border-hair">
      <div class="mx-auto max-w-6xl px-6 py-12 md:py-16">
        <SectionHead num="04" title="Kredit">
          Apa yang sungguhan di situs ini, dan siapa pembuatnya.
        </SectionHead>

        <div
          class="mt-8 overflow-hidden rounded-2xl border-2 border-hair bg-card"
        >
          <div class="overflow-x-auto">
            <table class="w-full border-collapse text-left text-sm">
              <caption
                class="border-b border-hair px-5 py-4 text-left font-mono text-[0.625rem] leading-relaxed tracking-wider text-quiet uppercase"
              >
                Komponen situs dan asal-usulnya.
              </caption>
              <thead>
                <tr class="border-b border-hair">
                  <th
                    scope="col"
                    class="px-5 py-3 font-mono text-[0.625rem] tracking-wider text-quiet uppercase"
                  >
                    Komponen
                  </th>
                  <th
                    scope="col"
                    class="px-5 py-3 font-mono text-[0.625rem] tracking-wider text-quiet uppercase"
                  >
                    Pembuat
                  </th>
                  <th
                    scope="col"
                    class="px-5 py-3 font-mono text-[0.625rem] tracking-wider text-quiet uppercase"
                  >
                    Lisensi
                  </th>
                </tr>
              </thead>
              <tbody>
                <tr
                  v-for="row in credits"
                  :key="row.component"
                  class="border-b border-hair transition-colors duration-150 ease-out last:border-b-0 hover:bg-sunken"
                >
                  <th
                    scope="row"
                    class="px-5 py-3 text-sm font-bold text-body"
                  >
                    {{ row.component }}
                  </th>
                  <td class="px-5 py-3 text-sm text-quiet">{{ row.maker }}</td>
                  <td class="px-5 py-3 text-sm text-quiet">
                    {{ row.license }}
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </section>

    <!-- 05. THE ONE-PARAGRAPH VERSION -->
    <section class="border-b-2 border-hair">
      <div class="mx-auto max-w-6xl px-6 py-12 md:py-16">
        <SectionHead num="05" title="Ringkasnya">
          Jika Anda ingin satu paragraf untuk ditunjukkan kepada siapa pun yang
          bertanya, pakai yang ini.
        </SectionHead>

        <blockquote
          class="m-0 mt-8 max-w-3xl rounded-2xl border-2 border-leaf-400 bg-[var(--harm-leaf-bg)] p-6 text-[1.0625rem] leading-relaxed text-body"
        >
          Situs ini adalah karya satire. Perusahaan, desa, mata uang, badan
          audit, dan seluruh angka di dalamnya adalah rekaan. Tidak ada
          perusahaan, lembaga, wilayah, atau orang nyata yang disebut atau
          dituduh. Semua foto dibuat dengan model generatif dan diberi
          keterangan sebagai demikian. Satu-satunya nama pinjaman adalah
          &ldquo;Konoha&rdquo; dari dunia fiksi Naruto, yang dipakai sebagai
          penanda fiksi.
        </blockquote>
      </div>
    </section>

    <FictionNotice label="Situs fiksi" />
  </article>
</template>

<script setup lang="ts">
// Bound, not literal: a literal public/ path gets rewritten into a static
// import by the bundler, and public/ is not an import root.
const logoUrl = '/company-sawit/logo.svg'

const disclaimer = [
  {
    head: 'PT Perkebunan Asap Emas Nusantara tidak ada.',
    body: ' Nama tersebut diciptakan untuk karya satire ini. Perusahaan tersebut tidak terdaftar di mana pun, tidak memiliki izin, tidak memiliki karyawan, tidak memiliki pabrik, dan tidak pernah melakukan apa pun yang dijelaskan di laman ini karena ia tidak pernah ada.',
  },
  {
    head: 'Seluruh angka, tabel, dan peristiwa adalah rekaan.',
    body: ' Setiap angka yang ditampilkan sebagai “dilaporkan perusahaan” tidak berasal dari perusahaan mana pun, karena tidak ada perusahaannya. Kolom berjudul “Yang tidak dicakup” ditulis untuk laman ini dan bukan kutipan dari dokumen nyata.',
  },
  {
    head: 'Tidak ada orang nyata yang dinamai.',
    body: ' Situs ini tidak menyebut nama orang, jabatan yang ditempati individu tertentu, atau peran apa pun yang bisa dihubungkan ke manusia sungguhan. Tabel pengurus memuat jabatan, bukan nama, justru karena itu.',
  },
  {
    head: 'Tidak ada tempat, lembaga, atau badan sungguhan yang disebut.',
    body: ' Desa Konoha beserta seluruh cakrawala situs ini adalah lokasi rekaan dalam dunia fiksi. Situs ini tidak menyebut nama provinsi, kota, pelabuhan, sungai, bursa efek, lembaga sertifikasi, atau badan pengawas mana pun di dunia nyata, dan tidak menuduh lembaga sungguhan atas apa pun. Nama mata uang “Ryo” adalah mata uang rekaan.',
  },
  {
    head: 'Tidak ada testimoni, tidak ada sumber, tidak ada kutipan.',
    body: ' Situs ini tidak mengutip media, laporan, putusan pengadilan, atau dokumen apa pun. Tidak ada klaim di laman ini yang diklaim berasal dari sumber primer, karena tidak ada sumbernya.',
  },
  {
    head: 'Gambar adalah hasil generatif.',
    body: ' Setiap foto di situs ini dibuat dengan model generatif, diberi keterangan sebagai demikian di tempatnya, dan bukan dokumentasi kejadian nyata.',
  },
]

const credits = [
  {
    component: 'Konsep, teks, dan struktur',
    maker: 'Dibuat atas permintaan pemilik repositori',
    license: 'Hak cipta pada pemilik situs',
  },
  {
    component: 'Foto lanskap dan objek',
    maker: 'Dihasilkan dengan model generatif',
    license: 'Lihat ketentuan penyedia model',
  },
  {
    component: 'Segel dan logo',
    maker: 'SVG digambar tangan untuk situs ini',
    license: 'Hak cipta pada pemilik situs',
  },
  {
    component: 'Font Nunito',
    maker: 'Vernon Adams dkk.',
    license: 'SIL Open Font License 1.1',
  },
  {
    component: 'Font IBM Plex Mono',
    maker: 'Mike Abbink, IBM',
    license: 'SIL Open Font License 1.1',
  },
  {
    component: 'Kerangka situs',
    maker: 'Nuxt 4 (MIT) dan Tailwind CSS (MIT)',
    license: 'MIT',
  },
  {
    component: 'Nama Desa Konoha',
    maker: 'Dunia fiksi Naruto',
    license: 'Hak cipta pemegang hak karya tersebut',
  },
]
</script>
