<template>
  <article>
    <!-- Register B: the land. A full-bleed photograph of the concession, with
         the company's opening claim sitting on it. The form is an annual
         report hero; the sentence underneath it is the arson. -->
    <section class="hero">
      <img
        class="hero__media"
        :src="'/company-sawit/img/hero-aerial.jpg'"
      />
      <div class="hero__scrim" />

      <div class="wrap hero__inner">
        <p class="hero__eyebrow">
          <img :src="'/company-sawit/logo-mark.svg'" />
          Laporan Tahunan 2024
          <span>&middot;</span>
          PT Perkebunan Asap Emas Nusantara Tbk
        </p>

        <h1>Mengubah hutan Kalimantan menjadi perkebunan yang menguntungkan.</h1>

        <p class="hero__lede">
          Selama dua puluh enam tahun kami mengelola 412.000 hektare konsesi
          dengan prinsip yang kami sebut pembangunan berkelanjutan. Laporan ini
          memuat angka yang kami laporkan sendiri, tanpa audit pihak ketiga.
        </p>

        <div class="hero__actions">
          <NuxtLink class="button" to="/tentang">Tentang perusahaan</NuxtLink>
          <a class="button button--ghost" href="#angka\'">Lihat angka</a>
        </div>
      </div>
    </section>

    <!-- Register A: the filing. The stat strip every listed plantation
         company opens with. Each figure is the company's own self-reported
         claim, and the note under the row says so. -->
    <section class="stats">
      <div class="wrap">
        <div class="stats__grid">
          <div class="stats__item">
            <p class="stats__value">412.000 ha</p>
            <p class="stats__label">Konsesi di bawah pengelolaan</p>
          </div>
          <div class="stats__item">
            <p class="stats__value">1,4 juta ton</p>
            <p class="stats__label">TBS dipanen 2024</p>
          </div>
          <div class="stats__item">
            <p class="stats__value">Rp 9,8 triliun</p>
            <p class="stats__label">Pendapatan bersih</p>
          </div>
          <div class="stats__item">
            <p class="stats__value">27%</p>
            <p class="stats__label">Lahan diklaim tidak bocor</p>
          </div>
        </div>
        <p class="stats__note">
          Seluruh angka pada laman ini dilaporkan oleh perusahaan dan tidak
          diverifikasi pihak independen. Tidak ada data primer yang dipublikasikan
          bersamanya.
        </p>
      </div>
    </section>

    <!-- Register B again: the numbers register. Same claim language as the
         filing, but the land's register and a table with a column the company
         did not have to write. -->
    <section id="angka">
      <div class="wrap">
        <div class="section-head">
          <span class="section-head__num">01</span>
          <div>
            <h2>Angka yang kami laporkan</h2>
            <p>
              Berikut angka yang kami cantumkan dalam laporan tahunan, berdampingan
              dengan catatan yang tidak kami sertakan pada laporan tersebut.
            </p>
          </div>
        </div>

        <div class="table-wrap" tabindex="0" role="region"
             aria-label="Tabel, geser ke samping untuk melihat kolom lain">
  <table class="table">
            <caption class="table__caption">
              Ringkasan operasional 2019&ndash;2024, sebagaimana dilaporkan
              perusahaan. Kolom terakhir ditulis untuk laman ini.
            </caption>
            <thead>
              <tr>
                <th scope="col">Tahun</th>
                <th scope="col">Luas tanam ditambah (ha)</th>
                <th scope="col">TBS (juta ton)</th>
                <th scope="col">Yang tidak dicakup</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <th scope="row">2019</th>
                <td>34.500</td>
                <td>0,98</td>
                <td>Permukiman 3 dusun diizinkan tinggal hingga kontrak tanam</td>
              </tr>
              <tr>
                <th scope="row">2020</th>
                <td>41.200</td>
                <td>1,05</td>
                <td>Kabut asap tercatat Mei&ndash;Oktober, tidak disebut sebabnya</td>
              </tr>
              <tr>
                <th scope="row">2021</th>
                <td>52.800</td>
                <td>1,12</td>
                <td>3 permohonan ganti rugi ditolak, alasan tidak dipublikasikan</td>
              </tr>
              <tr>
                <th scope="row">2022</th>
                <td>61.400</td>
                <td>1,21</td>
                <td>Drainase kanal baru melewati 4.100 ha gambut</td>
              </tr>
              <tr>
                <th scope="row">2023</th>
                <td>58.900</td>
                <td>1,31</td>
                <td>Luas turun, produksi naik; penjelasan tidak diberikan</td>
              </tr>
              <tr>
                <th scope="row">2024</th>
                <td>63.600</td>
                <td>1,40</td>
                <td>Audit RSPO ditunda ke 2026</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </section>

    <!-- Register B, photograph-led: the clearing process. The photo carries
         what the prose refuses to. -->
    <section class="landscape">
      <img
        :src="'/company-sawit/img/clear-cut.jpg'"
      />
      <div class="landscape__scrim" />
      <div class="wrap landscape__inner">
        <div class="section-head">
          <span class="section-head__num">02</span>
          <div>
            <h2>Proses pembukaan lahan</h2>
            <p>
              Kami menyebut tahap ini <em>pembukaan lahan terintegrasi</em>. Yang
              terjadi di dalamnya adalah penebangan hutan, penumpukan sisa kayu,
              dan pembakaran pada malam tanpa angin.
            </p>
          </div>
        </div>
        <p>
          Prosedur kami menyatakan pembakaran dilarang. Prosedur kami juga
          menyatakan bahwa sisa penebangan yang membusuk di tengah lahan baru
          berisiko menjadi sumber penyakit, sehingga pelaksanaan di lapangan
          memilih pembakaran. Kedua kalimat tersebut sama-sama tercantum dalam
          dokumen yang sama, dipisahkan dua puluh tiga halaman.
        </p>
      </div>
    </section>

    <!-- Register A: operations, filing register, photo beside text. -->
    <section class="split split--wide-text">
      <div class="wrap">
        <div>
          <div class="section-head">
            <span class="section-head__num">03</span>
            <div>
              <h2>Operasional pabrik</h2>
              <p>
                Pabrik kelapa sawit bekerja dua puluh empat jam. Buah yang tiba
                dipanen paling lambat delapan belas jam sebelumnya, karena setelah
                itu kadar minyaknya turun dan muatannya ditolak.
              </p>
            </div>
          </div>
          <p>
            Penolakan muatan dicatat sebagai ketidakpatuhan mitra, bukan sebagai
            kesalahan penjadwalan. Pada 2024 tercatat 1.840 muatan ditolak dari
            41.000, atau 4,5%. Angka tersebut tidak pernah muncul dalam laporan
            tahunan kami.
          </p>
        </div>
        <figure class="figure">
          <img
            :src="'/company-sawit/img/mill.jpg'"
          />
          <figcaption>
            Pabrik pengolahan blok tengah, kapasitas 60 ton TBS per jam. Gambar
            dibuat dengan model generatif untuk laman ini; bukan foto perkebunan
            yang ada.
          </figcaption>
        </figure>
      </div>
    </section>

    <!-- Register A: the product. -->
    <section class="split split--wide-photo">
      <div class="wrap">
        <figure class="figure">
          <img
            :src="'/company-sawit/img/ffb.jpg'"
          />
          <figcaption>
            Tandan buah segar siap olah. Gambar dibuat dengan model generatif
            untuk laman ini.
          </figcaption>
        </figure>
        <div>
          <div class="section-head">
            <span class="section-head__num">04</span>
            <div>
              <h2>Produk</h2>
              <p>
                CPO dan PK diekspor melalui pelabuhan Balikpapan. Selebihnya
                dijual ke pembeli lokal yang namanya tidak kami publikasikan,
                karena kami tidak mengaudit mereka dan mereka tidak mengaudit kami.
              </p>
            </div>
          </div>
          <p>
            Kami menerapkan kebijakan tanpa pembalakan, tanpa pembakaran, dan
            tanpa pengembangan gambut baru. Ketiganya berlaku untuk lahan yang
            kami tanami setelah 2018. Lahan yang kami tanami sebelum 2018 tidak
            tercakup, dan jumlahnya 391.000 hektare.
          </p>
        </div>
      </div>
    </section>

    <!-- Register A: the certification badge row, the shape every plantation
         company uses. Note that no certification body is named. -->
    <section class="badges-section">
      <div class="wrap">
        <div class="section-head">
          <span class="section-head__num">05</span>
          <div>
            <h2>Sertifikasi yang kami klaim</h2>
            <p>
              Segel berikut kami tampilkan sesuai praktik industri. Cakupan
              masing-masing tercatat apa adanya.
            </p>
          </div>
        </div>
        <div class="badges">
          <div class="badge">
            <img class="badge__seal" :src="'/company-sawit/logo-mark.svg'" />
            <div>
              <p class="badge__name">Keberlanjutan sawit</p>
              <p class="badge__scope">Berlaku untuk 21.000 ha ditanam setelah 2018</p>
            </div>
          </div>
          <div class="badge">
            <img class="badge__seal" :src="'/company-sawit/logo-mark.svg'" />
            <div>
              <p class="badge__name">Mutu produk kelapa sawit</p>
              <p class="badge__scope">Berlaku untuk 1 pabrik blok tengah</p>
            </div>
          </div>
          <div class="badge">
            <img class="badge__seal" :src="'/company-sawit/logo-mark.svg'" />
            <div>
              <p class="badge__name">Tanpa pembalakan</p>
              <p class="badge__scope">Berlaku sejak 2018, tidak berlaku surut</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Register B: the fire, named plainly. -->
    <section class="landscape">
      <img
        :src="'/company-sawit/img/fire.jpg'"
      />
      <div class="landscape__scrim" />
      <div class="wrap landscape__inner">
        <div class="section-head">
          <span class="section-head__num">06</span>
          <div>
            <h2>Kebakaran lahan gambut</h2>
            <p>
              Laporan kami menyebut kebakaran tahunan sebagai
              <em>peristiwa alam</em>. Lahan gambut tidak terbakar sendiri.
              Gambut yang telah dikeringkan dengan kanal drainase menjadi
              bahan bakar.
            </p>
          </div>
        </div>
        <p>
          Kami tidak memublikasikan lokasi kebakaran, luas yang terbakar, atau
          waktu pemadaman. Yang kami publikasikan adalah jumlah alat pemadam
          yang kami miliki, yaitu sebelas, untuk 412.000 hektare.
        </p>
      </div>
    </section>

    <!-- Register A: contact, the corporate form. -->
    <section id="kontak">
      <div class="wrap">
        <div class="section-head">
          <span class="section-head__num\'">07</span>
          <div>
            <h2>Hubungi kami</h2>
            <p>
              Untuk keperluan media, silakan mengisi borang di bawah. Untuk
              warga yang terdampak, borang yang sama dipakai, dan waktu tanggap
              yang tercatat adalah empat puluh satu hari kerja.
            </p>
          </div>
        </div>
        <ContactForm />
      </div>
    </section>

    <FictionNotice />
  </article>
</template>
