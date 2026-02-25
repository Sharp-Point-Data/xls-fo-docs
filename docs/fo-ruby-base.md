# fo:ruby-base

## Summary

The `fo:ruby-base` formatting object is used to contain a string of text that has ruby annotations. It holds the base text -- the primary text that the ruby annotation describes or annotates.

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_ruby-base -->

## Areas

The `fo:ruby-base` formatting object generates and returns one or more normal inline-areas.

## Constraints

- No area may have more than one normal child area returned by the same `fo:ruby-base` formatting object.
- The children of the normal area returned by an `fo:ruby-base` must satisfy the constraints specified in the inline-building section of the Area Model.

## Content Model

```
(#PCDATA|%inline;)*
```

The `fo:ruby-base` can contain character data and/or inline-level formatting objects.

## Properties

| Property | Inherited | Conformance Level |
|---|---|---|
| Common Accessibility Properties | N/A | Basic |
| Common Aural Properties | N/A | Extended |
| Common Font Properties | yes | Basic |
| Common Relative Position Properties | N/A | Extended |
| `color` | yes | Basic |
| `id` | N/A | Basic |
| `index-class` | N/A | Extended |
| `index-key` | N/A | Extended |
| `letter-spacing` | yes | Basic |
| `line-height` | yes | Basic |
| `score-spaces` | yes | Basic |
| `word-spacing` | yes | Basic |

## Usage Notes

- The `fo:ruby-base` is always a child of `fo:ruby` (in simple ruby) or `fo:ruby-base-container` (in complex ruby).
- In simple ruby, a single `fo:ruby-base` is followed by either `fo:ruby-text` or `fo:ruby-parenthesis`/`fo:ruby-text`/`fo:ruby-parenthesis`.
- In complex ruby, one or more `fo:ruby-base` elements are children of an `fo:ruby-base-container`.
- The content can be plain text (e.g., kanji characters) or inline formatting objects.

## Code Samples

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_ruby-base -->
```xml
(#PCDATA|%inline;)*
```

## See Also

- `fo:ruby` -- the parent formatting object for simple ruby
- `fo:ruby-base-container` -- the parent for base text in complex ruby
- `fo:ruby-text` -- the annotation text
- `fo:ruby-parenthesis` -- fallback delimiters
