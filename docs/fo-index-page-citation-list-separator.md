# fo:index-page-citation-list-separator

## Summary

The `fo:index-page-citation-list-separator` formatting object specifies the formatting objects used to separate singleton page numbers or page number ranges in the generated list of page numbers.

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_index-page-citation-list-separator -->

## Areas

The `fo:index-page-citation-list-separator` formatting object does not directly produce any areas. Its children will be retrieved and used by `fo:index-page-citation-list` when formatting the list of page references.

## Constraints

None.

## Content Model

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_index-page-citation-list-separator -->
```xml
(#PCDATA|%inline;)*
```

## Properties

This formatting object has no specific properties beyond those inherited from the content model.

## Usage Notes

- If no `fo:index-page-citation-list-separator` is specified, the default list separator is a comma followed by a space (U+002C U+0020).
- Implementations may provide an alternative default, for example to provide a language- or locale-specific index list separator.
- The separator content is inserted between each cited page item or range in the formatted page number list, except after the last item.
- Typical content is a comma and space, or a semicolon and space.

## Code Samples

No code samples in spec for this formatting object.

## See Also

- [fo:index-page-citation-list](fo-index-page-citation-list.md) — parent formatting object
- [fo:index-page-citation-range-separator](fo-index-page-citation-range-separator.md) — sibling for range separators
- [fo:index-key-reference](fo-index-key-reference.md) — sibling that generates page citations
