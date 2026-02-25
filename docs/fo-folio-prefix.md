# fo:folio-prefix

## Summary

The fo:folio-prefix formatting object specifies a static prefix for the folio numbers within a page-sequence. It does not directly produce any areas. Its children will be retrieved and used when formatting page numbers.

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_folio-prefix -->

## Content Model

`(#PCDATA | %inline;)*`

An fo:folio-prefix is not permitted to have an fo:page-number, fo:page-number-citation, or fo:page-number-citation-last as a descendant.

## Properties

This formatting object has no specific properties listed in the spec beyond those inherited from its content model. The formatting properties of its inline children apply as usual.

## Usage Notes

- fo:folio-prefix is a child of fo:page-sequence and provides a prefix that is prepended to every folio number generated within that page-sequence.
- The content of fo:folio-prefix is retrieved and used when formatting page numbers via fo:page-number and fo:page-number-citation.
- The child areas of an fo:page-number inline-area include the content of any fo:folio-prefix child of the reference-page-sequence, followed by the folio-number characters, followed by the content of any fo:folio-suffix.
- Circular references are prevented: fo:folio-prefix must not contain fo:page-number, fo:page-number-citation, or fo:page-number-citation-last as descendants.
- Common use cases include chapter prefixes (e.g., "A-" for appendix page numbers) or section identifiers prepended to page numbers.

## Code Samples

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_folio-prefix -->
```xml
(#PCDATA|%inline;)*
```

## See Also

- fo:folio-suffix -- for specifying a static suffix for folio numbers
- fo:page-number -- the formatting object that uses the folio-prefix content
- fo:page-number-citation -- also uses the folio-prefix content when formatting cited page numbers
- fo:page-sequence -- the parent element that contains fo:folio-prefix
