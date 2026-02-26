# fo:basic-link

## Summary

The `fo:basic-link` is used for representing the start resource of a simple one-directional single-target link. The object allows for traversal to the destination resource, typically by clicking on any of the containing areas.

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_basic-link -->

## Areas

The `fo:basic-link` formatting object generates one or more normal inline-areas. The `fo:basic-link` returns these areas, together with any normal block-areas, page-level-out-of-line areas, and reference-level-out-of-line areas returned by the children of the `fo:basic-link`.

An `fo:basic-link` can be enclosed in an `fo:block` to create a display area.

## Constraints

- One of the `external-destination` and `internal-destination` properties should be specified. If both are specified, the system may either report it as an error, or use the `internal-destination` property.
- No area may have more than one normal child area returned by the same `fo:basic-link` formatting object.
- The children of each normal area returned by an `fo:basic-link` must satisfy the constraints specified in the inline building section of the spec.

## Content Model

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_basic-link -->
```xml
(#PCDATA|%inline;|%block;)*
```

In addition this formatting object may have a sequence of zero or more `fo:marker`s as its initial children.

## Properties

| Property | Inherited | Conformance Level |
|---|---|---|
| Common Accessibility Properties | N/A | Basic |
| Common Aural Properties | N/A | Extended |
| Common Border, Padding, and Background Properties | N/A | Basic |
| Common Margin Properties - Inline | N/A | Basic |
| Common Relative Position Properties | N/A | Extended |
| `alignment-adjust` | no | Extended |
| `alignment-baseline` | no | Extended |
| `baseline-shift` | no | Extended |
| `destination-placement-offset` | no | Extended |
| `dominant-baseline` | no | Extended |
| `external-destination` | no | Basic |
| `id` | N/A | Basic |
| `index-class` | N/A | Extended |
| `index-key` | N/A | Extended |
| `indicate-destination` | no | Extended |
| `internal-destination` | no | Basic |
| `keep-together` | no | Extended |
| `keep-with-next` | no | Extended |
| `keep-with-previous` | no | Extended |
| `line-height` | yes | Basic |
| `show-destination` | no | Extended |
| `target-processing-context` | no | Extended |
| `target-presentation-context` | no | Extended |
| `target-stylesheet` | no | Extended |

## Usage Notes

- Use `internal-destination` to link to an element within the same document by specifying its `id` value.
- Use `external-destination` to link to an external resource by specifying a URI. The URI should be enclosed in `url()`.
- The `show-destination` property controls whether the destination replaces the current display or opens in a new window.
- The `indicate-destination` property can be used to visually highlight the destination when the link is traversed.
- The `destination-placement-offset` property specifies where on the destination page the view should be positioned after link traversal.
- The `fo:basic-link` can contain both inline and block content, making it suitable for wrapping paragraphs, images, or mixed content as clickable links.

## Code Samples

No code samples in spec for this formatting object. See the "Dynamic Effects: Link and Multi Formatting Objects" introduction section for examples demonstrating `fo:basic-link` usage within `fo:multi-switch` and `fo:multi-properties` contexts.

## See Also

- [fo:multi-switch](fo-multi-switch.md) — enables switching between alternative sub-trees, often combined with links
- [fo:multi-properties](fo-multi-properties.md) — enables property switching based on active state (link, visited, hover, etc.)
- [fo:multi-toggle](fo-multi-toggle.md) — triggers switching between multi-case alternatives
