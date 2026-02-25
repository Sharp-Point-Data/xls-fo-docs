# fo:list-item-body

## Summary

The `fo:list-item-body` formatting object contains the content of the body of a list-item.

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_list-item-body -->

## Areas

The `fo:list-item-body` formatting object does not generate any areas. The `fo:list-item-body` formatting object returns the sequence of areas created by concatenating the sequences of areas returned by each of the children of the `fo:list-item-body`.

## Constraints

The order of concatenation of the sequences of areas returned by the children of the `fo:list-item-body` is the same order as the children are ordered under the `fo:list-item-body`.

## Content Model

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_list-item-body -->
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

- The `fo:list-item-body` typically contains one or more `fo:block` elements with the main content of the list item.
- The starting position of the body content is determined by the `provisional-distance-between-starts` property on the ancestor `fo:list-block`. Use `start-indent="body-start()"` on the `fo:block` child to correctly position the body content.

## Code Samples

No code samples in spec for this formatting object.

## See Also

- `fo:list-item` -- parent formatting object
- `fo:list-item-label` -- sibling containing the label content
- `fo:list-block` -- grandparent that sets provisional distances
