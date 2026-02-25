# Color-related Properties

## Overview

<!-- Source: https://www.w3.org/TR/xslfo20/#color -->

The color-related properties control foreground color, color profile naming, and rendering intent for color management. The "color" property sets the foreground text color, while "color-profile-name" and "rendering-intent" are used with fo:color-profile for ICC color management workflows, particularly relevant for CMYK output.

## Properties

### color

| Field | Value |
|---|---|
| **Values** | `<color> \| inherit` |
| **Initial** | `depends on user agent` |
| **Applies to** | fo:bidi-override, fo:block, fo:character, fo:initial-property-set, fo:inline, fo:leader, fo:page-number, fo:page-number-citation, fo:page-number-citation-last, fo:table-and-caption, fo:table, fo:table-body, fo:table-header, fo:table-footer, fo:table-row, fo:table-cell, fo:list-block, fo:list-item |
| **Inherited** | Yes |
| **Percentages** | N/A |
| **Media** | visual |

<!-- Source: https://www.w3.org/TR/xslfo20/#color -->

This property describes the foreground color of an element's text content.

- **\<color\>** -- Any valid color specification.

XSL modifications: XSL adds an "rgb-icc" function as a valid value of this property, enabling specification of colors using ICC color profiles. The rgb-icc function takes an sRGB fallback color plus color-profile name and component values.

### color-profile-name

| Field | Value |
|---|---|
| **Values** | `<name> \| inherit` |
| **Initial** | `N/A, value is required` |
| **Applies to** | fo:color-profile |
| **Inherited** | No |
| **Percentages** | N/A |
| **Media** | visual |

<!-- Source: https://www.w3.org/TR/xslfo20/#color-profile-name -->

Specifies the name of a color-profile for internal references.

- **\<name\>** -- Specifies the name of a color-profile for internal references. This name is used within the "rgb-icc" function to reference the color profile declared by the fo:color-profile formatting object.

### rendering-intent

| Field | Value |
|---|---|
| **Values** | `auto \| perceptual \| relative-colorimetric \| saturation \| absolute-colorimetric \| inherit` |
| **Initial** | `auto` |
| **Applies to** | fo:color-profile |
| **Inherited** | No |
| **Percentages** | N/A |
| **Media** | visual |

<!-- Source: https://www.w3.org/TR/xslfo20/#rendering-intent -->

"rendering-intent" permits the specification of a color-profile rendering intent other than the default. "rendering-intent" is applicable primarily to color-profiles corresponding to CMYK color spaces. The different options cause different methods to be used for translating colors to the color gamut of the target rendering device.

Values have the following meanings:

- **auto** -- This is the default behavior. The User Agent determines the best intent based on the content type. For image content containing an embedded profile, it shall be assumed that the intent specified within the profile is the desired intent. Otherwise, the user agent shall use the current profile and force the intent, overriding any intent that might be stored in the profile itself.
- **perceptual** -- This method, often the preferred choice for images, preserves the relationship between colors. It attempts to maintain relative color values among the pixels as they are mapped to the target device gamut. Sometimes pixel values that were originally within the target device gamut are changed in order to avoid hue shifts and discontinuities and to preserve as much as possible the overall appearance of the scene.
- **relative-colorimetric** -- Leaves colors that fall inside the gamut unchanged. This method usually converts out of gamut colors to colors that have the same lightness but fall just inside the gamut.
- **saturation** -- Preserves the relative saturation (chroma) values of the original pixels. Out of gamut colors are converted to colors that have the same saturation but fall just inside the gamut.
- **absolute-colorimetric** -- Disables white point matching when converting colors. This option is generally not recommended.

## Code Samples

No code samples in spec for this property group.

## See Also

- [fo-color-profile.md](fo-color-profile.md) -- fo:color-profile uses color-profile-name and rendering-intent
- [fo-block.md](fo-block.md) -- fo:block uses color for text foreground
- [fo-inline.md](fo-inline.md) -- fo:inline uses color for text foreground
- [properties-character.md](properties-character.md) -- text-decoration color derives from the color property
