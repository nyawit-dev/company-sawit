// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2025-07-15',
  devtools: { enabled: true },

  // GitHub Pages project site serves from /company-sawit/, so every asset and
  // route must be generated under that base. Nitro's static output is
  // committed by the workflow; no Node process serves it.
  css: ['~/assets/theme.css'],

  nitro: {
    preset: 'github-pages',
  },
  app: {
    baseURL: '/company-sawit/',
    head: {
      htmlAttrs: { lang: 'id', 'data-theme': 'sakura' },
      title: 'PT Perkebunan Asap Emas Nusantara',
      meta: [
        { charset: 'utf-8' },
        { name: 'viewport', content: 'width=device-width, initial-scale=1' },
        {
          name: 'description',
          content:
            'Profil perusahaan perkebunan kelapa sawit fiksi. Seluruh isinya rekaan untuk karya satire.',
        },
        { name: 'robots', content: 'noindex, nofollow' },
      ],
    },
  },
})
