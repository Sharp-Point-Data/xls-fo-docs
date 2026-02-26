# fo:color-profile

## Summary

The `fo:color-profile` formatting object is used to declare an ICC Color Profile for a stylesheet. The color-profile is referenced via the name specified in the `color-profile-name` property. The color-profile is identified by the URI specified in the `src` property value. This URI may identify an internally recognized color-profile or it may point to an ICC Color Profile encoding that should be loaded and interpreted.

When the color-profile is referenced (e.g., via the `rgb-icc` function), the following rules are used:

1. If the color-profile is available, the color value identified from the color-profile should be used.
2. If the color-profile is not available, the sRGB fallback must be used.

## Areas

The `fo:color-profile` formatting object does not generate or return any areas.

## Constraints

None.

## Content Model

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_color-profile -->
```xml
EMPTY
```

The `fo:color-profile` element has no child elements.

## Properties

| Property | Type | Initial Value | Inherited | Conformance Level |
|---|---|---|---|---|
| src | `<uri-specification> \| inherit` | none, value required | no | Basic |
| color-profile-name | `<name> \| inherit` | N/A, value is required | no | Basic |
| rendering-intent | `auto \| perceptual \| relative-colorimetric \| saturation \| absolute-colorimetric \| inherit` | auto | no | Basic |

### Property Details

- **src**: Specifies the URI of the ICC Color Profile. This URI identifies either an internally recognized color-profile or points to an ICC Color Profile encoding to be loaded.
- **color-profile-name**: Specifies the name used to reference this color-profile internally. This name is used in the `rgb-icc()` function and other color-profile references.
- **rendering-intent**: Specifies the color-profile rendering intent. This is primarily applicable to color-profiles corresponding to CMYK color spaces. The different options cause different methods to be used for translating colors to the color gamut of the target rendering device.

## Usage Notes

The `fo:color-profile` element must appear as a child of `fo:declarations`. Each `fo:color-profile` declares a named color profile that can be referenced elsewhere in the document using the `rgb-icc()` color function.

A typical use is to declare a CMYK color profile for print-quality color output. The `color-profile-name` provides the local name used to reference the profile, while `src` provides the URI to the actual ICC profile data.

The `rendering-intent` property controls how colors are mapped between different color spaces:
- `auto` -- the User Agent determines the best intent based on content type
- `perceptual` -- preserves relationships between colors; preferred for images
- `relative-colorimetric` -- leaves in-gamut colors unchanged; maps out-of-gamut colors to nearest in-gamut equivalents
- `saturation` -- preserves saturation of colors
- `absolute-colorimetric` -- leaves in-gamut colors unchanged; clips out-of-gamut colors

## Code Samples

No code samples in spec for this formatting object. The spec section contains only the content model declaration shown above.

## See Also

- [fo:declarations](fo-declarations.md) — parent container for color profile declarations
- [fo:root](fo-root.md) — top-level element that contains fo:declarations
