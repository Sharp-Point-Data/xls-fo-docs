# Antenna House Extension Properties: Overflow Extension Properties

<!-- Source: XSL-FO-Reference-74-MID.pdf pp.312–476 -->

Properties controlling overflow behavior including text condensing (shrink-to-fit), overflow alignment, content replacement on overflow, and overflow limit thresholds.

## axf:condensed-text-align-last

Specifies whether to set `text-align-last="justify"` automatically after condensing the overflow.

This feature is only available when:

- Condensing in the block progression dimension.
- `font-size` or `font-stretch` condensing is occurring by `axf:overflow-condense`.
- `text-align-last` is not explicitly specified.

Values have the following meanings:

- `false`: Does nothing.
- `true`: Sets `text-align-last="justify"`.
- `justify`: Sets `text-align-last="justify"` when `text-align="justify"` is specified. Whether or not `text-align="justify"` is determined by whether or not the element with the `overflow="condense"` specified is `text-align="justify"`.
- `auto`: Follows the setting of `condensed-text-align-last` in the Option Settings File.

| Attribute | Value |
|---|---|
| **Applies to** | all block-level formatting objects |
| **Values** | `false \| true \| justify \| auto` |
| **Initial** | `auto` |
| **Inherited** | yes |

## axf:inline-overflow-align

Makes adjustments when the blocks in `<fo:inline-container>` overflow.

Values have the following meanings:

- `normal`: Does nothing. `axf:inline-overflow-align` is invalid.
- `start`: Shifts the blocks on the start side of the reference area that contains `<fo:inline-container>`.
- `end`: Shifts the blocks on the end side of the reference area that contains `<fo:inline-container>`.
- `left`: Shifts the blocks on the left side of the reference area that contains `<fo:inline-container>`.
- `right`: Shifts the blocks on the right side of the reference area that contains `<fo:inline-container>`.

| Attribute | Value |
|---|---|
| **Applies to** | `<fo:inline-container>` |
| **Values** | `normal \| start \| end \| left \| right` |
| **Initial** | `normal` |
| **Inherited** | yes |

## axf:overflow-align

Specifies the alignment of the overflowed block. This setting is invalid when `overflow="condense"` is specified.

Values have the following meanings:

- `normal`: Specifies the alignment of the block according to the `text-align` setting.
- `start`: Specifies the alignment of the block to the start side.
- `end`: Specifies the alignment of the block to the end side.
- `center`: Specifies the block to center aligned.

| Attribute | Value |
|---|---|
| **Applies to** | block-level formatting objects |
| **Values** | `normal \| start \| end \| center` |
| **Initial** | `normal` |
| **Inherited** | yes |

## axf:overflow-condense

Specifies how to condense the overflowed text within the region. When `overflow="condense"` is specified, the text within the region can be condensed by the way specified in the `axf:overflow-condense` property.

The adjustment for condensing the text includes both the inline progression direction and the block progression direction. There is a difference in the condensing process between inline and block. Inline condensing process occurs by specifying `<fo:inline-container>`, and block condensing process occurs by specifying `<fo:block-container>`.

For example, if there is an absolute value setting such as `font-size="20pt"` internally, the size setting will not be changed by the condensing process with `font-size`. The same is true for other `font-stretch` and `line-height`.

`text-align-last="justify"` may be set when the condensing process by `font-size` or `font-stretch` in a block occurs. See `axf:condensed-text-align-last`.

You can specify multiple methods, such as `="font-size font-stretch"`. In this example, if condensing process by `font-size` does not resolve the overflow, condensing process by `font-stretch` will continue to be attempted.

Values have the following meanings:

- `font-size`: Condenses the text by adjusting the font size.
- `font-stretch`: Condenses the text by adjusting the font width.
- `line-height`: Condenses the text by adjusting the line height. There is no condensing process that makes `line-height` negative.
- `letter-spacing`: Condenses the text by adjusting the letter spacing. Condensing process by specifying `letter-spacing` may cause overlapping characters. The display position of characters may also be reversed. It is recommended to avoid extreme condensing process with `axf:overflow-condense-limit-letter-spacing`.
- `auto`: It is considered `font-size` for the condensing process in the block, `font-stretch` for the condensing process in inline.
- `none`: Specifies not to condense the text. This can also be specified to the inline element and is not inherited.

| Attribute | Value |
|---|---|
| **Applies to** | all block-level formatting objects |
| **Values** | `[ font-size \| font-stretch \| line-height \| letter-spacing ]+ \| auto \| none` |
| **Initial** | `auto` |
| **Inherited** | yes |

## axf:overflow-condense-limit-font-size

Specifies the lower limit font size when `axf:overflow-condense="font-size"` is specified.

When the content exceeds the limit shown by `<length>`, the region still overflows. Then a solution can be specified, for example: `axf:overflow-condense-limit-font-size="4pt hidden"`. However, it is ignored when the following condensing method is specified in `axf:overflow-condense`.

When overflow cannot be resolved, such as when there is not enough block height or a large image is included, the condensing process may be terminated before reaching the lower limit value.

| Attribute | Value |
|---|---|
| **Applies to** | all block-level formatting objects |
| **Values** | `none \| [ <length> [ visible \| hidden \| error-if-overflow \| repeat ]? ]` |
| **Initial** | `none` |
| **Inherited** | yes |

## axf:overflow-condense-limit-font-stretch

Specifies the lower limit value when `axf:overflow-condense="font-stretch"` is specified.

When the content exceeds the limit shown by `<percentage>` or `<number>`, the region still overflows. Then a solution can be specified, for example: `axf:overflow-condense-limit-font-stretch="30% hidden"`. However, it is ignored when the following condensing method is specified in `axf:overflow-condense`.

When overflow cannot be resolved, such as when there is not enough block height or a large image is included, the condensing process may be terminated before reaching the lower limit value.

| Attribute | Value |
|---|---|
| **Applies to** | all block-level formatting objects |
| **Values** | `none \| [ [ <number> \| <percentage> ] [ visible \| hidden \| error-if-overflow \| repeat ]? ]` |
| **Initial** | `none` |
| **Inherited** | yes |

## axf:overflow-condense-limit-letter-spacing

Specifies the lower limit value when `axf:overflow-condense="letter-spacing"` is specified.

Values have the following meanings:

- `none`: It is considered that `-1em` is specified.
- `<length>`: Specifies the lower limit value of `letter-spacing`. `letter-spacing` is not made smaller than that value.

When the content exceeds the limit shown by `<length>`, the region still overflows. Then a solution can be specified.

When overflow cannot be resolved, such as when there is not enough block height or a large image is included, the condensing process may be terminated before reaching the lower limit value.

| Attribute | Value |
|---|---|
| **Applies to** | all block-level formatting objects |
| **Values** | `none \| [ <length> [ visible \| hidden \| error-if-overflow \| repeat ]? ]` |
| **Initial** | `none` |
| **Inherited** | yes |

## axf:overflow-condense-limit-line-height

Specifies the lower limit value when `axf:overflow-condense="line-height"` is specified.

Values have the following meanings:

- `none`: It is considered that `0` is specified.
- `<number>`: Specifies the lower limit value of `line-height`. `line-height` is not made smaller than that value. The value is a percentage against the font size. If you specify less than 0, it is considered that `0` is specified.

When the content exceeds the limit shown by `<number>`, the region still overflows. Then a solution can be specified, for example: `axf:overflow-condense-limit-line-height="1 hidden"`. However, it is ignored when the following condensing method is specified in `axf:overflow-condense`.

When overflow cannot be resolved, such as when there is not enough block height or a large image is included, the condensing process may be terminated before reaching the lower limit value.

| Attribute | Value |
|---|---|
| **Applies to** | all block-level formatting objects |
| **Values** | `none \| [ <number> [ visible \| hidden \| error-if-overflow \| repeat ]? ]` |
| **Initial** | `none` |
| **Inherited** | yes |

## axf:overflow-limit

Specifies the overflow limit value with `<length>`. If a single `<length>` value is specified, it gives both the inline and block overflow limit values. If two `<length>` values are specified, the first gives the inline overflow limit value and the second gives the block overflow limit value. Negative values are invalid.

When `overflow="error-if-overflow"` is specified, overflows greater than the overflow limit value are reported as error level 2 (warning) and smaller overflows are reported as error level 1 (information).

The initial values of the overflow limit can be set by `overflow-limit-inline` and `overflow-limit-block` in the Option Setting File.

This is a shorthand property for setting `axf:overflow-limit-inline` and `axf:overflow-limit-block`.

| Attribute | Value |
|---|---|
| **Applies to** | all formatting objects |
| **Values** | `<length>{1,2}` |
| **Initial** | depends on system |
| **Inherited** | yes |

## axf:overflow-limit-block

Specifies the block overflow limit value with `<length>`. Negative values are invalid.

For more details, see `axf:overflow-limit`.

| Attribute | Value |
|---|---|
| **Applies to** | all formatting objects |
| **Values** | `<length>` |
| **Initial** | depends on system |
| **Inherited** | yes |

## axf:overflow-limit-inline

Specifies the inline overflow limit value with `<length>`. Negative values are invalid.

For more details, see `axf:overflow-limit`.

| Attribute | Value |
|---|---|
| **Applies to** | all formatting objects |
| **Values** | `<length>` |
| **Initial** | depends on system |
| **Inherited** | yes |

## axf:overflow-replace

Specifies an alternative character string for the overflowed text.

When `overflow="replace"` is specified, the overflowed text is replaced by repeating the specified string. A complex character string cannot be specified.

| Attribute | Value |
|---|---|
| **Applies to** | all block-level formatting objects |
| **Values** | `<string>` |
| **Initial** | empty string |
| **Inherited** | yes |
