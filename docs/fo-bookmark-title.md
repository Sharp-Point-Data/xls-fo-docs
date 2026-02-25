# fo:bookmark-title

## Summary

The `fo:bookmark-title` formatting object is used to identify, in human readable form, an access point.

The `fo:bookmark-title` is a specialized form of the `fo:inline` with restrictions on the applicable properties and on its content model.

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_bookmark-title -->

## Areas

The `fo:bookmark-title` formatting object generates one or more normal inline-areas. The `fo:bookmark-title` returns these areas.

## Trait Derivation

Even though the `white-space-treatment`, `linefeed-treatment`, and `white-space-collapse` properties are not applicable to `fo:bookmark-title`, the implementation should behave as though these properties applied and had their initial values.

## Constraints

- No area may have more than one normal child area returned by the same `fo:bookmark-title` formatting object.
- The children of each normal area returned by an `fo:bookmark-title` must satisfy the constraints specified in the inline building section.

## Content Model

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_bookmark-title -->
```xml
(#PCDATA)
```

## Properties

| Property | Inherited | Conformance Level |
|---|---|---|
| Common Accessibility Properties | N/A | Basic |
| `color` | yes | Basic |
| `font-style` | yes | Basic |
| `font-weight` | yes | Basic |

Note: The `font-style` value space is limited to "normal" and "italic". The `font-weight` value space is limited to "normal" and "bold".

## Usage Notes

- The `fo:bookmark-title` can only contain text content (#PCDATA); it cannot contain child formatting objects.
- Only a limited set of formatting properties are available: `color`, `font-style` (normal/italic only), and `font-weight` (normal/bold only). This reflects the limited styling capabilities of bookmark panels in typical PDF viewers.
- The `fo:bookmark-title` must appear as the first child of an `fo:bookmark`.

## Code Samples

No code samples in spec for this formatting object.

## See Also

- `fo:bookmark` -- parent formatting object
- `fo:bookmark-tree` -- grandparent containing the bookmark hierarchy
