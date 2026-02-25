# fo:list-item-label

## Summary

The `fo:list-item-label` formatting object contains the content of the label of a list-item, typically used to either enumerate, identify, or adorn the list-item's body.

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_list-item-label -->

## Areas

The `fo:list-item-label` formatting object does not generate any areas. The `fo:list-item-label` formatting object returns the sequence of areas created by concatenating the sequences of areas returned by each of the children of the `fo:list-item-label`.

## Constraints

The order of concatenation of the sequences of areas returned by the children of the `fo:list-item-label` is the same order as the children are ordered under the `fo:list-item-label`.

## Content Model

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_list-item-label -->
```xml
(%block;)+
```

In addition this formatting object may have a sequence of zero or more `fo:marker`s as its initial children.

## Properties

| Property | Inherited | Conformance Level |
|---|---|---|
| Common Accessibility Properties | N/A | Basic |
| `id` | N/A | Basic |
| `index-class` | N/A | Extended |
| `index-key` | N/A | Extended |
| `keep-together` | no | Extended |

## Usage Notes

- The `fo:list-item-label` typically contains an `fo:block` with the label text (a bullet character, number, letter, or other marker).
- The width available for the label is determined by the `provisional-distance-between-starts` and `provisional-label-separation` properties set on the ancestor `fo:list-block`. The label content should be constrained (e.g., using `end-indent="label-end()"`) to avoid overlapping with the body content.
- Use the `label-end()` function in an `end-indent` expression on the `fo:block` child to correctly constrain the label width.

## Code Samples

No code samples in spec for this formatting object.

## See Also

- `fo:list-item` -- parent formatting object
- `fo:list-item-body` -- sibling containing the body content
- `fo:list-block` -- grandparent that sets provisional distances
