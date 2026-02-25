# Ruby Properties

## Overview

<!-- Source: https://www.w3.org/TR/xslfo20/#ruby -->

The ruby properties control the positioning, alignment, sizing, and behavior of ruby annotations in XSL-FO. Ruby annotations are small characters typically used in East Asian typography to indicate pronunciation or meaning alongside base characters. These properties are based on the CSS3 Ruby Module specification and are used with the fo:ruby, fo:ruby-base, fo:ruby-text, fo:ruby-base-container, and fo:ruby-text-container formatting objects.

## Properties

### ruby-position

| Field | Value |
|---|---|
| **Values** | `auto \| before \| after \| bopomofo \| inline \| inherit` |
| **Initial** | `auto` |
| **Applies to** | ruby formatting objects |
| **Inherited** | Yes |
| **Percentages** | N/A |
| **Media** | visual |

<!-- Source: https://www.w3.org/TR/xslfo20/#ruby-position -->

This property specifies the position of ruby annotations with respect to their corresponding base glyphs.

Values have the following meanings:

- **auto** -- Same as "before" for fo:ruby-text and the first fo:ruby-text-container, and same as "after" for the second fo:ruby-text-container. This is the initial value.
- **before** -- The ruby text appears before the base. This is the most common setting used in ideographic East Asian writing systems. When writing-mode is tb-rl, the ruby appears on the right side of the base and is rendered in the same layout mode as the base.
- **after** -- The ruby text appears after the base. This is a relatively rare setting used in ideographic East Asian writing systems, most often found in educational text. If the base appears in a tb-rl writing-mode, the bottom ruby appears on the left side of the base and is rendered in the same layout mode as the base (i.e. vertical).
- **bopomofo** -- The ruby text appears on the right of the base. Unlike "before" and "after", this value is not relative to the inline-direction. This value is provided for the special case of traditional Chinese as used especially in Taiwan: ruby (made of bopomofo glyphs) in that context appears vertically along the right side of the base glyph, whether the layout of the base characters is vertical or horizontal. Handling of ruby text that is not bopomofo when the value of ruby-position is set to "bopomofo" is not defined by this specification.
- **inline** -- Ruby text follows the ruby base with no special styling. The value can be used to disable ruby text positioning.

### ruby-alignment

| Field | Value |
|---|---|
| **Values** | `auto \| start \| center \| end \| inherit` |
| **Initial** | `auto` |
| **Applies to** | ruby formatting objects |
| **Inherited** | Yes |
| **Percentages** | N/A |
| **Media** | visual |

<!-- Source: https://www.w3.org/TR/xslfo20/#ruby-alignment -->

This property specifies alignment of a ruby annotation with respect to its base text.

Values have the following meanings:

- **auto** -- The user agent determines how the ruby contents are aligned. This is the initial value.
- **start** -- The ruby text content is aligned with the start edge of the base.
- **center** -- The ruby text content is centered within the width of the base. If the length of the base is smaller than the length of the ruby text, then the base is centered within the width of the ruby text.
- **end** -- The ruby text content is aligned with the end edge of the base.

### ruby-group-distribution

| Field | Value |
|---|---|
| **Values** | `auto \| distribute-letter \| distribute-space \| inherit` |
| **Initial** | `auto` |
| **Applies to** | ruby formatting objects |
| **Inherited** | Yes |
| **Percentages** | N/A |
| **Media** | visual |

<!-- Source: https://www.w3.org/TR/xslfo20/#ruby-group-distribution -->

This property specifies how the space between the ruby characters or the base characters (whichever is shortest) is distributed.

Values have the following meanings:

- **distribute-letter** -- If the width of the ruby text is smaller than that of the base, then the ruby text contents are evenly distributed across the width of the base, with the first and last ruby text glyphs lining up with the corresponding first and last base glyphs. If the width of the ruby text is at least the width of the base, then the letters of the base are evenly distributed across the width of the ruby text.
- **distribute-space** -- If the width of the ruby text is smaller than that of the base, then the ruby text contents are evenly distributed across the width of the base, with a certain amount of white space preceding the first and following the last character in the ruby text. That amount of white space is normally equal to half the amount of inter-character space of the ruby text. If the width of the ruby text is at least the width of the base, then the same type of space distribution applies to the base. This type of alignment is sometimes referred to as the "1:2:1" alignment [JIS4051].

### ruby-alignment-edge

| Field | Value |
|---|---|
| **Values** | `auto \| normal \| line-edge \| inherit` |
| **Initial** | `auto` |
| **Applies to** | ruby formatting objects |
| **Inherited** | Yes |
| **Percentages** | N/A |
| **Media** | visual |

<!-- Source: https://www.w3.org/TR/xslfo20/#ruby-alignment-edge -->

This property specifies what the formatter must do when ruby annotations occur at the start or end of lines.

Values have the following meanings:

- **auto** -- The user agent determines how the ruby contents are aligned at the edges of lines. This is the initial value.
- **normal** -- When the line head starts with ruby annotated text where the ruby text length is longer than that of the base characters, compose the text so that the first ruby character which overhangs the base text is aligned with the line head, and vice versa.
- **line-edge** -- If the ruby text is not adjacent to a line edge, it is aligned as in "normal". Where the ruby text length is longer than that of the base characters and it is adjacent to a line edge, then it is still aligned as in "normal", but the side of the ruby text that touches the end of the line is lined up with the corresponding edge of the base. In the other scenarios, this is just "normal".

### ruby-align

| Field | Value |
|---|---|
| **Values** | `auto \| start \| left \| center \| end \| right \| distribute-letter \| distribute-space \| line-edge \| inherit` |
| **Initial** | `0` |
| **Applies to** | fo:inline |
| **Inherited** | Yes |
| **Percentages** | refer to inherited font size |
| **Media** | visual |

<!-- Source: https://www.w3.org/TR/xslfo20/#ruby-align -->

This property is a shorthand for the "ruby-alignment", "ruby-group-distribution", and "ruby-alignment-edge" properties and maps as follows:

- **auto** -- ruby-alignment = "auto"; ruby-group-distribution = "auto"; ruby-alignment-edge = "auto"
- **start** -- ruby-alignment = "start"; ruby-group-distribution = "auto"; ruby-alignment-edge = "auto"
- **left** -- ruby-alignment = "start" or "end" depending on writing mode; ruby-group-distribution = "auto"; ruby-alignment-edge = "auto"
- **center** -- ruby-alignment = "center"; ruby-group-distribution = "auto"; ruby-alignment-edge = "auto"
- **end** -- ruby-alignment = "end"; ruby-group-distribution = "auto"; ruby-alignment-edge = "auto"
- **right** -- ruby-alignment = "end" or "start" depending on writing mode; ruby-group-distribution = "auto"; ruby-alignment-edge = "auto"
- **distribute-letter** -- ruby-alignment = "auto"; ruby-group-distribution = "distribute-letter"; ruby-alignment-edge = "auto"
- **distribute-space** -- ruby-alignment = "auto"; ruby-group-distribution = "distribute-space"; ruby-alignment-edge = "auto"
- **line-edge** -- ruby-alignment = "auto"; ruby-group-distribution = "auto"; ruby-alignment-edge = "line-edge"

### ruby-overhang

| Field | Value |
|---|---|
| **Values** | `auto \| start \| end \| none \| inherit` |
| **Initial** | `none` |
| **Applies to** | ruby formatting objects |
| **Inherited** | Yes |
| **Percentages** | N/A |
| **Media** | visual |

<!-- Source: https://www.w3.org/TR/xslfo20/#ruby-overhang -->

This property specifies whether, and on which side, ruby text is allowed to partially overhang any adjacent text in addition to its own base, when the ruby text is wider than the ruby base.

Ruby text is never allowed to overhang glyphs belonging to another ruby base. Also the user agent is free to assume a maximum amount by which ruby text may overhang adjacent text. The user agent may use the JIS4051 recommendation of using one ruby text character length as the maximum overhang length.

Values have the following meanings:

- **auto** -- The ruby text can overhang text adjacent to the base on either side. JIS4051 specifies the categories of characters that ruby text can overhang. The user agent is free to follow the JIS4051 recommendation or specify its own classes of characters to overhang. This is the initial value.
- **start** -- The ruby text can overhang the text that precedes it. That means, for example, that ruby can overhang text that is to the left of it in horizontal LTR layout, or it can overhang text that is above it in vertical-ideographic layout.
- **end** -- The ruby text can overhang the text that follows it. That means, for example, that ruby can overhang text that is to the right of it in horizontal LTR layout, or it can overhang text that is below it in vertical-ideographic layout.
- **none** -- The ruby text is not allowed to overhang adjacent text. This is the default behavior.

### ruby-overhang-length

| Field | Value |
|---|---|
| **Values** | `<length> \| auto` |
| **Initial** | `1em` |
| **Applies to** | ruby formatting objects |
| **Inherited** | Yes |
| **Percentages** | font-size of ruby |
| **Media** | visual |

<!-- Source: https://www.w3.org/TR/xslfo20/#ruby-overhang-length -->

This property specifies the maximum distance that ruby may overhang adjacent characters, when it is possible and necessary for the ruby to overhang.

Values have the following meanings:

- **auto** -- The user agent determines the maximum overhang.
- **\<length\>** -- The maximum distance the ruby may overhang adjacent characters.

### ruby-span

| Field | Value |
|---|---|
| **Values** | `<number> \| none \| inherit` |
| **Initial** | `none` |
| **Applies to** | ruby annotation elements |
| **Inherited** | No |
| **Percentages** | N/A |
| **Media** | visual |

<!-- Source: https://www.w3.org/TR/xslfo20/#ruby-span -->

This property controls the spanning behavior of ruby annotation elements.

Values have the following meanings:

- **\<number\>** -- The number of ruby base elements to be spanned by the annotation element. If the \<number\> is "0", it is replaced by "1". The \<number\> is the computed value.
- **none** -- No spanning. The computed value is "1".

### ruby-size

| Field | Value |
|---|---|
| **Values** | `<number> \| inherit` |
| **Initial** | `0.5` |
| **Applies to** | ruby text elements |
| **Inherited** | Yes |
| **Percentages** | font-size of base characters |
| **Media** | visual |

<!-- Source: https://www.w3.org/TR/xslfo20/#ruby-size -->

This property specifies the size of ruby text.

In Japanese layout, when ruby is attached to twelve point or larger base characters (usually used for headings), the size of the ruby letter is generally smaller than half the size of the base characters.

Values have the following meanings:

- **\<number\>** -- The ratio of the size of ruby characters to base characters.

### ruby-proportion

| Field | Value |
|---|---|
| **Values** | `normal \| narrow \| inherit` |
| **Initial** | `normal` |
| **Applies to** | ruby text elements |
| **Inherited** | Yes |
| **Percentages** | N/A |
| **Media** | visual |

<!-- Source: https://www.w3.org/TR/xslfo20/#ruby-proportion -->

This property controls the aspect ratio of ruby text.

Values have the following meanings:

- **normal** -- The ruby characters have normal proportions.
- **narrow** -- The ruby characters are narrower in the inline-direction so that more ruby characters can fit alongside a base character.

### ruby-mode

| Field | Value |
|---|---|
| **Values** | `mono \| compound \| inherit` |
| **Initial** | `mono` |
| **Applies to** | ruby formatting objects |
| **Inherited** | Yes |
| **Percentages** | N/A |
| **Media** | visual |

<!-- Source: https://www.w3.org/TR/xslfo20/#ruby-mode -->

This property specifies whether adjacent fo:ruby-text can intrude on each other.

Values have the following meanings:

- **mono** -- Ruby characters do not intrude upon each other. Ruby letters are attached to each base kanji character in a compound word individually.
- **compound** -- Adjacent fo:ruby-text are treated as being part of one compound word and may intrude upon each other. Ruby letters are attached to groups of kanji characters in compound words.

### line-stacking-annotation

| Field | Value |
|---|---|
| **Values** | `include-annotation \| exclude-annotation \| inherit` |
| **Initial** | `exclude-annotation` |
| **Applies to** | block-level formatting objects containing annotation areas |
| **Inherited** | Yes |
| **Percentages** | N/A |
| **Media** | visual |

<!-- Source: https://www.w3.org/TR/xslfo20/#line-stacking-annotation -->

This property determines the line stacking method for block elements containing annotation areas such as from ruby or emphasis dots. In all cases the areas returned by fo:ruby-base or fo:annotation-base are considered for line stacking.

Values have the following meanings:

- **exclude-annotation** -- The annotation areas are ignored for line stacking.
- **include-annotation** -- The annotation areas are considered for line stacking.

## Code Samples

No code samples in spec for this property group.

## See Also

- [fo-ruby](fo-ruby.md) -- Container formatting object for ruby annotations
- [fo-ruby-base](fo-ruby-base.md) -- Contains the base text for ruby annotations
- [fo-ruby-text](fo-ruby-text.md) -- Contains the annotation text for ruby
- [fo-ruby-base-container](fo-ruby-base-container.md) -- Groups ruby base elements
- [fo-ruby-text-container](fo-ruby-text-container.md) -- Groups ruby text elements
