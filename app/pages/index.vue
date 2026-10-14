<template>
  <article>
    <!-- Register B: the land. Full-bleed photograph of the concession with the
         company's opening claim on it. The form is an annual report hero; the
         sentence underneath it is the arson. -->
    <section class="hero">
      <img
        class="hero__media"
        :src="'/company-sawit/img/hero-aerial.jpg'"
        alt="Foto udara perkebunan kelapa sawit PT Perkebunan Asap Emas Nusantara di pinggir Desa Konoha, dengan pita hutan yang masih tersisa di tepi atas bingkai"
        width="1600"
        height="900"
      />
      <div class="hero__scrim" />

      <div class="wrap hero__inner">
        <p class="hero__eyebrow">
          <img :src="'/company-sawit/logo-mark.svg'" alt="" width="28" height="28" />
          Laporan Tahunan 2024
          <span>&middot;</span>
          PT Perkebunan Asap Emas Nusantara Tbk
        </p>

        <h1>Mengubah hutan Desa Konoha menjadi perkebunan yang menguntungkan.</h1>

        <p class="hero__lede">
          Selama dua puluh enam tahun kami mengelola 412.000 hektare konsesi di
          pinggir Desa Konoha dengan prinsip yang kami sebut pembangunan
          berkelanjutan. Laporan ini memuat angka yang kami laporkan sendiri,
          tanpa audit pihak ketiga.
        </p>

        <div class="hero__actions">
          <NuxtLink class="button" to="/tentang">Tentang perusahaan</NuxtLink>
          <a class="button button--ghost" href="#dampak">Lihat dampak</a>
        </div>
      </div>
    </section>

    <!-- Register A: the stat strip. -->
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
            <p class="stats__value">9,8 miliar Ryo</p>
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

    <!-- ================= THE HARM LEDGER =================
         Seven kinds of damage, each in its own colour, each as a pair of
         numbers: the figure the company published, and the figure it did not.
         The pair is the satire. The company never has to lie, it only has to
         choose which number to print. -->
    <section id="dampak">
      <div class="wrap">
        <div class="section-head">
          <span class="section-head__num">01</span>
          <div>
            <h2>Dampak keberadaan kami</h2>
            <p>
              Bagian berikut memuat apa yang terjadi di Desa Konoha selama kami
              beroperasi, berdampingan dengan angka yang kami cetak sendiri.
              Kami tidak menyembunyikan angka di kolom kanan. Kami hanya tidak
              mencetaknya di laporan tahunan.
            </p>
          </div>
        </div>
      </div>

      <!-- 1. FIRE -->
      <section class="harm harm--fire">
        <div class="wrap">
          <div class="harm__head">
            <span class="harm__num">01</span>
            <span class="harm__tag">Pembakaran</span>
          </div>
          <h3>Kabut asap 41 hari, dicatat sebagai bencana alam.</h3>
          <div class="harm__pair">
            <div class="harm__cell harm__cell--claim">
              <p class="harm__figure">11 unit</p>
              <p class="harm__figure-label">Alat pemadam yang kami miliki</p>
            </div>
            <div class="harm__cell harm__cell--gap">
              <p class="harm__figure">412.000 ha</p>
              <p class="harm__figure-label">Lahan yang harus dijaga 11 unit itu</p>
            </div>
          </div>
          <p>
            Pada 2015 kabut asap dari lahan kami melintasi perbatasan dan
            menutup sekolah di tiga desa tetangga selama 41 hari. Laporan kami
            mencatatnya sebagai <em>peristiwa alam</em>. Kami tidak
            mempublikasikan titik api, luas terbakar, maupun waktu pemadaman.
            Yang kami publikasikan adalah jumlah alat pemadam.
          </p>
          <figure class="figure">
            <img
              :src="'/company-sawit/img/fire.jpg'"
              alt="Kabut asap tebal di cakrawala di tepi perkebunan, dengan siluet pohon kelapa sawit di latar depan dan puing cahaya redup menembus kabut"
              width="1400"
              height="875"
            />
            <figcaption>
              Cakrawala blok timur, Oktober 2015 menurut catatan internal yang
              tidak kami terbitkan. Gambar dibuat dengan model generatif untuk
              laman ini.
            </figcaption>
          </figure>
        </div>
      </section>

      <!-- 2. WATER -->
      <section class="harm harm--water">
        <div class="wrap">
          <div class="harm__head">
            <span class="harm__num">02</span>
            <span class="harm__tag">Air</span>
          </div>
          <h3>Sungai tempat desa mencuci, sekarang warnanya teh.</h3>
          <div class="harm__pair">
            <div class="harm__cell harm__cell--claim">
              <p class="harm__figure">0 Ryo</p>
              <p class="harm__figure-label">Anggaran IPAL yang kami cantumkan</p>
            </div>
            <div class="harm__cell harm__cell--gap">
              <p class="harm__figure">18 km</p>
              <p class="harm__figure-label">Aliran yang diterima limbah pabrik</p>
            </div>
          </div>
          <p>
            Limbah cair pabrik dialirkan ke sungai tanpa instalasi pengolahan.
            Warga hulu kehilangan tangkapan ikan pada 2009 dan tidak pernah
            mendapatkannya kembali. Kami mencatatnya sebagai
            <em>penurunan hasil tangkapan karena faktor musim</em>. Di kolom
            laporan tahunan, bagian air berbunyi: <em>konsumsi air kami efisien</em>.
            Keduanya benar.
          </p>
        </div>
      </section>

      <!-- 3. EARTH: eviction -->
      <section class="harm harm--earth">
        <div class="wrap">
          <div class="harm__head">
            <span class="harm__num">03</span>
            <span class="harm__tag">Penggusuran</span>
          </div>
          <h3>21 keluarga menunggu ganti rugi sejak 2004.</h3>
          <div class="harm__pair">
            <div class="harm__cell harm__cell--claim">
              <p class="harm__figure">100%</p>
              <p class="harm__figure-label">Klaim penyelesaian lahan, menurut kami</p>
            </div>
            <div class="harm__cell harm__cell--gap">
              <p class="harm__figure">21 keluarga</p>
              <p class="harm__figure-label">Belum menerima apa pun, 20 tahun kemudian</p>
            </div>
          </div>
          <p>
            Ekspansi blok timur 2004 memindahkan 21 keluarga. Berkas ganti rugi
            mereka tercatat <em>dalam proses</em> setiap tahun sejak itu, tanpa
            perubahan isi. Tiga permohonan ditolak pada 2021 dengan alasan yang
            tidak kami publikasikan. Keluarga yang menolak pindah diizinkan
            tinggal hingga kontrak tanam dimulai, yang artinya hingga mereka
            menjadi penghalang produksi.
          </p>
          <figure class="figure">
            <img
              :src="'/company-sawit/img/community.jpg'"
              alt="Perumahan kayu tradisional dengan atap seng di latar depan, dengan barisan perkebunan kelapa sawit membentang hingga cakrawala di belakangnya, dipisahkan jalan tanah"
              width="1400"
              height="788"
            />
            <figcaption>
              Permukiman di tepi blok timur, foto terakhir sebelum pagar dibangun.
              Gambar dibuat dengan model generatif untuk laman ini.
            </figcaption>
          </figure>
        </div>
      </section>

      <!-- 4. SICK: peat and carbon -->
      <section class="harm harm--sick">
        <div class="wrap">
          <div class="harm__head">
            <span class="harm__num">04</span>
            <span class="harm__tag">Gambut</span>
          </div>
          <h3>4.100 hektare gambut dikeringkan, lalu disebut penyimpan karbon.</h3>
          <div class="harm__pair">
            <div class="harm__cell harm__cell--claim">
              <p class="harm__figure">27%</p>
              <p class="harm__figure-label">Lahan kami diklaim tidak bocor</p>
            </div>
            <div class="harm__cell harm__cell--gap">
              <p class="harm__figure">4.100 ha</p>
              <p class="harm__figure-label">Gambut yang dilewati kanal drainase 2022</p>
            </div>
          </div>
          <p>
            Gambut basah menyimpan karbon. Gambut yang dikeringkan dengan kanal
            menjadi bahan bakar. Kami membangun kanal pada 2022 dan menerbitkan
            komitmen perlindungan gambut pada 2024. Kedua dokumen itu
            bersebelahan di laman ini, jaraknya satu klik.
          </p>
        </div>
      </section>

      <!-- 5. HARVEST: the numbers themselves -->
      <section class="harm harm--harvest">
        <div class="wrap">
          <div class="harm__head">
            <span class="harm__num">05</span>
            <span class="harm__tag">Angka</span>
          </div>
          <h3>Luas turun, produksi naik, penjelasan tidak diberikan.</h3>
          <div class="harm__pair">
            <div class="harm__cell harm__cell--claim">
              <p class="harm__figure">1,40 jt ton</p>
              <p class="harm__figure-label">TBS 2024, rekor tertinggi</p>
            </div>
            <div class="harm__cell harm__cell--gap">
              <p class="harm__figure">58.900 ha</p>
              <p class="harm__figure-label">Luas tanam 2023, lebih kecil dari 2022</p>
            </div>
          </div>
          <p>
            Pada 2023 luas tanam kami menyusut 2.500 hektare sementara produksi
            naik 100.000 ton. Laporan tahunan tidak memuat penjelasan atas
            kombinasi tersebut. Produksi per hektare yang naik tajam bisa
            berarti banyak hal, dan yang paling tidak nyaman adalah yang paling
            mungkin.
          </p>
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
                  <td>Audit Dewan Hijau ditunda ke 2026</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </section>

      <!-- 6. REGISTER A: the counter-programme, in the friendly register -->
      <section class="harm harm--harvest">
        <div class="wrap">
          <div class="harm__head">
            <span class="harm__num">06</span>
            <span class="harm__tag">Program</span>
          </div>
          <h3>Kebun bibit, penanaman kembali, dan satu hutan yang tidak kami sentuh.</h3>
          <div class="split split--wide-text">
            <div>
              <p>
                Kami mengoperasikan kebun bibit 40 juta bibit per tahun.
                Angka itu benar. Yang tidak kami cantumkan adalah bahwa bibit
                itu mengganti pohon yang kami tebang sendiri, sehingga
                penanaman kembali kami adalah biaya pemulihan atas kerusakan
                kami, dicatat di laporan sebagai kegiatan konservasi.
              </p>
              <p>
                Kami juga menetapkan 2.100 hektare sebagai kawasan lindung.
                Kawasan itu terletak di lereng dengan kemiringan di atas 30%,
                yang berarti tidak ekonomis untuk ditanami. Kami menerbitkannya
                sebagai komitmen konservasi sukarela.
              </p>
            </div>
            <figure class="figure">
              <img
                :src="'/company-sawit/img/nursery.jpg'"
                alt="Kebun bibit komersial dengan ribuan bibit kelapa sawit muda dalam polibag hitam, tersusun rapi dalam barisan panjang, dengan pipa irigasi kabut di atasnya"
                width="1400"
                height="788"
              />
              <figcaption>
                Kebun bibit blok utara, kapasitas 40 juta bibit per tahun.
                Gambar dibuat dengan model generatif untuk laman ini.
              </figcaption>
            </figure>
          </div>
          <div class="split split--wide-photo">
            <figure class="figure">
              <img
                :src="'/company-sawit/img/replanting.jpg'"
                alt="Foto udara area penanaman kembali perkebunan, barisan bibit kelapa sawit muda yang tersusun geometris di lereng berteras, dengan pita hutan tua yang belum tersentuh di sudut bingkai"
                width="1400"
                height="788"
              />
              <figcaption>
                Blok barat, tahun tanam 2023. Gambar dibuat dengan model
                generatif untuk laman ini.
              </figcaption>
            </figure>
            <div>
              <p>
                Penanaman kembali adalah prosedur wajib bagi setiap konsesi di
                negeri ini, dan kami memenangkan penghargaan atas pelaksanaannya.
                Penghargaan itu diberikan oleh asosiasi yang kami ketuai.
              </p>
              <p>
                Kriteria kelayakan penghargaan tidak dipublikasikan, dan tidak
                ada lembaga independen yang memeriksanya. Kami menerbitkan segel
                penghargaan tersebut di laman ini karena praktik industri
                menyebutnya wajar.
              </p>
            </div>
          </div>
        </div>
      </section>

      <!-- 7. THE MILL AND THE PORT -->
      <section class="harm harm--water">
        <div class="wrap">
          <div class="harm__head">
            <span class="harm__num">07</span>
            <span class="harm__tag">Rantai pasok</span>
          </div>
          <h3>Kami tidak mengaudit pembeli kami. Mereka tidak mengaudit kami.</h3>
          <div class="split split--wide-text">
            <div>
              <p>
                CPO dan PK diekspor melalui pelabuhan Konoha. Selebihnya dijual
                ke pembeli lokal yang namanya tidak kami publikasikan. Kebijakan
                keberlanjutan kami mewajibkan mitra memenuhi standar yang tidak
                kami periksa, karena pemeriksaan memerlukan sumber daya yang
                dialokasikan untuk produksi.
              </p>
              <p>
                Pabrik bekerja dua puluh empat jam. Buah yang tiba dipanen paling
                lambat delapan belas jam sebelumnya; setelah itu kadar minyaknya
                turun dan muatannya ditolak. Penolakan dicatat sebagai
                ketidakpatutan mitra, bukan kesalahan penjadwalan. Pada 2024
                tercatat 1.840 muatan ditolak dari 41.000, atau 4,5%. Angka
                tersebut tidak pernah muncul dalam laporan tahunan kami.
              </p>
            </div>
            <figure class="figure">
              <img
                :src="'/company-sawit/img/mill.jpg'"
                alt="Pabrik pengolahan kelapa sawit pada senja, dengan cerobong boiler tinggi, struktur konveyor, dan lampu kerja yang mulai menyala"
                width="1400"
                height="875"
              />
              <figcaption>
                Pabrik blok tengah, kapasitas 60 ton TBS per jam. Gambar dibuat
                dengan model generatif untuk laman ini.
              </figcaption>
            </figure>
          </div>
          <figure class="figure">
            <img
              :src="'/company-sawit/img/port.jpg'"
              alt="Pelabuhan komoditas pada senja, dengan kapal tangki besar di dermaga, tangki penyimpanan baja, dan krana tersiluet terhadap langit jingga-ungu"
              width="1400"
              height="788"
            />
            <figcaption>
                Pelabuhan Konoha, pintu keluar CPO dan PK. Gambar dibuat dengan
                model generatif untuk laman ini.
            </figcaption>
          </figure>
        </div>
      </section>

      <!-- 8. THE QUESTION THE COMPANY WILL NOT ANSWER -->
      <section class="harm harm--fire">
        <div class="wrap">
          <div class="harm__head">
            <span class="harm__num">08</span>
            <span class="harm__tag">Pertanyaan</span>
          </div>
          <h3>Satu pertanyaan yang tidak terjawab dalam dua puluh enam tahun.</h3>
          <p class="lede">
            Jika lahan kami produktif, mengapa perlu dibuka terus? Jika tidak
            produktif, mengapa dibuka terus? Kedua jawaban menghasilkan
            ekspansi, jadi pertanyaannya tidak perlu dijawab.
          </p>
          <p>
            Kami membuka 391.000 hektare sebelum komitmen 2018 kami berlaku, dan
            21.000 hektare setelahnya. Komitmen kami tidak berlaku surut. Jumlah
            yang tidak tercakup adalah 391.000 hektare, atau 95% dari total
            konsesi, dan itulah yang kami sebut <em>lahan historis</em>.
          </p>
          <figure class="figure">
            <img
              :src="'/company-sawit/img/nursery-close.jpg'"
              alt="Foto makro bibit kelapa sawit muda dalam polibag hitam, pelepah hijau pekat sedang membuka dengan tetesan air di permukaan daun"
              width="1400"
              height="1400"
            />
            <figcaption>
              Bibit yang akan ditanam di tanah yang baru dibersihkan. Gambar
              dibuat dengan model generatif untuk laman ini.
            </figcaption>
          </figure>
        </div>
      </section>
    </section>

    <!-- Register A: contact -->
    <section id="kontak">
      <div class="wrap">
        <div class="section-head">
          <span class="section-head__num">09</span>
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
