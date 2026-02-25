# fo:page-number

## Summary

The fo:page-number formatting object is used to obtain an inline-area whose content is the page-number for the page on which the inline-area is placed. It generates and returns a single normal inline-area.

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_page-number -->

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

- The content of the inline-area depends on the reference-page and the reference-page-sequence. For fo:page-number, the reference-page is the page on which the inline-area is placed and the reference-page-sequence is the ancestor fo:page-sequence of the fo:page-number.
- The child areas of this inline-area are the same as the result of formatting a result-tree fragment consisting of: the content of any fo:folio-prefix child of the reference-page-sequence, followed by fo:character flow objects (one for each character in the folio-number string and with only the character property specified), followed by the content of any fo:folio-suffix child of the reference-page-sequence.
- The folio-number string is obtained by converting the folio-number for the reference-page in accordance with the number to string conversion properties of the reference-page-sequence.
- The conversion properties are: format, grouping-separator, grouping-size, letter-value, country, and language.
- fo:page-number is typically placed in fo:static-content to generate running page numbers in headers or footers.

## Code Samples

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_page-number -->
```xml
EMPTY
```

## See Also

- fo:page-number-citation -- for citing the page number of a referenced formatting object
- fo:page-number-citation-last -- for citing the last page number of a referenced formatting object
- fo:folio-prefix -- for specifying a static prefix for folio numbers
- fo:folio-suffix -- for specifying a static suffix for folio numbers
- fo:static-content -- common parent for running headers/footers containing page numbers
