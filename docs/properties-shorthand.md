# Shorthand Properties

## Overview

Shorthand properties allow multiple individual properties to be set simultaneously with a single property declaration. In XSL-FO, shorthands are only included in the highest conformance level: "complete." Shorthand properties take a list of subproperty values **or** the value "inherit." One cannot mix "inherit" with other subproperty values as it would not be possible to specify the subproperty to which "inherit" applied.

When a shorthand is specified, it first sets all the individual properties it controls to their initial values, then assigns explicit values given in the declaration. This means that a shorthand effectively resets any previously set individual properties.

<!-- Source: https://www.w3.org/TR/xslfo20/#background -->

## Properties

### background

| Field | Value |
|---|---|
| **Values** | `[<background-color> \|\| <background-image> \|\| <background-repeat> \|\| <background-attachment> \|\| <background-position>] \| inherit` |
| **Initial** | not defined for shorthand properties |
| **Applies to** | all formatting objects that generate areas |
| **Inherited** | No |
| **Conformance** | Complete |

<!-- Source: https://www.w3.org/TR/xslfo20/#background -->

The "background" property is a shorthand property for setting the individual background properties (i.e., `background-color`, `background-image`, `background-repeat`, `background-attachment` and `background-position`) at the same place in the stylesheet.

The "background" property first sets all the individual background properties to their initial values, then assigns explicit values given in the declaration.

**Expands to:** `background-color`, `background-image`, `background-repeat`, `background-attachment`, `background-position-horizontal`, `background-position-vertical`

### background-position

| Field | Value |
|---|---|
| **Values** | `[ [<percentage> \| <length>]{1,2} \| [ [top \| center \| bottom] \|\| [left \| center \| right] ] ] \| inherit` |
| **Initial** | `0% 0%` |
| **Applies to** | all formatting objects that generate areas |
| **Inherited** | No |
| **Conformance** | Complete |

<!-- Source: https://www.w3.org/TR/xslfo20/#background-position -->

If a "background-image" has been specified, this property specifies its initial position. XSL treats this as a shorthand and maps to `background-position-horizontal` and `background-position-vertical`.

Mapping rules:
- If only one percentage or length value is given, it sets the horizontal position only; the vertical position will be 50%.
- If two values are given, the horizontal position comes first.
- Keyword combinations map to percentage pairs (e.g., "top left" = 0% 0%, "center" = 50% 50%, "bottom right" = 100% 100%).

**Expands to:** `background-position-horizontal`, `background-position-vertical`

### border

| Field | Value |
|---|---|
| **Values** | `[ <border-width> \|\| <border-style> \|\| [ <color> \| transparent ] ] \| inherit` |
| **Initial** | see individual properties |
| **Applies to** | all formatting objects that generate areas |
| **Inherited** | No |
| **Conformance** | Complete |

<!-- Source: https://www.w3.org/TR/xslfo20/#border -->

The "border" property is a shorthand property for setting the same width, color, and style for all four borders, top, bottom, left, and right, of a box. Unlike the shorthand "margin" and "padding" properties, the "border" property cannot set different values on the four borders. To do so, one or more of the other border properties must be used.

**Expands to:** `border-top-width`, `border-right-width`, `border-bottom-width`, `border-left-width`, `border-top-style`, `border-right-style`, `border-bottom-style`, `border-left-style`, `border-top-color`, `border-right-color`, `border-bottom-color`, `border-left-color`

### border-bottom

| Field | Value |
|---|---|
| **Values** | `[ <border-width> \|\| <border-style> \|\| [ <color> \| transparent ] ] \| inherit` |
| **Initial** | see individual properties |
| **Applies to** | all formatting objects that generate areas |
| **Inherited** | No |
| **Conformance** | Complete |

<!-- Source: https://www.w3.org/TR/xslfo20/#border-bottom -->

A shorthand property for setting the width, style, and color of the bottom border of a block-area or inline-area.

**Expands to:** `border-bottom-width`, `border-bottom-style`, `border-bottom-color`

### border-color

| Field | Value |
|---|---|
| **Values** | `[ <color> \| transparent ]{1,4} \| inherit` |
| **Initial** | see individual properties |
| **Applies to** | all formatting objects that generate areas |
| **Inherited** | No |
| **Conformance** | Complete |

<!-- Source: https://www.w3.org/TR/xslfo20/#border-color -->

The "border-color" property sets the color of the four borders. It can have from one to four values. If an element's border color is not specified with a "border" property, user agents must use the value of the element's "color" property as the computed value for the border color.

See the "border-width" property for a description of how this property is interpreted when one through four values are provided.

**Expands to:** `border-top-color`, `border-right-color`, `border-bottom-color`, `border-left-color`

### border-left

| Field | Value |
|---|---|
| **Values** | `[ <border-width> \|\| <border-style> \|\| [ <color> \| transparent ] ] \| inherit` |
| **Initial** | see individual properties |
| **Applies to** | all formatting objects that generate areas |
| **Inherited** | No |
| **Conformance** | Complete |

<!-- Source: https://www.w3.org/TR/xslfo20/#border-left -->

A shorthand property for setting the width, style, and color of the left border of a block-area or inline-area.

**Expands to:** `border-left-width`, `border-left-style`, `border-left-color`

### border-right

| Field | Value |
|---|---|
| **Values** | `[ <border-width> \|\| <border-style> \|\| [ <color> \| transparent ] ] \| inherit` |
| **Initial** | see individual properties |
| **Applies to** | all formatting objects that generate areas |
| **Inherited** | No |
| **Conformance** | Complete |

<!-- Source: https://www.w3.org/TR/xslfo20/#border-right -->

A shorthand property for setting the width, style, and color of the right border of a block-area or inline-area.

**Expands to:** `border-right-width`, `border-right-style`, `border-right-color`

### border-spacing

| Field | Value |
|---|---|
| **Values** | `<length> <length>? \| inherit` |
| **Initial** | `0pt` |
| **Applies to** | fo:table |
| **Inherited** | Yes |
| **Conformance** | Complete |

<!-- Source: https://www.w3.org/TR/xslfo20/#border-spacing -->

In the separate borders model, each cell has an individual border. The "border-spacing" property specifies the distance between the borders of adjacent cells. This space is filled with the background of the table element.

If one length is specified, it gives both the horizontal and vertical spacing. If two are specified, the first gives the horizontal spacing and the second the vertical spacing. Lengths may not be negative.

XSL treats this as a shorthand:
- If one value is specified, both "border-separation.block-progression-direction" and "border-separation.inline-progression-direction" are set to that value.
- If two values are specified, "border-separation.block-progression-direction" is set to the second value and "border-separation.inline-progression-direction" is set to the first value.

**Expands to:** `border-separation.block-progression-direction`, `border-separation.inline-progression-direction`

### border-style

| Field | Value |
|---|---|
| **Values** | `<border-style>{1,4} \| inherit` |
| **Initial** | see individual properties |
| **Applies to** | all formatting objects that generate areas |
| **Inherited** | No |
| **Conformance** | Complete |

<!-- Source: https://www.w3.org/TR/xslfo20/#border-style -->

The "border-style" property sets the style of the four borders. It can have from one to four values. See the "border-width" property for a description of how this property is interpreted when one through four values are provided.

**Expands to:** `border-top-style`, `border-right-style`, `border-bottom-style`, `border-left-style`

### border-top

| Field | Value |
|---|---|
| **Values** | `[ <border-width> \|\| <border-style> \|\| [ <color> \| transparent ] ] \| inherit` |
| **Initial** | see individual properties |
| **Applies to** | all formatting objects that generate areas |
| **Inherited** | No |
| **Conformance** | Complete |

<!-- Source: https://www.w3.org/TR/xslfo20/#border-top -->

A shorthand property for setting the width, style, and color of the top border of a block-area or inline-area.

**Expands to:** `border-top-width`, `border-top-style`, `border-top-color`

### border-width

| Field | Value |
|---|---|
| **Values** | `<border-width>{1,4} \| inherit` |
| **Initial** | see individual properties |
| **Applies to** | all formatting objects that generate areas |
| **Inherited** | No |
| **Conformance** | Complete |

<!-- Source: https://www.w3.org/TR/xslfo20/#border-width -->

This property is a shorthand property for setting "border-top-width", "border-right-width", "border-bottom-width", and "border-left-width" at the same place in the stylesheet.

Value interpretation for 1-4 values:
- **One value** -- applies to all sides.
- **Two values** -- the top and bottom borders are set to the first value and the right and left are set to the second.
- **Three values** -- the top is set to the first value, the left and right are set to the second, and the bottom is set to the third.
- **Four values** -- they apply to the top, right, bottom, and left, respectively.

**Expands to:** `border-top-width`, `border-right-width`, `border-bottom-width`, `border-left-width`

### cue

| Field | Value |
|---|---|
| **Values** | `<cue-before> \|\| <cue-after> \| inherit` |
| **Initial** | not defined for shorthand properties |
| **Applies to** | all formatting objects |
| **Inherited** | No |
| **Conformance** | Complete |

<!-- Source: https://www.w3.org/TR/xslfo20/#cue -->

Shorthand for setting `cue-before` and `cue-after` (aural media).

**Expands to:** `cue-before`, `cue-after`

### font

| Field | Value |
|---|---|
| **Values** | `[ [ <font-style> \|\| <font-variant> \|\| <font-weight> ]? <font-size> [ / <line-height>]? <font-family> ] \| caption \| icon \| menu \| message-box \| small-caption \| status-bar \| inherit` |
| **Initial** | see individual properties |
| **Applies to** | all formatting objects that accept text content |
| **Inherited** | Yes |
| **Conformance** | Complete |

<!-- Source: https://www.w3.org/TR/xslfo20/#font -->

The "font" property is, except as described below, a shorthand property for setting "font-style", "font-variant", "font-weight", "font-size", "line-height", and "font-family", at the same place in the stylesheet.

All font-related properties are first reset to their initial values, including those listed in the preceding paragraph plus "font-stretch" and "font-size-adjust". Then, those properties that are given explicit values in the "font" shorthand are set to those values.

XSL modifications: In XSL the "font" property is a pure shorthand property. System font characteristics, such as font-family and font-size, may be obtained by the use of the "system-font" function in the expression language.

**Expands to:** `font-style`, `font-variant`, `font-weight`, `font-size`, `line-height`, `font-family`, `font-stretch`, `font-size-adjust`

### margin

| Field | Value |
|---|---|
| **Values** | `<margin-width>{1,4} \| inherit` |
| **Initial** | not defined for shorthand properties |
| **Applies to** | all formatting objects that generate areas |
| **Inherited** | No |
| **Conformance** | Complete |

<!-- Source: https://www.w3.org/TR/xslfo20/#margin -->

A shorthand property for setting margin-top, margin-right, margin-bottom, and margin-left of a block-area or inline-area.

Value interpretation for 1-4 values:
- **One value** -- applies to all sides.
- **Two values** -- the top and bottom margins are set to the first value and the right and left margins are set to the second.
- **Three values** -- the top is set to the first value, the left and right are set to the second, and the bottom is set to the third.
- **Four values** -- they apply to the top, right, bottom, and left, respectively.

XSL modifications: Margin is provided for compatibility with CSS. Details on the mapping of CSS "margin" properties for XSL are given in the refinement section of the spec.

**Expands to:** `margin-top`, `margin-right`, `margin-bottom`, `margin-left`

### padding

| Field | Value |
|---|---|
| **Values** | `<padding-width>{1,4} \| inherit` |
| **Initial** | not defined for shorthand properties |
| **Applies to** | all formatting objects that generate areas |
| **Inherited** | No |
| **Conformance** | Complete |

<!-- Source: https://www.w3.org/TR/xslfo20/#padding -->

A shorthand property for setting padding-top, padding-bottom, padding-left, and padding-right of a block-area or inline-area.

Value interpretation for 1-4 values:
- **One value** -- applies to all sides.
- **Two values** -- the top and bottom paddings are set to the first value and the right and left paddings are set to the second.
- **Three values** -- the top is set to the first value, the left and right are set to the second, and the bottom is set to the third.
- **Four values** -- they apply to the top, right, bottom, and left, respectively.

The surface color or image of the padding area is specified via the "background" property.

**Expands to:** `padding-top`, `padding-right`, `padding-bottom`, `padding-left`

### page-break-after

| Field | Value |
|---|---|
| **Values** | `auto \| always \| avoid \| left \| right \| inherit` |
| **Initial** | `auto` |
| **Applies to** | block-level formatting objects |
| **Inherited** | No |
| **Conformance** | Complete |

<!-- Source: https://www.w3.org/TR/xslfo20/#page-break-after -->

XSL treats this as a shorthand and maps as follows:

| Value | Expands to |
|---|---|
| `auto` | `break-after="auto"`, `keep-with-next="auto"` |
| `always` | `break-after="page"`, `keep-with-next="auto"` |
| `avoid` | `break-after="auto"`, `keep-with-next="always"` |
| `left` | `break-after="even-page"`, `keep-with-next="auto"` |
| `right` | `break-after="odd-page"`, `keep-with-next="auto"` |

**Expands to:** `break-after`, `keep-with-next`

### page-break-before

| Field | Value |
|---|---|
| **Values** | `auto \| always \| avoid \| left \| right \| inherit` |
| **Initial** | `auto` |
| **Applies to** | block-level formatting objects |
| **Inherited** | No |
| **Conformance** | Complete |

<!-- Source: https://www.w3.org/TR/xslfo20/#page-break-before -->

XSL treats this as a shorthand and maps as follows:

| Value | Expands to |
|---|---|
| `auto` | `break-before="auto"`, `keep-with-previous="auto"` |
| `always` | `break-before="page"`, `keep-with-previous="auto"` |
| `avoid` | `break-before="auto"`, `keep-with-previous="always"` |
| `left` | `break-before="even-page"`, `keep-with-previous="auto"` |
| `right` | `break-before="odd-page"`, `keep-with-previous="auto"` |

**Expands to:** `break-before`, `keep-with-previous`

### page-break-inside

| Field | Value |
|---|---|
| **Values** | `avoid \| auto \| inherit` |
| **Initial** | `auto` |
| **Applies to** | block-level formatting objects |
| **Inherited** | Yes |
| **Conformance** | Complete |

<!-- Source: https://www.w3.org/TR/xslfo20/#page-break-inside -->

XSL treats this as a shorthand and maps as follows:

| Value | Expands to |
|---|---|
| `auto` | `keep-together="auto"` |
| `avoid` | `keep-together="always"` |

**Expands to:** `keep-together`

### pause

| Field | Value |
|---|---|
| **Values** | `[<time> \| <percentage>]{1,2} \| inherit` |
| **Initial** | depends on user agent |
| **Applies to** | all formatting objects |
| **Inherited** | No |
| **Conformance** | Complete |

<!-- Source: https://www.w3.org/TR/xslfo20/#pause -->

Shorthand for setting `pause-before` and `pause-after` (aural media).

**Expands to:** `pause-before`, `pause-after`

### position

| Field | Value |
|---|---|
| **Values** | `static \| relative \| absolute \| fixed \| inherit` |
| **Initial** | `static` |
| **Applies to** | block-level formatting objects |
| **Inherited** | No |
| **Conformance** | Complete |

<!-- Source: https://www.w3.org/TR/xslfo20/#position -->

XSL treats this as a shorthand and maps as follows:

| Value | Expands to |
|---|---|
| `static` | `relative-position="static"`, `absolute-position="auto"` |
| `relative` | `relative-position="relative"`, `absolute-position="auto"` |
| `absolute` | `relative-position="static"`, `absolute-position="absolute"` |
| `fixed` | `relative-position="static"`, `absolute-position="fixed"` |

**Expands to:** `relative-position`, `absolute-position`

### size

| Field | Value |
|---|---|
| **Values** | `<length>{1,2} \| auto \| landscape \| portrait \| inherit` |
| **Initial** | `auto` |
| **Applies to** | fo:simple-page-master |
| **Inherited** | No |
| **Conformance** | Complete |

<!-- Source: https://www.w3.org/TR/xslfo20/#size -->

This property specifies the size and orientation of a page box. This is treated as a CSS shorthand property that is mapped to XSL's "page-height" and "page-width" properties.

- **auto** -- The page box will be set to the size and orientation of the target sheet.
- **landscape** -- Overrides the target's orientation. The page box is the same size as the target, and the longer sides are horizontal.
- **portrait** -- Overrides the target's orientation. The page box is the same size as the target, and the shorter sides are horizontal.
- **\<length\>** -- Length values create an absolute page box. If only one length value is specified, it sets both the width and height of the page box (i.e., the box is a square). Percentage values are not allowed.

**Expands to:** `page-height`, `page-width`

### vertical-align

| Field | Value |
|---|---|
| **Values** | `baseline \| middle \| sub \| super \| text-top \| text-bottom \| <percentage> \| <length> \| top \| bottom \| inherit` |
| **Initial** | `baseline` |
| **Applies to** | inline-level formatting objects |
| **Inherited** | No |
| **Conformance** | Complete |

<!-- Source: https://www.w3.org/TR/xslfo20/#vertical-align -->

XSL treats this as a shorthand and maps as follows:

| Value | alignment-baseline | alignment-adjust | baseline-shift | dominant-baseline |
|---|---|---|---|---|
| `baseline` | baseline | auto | baseline | auto |
| `top` | before-edge | auto | baseline | auto |
| `text-top` | text-before-edge | auto | baseline | auto |
| `middle` | middle | auto | baseline | auto |
| `bottom` | after-edge | auto | baseline | auto |
| `text-bottom` | text-after-edge | auto | baseline | auto |
| `sub` | baseline | auto | sub | auto |
| `super` | baseline | auto | super | auto |
| `<percentage>` | baseline | \<percentage\> | baseline | auto |
| `<length>` | baseline | \<length\> | baseline | auto |

**Expands to:** `alignment-baseline`, `alignment-adjust`, `baseline-shift`, `dominant-baseline`

### white-space

| Field | Value |
|---|---|
| **Values** | `normal \| pre \| nowrap \| inherit` |
| **Initial** | `normal` |
| **Applies to** | block-level formatting objects |
| **Inherited** | Yes |
| **Conformance** | Complete |

<!-- Source: https://www.w3.org/TR/xslfo20/#white-space -->

XSL splits control of white space collapsing, space and linefeed handling, and wrapping into separate properties. The CSS property is treated as a shorthand and maps as follows:

| Value | linefeed-treatment | white-space-collapse | white-space-treatment | wrap-option |
|---|---|---|---|---|
| `normal` | treat-as-space | true | ignore-if-surrounding-linefeed | wrap |
| `pre` | preserve | false | preserve | no-wrap |
| `nowrap` | treat-as-space | true | ignore-if-surrounding-linefeed | no-wrap |

**Expands to:** `linefeed-treatment`, `white-space-collapse`, `white-space-treatment`, `wrap-option`

### xml:lang

| Field | Value |
|---|---|
| **Values** | `<language-country> \| inherit` |
| **Initial** | not defined for shorthand properties |
| **Applies to** | all formatting objects |
| **Inherited** | Yes |
| **Conformance** | Complete |

<!-- Source: https://www.w3.org/TR/xslfo20/#xml.lang -->

Specifies the language and country to be used by the formatter in linguistic services (such as hyphenation) and in the determination of line breaks. The string may be any RFC 3066 code.

XSL treats `xml:lang` as a shorthand and uses it to set the `country` and `language` properties.

Note: In general, linguistic services (line-justification strategy, line-breaking and hyphenation) may depend on a combination of the "language", "script", and "country" properties.

**Expands to:** `language`, `country`

## Code Samples

No code samples in spec for this property group.

## See Also

- [properties-border-padding-background](properties-border-padding-background.md) -- individual border, padding, and background properties
- [properties-font](properties-font.md) -- individual font properties
- [properties-block-level](properties-block-level.md) -- break and keep properties expanded from page-break-* shorthands
- [properties-writing-mode](properties-writing-mode.md) -- direction and unicode-bidi
- [properties-inline-level](properties-inline-level.md) -- baseline alignment properties expanded from vertical-align
