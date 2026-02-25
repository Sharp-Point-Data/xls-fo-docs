# fo:conditional-table-header-reference

## Summary

The `fo:conditional-table-header-reference` formatting object is used to specify table header content given set conditions. It is a child of `fo:table-header-alternatives` and allows different header rows to be displayed depending on the boundary type (page, column, or region) at which a table breaks.

This is a new formatting object introduced in XSL-FO 2.0.

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_conditional-table-header-reference -->

## Areas

The `fo:conditional-table-header-reference` formatting object does not generate any areas directly, but returns the sequence of areas created by concatenating the areas returned by each of the children.

## Constraints

The order of concatenation of the sequences of areas returned by the children of the `fo:conditional-table-header-reference` is the same order as the children are ordered under the `fo:conditional-table-header-reference`.

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
| `header-position` | no | Extended |

**Note on Border, Padding, and Background Properties:** Only the background properties (`background-attachment`, `background-color`, `background-image`, `background-repeat`, `background-position-horizontal`, `background-position-vertical`) from this set apply. If the value of `border-collapse` is "collapse" or "collapse-with-precedence" for the table, the border properties (`border-before-color`, `border-before-style`, `border-before-width`, `border-after-color`, `border-after-style`, `border-after-width`, `border-start-color`, `border-start-style`, `border-start-width`, `border-end-color`, `border-end-style`, `border-end-width`, `border-top-color`, `border-top-style`, `border-top-width`, `border-bottom-color`, `border-bottom-style`, `border-bottom-width`, `border-left-color`, `border-left-style`, `border-left-width`, `border-right-color`, `border-right-style`, `border-right-width`) also apply.

## Usage Notes

- The `header-position` property is the key distinguishing property. It determines under which boundary condition (page, column, region) this particular header content is used.
- Multiple `fo:conditional-table-header-reference` elements with different `header-position` values allow different header content depending on whether the table breaks at a page boundary, column boundary, or other boundary type.
- The children follow the same pattern as `fo:table-header`: either `fo:table-row` or `fo:table-cell` elements.
- This enables use cases such as: a full header on the first page and a compact "continued" header on subsequent pages.

## Code Samples

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_conditional-table-header-reference -->
```xml
(table-row+|table-cell+)
```

## See Also

- `fo:table-header-alternatives` -- the parent formatting object
- `fo:table-header` -- the table header section
- `fo:conditional-table-footer-reference` -- the equivalent for footers
- `header-position` property
