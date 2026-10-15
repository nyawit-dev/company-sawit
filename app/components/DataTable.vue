<template>
  <!--
    THE TABLE.

    Tables carry the site's sharpest content: the company's own record in the
    left columns and the omission in the last one. Three things are deliberate
    here and easy to get wrong:

    1. The last column is visually separated, so the eye is drawn to it before
       the numbers, which is the opposite of how a real annual report orders it.
    2. Row hover moves the whole row, not the cells, because per-cell hover
       reads as a selection affordance this table does not have.
    3. Zebra striping is on the odd rows only and uses the sunken token, which
       survives both themes. Alternating white/card does not, because those two
       are 1.05:1 apart in night mode.
  -->
  <div
    data-table-scroll
    class="rounded-3xl border-2 border-hair bg-card shadow-[var(--shadow-card)]"
  >
    <table class="w-full border-collapse text-left text-[0.9375rem]">
      <!-- Column widths live here rather than in a stylesheet.

           `table-layout: fixed` distributes the available width EQUALLY unless
           the columns declare their own, and a stylesheet cannot win the fight
           against `width: 100%` on the table itself. Equal columns put "63.600"
           in a 315px cell and the year in a 315px cell, which is absurd: the
           year needs a fraction of that and the omission column needs the rest.
           A colgroup is the one place the browser reads first, so it works at
           every width without !important.

           The widths are generated from the actual column count rather than
           hardcoded, because the tables here have three columns and four, and a
           fixed list of <col> elements silently drops the trailing column of the
           shorter table — leaving it to share whatever is left of the last
           declared width.

           Each column also carries a min-width, and that pair matters more than
           the percentage alone. A percentage of a narrow parent is useless —
           6% of a 524px table is 31px, which cannot hold the word "TAHUN", so
           the table's min-content width takes over and the prose columns get
           squeezed to 94px and 79px. That is exactly how the history table came
           to be 524px wide with 367px-tall rows. The percentage sizes the column
           when there is room; the min-width is the floor when there is not.

           The omission column is unlisted on purpose — it absorbs the
           remainder, which is what gives a full sentence room to be a sentence. -->
      <colgroup>
        <col
          v-for="(col, i) in columns"
          :key="i"
          :class="i < columns.length - 1 ? colWidths[i] : undefined"
        />
      </colgroup>
      <caption
        v-if="caption"
        class="border-b-2 border-hair bg-sunken px-5 py-4 text-left font-mono text-[0.6875rem] font-bold tracking-wider text-quiet uppercase"
      >
        {{ caption }}
      </caption>
      <thead>
        <tr class="border-b-2 border-hair">
          <th
            v-for="(col, i) in columns"
            :key="i"
            scope="col"
            class="px-4 py-3.5 font-mono text-[0.625rem] font-bold tracking-wider break-words text-leaf-700 uppercase sm:whitespace-nowrap sm:px-5 dark:text-leaf-300"
            :class="col.omit ? 'border-l-2 border-leaf-400 dark:border-leaf-500' : ''"
          >
            {{ col.label }}
          </th>
        </tr>
      </thead>
      <tbody>
        <tr
          v-for="(row, r) in rows"
          :key="r"
          class="border-b border-hair transition-colors duration-150 ease-out last:border-b-0 hover:bg-leaf-100 dark:hover:bg-leaf-900/60"
          :class="r % 2 === 1 ? 'bg-sunken' : ''"
        >
          <th
            scope="row"
            class="px-4 py-3.5 text-left font-mono text-sm font-bold break-words text-body sm:whitespace-nowrap sm:px-5"
          >
            {{ row[0] }}
          </th>
          <td
            v-for="(cell, c) in row.slice(1)"
            :key="c"
            class="px-4 py-3.5 align-top break-words text-body sm:px-5"
            :class="
              isOmitColumn(c) ? 'border-l-2 border-leaf-400 dark:border-leaf-500' : ''
            "
          >
            {{ cell }}
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup lang="ts">
// Bound so the omission rule can be computed from the column count rather than
// hardcoded to an index that only fits one table.
const props = defineProps<{
  caption?: string
  /** Column labels. A column whose label starts with "YANG TIDAK" is the
   *  omission column and gets the accent rule. */
  columns: { label: string; omit?: boolean }[]
  /** Row cells. The first cell of each row is the row header. */
  rows: string[][]
}>()

// The omission column is the last one, so the rule is placed by counting back
// from the end. `row.slice(1)` drops the row header, so a cell index of
// length-2 is the final column.
function isOmitColumn(cellIndex: number) {
  return cellIndex === props.columns.length - 2
}

// Widths for every column except the last, which absorbs the remainder.
// Declared as a percentage with a floor, because the two fail in opposite
// situations: a percentage alone collapses on a narrow parent (6% of 524px is
// 31px, too small to hold "TAHUN"), while a min-width alone would leave the
// year column absurdly wide on a desktop. The last column is deliberately
// absent from this list so the prose keeps every spare pixel.
const colWidths = [
  'w-[6%] min-w-[4.5rem]',
  'w-[18%] min-w-[11rem]',
  'w-[15%] min-w-[8rem]',
]
</script>
