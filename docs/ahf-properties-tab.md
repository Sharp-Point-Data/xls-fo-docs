# Antenna House Extension Properties: Tab Properties

<!-- Source: XSL-FO-Reference-74-MID.pdf pp.312-476 -->

Properties for tab stop positioning and alignment, used with the `axf:tab` formatting object.

## axf:tab-align

Specifies the tab alignment at the tab stop position.

Values have the following meanings:
- **auto**: The alignment follows the setting in `axf:tab-stops` in the parent block (`<fo:block>`).
- **start**: Aligns the start of the string to the tab stop position.
- **center**: Aligns the center of the string to the tab stop position.
- **end**: Aligns the end of the string to the tab stop position.
- **left**: Aligns the left side of the string (the top of the string in case of vertical writing) to the tab stop position. Same as `start` in case of `writing-mode="lr-tb"` and `"tb-rl"`.
- **right**: Aligns the right side of the string (the bottom of the string in case of vertical writing) to the tab stop position. Same as `end` in case of `writing-mode="lr-tb"` and `"tb-rl"`.
- **decimal**: Considered that `"."` is specified.
- **\<string\>**: Aligns the start of the string to the tab stop position as specified.

| Attribute | Value |
|---|---|
| **Applies to** | `<axf:tab>` |
| **Values** | `auto \| start \| center \| end \| left \| right \| decimal \| <string>` |
| **Initial** | `auto` |
| **Inherited** | no |

## axf:tab-overlap-treatment

Specifies a behavior when tab alignment makes letters overlapped. The default value `auto` depends on the default value of the system. This is the value specified in `tab-overlap-treatment` in the Option Setting File. The value `ignore-tab` ignores the tab. The string will be shown just after the previous string. The value `next-tab` places the tab at the next tab stop position. Letters will not be overlapped when `axf:tab-align="start"` is specified.

| Attribute | Value |
|---|---|
| **Applies to** | `<fo:block>`, `<fo:character>` |
| **Values** | `auto \| ignore-tab \| next-tab` |
| **Initial** | `auto` |
| **Inherited** | yes |

## axf:tab-stops

This property is used to specify both the tab stops and the alignment of the content at the tab stop positions of the block lines in blocks (`<fo:block>`). These specifications are inherited by any subordinate blocks. For each tab stop, the alignment at the tab stop is set first, then the tab stop position (tab width) itself. All values are separated by spaces. If the alignment value is missing, the alignment value of the preceding tab stop position is assumed. If the alignment value at the beginning of the line is missing, then the `start` value applies. For the available alignment values, see `axf:tab-align`.

The tab width is set either by a length value (`<length>`) or a number (`<number>`). The number value corresponds to the number of spaces (U+0020). The default is eight spaces (8).

The `eol` value is the tab stop position at the end of a line. If this value is missing, then the last defined tab width is repeated to the end of the line.

| Attribute | Value |
|---|---|
| **Applies to** | practically useful in `<fo:block>` |
| **Values** | `[[<tab-align>? [<length>\|<number>]]* [<tab-align>? eol]?]!` |
| **Initial** | `8` |
| **Inherited** | yes |

## axf:tab-treatment

Specifies the method to treat the tab character (U+0009). The value `<number>` means the specified number of the white space characters (U+0020). You cannot specify a negative value. This white space is subject to processing of `white-space-treatment` and `white-space-collapse`, etc. The value `preserve` means treated as `<axf:tab>`.

| Attribute | Value |
|---|---|
| **Applies to** | `<fo:block>`, `<fo:character>` |
| **Values** | `<number> \| preserve` |
| **Initial** | `4` |
| **Inherited** | yes |
