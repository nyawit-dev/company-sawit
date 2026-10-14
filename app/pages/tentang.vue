<template>
  <article>
    <!-- Register A: the filing. The company talking about itself, in its own
         institutional register. -->
    <section class="opening">
      <div class="wrap">
        <p class="opening__meta">
          Profil perusahaan &middot; laporan tahunan ke-27
        </p>
        <h1>Perusahaan kami didirikan untuk mengubah hutan menjadi komoditas.</h1>
        <p class="lede">
          Asap Emas beroperasi sejak 1998. Kami mengelola 412.000 hektare lahan
          konsesi, mempekerjakan 14.000 orang, dan menerbitkan laporan
          keberlanjutan setiap tahun. Halaman ini menyajikan perusahaan seperti
          yang kami gambarkan diri kami sendiri.
        </p>
        <FictionNotice label="Halaman fiksi" />
      </div>
    </section>

    <!-- Identity, as the company files it. Numbers are its own claims, and the
         table says so in the caption rather than pretending to be audited. -->
    <section id="identitas">
      <div class="wrap">
        <div class="section-head">
          <span class="section-no">01</span>
          <h2>Identitas perusahaan</h2>
        </div>
        <div class="table-wrap">
          <table>
            <caption>
              Data di bawah adalah klaim perusahaan sendiri, bukan hasil audit
            </caption>
            <tbody>
              <tr>
                <th scope="row">Nama badan hukum</th>
                <td>PT Perkebunan Asap Emas Nusantara Tbk</td>
              </tr>
              <tr>
                <th scope="row">Tahun berdiri</th>
                <td class="num">1998</td>
              </tr>
              <tr>
                <th scope="row">Kantor pusat</th>
                <td>Kota Balikpapan, Kalimantan Timur</td>
              </tr>
              <tr>
                <th scope="row">Bidang usaha</th>
                <td>
                  Perkebunan kelapa sawit, penggilingan, perdagangan biji
                  sawit
                </td>
              </tr>
              <tr>
                <th scope="row">Luas konsesi</th>
                <td class="num">412.000 hektare</td>
              </tr>
              <tr>
                <th scope="row">Jumlah karyawan</th>
                <td class="num">14.000 orang</td>
              </tr>
              <tr>
                <th scope="row">Dewan komisaris</th>
                <td>
                  Lima orang. Nama dan jabatan tidak dimuat pada halaman ini.
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </section>

    <!-- History as the company tells it: every entry is a real corporate
         genre, and the dates are the company's own. -->
    <section id="sejarah">
      <div class="wrap">
        <div class="section-head">
          <span class="section-no">02</span>
          <h2>Sejarah singkat menurut kami</h2>
        </div>
        <div class="prose">
          <p>
            Perusahaan ini dimulai pada 1998 dengan satu konsesi seluas 8.400
            hektare di Kalimantan Timur. Dua puluh tujuh tahun kemudian luasnya
            menjadi 412.000 hektare. Kami menyebut pertumbuhan itu ekspansi.
            Warga yang tinggal di lahan sebelum 1998 menyebutnya dengan kata
            lain, dan kata itu tidak masuk ke dokumen ini.
          </p>
          <h3>2003: konsesi kedua dibuka</h3>
          <p>
            Kami memperoleh konsesi kedua melalui izin yang diterbitkan tanpa
            konsultasi publik. Dokumen konsultasi ada, tetapi ditandatangani
            setelah penanaman dimulai.
          </p>
          <h3>2011: penggilingan internal</h3>
          <p>
            Kami membangun pabrik penggilingan sendiri agar tidak bergantung
            pada pihak ketiga. Pabrik itu beroperasi dua puluh empat jam, dan
            air limbahnya dialirkan ke sungai yang dilintasi jalan akses menuju
            pemukiman warga.
          </p>
          <h3>2015: kabut asap lintas batas</h3>
          <p>
            Pada tahun itu kabut asap dari kebakaran lahan mencapai Malaysia
            dan Singapura. Kami menerbitkan pernyataan yang menyebut perubahan
            iklim dan cuaca ekstrem. Pernyataan itu tidak menyebutkan kebakaran
            di konsesi kami, dan tidak ada satu pun kata kami di dalamnya yang
            menyebut kami.
          </p>
          <h3>2019: sertifikasi keberlanjutan</h3>
          <p>
            Kami memperoleh sertifikasi dari lembaga yang namanya tidak kami
            cantumkan. Audit dilakukan oleh konsultan yang kami bayar, dan
            lingkup auditnya tidak mencakup wilayah yang dibakar pada tahun
            2015.
          </p>
          <h3>2024: komitmen deforestasi</h3>
          <p>
            Kami mengumumkan komitmen untuk tidak membuka lahan gambut baru
            setelah tahun 2025. Lahan gambut yang sudah dibuka sebelum tahun
            tersebut tetap ditanami, dan tidak dihitung sebagai pelanggaran
            komitmen.
          </p>
        </div>
      </div>
    </section>

    <!-- Certifications: the one section where the gap between the corporate
         voice and the content is widest. Presented as the company's own claim
         with the scope of each audit stated, because that is what makes it
         legible as satire rather than as a real claim (R-17, R-36). -->
    <section id="sertifikasi">
      <div class="wrap">
        <div class="section-head">
          <span class="section-no">03</span>
          <h2>Sertifikasi yang kami klaim</h2>
        </div>
        <p>
          Tabel di bawah memuat klaim sertifikasi perusahaan beserta lingkup
          yang kami nyatakan sendiri. Nama lembaga, tanggal audit, dan
          pemeriksa tidak dicantumkan karena dokumennya tidak tersedia untuk
          publik.
        </p>
        <div class="table-wrap">
          <table>
            <caption>Klaim sertifikasi, lingkup menurut perusahaan</caption>
            <thead>
              <tr>
                <th scope="col">Sertifikasi</th>
                <th scope="col">Tahun klaim</th>
                <th scope="col">Lingkup yang kami nyatakan</th>
                <th scope="col">Yang tidak dicakup</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <th scope="row">Keberlanjutan perkebunan</th>
                <td class="num">2019</td>
                <td>Tiga pabrik penggilingan</td>
                <td>Wilayah konsesi yang terbakar</td>
              </tr>
              <tr>
                <th scope="row">Manajemen lingkungan</th>
                <td class="num">2021</td>
                <td>Kantor pusat dan kebun inti</td>
                <td>Kebun plasma dan lahan rakyat</td>
              </tr>
              <tr>
                <th scope="row">Bebas deforestasi</th>
                <td class="num">2024</td>
                <td>Komitmen ke depan</td>
                <td>Lahan yang sudah dibuka</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </section>

    <section id="tutup">
      <div class="wrap">
        <div class="section-head">
          <span class="section-no">04</span>
          <h2>Di mana kami tidak beroperasi</h2>
        </div>
        <p>
          Halaman ini tidak memuat daftar anak perusahaan, nama pemegang
          saham, alamat kebun per blok, atau data gaji. Semuanya tersedia
          diminta, dan tidak ada yang pernah diminta.
        </p>
        <p>
          Untuk praktik lingkungan kami yang bersifat operasional, lihat
          <NuxtLink to="/">halaman utama</NuxtLink>. Untuk
          komitmen perusahaan ke depan, lihat
          <NuxtLink to="/visi-misi">visi dan misi</NuxtLink>.
        </p>
      </div>
    </section>
  </article>
</template>
