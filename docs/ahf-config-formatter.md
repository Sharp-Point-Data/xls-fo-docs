# Antenna House Configuration: Formatter Settings

<!-- Source: XSL-FO-Reference-74-MID.pdf pp.213–256 -->

## Overview

The `<formatter-config>` element is the root element of the Antenna House Formatter option setting file (`AHFSettings.xml`). It contains child elements for formatter settings, font settings, PDF output, PostScript output, SVG output, text output, MathML settings, CGM settings, XSLT settings, and analyzer settings.

The `<formatter-settings>` child element controls the core formatting behavior of AH Formatter.

To use the Antenna House extensions, the corresponding namespace must be added to the namespace declarations:

<!-- Source: XSL-FO-Reference-74-MID.pdf p.213 -->
```xml
xmlns:axf="http://www.antennahouse.com/names/XSL/Extensions"
```

## Element: `<formatter-config>`

The root element for the formatter configuration in the `AHFSettings.xml` file. The child elements concern formatter properties, font settings, output options for PDF, PostScript, SVG, CGM, InDesign, FrameMaker, and text output, math processing, XSLT preprocessing, and formatting analyses.

**Attributes:** None

**Child elements:** `<formatter-settings>`, `<font-settings>`, `<pdf-settings>`, `<ps-settings>`, `<svg-settings>`, `<text-settings>`, `<mathml-settings>`, `<cgm-settings>`, `<xslt-settings>`, `<analyzer-settings>`

## Element: `<formatter-settings>`

These settings are used for the formatting.

**Parent:** `<formatter-config>`

**Child elements:** `<list-style-type>`, `<quotationmark>`, `<script-chars>`, `<space-end-punctuation>`, `<space-start-punctuation>`, `<space-between-digit-and-punctuation>`, `<space-between-punctuation-and-digit>`, `<usercss>`, `<css>`, `<script-language-in-CJK>`, `<multimedia>`, `<GS1-128>`, `<UAX50>`, `<unbreakable-words>`

---

## Attributes of `<formatter-settings>`

### Page Defaults

| Attribute | Description | Values | Default |
|-----------|-------------|--------|---------|
| `default-page-height` | Specifies the default page height with the real type numerical value. | `<length>` | `297mm` (DIN A4 page height) |
| `default-page-width` | Specifies the default page width with the real type numerical value. | `<length>` | `210mm` (DIN A4 page width) |
| `default-page-margin-bottom` | Specifies a default page margin bottom with the real type numerical value. A percent value is considered a ratio out of the page width. | `<length>` \| `<percentage>` | `10%` |
| `default-page-margin-left` | Specifies a default page margin left with the real type numerical value. A percent value is considered a ratio out of the page height. | `<length>` \| `<percentage>` | `10%` |
| `default-page-margin-right` | Specifies a default page margin right with the real type numerical value. A percent value is considered a ratio out of the page height. | `<length>` \| `<percentage>` | `10%` |
| `default-page-margin-top` | Specifies a default page margin top with the real type numerical value. A percent value is considered a ratio out of the page width. | `<length>` \| `<percentage>` | `10%` |
| `use-default-page-margin-XSL` | Specifies whether `default-page-margin-bottom`, `default-page-margin-top`, `default-page-margin-left` and `default-page-margin-right` are adopted or not when there is no margin specification in `<fo:simple-page-master>` in XSL. | `true` \| `false` | `false` |
| `default-from-page-master-region` | In XSL 1.1, there is no compatibility with XSL 1.0 in the method of evaluating `writing-mode` or `reference-orientation`. If `true` is specified, it becomes the same operation as specifying `writing-mode="from-page-master-region()"` and `reference-orientation="from-page-master-region()"` for `<fo:page-sequence>`. | `true` \| `false` | `false` |

### Typography Defaults

| Attribute | Description | Values | Default |
|-----------|-------------|--------|---------|
| `default-color` | Specifies the default color of text with the format of `#RRGGBB`. You can also specify the color name, `rgb()` or `rgb-icc()`. However, RGB cannot be omitted with `rgb-icc()`. | colors with the format of `#RRGGBB` | `#000000` |
| `default-font-size` | Specifies the default font size with the real type numerical value. | `<length>` | `10pt` |
| `normal-line-height` | Specifies the default line height with the real type numerical value. A unit is not specified. The value means the ratio to the font size. Therefore, in case the font size is 10pt, the line height becomes 12pt. | `<number>` | `1.2` |
| `bold-ratio` | Specifies how thick a font should be displayed when bold is specified for fonts that do not have bold in the font family. When `1.0` is specified, only the amount decided by the system is made thicker. For instance, when `1.5` is specified, it is drawn 1.5 times thicker. When `0.0` or less is specified, it is considered 1.0 thick. This setting is effective with PDF Output and PostScript Output. | `<number>` | `1.0` |
| `oblique-skew` | Specifies the amount of the inclination when using `font-style="oblique"` or `"backslant"`. When 0 or less is specified, it is considered the system default. The font is inclined by the system default whenever there is no italic in the font when using `font-style="italic"`. Effective in GUI, PDF Output, PostScript Output, and XPS Output. | `<integer>` | `0` |
| `pxpi` | Specifies the coefficient, which converts the value of the specified `px`, as "the number of pixels per inch" when formatting. | `<integer>` | `96` |

### Border Width Defaults

| Attribute | Description | Values | Default |
|-----------|-------------|--------|---------|
| `border-thin-width` | Specifies the default border width in thin style with the real type numerical value. | `<length>` | `1pt` |
| `border-medium-width` | Specifies the default border width in medium style with the real type numerical value. | `<length>` | `3pt` |
| `border-thick-width` | Specifies the default border width in thick style with the real type numerical value. | `<length>` | `5pt` |

### Language and Encoding

| Attribute | Description | Values | Default |
|-----------|-------------|--------|---------|
| `default-lang` | Specifies the default language code (ISO 639-2). Specifies the language when FO doesn't have the language specification. This is outputted as the language information to the PDF. When empty, the language specified to `default-lang2` is adopted. | code according to ISO 639-2 | (none) |
| `default-lang2` | Specifies the language actually adopted when `default-lang` is empty. When `default-lang2` is empty, it depends on the locale of the system. | code according to ISO 639-2 | `eng` |
| `default-CJK` | Specifies the language (such as `jpn` or `kor`) to be applied when a script is ambiguous for CJK. Although the default value is determined from the operating environment, Japanese language is assumed when the operating environment is other than CJK. | `chi` \| `jpn` \| `kor` | `jpn` |
| `default-html-charset` | Specifies the default encoding of HTML. This setting is applied to HTML with unknown encoding. When the setting is in HTML, or the encoding can be recognized by BOM, they are adopted. Case insensitive. | see encoding | `UTF-8` |

### Hyphenation

| Attribute | Description | Values | Default |
|-----------|-------------|--------|---------|
| `HyphenationOption` | Specifies whether to hyphenate words by using the custom processing that supports over 40 languages or to use TeX hyphenation dictionaries. If `false` is specified, words will be hyphenated by using TeX dictionaries. If so, only the languages that have a dictionary can be hyphenated. | `true` \| `false` | `true` |
| `hyphenation-TeX` | When `HyphenationOption="true"` is specified, enumerates a comma-delimited list of languages that you want to hyphenate using a TeX dictionary, e.g.: `hyphenation-TeX="ces,deu"`. | short names for TeX dictionaries | (none) |
| `hyphen-min` | Specifies whether to enable `<hyphen-min>` in the Hyphenation Exception Dictionary. `false`: `<hyphen-min>` is ignored. `true`: The value of `<hyphen-min>` is the value when `hyphenation-remain-character-count="auto"` or `hyphenation-push-character-count="auto"` in XSL is specified. It is invalid when any property other than auto is specified. `without-exceptions`: Same as `true`, but words specified in `<exceptions>` in the exception dictionary are excluded. | `true` \| `false` \| `without-exceptions` | `false` |
| `hyphenation-keep-mode` | Specifies the processing method when the word at the end of the page (column) is hyphenated by `hyphenation-keep="page"`, etc. `word` pushes out the word to the next page (column). `line` pushes out that line to the next page (column). In `<fo:float>` where the value of `axf:float-x` is other than `none` and the value of `axf:float-y` is `none`, it is always considered `line`. | `word` \| `line` | `word` |
| `double-hyphen-translineation` | In Portuguese hyphenation, a hyphen is also placed at the start of the line when a line break occurs at a hyphen. Specify comma-separated languages for such hyphenation. If you specify empty or `false`, you can cancel the process. It is invalid when `hyphenate="false"` is specified. | comma-separated languages | `por` |

### Line Breaking (BPIL)

| Attribute | Description | Values | Default |
|-----------|-------------|--------|---------|
| `bpil` | Specifies a language or script to apply Knuth-Plass Breaking Paragraphs into Lines [BPIL] to the line breaking algorithm by separating each code with a space. When empty, it does not apply to any language. Language codes (ISO 639 or ISO 639-2), language-country codes (ISO 3166, hyphen-separated), or script codes (ISO 15924) can be specified. When a script is specified, it is considered that the language for which it is a representative script has been specified. | language/script codes | `Latn Grek Cyrl Armn Geor` |
| `bpil-limit-chars` | Specifies the maximum number of characters to which [BPIL] applies. Approximately more than this number of blocks will not apply [BPIL]. The value less than 1000 cannot be specified. | `<number>` | `50000` |
| `bpil-minimum-line-width` | Specifies the minimum line width to apply [BPIL] in units of em. The value less than 1 is considered 1. | `<number>` | `8` |
| `bpil-penalty-hyphenation` | Specifies the frequency of hyphenation in [BPIL] with a value of 0 to 1000. Hyphenation is more likely to occur with smaller values. | `<number>` (0--1000) | `100` |

### Line Break Characters

| Attribute | Description | Values | Default |
|-----------|-------------|--------|---------|
| `abbreviation-character-count` | Specify the number of characters considered an abbreviation when a line break is inserted. See also `axf:abbreviation-character-count`. | `<number>` | `3` |
| `append-non-end-of-line-characters` | Specifies to append the non-end-of-line characters. White spaces are disregarded even though they are specified. See also `axf:append-non-end-of-line-characters`. | `<string>` | (none) |
| `append-non-starter-characters` | Specifies to append the non-starter characters. White space characters are disregarded even though they are specified. See also `axf:append-non-starter-characters`. | `<string>` | (none) |
| `except-non-end-of-line-characters` | Specifies the except-non-end-of-line characters. This setting will be ignored even if white spaces are specified. See also `axf:except-non-end-of-line-characters`. | `<string>` | (none) |
| `except-non-starter-characters` | Specifies the except-non-starter characters. This setting will be ignored even if white spaces are specified. See also `axf:except-non-starter-characters`. | `<string>` | (none) |
| `non-starter-ideographic-space` | Specifies whether to treat the ideographic space as a non-starter character. | `true` \| `false` | `true` |
| `avoid-orphan-single-word` | Polish, Hungarian, Czech, etc. are not allowed to have single letter words at the end of lines. Specify such languages separated by commas. You can cancel the process by specifying an empty string or `false`. Specify `true` to apply to all languages. | `pol` \| `hun` \| `ces` \| `true` \| `false` \| empty string | `pol, hun, ces` |

### CJK and Asian Typography

| Attribute | Description | Values | Default |
|-----------|-------------|--------|---------|
| `punctuation-spacing` | Specifies the space width between the adjacent Japanese full width characters with the percentage value. The value means the ratio to the font size. This setting affects the value of `axf:punctuation-spacing="auto"` in extended FO. | `<percentage>` | `50%` |
| `punctuation-trim` | When Japanese full width characters (punctuation marks and brackets) are used in succession or come at the start of a line, specifies whether to trim the letter spacing or keep the same letter spacing. If `true`, the letter spacing will be tracked narrow. If `false`, it will be the same as that of other full width characters. Affects `axf:punctuation-trim="auto"` and `axf:text-justify-trim="auto"`. | `true` \| `false` | `true` |
| `text-autospace` | Specifies whether to insert spaces surrounding ideographic glyphs to make them look better, in documents where ideographic and non-ideographic glyphs are mixed. Affects `axf:text-autospace="auto"`. | `true` \| `false` | `true` |
| `text-autospace-width` | Specifies the space width surrounding ideographic glyphs characters with the percentage value. The value means the ratio to the font size. Affects `axf:text-autospace-width="auto"`. | `<percentage>` | `25%` |
| `text-kashida-space` | Specifies the percentage of the Kashida in Arabic justification. The value indicates the percentage of white space and Kashida. If `0%`, Kashida is not inserted and only the white space expands. If `100%`, Kashida is inserted as much as possible. Affects `axf:text-kashida-space="auto"`. | `<percentage>` | `100%` |
| `ruby-align` | Specifies the arrangement when `axf:ruby-align="auto"` is specified. When nothing or `auto` is specified, it is considered `space-around center`. | `auto` | (none) |
| `jamo-ligature` | Specifies whether to process the ligature of Hangul Jamo (U+1100 to U+11FF). If `true`, processes the ligature. This setting affects `axf:ligature-mode="auto"`. This ligature uses jamo of GSUB feature in the OpenType font. | `true` \| `false` | `true` |
| `avoid-widow-words-cjk-punctuation` | Specifies the initial value when `axf:avoid-widow-words-cjk-punctuation="auto"` is specified. | `false` \| `true` \| `<string>` | `false` |
| `condensed-text-align-last` | Specifies the initial value when `axf:condensed-text-align-last="auto"` is specified. | `false` \| `true` \| `justify` | `justify` |

### Text Justification and Decoration

| Attribute | Description | Values | Default |
|-----------|-------------|--------|---------|
| `text-justify-mode` | In AH Formatter V5 or later, there are some changes from XSL Formatter V4 in trimming a line. `4`: Operates the same as XSL Formatter V4 (ideograph and inter-word specified). `5`: Adds the improved operation by AH Formatter V5. | `4` \| `5` | `5` |
| `text-decoration-mode` | Specifies how much the underline, strikethrough and overline exceed the length of a word. `0`: Do not exceed the word length. `1`: Exceed half-length of the space between words. `2`: Do not exceed the start edge of a word, but exceed the end edge of a word by the full space between words. | `0` \| `1` \| `2` | `1` |
| `text-underline-mode` | Some improved changes have been added for the position of underline and overline with AH Formatter V6. Specify when you want to make it the same as V5. `5`: Operates the same as V5. `6`: Adds the improved operation by V6. | `5` \| `6` | `6` |
| `justify-leader` | Although the leader functions in the justified line, the leader itself is not justified. `leader-alignment="none"` specifies whether the leader itself is justified or not when the contents are only the text, by `leader-pattern="dots"` or `leader-pattern="use-content"`. If `true`, space may be generated between characters in the leader, making it irregular against other leaders, but the space at the end of the leader will disappear. | `true` \| `false` | `false` |

### Font and Ligature Settings

| Attribute | Description | Values | Default |
|-----------|-------------|--------|---------|
| `pair-kerning` | Specifies whether to process the pair kerning. If `true`, the kerning will be processed. This setting affects `axf:kerning-mode="auto"`. | `true` \| `false` | `true` |
| `latin-ligature` | Specifies whether to process the ligature in European languages. If `true`, the ligature will be processed. This setting affects `axf:ligature-mode="auto"`. | `true` \| `false` | `true` |
| `family-name-syntax` | Specify whether to strictly check the syntax of the value of `font-family`. When `strict` is specified, it is evaluated exactly as the font-family property. `loose` loosens the check. If `auto` is specified, it is considered `strict` in CSS and `loose` in FO. For example, `font-family="Abc 123"` is strictly an error; you must specify `font-family="'Abc 123'"`. | `strict` \| `loose` \| `auto` | `auto` |

### Small Caps Emulation

| Attribute | Description | Values | Default |
|-----------|-------------|--------|---------|
| `small-caps-emulation-always` | Specifies whether to always emulate small-caps. When `true`, it always emulates and does not use the font information. | `true` \| `false` | `false` |
| `small-caps-emulation-size` | Specifies the scale-down ratio when the font does not have small-caps when `font-variant="small-caps"` is specified. | `<percentage>` | `70%` |
| `small-caps-emulation-x-height` | If the font has x-height and cap-height, the emulation magnification of small-caps is x-height/cap-height. If the font does not have them, it will be `small-caps-emulation-size`. | `true` \| `false` | `true` |

### Space Width Settings

| Attribute | Description | Values | Default |
|-----------|-------------|--------|---------|
| `fixed-width-space-treatment` | Specifies the treatment of a fixed-width white space for characters such as EM SPACE (U+2003). `false`: Does nothing. `true`: Inserts a white space when there is no glyph in the font. When there is a glyph in the font, it will be used. `always`: Always inserts a white space without depending on the font. Target characters and widths (in em): U+2000 EN QUAD: 1/2, U+2001 EM QUAD: 1, U+2002 EN SPACE: 1/2, U+2003 EM SPACE: 1, U+2004 THREE-PER-EM SPACE: 1/3, U+2005 FOUR-PER-EM SPACE: 1/4, U+2006 SIX-PER-EM SPACE: 1/6, U+2007 FIGURE SPACE: same width as "0", U+2008 PUNCTUATION SPACE: same width as ".", U+2009 THIN SPACE: depends on `thin-space-width`, U+200A HAIR SPACE: depends on `hair-space-width`, U+205F MEDIUM MATHEMATICAL SPACE: 4/18. | `true` \| `false` \| `always` | `true` |
| `thin-space-width` | Specifies the character width of THIN SPACE (U+2009) in units of em, when `fixed-width-space-treatment="true"` is specified. | `<number>` | `0.2` |
| `hair-space-width` | Specifies the character width of HAIR SPACE (U+200A) in units of em, when `fixed-width-space-treatment="true"` is specified. | `<number>` | `0.1` |

### Table Settings

| Attribute | Description | Values | Default |
|-----------|-------------|--------|---------|
| `table-auto-layout-limit` | When `table-layout="auto"` is specified, the number of rows to read ahead can be limited because it takes a long time to read all rows in a huge table. If `0` is specified, all rows are read. | `<integer>` | `100` |
| `table-is-reference-area` | In XSL 1.1, there is no compatibility with XSL 1.0 about whether to make `<fo:table>` a reference area. If `true`, `fo:table` will be made a reference area and its operation will be the same as XSL 1.0. | `true` \| `false` | `false` |
| `justify-rowspan-height` | When there is a cell with rowspan and the height of the cell is high, specifies whether the height of each row occupied by the cell should be as even as possible. | `true` \| `false` | `false` |
| `tab-overlap-treatment` | Specifies a behavior when tab alignment makes letters overlapped. See `axf:tab-overlap-treatment`. | `ignore-tab` \| `next-tab` | `ignore-tab` |

### Footnote Settings

| Attribute | Description | Values | Default |
|-----------|-------------|--------|---------|
| `auto-break-footnote` | Specifies whether to break the footnote automatically when `axf:footnote-max-height` is specified. | `true` \| `false` | `true` |
| `keep-footnote-anchor` | When a block including a footnote anchor does not fit within the page, the lines up to the dividable position after the anchor are sent to the previous page. | `true` \| `false` | `true` |

### Overflow Settings

| Attribute | Description | Values | Default |
|-----------|-------------|--------|---------|
| `overflow-limit-block` | Specifies the default value of `axf:overflow-limit-block`. | `<length>` | `0pt` |
| `overflow-limit-inline` | Specifies the default value of `axf:overflow-limit-inline`. | `<length>` | `0pt` |
| `error-if-overflow` | Specifies whether to perform the same check as `error-if-overflow` and report an overflow error when `overflow="auto"` is specified. | `true` \| `false` | `false` |

### Shadow and Resolution Settings

| Attribute | Description | Values | Default |
|-----------|-------------|--------|---------|
| `boxshadow-resolution-dpi` | Specifies the resolution of the image when setting the blurring in `box-shadow` with the unit of dpi. Values from 70 to 1440 are effective. If out of range, the default value is adopted. | 70--1440 | `108` |
| `textshadow-resolution-minimum-dpi` | Specifies the minimum value of the resolution of the image when setting the blur in `text-shadow` with the unit of dpi. Only integer values >= 1 are effective. | `<integer>` | `108` |
| `textshadow-resolution-pixel-per-em` | Specifies the resolution of the image when setting the blur in `text-shadow` by the number of pixels per 1 font size. If the back-calculated dpi value is smaller than `textshadow-resolution-minimum-dpi`, the latter setting takes priority. Only integer values >= 1 are effective. | `<integer>` | `100` |
| `textshadow-blur-cannot-embed-font` | Selects whether to set the blur against the font that is not allowed to be embedded in `text-shadow`. If `true`, sets the blur. | `true` \| `false` | `false` |

### Vertical Writing Mode

| Attribute | Description | Values | Default |
|-----------|-------------|--------|---------|
| `text-orientation-mode` | Specifies whether UAX#50 (Unicode Vertical Text Layout) is taken into consideration by `axf:text-orientation` when rendering alphanumeric characters to be upright in vertical writing mode. `5`: UAX#50 is not taken into consideration. `6`: SVO and MVO are taken into consideration. `7`: In addition to 6, `axf:text-orientation="auto"` is treated as "mixed". Note: This setting does not work with AH Formatter V7.2 Lite (always considered 5). | `5` \| `6` \| `7` | `6` |
| `vertical-block-width-mode` | The behavior of the auto value of the width of vertical-text block within horizontal-text flow is changed with AH Formatter V6. `5`: Operates the same as V5 (width given by the width of the outer area). `6`: Adds the improved operation by V6 (width shrinks to fit the content). | `5` \| `6` | `6` |
| `vertical-underline-side` | Specifies whether to place the underline in vertical writing mode on the right side or on the left side. If `auto`, the underline is placed on the right side when the language is Japanese or Korean, and on the left side otherwise. Affects `axf:vertical-underline-side="auto"`. | `auto` \| `left` \| `right` | `auto` |

### Bidirectional Text

| Attribute | Description | Values | Default |
|-----------|-------------|--------|---------|
| `unicode-bidi-rev` | Specifies the revision of UAX#9 (Unicode Bidirectional Algorithm) that AH Formatter conforms to. A value >= 37 is considered 41. If the value is less than 37, it follows the algorithm compatible with V6.6 (about revision 27). At that time, U+2066 is considered U+202D, U+2067 is considered U+202E, and U+2069 is considered U+202C. If no value is set, the latest revision supported by AH Formatter is used. | `<integer>` | (none) |

### Unicode Normalization

| Attribute | Description | Values | Default |
|-----------|-------------|--------|---------|
| `normalize` | Specifies the method of the normalization to be adopted when `axf:normalize="auto"` is specified. `none`: Does not normalize text. `nfc`: Performs NFC. `nfd`: Performs NFD. `nfkc`: Performs NFKC. `nfkd`: Performs NFKD. | `none` \| `nfc` \| `nfd` \| `nfkc` \| `nfkd` | `nfc` |

### White Space Handling

| Attribute | Description | Values | Default |
|-----------|-------------|--------|---------|
| `white-space-collapse-mode` | The operation of `white-space-collapse` was corrected with AH Formatter V7. `6`: Operates the same as V6. `7`: Adds the modified operation by V7. | `6` \| `7` | `7` |
| `zwsp-mode` | The operation of ZERO WIDTH SPACE (U+200B) was corrected with AH Formatter V6. `5`: Operates the same as V5. `6`: Adds the modified operation by V6. | `5` \| `6` | `6` |

### Baseline and Compatibility Mode

| Attribute | Description | Values | Default |
|-----------|-------------|--------|---------|
| `baseline-mode` | In AH Formatter V6, there are some changes from XSL Formatter V4 in deciding the baseline in the text with different scripts like a mixture of Western and Japanese. `4`: Operates the same as V4. `5`: Adds the improved operation by V5. `6`: Adds the improved operation by V6. When `baseline-mode="4"` is specified, the `text-altitude` and `text-depth` properties are invalid. | `4` \| `5` \| `6` | `6` |
| `intrusion-displace-mode` | In AH Formatter V6, there are some changes from V5 in the behavior of the `intrusion-displace` property. `5`: Operates the same as V5. `6`: Adds the modified operation by V6. | `5` \| `6` | `6` |

### Printer Marks

| Attribute | Description | Values | Default |
|-----------|-------------|--------|---------|
| `printer-marks-line-length` | Specifies the length of the printer marks. | `<length>` | `10mm` |
| `printer-marks-line-width` | Specifies the width of the printer marks. | `<length>` | `0.24pt` |
| `printer-marks-zero-margin` | Specifies the margin between the page and the printer marks when `axf:bleed` is 0. | `<length>` | `3mm` |

### Watermark Settings

| Attribute | Description | Values | Default |
|-----------|-------------|--------|---------|
| `watermark-text` | Displays the specified watermark text on each page. Possible to make it multiple lines by delimiting with the line feed `&#10;`. Complex scripts such as Thai and Arabic cannot be specified. The text that cannot be outputted by a single font cannot be specified. | `<string>` | (none) |
| `watermark-font-family` | Specifies the font family for the watermark text. | `<family-name>` \| `<generic-family>` | `sans-serif` |
| `watermark-font-style` | Specifies the font style for the watermark text. | `normal` \| `italic` | `normal` |
| `watermark-font-weight` | Specifies the font weight for the watermark text. | `normal` \| `bold` \| `<integer>` (1--1000) | `normal` |
| `watermark2-text` | Displays the specified second watermark text on each page. Complex scripts such as Thai and Arabic cannot be specified. | `<string>` | (none) |
| `watermark2-font-family` | Specifies the font family for the second watermark text. If not specified, the default value is the same as `watermark-font-family`. | `<family-name>` \| `<generic-family>` | `watermark-font-family` |
| `watermark2-font-style` | Specifies the font style for the second watermark text. | `normal` \| `italic` | `normal` |
| `watermark2-font-weight` | Specifies the font weight for the second watermark text. | `normal` \| `bold` \| `<integer>` (1--1000) | `normal` |

### SVG and Image Handling

| Attribute | Description | Values | Default |
|-----------|-------------|--------|---------|
| `inherit-svg-fill-color` | In SVG, when "fill" in the root element is omitted, the value of "color" specified in the upper XML is inherited. | `true` \| `false` | `false` |
| `responsive-svg-size` | Specifies whether the size matches the viewBox setting when the width and height of the root element are omitted in SVG. `reference`: It is considered `width="100%" height="100%"` according to the SVG specification. `viewBox`: If viewBox is specified as the root element, it is considered its size. | `reference` \| `viewBox` | `reference` |
| `display-alttext` | Specifies whether to display an alternate text by `axf:alttext` or the `alt` attribute when there is no image in `<fo:external-graphic>` or HTML `<img>`. When `true`, an alternate text is displayed. When `false` and the `src` attribute is specified, an alternate image is displayed. | `true` \| `false` | `false` |
| `issue-scale-to-fit` | Specifies whether to report the scale-change ratio when the scale ratio of the image is changed by `scale-to-fit`/`scale-down-to-fit`/`scale-up-to-fit`. If `true`, level 1 is reported. | `true` \| `false` | `false` |

### HTML and CSS Processing

| Attribute | Description | Values | Default |
|-----------|-------------|--------|---------|
| `auto-formatter-type` | When the detection of formatting type is set automatically and the decision of XHTML or HTML is unclear, the priority can be given by specifying `html` or `xhtml`. | `html` \| `xhtml` | `html` |
| `href-page-link` | Unlike FO, HTML has `id` values that are not NCName, so id like "123" is allowed. When `href-page-link="true"` is specified, `<a href="#123">` will be considered a page number and easily move to the specified page in HTML. | `true` \| `false` | `false` |
| `axf-formatter-config` | Specifies whether the use of `<axf:formatter-config>` is permitted. When `false` is specified, `<axf:formatter-config>` will be ignored. | `true` \| `false` | `true` |

### Printing (Windows)

| Attribute | Description | Values | Default |
|-----------|-------------|--------|---------|
| `PrinterOrientation` | When the paper is placed in landscape in the PS Printer, there may be a case that the printer rotate-output the line and EPS incorrectly. Possible to correct the rotation by specifying an anti-clockwise rotation degree. This setting is effective only with Windows version. | `auto` \| `0` \| `90` \| `270` | `auto` |
| `PscriptPassThrough` | Makes Pass Through output invalid when outputting to PS printer. If `true`, Pass Through output is executed. If `false`, the output is executed only by GDI operator. This setting is effective only with Windows version. | `true` \| `false` | `true` |
| `SeparatePrinterDuplexJob` | Specifies whether to batch print without interrupting a job for printing, even if the switching of the printer between simplex/duplex modes is set when `axf:printer-duplex` is specified. If `true`, the file is split and outputted; if `false`, the file is batch printed. | `true` \| `false` | `true` |

### Security and External Access

| Attribute | Description | Values | Default |
|-----------|-------------|--------|---------|
| `descendant-or-self-files` | When `true` is specified, the location of the external files that can be read is restricted to be within the same directory as the FO or HTML, or within a subdirectory of it. It is not restricted by `http:` or `https:`. If `disable-network` is specified, all network access such as `http:` or `https:` are also restricted. | `true` \| `false` | `false` |
| `external-entity` | Specifies whether the external reference is allowed or not with `<!ENTITY>` of XML (FO, XHTML, SVG, MathML etc.) to be formatted. Note that it does not work on external XSLT processor called from AH Formatter V7.2. | `false` \| `true` | `true` |
| `ignore-certificate-error` | Listed in the attribute list of `<formatter-settings>`. No detailed description in source. | (not detailed in source) | (not specified) |

### Formatting Behavior

| Attribute | Description | Values | Default |
|-----------|-------------|--------|---------|
| `two-pass-formatting` | When formatting a huge document with a large amount of unresolved `<fo:page-number-citation>`, large amounts of memory are consumed. This parameter makes the formatting two passes. Processing time may increase but memory consumption will be extremely decreased. This setting is invalid with CSS formatting and GUI. | `true` \| `false` | `false` |
| `no-disp-warnings` | Suppress Error Messages that are output on GUI or Command-line. Specifies by enumerating the error code in decimal or hexadecimal, e.g. `no-disp-warnings="10754 0x320D"`. It is invalid for errors where the processing is interrupted. | `<string>` | (none) |
| `unresolved-internal-destination` | Listed in the attribute list of `<formatter-settings>`. No detailed description in source. | (not detailed in source) | (not specified) |

---

## Child Elements of `<formatter-settings>`

### `<list-style-type>`

<!-- Source: XSL-FO-Reference-74-MID.pdf p.251 -->

Specifies the character to use by `list-style-type`.

**Parent:** `<formatter-settings>`

**Attributes:** `box`, `check`, `circle`, `diamond`, `disc`, `hyphen`, `square`

**Values:** `<character>`

**Defaults:**

| Attribute | Default Character |
|-----------|-------------------|
| `box` | U+25AB |
| `check` | U+2713 |
| `circle` | U+25E6 |
| `diamond` | U+2666 |
| `disc` | U+2022 |
| `hyphen` | U+2043 |
| `square` | U+25AA |

### `<quotationmark>`

<!-- Source: XSL-FO-Reference-74-MID.pdf p.251 -->

Changes the handling of Quotation Mark. Specify the language code for `language`, the character code of quotation marks for `code`, and specify one of `QU` | `OP` | `CL` for `quotetype`. Only Western languages can be specified for the language code. CJK etc. cannot be specified.

**Parent:** `<formatter-settings>`

**Attributes:** `language`, `code`, `quotetype`

### `<script-chars>`, `<space-end-punctuation>`, `<space-start-punctuation>`, `<space-between-digit-and-punctuation>`, `<space-between-punctuation-and-digit>`

<!-- Source: XSL-FO-Reference-74-MID.pdf p.252 -->

These elements are used to specify certain character and space mappings, especially for Asian languages. For details see the Online Manual of the AH XSL Formatter (file: `ahf-optset.html`).

**Parent:** `<formatter-settings>`

### `<usercss>`

<!-- Source: XSL-FO-Reference-74-MID.pdf p.252 -->

Specifies the CSS user stylesheet you want to add by `<css>`.

**Parent:** `<formatter-settings>`

**Child element:** `<css>`

### `<css>`

<!-- Source: XSL-FO-Reference-74-MID.pdf p.252 -->

Specifies the path of the CSS user stylesheet.

**Parent:** `<usercss>`

**Attribute:** `path`

**Default:** (none)

### `<script-language-in-CJK>`

<!-- Source: XSL-FO-Reference-74-MID.pdf pp.252–253 -->

When the script specified to the `script` attribute appears in the sentence of CJK languages, the character string of the script is considered the language that is specified to the `language` attribute. The CJK languages cannot be specified to `language`. When nothing is specified to the `language` attribute, the language specification to the `script` attribute is canceled.

**Parent:** `<formatter-settings>`

**Attributes:** `script`, `language`

<!-- Source: XSL-FO-Reference-74-MID.pdf p.252 -->
```xml
<script-language-in-CJK script="Latn" language="eng"/>
```

The `Latn` character string that appears in Japanese or Chinese sentences can be recognized as English. If `hyphenate="true"` is specified, the hyphenation can be processed by considering this part as English.

### `<multimedia>`

<!-- Source: XSL-FO-Reference-74-MID.pdf p.253 -->

When specifying multimedia, such as audio or video as graphics, the setting of `content-type` is required. AH Formatter may sometimes not automatically recognize if a content-type other than `audio/*` or `video/*` formats indicates it is multimedia. For such content-type, specify `audio`, `video` or `flash` explicitly.

**Parent:** `<formatter-settings>`

**Attributes:** `video`, `audio`, `flash`

By default, `audio/*` is considered as audio, `video/*` as video, `application/x-shockwave-flash` as Flash.

<!-- Source: XSL-FO-Reference-74-MID.pdf p.253 -->
```xml
<multimedia flash="application/x-shockwave-flash"/>
```

### `<GS1-128>`

<!-- Source: XSL-FO-Reference-74-MID.pdf pp.253–254 -->

Registers the format of application identifier (AI) of GS1-128. Some formats of AI have been already registered, but you can specify when you change the format or the format is not registered. AI is a number with 2 to 4 digits. AI starting from 0 should be 2 digits. The last digit can be set as `*` if AI is a 3 or 4 digit number. For instance, `AI="380*"` indicates 3800 to 3809.

The following formats can be specified to the `format` attribute:
- `n3`: 3-digit numbers
- `x3`: 3-digit arbitrary characters
- `n-10`: Numbers with >= 1 and <= 10 digits
- `x3-10`: Arbitrary characters with >= 3 and <= 10 digits

**Parent:** `<formatter-settings>`

**Attributes:** `AI`, `format`

<!-- Source: XSL-FO-Reference-74-MID.pdf p.254 -->
```xml
<GS1-128 AI="380*" format="n-15"/>
```

### `<UAX50>`

<!-- Source: XSL-FO-Reference-74-MID.pdf p.254 -->

Specifies the code point to change. The code point can be specified as:
- One character: `"` or `&#x201C;`, etc.
- 4-digit hexadecimal numbers: `201C`
- Set of 4-digit hexadecimal numbers: `202A - 202E`

Characters greater than or equal to U+10000 cannot be specified. `U` or `R` or `V` can be specified to `SVO` or `MVO`. `U` renders upright, `R` rotates 90-degree clockwise. `V` is same as `U`, but when vertical writing glyph is designed to rotate 90-degree counterclockwise originally, it is displayed by rotating 90-degree clockwise. See also `text-orientation-mode`.

**Parent:** `<formatter-settings>`

**Attributes:** `code`, `SVO`, `MVO`

### `<unbreakable-words>`

<!-- Source: XSL-FO-Reference-74-MID.pdf pp.255–256 -->

Lists the unbreakable words by the line break. The character string of each line will become unbreakable. The leading and trailing white spaces (U+0009, U+0020) will be discarded. Consecutive white spaces (U+0009, U+0020) are grouped together and match consecutive white spaces (U+0009, U+000A, U+000D, U+0020) including line breaks.

Because the first phrase found from the beginning of the character string is the target, and AH Formatter tries to adopt as long a phrase as possible, ordering matters. It is case sensitive.

Note:
- This processing is performed for character string of input XML. It is performed before processing `axf:normalize` or `axf:text-replace`, etc.
- If a character string that causes ligature, for example, `ffi` is specified as unbreakable up to `ff`, ligature as `ffi` will not occur.

**Parent:** `<formatter-settings>`

**Attribute:** `src`

#### `src` attribute

You can specify external XML for `src`. That XML looks the same as this element, but `src` cannot be specified.

**Applies to:** `<unbreakable-words>`

**Values:** `<uri-specification>`

**Default:** (none)

<!-- Source: XSL-FO-Reference-74-MID.pdf p.255 -->
```xml
<unbreakable-words>
こんにちは
Hello World
</unbreakable-words>
```

In this example, two phrases will become unbreakable. Any of the following will also become unbreakable: "Hello World", "Hello    World", or "Hello" followed by a line break and "World".
