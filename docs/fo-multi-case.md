# fo:multi-case

## Summary

The `fo:multi-case` is used to contain (within an `fo:multi-switch`) each alternative sub-tree of formatting objects among which the parent `fo:multi-switch` will choose one to show and will hide the rest.

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_multi-case -->

## Areas

The `fo:multi-case` formatting object does not generate any areas. The `fo:multi-case` formatting object returns the sequence of areas created by concatenating the sequences of areas returned by each of the children of the `fo:multi-case`.

## Constraints

- The order of concatenation of the sequences of areas returned by the children of the `fo:multi-case` is the same order as the children are ordered under the `fo:multi-case`.
- An `fo:multi-case` is only permitted to have children that would be permitted to be children of the parent of the `fo:multi-switch` that is the parent of the `fo:multi-case`, except that an `fo:multi-case` may not contain `fo:marker` children. In particular, it can contain `fo:multi-toggle` objects (at any depth), which controls the `fo:multi-case` switching.
- This restriction applies recursively. For example, an `fo:multi-case` whose parent `fo:multi-switch` is a child of another `fo:multi-case` may only have children that would be permitted in place of the outer `fo:multi-case`'s parent `fo:multi-switch`.

## Content Model

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_multi-case -->
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
| `starting-state` | no | Extended |
| `case-name` | no | Extended |
| `case-title` | no | Extended |

## Usage Notes

- Set `starting-state="show"` on the `fo:multi-case` that should be initially visible. Set `starting-state="hide"` on all others.
- The `case-name` property provides a name that can be referenced by `fo:multi-toggle`'s `switch-to` property to select this case.
- The `case-title` property provides a human-readable title for the case. When the `switch-to` value is "any", an implementation would typically present a list of choices labeled using the `case-title` property.
- The content model is context-dependent: the `fo:multi-case` may only contain children that would be valid in the position where the parent `fo:multi-switch` appears.

## Code Samples

No code samples in spec for this formatting object. See the "Expandable/Collapsible Table of Contents" example in the "Dynamic Effects: Link and Multi Formatting Objects" introduction section for a comprehensive demonstration.

## See Also

- `fo:multi-switch` -- parent formatting object that wraps all multi-case alternatives
- `fo:multi-toggle` -- descendant formatting object that triggers case switching
