# Antenna House Extension Properties: Float Extension Properties

<!-- Source: XSL-FO-Reference-74-MID.pdf pp.312–476 -->

Extensions to float behavior including page floats, float positioning (x/y coordinates), wrap control, centering, and margin settings for advanced float placement in PDF output.

## axf:float-centering-x

Specifies whether the float is centered when the width for the text wrapping around the float is insufficient.

Values have the following meanings:

- `none`: The float is not centered.
- `auto`: The float is centered when the width for the text wrapping around the float is less than the width specified by the `axf:float-min-wrap-x` property.
- `<length>` / `<percentage>`: The float is centered when the width for the text wrapping around the float is less than the width specified by this property.

| Attribute | Value |
|---|---|
| **Applies to** | `<fo:float>` |
| **Values** | `none \| auto \| <length> \| <percentage>` |
| **Initial** | `none` |
| **Inherited** | no |

## axf:float-centering-y

Specifies whether the float is centered when the extent for the text placed before and after the float is insufficient.

Values have the following meanings:

- `none`: The float is not centered.
- `auto`: The float is centered when the extent for the text placed before and after the float is less than the extent specified by the `axf:float-min-wrap-y` property.
- `<length>` / `<percentage>`: The float is centered when the extent for the text placed before and after the float is less than the extent specified by this property.

| Attribute | Value |
|---|---|
| **Applies to** | `<fo:float>` |
| **Values** | `none \| auto \| <length> \| <percentage>` |
| **Initial** | `none` |
| **Inherited** | no |

## axf:float-float-margin-x

Specifies the space between the float and another neighboring float (in x-axis).

The initial value `auto` is same as the `axf:float-margin-x` value. When two values are specified, the first one will be the value of the start side, the next one will be the value of the end side.

The `axf:float-float-margin-x` value cannot exceed the `axf:float-margin-x` value.

| Attribute | Value |
|---|---|
| **Applies to** | `<fo:float>` |
| **Values** | `auto \| [[<length> \| <percentage>] [<length> \| <percentage>]?]` |
| **Initial** | `auto` |
| **Inherited** | no |

## axf:float-float-margin-y

Specifies the space between the float and another neighboring float (in y-axis).

The initial value `auto` is same as the `axf:float-margin-y` value. When two values are specified, the first one will be the value of the before side, the next one will be the value of the after side.

The `axf:float-float-margin-y` value cannot exceed the `axf:float-margin-y` value.

| Attribute | Value |
|---|---|
| **Applies to** | `<fo:float>` |
| **Values** | `auto \| [[<length> \| <percentage>] [<length> \| <percentage>]?]` |
| **Initial** | `auto` |
| **Inherited** | no |

## axf:float-margin-x

Specifies the space between the float and the text wrapping around the float (in x-axis).

When two values are specified, the first one will be the value of the start side, the next one will be the value of the end side.

| Attribute | Value |
|---|---|
| **Applies to** | `<fo:float>` |
| **Values** | `[<length> \| <percentage>] [<length> \| <percentage>]?` |
| **Initial** | `0pt` |
| **Inherited** | no |

## axf:float-margin-y

Specifies the space between the float and the text before and after the float (in y-axis).

When two values are specified, the first one will be the value of the before side, the next one will be the value of the after side.

| Attribute | Value |
|---|---|
| **Applies to** | `<fo:float>` |
| **Values** | `[<length> \| <percentage>] [<length> \| <percentage>]?` |
| **Initial** | `0pt` |
| **Inherited** | no |

## axf:float-min-wrap-x

Specifies the minimum width for the text wrapping around the float.

If the width for the text wrapping around the float is smaller than the width specified by this property, the text doesn't wrap.

The initial value `normal` is the minimum wrapping width of normal floats. It is same as `0pt`.

| Attribute | Value |
|---|---|
| **Applies to** | `<fo:float>` |
| **Values** | `normal \| <length> \| <percentage>` |
| **Initial** | `normal` |
| **Inherited** | no |

## axf:float-min-wrap-y

Specifies the minimum extent for the text placed before and after the float.

When the `axf:float-y` value is not `none` and there is remaining space to place the text before or after the float within the formatting target area, if the extent of that space is smaller than the extent specified by this property, the text is not placed to that space.

If the value of `axf:float-y` is `none`, it is processed as follows:

- If the value of `axf:float-move` is `auto-next` and there is space left to place text after the float within the formatting target area, if its height (width in vertical writing) is smaller than the height (width in vertical writing) specified in this property, moves the float position so that its height (width in vertical writing) becomes zero. Text that was after the float will move before the float.
- If the value of `axf:float-move` is `auto-move`, it is the same as the case of `auto-next`, but within the formatting target area, if the height (width in vertical writing) of the text placement space before the float, not only after the float, is smaller than the height (width in vertical writing) specified in this property, moves the float position so that its height (width in vertical writing) becomes zero. Text that was before the float will move after the float.
- If the value of `axf:float-move` is other than these, text will wrap around if there is space left to place text after the float in the formatting target area, otherwise it will not wrap around.

The initial value `normal` is the same as `0pt`.

| Attribute | Value |
|---|---|
| **Applies to** | `<fo:float>` |
| **Values** | `normal \| <length> \| <percentage>` |
| **Initial** | `normal` |
| **Inherited** | no |

## axf:float-move

Specifies whether the float moves to the next page (or column).

Values have the following meanings:

- `auto`: Same as `keep` if `axf:float-y` is `none`, same as `auto-next` otherwise.
- `next`: The float is moved to the next page (or column).
- `auto-next`: The float is moved to the next page (or column) if there is not enough space in the current page (or column).
- `auto-move`: The float is moved to the next page (or column) if there is not enough space in the current page (or column). It is also possible that the float anchor and around text are moved to the next page (or column) instead.
- `keep`: The float and its anchor are always placed on the same page (or column). If there is not enough space for that, a page (or column) break occurs before the float anchor and a blank space is left.
- `keep-float`: Although it is almost the same as `keep`, the following points differ. With `keep`, `keep-with-next="always"` is automatically set to anchor area and a page break (or column break) is deterred between the next area. However, it is not performed by `keep-float`. The difference on operation will appear when the height of anchor area is zero.
- `after-edge`: Aligns the bottom edge of the float with the position of the anchor when `axf:float-y` is `none`.
- `<integer>`: The numerical value is considered the page number and moves the float to that page. If it is larger than the number of pages in the document, pages with no contents (not blank pages) will be inserted. It does not work when `axf:float-y` is `none`. At that time, it is considered that `auto` is specified. (New in V7.1) Page numbers are considered logical page numbers.

If both `axf:float-x` and `axf:float-y` are `none`, the object is not floated and the `axf:float-move` specification is ineffective.

| Attribute | Value |
|---|---|
| **Applies to** | `<fo:float>` |
| **Values** | `auto \| normal \| page \| multicol \| column` |
| **Initial** | `auto` |
| **Inherited** | no |

## axf:float-offset-x

Specifies the offset placement for the float (in x-axis).

If `axf:float-x` is `start`, the offset to the end side is specified. If it is `end`, the offset to the start side is specified.

| Attribute | Value |
|---|---|
| **Applies to** | `<fo:float>` |
| **Values** | `<length> \| <percentage>` |
| **Initial** | `0pt` |
| **Inherited** | no |

## axf:float-offset-y

Specifies the offset placement for the float (in y-axis).

If `axf:float-y` is `before`, the offset to the after side is specified. If it is `after`, the offset to the before side is specified.

| Attribute | Value |
|---|---|
| **Applies to** | `<fo:float>` |
| **Values** | `<length> \| <percentage>` |
| **Initial** | `0pt` |
| **Inherited** | no |

## axf:float-reference

Specifies reference area where the float is placed.

Values have the following meanings:

- `auto`: Same as `normal`.
- `normal`: The float is placed in the current reference area.
- `page`: The float is placed in the page area (`<fo:region-body>`).
- `multicol`: The float is placed in the multi-column area.
- `column`: The float is placed in the column area.

When `axf:float-y` is `none`, the reference area in x-axis will be set.

| Attribute | Value |
|---|---|
| **Applies to** | `<fo:float>` |
| **Values** | `auto \| normal \| page \| multicol \| column` |
| **Initial** | `auto` |
| **Inherited** | no |

## axf:float-wrap

Specifies the text wrapping.

Values have the following meanings:

- `auto`: Same as `wrap` if `axf:float-x` is other than `none`. Same as `skip` if it is `none`.
- `wrap`: Wraps the text around the float. However, when there is a space on both side of a float within the column (by specifying `center` to `axf:float-x` or `axf:float-offset-x`), it is the same as `skip`.
- `skip`: The text doesn't wrap around the float. The text is positioned by skipping the float.

| Attribute | Value |
|---|---|
| **Applies to** | `<fo:float>` |
| **Values** | `auto \| wrap \| skip` |
| **Initial** | `auto` |
| **Inherited** | no |

## axf:float-x

Specifies horizontal (or vertical if writing-mode is vertical) float alignment.

Values have the following meanings:

- `none`: Not floated horizontally (or vertically if writing-mode is vertical).
- `start`: Floated to the start side. Same as `left` in horizontal left-to-right writing-mode.
- `end`: Floated to the end side. Same as `right` in horizontal left-to-right writing-mode.
- `left`: Floated to the left side. Used only for horizontal writing. It cannot be specified for vertical writing.
- `right`: Floated to the right side. Used only for horizontal writing. It cannot be specified for vertical writing.
- `top`: Floated to the top. Used only for vertical writing. It cannot be specified for horizontal writing.
- `bottom`: Floated to the bottom. Used only for vertical writing. It cannot be specified for horizontal writing.
- `center`: Floated to the center horizontally (or vertically if writing-mode is vertical).
- `inside`: Floated to the inside (left side on a right page, right side on a left page). Used only for horizontal writing. It cannot be specified for vertical writing.
- `outside`: Floated to the outside (right side on a right page, left side on a left page). Used only for horizontal writing. It cannot be specified for vertical writing.
- `alternate`: When the float area is in the first column, it's considered that `end` is specified, when the float area is in the last column, it's considered that `start` is specified, if it is not in the column, it's considered that `center` is specified.
- `column-outside`: When the float area is in the last column, it's considered that `end` is specified, when the float area is in other columns, it's considered that `start` is specified, if it is not in the column, it's considered that `start` is specified. (New in V7.1)

| Attribute | Value |
|---|---|
| **Applies to** | `<fo:float>` |
| **Values** | `none \| start \| end \| left \| right \| top \| bottom \| center \| inside \| outside \| alternate \| column-outside` |
| **Initial** | `none` |
| **Inherited** | no |

## axf:float-y

Specifies vertical (or horizontal if writing-mode is vertical) float alignment.

Values have the following meanings:

- `none`: Not floated vertically (or horizontally if writing-mode is vertical).
- `before`: Floated to the before side. Same as `top` in horizontal left-to-right writing-mode.
- `after`: Floated to the after side. Same as `bottom` in horizontal left-to-right writing-mode.
- `top`: Floated to the top. Used only for horizontal writing. It cannot be specified for vertical writing.
- `bottom`: Floated to the bottom. Used only for horizontal writing. It cannot be specified for vertical writing.
- `left`: Floated to the left side. Used only for vertical writing. It cannot be specified for horizontal writing.
- `right`: Floated to the right side. Used only for vertical writing. It cannot be specified for horizontal writing.
- `center`: Floated to the center vertically (or horizontally if writing-mode is vertical).
- `inside`: Floated to the inside (left side on a right page, right side on a left page). Used only for vertical writing. It cannot be specified for horizontal writing.
- `outside`: Floated to the outside (right side on a right page, left side on a left page). Used only for vertical writing. It cannot be specified for horizontal writing.
- `anchor`: Floated to the anchor point.

| Attribute | Value |
|---|---|
| **Applies to** | `<fo:float>` |
| **Values** | `none \| before \| after \| top \| bottom \| left \| right \| center \| inside \| outside \| anchor` |
| **Initial** | `none` |
| **Inherited** | no |
