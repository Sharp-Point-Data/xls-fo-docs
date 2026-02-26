# fo:ruby

## Summary

The `fo:ruby` formatting object is used to contain a string of text that has ruby annotations. Ruby is a typographic convention used primarily in East Asian documents to provide pronunciation guidance or semantic annotations for characters. The `fo:ruby` supports both simple ruby (a single base with a single annotation) and complex ruby (multiple bases with multiple annotations using containers).

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_ruby -->

## Areas

The `fo:ruby` formatting object generates one or more normal inline-areas. It returns these areas, together with any page-level-out-of-line areas and reference-level-out-of-line areas returned by the children of the `fo:ruby`.

## Constraints

- No area may have more than one normal child area returned by the same `fo:ruby` formatting object.
- The children of each normal area returned by an `fo:ruby` must satisfy the constraints specified in the inline-building section of the Area Model.
- In addition the constraints imposed by the traits derived from the properties applicable to this formatting object must be satisfied. The geometric constraints are rigorously defined in the Area Model.

## Content Model

```
((fo:ruby-base, (fo:ruby-text |
    (fo:ruby-parenthesis, fo:ruby-text, fo:ruby-parenthesis)) |
    (fo:ruby-base-container, fo:ruby-text-container, fo:ruby-text-container?))
```

There are two structural patterns:

1. **Simple ruby:** `fo:ruby-base` followed by either:
   - `fo:ruby-text` alone, or
   - `fo:ruby-parenthesis`, `fo:ruby-text`, `fo:ruby-parenthesis` (ruby text with fallback parentheses).
2. **Complex ruby:** `fo:ruby-base-container` followed by `fo:ruby-text-container`, and optionally a second `fo:ruby-text-container` (for double-sided ruby).

In addition this formatting object may have a sequence of zero or more `fo:marker`s as its initial children.

## Properties

| Property | Inherited | Conformance Level |
|---|---|---|
| Common Accessibility Properties | N/A | Basic |
| Common Aural Properties | N/A | Extended |
| Common Border, Padding, and Background Properties | N/A | Basic |
| Common Font Properties | yes | Basic |
| Common Margin Properties - Inline | N/A | Basic |
| Common Relative Position Properties | N/A | Extended |
| `alignment-adjust` | no | Extended |
| `alignment-baseline` | no | Extended |
| `baseline-shift` | no | Extended |
| `block-progression-dimension` | no | Basic |
| `color` | yes | Basic |
| `dominant-baseline` | no | Extended |
| `height` | no | Basic |
| `id` | N/A | Basic |
| `index-class` | N/A | Extended |
| `index-key` | N/A | Extended |
| `inline-progression-dimension` | no | Basic |
| `keep-with-next` | no | Extended |
| `keep-with-previous` | no | Extended |
| `line-height` | yes | Basic |
| `text-decoration` | no | Basic |
| `visibility` | no | Extended |
| `width` | no | Basic |
| `wrap-option` | yes | Basic |
| `ruby-align` | yes | Extended |
| `ruby-overhang` | yes | Extended |
| `ruby-position` | yes | Extended |
| `ruby-proportion` | yes | Extended |
| `ruby-mode` | yes | Extended |

## Usage Notes

- Use simple ruby (with `fo:ruby-base` and `fo:ruby-text`) for the common case of annotating a single base string with a single annotation string (e.g., furigana in Japanese).
- Use `fo:ruby-parenthesis` around the `fo:ruby-text` to provide fallback rendering for user agents that cannot render ruby annotations; the parentheses will be shown inline as delimiters.
- Use complex ruby (with `fo:ruby-base-container` and `fo:ruby-text-container`) when multiple base strings need to share a single annotation, or when double-sided annotations (e.g., one above and one below) are needed.
- The `ruby-align` property controls how the ruby text is aligned relative to the base text.
- The `ruby-position` property controls where the annotation appears relative to the base text (e.g., "before", "after").
- The `ruby-overhang` property controls whether ruby text can overhang adjacent base characters.

## Code Samples

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_ruby -->
```xml
((fo:ruby-base, (fo:ruby-text |
    (fo:ruby-parenthesis, fo:ruby-text, fo:ruby-parenthesis)) |
    (fo:ruby-base-container, fo:ruby-text-container, fo:ruby-text-container?))
```

## See Also

- [fo:ruby-base](fo-ruby-base.md) — contains the base text being annotated
- [fo:ruby-text](fo-ruby-text.md) — contains the annotation text
- [fo:ruby-parenthesis](fo-ruby-parenthesis.md) — fallback delimiters for inline rendering
- fo:ruby-base-container — groups multiple base texts for complex ruby
- [fo:ruby-text-container](fo-ruby-text-container.md) — groups multiple annotation texts for complex ruby
- ruby-align property
- ruby-position property
- ruby-overhang property
