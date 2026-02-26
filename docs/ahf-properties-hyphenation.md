# Antenna House Extension Properties: Hyphenation Extension Properties

<!-- Source: XSL-FO-Reference-74-MID.pdf pp.312-476 -->

Extensions to hyphenation control including caps-word hyphenation, double-hyphen translineation, and soft-hyphen treatment.

## axf:double-hyphen-translineation

Specifies whether to place a hyphen also at the start of the line when breaking lines at a hyphen.

This setting is effective when `hyphenate="true"` is specified.

Values have the following meanings:

- **auto**: Works as `true` when the language is specified by `double-hyphen-translineation` in the Option Setting File.
- **true**: Place a hyphen also at the start of the line when a line break occurs at a hyphen.
- **false**: Does not place a hyphen at the start of the line when a line break occurs at a hyphen.

| Attribute | Value |
|---|---|
| **Applies to** | `<fo:block>` |
| **Values** | `auto \| true \| false` |
| **Initial** | auto |
| **Inherited** | yes |

## axf:hyphenate-caps-word

Specifies whether to hyphenate words consisting only of uppercase letters.

A phrase like ANTENNA-HOUSE with hyphens is considered multiple words. There is a possibility of a line break at the hyphen position. Even letters processed as small-caps are considered lowercase if the original letters are lowercase. This setting is invalid when `hyphenate="false"` is specified.

Values have the following meanings:

- **true**: Hyphenates a word.
- **false**: Does not hyphenate a word that consists of all capital letters. A word that does not consist of all capital letters, such as a word that has only the first letter capitalized, is hyphenated.
- **false-all**: Does not hyphenate all words that start with a capital letter.

| Attribute | Value |
|---|---|
| **Applies to** | `<fo:block>` |
| **Values** | `true \| false \| false-all` |
| **Initial** | true |
| **Inherited** | yes |

## axf:hyphenate-hyphenated-word

Specifies whether to hyphenate the already hyphenated word or not. This setting is invalid when `hyphenate="false"` is specified.

Values have the following meanings:

- **true**: Hyphenates a word.
- **false**: Does not hyphenate a word. The line may break only at the hyphen position.

The following are recognized as hyphens:

- U+002D HYPHEN-MINUS
- U+00AD SOFT HYPHEN
- U+2010 HYPHEN
- U+2011 NON-BREAKING HYPHEN

| Attribute | Value |
|---|---|
| **Applies to** | `<fo:block>` |
| **Values** | `true \| false` |
| **Initial** | true |
| **Inherited** | yes |

## axf:hyphenation-minimum-character-count

Specifies the minimum number of characters a word must have before it can be hyphenated. The `axf:hyphenation-minimum-character-count` must be an integer number of 1 or more.

| Attribute | Value |
|---|---|
| **Applies to** | `<fo:block>`, `<fo:character>` |
| **Values** | `<integer>` |
| **Initial** | 1 |
| **Inherited** | yes |

## axf:hyphenation-zone

Limits the range where a hyphenation is available.

Values have the following meanings:

- **none**: Nothing is limited in hyphenation.
- **\<length\>**: If the length from the end of a word to the end of line is less or equal to the specified value, the following word is not hyphenated. It is invalid when 0 or less value is specified.
- **\<percentage\>**: Refer to the width of containing block.

| Attribute | Value |
|---|---|
| **Applies to** | `<fo:block>` |
| **Values** | `none \| <length> \| <percentage>` |
| **Initial** | none |
| **Inherited** | yes |

## axf:soft-hyphen-treatment

Specifies the treatment of SOFT HYPHEN (U+00AD) characters.

The value `auto` has the meaning SOFT HYPHEN is deleted except when needed for line breaking. The value `preserve` has the meaning SOFT HYPHEN is not deleted and the target glyph is output.

| Attribute | Value |
|---|---|
| **Applies to** | all formatting elements on block and inline level |
| **Values** | `auto \| preserve` |
| **Initial** | auto |
| **Inherited** | yes |
