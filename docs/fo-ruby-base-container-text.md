# fo:ruby-base-container-text

## Summary

The `fo:ruby-base-container-text` formatting object is used to contain one or more strings of text that have ruby annotations. It groups multiple `fo:ruby-base` elements in complex ruby, where multiple base text segments share annotations from one or more `fo:ruby-text-container` elements.

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_ruby-base_container -->

## Areas

The `fo:ruby-base-container` formatting object does not generate any areas. It returns the sequence of areas created by concatenating the sequences of areas returned by each of the children of the `fo:ruby-base-container`.

## Constraints

- No area may have more than one normal child area returned by the same `fo:ruby-base-container` formatting object.
- The children of each normal area returned by an `fo:ruby` must satisfy the constraints specified in the line-building section of the Area Model.

## Content Model

```
(fo:ruby-base)+
```

One or more `fo:ruby-base` children.

## Properties

No properties are listed in the spec for this formatting object. It serves as a structural container, grouping `fo:ruby-base` elements for complex ruby.

## Usage Notes

- `fo:ruby-base-container-text` (referenced in the spec as `fo:ruby-base-container`) is only used in complex ruby. In simple ruby, `fo:ruby-base` is a direct child of `fo:ruby`.
- In complex ruby, the content model within `fo:ruby` is: `fo:ruby-base-container`, `fo:ruby-text-container`, and optionally a second `fo:ruby-text-container`.
- Each `fo:ruby-base` within the container holds one segment of the base text. The annotation texts in the sibling `fo:ruby-text-container`(s) correspond positionally to these base segments.
- Complex ruby is used when multiple base characters need to be annotated as a group, or when double-sided annotations (above and below) are needed.

## Code Samples

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_ruby-base_container -->
```xml
(fo:ruby-base)+
```

## See Also

- [fo:ruby](fo-ruby.md) — the parent formatting object
- [fo:ruby-base](fo-ruby-base.md) — individual base text segments
- [fo:ruby-text-container](fo-ruby-text-container.md) — the sibling container for annotation texts
- [fo:ruby-text](fo-ruby-text.md) — individual annotation text segments
