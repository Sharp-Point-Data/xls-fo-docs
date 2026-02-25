# fo:list-block

## Summary

The `fo:list-block` formatting object is used to format a list. It generates one or more normal block-areas containing the list items. Each child `fo:list-item` provides one item in the list.

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_list-block -->

## Areas

The `fo:list-block` formatting object generates one or more normal block-areas. The `fo:list-block` returns these areas, any page-level-out-of-line areas, and any reference-level-out-of-line areas returned by the children of the `fo:list-block`.

## Constraints

- No area may have more than one normal child area returned by the same `fo:list-block` formatting object.
- The children of each normal area returned by an `fo:list-block` formatting object must be normal block-areas returned by the children of the `fo:list-block`, must be properly stacked, and must be properly ordered.

## Content Model

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_list-block -->
```xml
(list-item+)
```

In addition this formatting object may have a sequence of zero or more `fo:marker`s as its initial children.

## Properties

| Property | Inherited | Conformance Level |
|---|---|---|
| Common Accessibility Properties | N/A | Basic |
| Common Aural Properties | N/A | Extended |
| Common Border, Padding, and Background Properties | N/A | Basic |
| Common Margin Properties - Block | N/A | Basic |
| Common Relative Position Properties | N/A | Extended |
| `break-after` | no | Basic |
| `break-before` | no | Basic |
| `clear` | no | Extended |
| `id` | N/A | Basic |
| `index-class` | N/A | Extended |
| `index-key` | N/A | Extended |
| `intrusion-displace` | yes | Extended |
| `keep-together` | no | Extended |
| `keep-with-next` | no | Extended |
| `keep-with-previous` | no | Extended |
| `provisional-distance-between-starts` | yes | Basic |
| `provisional-label-separation` | yes | Basic |

## Usage Notes

- The `fo:list-block` is the top-level container for lists. It must contain one or more `fo:list-item` children.
- The `provisional-distance-between-starts` property controls the distance from the start-edge of the list-item-label to the start-edge of the list-item-body. This is typically used to set consistent indentation for list item content.
- The `provisional-label-separation` property controls the minimum gap between the end of the label and the start of the body content.
- Use `keep-together`, `keep-with-next`, and `keep-with-previous` to control page/column breaks within and around the list.
- The list-block itself does not define whether items are numbered, bulleted, or labeled; that is determined by the content placed in each `fo:list-item-label`.

## Code Samples

No code samples in spec for this formatting object.

## See Also

- `fo:list-item` -- child formatting object containing label and body for each list entry
- `fo:list-item-label` -- contains the label content (bullet, number, etc.)
- `fo:list-item-body` -- contains the body content of a list item
