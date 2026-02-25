# fo:multi-toggle

## Summary

The `fo:multi-toggle` is typically used to establish an area that when actuated (for example implemented as "clicked"), has the effect of switching from one `fo:multi-case` to another. The `switch-to` property value of the `fo:multi-toggle` typically matches the `case-name` property value of the `fo:multi-case` to switch to.

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_multi-toggle -->

## Areas

The `fo:multi-toggle` formatting object does not generate any areas. The `fo:multi-toggle` formatting object returns the sequence of areas created by concatenating the sequences of areas returned by each of the children of the `fo:multi-toggle`. Each of the areas returned by the `fo:multi-toggle` has a `switch-to` trait with the same value as on the returning `fo:multi-toggle`.

## Constraints

- The order of concatenation of the sequences of areas returned by the children of the `fo:multi-toggle` is the same order as the children are ordered under the `fo:multi-toggle`.
- Activating an area returned by an `fo:multi-toggle` causes a change to the value of the `currently-visible-multi-case` of the closest ancestor `fo:multi-switch`. See the `switch-to` property for how the `switch-to` value selects an `fo:multi-case`.
- An `fo:multi-toggle` is only permitted as a descendant of an `fo:multi-case`.

## Content Model

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_multi-toggle -->
```xml
(#PCDATA|%inline;|%block;)*
```

## Properties

| Property | Inherited | Conformance Level |
|---|---|---|
| Common Accessibility Properties | N/A | Basic |
| `id` | N/A | Basic |
| `index-class` | N/A | Extended |
| `index-key` | N/A | Extended |
| `switch-to` | no | Extended |

## Usage Notes

- The `switch-to` property specifies which `fo:multi-case` to make visible when this toggle is activated. The value typically matches a `case-name` on one of the sibling `fo:multi-case` elements.
- Special `switch-to` values include "xsl-preceding" (switch to the previous `fo:multi-case`), "xsl-following" (switch to the next `fo:multi-case`), and "xsl-any" (present a choice of all available cases).
- The `fo:multi-toggle` must appear as a descendant of an `fo:multi-case`. It triggers switching on the closest ancestor `fo:multi-switch`.
- Typical content for an `fo:multi-toggle` includes an icon or text label indicating the action (e.g., a plus/minus icon for expand/collapse).

## Code Samples

No code samples in spec for this formatting object. See the "Expandable/Collapsible Table of Contents" example in the "Dynamic Effects: Link and Multi Formatting Objects" introduction section for a comprehensive demonstration.

## See Also

- `fo:multi-switch` -- ancestor formatting object that controls which multi-case is visible
- `fo:multi-case` -- parent formatting object containing the alternative content sub-trees
