<script setup lang="ts">
/**
 * IN-PAGE SECTION NAVIGATION.
 *
 * The homepage is eight harm blocks plus a stat strip and a contact form. The
 * only way to reach block 06 used to be scrolling past five other blocks, and
 * the header nav has four page links that do not help with that at all. This
 * is the piece that was missing: a sticky bar under the header that names every
 * section on the page.
 *
 * Two decisions worth stating, because both were the wrong way first:
 *
 * The active section is tracked with IntersectionObserver rather than by
 * listening to scroll and comparing offsets. A scroll handler re-reads layout
 * on every frame, which is what makes sticky navigation jank; the observer only
 * fires when a section actually crosses the line.
 *
 * The bar scrolls horizontally on a phone instead of wrapping to two rows. A
 * wrapping row of pills doubles the bar's height mid-scroll, which pushes the
 * content under it and reads as a layout jump. One row that scrolls sideways
 * keeps a constant height.
 */
const props = defineProps<{
  items: { id: string; label: string; num?: string }[]
}>()

const activeId = ref('')
const route = useRoute()
const router = useRouter()

let observer: IntersectionObserver | null = null

// A section counts as current when its top edge crosses this line, which sits
// just below the sticky header so the label changes as the heading arrives
// rather than after it has already passed.
const ROOT_MARGIN_TOP = '-128px 0px 0px 0px'

/**
 * Navigation goes through the ROUTER, not a bare anchor tag.
 *
 * An `<a href="#blok-03">` sets location.hash directly, which is a browser
 * navigation: Vue never sees it, `useRoute().hash` never changes, and the jump
 * lands the heading underneath the sticky header because the browser's native
 * anchor scroll ignores `scroll-margin-top`. Routing the click means the hash
 * lives in router state, the pill can be linked, and the scroll offset is ours
 * to correct.
 */
function goTo(id: string) {
  router.push({ path: route.path, hash: `#${id}` })
}

/**
 * Scroll a hash target into view with the sticky header accounted for.
 *
 * The router's own hash scrolling is not used because it does not compensate
 * for the header, and the section's `scroll-mt-24` is only respected by the
 * browser's native anchor jump — which we no longer take. So the offset is
 * measured here from the header's real height rather than hardcoded, so it
 * stays right if the header ever changes height.
 */
function scrollToSection(id: string, behavior: ScrollBehavior = 'smooth') {
  const el = document.getElementById(id)
  if (!el) return
  const header = document.querySelector('header')
  const headerH = header ? header.getBoundingClientRect().height : 0
  // A small gap so the section's top border is not flush against the header.
  const gap = 12
  const top = el.getBoundingClientRect().top + window.scrollY - headerH - gap
  window.scrollTo({ top: Math.max(top, 0), behavior })
}

onMounted(() => {
  window.addEventListener('hashchange', onHashChange)

  // A link that arrived with a hash (shared URL, or a reload mid-page) must be
  // honoured on mount, or the page loads showing the top of the page while the
  // address bar says otherwise. `instant` because the reader did not ask for an
  // animation they cannot see.
  if (route.hash) {
    const id = route.hash.slice(1)
    // Wait a frame: the reveal animation sets up on mount and the sections are
    // still at their pre-animation positions when the first callback runs.
    requestAnimationFrame(() => scrollToSection(id, 'instant'))
  }

  observer = new IntersectionObserver(
    (entries) => {
      // Pick the entry nearest the top of the viewport. Several can fire in one
      // batch during a fast scroll, and taking the last one reported gave a
      // label that lagged a section behind.
      const visible = entries
        .filter((e) => e.isIntersecting)
        .sort((a, b) => a.boundingClientRect.top - b.boundingClientRect.top)
      if (visible.length) {
        activeId.value = visible[0].target.id
      } else {
        // Nothing is intersecting, which happens above the first section and
        // below the last. Keep whichever was last rather than clearing to a
        // state with nothing selected.
        const stillVisible = [...document.querySelectorAll('[data-sectionnav-item]')].some(
          (el) => {
            const r = el.getBoundingClientRect()
            return r.top < window.innerHeight * 0.5 && r.bottom > 0
          },
        )
        if (!stillVisible) activeId.value = ''
      }
    },
    { rootMargin: ROOT_MARGIN_TOP, threshold: 0 },
  )

  for (const item of props.items) {
    const el = document.getElementById(item.id)
    if (el) observer.observe(el)
  }
})

onBeforeUnmount(() => {
  observer?.disconnect()
  observer = null
  window.removeEventListener('hashchange', onHashChange)
})

/**
 * The router changes the hash without scrolling, so back and forward would move
 * the address bar while the page stayed where it was. Watching hashchange keeps
 * the two in step. It is registered rather than relied on because `router.push`
 * with a hash deliberately does not scroll — that is what lets `goTo` own the
 * offset — so the scroll has to be triggered separately.
 */
function onHashChange() {
  const id = route.hash.slice(1)
  if (id) scrollToSection(id)
  else window.scrollTo({ top: 0, behavior: 'smooth' })
}

</script>

<template>
  <nav
    aria-label="Bagian pada halaman ini"
    class="sticky top-[var(--header-h)] z-30 border-b-2 border-hair bg-paper/95 backdrop-blur-md"
  >
    <!-- The pills live in one scrolling row. `no-scrollbar` keeps the bar from
         growing a second row of scrollbar on desktop.

         The offset is `var(--header-h)`, not a hardcoded rem value. It used to
         be `top-[4.125rem]` (66px), which matched the desktop header — but the
         header is 168px tall at 320px and ~76px on phones after the wordmark
         change, so a fixed offset either left a gap over the content or parked
         this bar under the header. app.vue measures the real header height and
         publishes it as `--header-h` on :root, so the two stay in step at every
         width. -->
    <div class="mx-auto max-w-6xl px-6">
      <ul
        class="no-scrollbar -mx-1 flex items-center gap-1.5 overflow-x-auto py-2.5"
      >
        <li v-for="item in items" :key="item.id" class="shrink-0">
          <!-- ROUTED, not an anchor tag. `router.push` keeps the hash in router
               state so the pill is linkable and the address bar stays honest,
               and the click handler does the scroll with the sticky header
               compensated. A bare `href="#..."` here would bypass all of that.

               Still a real link to assistive tech and to middle-click: the href
               is present, the router call happens in the click handler, and
               preventDefault only fires once the router has accepted it. -->
          <a
            :href="`#${item.id}`"
            :data-sectionnav-item="item.id"
            :aria-current="activeId === item.id ? 'true' : undefined"
            class="inline-flex min-h-9 items-center gap-2 rounded-full border-2 px-3.5 py-1.5 font-mono text-[0.75rem] font-semibold tracking-wide uppercase no-underline transition-colors duration-150 ease-out"
            :class="
              activeId === item.id
                ? 'border-leaf-600 bg-leaf-600 text-white'
                : 'border-hair bg-card text-quiet hover:border-leaf-400 hover:text-leaf-700 dark:hover:border-leaf-500 dark:hover:text-leaf-200'
            "
            @click.prevent="goTo(item.id)"
          >
            <span v-if="item.num" class="opacity-70">{{ item.num }}</span>
            {{ item.label }}
          </a>
        </li>
      </ul>
    </div>
  </nav>
</template>
