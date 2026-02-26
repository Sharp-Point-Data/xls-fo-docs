# fo:scaling-value-citation

## Summary

The fo:scaling-value-citation is used to obtain the scale-factor applied to the cited fo:external-graphic. It generates and returns a single normal inline-area. It may be used to provide the scale used in applications where a graphic is normally shown at true size, but is scaled down if it does not fit.

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_scaling-value-citation -->

## Content Model

`EMPTY`

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
| country | Yes | Extended |
| dominant-baseline | No | Extended |
| format | No | Extended |
| grouping-separator | No | Extended |
| grouping-size | No | Extended |
| id | No | Basic |
| index-class | No | Extended |
| index-key | No | Extended |
| keep-with-next | No | Extended |
| keep-with-previous | No | Extended |
| language | Yes | Extended |
| letter-spacing | Yes | Basic |
| letter-value | No | Extended |
| line-height | Yes | Basic |
| intrinsic-scale-value | No | Extended |
| ref-id | No | Extended |
| score-spaces | Yes | Basic |
| scale-option | No | Extended |
| text-altitude | No | Extended |
| text-decoration | No | Basic |
| text-depth | No | Extended |
| text-shadow | No | Extended |
| text-transform | Yes | Basic |
| visibility | Yes | Extended |
| word-spacing | Yes | Basic |
| wrap-option | Yes | Extended |

## Usage Notes

- The cited fo:external-graphic is the fo:external-graphic with an id trait matching the ref-id trait of the fo:scaling-value-citation.
- The applied scale-factor is the scale-factor that was applied to the intrinsic size of the cited fo:external-graphic multiplied by the value of the intrinsic-scale-value property. It is expressed as an integer percentage value.
- The scale-option property specifies if the scale-factor for the width or height should be used.
- In the case when the graphics format does not specify an intrinsic size of the graphic and the size has been determined in an implementation-defined manner, the scale factor obtained may not be meaningful.
- The applied scale-factor string is obtained by converting the applied scale-factor in accordance with the number to string conversion properties (format, grouping-separator, grouping-size, letter-value, country, and language).
- The child areas of the generated inline-area are the same as the result of formatting a result-tree fragment consisting of fo:character flow objects, one for each character in the applied scale-factor string and with only the character property specified.

## Code Samples

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_scaling-value-citation -->
```xml
EMPTY
```

## See Also

- [fo:external-graphic](fo-external-graphic.md) — the formatting object whose scale-factor is cited
- [fo:page-number-citation](fo-page-number-citation.md) — similar pattern for citing page numbers
