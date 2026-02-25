# Number to String Conversion Properties

## Overview

These properties control how numeric values are converted to string representations, primarily used with `fo:page-number`, `fo:page-number-citation`, and `fo:page-number-citation-last`. They are defined by reference to XSLT's Number to String Conversion Attributes.

<!-- Source: https://www.w3.org/TR/xslfo20/#format -->

## Properties

### format

| Field | Value |
|---|---|
| **Values** | `<string>` |
| **Initial** | `1` |
| **Applies to** | fo:page-sequence |
| **Inherited** | No |
| **Conformance** | Basic |

<!-- Source: https://www.w3.org/TR/xslfo20/#format -->

This property is defined in XSLT: Number to String Conversion Attributes.

The `format` property specifies the format token used to convert a number to a string. The format token `1` produces `1 2 3 ... 10 11 12 ...`. The format token `01` produces `01 02 ... 09 10 11 ...`. The format token `a` produces `a b c ... z aa ab ...`. The format token `A` produces `A B C ... Z AA AB ...`. The format token `i` produces `i ii iii iv v vi ...`. The format token `I` produces `I II III IV V VI ...`.

### grouping-separator

| Field | Value |
|---|---|
| **Values** | `<character>` |
| **Initial** | no separator |
| **Applies to** | fo:page-sequence |
| **Inherited** | No |
| **Conformance** | Basic |

<!-- Source: https://www.w3.org/TR/xslfo20/#grouping-separator -->

This property is defined in XSLT: Number to String Conversion Attributes.

Specifies the character used to separate groups of digits. For example, using a comma as the grouping-separator and a grouping-size of 3 would produce numbers like `1,000` and `1,000,000`.

### grouping-size

| Field | Value |
|---|---|
| **Values** | `<number>` |
| **Initial** | no grouping |
| **Applies to** | fo:page-sequence |
| **Inherited** | No |
| **Conformance** | Basic |

<!-- Source: https://www.w3.org/TR/xslfo20/#grouping-size -->

This property is defined in XSLT: Number to String Conversion Attributes.

Specifies the size of the grouping (the number of digits in each group). The `grouping-separator` property specifies the separator to use between groups.

### letter-value

| Field | Value |
|---|---|
| **Values** | `auto \| alphabetic \| traditional \| <implementer extension>` |
| **Initial** | `auto` |
| **Applies to** | fo:page-sequence |
| **Inherited** | No |
| **Conformance** | Basic |

<!-- Source: https://www.w3.org/TR/xslfo20/#letter-value -->

The `letter-value` property disambiguates between numbering sequences that use letters, such as Roman (i, ii, iii) and Alphabetic (i, j, k).

In many languages there are two commonly used numbering sequences that use letters. One numbering sequence assigns numeric values to letters in alphabetic sequence, and the other assigns numeric values to each letter in some other manner traditional in that language. In English, these would correspond to the numbering sequences specified by the format tokens `a` and `i`. In some languages, the first member of each sequence is the same, and so the format token alone would be ambiguous. A value of `alphabetic` specifies the alphabetic sequence; a value of `traditional` specifies the other sequence. If the `letter-value` property is not specified, then it is implementation-dependent how any ambiguity is resolved.

## Code Samples

No code samples in spec for this property group.

## See Also

- [fo-page-sequence](fo-page-sequence.md) -- uses these properties for page numbering
- [fo-page-number](fo-page-number.md) -- displays the current page number
- [fo-page-number-citation](fo-page-number-citation.md) -- displays the page number of a referenced element
