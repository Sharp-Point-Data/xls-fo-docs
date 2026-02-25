# Character Properties

## Overview

<!-- Source: https://www.w3.org/TR/xslfo20/#character -->

The character properties control the presentation of individual characters and the spacing between them. They include the character value itself, letter and word spacing, text decoration (underline, overline, strikethrough), text shadow effects, text transformation (capitalization), glyph orientation for vertical writing modes, and control over whether a character is treated as a word space.

## Properties

### character

| Field | Value |
|---|---|
| **Values** | `<character>` |
| **Initial** | `N/A, value is required` |
| **Applies to** | fo:character |
| **Inherited** | No, a value is required |
| **Percentages** | N/A |
| **Media** | visual |

<!-- Source: https://www.w3.org/TR/xslfo20/#character -->

Specifies the Unicode character to be presented.

- **\<character\>** -- Specifies the Unicode character to be presented.

### font-variant

| Field | Value |
|---|---|
| **Values** | `normal \| small-caps \| inherit` |
| **Initial** | `normal` |
| **Applies to** | fo:block, fo:character, fo:initial-property-set, fo:inline, fo:page-number, fo:page-number-citation, fo:page-number-citation-last |
| **Inherited** | Yes |
| **Percentages** | N/A |
| **Media** | visual |

<!-- Source: https://www.w3.org/TR/xslfo20/#font-variant -->

In a small-caps font, the glyphs for lowercase letters look similar to the uppercase ones, but in a smaller size and with slightly different proportions. The "font-variant" property requests such a font for bicameral (having two cases, as with Roman script). This property has no visible effect for scripts that are unicameral (having only one case, as with most of the world's writing systems).

Values have the following meanings:

- **normal** -- Specifies a font that is not labeled as a small-caps font.
- **small-caps** -- Specifies a font that is labeled as a small-caps font. If a genuine small-caps font is not available, user agents should simulate a small-caps font, for example by taking a normal font and replacing the lowercase letters by scaled uppercase characters. As a last resort, unscaled uppercase letter glyphs in a normal font may replace glyphs in a small-caps font so that the text appears in all uppercase letters.

Insofar as this property causes text to be transformed to uppercase, the same considerations as for "text-transform" apply.

XSL modifications: XSL incorporates the following text from CSS2 15.5 as part of the property definition. "normal" matches a font not labeled as "small-caps"; "small-caps" matches (1) a font labeled as "small-caps", (2) a font in which the small caps are synthesized, or (3) a font where all lowercase letters are replaced by uppercase letters. A small-caps font may be synthesized by electronically scaling uppercase letters from a normal font.

### glyph-orientation-horizontal

| Field | Value |
|---|---|
| **Values** | `<angle> \| inherit` |
| **Initial** | `0deg` |
| **Applies to** | fo:character |
| **Inherited** | Yes |
| **Percentages** | N/A |
| **Media** | visual |

<!-- Source: https://www.w3.org/TR/xslfo20/#glyph-orientation-horizontal -->

This property specifies the orientation of glyphs relative to the path direction specified by the "writing-mode". This property is applied only to text written in a horizontal writing-mode.

Values have the following meanings:

- **\<angle\>** -- The angle is restricted to 0, 90, 180, and 270 degrees. The User Agent shall round the value of the angle to the closest of the permitted values. A value of "0deg" indicates that all glyphs are set with the top of the glyphs toward the top of the reference-area. The top of the reference-area is defined by the reference-area's reference-orientation. A value of "90deg" indicates a rotation of 90-degrees clockwise from the "0deg" orientation.

The value of this property affects both the alignment and width of the glyph-areas generated for the affected glyphs. If a glyph is oriented so that it is not perpendicular to the dominant-baseline, then the vertical alignment-point of the rotated glyph is aligned with the alignment-baseline appropriate to that glyph. The width of the glyph-area is determined from the vertical width font characteristic for the glyph.

### glyph-orientation-vertical

| Field | Value |
|---|---|
| **Values** | `auto \| <angle> \| inherit` |
| **Initial** | `auto` |
| **Applies to** | fo:character |
| **Inherited** | Yes |
| **Percentages** | N/A |
| **Media** | visual |

<!-- Source: https://www.w3.org/TR/xslfo20/#glyph-orientation-vertical -->

This property specifies the orientation of glyphs relative to the path direction specified by the writing-mode. This property is applied only to text written with an inline-progression-direction top-to-bottom or bottom-to-top.

Its most common usage is to differentiate between the preferred orientation of alphabetic text in vertically written Japanese documents (glyph-orientation="auto") vs. the orientation of alphabetic text in western signage and advertising (glyph-orientation="0deg").

Values have the following meanings:

- **auto** -- Fullwidth ideographic and fullwidth Latin text (excluding ideographic punctuation) will be set with a glyph-orientation of 0-degrees. Ideographic punctuation and other ideographic characters having alternate horizontal and vertical forms will use the vertical form of the glyph. Text which is not fullwidth will be set with a glyph-orientation of 90-degrees. This reorientation rule applies only to the first-level non-ideographic text. All further embedding of writing-modes or BIDI processing will be based on the first-level rotation.
- **\<angle\>** -- The angle is restricted to 0, 90, 180, and 270 degrees. The User Agent shall round the value of the angle to the closest of the permitted values. A value of "0deg" indicates that all glyphs are set with the top of the glyphs toward the top of the reference-area. A value of "90deg" indicates a rotation of 90-degrees clockwise from the "0deg" orientation.

The value of this property affects both the alignment and width of the glyph-areas generated for the affected glyphs. If a glyph is oriented so that it is perpendicular to the dominant-baseline, then the horizontal alignment-point of the rotated glyph is aligned with the alignment-baseline appropriate to that glyph. The width of the glyph-area is determined from the horizontal width font characteristic for the glyph.

### letter-spacing

| Field | Value |
|---|---|
| **Values** | `normal \| <length> \| <space> \| inherit` |
| **Initial** | `normal` |
| **Applies to** | fo:block, fo:character, fo:initial-property-set, fo:inline, fo:page-number, fo:page-number-citation, fo:page-number-citation-last |
| **Inherited** | Yes |
| **Percentages** | N/A |
| **Media** | visual |

<!-- Source: https://www.w3.org/TR/xslfo20/#letter-spacing -->

This property specifies inter-character space in addition to the default space between characters. Values may be negative. Note: an implementation may limit the values, for example based on language and script, or on font format or output device type, or for other reasons.

Values have the following meanings:

- **normal** -- The spacing is the normal spacing for the current font. This value allows the user agent to alter the space between characters in order to justify text.
- **\<length\>** -- This value indicates inter-character space in addition to the default space between characters. Values may be negative, but there may be implementation-specific limits. User agents may not further increase or decrease the inter-character space in order to justify text.
- **\<space\>** -- (XSL extension) This allows the user to specify a range of adjustments in addition to the default space between characters. The minimum and maximum values specify the limits of the adjustment.

Character-spacing algorithms are user agent dependent. Character spacing may also be influenced by justification (see the "text-align" property).

When the resultant space between two characters is not the same as the default space, user agents should not use ligatures.

Default space between characters is defined to be 0pt, i.e., glyph-areas stacked with no extra space between the allocation-rectangles of the glyph-areas.

For an fo:character that in the Unicode database is classified as "Alphabetic", unless the treat-as-word-space trait has the value "true", the space-start and space-end traits are each set to a value as follows:

- For "normal": .optimum = "the normal spacing for the current font" / 2, .maximum = auto, .minimum = auto, .precedence = force, and .conditionality = discard. A value of auto for a component implies that the limits are User Agent specific.
- For a \<length\>: .optimum = \<length\> / 2, .maximum = .optimum, .minimum = .optimum, .precedence = force, and .conditionality = discard.
- For a \<space\>: a value that is half the value of the "letter-spacing" property for the numeric components and the value for the .precedence and .conditionality components. The initial values for .precedence is "force" and for .conditionality "discard".

The CSS statement that "Conforming user agents may consider the value of the 'letter-spacing' property to be 'normal'." does not apply in XSL, if the User Agent implements the "Extended" property set.

### suppress-at-line-break

| Field | Value |
|---|---|
| **Values** | `auto \| suppress \| retain \| inherit` |
| **Initial** | `auto` |
| **Applies to** | fo:character |
| **Inherited** | No |
| **Percentages** | N/A |
| **Media** | visual |

<!-- Source: https://www.w3.org/TR/xslfo20/#suppress-at-line-break -->

This property applies only to fo:character and determines whether the character's representation shall be suppressed when it would occur adjacent to a line break. Multiple characters may be so suppressed.

Values have the following meanings:

- **auto** -- The value of this property is determined by the Unicode value of the object's character property. The character at code point U+0020 is treated as if 'suppress' had been specified. All other characters are treated as if 'retain' had been specified. This value does not automatically suppress the presentation of the non-breaking-space (U+00A0), the fixed spaces (U+2000 through U+200A), or the ideographic-space (U+3000).
- **suppress** -- The glyph area generated by the fo:character is eligible to be suppressed at the start or end of a line-area depending on the white-space-treatment property.
- **retain** -- The glyph area generated by the fo:character shall be placed in the area tree whether or not it is first or last in a line-area.

### text-decoration

| Field | Value |
|---|---|
| **Values** | `none \| [ [ underline \| no-underline ] \|\| [ overline \| no-overline ] \|\| [ line-through \| no-line-through ] \|\| [ blink \| no-blink ] ] \| inherit` |
| **Initial** | `none` |
| **Applies to** | fo:block, fo:character, fo:initial-property-set, fo:inline, fo:page-number, fo:page-number-citation, fo:page-number-citation-last |
| **Inherited** | No, but see prose |
| **Percentages** | N/A |
| **Media** | visual |

<!-- Source: https://www.w3.org/TR/xslfo20/#text-decoration -->

This property describes decorations that are added to the text of an element. If the property is specified for a block-level element, it affects all inline-level descendants of the element. If it is specified for (or affects) an inline-level element, it affects all boxes generated by the element.

Values have the following meanings:

- **none** -- Produces no text decoration.
- **underline** -- Each line of text is underlined.
- **overline** -- Each line of text has a line above it.
- **line-through** -- Each line of text has a line through the middle.
- **blink** -- Text blinks (alternates between visible and invisible). Conforming user agents are not required to support this value.
- **no-underline** -- (XSL extension) Turns off underlining, if any.
- **no-overline** -- (XSL extension) Turns off overlining, if any.
- **no-line-through** -- (XSL extension) Turns off line-through, if any.
- **no-blink** -- (XSL extension) Turns off blinking, if any.

The color(s) required for the text decoration should be derived from the "color" property value.

This property is not inherited, but descendant boxes of a block box should be formatted with the same decoration (e.g., they should all be underlined). The color of decorations should remain the same even if descendant elements have different "color" values.

XSL modifications: The placement of the underline depends on whether the "inline-progression-direction" is oriented horizontally or vertically and on the "language" property. For horizontal text the underline is placed below the text. For vertical text the placement depends on the value of the "language" property.

### text-shadow

| Field | Value |
|---|---|
| **Values** | `none \| [<color> \|\| <length> <length> <length>? ,]* [<color> \|\| <length> <length> <length>?] \| inherit` |
| **Initial** | `none` |
| **Applies to** | fo:block, fo:character, fo:initial-property-set, fo:inline, fo:page-number, fo:page-number-citation, fo:page-number-citation-last |
| **Inherited** | No, see prose |
| **Percentages** | N/A |
| **Media** | visual |

<!-- Source: https://www.w3.org/TR/xslfo20/#text-shadow -->

This property accepts a comma-separated list of shadow effects to be applied to the text of the element. The shadow effects are applied in the order specified and may thus overlay each other, but they will never overlay the text itself. Shadow effects do not alter the size of a box, but may extend beyond its boundaries.

Each shadow effect must specify a shadow offset and may optionally specify a blur radius and a shadow color:

- A shadow offset is specified with two "length" values that indicate the distance from the text. The first length value specifies the horizontal distance to the right of the text. A negative horizontal length value places the shadow to the left of the text. The second length value specifies the vertical distance below the text. A negative vertical length value places the shadow above the text.
- A blur radius may optionally be specified after the shadow offset. The blur radius is a length value that indicates the boundaries of the blur effect. The exact algorithm for computing the blur effect is not specified.
- A color value may optionally be specified before or after the length values of the shadow effect. The color value will be used as the basis for the shadow effect. If no color is specified, the value of the "color" property will be used instead.

XSL modifications: The "text-shadow" property is not inherited; it is converted into a rendering trait. This rendering trait specifies that a rendering effect is to be applied, collectively, to the glyph images within the area forest returned by the children of the formatting object on which the property is specified.

### text-transform

| Field | Value |
|---|---|
| **Values** | `capitalize \| uppercase \| lowercase \| none \| inherit` |
| **Initial** | `none` |
| **Applies to** | fo:block, fo:character, fo:initial-property-set, fo:inline, fo:page-number, fo:page-number-citation, fo:page-number-citation-last |
| **Inherited** | Yes |
| **Percentages** | N/A |
| **Media** | visual |

<!-- Source: https://www.w3.org/TR/xslfo20/#text-transform -->

This property controls capitalization effects of an element's text.

Values have the following meanings:

- **capitalize** -- Puts the first character of each word in uppercase.
- **uppercase** -- Puts all characters of each word in uppercase.
- **lowercase** -- Puts all characters of each word in lowercase.
- **none** -- No capitalization effects.

The actual transformation in each case is written language dependent. Conforming user agents may consider the value of "text-transform" to be "none" for characters that are not from the ISO Latin-1 repertoire and for elements in languages for which the transformation is different from that specified by the case-conversion tables of Unicode or ISO 10646.

XSL modifications: There are severe internationalization issues with the use of this property. It has been retained for CSS compatibility, but its use is not recommended in XSL.

### treat-as-word-space

| Field | Value |
|---|---|
| **Values** | `auto \| true \| false \| inherit` |
| **Initial** | `auto` |
| **Applies to** | fo:character |
| **Inherited** | No |
| **Percentages** | N/A |
| **Media** | visual |

<!-- Source: https://www.w3.org/TR/xslfo20/#treat-as-word-space -->

This property determines if the character shall be treated as a word space or as a normal letter.

Values have the following meanings:

- **auto** -- The value of this property is determined by the Unicode code point for the character. As the default behavior: The characters at code points U+0020 and U+00A0 are treated as if 'true' had been specified. All other characters are treated as if 'false' had been specified. This property does not automatically apply word spacing to the fixed spaces (U+2000 through U+200A) or the ideographic-space (U+3000). This default behavior can be overridden by information in the font used for formatting the character, which can specify additional characters that may be treated as "word spaces".
- **true** -- The inline-progression-dimension of the character shall be adjusted as described in the "word-spacing" property.
- **false** -- This character shall not have a word spacing adjustment applied.

### word-spacing

| Field | Value |
|---|---|
| **Values** | `normal \| <length> \| <space> \| inherit` |
| **Initial** | `normal` |
| **Applies to** | fo:block, fo:character, fo:initial-property-set, fo:inline, fo:page-number, fo:page-number-citation, fo:page-number-citation-last |
| **Inherited** | Yes |
| **Percentages** | N/A |
| **Media** | visual |

<!-- Source: https://www.w3.org/TR/xslfo20/#word-spacing -->

This property specifies spacing behavior between words.

Values have the following meanings:

- **normal** -- The normal inter-word space, as defined by the current font and/or the UA.
- **\<length\>** -- This value indicates inter-word space in addition to the default space between words. Values may be negative, but there may be implementation-specific limits.
- **\<space\>** -- (XSL extension) This allows the user to specify a range of adjustments in addition to the default space between words. The minimum and maximum values specify the limits of the adjustment.

Word spacing algorithms are user agent-dependent. Word spacing is also influenced by justification (see the "text-align" property).

Default space between words is defined to be the inline-progression-dimension of the glyph-area obtained by formatting the current fo:character whose treat-as-word-space trait has the value "true".

Note: The "word-spacing" property only affects the placement of glyphs and not the shape that may be associated with the characters.

## Code Samples

No code samples in spec for this property group.

## See Also

- [fo-character.md](fo-character.md) -- fo:character uses character, suppress-at-line-break, treat-as-word-space
- [fo-block.md](fo-block.md) -- fo:block uses text-decoration, letter-spacing, word-spacing
- [fo-inline.md](fo-inline.md) -- fo:inline uses text-decoration, letter-spacing, word-spacing
- [properties-block-line.md](properties-block-line.md) -- block and line-related properties including text-align
