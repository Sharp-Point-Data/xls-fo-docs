# Antenna House Extension Properties: Text Emphasis Properties

<!-- Source: XSL-FO-Reference-74-MID.pdf pp.312-476 -->

Properties for text emphasis marks (bouten), used in CJK typography to draw small symbols above or below characters for emphasis. Controls emphasis mark style, position, offset, skip behavior, font, and color.

## axf:text-emphasis-color

Specifies the color of emphasis marks. If nothing is specified, it's considered the same as color.

| Attribute | Value |
|---|---|
| **Applies to** | emphasis elements |
| **Values** | &lt;color&gt; |
| **Initial** | empty |
| **Inherited** | yes |

## axf:text-emphasis-font-family

Specifies the font family of emphasis marks. If nothing is specified, it's considered the same as font-family.

| Attribute | Value |
|---|---|
| **Applies to** | emphasis elements |
| **Values** | [&lt;family-name&gt; \| &lt;generic-family&gt;]# |
| **Initial** | empty string |
| **Inherited** | yes |

## axf:text-emphasis-font-size

Specifies the font size of emphasis marks. When specified using &lt;number&gt;, the value is what is obtained by multiplying font-size by the specified &lt;number&gt;.

| Attribute | Value |
|---|---|
| **Applies to** | emphasis elements |
| **Values** | &lt;number&gt; \| &lt;absolute-size&gt; \| &lt;relative-size&gt; \| &lt;length&gt; \| &lt;percentage&gt; |
| **Initial** | 0.5 |
| **Inherited** | yes |

## axf:text-emphasis-font-stretch

Specifies the font stretching of emphasis marks. If nothing is specified, it's considered the same as font-stretch.

| Attribute | Value |
|---|---|
| **Applies to** | emphasis elements |
| **Values** | normal \| wider \| narrower \| ultra-condensed \| extra-condensed \| condensed \| semi-condensed \| semi-expanded \| expanded \| extra-expanded \| ultra-expanded \| &lt;percentage&gt; \| &lt;number&gt; |
| **Initial** | empty |
| **Inherited** | yes |

## axf:text-emphasis-font-style

Specifies whether emphasis marks are made italic. If nothing is specified, it's considered the same as font-style.

| Attribute | Value |
|---|---|
| **Applies to** | emphasis elements |
| **Values** | normal \| italic |
| **Initial** | empty |
| **Inherited** | yes |

## axf:text-emphasis-font-weight

Specifies the font weight of emphasis marks. If nothing is specified, it's considered the same as font-weight.

| Attribute | Value |
|---|---|
| **Applies to** | emphasis elements |
| **Values** | normal \| bold \| bolder \| lighter \| 100 \| 200 \| 300 \| 400 \| 500 \| 600 \| 700 \| 800 \| 900 \| 1000 |
| **Initial** | empty |
| **Inherited** | yes |

## axf:text-emphasis-offset

Specifies the space between emphasis marks and the base characters. When specified using &lt;number&gt;, the value is what is obtained by multiplying axf:text-emphasis-font-size by the specified &lt;number&gt;. When ruby and emphasis marks are put on the same side, it is adjusted to the larger one of the specified value and the ruby height.

| Attribute | Value |
|---|---|
| **Applies to** | all elements |
| **Values** | &lt;number&gt; \| &lt;length&gt; \| &lt;percentage&gt; |
| **Initial** | 0pt |
| **Inherited** | yes |

## axf:text-emphasis-position

Specifies on which side of base characters emphasis marks are put.

Values have the following meanings:
- `before`: Emphasis marks are put on the before side.
- `after`: Emphasis marks are put on the after side.

| Attribute | Value |
|---|---|
| **Applies to** | all elements |
| **Values** | before \| after |
| **Initial** | before |
| **Inherited** | yes |

## axf:text-emphasis-skip

Specifies the character to which emphasis marks are not applied.

Values have the following meanings:
- `none`: No character is excluded.
- `spaces`: White space characters are excluded.
- `punctuation`: Punctuation marks are excluded.
- `symbols`: Symbols are excluded.
- `narrow`: Non full width characters (half width characters, etc.) are excluded.

| Attribute | Value |
|---|---|
| **Applies to** | all elements |
| **Values** | none \| [spaces \|\| punctuation \|\| symbols \|\| narrow] |
| **Initial** | spaces |
| **Inherited** | yes |

## axf:text-emphasis-style

Specifies the style of emphasis marks.

Values have the following meanings:
- `none`: No emphasis marks.
- `filled`: Specifies a character with color-fill.
- `open`: Specifies a character with an outline without color-fill.
- `dot`: Specifies a filled dot. filled dot is U+2022, open dot is U+25E6.
- `circle`: Specifies a circle. filled circle is U+25CF, open circle is U+25CB.
- `double-circle`: Specifies a double-circle. filled double-circle is U+25C9, open double-circle is U+25CE.
- `triangle`: Specifies a triangle. filled triangle is U+25B2, open triangle is U+25B3.
- `sesame`: Specifies a sesame dot. filled sesame is U+FE45, open sesame is U+FE46.
- `<string>`: Specifies an arbitrary character string. When multiple characters are specified, overlapping of emphasis marks is not considered though everything is displayed.

When filled or open is not specified, it's considered filled. When filled or open is specified without a shape, it's considered circle in vertical writing mode.

| Attribute | Value |
|---|---|
| **Applies to** | all elements |
| **Values** | none \| [[filled \| open] \|\| [dot \| circle \| double-circle \| triangle \| sesame]] \| &lt;string&gt; |
| **Initial** | none |
| **Inherited** | yes |
