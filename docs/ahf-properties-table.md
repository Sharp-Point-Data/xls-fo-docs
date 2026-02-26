# Antenna House Extension Properties: Table Extension Properties

<!-- Source: XSL-FO-Reference-74-MID.pdf pp.312-476 -->

Extensions to table formatting including auto-layout limits, row orphan/widow control, cell content repetition at breaks, footnote handling in table headers/footers, and table accessibility summary.

## axf:repeat-cell-content-at-break

Specifies whether to copy the contents of a cell when a cell breaks.

Values have the following meanings:
- **true**: When the content of table cell fits in table-cell-area without breaking and table-cell-area breaks according to the break of other table-cell in the same row, or according to the break among the multiple rows with `number-rows-spanned`, usually the content of table-cell-area becomes empty. When `axf:repeat-cell-content-at-break` is specified to `<fo:table-cell>`, the content of the cell before break is copied and repeated.
- **false**: The content of the cell is not copied.

| Attribute | Value |
|---|---|
| **Applies to** | `<fo:table-cell>` |
| **Values** | `true \| false` |
| **Initial** | `false` |
| **Inherited** | no |

## axf:repeat-footnote-in-table-footer

Specifies whether to repeat the `<fo:footnote>` in the `<fo:table-footer>` that is repeated by `table-omit-footer-at-break="false"`.

Values have the following meanings:
- **true**: Process `<fo:footnote>` repeatedly.
- **false**: Do not process `<fo:footnote>` repeatedly.

| Attribute | Value |
|---|---|
| **Applies to** | `<fo:table-footer>` |
| **Values** | `true \| false` |
| **Initial** | `true` |
| **Inherited** | yes |

## axf:repeat-footnote-in-table-header

Specifies whether to repeat the `<fo:footnote>` in the `<fo:table-header>` that is repeated by `table-omit-header-at-break="false"`.

Values have the following meanings:
- **true**: Process `<fo:footnote>` repeatedly.
- **false**: Do not process `<fo:footnote>` repeatedly.

| Attribute | Value |
|---|---|
| **Applies to** | `<fo:table-header>` |
| **Values** | `true \| false` |
| **Initial** | `true` |
| **Inherited** | yes |

## axf:retrieve-table-rows

Specifies the maximum number of `<fo:table-row>` in `<fo:marker>` referenced from `<fo:retrieve-table-marker>`.

When multiple rows are retrieved, the number of rows may be inconsistent and the rows may be duplicated. In such cases, specify the maximum number of lines to avoid it. Values less than 1 are considered 1.

| Attribute | Value |
|---|---|
| **Applies to** | `<fo:retrieve-table-marker>` |
| **Values** | `<integer>` |
| **Initial** | `1` |
| **Inherited** | no |

## axf:table-auto-layout-limit

Specifies the number of rows of `<fo:table>` to read ahead to determine the width of column when `table-layout="auto"` is specified.

| Attribute | Value |
|---|---|
| **Applies to** | `<fo:table>` |
| **Values** | `auto \| <number>` |
| **Initial** | `auto` |
| **Inherited** | yes |

## axf:table-row-orphans

Specifies the number of table-rows that must remain at the bottom of the page (column).

| Attribute | Value |
|---|---|
| **Applies to** | `<fo:table-body>` |
| **Values** | `<integer>` |
| **Initial** | `1` |
| **Inherited** | yes |

## axf:table-row-widows

Specifies the number of table-rows that must remain at the top of the page (column).

| Attribute | Value |
|---|---|
| **Applies to** | `<fo:table-body>` |
| **Values** | `<integer>` |
| **Initial** | `1` |
| **Inherited** | yes |

## axf:table-summary

Describes the table summary. This is equivalent to `<table summary="<string>">` in HTML. It does not affect the formatting result. It is outputted with Tagged PDF.

| Attribute | Value |
|---|---|
| **Applies to** | `<fo:table>` |
| **Values** | `<string>` |
| **Initial** | empty |
| **Inherited** | no |
