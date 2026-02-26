# fo:inline

## Summary

The fo:inline formatting object is commonly used for formatting a portion of text with a background or enclosing it in a border. It generates one or more normal inline-areas and returns these areas together with any normal block-areas, page-level-out-of-line areas, and reference-level-out-of-line areas returned by its children.

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_inline -->

## Content Model

`(#PCDATA | %inline; | %block;)*`

In addition, this formatting object may have a sequence of zero or more fo:marker elements as its initial children.

An fo:inline that is a child of an fo:footnote may not have block-level children. An fo:inline that is a descendant of an fo:leader or of the fo:inline child of an fo:footnote may not have block-level children, unless it has a nearer ancestor that is an fo:inline-container.

## Properties

| Property | Inherited | Conformance Level |
|----------|-----------|-------------------|
| Common Accessibility Properties | N/A | Basic |
| Common Aural Properties | N/A | Extended |
| Common Border, Padding, and Background Properties | No | Basic |
| Common Font Properties | Yes | Basic |
| Common Margin Properties-Inline | No | Basic |
| Common Relative Position Properties | No | Extended |
| alignment-adjust | No | Extended |
| alignment-baseline | No | Extended |
| baseline-shift | No | Extended |
| block-progression-dimension | No | Extended |
| color | Yes | Basic |
| dominant-baseline | No | Extended |
| height | No | Extended |
| id | No | Basic |
| index-class | No | Extended |
| index-key | No | Extended |
| inline-progression-dimension | No | Extended |
| keep-together | Yes | Extended |
| keep-with-next | No | Extended |
| keep-with-previous | No | Extended |
| line-height | Yes | Basic |
| text-decoration | No | Basic |
| visibility | Yes | Extended |
| width | No | Extended |
| wrap-option | Yes | Extended |
| border-collapse | Yes | Extended |

## Usage Notes

- fo:inline is the primary mechanism for applying inline-level formatting (such as font changes, colors, borders, or backgrounds) to a portion of text within a block.
- No area may have more than one normal child area returned by the same fo:inline formatting object.
- The children of each normal area returned by an fo:inline must satisfy the constraints specified in the inline-building section of the area model.
- The geometric constraints imposed by the traits derived from the applicable properties must be satisfied, as rigorously defined in the area model.
- fo:inline can contain both inline-level and block-level children (mixed content), though block-level children are restricted in certain contexts (descendants of fo:leader, or the fo:inline child of fo:footnote).

## Code Samples

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_inline -->
```xml
(#PCDATA|%inline;|%block;)*
```

## See Also

- [fo:inline-container](fo-inline-container.md) — for inline reference-areas with different writing-modes
- [fo:bidi-override](fo-bidi-override.md) — for overriding the Unicode BIDI algorithm
- [fo:block](fo-block.md) — the block-level counterpart
- [fo:leader](fo-leader.md) — for generating leaders and rules
- [fo:character](fo-character.md) — for explicit character-to-glyph mapping
