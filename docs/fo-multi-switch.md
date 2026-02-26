# fo:multi-switch

## Summary

The `fo:multi-switch` wraps the specification of alternative sub-trees of formatting objects (each sub-tree being within an `fo:multi-case`), and controls the switching (activated via `fo:multi-toggle`) from one alternative to another.

The direct children of an `fo:multi-switch` object are `fo:multi-case` objects. Only a single `fo:multi-case` may be visible at a single time. The user may switch between the available multi-cases.

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_multi-switch -->

## Areas

The `fo:multi-switch` formatting object does not generate any areas. The `fo:multi-switch` formatting object returns the sequence of areas returned by the currently visible `fo:multi-case`. If there is no currently visible `fo:multi-case` no areas are returned.

## Trait Derivation

The `currently-visible-multi-case` trait has as its initial value a reference to the first `fo:multi-case` child that has a value of "show" of the `starting-state` trait. If there is no such child, it has a value indicating that there is no currently visible `fo:multi-case`.

When an `fo:multi-toggle` is actuated, its closest ancestral `fo:multi-switch`'s `currently-visible-multi-case` trait value changes to refer to the `fo:multi-case` selected by the `switch-to` property value of the `fo:multi-toggle`. Once the `currently-visible-multi-case` trait gets a value indicating that there is no currently visible `fo:multi-case`, it becomes impossible to actuate an `fo:multi-toggle` in this `fo:multi-switch`.

## Constraints

- The order of the sequence of areas returned by the `fo:multi-switch` is the same as the order of the areas returned by the currently visible `fo:multi-case`.
- Any number of the `fo:multi-case` objects may assign `starting-state` to "show".
- If no `fo:multi-case` has `starting-state` property value of "show", the contents of no `fo:multi-case` should be displayed.
- If no multi-case is displayed, the entire `fo:multi-switch` will effectively be hidden.

## Content Model

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_multi-switch -->
```xml
(multi-case+)
```

## Properties

| Property | Inherited | Conformance Level |
|---|---|---|
| Common Accessibility Properties | N/A | Basic |
| `auto-restore` | no | Extended |
| `id` | N/A | Basic |
| `index-class` | N/A | Extended |
| `index-key` | N/A | Extended |

## Usage Notes

- An `fo:multi-switch` can be used for many interactive tasks, such as table-of-content views, embedding link targets, or generalized (even multi-layered hierarchical) next/previous views.
- Each `fo:multi-case` child specifies a `case-name` and `starting-state`. Set `starting-state="show"` on the initially visible case and `starting-state="hide"` on the others.
- The `auto-restore` property, when set to "true", causes the `fo:multi-switch` to automatically restore its initial state when the user navigates away from the page containing it.
- Nest `fo:multi-toggle` elements within `fo:multi-case` children to provide clickable elements that trigger the switch to a different case.

## Code Samples

No code samples in spec for this formatting object. See the "Expandable/Collapsible Table of Contents" example in the "Dynamic Effects: Link and Multi Formatting Objects" introduction section for a comprehensive demonstration.

## See Also

- [fo:multi-case](fo-multi-case.md) — child formatting object containing each alternative sub-tree
- [fo:multi-toggle](fo-multi-toggle.md) — triggers switching from one multi-case to another
- [fo:basic-link](fo-basic-link.md) — often used within multi-case content for navigation
