# fo:conditional-table-footer-reference

## Summary

The `fo:conditional-table-footer-reference` formatting object is used to specify table footer content given set conditions. It is a child of `fo:table-footer-alternatives` and allows different footer rows to be displayed depending on the boundary type (page, column, or region) at which a table breaks.

This is a new formatting object introduced in XSL-FO 2.0.

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_conditional-table-footer-reference -->

## Areas

The `fo:conditional-table-footer-reference` formatting object does not generate any areas directly, but returns the sequence of areas created by concatenating the areas returned by each of the children.

## Constraints

The order of concatenation of the sequences of areas returned by the children of the `fo:conditional-table-footer-reference` is the same order as the children are ordered under the `fo:conditional-table-footer-reference`.

## Content Model

```
(fo:table-row+ | fo:table-cell+)
```

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
| `footer-position` | no | Extended |

**Note on Border, Padding, and Background Properties:** Only the background properties (`background-attachment`, `background-color`, `background-image`, `background-repeat`, `background-position-horizontal`, `background-position-vertical`) from this set apply. If the value of `border-collapse` is "collapse" or "collapse-with-precedence" for the table, the border properties (`border-before-color`, `border-before-style`, `border-before-width`, `border-after-color`, `border-after-style`, `border-after-width`, `border-start-color`, `border-start-style`, `border-start-width`, `border-end-color`, `border-end-style`, `border-end-width`, `border-top-color`, `border-top-style`, `border-top-width`, `border-bottom-color`, `border-bottom-style`, `border-bottom-width`, `border-left-color`, `border-left-style`, `border-left-width`, `border-right-color`, `border-right-style`, `border-right-width`) also apply.

## Usage Notes

- The `footer-position` property is the key distinguishing property. It determines under which boundary condition (page, column, region) this particular footer content is used.
- Multiple `fo:conditional-table-footer-reference` elements with different `footer-position` values allow different footer content depending on whether the table breaks at a page boundary, column boundary, or other boundary type.
- The children follow the same pattern as `fo:table-footer`: either `fo:table-row` or `fo:table-cell` elements.
- This enables use cases such as: a "continued on next page" footer on intermediate pages and a summary/totals footer on the last page.

## Code Samples

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_conditional-table-footer-reference -->
```xml
(table-row+|table-cell+)
```

## See Also

- [fo:table-footer-alternatives](fo-table-footer-alternatives.md) — the parent formatting object
- [fo:table-footer](fo-table-footer.md) — the table footer section
- [fo:conditional-table-header-reference](fo-conditional-table-header-reference.md) — the equivalent for headers
- footer-position property
