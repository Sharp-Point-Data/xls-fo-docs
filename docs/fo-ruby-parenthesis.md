# fo:ruby-parenthesis

## Summary

The `fo:ruby-parenthesis` formatting object is used to contain a string of text that is used to denote the beginning or end of ruby text when user agents do not have other ways to present ruby text distinctively from the base text. Parentheses (or similar characters) can provide an acceptable fallback. In this situation, ruby text will only degrade to be rendered inline and enclosed in the fallback parentheses. This is the least inappropriate rendering under the condition that only inline rendering is available.

The `fo:ruby-parenthesis` formatting object cannot be used with complex ruby formatting objects (i.e., it is only used in simple ruby).

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_ruby-parenthesis -->

## Areas

When generating annotation areas for ruby is not possible, the `fo:ruby-parenthesis` formatting object generates one or more normal inline-areas. It returns these areas.

## Constraints

- No area may have more than one normal child area returned by the same `fo:ruby-parenthesis` formatting object.
- The children of each normal area returned by an `fo:ruby-parenthesis` must satisfy the constraints specified in the line-building section of the Area Model.
- In addition the constraints imposed by the traits derived from the properties applicable to this formatting object must be satisfied. The geometric constraints are rigorously defined in the Area Model.

## Content Model

```
(#PCDATA)
```

The `fo:ruby-parenthesis` contains only character data, typically a single parenthesis or bracket character.

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

- The `fo:ruby-parenthesis` is used in pairs within an `fo:ruby`: one before and one after the `fo:ruby-text`.
- The content model within `fo:ruby` when using parentheses is: `fo:ruby-base`, `fo:ruby-parenthesis`, `fo:ruby-text`, `fo:ruby-parenthesis`.
- The typical content for the opening parenthesis is "(" and for the closing is ")", though any appropriate delimiter character may be used.
- When the formatter supports proper ruby annotation rendering, the parenthesis content is not displayed. It is only shown as a fallback when the user agent cannot render ruby annotations above/below the base text.
- This formatting object cannot be used with complex ruby (i.e., when using `fo:ruby-base-container` and `fo:ruby-text-container`).

## Code Samples

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_ruby-parenthesis -->
```xml
(#PCDATA)
```

## See Also

- `fo:ruby` -- the parent formatting object
- `fo:ruby-base` -- the base text being annotated
- `fo:ruby-text` -- the annotation text
