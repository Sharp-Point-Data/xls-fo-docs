# Font Properties

## Overview

<!-- Source: https://www.w3.org/TR/xslfo20/#common-font-properties -->

The common font properties control font selection for text rendering. These properties are all taken from CSS2 (reference: http://www.w3.org/TR/2008/REC-CSS2-20080411/fonts.html). Although these properties reference the individual properties in the CSS specification, it is recommended to read the entire font section of the CSS2 specification for full context.

Font properties apply to formatting objects that produce inline-level areas containing text, such as `fo:block`, `fo:inline`, `fo:character`, `fo:leader`, and others.

## Properties

### font-family

| Field | Value |
|---|---|
| **Values** | `[[ <family-name> \| <generic-family> ],]* [<family-name> \| <generic-family>] \| inherit` |
| **Initial** | depends on user agent |
| **Applies to** | all formatting objects that accept common font properties |
| **Inherited** | Yes |
| **Percentages** | N/A |
| **Media** | visual |

<!-- Source: https://www.w3.org/TR/xslfo20/#font-family -->

CSS2 Definition (as amended by errata).

This property specifies a prioritized list of font family names and/or generic family names. To deal with the problem that a single font may not contain glyphs to display all the characters in a document, or that not all fonts are available on all systems, this property allows authors to specify a list of fonts, all of the same style and size, that are tried in sequence to see if they contain a glyph for a certain character. This list is called a font set.

The generic font family will be used if one or more of the other fonts in a font set is unavailable. Although many fonts provide the "missing character" glyph, typically an open box, as its name implies this should not be considered a match except for the last font in a font set.

There are two types of font family names:

- **\<family-name\>** -- The name of a font-family of choice. Font family names containing whitespace should be quoted. If quoting is omitted, any whitespace characters before and after the font name are ignored and any sequence of whitespace characters inside the font name is converted to a single space.
- **\<generic-family\>** -- The following generic families are defined: "serif", "sans-serif", "cursive", "fantasy", and "monospace". Generic font family names are keywords, and therefore must not be quoted.

**XSL modifications to the CSS definition:**

- **\<string\>** -- The names are syntactically expressed as strings. See the expression language for a two-argument "system-font" function that returns a characteristic of a system-font. This may be used, instead of the "font" shorthand, to specify the name of a system-font.

### font-selection-strategy

| Field | Value |
|---|---|
| **Values** | `auto \| character-by-character \| inherit` |
| **Initial** | `auto` |
| **Applies to** | all formatting objects that accept common font properties |
| **Inherited** | Yes |
| **Percentages** | N/A |
| **Media** | visual |

<!-- Source: https://www.w3.org/TR/xslfo20/#font-selection-strategy -->

XSL Definition.

There is no XSL mechanism to specify a particular font; instead, a *selected font* is chosen from the fonts available to the User Agent based on a set of selection criteria. The selection criteria are the following font properties: `font-family`, `font-style`, `font-variant`, `font-weight`, `font-stretch`, and `font-size`, plus, for some formatting objects, one or more characters. These characters are called the *contextual characters*. The contextual characters can be as few as a single character and as many as the entire character complement of the result tree being processed.

Except for the `fo:character` formatting object, for all other formatting objects where `font-family` applies, the selection criteria consist of the above font properties only. For the `fo:character` formatting object, the selection criteria are these properties plus either the value of the `character` property of the `fo:character` alone or that character together with other contextual characters.

The strategy to be followed for selecting a font based on these criteria is specified by the `font-selection-strategy` property.

The `font-family` property is a prioritized list of font family names, which are tried in sequence to find an available font that matches the selection criteria. If no matching font is found, a fallback selection is determined in a system-dependent manner.

If no match has been found for a particular character, there is no selected font and the User Agent should provide a visual indication that a character is not being displayed (for example, using the 'missing character' glyph).

Values have the following meanings:

- **auto** -- The selection criterion given by the contextual characters is used in an implementation defined manner. An implementation may, for example, use an algorithm where all characters in the result tree having the same set of font selection property values influence the selection, or it may only use the character property of a single `fo:character` formatting object for which a font is to be selected.
- **character-by-character** -- The set of contextual characters consists of the single character that is the value of the `character` property of the `fo:character` for which a font is to be selected. This selection strategy is the same as the strategy used to select fonts in CSS.

### font-size

| Field | Value |
|---|---|
| **Values** | `<absolute-size> \| <relative-size> \| <length> \| <percentage> \| inherit` |
| **Initial** | `medium` |
| **Applies to** | all formatting objects that accept common font properties |
| **Inherited** | Yes (the computed value is inherited) |
| **Percentages** | refer to parent element's font size |
| **Media** | visual |

<!-- Source: https://www.w3.org/TR/xslfo20/#font-size -->

CSS2 Definition (as amended by errata).

This property describes the size of the font when set solid. The font size corresponds to the em square, a concept used in typography. Note that certain glyphs may bleed outside their em squares.

Values have the following meanings:

- **\<absolute-size\>** -- An \<absolute-size\> keyword refers to an entry in a table of font sizes computed and kept by the user agent. Possible values are: `xx-small | x-small | small | medium | large | x-large | xx-large`. On a computer screen a scaling factor of 1.2 is suggested between adjacent indexes; if the "medium" font is 12pt, the "large" font could be 14.4pt. Different media may need different scaling factors. Also, the user agent should take the quality and availability of fonts into account when computing the table.
- **\<relative-size\>** -- A \<relative-size\> keyword is interpreted relative to the table of font sizes and the font size of the parent element. Possible values are: `larger | smaller`. For example, if the parent element has a font size of "medium", a value of "larger" will make the font size of the current element be "large".
- **\<length\>** -- A length value specifies an absolute font size (that is independent of the user agent's font table). Negative lengths are illegal.
- **\<percentage\>** -- A percentage value specifies an absolute font size relative to the parent element's font size. Use of percentage values, or values in "em's", leads to more robust and cascadable stylesheets.

The actual value of this property may differ from the computed value due to a numerical value on 'font-size-adjust' and the unavailability of certain font sizes. Child elements inherit the computed 'font-size' value (otherwise, the effect of 'font-size-adjust' would compound).

**XSL modifications to the CSS definition:** 'font-size' must be matched within a UA-dependent margin of tolerance. (Typically, sizes for scalable fonts are rounded to the nearest whole pixel, while the tolerance for bitmapped fonts could be as large as 20%.) Further computations, e.g., by 'em' values in other properties, are based on the computed 'font-size' value.

### font-stretch

| Field | Value |
|---|---|
| **Values** | `normal \| wider \| narrower \| ultra-condensed \| extra-condensed \| condensed \| semi-condensed \| semi-expanded \| expanded \| extra-expanded \| ultra-expanded \| inherit` |
| **Initial** | `normal` |
| **Applies to** | all formatting objects that accept common font properties |
| **Inherited** | Yes |
| **Percentages** | N/A |
| **Media** | visual |

<!-- Source: https://www.w3.org/TR/xslfo20/#font-stretch -->

CSS2 Definition.

The 'font-stretch' property selects a normal, condensed, or extended face from a font family.

- **ultra-condensed** -- ultra-condensed face
- **extra-condensed** -- extra-condensed face
- **condensed** -- condensed face
- **semi-condensed** -- semi-condensed face
- **normal** -- normal face
- **semi-expanded** -- semi-expanded face
- **expanded** -- expanded face
- **extra-expanded** -- extra-expanded face
- **ultra-expanded** -- ultra-expanded face
- **wider** -- The relative keyword "wider" sets the value to the next expanded value above the inherited value (while not increasing it above "ultra-expanded").
- **narrower** -- The relative keyword "narrower" sets the value to the next condensed value below the inherited value (while not decreasing it below "ultra-condensed").

### font-size-adjust

| Field | Value |
|---|---|
| **Values** | `<number> \| none \| inherit` |
| **Initial** | `none` |
| **Applies to** | all formatting objects that accept common font properties |
| **Inherited** | Yes |
| **Percentages** | N/A |
| **Media** | visual |

<!-- Source: https://www.w3.org/TR/xslfo20/#font-size-adjust -->

CSS2 Definition.

In bicameral scripts, the subjective apparent size and legibility of a font are less dependent on their 'font-size' value than on the value of their 'x-height', or, more usefully, on the ratio of these two values, called the aspect value (x-height divided by font size). The higher the aspect value, the more likely it is that a font at smaller sizes will be legible.

This property allows authors to specify an aspect value for an element that will preserve the x-height of the first choice font in the substitute font.

- **none** -- Do not preserve the font's x-height.
- **\<number\>** -- Specifies the aspect value. The number refers to the aspect value of the first choice font. The scaling factor for available fonts is computed according to the formula: `y(a/a') = c` where `y` = font-size of first-choice font, `a` = aspect value of first-choice font, `a'` = aspect value of available font, `c` = font-size to apply to available font.

For example, the popular font Verdana has an aspect value of 0.58; when Verdana's font size is 100 units, its x-height is 58 units. For comparison, Times New Roman has an aspect value of 0.46. Verdana will therefore tend to remain legible at smaller sizes than Times New Roman.

Font size adjustments take place when computing the actual value of "font-size". Since inheritance is based on the computed value, child elements will inherit unadjusted values.

### font-style

| Field | Value |
|---|---|
| **Values** | `normal \| italic \| oblique \| backslant \| inherit` |
| **Initial** | `normal` |
| **Applies to** | all formatting objects that accept common font properties |
| **Inherited** | Yes |
| **Percentages** | N/A |
| **Media** | visual |

<!-- Source: https://www.w3.org/TR/xslfo20/#font-style -->

CSS2 Definition.

The "font-style" property requests normal (sometimes referred to as "roman" or "upright"), italic, and oblique faces within a font family.

- **normal** -- Specifies a font that is classified as "normal" in the UA's font database.
- **oblique** -- Specifies a font that is classified as "oblique" in the UA's font database. Fonts with Oblique, Slanted, or Incline in their names will typically be labeled "oblique" in the font database. A font that is labeled "oblique" in the UA's font database may actually have been generated by electronically slanting a normal font.
- **italic** -- Specifies a font that is classified as "italic" in the UA's font database, or, if that is not available, one labeled 'oblique'. Fonts with Italic, Cursive, or Kursiv in their names will typically be labeled "italic".

**XSL modifications to the CSS definition:** The following value type has been added for XSL:

- **backslant** -- Specifies a font that is classified as "backslant" in the UA's font database.

XSL incorporates from CSS2 15.5: 'italic' will be satisfied if there is either a face in the UA's font database labeled with the CSS keyword 'italic' (preferred) or 'oblique'. Otherwise the values must be matched exactly or font-style will fail.

### font-variant

| Field | Value |
|---|---|
| **Values** | `normal \| small-caps \| inherit` |
| **Initial** | `normal` |
| **Applies to** | all formatting objects that accept common font properties |
| **Inherited** | Yes |
| **Percentages** | N/A |
| **Media** | visual |

<!-- Source: https://www.w3.org/TR/xslfo20/#font-variant -->

CSS2 Definition.

In a small-caps font, the glyphs for lowercase letters look similar to the uppercase ones, but in a smaller size and with slightly different proportions. The "font-variant" property requests such a font for bicameral scripts (having two cases, as with Roman script). This property has no visible effect for scripts that are unicameral (having only one case, as with most of the world's writing systems).

- **normal** -- Specifies a font that is not labeled as a small-caps font.
- **small-caps** -- Specifies a font that is labeled as a small-caps font. If a genuine small-caps font is not available, user agents should simulate a small-caps font, for example by taking a normal font and replacing the lowercase letters by scaled uppercase characters. As a last resort, unscaled uppercase letter glyphs in a normal font may replace glyphs in a small-caps font so that the text appears in all uppercase letters.

Insofar as this property causes text to be transformed to uppercase, the same considerations as for "text-transform" apply.

**XSL modifications to the CSS definition:** XSL incorporates from CSS2 15.5: 'normal' matches a font not labeled as 'small-caps'; 'small-caps' matches (1) a font labeled as 'small-caps', (2) a font in which the small caps are synthesized, or (3) a font where all lowercase letters are replaced by uppercase letters. A small-caps font may be synthesized by electronically scaling uppercase letters from a normal font.

### font-weight

| Field | Value |
|---|---|
| **Values** | `normal \| bold \| bolder \| lighter \| 100 \| 200 \| 300 \| 400 \| 500 \| 600 \| 700 \| 800 \| 900 \| inherit` |
| **Initial** | `normal` |
| **Applies to** | all formatting objects that accept common font properties |
| **Inherited** | Yes |
| **Percentages** | N/A |
| **Media** | visual |

<!-- Source: https://www.w3.org/TR/xslfo20/#font-weight -->

CSS2 Definition.

The "font-weight" property specifies the weight of the font.

- **normal** -- Same as "400".
- **bold** -- Same as "700".
- **bolder** -- Specifies the next weight that is assigned to a font that is darker than the inherited one. If there is no such weight, it simply results in the next darker numerical value (and the font remains unchanged), unless the inherited value was "900", in which case the resulting weight is also "900".
- **lighter** -- Specifies the next weight that is assigned to a font that is lighter than the inherited one. If there is no such weight, it simply results in the next lighter numerical value (and the font remains unchanged), unless the inherited value was "100", in which case the resulting weight is also "100".
- **\<integer\>** (100-900) -- These values form an ordered sequence, where each number indicates a weight that is at least as dark as its predecessor.

Child elements inherit the computed value of the weight.

**XSL modifications to the CSS definition:** XSL incorporates from CSS2 15.5.1: The association of other weights within a family to the numerical weight values is intended only to preserve the ordering of weights within that family. User agents must map names to values in a way that preserves visual order; a face mapped to a value must not be lighter than faces mapped to lower values.

The following heuristics describe how assignment is done in typical cases: If the font family already uses a numerical scale with nine values (as e.g., OpenType does), the font weights should be mapped directly.

If there is both a face labeled Medium and one labeled Book, Regular, Roman or Normal, then the Medium is normally assigned to the '500'. The font labeled "Bold" will often correspond to the weight value '700'.

If there are fewer than 9 weights in the family, the default algorithm for filling the "holes" is as follows: If '500' is unassigned, it will be assigned the same font as '400'. If any of the values '600', '700', '800', or '900' remains unassigned, they are assigned to the same face as the next darker assigned keyword, if any, or the next lighter one otherwise. If any of '300', '200', or '100' remains unassigned, it is assigned to the next lighter assigned keyword, if any, or the next darker otherwise.

There is no guarantee that there will be a darker face for each of the 'font-weight' values; for example, some fonts may have only a normal and a bold face, others may have eight different face weights.

## Code Samples

No code samples in spec for this property group.

## See Also

- [fo-block](fo-block.md) -- Block-level formatting object that uses font properties
- [fo-inline](fo-inline.md) -- Inline-level formatting object that uses font properties
- [fo-character](fo-character.md) -- Character formatting object, the primary context for font-selection-strategy
- [Guide: Data Types](guide-datatypes.md) -- Understanding value types like \<length\>, \<percentage\>
