# Antenna House Extension Properties: Border Extension Properties

<!-- Source: XSL-FO-Reference-74-MID.pdf pp.312-476 -->

Extensions to border styling including border-radius (rounded corners), box-shadow, diagonal borders, double-line thickness control, and wave-form borders.

## axf:border-connection-form

Specifies the shape of the connecting portion of borders. In the table of border-collapse="collapse", axf:border-connection-form specified in `<fo:table-row>`, `<fo:table-cell>`, etc. in that table is invalid. The one specified in `<fo:table>` is adopted.

Values have the following meanings:

- **wedge:** Connects borders in wedge shape. Forms the X shape at the cross-shaped intersecting portion, and forms the Y shape at the T-shaped intersecting portion.
- **mixed:** Connects borders with the same thickness in rectangle shape at the T-shaped intersecting portion. Others will be in wedge shape.
- **precedence:** Draws thick borders to the edge. For the same thickness, draws a stronger border to the edge by the border priority.

| Attribute | Value |
|---|---|
| **Applies to** | all elements |
| **Values** | wedge \| mixed \| precedence |
| **Initial** | mixed |
| **Inherited** | yes |

## axf:border-double-thickness

Specifies the line thickness of border-style="double". In `<value>`, either `<number>` or `<length>` can be specified. The values are outside line width, spacing and inside line width in order from left to right. If the value is omitted, it is considered to be equivalent to the preceding value. Negative values are not available. The line width can directly be specified in `<length>`. We do not guarantee the best result if the total of `<length>` exceeds the border-width. The values in `<number>` is summed and then the total of `<length>` is deducted from the actual border-width for proportional distribution.

For example, if the border-width is 10pt and axf:border-double-thickness="4pt 2 1" is specified, it will be shown as follows:

- Outside line width = 4pt
- Spacing = (10pt-4pt)/(2+1)*2 = 4pt
- Inside line width = (10pt-4pt)/(2+1)*1 = 2pt

| Attribute | Value |
|---|---|
| **Applies to** | all elements |
| **Values** | `<value>` [ `<value>` [ `<value>` ]] |
| **Initial** | 1 |
| **Inherited** | yes |

## axf:border-top-right-radius

Specifies the radii of the rounded corners. The first value is the horizontal radius (or vertical if vertical writing). The second value is the other radius. If the second length is omitted it is equal to the first. If either length is less or equal 0, the corner is square, not rounded. When specifying rounding corners for the table, if border-collapse="collapse" is specified, axf:border-radius is effective only when specified to `<fo:table>`.

If diagonal is specified, the diagonal border will be drawn in a straight line without being rounded. Rounded corners do not apply to the border-style wave.

| Attribute | Value |
|---|---|
| **Applies to** | all elements which can have borders |
| **Values** | [`<length>` \| `<percentage>`] [`<length>` \| `<percentage>`]? diagonal? |
| **Initial** | 0 |
| **Inherited** | no |

## axf:border-triple-thickness

Specifies the line thickness of border-style="triple". In `<value>`, either `<number>` or `<length>` can be specified. The values are outside line width, spacing, middle line width, spacing, and inside line width in order from left to right. If the value is omitted, it is considered to be equivalent to the preceding value. Negative values are not available. See axf:border-double-thickness for `<value>`.

| Attribute | Value |
|---|---|
| **Applies to** | all elements |
| **Values** | `<value>` {1,5} |
| **Initial** | 1 |
| **Inherited** | yes |

## axf:border-wave-form

Specifies the wave form of border-style="wave", border-style="double-wave". In `<value>`, either `<number>` or `<length>` or auto can be specified. The values are wave form and line width in order from left to right. If the value is auto or omitted, it is considered 6 and 0.125 each. Negative values are not available. The wave form or the line width can directly be specified in `<length>`. `<number>` is proportional to the border-width. The third value is effective for double-wave and indicates the wave width. If the value is omitted or auto, it is considered 0.5.

| Attribute | Value |
|---|---|
| **Applies to** | all elements |
| **Values** | `<value>`{1,3} |
| **Initial** | auto |
| **Inherited** | yes |

## axf:box-shadow

Specifies the box shadow. Values have the following meanings:

- **none:** No shadow is displayed.
- **inset:** An inner shadow is displayed.

The meanings of `<length>`s and a `<color>` are as follows:

- The first `<length>` is an offset of a horizontal shadow. It becomes a right-side shadow of a region when a positive value is specified. It becomes a left-side shadow of a region when a negative value is specified.
- The second `<length>` is an offset of a vertical shadow. It becomes a bottom-side shadow of a region when a positive value is specified. It becomes a top-side shadow of a region when a negative value is specified.
- The 3rd `<length>` must be a non-negative value and specifies the blur radius. If the value is 0, there is no blur.
- The 4th `<length>` extends a shadow. When a positive value is specified, the region will be expanded. When a negative value is specified, the region will be reduced.
- The color of the shadow can be specified by `<color>`.

CAUTION: The minimum unit of `<length>` which can be specified is 1in/96=0.265mm. The value is rounded to its multiple number.

CAUTION: The blur setting is ignored with the device that cannot output in transparent mode like PDF/X. The blur setting is also ignored when transparency output is disabled.

| Attribute | Value |
|---|---|
| **Applies to** | all elements which can have borders |
| **Values** | none \| [inset? && [ `<length>`{2,4} && `<color>`? ]]# |
| **Initial** | none |
| **Inherited** | no |

## axf:diagonal-border-color

Specifies the color of the diagonal border.

| Attribute | Value |
|---|---|
| **Applies to** | all elements which can have borders |
| **Values** | `<color>` |
| **Initial** | the value of the color property |
| **Inherited** | yes |

## axf:diagonal-border-style

Specifies the style of the diagonal border.

| Attribute | Value |
|---|---|
| **Applies to** | all elements which can have borders |
| **Values** | `<border-style>` |
| **Initial** | none |
| **Inherited** | no |

## axf:diagonal-border-width

Specifies the width of the diagonal border.

| Attribute | Value |
|---|---|
| **Applies to** | all elements which can have borders |
| **Values** | `<border-width>` |
| **Initial** | medium |
| **Inherited** | yes |

## axf:reverse-diagonal-border-color

Specifies the color of the reverse diagonal border.

| Attribute | Value |
|---|---|
| **Applies to** | all elements which can have borders |
| **Values** | `<color>` |
| **Initial** | the value of the 'color' property |
| **Inherited** | yes |

## axf:reverse-diagonal-border-style

Specifies the style of the reverse diagonal border.

| Attribute | Value |
|---|---|
| **Applies to** | all elements which can have borders |
| **Values** | `<border-style>` |
| **Initial** | none |
| **Inherited** | no |

## axf:reverse-diagonal-border-width

Specifies the width of the reverse diagonal border.

| Attribute | Value |
|---|---|
| **Applies to** | all elements which can have borders |
| **Values** | `<border-width>` |
| **Initial** | medium |
| **Inherited** | yes |
