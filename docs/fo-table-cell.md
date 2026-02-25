# fo:table-cell

## Summary

The `fo:table-cell` formatting object is used to group content to be placed in a table cell. A table-cell occupies one or more grid units in the row-progression-direction and column-progression-direction. The `starts-row` and `ends-row` properties can be used when the input data does not have elements containing the cells in each row, but instead each row starts at elements of a particular type.

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_table-cell -->

## Areas

The `fo:table-cell` formatting object generates one or more normal reference-areas. It returns these reference-areas and any page-level-out-of-line areas returned by the children of the `fo:table-cell`.

## Trait Derivation

The method for deriving the `border` for a cell is specified by the `border-collapse` trait:

### Separate Borders (`border-collapse="separate"`)

The border is composed of two components:
1. The first is placed with the outside edge coincident with the table grid boundary line, with a width of half the value for the `border-separation` trait. It is filled in accordance with the `background` trait of the `fo:table`.
2. Inside this border is placed, for each side of the cell, a border based on a border specified on the cell or inherited.

### Collapsing Borders with Precedence (`border-collapse="collapse-with-precedence"`)

The border for each side of the cell is determined by, for each segment of a border, selecting from all border specifications for that segment the border that has the highest precedence. It is an error if there are two such borders that have the same precedence but are not identical. An implementation may recover by selecting one of the borders. Each border segment is placed centered on the table grid boundary line. On devices that do not support sub-pixel rendering, if an effective border width is determined to be an odd number of pixels it is implementation defined on which side of the grid boundary line the odd pixel is placed.

### Collapsing Borders (`border-collapse="collapse"`)

The border for each side of the cell is determined by, for each segment of a border, selecting from all border specifications for that segment the border that has the most "eye catching" border style. Each border segment is placed centered on the table grid boundary line. Where there is a conflict between the styles of border segments that collapse, the following rules determine which border style "wins":

1. Borders with the `border-style` of "hidden" take precedence over all other conflicting borders. Any border with this value suppresses all borders at this location.
2. Borders with a style of "none" have the lowest priority. Only if the border properties of all the elements meeting at this edge are "none" will the border be omitted (but note that "none" is the default value for the border style).
3. If none of the styles is "hidden" and at least one of them is not "none", then narrow borders are discarded in favor of wider ones.
4. If the remaining border styles have the same `border-width`, then styles are preferred in this order: "double", "solid", "dashed", "dotted", "ridge", "outset", "groove", and the lowest: "inset".
5. If border styles differ only in color, then a style set on a cell wins over one on a row, which wins over a row group, column, column group and, lastly, table.

## Constraints

- A table-cell occupies one or more grid units in the row-progression-direction and column-progression-direction.
- The content-rectangle of the cell is the size of the portion of the grid the cell occupies minus, for each of the four sides:
  - If `border-collapse` is "separate": half the value of the `border-separation` trait; otherwise 0.
  - If `border-collapse` is "separate": the thickness of the cell-border; otherwise half the thickness of the effective border.
  - The cell padding.
- The method for determining the `block-progression-dimension` of the cell in the grid is governed by the `row-height` trait.
- No area may have more than one normal child area returned by the same `fo:table-cell` formatting object.
- The children of each normal area returned by an `fo:table-cell` formatting object must be normal block-areas returned by the children of the `fo:table-cell`, must be properly stacked, and must be properly ordered.
- Any reference-level-out-of-line areas returned by the children of the `fo:table-cell` are handled as described in `fo:float`.

## Content Model

```
(%block;)+
```

In addition this formatting object may have a sequence of zero or more `fo:marker`s as its initial children.

## Properties

| Property | Inherited | Conformance Level |
|---|---|---|
| Common Accessibility Properties | N/A | Basic |
| Common Aural Properties | N/A | Extended |
| Common Border, Padding, and Background Properties | N/A | Basic |
| Common Relative Position Properties | N/A | Extended |
| `border-after-precedence` | no | Basic (collapsing) |
| `border-before-precedence` | no | Basic (collapsing) |
| `border-end-precedence` | no | Basic (collapsing) |
| `border-start-precedence` | no | Basic (collapsing) |
| `block-progression-dimension` | no | Basic |
| `column-number` | no | Basic |
| `display-align` | yes | Basic |
| `relative-align` | yes | Extended |
| `empty-cells` | yes | Basic |
| `ends-row` | no | Basic |
| `height` | no | Basic |
| `id` | N/A | Basic |
| `index-class` | N/A | Extended |
| `index-key` | N/A | Extended |
| `inline-progression-dimension` | no | Basic |
| `number-columns-spanned` | no | Basic |
| `number-rows-spanned` | no | Basic |
| `starts-row` | no | Basic |
| `width` | no | Basic |

## Usage Notes

- Each `fo:table-cell` must contain at least one block-level formatting object (typically `fo:block`).
- Use `column-number` to explicitly place a cell in a specific column. If omitted, the cell is placed in the next available column.
- Use `number-columns-spanned` and `number-rows-spanned` to span multiple columns or rows.
- Use `display-align` to control the vertical alignment of content within the cell ("before", "center", "after").
- Use `starts-row` and `ends-row` when placing cells directly under `fo:table-body`/`fo:table-header`/`fo:table-footer` without explicit `fo:table-row` elements.
- The `empty-cells` property controls whether borders and backgrounds are rendered for cells with no content (applicable only when `border-collapse` is "separate").
- The full border, padding, and background properties apply to `fo:table-cell`, unlike `fo:table-row`, `fo:table-body`, `fo:table-header`, and `fo:table-footer` where only background (and sometimes collapsing borders) apply.

## Code Samples

No code samples in spec for this formatting object's own section. The content model is `(%block;)+`.

For complete examples of `fo:table-cell` usage including column and row spanning (`number-columns-spanned`, `number-rows-spanned`), explicit column positioning, nested tables within cells, and cell-level styling with `background-color`, see **guide-tables-advanced**.

## See Also

- `fo:table` -- the parent table formatting object
- `fo:table-row` -- groups cells into rows
- `fo:table-body` -- table body section
- `fo:table-header` -- table header section
- `fo:table-footer` -- table footer section
- `fo:table-column` -- column specifications
- `column-number` property
- `number-columns-spanned` property
- `number-rows-spanned` property
- `display-align` property
- `empty-cells` property
- `starts-row` property
- `ends-row` property
- `border-collapse` property
