# fo:index-range-end

## Summary

The `fo:index-range-end` is used to indicate the end of an "indexed range" that is started by its matching `fo:index-range-begin`. See `fo:index-range-begin` for details.

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_index-range-end -->

## Areas

The `fo:index-range-end` does not generate any area.

## Constraints

- Preceding this `fo:index-range-end` in document order, there must be an `fo:index-range-begin` with which it forms a matching pair. If there is no such `fo:index-range-begin`, it is an error, and the implementation should recover by ignoring this `fo:index-range-end`.

## Content Model

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_index-range-end -->
```xml
EMPTY
```

## Properties

| Property | Inherited | Conformance Level |
|---|---|---|
| `ref-id` | no | Extended |

## Usage Notes

- The `ref-id` property must match the `id` value of the corresponding `fo:index-range-begin` to form a matching pair.
- The `fo:index-range-end` does not itself carry an `index-key`; the index key is specified on the matching `fo:index-range-begin`.

## Code Samples

No code samples in spec for this formatting object. See the "Formatting Objects for Indexing" introduction section for comprehensive examples.

## See Also

- `fo:index-range-begin` -- matching formatting object that starts the index range
- `fo:index-key-reference` -- references index keys to generate page citations
