# fo:ruby-text-container

## Summary

The `fo:ruby-text-container` formatting object is used to contain one or more strings of text that are ruby annotations. It groups multiple `fo:ruby-text` elements in complex ruby, where multiple annotation text segments correspond to the base text segments in a sibling `fo:ruby-base-container`.

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_ruby-text-container -->

## Areas

The `fo:ruby-text-container` formatting object does not generate any areas. It returns the sequence of areas created by concatenating the sequences of areas returned by each of the children of the `fo:ruby-text-container`.

## Constraints

- No area may have more than one normal child area returned by the same `fo:ruby-text` formatting object.
- The children of each normal area returned by an `fo:ruby-text` must satisfy the constraints specified in the line-building section of the Area Model.
- In addition the constraints imposed by the traits derived from the properties applicable to this formatting object must be satisfied. The geometric constraints are rigorously defined in the Area Model.

## Content Model

```
(fo:ruby-text)+
```

One or more `fo:ruby-text` children.

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
| `ruby-overhang` | yes | Extended |
| `ruby-position` | yes | Extended |

## Usage Notes

- `fo:ruby-text-container` is only used in complex ruby. In simple ruby, `fo:ruby-text` is a direct child of `fo:ruby`.
- In complex ruby, the content model within `fo:ruby` is: `fo:ruby-base-container`, `fo:ruby-text-container`, and optionally a second `fo:ruby-text-container` (for double-sided ruby).
- Each `fo:ruby-text` within the container holds one annotation segment, corresponding positionally to the `fo:ruby-base` elements in the sibling `fo:ruby-base-container`.
- When two `fo:ruby-text-container` elements are present, one provides annotations on one side of the base text (e.g., above) and the other on the opposite side (e.g., below), enabling double-sided ruby annotations.
- The `ruby-position` property on this container controls which side the annotation appears on (e.g., "before" or "after").
- The `ruby-overhang` property controls whether the annotation text can overhang adjacent base characters.

## Code Samples

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_ruby-text-container -->
```xml
(fo:ruby-text)+
```

## See Also

- [fo:ruby](fo-ruby.md) — the parent formatting object
- [fo:ruby-text](fo-ruby-text.md) — individual annotation text segments
- fo:ruby-base-container — the sibling container for base texts
- [fo:ruby-base](fo-ruby-base.md) — individual base text segments
- ruby-position property
- ruby-overhang property
