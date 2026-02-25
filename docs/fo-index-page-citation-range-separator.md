# fo:index-page-citation-range-separator

## Summary

The `fo:index-page-citation-range-separator` formatting object specifies the formatting objects used to separate two page numbers forming a range in the generated list of page numbers.

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_index-page-citation-range-separator -->

## Areas

The `fo:index-page-citation-range-separator` formatting object does not directly produce any areas. Its children will be retrieved and used by `fo:index-page-citation-list` when formatting the list of page references.

## Constraints

None.

## Content Model

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_index-page-citation-range-separator -->
```xml
(#PCDATA|%inline;)*
```

## Properties

This formatting object has no specific properties beyond those inherited from the content model.

## Usage Notes

- If no `fo:index-page-citation-range-separator` is specified, the default range separator is an en dash (U+2013).
- Implementations may provide an alternative default, for example to provide a language- or locale-specific index range separator.
- The range separator is inserted between the first and last page numbers of a cited page item range (e.g., "5-8" where "-" is the range separator).
- The range separator has `keep-with-previous.within-line` and `keep-with-next.within-line` set to "always" to prevent line breaks within a range.

## Code Samples

No code samples in spec for this formatting object.

## See Also

- `fo:index-page-citation-list` -- parent formatting object
- `fo:index-page-citation-list-separator` -- sibling for list separators
- `fo:index-key-reference` -- sibling that generates page citations
