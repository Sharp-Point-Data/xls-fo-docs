# fo:bidi-override

## Summary

The fo:bidi-override formatting object is used when the Unicode BIDI algorithm fails. It forces a string of text to be written in a specific direction. It generates one or more normal inline-areas.

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_bidi-override -->

## Content Model

`(#PCDATA | %inline; | %block;)*`

In addition, this formatting object may have a sequence of zero or more fo:marker elements as its initial children.

An fo:bidi-override that is a descendant of an fo:leader or of the fo:inline child of an fo:footnote may not have block-level children, unless it has a nearer ancestor that is an fo:inline-container.

## Properties

| Property | Inherited | Conformance Level |
|----------|-----------|-------------------|
| Common Aural Properties | N/A | Extended |
| Common Font Properties | Yes | Basic |
| Common Relative Position Properties | No | Extended |
| color | Yes | Basic |
| direction | Yes | Basic |
| id | No | Basic |
| index-class | No | Extended |
| index-key | No | Extended |
| letter-spacing | Yes | Basic |
| line-height | Yes | Basic |
| score-spaces | Yes | Basic |
| unicode-bidi | No | Basic |
| word-spacing | Yes | Basic |

## Usage Notes

- The fo:bidi-override returns its generated inline-areas together with any normal block-areas, page-level-out-of-line areas, and reference-level-out-of-line areas returned by its children.
- The direction traits are derived from the writing-mode, direction, and unicode-bidi properties as described in the writing-mode refinement rules.
- No area may have more than one normal child area returned by the same fo:bidi-override formatting object.
- The children of each normal area returned by an fo:bidi-override must satisfy the constraints specified in the inline-building section of the area model.
- fo:bidi-override is used to override the Unicode Bidirectional Algorithm when it produces incorrect results. In most cases, the algorithm handles bidirectional text correctly without explicit overrides.

## Code Samples

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_bidi-override -->
```xml
(#PCDATA|%inline;|%block;)*
```

## See Also

- [fo:inline](fo-inline.md) — for general inline-level formatting
- [fo:inline-container](fo-inline-container.md) — for inline reference-areas with a different writing-mode
