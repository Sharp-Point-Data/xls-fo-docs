# fo:page-number-citation

## Summary

The fo:page-number-citation is used to reference the page-number for the page containing the first normal area returned by the cited formatting object. It generates and returns a single normal inline-area. It may be used to provide the page-numbers in the table of contents, cross-references, and index entries.

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_page-number-citation -->

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

- The cited page is the page containing, as a descendant, the first normal area returned by the formatting object with an id trait matching the ref-id trait of the fo:page-number-citation (the referenced formatting object).
- The child areas of the generated inline-area are the same as the result of formatting the result-tree fragment defined in the fo:page-number specification, using the cited page as the reference-page and the fo:page-sequence that generated the cited-page as the reference-page-sequence.
- The ref-id property is required and must reference the id of another formatting object in the document.
- fo:page-number-citation is commonly used in table-of-contents entries together with fo:leader and fo:basic-link, and in cross-references within the body text.

## Code Samples

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_page-number-citation -->
```xml
EMPTY
```

## See Also

- fo:page-number -- for the current page number
- fo:page-number-citation-last -- for citing the last page containing areas from a formatting object
- fo:leader -- commonly used with fo:page-number-citation in TOC entries
- fo:basic-link -- for creating hyperlinks alongside page citations
