# fo:character

## Summary

The fo:character flow object represents a character that is mapped to a glyph for presentation. It is an atomic unit to the formatter. When the result tree is interpreted as a tree of formatting objects, a character in the result tree is treated as if it were an empty element of type fo:character with a character attribute equal to the Unicode representation of the character.

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_character -->

## Content Model

`EMPTY`

## Properties

| Property | Inherited | Conformance Level |
|----------|-----------|-------------------|
| Common Aural Properties | N/A | Extended |
| Common Border, Padding, and Background Properties | No | Basic |
| Common Font Properties | Yes | Basic |
| Common Hyphenation Properties | Yes | Basic |
| Common Margin Properties-Inline | No | Basic |
| Common Relative Position Properties | No | Extended |
| alignment-adjust | No | Extended |
| treat-as-word-space | No | Extended |
| alignment-baseline | No | Extended |
| baseline-shift | No | Extended |
| character | No | Basic |
| color | Yes | Basic |
| dominant-baseline | No | Extended |
| text-depth | No | Extended |
| text-altitude | No | Extended |
| glyph-orientation-horizontal | Yes | Extended |
| glyph-orientation-vertical | Yes | Extended |
| id | No | Basic |
| index-class | No | Extended |
| index-key | No | Extended |
| keep-with-next | No | Extended |
| keep-with-previous | No | Extended |
| letter-spacing | Yes | Basic |
| line-height | Yes | Basic |
| score-spaces | Yes | Basic |
| suppress-at-line-break | No | Extended |
| text-decoration | No | Basic |
| text-shadow | No | Extended |
| text-transform | Yes | Basic |
| visibility | Yes | Extended |
| word-spacing | Yes | Basic |

## Usage Notes

- The fo:character formatting object generates and returns one or more normal inline-areas.
- Cases where more than one inline-area is generated are encountered in scripts where a single character generates both a prefix and a suffix glyph to some other character.
- The dimensions of the areas are determined by the font metrics for the glyph.
- In a stylesheet, the explicit creation of an fo:character may be used to explicitly override the default character-to-glyph mapping.
- The semantics of an "auto" value for character properties, which is typically their initial value, are based on the Unicode code point. Overrides may be specified in an implementation-specific manner.
- When formatting an fo:character with a treat-as-word-space value of "true", the User Agent may use a different method for determining the inline-progression-dimension of the area (typically using a word space value stored in the font, or a formatter-defined word space value).
- Unicode Tag Characters need not be supported. Unicode Version 3.1 states that they are not to be used with any protocols that provide alternate means for language tagging, such as HTML or XML.

## Code Samples

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_character -->
```xml
EMPTY
```

## See Also

- [fo:inline](fo-inline.md) — for formatting portions of text with borders or backgrounds
- [fo:page-number](fo-page-number.md) — generates inline-areas whose content is the page number
- [fo:page-number-citation](fo-page-number-citation.md) — generates inline-areas citing a page number
