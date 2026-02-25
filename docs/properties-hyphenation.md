# Common Hyphenation Properties

<!-- Source: https://www.w3.org/TR/xslfo20/#common-hyphenation-properties -->

## Overview

The common hyphenation properties control how the formatter performs hyphenation during line breaking. These properties specify the language, country, and script context for locale-coupled formatting services, the hyphenation character to display, and constraints on minimum character/syllable counts before and after hyphenation breaks. They also include properties for controlling hyphenation exceptions, syllable-level constraints, word widows, and minimum last-line lengths.

These properties apply to block-level formatting objects that contain text content (primarily `fo:block` and `fo:character`). All hyphenation properties are inherited, allowing them to be set at a high level (e.g., on `fo:page-sequence` or `fo:flow`) and inherited by descendant blocks.

## Properties

### country

| Field | Value |
|---|---|
| **Values** | `none \| <country> \| inherit` |
| **Initial** | `none` |
| **Applies to** | all elements with hyphenation properties |
| **Inherited** | Yes |
| **Percentages** | N/A |

Specifies the country to be used by the formatter in language-/locale-coupled services, such as line-justification strategy, line-breaking, and hyphenation.

Values have the following meanings:

- **none** -- Indicates the country is unknown or is not significant to the proper formatting of this object.
- **\<country\>** -- A country-specifier in conformance with ISO 3166 (ISO 3166-1, ISO 3166-2, and ISO 3166-3).

Note: This may affect line composition in a system-dependent way.

### hyphenate

| Field | Value |
|---|---|
| **Values** | `false \| true \| inherit` |
| **Initial** | `false` |
| **Applies to** | all elements with hyphenation properties |
| **Inherited** | Yes |
| **Percentages** | N/A |

Specifies whether hyphenation is allowed during line-breaking when the formatter is formatting this formatting object.

Values have the following meanings:

- **false** -- Hyphenation may not be used in the line-breaking algorithm between characters with this value.
- **true** -- Hyphenation may be used in the line-breaking algorithm between characters with this value.

It is implementation defined whether hyphenation may be used between a character for which the value is "true" and one for which the value is "false".

### hyphenation-character

| Field | Value |
|---|---|
| **Values** | `<character> \| inherit` |
| **Initial** | `The Unicode hyphen character U+2010` |
| **Applies to** | all elements with hyphenation properties |
| **Inherited** | Yes |
| **Percentages** | N/A |

Specifies the Unicode character to be presented when a hyphenation break occurs.

Values have the following meanings:

- **\<character\>** -- Specifies the Unicode character to be presented when a hyphenation break occurs.

The styling properties of this character are those inherited from its containing flow object.

### hyphenation-push-character-count

| Field | Value |
|---|---|
| **Values** | `<number> \| inherit` |
| **Initial** | `2` |
| **Applies to** | all elements with hyphenation properties |
| **Inherited** | Yes |
| **Percentages** | N/A |

The hyphenation-push-character-count specifies the minimum number of characters in a hyphenated word after the hyphenation character. This is the minimum number of characters in the word pushed to the next line after the line ending with the hyphenation character.

Values have the following meanings:

- **\<number\>** -- A positive integer. If a non-positive or non-integer value is provided, the value will be rounded to the nearest integer value greater than or equal to 1.

### hyphenation-remain-character-count

| Field | Value |
|---|---|
| **Values** | `<number> \| inherit` |
| **Initial** | `2` |
| **Applies to** | all elements with hyphenation properties |
| **Inherited** | Yes |
| **Percentages** | N/A |

The hyphenation-remain-character-count specifies the minimum number of characters in a hyphenated word before the hyphenation character. This is the minimum number of characters in the word left on the line ending with the hyphenation character.

Values have the following meanings:

- **\<number\>** -- A positive integer. If a non-positive or non-integer value is provided, the value will be rounded to the nearest integer value greater than or equal to 1.

### language

| Field | Value |
|---|---|
| **Values** | `none \| <language> \| inherit` |
| **Initial** | `none` |
| **Applies to** | all elements with hyphenation properties |
| **Inherited** | Yes |
| **Percentages** | N/A |

Specifies the language to be used by the formatter in language-/locale-coupled services, such as line-justification strategy, line-breaking, and hyphenation.

Values have the following meanings:

- **none** -- Indicates the language is unknown or is not significant to the proper formatting of this object.
- **\<language\>** -- A 3-letter code conforming to a ISO 639-2 terminology or bibliographic code or a 2-letter code conforming to a ISO 639 2-letter code.

Note: This may affect line composition in a system-dependent way.

Note: ISO 639 2-letter and ISO 639-2 terminology 3-letter codes are also used in the language component of RFC 3066, but user-defined and IANA registered language codes that are allowed in RFC 3066 are not allowed as the value of this property.

### script

| Field | Value |
|---|---|
| **Values** | `none \| auto \| <script> \| inherit` |
| **Initial** | `auto` |
| **Applies to** | all elements with hyphenation properties |
| **Inherited** | Yes |
| **Percentages** | N/A |

Specifies the script to be used by the formatter in language-/locale-coupled services, such as line-justification strategy, line-breaking, and hyphenation.

Values have the following meanings:

- **auto** -- Indicates that the script is determined based on testing a character in the document against script identifiers assigned to Unicode code point ranges. For `fo:character` the character tested is given by the "character" property. For other formatting objects the character tested is the first character descendant, as determined by the pre-order traversal of the refined formatting object tree, which has an unambiguous script identifier. Note: This provides the automatic differentiation between Kanji, Katakana, Hiragana, and Romanji used in JIS-4051 and similar services in some other countries/languages.
- **none** -- Indicates the script is unknown or is not significant to the proper formatting of this object.
- **\<script\>** -- A script specifier in conformance with ISO 15924.

Note: This may affect line composition in a system-dependent way.

### hyphenation-push-syllable-count

| Field | Value |
|---|---|
| **Values** | `<number>` |
| **Initial** | `1` |
| **Applies to** | all elements |
| **Inherited** | Yes |
| **Percentages** | N/A |

The hyphenation-push-syllable-count property specifies the minimum number of syllables permitted in a hyphenated word after the hyphenation character. Formatters must not insert hyphens during line breaking in places that would result in word fragments violating this property.

Values have the following meanings:

- **\<number\>** -- A positive integer. If a non-positive or non-integer value is provided, the value will be rounded to the nearest integer value greater than or equal to 1.

### hyphenation-remain-syllable-count

| Field | Value |
|---|---|
| **Values** | `<number>` |
| **Initial** | `1` |
| **Applies to** | all elements |
| **Inherited** | Yes |
| **Percentages** | N/A |

The hyphenation-remain-syllable-count specifies the minimum number of syllables in a hyphenated word before the hyphenation character. This is the minimum number of syllables in the word left on the line ending with the hyphenation character.

Values have the following meanings:

- **\<number\>** -- A positive integer. If a non-positive or non-integer value is provided, the value will be rounded to the nearest integer value greater than or equal to 1.

### syllable-widows

| Field | Value |
|---|---|
| **Values** | `<number>` |
| **Initial** | `1` |
| **Applies to** | all elements |
| **Inherited** | Yes |
| **Percentages** | N/A |

The "syllable-widows" property specifies the minimum number of syllables in the last line-area of a block-area.

Values have the following meanings:

- **\<number\>** -- A positive integer. If a non-positive or non-integer value is provided, the value will be rounded to the nearest integer value greater than or equal to 1. The syllable-widows specifies the minimum number of syllables in the last line-area of the block-area for which it is in effect.

### hyphenation-exceptions

| Field | Value |
|---|---|
| **Values** | `<uri-specification> \| none \| inherit` |
| **Initial** | `none` |
| **Applies to** | all elements |
| **Inherited** | No |
| **Percentages** | N/A |

This property specifies a set of hyphenation-exception words to be used by the hyphenation algorithm.

Values have the following meanings:

- **none** -- No exceptions are used.
- **\<uri-specification\>** -- A URI specification giving a reference to the resource containing the exception words.

Note: The format for the exception-words resource has not been defined by the spec.

### word-widows

| Field | Value |
|---|---|
| **Values** | `<number>` |
| **Initial** | `0` |
| **Applies to** | all elements |
| **Inherited** | Yes |
| **Percentages** | N/A |

The "word-widows" property specifies the minimum number of words or partial words in the last line-area of a block-area.

When a word is hyphenated, the remaining portion, a partial word, brought down onto the next line, is to be considered to be a whole word for the purpose of counting words.

Values have the following meanings:

- **\<number\>** -- A positive integer. If a non-positive or non-integer value is provided, the value will be rounded to the nearest integer value greater than or equal to 1.
- **\<percentage\>** -- The permitted minimum deficit is a percentage of the containing block width.

The "word-widows" property specifies the minimum number of words in the last line-area of the block-area for which it is in effect.

### min-length-of-last-line

| Field | Value |
|---|---|
| **Values** | `<length>` |
| **Initial** | `1` |
| **Applies to** | all elements |
| **Inherited** | Yes |
| **Percentages** | refer to width of containing block |

The min-length-of-last-line property specifies the minimum inline-dimension of the last line-area in a block-area.

Values have the following meanings:

- **\<length\>** -- Specifies a fixed minimum line length.
- **\<percentage\>** -- The minimum line length is a percentage of the containing block width.

The value must not be negative.

### last-line-minimum-deficit

| Field | Value |
|---|---|
| **Values** | `<length> \| <percentage> \| inherit` |
| **Initial** | `0pt` |
| **Applies to** | fo:block |
| **Inherited** | Yes |
| **Percentages** | refer to width of containing block |

The last-line-minimum-deficit property specifies a length (x) for the minimum line length deficit for the last line-area of a block-area. More precisely, it specifies a constraint on the last line-area child of the last block-area L generated and returned by the formatting object, such that the inline L is either equal to the available width (w) in the inline-dimension (as the term is used in the "justify" value of "text-align"), or is less than or equal to w minus x.

Values have the following meanings:

- **\<length\>** -- The minimum line length deficit is a fixed length.
- **\<percentage\>** -- The minimum line length deficit is a percentage of the containing block width.

The value must not be negative.

### hyphenation-permitted-minimum-deficit

| Field | Value |
|---|---|
| **Values** | `<length> \| <percentage> \| inherit` |
| **Initial** | `100%` |
| **Applies to** | all elements |
| **Inherited** | Yes |
| **Percentages** | refer to width of containing block |

This property specifies a length (x) for the hyphenation margin for a block. More precisely, it specifies a limitation on the effect of a "hyphenate" value of "true"; hyphenation may be used in the line-breaking algorithm within a given line-area when otherwise the inline-dimension of the line area would be less than the available width in the inline-dimension by an amount greater than x.

Values have the following meanings:

- **\<length\>** -- The permitted minimum deficit is a fixed length.
- **\<percentage\>** -- The permitted minimum deficit is a percentage of the containing block width.

The value must not be negative.

## Code Samples

No code samples in spec for this property group.

## See Also

- [fo:block](fo-block.md) -- Primary block-level FO that uses these properties
- [fo:character](fo-character.md) -- Inline FO for individual character representation
- [Common Margin Properties - Block](properties-margin-block.md) -- Block-level spacing properties often used alongside hyphenation
