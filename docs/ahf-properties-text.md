# Antenna House Extension Properties: Text Extension Properties

<!-- Source: XSL-FO-Reference-74-MID.pdf pp.312-476 -->

Properties for text handling including text alignment extensions, autospacing, text combination (tate-chu-yoko), text stroke, text decoration line styling, text overflow, word break, word wrap, and URL break control.

## axf:text-align-first

Specifies the text alignment of the first line. Specifies the alignment of the child of the first line area and the alignment of the line coming right after the line with U+000A at the end. Priority is given above text-align-last.

Values have the following meanings:
- `relative`: Does nothing. axf:text-align-first is invalid.
- `start`, `center`, `end`, `justify`, `inside`, `outside`, `left`, `right`: Same as text-align or text-align-last.

| Attribute | Value |
|---|---|
| **Applies to** | fo:block |
| **Values** | relative \| start \| center \| end \| justify \| inside \| outside \| left \| right |
| **Initial** | relative |
| **Inherited** | yes |

## axf:text-align-string

Specifies the text alignment when text-align="&lt;string&gt;". Although the specification of &lt;string&gt; to fo:table-cell aligns the character position of decimal point, etc., there is no definition for the alignment of the whole character string. At a default, AH XSL Formatter displayed it right aligned according to the illustration of 17.5.4 Horizontal alignment in a column. AH XSL Formatter extends the alignment and makes it possible to align left or align center.

Values have the following meanings:
- `start`, `center`, `end`, `inside`, `outside`, `left`, `right`: Same as text-align or text-align-last.

| Attribute | Value |
|---|---|
| **Applies to** | fo:table-cell |
| **Values** | start \| center \| end \| inside \| outside \| left \| right |
| **Initial** | end |
| **Inherited** | yes |

## axf:text-autospace

Specifies whether to add space surrounding ideographic glyphs or not. The initial value of whether space is added or not can be set by text-autospace in the Option Setting File. It can also be set in the Format Option Setting Dialog in the GUI.

Values have the following meanings:
- `none`: Space is not added.
- `ideograph-numeric`: Space is added between ideograph character and non-ideographic number character. Non-ideographic number character mentioned here indicates the character of Nd classified by Unicode and the non-full-width character.
- `ideograph-alpha`: Space is added between ideograph character and non-ideographic alphabet character. Non-ideographic alphabet character mentioned here indicates the character of Lu, Ll, Lt and Lm classified by Unicode.
- `ideograph-parenthesis`: Space is added between ideograph character and non-ideographic parenthesis character. However space is not added between ideograph character and non-ideographic closing parenthesis or between non-ideographic opening parenthesis and ideograph character.
- `auto`: Dependent on the system setting. It's considered axf:text-autospace="none" or axf:text-autospace="ideograph-numeric ideograph-alpha" according to the setting.

| Attribute | Value |
|---|---|
| **Applies to** | all block-level and inline-level formatting objects |
| **Values** | none \| [ ideograph-numeric \|\| ideograph-alpha \|\| ideograph-parenthesis ] \| auto |
| **Initial** | auto |
| **Inherited** | yes |

## axf:text-autospace-width

Specifies the width for axf:text-autospace.

Values have the following meanings:
- `<length>`: Specifies the amount of the space with an absolute value.
- `<percentage>`: It's a relative setting to the font size when actually applied.
- `auto`: Dependent on the system setting. This is the value specified by text-autospace-width in the Option Setting File.

| Attribute | Value |
|---|---|
| **Applies to** | all block-level and inline-level formatting objects |
| **Values** | &lt;length&gt; \| &lt;percentage&gt; \| auto |
| **Initial** | auto |
| **Inherited** | yes |

## axf:text-combine-horizontal

Sets horizontal-in-vertical composition in vertical writing mode automatically.

CAUTION: Automatic horizontal-in-vertical composition is not recommended to use in any other way than axf:text-orientation="upright". Automatic horizontal-in-vertical composition is invalid in the following cases. Emphasis marks in horizontal-in-vertical composition will be deleted:
- In horizontal writing mode (includes the case where the value for axf:text-orientation is sideways in horizontal-in-vertical composition)
- When languages other than CJK are specified
- Within ruby
- Character strings generated dynamically, such as fo:page-number.

Values have the following meanings:
- `none`: Does not set horizontal-in-vertical composition.
- `all`: The whole element which consists of only text is set to horizontal-in-vertical composition.
- `digits <integer>`: A sequence of consecutive numbers (0-9) that are less than or equal to the digit number specified by &lt;integer&gt; is set to horizontal-in-vertical composition.
- `alpha <integer>`: A sequence of consecutive alphabetic characters (A-Z, a-z) that are less than or equal to the digit number specified by &lt;integer&gt; is set to horizontal-in-vertical composition.
- `alphanumeric <integer>`: A sequence of consecutive alphanumeric characters (0-9, A-Z, a-z) that are less than or equal to the digit number specified by &lt;integer&gt; is set to horizontal-in-vertical composition.
- `emoji`: Makes the emoji horizontal-in-vertical composition.

| Attribute | Value |
|---|---|
| **Applies to** | all block-level and inline-level formatting objects |
| **Values** | none \| all \| [ &lt;integer&gt; \|\| alpha &lt;integer&gt; \|\| alphanumeric &lt;integer&gt; \|\| emoji ] |
| **Initial** | none |
| **Inherited** | yes |

## axf:text-indent-if-first-on-page

Specifies the text-indent of a block at the top of the page or the top of the column.

Values have the following meanings:
- `<length>`, `<percentage>`: When the block comes to the top of the page or column, if the first line is on that page or column, the value of this property substitutes for the value of text-indent.
- `auto`: Does nothing.

| Attribute | Value |
|---|---|
| **Applies to** | fo:block, fo:block-container |
| **Values** | &lt;length&gt; \| &lt;percentage&gt; \| auto |
| **Initial** | auto |
| **Inherited** | yes |

## axf:text-justify

Specifies how to justify text.

Values have the following meanings:
- `auto`: Uses the best text justification method for the script. For instance, in case of Japanese Kanji, Hiragana and Katakana, spaces between letters are expanded. In case of Arabic scripts, Kashida is used while spaces between words are expanded for the other scripts.
- `inter-word`: Justifies text by expanding the space between words.
- `inter-character`: Justifies text by expanding the space between letters.
- `distribute`: Changed to inter-character with CSS Text 2017-08-22. Also accepted for compatibility.

CAUTION: If inter-character is specified, kerning and ligature are limited.

| Attribute | Value |
|---|---|
| **Applies to** | all block-level and inline-level formatting objects |
| **Values** | auto \| inter-word \| inter-character \| distribute |
| **Initial** | auto |
| **Inherited** | yes |

## axf:text-justify-trim

Specifies the way to trim in text justification. Trim the spaces between characters as specified so that text fits into a line. When axf:punctuation-trim="all" is specified, there may be no more space to trim.

Values have the following meanings:
- `none`: Do not trim Japanese text.
- `punctuation`: Trim text with parentheses, middle dots, and punctuations of full width in Japanese.
- `punctuation-except-fullstop`: Behaves as the same as the punctuation value except for U+3002 IDEOGRAPHIC FULL STOP and U+FF0E FULLWIDTH FULL STOP.
- `punctuation-except-middledot`: Behaves as the same as the punctuation value except for U+30FB KATAKANA MIDDLE DOT, U+FF1A FULLWIDTH COLON, and U+FF1B FULLWIDTH SEMICOLON.
- `kana`: Trim Hiragana and Katakana a bit.
- `ideograph`: Trim spaces between Kanji or Kana.
- `inter-word`: Trim spaces between Western words.
- `auto`: Dependent on the system setting. This is the value specified by punctuation-trim and text-justify-mode in the Option Setting File. However, when axf:avoid-widow-words is enabled, it is considered that axf:text-justify-trim="ideograph inter-word" is specified.

| Attribute | Value |
|---|---|
| **Applies to** | all block-level and inline-level formatting objects |
| **Values** | none \| [ punctuation \|\| punctuation-except-fullstop \|\| punctuation-except-middledot \|\| [ kana \| ideograph ] \|\| inter-word ] \| auto |
| **Initial** | auto |
| **Inherited** | yes |

## axf:text-kashida-space

Specifies the percentage of Kashida in Arabic justification. The initial value of the percentage can be set by text-kashida-space in the Option Setting File.

Values have the following meanings:
- `<percentage>`: Indicates the percentage of white space and Kashida. If the value is 0%, Kashida is not inserted and only the white space expands as well as the normal justification. If the value is 100%, Kashida is inserted as much as possible. The value should be from 0% to 100%.
- `auto`: Dependent on the system setting.

| Attribute | Value |
|---|---|
| **Applies to** | all block-level and inline-level formatting objects |
| **Values** | &lt;percentage&gt; \| auto |
| **Initial** | auto |
| **Inherited** | yes |

## axf:text-line-color

Specifies the color of underline, strikethrough, and overline.

| Attribute | Value |
|---|---|
| **Applies to** | all elements with and generated content with textual content |
| **Values** | auto \| &lt;color&gt; |
| **Initial** | the value of the 'color' property |
| **Inherited** | no |

## axf:text-line-style

Specifies the style of underline, strikethrough, and overline. `none` cannot be specified to &lt;border-style&gt;.

| Attribute | Value |
|---|---|
| **Applies to** | all elements with and generated content with textual content |
| **Values** | &lt;border-style&gt; |
| **Initial** | solid |
| **Inherited** | no |

## axf:text-line-width

Specifies the width of underline, strikethrough, and overline.

| Attribute | Value |
|---|---|
| **Applies to** | all elements with and generated content with textual content |
| **Values** | auto \| &lt;border-width&gt; |
| **Initial** | auto |
| **Inherited** | no |

## axf:text-orientation

Specifies the orientation of text in vertical writing mode. This property is not effective in horizontal writing mode. In addition, complicated scripts, such as Arabic or Thai, cannot be rendered upright.

Values have the following meanings:
- `mixed`: Rotates alphanumeric characters, etc. 90-degree clockwise.
- `upright`: Renders all the characters upright except for punctuation marks, such as parentheses.
- `sideways-rl`, `sideways`: Rotates all the characters 90-degree clockwise. This has the same effect as setting some parts in horizontal layout in the vertical writing mode.
- `none`: Dependent on the system. Although the operation is close to mixed, which character is rotated is decided by considering the compatibility with the old version.
- `auto`: It is considered mixed when the value of text-orientation-mode is 7 in the Option Setting File, none when the value is less than or equal to 6.

It is always considered axf:word-break="break-all", hyphenate="false" in upright character strings.

| Attribute | Value |
|---|---|
| **Applies to** | all block-level and inline-level formatting objects |
| **Values** | mixed \| upright \| sideways-rl \| sideways \| none \| auto |
| **Initial** | auto |
| **Inherited** | yes |

## axf:text-overflow

Specifies the display method at the end of the content when overflowing in the inline progression direction. This feature is effective only when overflow="hidden" is specified. It has no effect on the overflow in the block progression direction.

When overflowing with only the first one character (or an object such as the first image), an ellipsis (abbreviated character string) is not added and it is treated as clip. If the first one character (or an object such as the first image) does not overflow, but if it overflows when an ellipsis (abbreviated character string) is attached, the ellipsis (abbreviated character string) is also displayed.

Values have the following meanings:
- `clip`: When overflowing in the inline progression direction, no processing is performed.
- `ellipsis`: When overflowing in the inline progression direction, narrow the display area by the extent that the ellipsis (U+2026) is entered, and then insert the ellipsis at the end.
- `<string>`: When overflowing in the inline progression direction, narrow the display area by the extent that the character string is entered, and then insert the specified character string at the end.

| Attribute | Value |
|---|---|
| **Applies to** | block level elements |
| **Values** | clip \| ellipsis \| &lt;string&gt; |
| **Initial** | clip |
| **Inherited** | no |

## axf:text-replace

Replaces the character strings. When it is simultaneously specified with text-transform or axf:number-transform, axf:text-replace will be evaluated last.

Values have the following meanings:
- `none`: Does nothing.
- `<string> <string>`: The first pair of character strings is replaced by the latter character strings. You have to specify a character string by a pair. It is not replaced when character strings are odd pieces or the first character string is empty. White space characters will be replaced after being processed by white-space-treatment, etc.

| Attribute | Value |
|---|---|
| **Applies to** | all block-level and inline-level formatting objects |
| **Values** | none \| [ &lt;string&gt; &lt;string&gt; ]+ |
| **Initial** | none |
| **Inherited** | yes |

## axf:text-stroke

Specifies the stroke of the character. This is a shorthand property for axf:text-stroke-width and axf:text-stroke-color.

CAUTION: This property is valid for GUI and PDF output, SVG output. Ignored on other outputs.

CAUTION: Contiguous character strings such as Arabic or Devanagari draw strokes at character boundaries.

| Attribute | Value |
|---|---|
| **Applies to** | all block-level and inline-level formatting objects |
| **Values** | &lt;length&gt; &lt;color&gt;? \| &lt;color&gt; |
| **Initial** | 0pt transparent |
| **Inherited** | yes |

## axf:text-stroke-color

Specifies the stroke color of the character. Strokes are not drawn when these are transparent.

CAUTION: This property is valid for GUI and PDF output, SVG output. Ignored on other outputs.

CAUTION: Contiguous character strings such as Arabic or Devanagari draw strokes at character boundaries.

| Attribute | Value |
|---|---|
| **Applies to** | all block-level and inline-level formatting objects |
| **Values** | &lt;color&gt; |
| **Initial** | transparent |
| **Inherited** | yes |

## axf:text-stroke-width

Specifies the stroke width of the character. Strokes are not drawn when these are less than or equal to 0.

CAUTION: This property is valid for GUI and PDF output, SVG output. Ignored on other outputs.

CAUTION: Contiguous character strings such as Arabic or Devanagari draw strokes at character boundaries.

| Attribute | Value |
|---|---|
| **Applies to** | all block-level and inline-level formatting objects |
| **Values** | &lt;length&gt; |
| **Initial** | 0pt |
| **Inherited** | yes |

## axf:text-treat-as

Specifies the character string treatable for trimming space between ideograph character and non-ideographic alphabet character and full width punctuation.

| Attribute | Value |
|---|---|
| **Applies to** | inline formatting objects |
| **Values** | &lt;string&gt; [both \| start \| end]? |
| **Initial** | empty string |
| **Inherited** | no |

## axf:text-underline-position

Specifies the position of underline.

Values have the following meanings:
- `auto`: The underline is placed on the automatically adjusted position. The specification of axf:vertical-underline-side in vertical writing mode is effective.
- `before-edge`: The underline is placed on the before-edge. When &lt;percentage&gt; or &lt;length&gt; is not specified, the upper end of the height of an underline is placed on the before-edge. When &lt;percentage&gt; or &lt;length&gt; is specified, the center of the height of an underline is placed on the before-edge.
- `alphabetic`: The underline is placed on the position of the baseline. When &lt;percentage&gt; or &lt;length&gt; is not specified, the upper end of the height of an underline is placed on the baseline. When &lt;percentage&gt; or &lt;length&gt; is specified, the center of the height of an underline is placed on the baseline.
- `after-edge`: The underline is placed on the after-edge. When &lt;percentage&gt; or &lt;length&gt; is not specified, the upper end of the height of an underline is placed on the after-edge. When &lt;percentage&gt; or &lt;length&gt; is specified, the center of the height of an underline is placed on the after-edge.
- `<percentage>`, `<length>`: The underline position is shifted by the specified amount. When the underline is placed on the right side by axf:vertical-underline-side, it is moved to the opposite direction of the left side.

| Attribute | Value |
|---|---|
| **Applies to** | all elements with and generated content with textual content |
| **Values** | auto \| [ [ before-edge \| alphabetic \| after-edge ] \|\| [ &lt;percentage&gt; \| &lt;length&gt; ] ] |
| **Initial** | auto |
| **Inherited** | yes |

## axf:url-break

Specifies how to perform the line breaking in a URL.

Values have the following meanings:
- `normal`: Follows a normal line breaking rule.
- `chicago`: Breaks lines for substrings such as URLs in text, as in The Chicago Manual of Style. That is, follows these rules:
  - Disallows breaking after /.
  - Allows breaking before a single / other than at the end of the URL. (Disallows breaking before //.)
  - Other than these, follows a normal line breaking rule.

CAUTION: Whether a string is a URL does not determine whether it strictly follows the URL syntax. It is determined only by whether it starts with http://, https:// or file://.

| Attribute | Value |
|---|---|
| **Applies to** | all block-level and inline-level formatting objects |
| **Values** | normal \| chicago |
| **Initial** | normal |
| **Inherited** | yes |

## axf:vertical-underline-side

Specifies on which side of the text to put underline in vertical writing-mode. This property is effective only when axf:text-underline-position="auto" is specified. The overline is placed on the opposite position of the underline.

The initial value of the underline position can be set by vertical-underline-side in the Option Setting File. It can also be set in the Format Option Setting Dialog in the GUI.

When axf:vertical-underline-side="auto" is specified and the initial value of the system is also auto, the underline is placed on the right side when the language property is Japanese (jpn) or Korean (kor). The underline is placed on the left side when the language property is other than Japanese (jpn) or Korean (kor). If there is no language properties specified, it depends on the Default CJK language setting (default-CJK).

| Attribute | Value |
|---|---|
| **Applies to** | all block-level and inline-level formatting objects |
| **Values** | left \| right \| depend-on-language \| auto |
| **Initial** | auto |
| **Inherited** | yes |

## axf:word-break

Specifies whether to enable line breaking even inside a word.

Values have the following meanings:
- `normal`: Follows a normal line breaking rule.
- `keep-all`: Does not break inside words. A word here indicates a character string which consists of the following category (General Category) of Unicode: Letter, Mark, Number. Whether to break lines on a boundary with characters other than these follows the rule of the standard line break. Moreover, hyphenate="true" is disregarded.
- `break-all`: The line breaking is enabled between all the characters in the word. This is effective only with the following scripts: Latn, Cyrl, Grek, Zyyy. axf:word-wrap="normal" is disregarded.
- `keep-non-spaces`: Does not break between non-whitespace characters.

Within the word oriented upright by axf:text-orientation="upright", it is always considered axf:word-break="break-all".

| Attribute | Value |
|---|---|
| **Applies to** | all block-level and inline-level formatting objects |
| **Values** | normal \| keep-all \| break-all \| keep-non-spaces |
| **Initial** | normal |
| **Inherited** | yes |

## axf:word-wrap

Specifies whether to break word forcibly when line break cannot be performed.

Values have the following meanings:
- `normal`: The line is not broken forcibly. The text will overflow across the region.
- `break-word`: The line is broken forcibly at an appropriate position.

| Attribute | Value |
|---|---|
| **Applies to** | all block-level and inline-level formatting objects |
| **Values** | normal \| break-word |
| **Initial** | break-word |
| **Inherited** | yes |
