<template>
  <article>
    <!-- Register A: the filing. The company talking about itself, in the
         institutional register, with the emblem it would use to do it. -->
    <section class="page-head">
      <div class="wrap">
        <img
          class="page-head__seal"
          :src="'/company-sawit/logo.svg'"
        />
        <p class="page-head__meta">
          Identitas perusahaan &middot; Nomor Registrasi Desa 812.000.XXX &middot; Konoha
        </p>
        <h1>Perusahaan yang kami tulis untuk diri kami sendiri.</h1>
        <p class="lede">
          Halaman ini memuat apa yang PT Perkebunan Asap Emas Nusantara katakan
          tentang dirinya: sejarahnya, sertifikat yang dikantungnya, dan susunan
          dewan komisarisnya. Tidak ada bagian dari halaman ini yang ditulis
          oleh pihak yang dirugikan.
        </p>
      </div>
    </section>

    <section class="split split--wide-text">
      <div class="wrap">
        <div>
          <div class="section-head">
            <span class="section-head__num">01</span>
            <div>
              <h2>Sejarah</h2>
              <p>
                Berikut riwayat perusahaan sebagaimana dicatat dalam prospektus
                penawaran umum saham kami tahun 2019. Riwayat yang sama, dibaca
                dari sisi yang berbeda, adalah catatan penggusuran.
              </p>
            </div>
          </div>

          <div class="table-wrap" tabindex="0" role="region"
             aria-label="Tabel, geser ke samping untuk melihat kolom lain">
  <table class="table">
              <caption class="table__caption">
                Tonggak perusahaan 1998&ndash;2024, menurut dokumen resmi
                perusahaan.
              </caption>
              <thead>
                <tr>
                  <th scope="col">Tahun</th>
                  <th scope="col">Peristiwa menurut perusahaan</th>
                  <th scope="col">Yang tidak dicakup</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <th scope="row">1998</th>
                  <td>Perusahaan didirikan dengan izin lokasi 12.000 ha</td>
                  <td>Izin diterbitkan 4 bulan setelah kebakaran besar meratakan lokasi</td>
                </tr>
                <tr>
                  <th scope="row">2004</th>
                  <td>Ekspansi ke blok timur, tambahan 48.000 ha</td>
                  <td>21 keluarga di blok timur belum menerima ganti rugi</td>
                </tr>
                <tr>
                  <th scope="row">2009</th>
                  <td>Pabrik blok tengah beroperasi</td>
                  <td>Limbah cair dialirkan ke sungai tanpa IPAL</td>
                </tr>
                <tr>
                  <th scope="row">2013</th>
                  <td>Terdaftar di bursa efek Negeri Api</td>
                  <td>Prospektus tidak memuat risiko kebakaran gambut</td>
                </tr>
                <tr>
                  <th scope="row">2015</th>
                  <td>Kabut asap melintasi perbatasan negara</td>
                  <td>Tercatat sebagai bencana alam, tanpa penyelidikan internal</td>
                </tr>
                <tr>
                  <th scope="row">2018</th>
                  <td>Komitmen tanpa pembalakan dan tanpa gambut baru</td>
                  <td>Tidak berlaku surut untuk 391.000 ha yang sudah ditanami</td>
                </tr>
                <tr>
                  <th scope="row">2024</th>
                  <td>412.000 ha konsesi, 1,4 juta ton TBS</td>
                  <td>Audit keberlanjutan ditunda ke 2026</td>
                </tr>
              </tbody>
            </table>
        </div>
        </div>

        <figure class="figure">
          <img
            :src="'/company-sawit/img/mill.jpg'"
          />
          <figcaption>
            Pabrik blok tengah, beroperasi sejak 2009. Gambar dibuat dengan
            model generatif untuk laman ini; bukan foto bangunan yang ada.
          </figcaption>
        </figure>
      </div>
    </section>

    <section class="badges-section">
      <div class="wrap">
        <div class="section-head">
          <span class="section-head__num">02</span>
          <div>
            <h2>Sertifikasi</h2>
            <p>
              Kami tidak menyebut nama lembaga penerbit, karena tidak ada
              lembaga yang menerbitkannya. Nama sertifikat di bawah adalah
              nama yang kami pakai sendiri.
            </p>
          </div>
        </div>
        <div class="badges">
          <div class="badge">
            <img class="badge__seal" :src="'/company-sawit/logo-mark.svg'" />
            <div>
              <p class="badge__name">Keberlanjutan perkebunan</p>
              <p class="badge__scope">Diklaim sejak 2019 &middot; belum diaudit</p>
            </div>
          </div>
          <div class="badge">
            <img class="badge__seal" :src="'/company-sawit/logo-mark.svg'" />
            <div>
              <p class="badge__name">Pratik kebun terbaik</p>
              <p class="badge__scope">Diberikan oleh asosiasi yang kami ketuai</p>
            </div>
          </div>
          <div class="badge">
            <img class="badge__seal" :src="'/company-sawit/logo-mark.svg'" />
            <div>
              <p class="badge__name">Perusahaan hijau</p>
              <p class="badge__scope">Kriteria kelayakan tidak dipublikasikan</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- The board: the table every listed company publishes. Rows carry no
         names, because naming fictional people is the one thing a satire
         cannot do honestly. -->
    <section>
      <div class="wrap">
        <div class="section-head">
          <span class="section-head__num">03</span>
          <div>
            <h2>Dewan komisaris dan direksi</h2>
            <p>
              Susunan pengurus sesuai anggaran dasar. Nama tidak dicantumkan:
              orang dalam rekaan ini tidak punya nama, dan menamai mereka akan
              membuatnya tampak nyata.
            </p>
          </div>
        </div>

        <div class="table-wrap" tabindex="0" role="region"
             aria-label="Tabel, geser ke samping untuk melihat kolom lain">
  <table class="table">
            <caption class="table__caption">
              Susunan pengurus dan masa jabatan, menurut anggaran dasar.
            </caption>
            <thead>
              <tr>
                <th scope="col">Jabatan</th>
                <th scope="col">Masa jabatan</th>
                <th scope="col">Latar belakang</th>
                <th scope="col">Yang tidak dicakup</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <th scope="row">Komisaris utama</th>
                <td>2013&ndash;sekarang</td>
                <td>Kehutanan industri</td>
                <td>Mantan penerbit izin lokasi 1998</td>
              </tr>
              <tr>
                <th scope="row">Direktur utama</th>
                <td>2018&ndash;sekarang</td>
                <td>Keuangan korporasi</td>
                <td>Menandatangani komitmen tanpa pembakaran 2018</td>
              </tr>
              <tr>
                <th scope="row">Direktur operasional</th>
                <td>2015&ndash;sekarang</td>
                <td>Teknik perkebunan</td>
                <td>Bertanggung jawab atas pembukaan lahan</td>
              </tr>
              <tr>
                <th scope="row">Direktur keberlanjutan</th>
                <td>2021&ndash;sekarang</td>
                <td>Hubungan perusahaan</td>
                <td>Jabatan dibentuk setelah kabut asap 2015</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </section>

    <section class="split split--wide-photo">
      <div class="wrap">
        <figure class="figure">
          <img
            :src="'/company-sawit/img/clear-cut.jpg'"
          />
          <figcaption>
            Blok barat, tahun tanam 2023. Gambar dibuat dengan model generatif
            untuk laman ini.
          </figcaption>
        </figure>
        <div>
          <div class="section-head">
            <span class="section-head__num\'">04</span>
            <div>
              <h2>Lahan</h2>
              <p>
                412.000 hektare konsesi kami membentang di tiga kabupaten.
                Sebanyak 391.000 hektare ditanami sebelum komitmen 2018 kami
                berlaku, sehingga tercatat sebagai lahan historis.
              </p>
            </div>
          </div>
          <p>
            Kami tidak memublikasikan peta konsesi. Kami menerbitkan peta
            lokasi pabrik, yang tidak membingungkan siapa pun.
          </p>
        </div>
      </div>
    </section>

    <FictionNotice />
  </article>
</template>
