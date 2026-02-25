# Writing-Mode-Related Properties

## Overview

The properties in this section control the setting of the inline-progression-direction, the block-progression-direction, and the orientation of glyphs that are placed on a baseline in the inline-progression-direction. The `writing-mode` property sets both the inline-progression-direction and the block-progression-direction. The `direction` property, controlled by the `unicode-bidi` property, only affects text in which the orientation of the glyphs is perpendicular to the dominant-baseline.

The glyph orientation properties (`glyph-orientation-horizontal` and `glyph-orientation-vertical`) set the orientation of the glyph relative to the default glyph orientation. The default orientation for glyphs is with the top of the glyph oriented toward the top of the reference area of which the glyph area is a descendant. Glyphs oriented at 90 or -90 degrees from the reference-orientation are said to be "rotated glyphs." Glyphs oriented 180 degrees from the reference-orientation are said to be "inverted glyphs."

<!-- Source: https://www.w3.org/TR/xslfo20/#writing-mode-related -->

## Properties

### writing-mode

| Field | Value |
|---|---|
| **Values** | `lr-tb \| rl-tb \| tb-rl \| tb-lr \| bt-lr \| bt-rl \| lr-bt \| rl-bt \| lr-alternating-rl-bt \| lr-alternating-rl-tb \| lr-inverting-rl-bt \| lr-inverting-rl-tb \| tb-lr-in-lr-pairs \| lr \| rl \| tb \| inherit` |
| **Initial** | `lr-tb` |
| **Applies to** | fo:page-sequence, fo:simple-page-master, fo:region-body, fo:region-before, fo:region-after, fo:region-start, fo:region-end, fo:block-container, fo:inline-container, fo:table |
| **Inherited** | Yes (see prose) |
| **Conformance** | Basic |

<!-- Source: https://www.w3.org/TR/xslfo20/#writing-mode -->

The writing-mode trait on an area is indirectly derived from the "writing-mode" property on the formatting object that generates the area or the formatting object ancestors of that formatting object. The "writing-mode" property applies only to formatting objects that set up a reference-area. Each value of writing-mode sets all three of the direction traits indicated in each of the value descriptions on the reference-area.

Values have the following meanings:

- **lr-tb** -- Inline components and text within a line are written left-to-right. Lines and blocks are placed top-to-bottom. Typically the writing-mode for normal "alphabetic" text. Establishes: inline-progression-direction to left-to-right, block-progression-direction to top-to-bottom, shift-direction to bottom-to-top.
- **rl-tb** -- Inline components and text within a line are written right-to-left. Lines and blocks are placed top-to-bottom. Typically used in Arabic and Hebrew text. Establishes: inline-progression-direction to right-to-left, block-progression-direction to top-to-bottom, shift-direction to bottom-to-top.
- **tb-rl** -- Inline components and text within a line are written top-to-bottom. Lines and blocks are placed right-to-left. Typically used in Chinese and Japanese text. Establishes: inline-progression-direction to top-to-bottom, block-progression-direction to right-to-left, shift-direction to left-to-right.
- **tb-lr** -- Inline components and text within a line are stacked top-to-bottom. Lines and blocks are stacked left-to-right. Establishes: inline-progression-direction to top-to-bottom, block-progression-direction to left-to-right, shift-direction to right-to-left.
- **bt-lr** -- Inline components and text within a line are stacked bottom-to-top. Lines and blocks are stacked left-to-right. Establishes: inline-progression-direction to bottom-to-top, block-progression-direction to left-to-right, shift-direction to right-to-left.
- **bt-rl** -- Inline components and text within a line are stacked bottom-to-top. Lines and blocks are stacked right-to-left. Establishes: inline-progression-direction to bottom-to-top, block-progression-direction to right-to-left, shift-direction to left-to-right.
- **lr-bt** -- Inline components and text within a line are stacked left-to-right. Lines and blocks are stacked bottom-to-top. Establishes: inline-progression-direction to left-to-right, block-progression-direction to bottom-to-top, shift-direction to bottom-to-top.
- **rl-bt** -- Inline components and text within a line are stacked right-to-left. Lines and blocks are stacked bottom-to-top. Establishes: inline-progression-direction to right-to-left, block-progression-direction to bottom-to-top, shift-direction to bottom-to-top.
- **lr-alternating-rl-bt** -- Inline components and text within the first line are stacked left-to-right, within the second line they are stacked right-to-left; continuing in alternation. Lines and blocks are stacked bottom-to-top. Inline-progression-direction alternates left-to-right for odd-numbered lines and right-to-left for even-numbered lines.
- **lr-alternating-rl-tb** -- Same as lr-alternating-rl-bt but lines and blocks are stacked top-to-bottom.
- **lr-inverting-rl-bt** -- Inline components and text within the first line are stacked left-to-right, within the second line they are inverted and stacked right-to-left; continuing in alternation. Lines and blocks are stacked bottom-to-top. Shift-direction alternates between bottom-to-top for odd-numbered lines and top-to-bottom for even-numbered lines.
- **lr-inverting-rl-tb** -- Same as lr-inverting-rl-bt but lines and blocks are stacked top-to-bottom.
- **tb-lr-in-lr-pairs** -- Text is written in two character, left-to-right, pairs. The pairs are then stacked top-to-bottom to form a line. Lines and blocks are stacked left-to-right. Establishes: inline-progression-direction to top-to-bottom, block-progression-direction to left-to-right, shift-direction to right-to-left.
- **lr** -- Shorthand for lr-tb.
- **rl** -- Shorthand for rl-tb.
- **tb** -- Shorthand for tb-rl.

Note: To change the "writing-mode" within an `fo:flow` or `fo:static-content`, either the `fo:block-container` or the `fo:inline-container`, as appropriate, should be used. If one only wishes to change the inline-progression-direction to override the Unicode BIDI-rule, one need not use an `fo:inline-container`. Instead, one may use the "direction" property on the `fo:bidi-override`.

Implementations must support at least one of the "writing-mode" values defined in this Recommendation.

### direction

| Field | Value |
|---|---|
| **Values** | `ltr \| rtl \| inherit` |
| **Initial** | `ltr` |
| **Applies to** | all formatting objects (but see prose) |
| **Inherited** | Yes |
| **Conformance** | Extended |

<!-- Source: https://www.w3.org/TR/xslfo20/#direction -->

This property specifies the base writing direction of blocks and the direction of embeddings and overrides (see Unicode TR #9) for the Unicode BIDI algorithm. In addition, it specifies the direction of table column layout, the direction of horizontal overflow, and the position of an incomplete last line in a block in case of `text-align: justify`.

- **ltr** -- Left to right direction.
- **rtl** -- Right to left direction.

For the "direction" property to have any effect on inline-level elements, the "unicode-bidi" property's value must be "embed" or "override."

XSL modifications:
- The "direction" property only affects text in which the orientation of the glyphs is perpendicular to the inline-progression-direction. Therefore, vertical ideographic text with the initial value for "glyph-orientation-vertical" is not affected by this property; vertical text for which the "glyph-orientation-vertical" property has the value of "90" or "-90" degrees is affected.
- The "writing-mode" property establishes both the block-progression-direction and the inline-progression-direction. The "direction" property only changes the inline-progression-direction and is used primarily for formatting objects that generate inline-areas that are not also reference areas. Use of the "direction" property for other formatting objects is deprecated in this specification.
- When mapping CSS to XSL, the XSL "writing-mode" property should be used rather than the "direction" property for all block-level directionality control.

### unicode-bidi

| Field | Value |
|---|---|
| **Values** | `normal \| embed \| bidi-override \| inherit` |
| **Initial** | `normal` |
| **Applies to** | all formatting objects (but see prose) |
| **Inherited** | No |
| **Conformance** | Extended |

<!-- Source: https://www.w3.org/TR/xslfo20/#unicode-bidi -->

Values have the following meanings:

- **normal** -- The element does not open an additional level of embedding with respect to the bidirectional algorithm. For inline-level elements, implicit reordering works across element boundaries.
- **embed** -- If the element is inline-level, this value opens an additional level of embedding with respect to the bidirectional algorithm. The direction of this embedding level is given by the "direction" property. Inside the element, reordering is done implicitly. This corresponds to adding a LRE (U+202A; for "direction: ltr") or RLE (U+202B; for "direction: rtl") at the start of the element and a PDF (U+202C) at the end of the element.
- **bidi-override** -- If the element is inline-level or a block-level element that contains only inline-level elements, this creates an override. This means that inside the element, reordering is strictly in sequence according to the "direction" property; the implicit part of the bidirectional algorithm is ignored. This corresponds to adding a LRO (U+202D; for "direction: ltr") or RLO (U+202E; for "direction: rtl") at the start of the element and a PDF (U+202C) at the end of the element.

XSL modifications: In Unicode 3.0, the Unicode Consortium has increased the limit of the levels of embedding to 61 (definition BD2 in Unicode TR #9).

Fallback: If it is not possible to present the characters in the correct order, then the User Agent should display either a "missing character" glyph or display some indication that the content cannot be correctly rendered.

### glyph-orientation-horizontal

| Field | Value |
|---|---|
| **Values** | `<angle> \| inherit` |
| **Initial** | `0deg` |
| **Applies to** | character-level formatting objects |
| **Inherited** | Yes |
| **Conformance** | Extended |

<!-- Source: https://www.w3.org/TR/xslfo20/#glyph-orientation-horizontal -->

This property specifies the orientation of glyphs relative to the path direction specified by the "writing-mode". This property is applied only to text written in a horizontal writing-mode.

The angle is restricted to 0, 90, 180, and 270 degrees. The User Agent shall round the value of the angle to the closest of the permitted values.

- **0deg** -- All glyphs are set with the top of the glyphs toward the top of the reference-area. The top of the reference-area is defined by the reference-area's reference-orientation.
- **90deg** -- Indicates a rotation of 90-degrees clockwise from the "0deg" orientation.

The value of this property affects both the alignment and width of the glyph-areas generated for the affected glyphs. If a glyph is oriented so that it is not perpendicular to the dominant-baseline, then the vertical alignment-point of the rotated glyph is aligned with the alignment-baseline appropriate to that glyph. The width of the glyph-area is determined from the vertical width font characteristic for the glyph.

### glyph-orientation-vertical

| Field | Value |
|---|---|
| **Values** | `auto \| <angle> \| inherit` |
| **Initial** | `auto` |
| **Applies to** | character-level formatting objects |
| **Inherited** | Yes |
| **Conformance** | Extended |

<!-- Source: https://www.w3.org/TR/xslfo20/#glyph-orientation-vertical -->

This property specifies the orientation of glyphs relative to the path direction specified by the writing-mode. This property is applied only to text written with an inline-progression-direction top-to-bottom or bottom-to-top. Its most common usage is to differentiate between the preferred orientation of alphabetic text in vertically written Japanese documents (glyph-orientation="auto") vs. the orientation of alphabetic text in western signage and advertising (glyph-orientation="0deg").

- **auto** -- Fullwidth ideographic and fullwidth Latin text (excluding ideographic punctuation) will be set with a glyph-orientation of 0-degrees. Ideographic punctuation and other ideographic characters having alternate horizontal and vertical forms will use the vertical form of the glyph. Text which is not fullwidth will be set with a glyph-orientation of 90-degrees. This reorientation rule applies only to the first-level non-ideographic text. All further embedding of writing-modes or BIDI processing will be based on the first-level rotation.
- **\<angle\>** -- The angle is restricted to 0, 90, 180, and 270 degrees. The User Agent shall round the value of the angle to the closest of the permitted values. A value of "0deg" indicates that all glyphs are set with the top of the glyphs toward the top of the reference-area. A value of "90deg" indicates a rotation of 90-degrees clockwise from the "0deg" orientation.

The value of this property affects both the alignment and width of the glyph-areas generated for the affected glyphs. If a glyph is oriented so that it is perpendicular to the dominant-baseline, then the horizontal alignment-point of the rotated glyph is aligned with the alignment-baseline appropriate to that glyph. The width of the glyph-area is determined from the horizontal width font characteristic for the glyph.

### text-altitude

| Field | Value |
|---|---|
| **Values** | `use-font-metrics \| <length> \| <percentage> \| inherit` |
| **Initial** | `use-font-metrics` |
| **Applies to** | fo:block, fo:character, fo:leader |
| **Inherited** | No |
| **Conformance** | Extended |

<!-- Source: https://www.w3.org/TR/xslfo20/#text-altitude -->

Specifies the "height" to be used for the ascent above the dominant baseline.

- **use-font-metrics** -- Uses a value for the "height" of the font above the dominant baseline, calculated as the distance between the text-before baseline and the dominant baseline, obtained from the nominal font for `fo:block`, `fo:character`, and `fo:leader` when the leader-pattern does not have the value "use-content". For `fo:leader`, when the leader-pattern has the value "use-content", it is obtained from the nominal font of the first child. Conforming implementations may choose as an actual value any value in the range of text-altitudes used by fonts of the same script and font-size, instead of the values from the font data.
- **\<length\>** -- Replaces the "height" value found in the font.

### text-depth

| Field | Value |
|---|---|
| **Values** | `use-font-metrics \| <length> \| <percentage> \| inherit` |
| **Initial** | `use-font-metrics` |
| **Applies to** | fo:block, fo:character, fo:leader |
| **Inherited** | No |
| **Conformance** | Extended |

<!-- Source: https://www.w3.org/TR/xslfo20/#text-depth -->

Specifies the "depth" to be used for the descent below the dominant baseline.

- **use-font-metrics** -- Uses a value for the "depth" of the font below the baseline, calculated as the distance between the dominant baseline and the text-after baseline, obtained from the nominal font for `fo:block`, `fo:character`, and `fo:leader` when the leader-pattern does not have the value "use-content". For `fo:leader`, when the leader-pattern has the value "use-content", it is obtained from the nominal font of the first child. Conforming implementations may choose as an actual value any value in the range of text-depths used by fonts of the same script and font-size, instead of the values from the font data.
- **\<length\>** -- Replaces the "depth" value found in the font.

## Code Samples

No code samples in spec for this property group.

## See Also

- [guide-writing-modes](guide-writing-modes.md) -- guide to writing mode concepts
- [guide-bidi](guide-bidi.md) -- guide to bidirectional text
- [fo-block-container](fo-block-container.md) -- can override writing-mode
- [fo-inline-container](fo-inline-container.md) -- can override writing-mode
- [fo-bidi-override](fo-bidi-override.md) -- explicit bidi control
- [properties-inline-level](properties-inline-level.md) -- baseline alignment properties
