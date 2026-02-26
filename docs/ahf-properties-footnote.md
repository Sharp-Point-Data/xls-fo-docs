# Antenna House Extension Properties: Footnote Extension Properties

<!-- Source: XSL-FO-Reference-74-MID.pdf pp.312–476 -->

Properties controlling footnote numbering, positioning, alignment, stacking behavior, and maximum height.

## axf:footnote-align

Specifies the alignment of the footnotes. Specifies the method of arrangement of footnotes or sidenotes.

When it is sidenotes (footnote arrangement into `<fo:region-start>` or `<fo:region-end>` is specified by `axf:footnote-position`), it's possible to specify whether it is arranged automatically, or it is arranged near by the before side, or it is arranged near by the after side.

Values have the following meanings:

- `auto`: Footnotes are placed automatically. Footnotes are the usual arrangement. When the text is one column, sidenotes are arranged with an anchor position, and in the case of two or more columns, sidenotes are arranged near by the before side.
- `before`: Sidenotes are arranged near by the before side. In the case of usual footnotes that are not sidenotes, footnotes are arranged immediately after the text in a page.
- `after`: Sidenotes are arranged near by the after side. In the case of usual footnotes that are not sidenotes, footnotes are arranged at the last of a page.

| Attribute | Value |
|---|---|
| **Applies to** | `<fo:region-body>`, `<fo:footnote>` |
| **Values** | `auto \| before \| after` |
| **Initial** | `auto` |
| **Inherited** | no |

## axf:footnote-keep

Specifies whether to arrange a footnote and an anchor in the same page.

Values have the following meanings:

- `auto`: When a footnote does not fit within the column, it is sent to the next page or the next column.
- `always`: When a footnote does not fit within the column, the line of the anchor and the subsequent lines are sent to the following page, and a footnote and an anchor are arranged in the same page. When `axf:footnote-position="column"` is specified, a footnote and an anchor are arranged in the same column. A footnote and an anchor may not be arranged in the same page when the cell containing the anchor is large or at the bottom of the page.
- `none`: When a footnote does not fit within the column, the line of the anchor and the subsequent lines are sent to the next page, and attempts to fit the footnote itself within the page. (New in V7.1)

| Attribute | Value |
|---|---|
| **Applies to** | `<fo:region-body>`, `<fo:footnote>` |
| **Values** | `auto \| always \| none` |
| **Initial** | `auto` |
| **Inherited** | no |

## axf:footnote-max-height

Specifies the maximum height of footnote. The behavior when `auto` is specified depends on the value of `auto-break-footnote` in the Option Setting File.

- When `axf:footnote-max-height="auto"` and `auto-break-footnote="false"` are specified: Page (column) break did not occur within `<fo:footnote-body>`. In case a footnote is big and exceeds the page height, an overflow occurs. However, only in case a footnote is small, is it possible to format without breaking a footnote.
- When `axf:footnote-max-height="auto"` and `auto-break-footnote="true"` are specified: It is considered that the page height is specified to `axf:footnote-max-height` and page break (column break) occurs within `<fo:footnote-body>`.
- When `axf:footnote-max-height="<length>"` or `"<percentage>"` is specified: The value must be positive. `auto-break-footnote` is not referred to. At this time, page (column) break may occur within `<fo:footnote-body>`. The footnote will be put after an anchor position as much as possible and the remaining part will be split and sent to the next page (column). Note that `axf:footnote-max-height` is invalid for pages without text.

| Attribute | Value |
|---|---|
| **Applies to** | `<fo:region-body>` |
| **Values** | `auto \| <length> \| <percentage>` |
| **Initial** | `auto` |
| **Inherited** | no |

## axf:footnote-number-format

Specifies the format of footnote number. Adopted as a format of `<axf:footnote-number>`. It can be specified in the same way as the `format` property.

| Attribute | Value |
|---|---|
| **Applies to** | `<fo:page-sequence>` |
| **Values** | `<string>` |
| **Initial** | `1` |
| **Inherited** | no |

## axf:footnote-number-initial

Specifies the initial footnote number.

Values have the following meanings:

- `auto`: Succeeded from the before existing `<fo:page-sequence>` without initializing a footnote number. When `<fo:page-sequence>` does not exist before, it is set to 1.
- `<number>`: Initializes the footnote number with the specified value. The value must be greater than or equal to 1. Actual initialization takes place at the time when `axf:footnote-number-reset` is specified.

| Attribute | Value |
|---|---|
| **Applies to** | `<fo:page-sequence>` |
| **Values** | `auto \| <number>` |
| **Initial** | `auto` |
| **Inherited** | no |

## axf:footnote-number-reset

Resets the footnote numbering. A footnote number is reset by the value specified by `axf:footnote-number-initial`.

Values have the following meanings:

- `auto`: Succeeded from the before existing `<fo:page-sequence>`. When `<fo:page-sequence>` does not exist before, it is set to `none`.
- `none`: Does not reset the footnote number.
- `page`: Resets the footnote number when a page breaks.
- `odd-page`: Resets the footnote number when an odd page breaks.
- `even-page`: Resets the footnote number when an even page breaks.
- `column`: Resets the footnote number when a column breaks.

| Attribute | Value |
|---|---|
| **Applies to** | `<fo:page-sequence>` |
| **Values** | `auto \| none \| page \| odd-page \| even-page \| column` |
| **Initial** | `auto` |
| **Inherited** | no |

## axf:footnote-position

Specifies the location to place the footnote.

Values have the following meanings:

- `page`: Footnotes are placed on the after side of each page in `<fo:region-body>`. This is the standard layout of XSL specification.
- `odd-page`: Footnotes are placed on the after side of each odd page in `<fo:region-body>`. This is the standard layout of sidenotes in vertical writing. (On the outside in odd page.)
- `even-page`: Footnotes are placed on the after side of each even page in `<fo:region-body>`.
- `start`: Footnotes are placed on each page in `<fo:region-start>`. Headnotes in vertical writing. Sidenotes on the left side in horizontal writing.
- `end`: Footnotes are placed on each page in `<fo:region-end>`. Footnotes in vertical writing. Sidenotes on the right side in horizontal writing.
- `inside`: Footnotes are placed at each even page in `<fo:region-end>` and each odd page in `<fo:region-start>`. Sidenotes on the inside in horizontal writing.
- `outside`: Footnotes are placed on each even page in `<fo:region-start>` and each odd page in `<fo:region-end>`. This is a standard sidenotes in horizontal writing. (On the outside of both right and left pages.)
- `column`: Footnotes are placed on the after side of each column. This is a standard footnote in horizontal writing. Same as `page` if the document is non multi-columns.
- `start-column`: Footnotes are placed on the after side of the first column. Same as `start` if the document is non multi-columns.
- `end-column`: Footnotes are placed on the after side of the end column. Same as `end` if the document is non multi-columns.
- `inside-column`: Footnotes are placed in the same way as `end-column` at even page and in the same way as `start-column` at odd page. Footnotes are put together on the inside column in horizontal writing.
- `outside-column`: Footnotes are placed in the same way as `start-column` at even page and in the same way as `end-column` at odd page. Footnotes are put together on the outside column in horizontal writing.

It is possible to arrange footnotes inside the `<fo:region-start>` or the `<fo:region-end>` (these notes are called sidenotes). Besides specifying them to `<fo:region-body>`, it is also effective to specify to individual `<fo:footnote>`. It is possible to make several types of notes intermingled by this extension.

There are following restrictions for sidenotes:

- The sidenotes which run over from the specified area will overflow.
- The `xsl-footnote-separator` is not effective.

`start-column`, `end-column`, `inside-column` and `outside-column` have the following restrictions:

- It is not possible to specify these values to `<fo:footnote>`. It is only available to specify them to `<fo:region-body>`.
- When you specify these values to `<fo:region-body>`, `column` cannot be specified to `<fo:footnote>`.
- These values cannot be used with the forcible column break such as `break-before="column"`, etc. These values cannot be used for a large volume of footnotes.

`odd-page` and `even-page` have the following restrictions:

- It is not possible to specify these values to `<fo:footnote>`. It is only available to specify them to `<fo:region-body>`.

| Attribute | Value |
|---|---|
| **Applies to** | `<fo:region-body>`, `<fo:footnote>` |
| **Values** | `page \| odd-page \| even-page \| start \| end \| inside \| outside \| column \| start-column \| end-column \| inside-column \| outside-column` |
| **Initial** | `page` |
| **Inherited** | no |

## axf:footnote-stacking

Specifies the method to layout the footnote.

Values have the following meanings:

- `block`: Arranges the footnotes in the block progression direction.
- `inline`: Arranges the footnotes in the inline progression direction.

| Attribute | Value |
|---|---|
| **Applies to** | `<fo:region-body>`, `<fo:footnote>` |
| **Values** | `block \| inline` |
| **Initial** | `block` |
| **Inherited** | no |
