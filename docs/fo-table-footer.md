# fo:table-footer

## Summary

The `fo:table-footer` formatting object is used to contain the content of the table footer. The footer content may be repeated on each page or column break when the table spans multiple pages or columns, depending on the `table-omit-footer-at-break` property on the parent `fo:table`.

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_table-footer -->

## Areas

The `fo:table-footer` formatting object does not generate any areas. It returns the sequence of areas created by concatenating the sequences of areas returned by each of the children of the `fo:table-footer`.

## Constraints

The order of concatenation of the sequences of areas returned by the children of the `fo:table-footer` is the same order as the children are ordered under the `fo:table-footer`.

## Content Model

```
(fo:table-row+ | fo:table-cell+)
```

The `fo:table-footer` has `fo:table-row` (one or more) as its children, or alternatively `fo:table-cell` (one or more). In the latter case cells are grouped into rows using the `starts-row` and `ends-row` properties.

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

- Use `fo:table-footer` to define rows that should appear at the bottom of each table fragment when the table breaks across pages.
- Control footer repetition with the `table-omit-footer-at-break` property on the parent `fo:table`.
- You can use either explicit `fo:table-row` children or direct `fo:table-cell` children (with `starts-row`/`ends-row` to indicate row boundaries).
- In the `fo:table` content model, the `fo:table-footer` appears before the `fo:table-body` children even though it renders after the body content. This allows streaming processors to handle the footer without requiring a second pass.

## Code Samples

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_table-footer -->
```xml
(table-row+|table-cell+)
```

## See Also

- `fo:table` -- the parent table formatting object
- `fo:table-header` -- table header rows
- `fo:table-body` -- table body rows
- `fo:table-row` -- groups cells into rows
- `fo:table-cell` -- individual cell content
- `fo:table-footer-alternatives` -- alternative footer content (XSL-FO 2.0)
- `table-omit-footer-at-break` property
