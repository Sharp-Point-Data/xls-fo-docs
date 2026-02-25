# Table Properties

## Overview

These properties control the layout and behavior of tables in XSL-FO, including border models, column and row spanning, header/footer repetition, and table pagination. Many of these properties apply to `fo:table`, `fo:table-column`, `fo:table-cell`, `fo:table-row`, `fo:table-body`, `fo:table-header`, and `fo:table-footer`.

<!-- Source: https://www.w3.org/TR/xslfo20/#border-after-precedence -->

## Properties

### border-after-precedence

| Field | Value |
|---|---|
| **Values** | `force \| <integer> \| inherit` |
| **Initial** | fo:table: 6, fo:table-cell: 5, fo:table-column: 4, fo:table-row: 3, fo:table-body: 2, fo:table-header: 1, fo:table-footer: 0 |
| **Applies to** | fo:table, fo:table-body, fo:table-header, fo:table-footer, fo:table-column, fo:table-row, fo:table-cell |
| **Inherited** | No |
| **Conformance** | Extended |

<!-- Source: https://www.w3.org/TR/xslfo20/#border-after-precedence -->

Specifies the precedence of the border specification on this formatting object for the border-after.

- **force** -- The precedence is higher than any `<integer>`.
- **\<integer\>** -- A numeric precedence specification. A higher value has a higher precedence than a lower one.

### border-before-precedence

| Field | Value |
|---|---|
| **Values** | `force \| <integer> \| inherit` |
| **Initial** | fo:table: 6, fo:table-cell: 5, fo:table-column: 4, fo:table-row: 3, fo:table-body: 2, fo:table-header: 1, fo:table-footer: 0 |
| **Applies to** | fo:table, fo:table-body, fo:table-header, fo:table-footer, fo:table-column, fo:table-row, fo:table-cell |
| **Inherited** | No |
| **Conformance** | Extended |

<!-- Source: https://www.w3.org/TR/xslfo20/#border-before-precedence -->

Specifies the precedence of the border specification on this formatting object for the border-before.

See definition of property `border-after-precedence`.

### border-collapse

| Field | Value |
|---|---|
| **Values** | `collapse \| collapse-with-precedence \| separate \| inherit` |
| **Initial** | `collapse` |
| **Applies to** | fo:table |
| **Inherited** | Yes |
| **Conformance** | Basic |

<!-- Source: https://www.w3.org/TR/xslfo20/#border-collapse -->

This property selects a table's border model. The value "separate" selects the separated borders border model. The value "collapse" selects the collapsing borders model.

- **collapse** -- Selects the collapsing borders model.
- **separate** -- Selects the separated borders border model.
- **collapse-with-precedence** -- XSL addition. Selects the collapsing borders model and the use of the border precedence properties for conflict resolution.

### border-end-precedence

| Field | Value |
|---|---|
| **Values** | `force \| <integer> \| inherit` |
| **Initial** | fo:table: 6, fo:table-cell: 5, fo:table-column: 4, fo:table-row: 3, fo:table-body: 2, fo:table-header: 1, fo:table-footer: 0 |
| **Applies to** | fo:table, fo:table-body, fo:table-header, fo:table-footer, fo:table-column, fo:table-row, fo:table-cell |
| **Inherited** | No |
| **Conformance** | Extended |

<!-- Source: https://www.w3.org/TR/xslfo20/#border-end-precedence -->

Specifies the precedence of the border specification on this formatting object for the border-end.

See definition of property `border-after-precedence`.

### border-separation

| Field | Value |
|---|---|
| **Values** | `<length-bp-ip-direction> \| inherit` |
| **Initial** | `.block-progression-direction="0pt" .inline-progression-direction="0pt"` |
| **Applies to** | fo:table |
| **Inherited** | Yes |
| **Conformance** | Basic |

<!-- Source: https://www.w3.org/TR/xslfo20/#border-separation -->

In the separate borders model, each cell has an individual border. The "border-separation" property specifies the distance between the borders of adjacent cells. This space is filled with the background of the table element. Rows, columns, row groups, and column groups cannot have borders (i.e., user agents must ignore the border properties for those elements).

- **\<length-bp-ip-direction\>** -- The lengths specify the distance that separates adjacent cell borders in the row-stacking-direction (given by the block-progression-direction of the table), and in the column-stacking-direction (given by the inline-progression-direction of the table).

### border-start-precedence

| Field | Value |
|---|---|
| **Values** | `force \| <integer> \| inherit` |
| **Initial** | fo:table: 6, fo:table-cell: 5, fo:table-column: 4, fo:table-row: 3, fo:table-body: 2, fo:table-header: 1, fo:table-footer: 0 |
| **Applies to** | fo:table, fo:table-body, fo:table-header, fo:table-footer, fo:table-column, fo:table-row, fo:table-cell |
| **Inherited** | No |
| **Conformance** | Extended |

<!-- Source: https://www.w3.org/TR/xslfo20/#border-start-precedence -->

Specifies the precedence of the border specification on this formatting object for the border-start.

See definition of property `border-after-precedence`.

### caption-side

| Field | Value |
|---|---|
| **Values** | `before \| after \| start \| end \| top \| bottom \| left \| right \| inherit` |
| **Initial** | `before` |
| **Applies to** | fo:table-and-caption |
| **Inherited** | Yes |
| **Conformance** | Extended |

<!-- Source: https://www.w3.org/TR/xslfo20/#caption-side -->

This property specifies the position of the caption box with respect to the table box.

- **before** -- Positions the caption before the table in the block-progression-direction.
- **after** -- Positions the caption after the table in the block-progression-direction.
- **start** -- Positions the caption before the table in the inline-progression-direction.
- **end** -- Positions the caption after the table in the inline-progression-direction.
- **top** -- Positions the caption box above the table box.
- **bottom** -- Positions the caption box below the table box.
- **left** -- Positions the caption box to the left of the table box.
- **right** -- Positions the caption box to the right of the table box.

XSL modifications: The CSS qualifications (1) and (2) do not apply. The last three sentences in the last paragraph (referencing "vertical-align") do not apply.

### column-number

| Field | Value |
|---|---|
| **Values** | `<number>` |
| **Initial** | see prose |
| **Applies to** | fo:table-column, fo:table-cell |
| **Inherited** | No |
| **Conformance** | Basic |

<!-- Source: https://www.w3.org/TR/xslfo20/#column-number -->

A positive integer. If a non-positive or non-integer value is provided, the value will be rounded to the nearest integer value greater than or equal to 1.

For an `fo:table-column` formatting object, it specifies the column-number of the table cells that may use properties from this `fo:table-column` formatting object by using the from-table-column() function. The initial value is 1 plus the column-number of the previous table-column, if there is a previous table-column, and otherwise 1.

For an `fo:table-cell` it specifies the number of the first column to be spanned by the table-cell. The initial value is the current column-number. For the first table-cell in a table-row, the current column number is 1. For other table-cells, the current column-number is the column-number of the previous table-cell in the row plus the number of columns spanned by that previous cell.

Note: There is no requirement for column-numbers to be monotonically increasing from formatting object to formatting object.

### column-width

| Field | Value |
|---|---|
| **Values** | `<length> \| <percentage>` |
| **Initial** | see prose |
| **Applies to** | fo:table-column |
| **Inherited** | No |
| **Conformance** | Basic |

<!-- Source: https://www.w3.org/TR/xslfo20/#column-width -->

The "column-width" property specifies the width of the column whose value is given by the "column-number" property.

This property, if present, is ignored if the "number-columns-spanned" property is greater than 1. The "column-width" property must be specified for every column, unless the automatic table layout is used.

Note: The use of the "proportional-column-width()" function is only permitted when the fixed table layout is used. If the use of proportional column widths are desired on a table of an unknown explicit width, the inline-progression-dimension cannot be specified to be "auto". Instead, the width must be specified as a percentage. For example, setting `table-layout="fixed"` and `inline-progression-dimension="100%"` would allow proportional column widths while simultaneously creating a table as wide as possible in the current context.

Note: The result of using a percentage for the width may be unpredictable, especially when using the automatic table layout.

### empty-cells

| Field | Value |
|---|---|
| **Values** | `show \| hide \| inherit` |
| **Initial** | `show` |
| **Applies to** | fo:table-cell |
| **Inherited** | Yes |
| **Conformance** | Extended |

<!-- Source: https://www.w3.org/TR/xslfo20/#empty-cells -->

In the separated borders model, this property controls the rendering of borders around cells and the rendering of the background of cells that have no visible content. Empty cells and cells with the "visibility" property set to "hidden" are considered to have no visible content. Visible content includes "&nbsp;" (non-breaking-space) and other whitespace except ASCII CR ("\0D"), LF ("\0A"), tab ("\09"), and space ("\20").

- **show** -- Borders are drawn around empty cells (like normal cells).
- **hide** -- No borders are drawn around empty cells. Furthermore, if all the cells in a row have a value of "hide" and have no visible content, the entire row behaves as if it had "display: none".

### ends-row

| Field | Value |
|---|---|
| **Values** | `true \| false` |
| **Initial** | `false` |
| **Applies to** | fo:table-cell |
| **Inherited** | No |
| **Conformance** | Extended |

<!-- Source: https://www.w3.org/TR/xslfo20/#ends-row -->

Specifies whether this cell ends a row. This is only allowed for table-cells that are not in table-rows.

- **true** -- This cell ends a row.
- **false** -- This cell does not end a row.

### number-columns-repeated

| Field | Value |
|---|---|
| **Values** | `<number>` |
| **Initial** | `1` |
| **Applies to** | fo:table-column |
| **Inherited** | No |
| **Conformance** | Basic |

<!-- Source: https://www.w3.org/TR/xslfo20/#number-columns-repeated -->

A positive integer. If a non-positive or non-integer value is provided, the value will be rounded to the nearest integer value greater than or equal to 1.

The "number-columns-repeated" property specifies the repetition of a table-column specification n times; with the same effect as if the `fo:table-column` formatting object had been repeated n times in the result tree. The "column-number" property, for all but the first, is the column-number of the previous one plus its value of the "number-columns-spanned" property.

Note: This handles HTML's "colgroup" element.

### number-columns-spanned

| Field | Value |
|---|---|
| **Values** | `<number>` |
| **Initial** | `1` |
| **Applies to** | fo:table-column, fo:table-cell |
| **Inherited** | No |
| **Conformance** | Basic |

<!-- Source: https://www.w3.org/TR/xslfo20/#number-columns-spanned -->

A positive integer or zero. If a negative or non-integer value is provided, the value will be rounded to the nearest integer value greater than or equal to 0. The value zero ("0") means that the cell spans all columns from the current column to the last column of the column group in which the cell is defined.

For an `fo:table-column` the "number-columns-spanned" property specifies the number of columns spanned by table-cells that may use properties from this `fo:table-column` formatting object using the from-table-column() function.

For an `fo:table-cell` the "number-columns-spanned" property specifies the number of columns which this cell spans in the column-progression-direction starting with the current column.

### number-rows-spanned

| Field | Value |
|---|---|
| **Values** | `<number>` |
| **Initial** | `1` |
| **Applies to** | fo:table-cell |
| **Inherited** | No |
| **Conformance** | Basic |

<!-- Source: https://www.w3.org/TR/xslfo20/#number-rows-spanned -->

A positive integer or zero. If a negative or non-integer value is provided, the value will be rounded to the nearest integer value greater than or equal to 0.

The `number-rows-spanned` property specifies the number of rows which this cell spans in the row-progression-direction starting with the current row. The value zero ("0") means that the cell spans all columns from the current column to the last column of the column group in which the cell is defined.

### starts-row

| Field | Value |
|---|---|
| **Values** | `true \| false` |
| **Initial** | `false` |
| **Applies to** | fo:table-cell |
| **Inherited** | No |
| **Conformance** | Extended |

<!-- Source: https://www.w3.org/TR/xslfo20/#starts-row -->

Specifies whether this cell starts a row. This is only allowed for table-cells that are not in table-rows.

- **true** -- This cell starts a row.
- **false** -- This cell does not start a row.

Note: The "starts-row" and "ends-row" properties with a "true" value are typically used when the input data does not have elements containing the cells in each row, but instead, for example, each row starts at elements of a particular type.

### table-layout

| Field | Value |
|---|---|
| **Values** | `auto \| fixed \| inherit` |
| **Initial** | `auto` |
| **Applies to** | fo:table |
| **Inherited** | No |
| **Conformance** | Basic |

<!-- Source: https://www.w3.org/TR/xslfo20/#table-layout -->

The "table-layout" property controls the algorithm used to lay out the table cells, rows, and columns.

- **fixed** -- Use the fixed table layout algorithm.
- **auto** -- Use any automatic table layout algorithm.

### table-omit-footer-at-break

| Field | Value |
|---|---|
| **Values** | `true \| false` |
| **Initial** | `false` |
| **Applies to** | fo:table |
| **Inherited** | No |
| **Conformance** | Extended |

<!-- Source: https://www.w3.org/TR/xslfo20/#table-omit-footer-at-break -->

The "table-omit-footer-at-break" property specifies if a table whose last area is not at the end of an area produced by the table should end with the content of the `fo:table-footer` formatting object or not.

- **true** -- The footer should be omitted.
- **false** -- The footer should not be omitted.

### table-omit-header-at-break

| Field | Value |
|---|---|
| **Values** | `true \| false` |
| **Initial** | `false` |
| **Applies to** | fo:table |
| **Inherited** | No |
| **Conformance** | Extended |

<!-- Source: https://www.w3.org/TR/xslfo20/#table-omit-header-at-break -->

The "table-omit-header-at-break" property specifies if a table whose first area is not at the beginning of an area produced by the table should start with the content of the `fo:table-header` formatting object or not.

- **true** -- The header should be omitted.
- **false** -- The header should not be omitted.

### header-position

| Field | Value |
|---|---|
| **Values** | `page \| column \| region` |
| **Initial** | `page` |
| **Applies to** | fo:conditional-table-header-reference |
| **Inherited** | No |
| **Conformance** | Extended |

<!-- Source: https://www.w3.org/TR/xslfo20/#header-position -->

Controls when a conditional table header reference is used.

- **page** -- The `fo:conditional-table-header-reference` element is used when the formatter detects this is the first use on a new page.
- **column** -- The `fo:conditional-table-header-reference` element is used when the formatter detects this is the first use in a new column.
- **region** -- The `fo:conditional-table-header-reference` element is used when the formatter detects this is the first use in a new region.

If the `header-position` property is not specified, then the `fo:conditional-table-header-reference` is the default reference for the table.

### footer-position

| Field | Value |
|---|---|
| **Values** | `page \| column \| region` |
| **Initial** | `page` |
| **Applies to** | fo:conditional-table-footer-reference |
| **Inherited** | No |
| **Conformance** | Extended |

<!-- Source: https://www.w3.org/TR/xslfo20/#footer-position -->

Controls when a conditional table footer reference is used.

- **page** -- The `fo:conditional-table-footer-reference` element is used when the formatter detects this is the first use on a new page.
- **column** -- The `fo:conditional-table-footer-reference` element is used when the formatter detects this is the first use in a new column.
- **region** -- The `fo:conditional-table-footer-reference` element is used when the formatter detects this is the first use in a new region.

If the `footer-position` property is not specified, then the `fo:conditional-table-footer-reference` is the default reference for the table.

### table-overflow

| Field | Value |
|---|---|
| **Values** | `paginate-column-first \| paginate-row-first \| auto` |
| **Initial** | `auto` |
| **Applies to** | fo:table |
| **Inherited** | No |
| **Conformance** | Extended |

<!-- Source: https://www.w3.org/TR/xslfo20/#table-overflow -->

The `table-overflow` property specifies the method for paginating a large table into multiple pages.

- **paginate-column-first** -- Columns should be paginated before rows.
- **paginate-row-first** -- Rows should be paginated before columns.
- **auto** -- The User Agent determines the pagination method.

### border-break

| Field | Value |
|---|---|
| **Values** | `auto \| hidden \| extend` |
| **Initial** | `auto` |
| **Applies to** | fo:table, fo:table-cell |
| **Inherited** | No |
| **Conformance** | Extended |

<!-- Source: https://www.w3.org/TR/xslfo20/#border-break -->

The `border-break` property specifies how the potential break across boundaries is to be handled by the formatter.

- **auto** -- The formatter decides what to do.
- **hidden** -- The border breaks are hidden.
- **extend** -- The borders are to be extended.

### border-before-break

| Field | Value |
|---|---|
| **Values** | `auto \| hidden \| extend` |
| **Initial** | `auto` |
| **Applies to** | fo:table, fo:table-cell |
| **Inherited** | No |
| **Conformance** | Extended |

<!-- Source: https://www.w3.org/TR/xslfo20/#border-before-break -->

The `border-before-break` property specifies how the potential break across before direction boundary is to be handled by the formatter.

- **auto** -- The formatter decides what to do.
- **hidden** -- The border breaks are hidden.
- **extend** -- The borders are to be extended.

### border-after-break

| Field | Value |
|---|---|
| **Values** | `auto \| hidden \| extend` |
| **Initial** | `auto` |
| **Applies to** | fo:table, fo:table-cell |
| **Inherited** | No |
| **Conformance** | Extended |

<!-- Source: https://www.w3.org/TR/xslfo20/#border-after-break -->

The `border-after-break` property specifies how the potential break across the after boundary is to be handled by the formatter.

- **auto** -- The formatter decides what to do.
- **hidden** -- The border breaks are hidden.
- **extend** -- The borders are to be extended.

### border-start-break

| Field | Value |
|---|---|
| **Values** | `auto \| hidden \| extend` |
| **Initial** | `auto` |
| **Applies to** | fo:table, fo:table-cell |
| **Inherited** | No |
| **Conformance** | Extended |

<!-- Source: https://www.w3.org/TR/xslfo20/#border-start-break -->

The `border-start-break` property specifies how the potential break across the start boundary is to be handled by the formatter.

- **auto** -- The formatter decides what to do.
- **hidden** -- The border breaks are hidden.
- **extend** -- The borders are to be extended.

### border-end-break

| Field | Value |
|---|---|
| **Values** | `auto \| hidden \| extend` |
| **Initial** | `auto` |
| **Applies to** | fo:table, fo:table-cell |
| **Inherited** | No |
| **Conformance** | Extended |

<!-- Source: https://www.w3.org/TR/xslfo20/#border-end-break -->

The `border-end-break` property specifies how the potential break across the end boundary is to be handled by the formatter.

- **auto** -- The formatter decides what to do.
- **hidden** -- The border breaks are hidden.
- **extend** -- The borders are to be extended.

## Pagination and Layout Properties Used with Tables

The following properties from the Pagination and Layout Properties group are commonly used in table contexts:

### column-count

| Field | Value |
|---|---|
| **Values** | `<number> \| inherit` |
| **Initial** | `1` |
| **Applies to** | fo:region-body |
| **Inherited** | No |
| **Conformance** | Extended |

<!-- Source: https://www.w3.org/TR/xslfo20/#column-count -->

Specifies the number of columns in the region. A positive integer. If a non-positive or non-integer value is provided, the value will be rounded to the nearest integer value greater than or equal to 1. A value of 1 indicates that this is not a multi-column region.

### column-gap

| Field | Value |
|---|---|
| **Values** | `<length> \| <percentage> \| inherit` |
| **Initial** | `12.0pt` |
| **Applies to** | fo:region-body |
| **Inherited** | No |
| **Conformance** | Extended |

<!-- Source: https://www.w3.org/TR/xslfo20/#column-gap -->

Specifies the width of the separation between adjacent columns in a multi-column region. This is an unsigned length. If a negative value has been specified a value of 0pt will be used. Percentages refer to the inline-progression-dimension of the content-rectangle of the region.

## Code Samples

No code samples in spec for this property group.

## See Also

- [fo-table](fo-table.md) -- the table formatting object
- [fo-table-column](fo-table-column.md) -- column specifications
- [fo-table-cell](fo-table-cell.md) -- individual table cells
- [fo-table-row](fo-table-row.md) -- table rows
- [fo-table-body](fo-table-body.md) -- table body group
- [fo-table-header](fo-table-header.md) -- repeating table header
- [fo-table-footer](fo-table-footer.md) -- repeating table footer
- [fo-table-and-caption](fo-table-and-caption.md) -- table with caption
