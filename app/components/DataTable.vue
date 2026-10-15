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
    <table class="min-w-0 border-collapse text-left text-[0.9375rem]">
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
</script>
