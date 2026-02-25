# fo:page-number-citation-last

## Summary

The fo:page-number-citation-last is used to reference the page-number for the last page containing an area that is (a) returned by the cited formatting object and (b) has an area-class that is consistent with the specified page-citation-strategy. It generates and returns a single normal inline-area. It may be used to provide the page-numbers in the table of contents, cross-references, and, when combined with fo:page-number-citation, for page range entries.

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_page-number-citation-last -->

## Content Model

`EMPTY`

## Properties

| Property | Inherited | Conformance Level |
|----------|-----------|-------------------|
| Common Accessibility Properties | N/A | Basic |
| Common Aural Properties | N/A | Extended |
| Common Border, Padding, and Background Properties | No | Basic |
| Common Font Properties | Yes | Basic |
| Common Margin Properties-Inline | No | Basic |
| Common Relative Position Properties | No | Extended |
| alignment-adjust | No | Extended |
| alignment-baseline | No | Extended |
| baseline-shift | No | Extended |
| dominant-baseline | No | Extended |
| id | No | Basic |
| index-class | No | Extended |
| index-key | No | Extended |
| keep-with-next | No | Extended |
| keep-with-previous | No | Extended |
| letter-spacing | Yes | Basic |
| line-height | Yes | Basic |
| page-citation-strategy | No | Extended |
| ref-id | No | Basic |
| score-spaces | Yes | Basic |
| text-altitude | No | Extended |
| text-decoration | No | Basic |
| text-depth | No | Extended |
| text-shadow | No | Extended |
| text-transform | Yes | Basic |
| visibility | Yes | Extended |
| word-spacing | Yes | Basic |
| wrap-option | Yes | Extended |

## Usage Notes

- The cited page is the page of the last page area (in the pre-order traversal order of the area tree) that satisfies the constraints of the page-citation-strategy on this fo:page-number-citation-last.
- The child areas of the generated inline-area are the same as the result of formatting the result-tree fragment defined in the fo:page-number specification, using the cited page as the reference-page and the fo:page-sequence that generated the cited-page as the reference-page-sequence.
- The page-citation-strategy property controls which types of areas (normal, footnote, etc.) are considered when determining the last page.
- fo:page-number-citation-last is commonly combined with fo:page-number-citation to create page range entries (e.g., "pp. 5-12") in indexes and cross-references.

## Code Samples

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_page-number-citation-last -->
```xml
EMPTY
```

## See Also

- fo:page-number-citation -- for citing the first page of a referenced formatting object
- fo:page-number -- for the current page number
- fo:folio-prefix -- for specifying a static prefix for folio numbers
- fo:folio-suffix -- for specifying a static suffix for folio numbers
