# fo:index-range-begin

## Summary

The `fo:index-range-begin` formatting object is used to indicate the beginning of an "indexed range" associated with an index key. The index range is ended by a corresponding `fo:index-range-end`.

All formatting objects following (in document order) this `fo:index-range-begin`, and up to the matching `fo:index-range-end`, are considered to be under the index range influence of this `fo:index-range-begin`.

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_index-range-begin -->

## Areas

The `fo:index-range-begin` does not generate any area.

## Constraints

- Each `fo:index-range-begin` formatting object must specify both an `id` and an `index-key` property.
- An `fo:index-range-begin`/`fo:index-range-end` pair is considered a matching pair if the `ref-id` property of the `fo:index-range-end` has the same value as the `id` property on the `fo:index-range-begin`.
- Following this `fo:index-range-begin` in document order, there must be an `fo:index-range-end` with which it forms a matching pair. If there is no such `fo:index-range-end`, it is an error, and the implementation should recover by assuming the equivalent of a matching `fo:index-range-end` at the end of the document.

## Content Model

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_index-range-begin -->
```xml
EMPTY
```

## Properties

| Property | Inherited | Conformance Level |
|---|---|---|
| `id` | N/A | Basic |
| `index-key` | N/A | Extended |
| `index-class` | N/A | Extended |

## Usage Notes

- Use `fo:index-range-begin` and `fo:index-range-end` as a pair to mark a range of content associated with an index key. All pages spanned by this range will be included in the index page citation list for that key.
- The `id` property on `fo:index-range-begin` must be unique and is used by the matching `fo:index-range-end` via its `ref-id` property.
- The `index-key` property specifies the key value that will be referenced by `fo:index-key-reference` elements in the back-of-the-book index.
- The `index-class` property can be used to categorize the index entry (e.g., distinguishing entries in the preface from entries in chapters).

## Code Samples

No code samples in spec for this formatting object. See the "Formatting Objects for Indexing" introduction section for comprehensive examples of index range usage.

## See Also

- [fo:index-range-end](fo-index-range-end.md) — matching formatting object that ends the index range
- [fo:index-key-reference](fo-index-key-reference.md) — references index keys to generate page citations
- [fo:index-page-citation-list](fo-index-page-citation-list.md) — groups and formats index page citations
