# Antenna House Extension Properties: Typography Extension Properties

<!-- Source: XSL-FO-Reference-74-MID.pdf pp.312-476 -->

General typography extensions for letter spacing, widow/orphan control, baseline grids, text balancing, kerning, ligatures, line break algorithms, and text normalization.

## axf:abbreviation-character-count

Specifies the maximum number of characters considered an abbreviation.

Values have the following meanings:

- **auto**: The value specified by `abbreviation-character-count` in the Option Setting File is adopted.
- **\<number\>**: Specifies the number of characters considered an abbreviation.

| Attribute | Value |
|---|---|
| **Applies to** | `<fo:block>` |
| **Values** | `auto \| <number>` |
| **Initial** | auto |
| **Inherited** | yes |

## axf:adjust-last-line-spacing

Adjusts the spacing on the last line.

Values have the following meanings:

- **false**: Does nothing.
- **true**: Reduces the difference between the spacing on the last line and the spacing on the second-last line.

This processing applies under the following conditions:

- `text-align` is `"justify"`
- `text-align-last` is not `"justify"`
- When the algorithm of Breaking Paragraphs into Lines is applied, such as when `axf:line-break="bpil"` is specified

If the result of adjusting the spacing satisfies the condition of `axf:flush-zone`, `axf:flush-zone` will be applied.

| Attribute | Value |
|---|---|
| **Applies to** | `<fo:block>` |
| **Values** | `false \| true` |
| **Initial** | false |
| **Inherited** | yes |

## axf:auto-letter-spacing

Changes letter-spacing depending on the number of characters. For the meaning of the values, see the corresponding specifications in the AHF Online Manual.

| Attribute | Value |
|---|---|
| **Applies to** | inline-level formatting objects |
| **Values** | `[none \| <length> \| <percentage> ]*` |
| **Initial** | none |
| **Inherited** | no |

## axf:avoid-widow-words

Specifies spacing behavior between words or characters so that the last line of the paragraph does not have only one word left (one character for CJK).

Values have the following meanings:

- **false**: Does nothing.
- **true**: Adjusts the spacing so that the last line of the paragraph does not have only one word left (one character for CJK). When `axf:text-justify-trim="auto"` is specified, it is considered that `axf:text-justify-trim="ideograph inter-word"` is specified.
- **\<length\>** and **\<percentage\>**: See the corresponding specifications in the AHF Online Manual.

| Attribute | Value |
|---|---|
| **Applies to** | `<fo:block>` |
| **Values** | `false \| true \| <length> \| <percentage>` |
| **Initial** | false |
| **Inherited** | yes |

## axf:avoid-widow-words-cjk-punctuation

Specifies whether to include the last punctuation mark and count them in one character when `axf:avoid-widow-words="true"` is specified in CJK. For the meaning of the values, see the corresponding specifications in the AHF Online Manual.

| Attribute | Value |
|---|---|
| **Applies to** | `<fo:block>` |
| **Values** | `auto \| true \| false <string>` |
| **Initial** | auto |
| **Inherited** | yes |

## axf:balanced-text-align

Specifies whether to balance the entire block including the last line.

Values have the following meanings:

- **true**: The entire block is adjusted to be balanced including the last line.
- **false**: Does not balance the last line.
- **auto**: When applied to a block with any of the following conditions, the entire block including the last line is adjusted to be balanced:
  - `text-align="justify"` and `text-align-last="justify"`
  - `text-align="center"` and `text-align-last="center"`

This property is only valid when the line breaking algorithm of Breaking Paragraphs into Lines is applied, such as when `axf:line-break="bpil"` is specified. Otherwise it is considered `false`.

| Attribute | Value |
|---|---|
| **Applies to** | `<fo:block>` |
| **Values** | `true \| false \| auto` |
| **Initial** | auto |
| **Inherited** | yes |

## axf:baseline-block-snap

This property specifies how to align blocks other than normal line boxes, such as headings, figures and tables, on the baseline grid. See `axf:baseline-grid` for usage.

Values have the following meanings:

- **none**: The block is not aligned with the baseline grid.
- **auto**: Same as `before` on top of column, same as `after` at bottom of column, otherwise `center`.
- **before**: The before edge of the block is aligned with a text-before-edge baseline on the baseline grid.
- **after**: The after edge of the block is aligned with a text-after-edge baseline on the baseline grid.
- **center**: The block is centered between a text-before-edge and a text-after-edge baselines on the baseline grid.
- **border-box**: The border edge is used to align the block on the baseline grid.
- **margin-box**: The margin edge is used to align the block on the baseline grid.

CAUTION: `axf:baseline-block-snap` is valid when `axf:baseline-grid` is specified in the parent block of the block where it is specified.

| Attribute | Value |
|---|---|
| **Applies to** | block-level elements |
| **Values** | `none \| [auto \| before \| after \| center] \|\| [border-box \| margin-box]` |
| **Initial** | auto border-box |
| **Inherited** | no |

## axf:baseline-grid

Sets or clears the baseline grid.

Inside the area where a baseline grid is set, the lines are aligned with baselines on the baseline grid. Half-leading is not added before the first line and after the last line so that the em-box edges are aligned with the before and after edges of the content box.

CAUTION: `axf:baseline-grid` works within the block where it is specified. The block itself depends on the parent's block. The baseline grid is not available in the area with `display-align` other than `auto`.

Values have the following meanings:

- **normal**: Neither sets nor clears the baseline grid.
- **none**: Clears the baseline grid and the content will not align with a baseline grid.
- **new**: Sets a new baseline grid. The new baseline grid is established by using the font and the `line-height` settings of this element.
- **root**: Sets the baseline grid defined by the root element. The root baseline grid is defined by using the font and the `line-height` settings of the root element.

An XSL-FO example with baseline grids can be found in the Online Manual.

| Attribute | Value |
|---|---|
| **Applies to** | block-level formatting objects, `<fo:flow>`, and `<fo:static-content>`/block-containers |
| **Values** | `normal \| none \| root \| new` |
| **Initial** | normal |
| **Inherited** | no |

## axf:break-distance

Specifies effective heights for `break-after` and `break-before`.

Values have the following meanings:

- **always**: `break-after` and `break-before` are always effective.
- **\<length\>** | **\<percentage\>**: Are effective when the height of the remaining area is less than the specified height. The value percentage refers to the height of containing block.

| Attribute | Value |
|---|---|
| **Applies to** | block-level formatting objects |
| **Values** | `always \| <length> \| <percentage>` |
| **Initial** | always |
| **Inherited** | no |

## axf:flush-zone

Adjusts the space at the end of the last line.

Values have the following meanings:

- **none**: Does nothing.
- **\<length\>** | **\<percentage\>**: If `text-align="justify"` is specified but `text-align-last="justify"` is not specified, and the space at the end of the last line is less than or equal to the specified value, the last line is processed as if `text-align-last="justify"` is specified.

| Attribute | Value |
|---|---|
| **Applies to** | `<fo:block>` |
| **Values** | `none \| <length> \| <percentage>` |
| **Initial** | none |
| **Inherited** | yes |

## axf:indent-here

Aligns the indent position to the region position when a line break occurs.

In order to indent lines, specify `<fo:inline>` which contains this property as follows:

```xml
<fo:block>Indent-here: <fo:inline axf:indent-here="0pt"/>The quick
brown fox jumps over the lazy dog ...</fo:block>
```

The start position of `<fo:inline>` becomes the standard of indentation.

Values have the following meanings:

- **none**: Does nothing.
- **\<length\>**: Aligns the indent position to the shifted position by `<length>` from the beginning of the specified line area.

| Attribute | Value |
|---|---|
| **Applies to** | `<fo:inline>` |
| **Values** | `none \| <length>` |
| **Initial** | none |
| **Inherited** | no |

## axf:intrude-into-punctuation

Intrudes the inline element into the punctuation. For the meaning of the values, see the corresponding specifications in the AHF Online Manual.

| Attribute | Value |
|---|---|
| **Applies to** | inline elements |
| **Values** | `none \| [start \|\| end]` |
| **Initial** | none |
| **Inherited** | yes |

## axf:justify-nbsp

Specifies whether to justify NON-BREAKING SPACE or not.

Generally, NON-BREAKING SPACE (U+00A0) is intended for justification. The `axf:justify-nbsp` property can be used when you want to check off U+00A0 from justification.

Values have the following meanings:

- **true**: NON-BREAKING SPACE is included for justification.
- **false**: NON-BREAKING SPACE is not included for justification.

| Attribute | Value |
|---|---|
| **Applies to** | all formatting objects |
| **Values** | `true \| false` |
| **Initial** | true |
| **Inherited** | yes |

## axf:keep-together-within-dimension

Specifies the upper limit height of the `keep-together` condition.

If `keep-together.within-page` or `.within-column` is not `auto`, you can specify the height for `keep-together` to apply to that block. When it is `all`, the height is not restricted. If you specify a height with `<length>`, `keep-together` will be applied to that height, but after that it behaves as if `auto` was specified for `keep-together`.

For example, if you want to specify `keep-together.within-page="always"` for a block, but want to break it if it is a block that exceeds the height of the page, specify as follows:

```xml
<fo:block keep-together.within-page="always"
   axf:keep-together-within-dimension="100vh">
```

| Attribute | Value |
|---|---|
| **Applies to** | block-level formatting objects |
| **Values** | `all \| <length>` |
| **Initial** | all |
| **Inherited** | no |

## axf:keep-together-within-inline-dimension

Specifies the upper limit width of the `keep-together.within-line` condition.

When `keep-together.within-line` is not `auto`, you can specify the width to apply `keep-together.within-line` to the block. When `all` is specified, the width is not limited. If you specify a width with `<length>`, `keep-together` is applied up to that width, but for a width longer than that, `keep-together` behaves as if `auto` is specified.

| Attribute | Value |
|---|---|
| **Applies to** | block-level formatting objects |
| **Values** | `all \| <length>` |
| **Initial** | all |
| **Inherited** | no |

## axf:kerning-mode

Specifies whether to process the kerning. You can specify whether pair kerning is performed or not by `pair-kerning` in the Option Setting File. This can also be set in the Format Option Setting dialog in GUI.

Values have the following meanings:

- **none**: The kerning is not processed.
- **pair**: The pair kerning is processed.
- **auto**: Dependent on the system setting.

| Attribute | Value |
|---|---|
| **Applies to** | all block-level and inline-level formatting objects |
| **Values** | `none \| pair \| auto` |
| **Initial** | auto |
| **Inherited** | yes |

## axf:leader-expansion

Specifies whether to expand a leader forcibly.

Values have the following meanings:

- **auto**: Operates as usual by specifying `text-align`.
- **force**: Considers a line with leaders as `text-align="justify"`. Consequently, leaders will expand.

For illustrated examples, see `axf:leader-expansion` in XSL/CSS Extensions in Features of the Online Manual.

| Attribute | Value |
|---|---|
| **Applies to** | `<fo:block>` |
| **Values** | `auto \| force` |
| **Initial** | auto |
| **Inherited** | yes |

## axf:letter-spacing-side

Specifies on which side of the character the space by `letter-spacing` is distributed.

Values have the following meanings:

- **both**: Half the amount of space is distributed on both sides of the character for each.
- **start**: The space is distributed only on the start side of the character.
- **end**: The space is distributed only on the end side of the character.

| Attribute | Value |
|---|---|
| **Applies to** | inline-level formatting objects |
| **Values** | `both \| start \| end` |
| **Initial** | both |
| **Inherited** | yes |

## axf:ligature-mode

Specifies whether to perform the ligature processing.

The ligature processed here is the ligature defined in the font itself. The ligatures defined in Unicode are not processed. (It is called Canonical Composition.) In order to normalize ligatures defined in Unicode Standard, specify `axf:normalize="nfc"`.

Values have the following meanings:

- **none**: The ligature processing is not performed.
- **latin**: Processes the ligature in Western languages. It is processed when the scripts are the following: Latn, Grek, Cyrl.
- **kana**: Processes the ligature of Kana + semivoiced sound symbol in JIS X 0213:2004 as follows: U+304B + U+309A, U+304D + U+309A, U+304F + U+309A, U+3051 + U+309A, U+3053 + U+309A, U+30AB + U+309A, U+30AD + U+309A, U+30AF + U+309A, U+30B1 + U+309A, U+30B3 + U+309A, U+30BB + U+309A, U+30C4 + U+309A, U+30C8 + U+309A, U+31F7 + U+309A. Although the ligature of Western languages and the ligature of symbols are included in JIS X 0213:2004, these are processed by `axf:ligature-mode="latin"`.
- **jamo**: Processes the ligature of Hangul Jamo U+1100 to U+11FF.
- **all**: `latin kana jamo` is considered to be specified.
- **auto**: The ligature of kana is performed. `latin-ligature` in the Option Setting File will decide whether to perform the ligature of Western words. This setting can also be done with the Format Option Setting dialog in GUI. Whether to process the ligature of Hangul Jamo depends on `jamo-ligature` in the Option Setting File.

| Attribute | Value |
|---|---|
| **Applies to** | all block-level and inline-level formatting objects |
| **Values** | `none \| [ latin \|\| kana \|\| jamo ] \| all \| auto` |
| **Initial** | auto |
| **Inherited** | yes |

## axf:line-break

Specifies the method of line breaking.

Values have the following meanings:

- **auto**: It is assumed that `normal` is specified.
- **normal**: CJK Nonstarter characters (prolonged sound mark, small hiragana letters, small katakana letters, and iteration marks) defined in JIS X 4051:2004 are not treated as Nonstarter characters. Characters marked with [NS] in the character list are processed.
- **strict**: CJK Nonstarter character is treated. Characters marked with [NS] and [JIS] in the character list are processed.
- **line**: Line breaking is performed one by one by a simple algorithm.
- **bpil**: Line breaking is performed according to the line breaking algorithm by Knuth-Plass's Breaking Paragraphs into Lines. At this time, the bpil specification in the Option Setting File is ignored. Depending on the conditions, this algorithm may not be applicable. See Line Breaking in Technical Notes in Technical of the Online Manual.

If neither `normal` nor `strict` is specified, it is assumed that `normal` is specified. When neither `line` nor `bpil` is specified, the algorithm is selected according to the specification of bpil in the Option Setting File. The line breaking other than Nonstarter characters in CJK complies with UAX#14: Line Breaking Properties. At this time, characters specified to the properties of `axf:append-non-starter-characters`, `axf:except-non-starter-characters`, `axf:append-non-end-of-line-characters` and `axf:except-non-end-of-line-characters` are included.

The CJK Nonstarter characters include various categories:

- [NS] classified characters: double exclamation mark, interrobang, double question marks, wave dash, katakana middle dot, sound marks, and others classified into NS in Line Break Properties.
- [JIS] classified characters: ideographic iteration marks, small hiragana/katakana letters, prolonged sound marks, iteration marks, and others classified as Nonstarter characters in JIS X 4051:2004.

| Attribute | Value |
|---|---|
| **Applies to** | all block-level formatting objects |
| **Values** | `auto \| [[normal \| strict] \|\| [line \| bpil]]` |
| **Initial** | auto |
| **Inherited** | yes |

## axf:normalize

Specifies the normalization of text.

Specifies whether the normalization defined in UAX#15: Unicode Normalization Forms is performed. The normalization is performed to the character strings described in the text area. If you use only the normalized code from the start, it is not necessary to specify the normalization. If not, the normalization by NFC will be a good choice for practical use.

In these conversions, all the Composition Exclusions are excluded from the normalization processing when `axf:normalize-exclude="full-composition-exclusion"` is specified.

CAUTION: Keep in mind that U+00A0, which is a meaningful code as FO, will be transformed to U+0020, etc. by performing the normalization with NFKC, for example.

Values have the following meanings:

- **auto**: Depends on the value of `normalize` specified in the Option Setting File.
- **none**: Does not normalize text.
- **nfc**: Performs NFC.
- **nfkc**: Performs NFKC.
- **nfd**: Performs NFD.
- **nfkd**: Performs NFKD.

| Attribute | Value |
|---|---|
| **Applies to** | all block-level and inline-level formatting objects |
| **Values** | `auto \| none \| nfc \| nfkc \| nfd \| nfkd` |
| **Initial** | auto |
| **Inherited** | yes |

## axf:normalize-exclude

Specifies whether Composition Exclusions are excluded or not when the normalization (`axf:normalize`) is specified.

Values have the following meanings:

- **full-composition-exclusion**: Excludes all the characters specified in Composition Exclusions.
- **none**: Does not exclude.

| Attribute | Value |
|---|---|
| **Applies to** | all block-level and inline-level formatting objects |
| **Values** | `full-composition-exclusion \| none` |
| **Initial** | full-composition-exclusion |
| **Inherited** | yes |

## axf:quotetype

Specifies the direction of the quotes.

For non-directional quotation marks such as U+0022, explicitly specify the direction as follows to encourage proper line breaks:

```xml
Lorem
<fo:character character="&#x22;"
   axf:quotetype="OP"/>ipsum<fo:character character="&#x22;"
   axf:quotetype="CL"/>
dolor sit amet,
```

Specifying the property to characters other than quotation marks is invalid. See Quotation Mark in Technical Notes in Technical of the Online Manual for how to handle quotation marks. If not specified, the setting there will be used.

Values have the following meanings (they are case insensitive):

- **QU**: Considered to be a non-directional quotation mark.
- **OP**: Considered to be an open quotation mark.
- **CL**: Considered to be a close quotation mark.

| Attribute | Value |
|---|---|
| **Applies to** | `<fo:character>` |
| **Values** | `QU \| OP \| CL` |
| **Initial** | empty |
| **Inherited** | no |

## axf:transform

Specifies the block transformation.

CAUTION: The transformation of the region does not happen. Only the contents are transformed.

Values have the following meanings:

- **none**: Does not transform the block.
- The following transformations can be specified:
  - `matrix(<number>, <number>, <number>, <number>, <number>, <number>)`
  - `translate(<translation-value>[, <translation-value>])`
  - `translateX(<translation-value>)`
  - `translateY(<translation-value>)`
  - `scale(<number>[, <number>])`
  - `scaleX(<number>)`
  - `scaleY(<number>)`
  - `rotate(<angle>)`
  - `skew(<angle>[, <number>])`
  - `skewX(<number>)`
  - `skewY(<number>)`

| Attribute | Value |
|---|---|
| **Applies to** | transformable objects |
| **Values** | `none \| <transform-function> +` |
| **Initial** | none |
| **Inherited** | no |

## axf:transform-origin

Specifies the origin of the block transformation.

| Attribute | Value |
|---|---|
| **Applies to** | transformable objects |
| **Values** | `[ <percentage> \| <length> \| left \| center \| right \| top \| bottom ] \| [ [ <percentage> \| <length> \| left \| center \| right ] && [ <percentage> \| <length> \| top \| center \| bottom ] ]` |
| **Initial** | center center |
| **Inherited** | no |
