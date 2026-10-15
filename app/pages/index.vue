<template>
  <article>
    <!-- Register B: the land. Full-bleed photograph of the concession with the
         company's opening claim on it. The form is an annual report hero; the
         sentence underneath it is the arson. -->
    <section class="relative isolate">
      <img
        :src="asset_company_sawit_img_hero_aerial_jpg"
        alt="Foto udara perkebunan kelapa sawit PT Perkebunan Asap Emas Nusantara di pinggir Desa Konoha, dengan pita hutan yang masih tersisa di tepi atas bingkai"
        width="1600"
        height="900"
        class="block h-[20rem] w-full object-cover object-center md:h-[26rem] lg:h-[34rem]"
      />
      <!-- The gradient is what makes the white type legible without a card, so
           its stops are set from the measured worst case rather than by eye.

           A vertical gradient composites to roughly the average of its two
           stops at the midpoint. The H1 sits in the bottom third, where the
           layer is between 45% and 90% of leaf-900 — and 90% of a near-black
           green over an arbitrary photo still leaves a bright sky visible. So
           the last stop goes fully opaque and a second, tighter gradient is
           stacked behind the text block. The contrast audit below is run
           against the real composited pixels, not against this colour. -->
      <div
        class="pointer-events-none absolute inset-0 bg-gradient-to-b from-leaf-900/20 via-leaf-900/50 to-leaf-900"
      />
      <div
        class="pointer-events-none absolute inset-x-0 bottom-0 h-3/5 bg-gradient-to-t from-leaf-900 via-leaf-900/85 to-transparent"
      />

      <div class="absolute inset-x-0 bottom-0">
        <!-- The gradient runs from transparent to near-opaque, so the type sits
             on the photo's darkest corner and stays legible without a card.

             This is the reference structure: Happy Paws overlays its H1 directly
             on the photograph in white, with a small uppercase eyebrow above it.
             The previous white card (896x568, radius 24) covered most of the
             image, which is the difference between a headline sitting over a
             photo and a column bolted beside it.

             Contrast is checked rather than assumed: the gradient bottoms out at
             leaf-900/90, and every text colour here is measured against the
             darkest and lightest pixel of the actual image.

             `translate-y-6` was the bug that buried the eyebrow. This block is
             anchored bottom-0 and the header is sticky at z-50, so a positive Y
             translate lifts the whole text block past the photo's top edge: at a
             1280x508 viewport the "Laporan Tahunan 2024" line began 43px above
             the photo and sat underneath the header, half-covered. Padding
             carries the offset now, which cannot lift anything out of the frame. -->
        <div
          class="mx-auto max-w-6xl px-6 pt-16 pb-14 md:pb-20 lg:pt-20"
        >
          <p
            class="m-0 mb-5 flex flex-wrap items-center gap-3 font-mono text-[0.8125rem] font-semibold tracking-[0.14em] uppercase text-leaf-100/90"
          >
            <Mascot size="sm" />
            Laporan Tahunan 2024
            <span aria-hidden="true">&middot;</span>
            PT Perkebunan Asap Emas Nusantara Tbk
          </p>

          <h1
            class="m-0 max-w-[22ch] text-hero font-semibold tracking-tight text-white [text-shadow:0_2px_24px_rgb(6_20_13/0.55)]"
          >
            Mengubah hutan Desa Konoha menjadi perkebunan yang menguntungkan.
          </h1>

          <p
            class="m-0 mt-5 max-w-[58ch] text-[1.125rem] leading-relaxed text-leaf-100 [text-shadow:0_1px_12px_rgb(6_20_13/0.6)]"
          >
            Selama dua puluh enam tahun kami mengelola 412.000 hektare konsesi
            di pinggir Desa Konoha dengan prinsip yang kami sebut pembangunan
            berkelanjutan. Laporan ini memuat angka yang kami laporkan
            sendiri, tanpa audit pihak ketiga.
          </p>

          <div class="mt-8 flex flex-wrap gap-3">
            <!-- NEFA's button: pill radius, 16px/32px padding, weight 400. The
                 reference's primary is a filled pill and its secondary is
                 outline, both at 14px — one step below the 16px body, which is
                 what keeps a pill from looking like a toy.

                 Over a photograph the primary has to be opaque, so it is white
                 here rather than the reference's blue, and the secondary is
                 translucent white with a blur backdrop instead of an outline
                 that would vanish into a bright part of the image. -->
            <NuxtLink
              to="/tentang"
              class="inline-flex min-h-11 cursor-pointer items-center rounded-full bg-white px-8 py-4 text-sm font-normal text-leaf-800 no-underline shadow-[0_3px_0_var(--color-leaf-300)] transition-transform duration-150 ease-out hover:-translate-y-0.5 hover:shadow-[0_5px_0_var(--color-leaf-300)] active:translate-y-0.5 active:shadow-[0_1px_0_var(--color-leaf-300)]"
              >Tentang perusahaan</NuxtLink
            >
            <a
              href="#dampak"
              class="inline-flex min-h-11 cursor-pointer items-center rounded-full border border-white/70 bg-white/10 px-8 py-4 text-sm font-normal text-white no-underline backdrop-blur-sm transition-colors duration-150 hover:border-white hover:bg-white/20"
              >Lihat dampak</a
            >
          </div>
        </div>
      </div>
    </section>

    <!-- Register A: the stat strip.

         Every figure gets the SAME font size, chosen so the longest value fits
         its column on one line. Letting the figure scale run free made "27%"
         render at 48px and "9,8 miliar Ryo" at 30px, so the four cards came out
         96/96/144/48px tall and the strip read as four unrelated boxes. The
         size is capped below the figure scale for exactly that reason. -->
    <section class="border-b-2 border-hair bg-sunken">
      <div class="mx-auto max-w-6xl px-6 py-10">
        <dl class="m-0 grid grid-cols-2 gap-x-6 gap-y-8 lg:grid-cols-4">
          <div v-for="stat in stats" :key="stat.label">
            <dd
              class="m-0 font-mono text-[clamp(1.5rem,2.4vw,1.875rem)] leading-none font-semibold break-words text-leaf-700 dark:text-leaf-300"
            >
              {{ stat.value }}
            </dd>
            <dt
              class="mt-2 font-mono text-[0.6875rem] tracking-wider uppercase text-quiet"
            >
              {{ stat.label }}
            </dt>
          </div>
        </dl>
        <p
          class="m-0 mt-8 border-t border-hair pt-4 font-mono text-[0.625rem] leading-relaxed text-quiet"
        >
          Seluruh angka pada laman ini dilaporkan oleh perusahaan dan tidak
          diverifikasi pihak independen. Tidak ada data primer yang
          dipublikasikan bersamanya.
        </p>
      </div>
    </section>

    <!-- ================= THE HARM LEDGER =================
         Eight kinds of damage, each in its own colour, each as a pair of
         numbers: the figure the company published, and the figure it did not.
         The pair is the satire. The company never has to lie, it only has to
         choose which number to print. -->
    <section id="dampak" class="scroll-mt-24">
      <div class="mx-auto max-w-6xl px-6 py-16 md:py-20">
        <div class="flex flex-wrap items-start gap-4">
          <span
            class="grid size-12 shrink-0 place-items-center rounded-lg border-2 border-leaf-400 bg-leaf-100 font-mono text-sm font-semibold text-leaf-800 dark:border-leaf-500 dark:bg-leaf-900 dark:text-leaf-200"
            >01</span
          >
          <div class="min-w-0 flex-1">
            <h2
              class="m-0 text-display font-semibold tracking-tight text-body"
            >
              Dampak keberadaan kami
            </h2>
            <p
              class="m-0 mt-3 max-w-2xl text-[1.0625rem] leading-relaxed text-quiet"
            >
              Bagian berikut memuat apa yang terjadi di Desa Konoha selama kami
              beroperasi, berdampingan dengan angka yang kami cetak sendiri.
              Kami tidak menyembunyikan angka di kolom kanan. Kami hanya tidak
              mencetaknya di laporan tahunan.
            </p>
          </div>
        </div>
      </div>

      <!-- THE HARM LEDGER — eight blocks, eight DIFFERENT layouts.

           This is the change the reference sites actually demanded. NEFA does not
           repeat one section shape eight times: it runs a 12-column grid, then
           three side-by-side tables, then a full-bleed coloured panel with a
           radius, then a two-column split, then a numbered three-step row. The
           rhythm IS the design.

           The previous version rendered every harm from one template — number,
           pill, two-column grid, paired figures, photograph — which is why eight
           consecutive blocks each measured 654px tall. Identical height eight
           times over is the signature of a template, not of a designed page.

           Each harm now declares its own `layout`, and the templates below are
           deliberately unlike each other in more than colour:

             stack   full-bleed band, figure above, pair of numbers below
             split   asymmetric 5/7 grid, prose left, figure bleeding right
             lead    the pair of numbers leads at figure size, prose under it
             data    the table is the subject; prose is a sidebar beside it
             cards   three photographs as equal cards, no pair of numbers
             wide    one full-width photograph with the prose over it
             quote   a single sentence set large, no figure at all

           The number and the pill survive in every variant, because they are the
           annual-report register the whole satire is written in. -->
      <section
        v-for="harm in harms"
        :key="harm.num"
        class="reveal border-t-2 border-hair"
        :style="{ background: `var(--harm-${harm.hue}-bg)` }"
      >
        <div class="mx-auto max-w-6xl px-6 py-14 md:py-20">
          <!-- The register, identical in every variant on purpose. -->
          <div class="mb-10 flex flex-wrap items-center gap-3">
            <span
              class="grid size-10 shrink-0 place-items-center rounded-lg border-2 font-mono text-xs font-semibold"
              :style="{
                color: `var(--harm-${harm.hue}-num)`,
                borderColor: `var(--harm-${harm.hue}-br)`,
              }"
              >{{ harm.num }}</span
            >
            <span
              class="rounded-full border-2 px-3 py-1.5 font-mono text-[0.6875rem] tracking-wider uppercase"
              :style="{
                color: `var(--harm-${harm.hue}-fg)`,
                borderColor: `var(--harm-${harm.hue}-br)`,
                background: `var(--harm-${harm.hue}-bg)`,
              }"
              >{{ harm.tag }}</span
            >
          </div>

          <!-- LAYOUT: stack — full-bleed band, figure first, numbers under. -->
          <template v-if="harm.layout === 'stack'">
            <h3 class="m-0 max-w-[26ch] text-title text-body">
              {{ harm.title }}
            </h3>
            <Figure
              v-if="harm.photo"
              class="mt-8"
              ratio="4/3"
              :src="`/company-sawit/img/${harm.photo.file}`"
              :alt="harm.photo.alt"
              :caption="harm.photo.caption"
            />
            <div class="mt-8 grid gap-8 lg:grid-cols-12 lg:gap-12">
              <HarmPair :harm="harm" class="lg:col-span-5" />
              <div class="lg:col-span-7">
                <p
                  v-for="(para, i) in harm.body"
                  :key="i"
                  class="m-0 mb-4 text-[1.0625rem] leading-relaxed text-quiet last:mb-0"
                >
                  <!-- eslint-disable-next-line vue/no-v-html -->
                  <span v-html="para"></span>
                </p>
              </div>
            </div>
          </template>

          <!-- LAYOUT: split — asymmetric 5/7, prose left, figure bleeding right. -->
          <template v-else-if="harm.layout === 'split'">
            <div class="grid items-start gap-10 lg:grid-cols-12 lg:gap-14">
              <div class="lg:col-span-5">
                <h3 class="m-0 text-title text-body">{{ harm.title }}</h3>
                <p
                  v-for="(para, i) in harm.body"
                  :key="i"
                  class="m-0 mt-5 text-[1.0625rem] leading-relaxed text-quiet"
                >
                  <!-- eslint-disable-next-line vue/no-v-html -->
                  <span v-html="para"></span>
                </p>
                <HarmPair v-if="harm.claim" :harm="harm" class="mt-8" />
              </div>
              <Figure
                v-if="harm.photo"
                ratio="5/4"
                :src="`/company-sawit/img/${harm.photo.file}`"
                :alt="harm.photo.alt"
                :caption="harm.photo.caption"
                class="lg:col-span-7" />
            </div>
          </template>

          <!-- LAYOUT: lead — the pair of numbers leads at figure size. The
               numbers ARE the block; the prose explains them underneath. -->
          <template v-else-if="harm.layout === 'lead'">
            <h3 class="m-0 max-w-[24ch] text-title text-body">
              {{ harm.title }}
            </h3>
            <HarmPair v-if="harm.claim" :harm="harm" class="mt-10" />
            <div class="mt-10 max-w-[62ch]">
              <p
                v-for="(para, i) in harm.body"
                :key="i"
                class="m-0 mb-4 text-[1.0625rem] leading-relaxed text-quiet last:mb-0"
              >
                <!-- eslint-disable-next-line vue/no-v-html -->
                <span v-html="para"></span>
              </p>
            </div>
            <Figure
              v-if="harm.photo"
              class="mt-10"
              ratio="16/9"
              :src="`/company-sawit/img/${harm.photo.file}`"
              :alt="harm.photo.alt"
              :caption="harm.photo.caption"
            />
          </template>

          <!-- LAYOUT: data — the table is the subject and gets the width;
               the prose is a narrow sidebar beside it, not a paragraph above. -->
          <template v-else-if="harm.layout === 'data'">
            <div
              class="grid items-start gap-10 lg:grid-cols-12 lg:gap-14"
            >
              <div class="lg:sticky lg:top-24 lg:col-span-4">
                <h3 class="m-0 text-title text-body">{{ harm.title }}</h3>
                <HarmPair v-if="harm.claim" :harm="harm" class="mt-8" />
                <p
                  v-for="(para, i) in harm.body"
                  :key="i"
                  class="m-0 mt-5 text-[1.0625rem] leading-relaxed text-quiet"
                >
                  <!-- eslint-disable-next-line vue/no-v-html -->
                  <span v-html="para"></span>
                </p>
              </div>
              <DataTable
                class="lg:col-span-8"
                caption="Ringkasan operasional 2019&ndash;2024, sebagaimana dilaporkan perusahaan. Kolom terakhir ditulis untuk laman ini."
                :columns="harm.table.columns.map((label) => ({ label }))"
                :rows="harm.table.rows.map((row) => [row.year, row.area, row.tbs, row.omitted])"
              />
            </div>
          </template>

          <!-- LAYOUT: cards — three photographs as equal cards, and no pair of
               numbers, because this block's argument is the photographs. -->
          <template v-else-if="harm.layout === 'cards'" class="lg:col-span-7">
            <h3 class="m-0 max-w-[28ch] text-title text-body">
              {{ harm.title }}
            </h3>
            <div class="mt-8 max-w-[62ch]">
              <p
                v-for="(para, i) in harm.body"
                :key="i"
                class="m-0 mb-4 text-[1.0625rem] leading-relaxed text-quiet last:mb-0"
              >
                <!-- eslint-disable-next-line vue/no-v-html -->
                <span v-html="para"></span>
              </p>
            </div>
            <div class="mt-10 grid gap-6 md:grid-cols-3">
              <Figure
                v-for="shot in harm.gallery"
                :key="shot.file"
                ratio="1/1"
                :src="`/company-sawit/img/${shot.file}`"
                :alt="shot.alt"
                :caption="shot.caption"
              />
            </div>
            <div
              v-if="harm.after"
              class="mt-10 grid gap-6 border-t-2 border-hair pt-8 md:grid-cols-2"
            >
              <p
                v-for="(para, i) in harm.after"
                :key="i"
                class="m-0 text-[1.0625rem] leading-relaxed text-quiet"
              >
                <!-- eslint-disable-next-line vue/no-v-html -->
                <span v-html="para"></span>
              </p>
            </div>
          </template>

          <!-- LAYOUT: wide — one full-width photograph with the prose set over
               its lower edge, the way the hero does it. -->
          <template v-else-if="harm.layout === 'wide'">
            <h3 class="m-0 max-w-[24ch] text-title text-body">
              {{ harm.title }}
            </h3>
            <div
              v-if="harm.photo"
              class="relative mt-10 overflow-hidden rounded-lg"
            >
              <img
                :src="`/company-sawit/img/${harm.photo.file}`"
                :alt="harm.photo.alt"
                width="1600"
                height="900"
                class="block h-[22rem] w-full object-cover md:h-[28rem]"
              />
              <!-- The gradient is perked to FULL opacity at the bottom, not the
                   70% the hero uses, and the reason is measured rather than
                   assumed: with 70%, the two photographs in these blocks
                   composited to 2.69:1 and 1.34:1 against white type, because
                   both images have a bright sky band that survives a 30%
                   transparent layer. 1.34:1 is unreadable.

                   A solid plate is the fix that works on an arbitrary
                   photograph, which is what these are: the images are generated
                   and could be swapped for anything. -->
              <div
                class="pointer-events-none absolute inset-0 bg-gradient-to-t from-leaf-900 via-leaf-900 to-leaf-900/80"
              />
              <div class="absolute inset-x-0 bottom-0 p-6 md:p-10">
                <p
                  class="m-0 max-w-[54ch] text-[1.0625rem] leading-relaxed text-leaf-100"
                >
                  <!-- eslint-disable-next-line vue/no-v-html -->
                  <span v-html="harm.body[0]"></span>
                </p>
              </div>
            </div>
            <div class="mt-8 grid gap-8 lg:grid-cols-12 lg:gap-12">
              <div class="lg:col-span-7">
                <p
                  v-for="(para, i) in harm.body.slice(1)"
                  :key="i"
                  class="m-0 mb-4 text-[1.0625rem] leading-relaxed text-quiet last:mb-0"
                >
                  <!-- eslint-disable-next-line vue/no-v-html -->
                  <span v-html="para"></span>
                </p>
              </div>
              <HarmPair
                v-if="harm.claim"
                :harm="harm"
                class="lg:col-span-5"
              />
            </div>
          </template>

          <!-- LAYOUT: quote — one sentence, set large, no figure at all. The
               block that asks the unanswerable question does not need a
               photograph to make its point. -->
          <template v-else-if="harm.layout === 'quote'">
            <h3
              class="m-0 max-w-[34ch] text-display leading-tight text-body"
            >
              {{ harm.title }}
            </h3>
            <blockquote
              class="m-0 mt-10 max-w-[46ch] border-l-4 pl-6 text-[1.375rem] leading-relaxed text-body italic"
              :style="{ borderColor: `var(--harm-${harm.hue}-br)` }"
            >
              <span v-html="harm.body[0]"></span>
            </blockquote>
            <div class="mt-10 grid gap-8 lg:grid-cols-12 lg:gap-12">
              <div class="lg:col-span-7">
                <p
                  v-for="(para, i) in harm.body.slice(1)"
                  :key="i"
                  class="m-0 mb-4 text-[1.0625rem] leading-relaxed text-quiet last:mb-0"
                >
                  <!-- eslint-disable-next-line vue/no-v-html -->
                  <span v-html="para"></span>
                </p>
              </div>
              <HarmPair
                v-if="harm.claim"
                :harm="harm"
                class="lg:col-span-5"
              />
            </div>
          </template>

          <!-- Fallback: any harm without a declared layout. Kept so adding a
               block without choosing a layout degrades to something readable
               rather than to nothing. -->
          <template v-else>
            <div class="grid items-start gap-10 lg:grid-cols-2 lg:gap-14">
              <div>
                <h3 class="m-0 text-title text-body">{{ harm.title }}</h3>
                <p
                  v-for="(para, i) in harm.body"
                  :key="i"
                  class="m-0 mt-5 text-[1.0625rem] leading-relaxed text-quiet"
                >
                  <!-- eslint-disable-next-line vue/no-v-html -->
                  <span v-html="para"></span>
                </p>
                <HarmPair v-if="harm.claim" :harm="harm" class="mt-8" />
              </div>
              <Figure
                v-if="harm.photo"
                :src="`/company-sawit/img/${harm.photo.file}`"
                :alt="harm.photo.alt"
                :caption="harm.photo.caption"
              />
            </div>
          </template>
        </div>
      </section>
    </section>

    <!-- ================= CONTACT ================= -->
    <section class="border-t-2 border-hair">
      <div class="mx-auto max-w-6xl px-6 py-16 md:py-20">
        <div class="flex flex-wrap items-start gap-4">
          <span
            class="grid size-12 shrink-0 place-items-center rounded-lg border-2 border-leaf-400 bg-leaf-100 font-mono text-sm font-semibold text-leaf-800 dark:border-leaf-500 dark:bg-leaf-900 dark:text-leaf-200"
            >09</span
          >
          <div class="min-w-0 flex-1">
            <h2
              class="m-0 text-display font-semibold tracking-tight text-body"
            >
              Hubungi kami
            </h2>
            <p
              class="m-0 mt-3 max-w-2xl text-[1.0625rem] leading-relaxed text-quiet"
            >
              Untuk keperluan media, silakan mengisi borang di bawah. Untuk
              warga yang terdampak, borang yang sama dipakai, dan waktu tanggap
              yang tercatat adalah empat puluh satu hari kerja.
            </p>
          </div>
        </div>

        <ContactForm />
      </div>
    </section>

    <FictionNotice
      label="Situs fiksi"
      link="/legal"
      link-label="Baca penafian lengkap dan daftar kredit"
    />
  </article>
</template>

<script setup lang="ts">
// Bound rather than literal: rolldown rewrites a literal public/
// path into a static import, and public/ is not an import root.
const asset_company_sawit_img_hero_aerial_jpg = '/company-sawit/img/hero-aerial.jpg'

// The phrase the company puts in italics is the euphemism itself. Marking it
// in the markup rather than styling the whole paragraph is what lets the
// emphasis carry the sarcasm: the words are theirs, not the page's.
const quote = (text: string) => `<em class="font-semibold not-italic">${text}</em>`

const stats = [
  { value: '412.000 ha', label: 'Konsesi di bawah pengelolaan' },
  { value: '1,4 juta ton', label: 'TBS dipanen 2024' },
  { value: '9,8 miliar Ryo', label: 'Pendapatan bersih' },
  { value: '27%', label: 'Lahan diklaim tidak bocor' },
]

const harms = [
  {
    num: '01',
    layout: 'split',
    hue: 'fire',
    tag: 'Pembakaran',
    title: 'Kabut asap 41 hari, dicatat sebagai bencana alam.',
    body: [
      `Pada 2015 kabut asap dari lahan kami melintasi perbatasan dan menutup sekolah di tiga desa tetangga selama 41 hari. Laporan kami mencatatnya sebagai ${quote('peristiwa alam')}. Kami tidak mempublikasikan titik api, luas terbakar, maupun waktu pemadaman. Yang kami publikasikan adalah jumlah alat pemadam.`,
    ],
    claim: { value: '11 unit', label: 'Alat pemadam yang kami miliki' },
    unprinted: {
      value: '412.000 ha',
      label: 'Lahan yang harus dijaga 11 unit itu',
    },
    photo: {
      file: 'fire.jpg',
      alt: 'Bekas kebakaran di lahan konsesi: tunggul pohon hitam dan tanah berabu, dengan pita hutan yang tidak terbakar di kejauhan',
      caption:
        'Bekas kebakaran, blok timur, tercatat sebagai "peristiwa alam" pada 2015. Gambar dibuat dengan model generatif untuk laman ini.',
    },
  },
  {
    num: '02',
    layout: 'stack',
    hue: 'water',
    tag: 'Air',
    title: 'Sungai tempat desa mencuci, sekarang warnanya teh.',
    body: [
      `Limbah cair pabrik dialirkan ke sungai tanpa instalasi pengolahan. Warga hulu kehilangan tangkapan ikan pada 2009 dan tidak pernah mendapatkannya kembali. Kami mencatatnya sebagai ${quote('penurunan hasil tangkapan karena faktor musim')}. Di kolom laporan tahunan, bagian air berbunyi: ${quote('konsumsi air kami efisien')}. Keduanya benar.`,
    ],
    claim: {
      value: '0 Ryo',
      label: 'Anggaran IPAL yang kami cantumkan',
    },
    unprinted: {
      value: '18 km',
      label: 'Aliran yang diterima limbah pabrik',
    },
    photo: {
      file: 'community.jpg',
      alt: 'Pemukiman di tepi konsesi: deretan rumah kayu dengan pepohonan sisa di sekitarnya',
      caption:
        'Permukiman di tepi konsesi, di luar pagar blok timur. Gambar dibuat dengan model generatif untuk laman ini.',
    },
  },
  {
    num: '03',
    layout: 'lead',
    hue: 'soil',
    tag: 'Penggusuran',
    title: '21 keluarga menunggu ganti rugi sejak 2004.',
    body: [
      `Ekspansi blok timur 2004 memindahkan 21 keluarga. Berkas ganti rugi mereka tercatat ${quote('dalam proses')} setiap tahun sejak itu, tanpa perubahan isi. Tiga permohonan ditolak pada 2021 dengan alasan yang tidak kami publikasikan. Keluarga yang menolak pindah diizinkan tinggal hingga kontrak tanam dimulai, yang artinya hingga mereka menjadi penghalang produksi.`,
    ],
    claim: {
      value: '100%',
      label: 'Klaim penyelesaian lahan, menurut kami',
    },
    unprinted: {
      value: '21 keluarga',
      label: 'Belum menerima apa pun, 20 tahun kemudian',
    },
    photo: {
      file: 'mill.jpg',
      alt: 'Pabrik pengolahan kelapa sawit dengan kawasan penanaman baru di sekitarnya',
      caption:
        'Lahan yang baru dibersihkan di sekitar pabrik, blok timur, sesudah ganti rugi tercatat "dalam proses" sejak 2004. Gambar dibuat dengan model generatif untuk laman ini.',
    },
  },
  {
    num: '04',
    layout: 'wide',
    hue: 'sick',
    tag: 'Gambut',
    title: '4.100 hektare gambut dikeringkan, lalu disebut penyimpan karbon.',
    body: [
      'Gambut basah menyimpan karbon. Gambut yang dikeringkan dengan kanal menjadi bahan bakar. Kami membangun kanal pada 2022 dan menerbitkan komitmen perlindungan gambut pada 2024. Kedua dokumen itu bersebelahan di laman ini, jaraknya satu klik.',
    ],
    claim: {
      value: '27%',
      label: 'Lahan kami diklaim tidak bocor',
    },
    unprinted: {
      value: '4.100 ha',
      label: 'Gambut yang dilewati kanal drainase 2022',
    },
    photo: {
      file: 'kanal-gambut.jpg',
      alt: 'Kanal drainase lurus memotong lahan gambut tropis, airnya gelap kecokelatan seperti teh, tebing tanah gambut hitam mengelupas, dengan pohon tumbang dan cakrawala berkabut di kejauhan',
      caption:
        'Kanal drainase blok gambut selatan. Gambar dibuat dengan model generatif untuk laman ini.',
    },
  },
  {
    num: '05',
    layout: 'data',
    hue: 'leaf',
    tag: 'Angka',
    title: 'Luas turun, produksi naik, penjelasan tidak diberikan.',
    body: [
      'Pada 2023 luas tanam kami menyusut 2.500 hektare sementara produksi naik 100.000 ton. Laporan tahunan tidak memuat penjelasan atas kombinasi tersebut. Produksi per hektare yang naik tajam bisa berarti banyak hal, dan yang paling tidak nyaman adalah yang paling mungkin.',
    ],
    claim: {
      value: '1,40 jt ton',
      label: 'TBS 2024, rekor tertinggi',
    },
    unprinted: {
      value: '58.900 ha',
      label: 'Luas tanam 2023, lebih kecil dari 2022',
    },
    table: {
      columns: [
        'Tahun',
        'Luas tanam ditambah (ha)',
        'TBS (juta ton)',
        'Yang tidak dicakup',
      ],
      rows: [
        {
          year: '2019',
          area: '34.500',
          tbs: '0,98',
          omitted: 'Permukiman 3 dusun diizinkan tinggal hingga kontrak tanam',
        },
        {
          year: '2020',
          area: '41.200',
          tbs: '1,05',
          omitted: 'Kabut asap tercatat Mei–Oktober, tidak disebut sebabnya',
        },
        {
          year: '2021',
          area: '52.800',
          tbs: '1,12',
          omitted:
            '3 permohonan ganti rugi ditolak, alasan tidak dipublikasikan',
        },
        {
          year: '2022',
          area: '61.400',
          tbs: '1,21',
          omitted: 'Drainase kanal baru melewati 4.100 ha gambut',
        },
        {
          year: '2023',
          area: '58.900',
          tbs: '1,31',
          omitted: 'Luas turun, produksi naik; penjelasan tidak diberikan',
        },
        {
          year: '2024',
          area: '63.600',
          tbs: '1,40',
          omitted: 'Audit Dewan Hijau ditunda ke 2026',
        },
      ],
    },
  },
  {
    num: '06',
    layout: 'cards',
    hue: 'leaf',
    tag: 'Program',
    title:
      'Kebun bibit, penanaman kembali, dan satu hutan yang tidak kami sentuh.',
    body: [],
    after: [
      'Kami mengoperasikan kebun bibit 40 juta bibit per tahun. Angka itu benar. Yang tidak kami cantumkan adalah bahwa bibit itu mengganti pohon yang kami tebang sendiri, sehingga penanaman kembali kami adalah biaya pemulihan atas kerusakan kami, dicatat di laporan sebagai kegiatan konservasi.',
      `Kami juga menetapkan 2.100 hektare sebagai kawasan lindung. Kawasan itu terletak di lereng dengan kemiringan di atas 30%, yang berarti tidak ekonomis untuk ditanami. Kami menerbitkannya sebagai komitmen konservasi sukarela.`,
      `Penanaman kembali adalah prosedur wajib bagi setiap konsesi di negeri ini, dan kami memenangkan penghargaan atas pelaksanaannya. Penghargaan itu diberikan oleh asosiasi yang kami ketuai.`,
    ],
    gallery: [
      {
        file: 'nursery.jpg',
        alt: 'Kebun bibit komersial dengan ribuan bibit kelapa sawit muda dalam polibag hitam tersusun barisan rapi, dengan pipa irigasi kabut di atasnya',
        caption: 'Kebun bibit blok utara, kapasitas 40 juta bibit per tahun.',
      },
      {
        file: 'replanting.jpg',
        alt: 'Foto udara area penanaman kembali dengan barisan bibit kelapa sawit muda tersusun geometris di lereng berteras, dan pita hutan tua hijau gelap di sudut bingkai',
        caption: 'Blok barat, tahun tanam 2023.',
      },
      {
        file: 'clear-cut.jpg',
        alt: 'Lantai hutan yang ditebang: tunggak-potong pucat di tanah merah dengan serbuk gergaji, dan satu pohon meranti tinggi utuh berdiri sendiri di tepi bingkai di bawah kanopi hijau lebat',
        caption: 'Kawasan lindung 2.100 ha, kemiringan di atas 30%. Gambar dibuat dengan model generatif untuk laman ini.',
      },
    ],
  },
  {
    num: '07',
    layout: 'wide',
    hue: 'soil',
    tag: 'Rantai pasok',
    title: 'Kami tidak mengaudit pembeli kami. Mereka tidak mengaudit kami.',
    body: [
      'CPO dan PK diekspor melalui pelabuhan Konoha. Selebihnya dijual ke pembeli lokal yang namanya tidak kami publikasikan. Kebijakan keberlanjutan kami mewajibkan mitra memenuhi standar yang tidak kami periksa, karena pemeriksaan memerlukan sumber daya yang dialokasikan untuk produksi.',
      'Pabrik bekerja dua puluh empat jam. Buah yang tiba dipanen paling lambat delapan belas jam sebelumnya; setelah itu kadar minyaknya turun dan muatannya ditolak. Penolakan dicatat sebagai ketidakpatutan mitra, bukan kesalahan penjadwalan. Pada 2024 tercatat 1.840 muatan ditolak dari 41.000, atau 4,5%. Angka tersebut tidak pernah muncul dalam laporan tahunan kami.',
    ],
    photo: {
      // ffb.jpg is a 1400x1400 square. Setting it in the `wide` overlay forces a
      // 0.406 letterbox, so `object-fit: cover` discards roughly 60% of the frame
      // and the fruit is cut out of its own photograph. port.jpg is a 0.563
      // landscape of the same width, which loses far less to the crop. The
      // square image stays unused rather than being cropped into something the
      // caption cannot honestly describe.
      file: 'port.jpg',
      alt: 'Pelabuhan muat CPO dan PK dengan kapal kargo dan deretan tandan buah menunggu angkutan',
      caption:
        'Tandan buah hasil panen menunggu angkutan di pelabuhan, blok tengah. Gambar dibuat dengan model generatif untuk laman ini.',
    },
  },
  {
    num: '08',
    layout: 'quote',
    hue: 'fire',
    tag: 'Pertanyaan',
    title: 'Satu pertanyaan yang tidak terjawab dalam dua puluh enam tahun.',
    body: [
      'Jika lahan kami produktif, mengapa perlu dibuka terus? Jika tidak produktif, mengapa dibuka terus? Kedua jawaban menghasilkan ekspansi, jadi pertanyaannya tidak perlu dijawab.',
      `Kami membuka 391.000 hektare sebelum komitmen 2018 kami berlaku, dan 21.000 hektare setelahnya. Komitmen kami tidak berlaku surut. Jumlah yang tidak tercakup adalah 391.000 hektare, atau 95% dari total konsesi, dan itulah yang kami sebut ${quote('lahan historis')}.`,
    ],
    photo: {
      file: 'nursery-close.jpg',
      alt: 'Foto makro bibit kelapa sawit muda dalam polibag hitam, pelepah hijau pekat sedang membuka dengan tetesan air di permukaan daun dan kompos gelap di pangkalnya',
      caption:
        'Bibit yang akan ditanam di tanah yang baru dibersihkan. Gambar dibuat dengan model generatif untuk laman ini.',
    },
  },
]

// The scroll reveal. Every element starts visible in the CSS and only the
// observer opts it in, so a reader whose observer never fires still reads
// everything.
onMounted(() => {
  const targets = document.querySelectorAll('.reveal')
  if (!('IntersectionObserver' in window)) {
    targets.forEach((t) => t.classList.add('is-in'))
    return
  }
  const observer = new IntersectionObserver(
    (entries) => {
      for (const entry of entries) {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-in')
          observer.unobserve(entry.target)
        }
      }
    },
    { rootMargin: '0px 0px -12% 0px', threshold: 0.08 },
  )
  targets.forEach((t) => observer.observe(t))
})
</script>
