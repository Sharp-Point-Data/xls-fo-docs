# fo:repeatable-page-master-reference

## Summary

An `fo:repeatable-page-master-reference` is the next simplest sub-sequence-specifier after `fo:single-page-master-reference`. It specifies a sub-sequence consisting of repeated instances of a single page-master. The number of repetitions may be bounded or potentially unbounded.

## Areas

The `fo:repeatable-page-master-reference` formatting object generates no area directly. It is used by the `fo:page-sequence` formatting object to generate pages.

## Constraints

The `fo:repeatable-page-master-reference` has a reference to the `fo:simple-page-master` which has the same `master-name` as the `master-reference` trait on the `fo:repeatable-page-master-reference`.

The sub-sequence of pages mapped to this sub-sequence-specifier satisfies the constraints of this sub-sequence-specifier if:

1. The sub-sequence of pages consists of zero or more pages.
2. Each page is generated using the `fo:simple-page-master` referenced by the `fo:repeatable-page-master-reference`.
3. The length of the sub-sequence is less than or equal to the value of `maximum-repeats`.

If no region-master child of the page-master referred to by this formatting object has a `region-name` associated to any flow in an `fo:page-sequence`, then the sub-sequence is constrained to have length zero.

## Content Model

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_repeatable-page-master-reference -->
```xml
EMPTY
```

The `fo:repeatable-page-master-reference` element has no child elements.

## Properties

| Property | Type | Initial Value | Inherited | Conformance Level |
|---|---|---|---|---|
| master-reference | `<name>` | an empty name | no, a value is required | Basic |
| maximum-repeats | `<number> \| no-limit \| inherit` | no-limit | no | Basic |

### Property Details

- **master-reference**: Specifies the name of the page-master to be used in repetition until the content is exhausted or the `maximum-repeats` limit is reached, whichever occurs first. The name must not be empty and must refer to a `master-name` in the current or a preceding `fo:layout-master-set`.
- **maximum-repeats**: Specifies the maximum number of pages in the sub-sequence. `no-limit` means no constraint is specified. A numeric value specifies the maximum number of pages. A value of 0 indicates this `master-reference` will not be used. If a fractional value or a value less than 0 is specified, it will be rounded to the nearest integer greater than or equal to 0.

## Usage Notes

The `fo:repeatable-page-master-reference` is the simplest way to specify that all pages in a page-sequence (or a bounded portion of them) should use the same page layout. It is used within an `fo:page-sequence-master`.

Common usage patterns:

- **Unbounded repetition** (`maximum-repeats="no-limit"`): All pages use the same layout. This is the simplest page-sequence-master configuration, suitable for documents where every page has the same structure.
- **Bounded repetition**: A fixed number of pages use one layout before the page-sequence-master moves to the next sub-sequence-specifier. For example, the first 3 pages might use one layout, then remaining pages use another.

When the referenced page-master has no regions with names matching any flow in the `fo:page-sequence`, the sub-sequence length is constrained to zero, effectively skipping this sub-sequence-specifier.

## Code Samples

No code samples in spec for this formatting object. The spec section contains only the content model declaration shown above.

## See Also

- fo:page-sequence-master -- parent container
- fo:single-page-master-reference -- for exactly one page with a given master
- fo:repeatable-page-master-alternatives -- for conditional page-master selection
- fo:simple-page-master -- the page-master referenced by master-reference
