# fo:folio-suffix

## Summary

The fo:folio-suffix formatting object specifies a static suffix for the folio numbers within a page-sequence. It does not directly produce any areas. Its children will be retrieved and used when formatting page numbers.

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_folio-suffix -->

## Content Model

`(#PCDATA | %inline;)*`

An fo:folio-suffix is not permitted to have an fo:page-number, fo:page-number-citation, or fo:page-number-citation-last as a descendant.

## Properties

This formatting object has no specific properties listed in the spec beyond those inherited from its content model. The formatting properties of its inline children apply as usual.

## Usage Notes

- fo:folio-suffix is a child of fo:page-sequence and provides a suffix that is appended to every folio number generated within that page-sequence.
- The content of fo:folio-suffix is retrieved and used when formatting page numbers via fo:page-number and fo:page-number-citation.
- The child areas of an fo:page-number inline-area include the content of any fo:folio-prefix child of the reference-page-sequence, followed by the folio-number characters, followed by the content of any fo:folio-suffix.
- Circular references are prevented: fo:folio-suffix must not contain fo:page-number, fo:page-number-citation, or fo:page-number-citation-last as descendants.

## Code Samples

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_folio-suffix -->
```xml
(#PCDATA|%inline;)*
```

## See Also

- [fo:folio-prefix](fo-folio-prefix.md) — for specifying a static prefix for folio numbers
- [fo:page-number](fo-page-number.md) — the formatting object that uses the folio-suffix content
- [fo:page-number-citation](fo-page-number-citation.md) — also uses the folio-suffix content when formatting cited page numbers
- [fo:page-sequence](fo-page-sequence.md) — the parent element that contains fo:folio-suffix
