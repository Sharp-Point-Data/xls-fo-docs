# fo:ruby-text

## Summary

The `fo:ruby-text` formatting object is used to contain a string of text that is a ruby annotation. This is the annotation text that appears alongside the base text, typically in a smaller font size, providing pronunciation guidance or semantic information.

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_ruby-text -->

## Areas

The `fo:ruby-text` formatting object generates one normal annotation-area. It returns this area.

## Constraints

- No area may have more than one normal child area returned by the same `fo:ruby-text` formatting object.
- The children of each normal area returned by an `fo:ruby-text` must satisfy the constraints specified in the inline-building section of the Area Model.
- In addition the constraints imposed by the traits derived from the properties applicable to this formatting object must be satisfied. The geometric constraints are rigorously defined in the Area Model.

## Content Model

```
#PCDATA
```

The `fo:ruby-text` contains only character data (text content). It does not accept child formatting objects.

## Properties

| Property | Inherited | Conformance Level |
|---|---|---|
| Common Font Properties | yes | Basic |
| `color` | yes | Basic |
| `letter-spacing` | yes | Basic |
| `score-spaces` | yes | Basic |
| `text-decoration` | no | Basic |
| `text-shadow` | no | Extended |
| `text-transform` | yes | Basic |
| `word-spacing` | yes | Basic |
| `ruby-size` | no | Extended |
| `ruby-proportion` | yes | Extended |

## Usage Notes

- The `fo:ruby-text` is a child of either `fo:ruby` (in simple ruby, optionally bracketed by `fo:ruby-parenthesis` elements) or `fo:ruby-text-container` (in complex ruby).
- The content is typically pronunciation text (e.g., hiragana characters for Japanese kanji, pinyin for Chinese characters, or bopomofo).
- The `ruby-size` property controls the font size of the annotation relative to the base text.
- The `ruby-proportion` property controls how the annotation text is sized relative to the base.
- Only `#PCDATA` is allowed as content -- no inline formatting objects.

## Code Samples

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_ruby-text -->
```xml
#PCDATA
```

## See Also

- `fo:ruby` -- the parent formatting object for simple ruby
- `fo:ruby-base` -- the base text being annotated
- `fo:ruby-parenthesis` -- fallback delimiters for inline rendering
- `fo:ruby-text-container` -- groups annotation texts for complex ruby
- `ruby-size` property
- `ruby-align` property
- `ruby-position` property
