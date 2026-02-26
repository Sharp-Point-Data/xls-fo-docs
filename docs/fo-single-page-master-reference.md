# fo:single-page-master-reference

## Summary

An `fo:single-page-master-reference` is the simplest sub-sequence-specifier. It specifies a sub-sequence consisting of a single instance of a single page-master. It is used to specify the use of a particular page-master at a given point in the sequence of pages that would be generated using the `fo:page-sequence-master` that is the parent of the `fo:single-page-master-reference`.

## Areas

The `fo:single-page-master-reference` formatting object generates no area directly. It is used by the `fo:page-sequence` formatting object to generate pages.

## Constraints

The `fo:single-page-master-reference` has a reference to the `fo:simple-page-master` which has the same `master-name` as the `master-reference` trait on the `fo:single-page-master-reference`.

The sub-sequence of pages mapped to this sub-sequence-specifier satisfies the constraints of this sub-sequence-specifier if:

1. The sub-sequence of pages consists of a single page.
2. That page is constrained to have been generated using the `fo:simple-page-master` referenced by the `fo:single-page-master-reference`.

## Content Model

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_single-page-master-reference -->
```xml
EMPTY
```

The `fo:single-page-master-reference` element has no child elements.

## Properties

| Property | Type | Initial Value | Inherited | Conformance Level |
|---|---|---|---|---|
| master-reference | `<name>` | an empty name | no, a value is required | Basic |

### Property Details

- **master-reference**: Specifies the name of the page-master to be used to create a single page instance. The name must not be empty and must refer to a `master-name` that exists within the current or a preceding `fo:layout-master-set`. If the name is empty, an error shall be reported.

## Usage Notes

The `fo:single-page-master-reference` is used within an `fo:page-sequence-master` to specify that exactly one page should be generated using the referenced page-master before moving to the next sub-sequence-specifier in the sequence.

This is typically used for pages that occur exactly once in a page-sequence, such as:

- A title page at the beginning of a chapter
- A separator page between sections
- A dedicated table-of-contents page

If the content for the page-sequence requires more than one page and the `fo:single-page-master-reference` is the only sub-sequence-specifier, an error will occur because the sub-sequence-specifier sequence will be exhausted while content remains to be placed.

## Code Samples

No code samples in spec for this formatting object. The spec section contains only the content model declaration shown above.

## See Also

- [fo:page-sequence-master](fo-page-sequence-master.md) — parent container
- [fo:repeatable-page-master-reference](fo-repeatable-page-master-reference.md) — for repeated use of a single page-master
- [fo:repeatable-page-master-alternatives](fo-repeatable-page-master-alternatives.md) — for conditional page-master selection
- [fo:simple-page-master](fo-simple-page-master.md) — the page-master referenced by master-reference
