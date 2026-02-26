# fo:footnote-body

## Summary

The `fo:footnote-body` is used to generate the footnote content that is placed in the footnote-reference-area near the after-edge of the page.

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_footnote-body -->

## Areas

The `fo:footnote-body` generates and returns one or more block-level areas with area-class "xsl-footnote".

## Constraints

- The `fo:footnote-body` is only permitted as a child of an `fo:footnote`.
- No area may have more than one child block-area returned by the same `fo:footnote-body` formatting object.
- Areas with area-class "xsl-footnote" must be properly ordered within the area tree relative to other areas with the same area-class.

## Content Model

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_footnote-body -->
```xml
(%block;)+
```

## Properties

| Property | Inherited | Conformance Level |
|---|---|---|
| Common Accessibility Properties | N/A | Basic |
| `id` | N/A | Basic |
| `index-class` | N/A | Extended |
| `index-key` | N/A | Extended |

## Usage Notes

- The `fo:footnote-body` typically contains one or more `fo:block` elements with the footnote text.
- The footnote body areas are placed in the footnote-reference-area, which is located near the after-edge of the region-body on the page containing (or following) the footnote anchor.
- The `fo:footnote-body` can only appear as the second child of an `fo:footnote`.

## Code Samples

No code samples in spec for this formatting object.

## See Also

- [fo:footnote](fo-footnote.md) — parent formatting object
- [fo:inline](fo-inline.md) — sibling providing the inline footnote citation
