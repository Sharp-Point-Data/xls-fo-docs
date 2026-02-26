# axf:footnote-number-citation

## Summary

The `axf:footnote-number-citation` extension object can be used to reference the number of a footnote generated with `axf:footnote-number` and located in the same parent structure level.

<!-- Source: XSL-FO-Reference-74-MID.pdf p.298 -->

## Properties

| Property | Description |
|---|---|
| `ref-id` | The identifier of the corresponding `axf:footnote-number` element to reference |

## Parent Objects

- `fo:footnote-body`

## Child Objects

None. This is an empty formatting object.

## Code Samples

See the application example in `axf:footnote-number` (ahf-fo-footnote-number.md) which demonstrates the combined usage of `axf:footnote-number` and `axf:footnote-number-citation` together.

## See Also

- `axf:footnote-number` -- generates the footnote number that this object references
