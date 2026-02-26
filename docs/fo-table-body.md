# fo:table-body

## Summary

The `fo:table-body` formatting object is used to contain the content of the table body. A table must have at least one `fo:table-body`, and may have multiple bodies to logically group rows.

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_table-body -->

## Areas

The `fo:table-body` formatting object does not generate any areas. It returns the sequence of areas created by concatenating the sequences of areas returned by each of the children of the `fo:table-body`.

## Constraints

The order of concatenation of the sequences of areas returned by the children of the `fo:table-body` is the same order as the children are ordered under the `fo:table-body`.

## Content Model

```
(fo:table-row+ | fo:table-cell+)
```

The `fo:table-body` has `fo:table-row` (one or more) as its children, or alternatively `fo:table-cell` (one or more). In the latter case cells are grouped into rows using the `starts-row` and `ends-row` properties.

In addition this formatting object may have a sequence of zero or more `fo:marker`s as its initial children.

## Properties

| Property | Inherited | Conformance Level |
|---|---|---|
| Common Accessibility Properties | N/A | Basic |
| Common Aural Properties | N/A | Extended |
| Common Border, Padding, and Background Properties | N/A | Basic (see note) |
| Common Relative Position Properties | N/A | Extended |
| `border-after-precedence` | no | Basic (collapsing) |
| `border-before-precedence` | no | Basic (collapsing) |
| `border-end-precedence` | no | Basic (collapsing) |
| `border-start-precedence` | no | Basic (collapsing) |
| `id` | N/A | Basic |
| `index-class` | N/A | Extended |
| `index-key` | N/A | Extended |
| `visibility` | no | Extended |

**Note on Border, Padding, and Background Properties:** Only the background properties (`background-attachment`, `background-color`, `background-image`, `background-repeat`, `background-position-horizontal`, `background-position-vertical`) from this set apply. If the value of `border-collapse` is "collapse" or "collapse-with-precedence" for the table, the border properties (`border-before-color`, `border-before-style`, `border-before-width`, `border-after-color`, `border-after-style`, `border-after-width`, `border-start-color`, `border-start-style`, `border-start-width`, `border-end-color`, `border-end-style`, `border-end-width`, `border-top-color`, `border-top-style`, `border-top-width`, `border-bottom-color`, `border-bottom-style`, `border-bottom-width`, `border-left-color`, `border-left-style`, `border-left-width`, `border-right-color`, `border-right-style`, `border-right-width`) also apply.

## Usage Notes

- Every `fo:table` must contain at least one `fo:table-body`.
- Multiple `fo:table-body` elements can be used to logically group rows, with each body potentially having different background properties.
- You can use either explicit `fo:table-row` children or direct `fo:table-cell` children (with `starts-row`/`ends-row` to indicate row boundaries).
- Table-cells must each be entirely contained within a single `fo:table-body`; cells cannot span across body boundaries.
- The `fo:table-body` is a structural grouping container that does not generate areas itself; it merely passes through the areas from its child rows/cells.

## Code Samples

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_table-body -->
```xml
(table-row+|table-cell+)
```

## See Also

- [fo:table](fo-table.md) — the parent table formatting object
- [fo:table-header](fo-table-header.md) — table header rows
- [fo:table-footer](fo-table-footer.md) — table footer rows
- [fo:table-row](fo-table-row.md) — groups cells into rows
- [fo:table-cell](fo-table-cell.md) — individual cell content
