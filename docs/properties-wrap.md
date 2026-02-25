# Common Wrap Properties

<!-- Source: https://www.w3.org/TR/xslfo20/#common-wrap-properties -->

## Overview

The common wrap properties are used to express the runaround interaction between regions. Regions interact based on their z-index values. Regions with higher z-index are considered overlapping regions with lower z-index.

These properties control how text and other inline content in one region flows around (or through, or skips) the area occupied by an overlapping region. The `wrap` property determines the overall wrapping strategy, `wrap-path` controls how the wrap contour is determined, and `wrap-side` specifies which side(s) of the intrusion allow text flow.

These properties apply to `fo:region` formatting objects.

## Properties

### wrap

| Field | Value |
|---|---|
| **Values** | `skip \| path \| none` |
| **Initial** | `skip` |
| **Applies to** | fo:region |
| **Inherited** | No |
| **Percentages** | N/A |

Use the "wrap" property to specify flow run-around.

Values have the following meanings:

- **skip** -- This is the default behavior. The content in the flow will skip the entire intrusion area continuing from the first available un-intruded allocation area.
- **path** -- The runaround contour is determined following the wrap-path property strategy.
- **none** -- No runaround is applied. If regions are overlapping their content will overlap.

### wrap-path

| Field | Value |
|---|---|
| **Values** | `shape \| bounding-box \| auto` |
| **Initial** | `shape` |
| **Applies to** | fo:region |
| **Inherited** | No |
| **Percentages** | N/A |

When two or more shaped areas interact, the "wrap-path" property determines how text and other inline objects in one area flow around the shape of the other area.

Values have the following meanings:

- **shape** -- This is the default behavior. The path is custom and it is indicated using the shape-path-specifier within the shape-assignment for the region. If there is no shape-map associated with the intruded region the behaviour is defaulted to bounding-box.
- **bounding-box** -- The path is determined by the bounding-box of the overlapping region.
- **auto** -- The path is inferred as follows: clip-path embedded in the content of the intruding region; path detection through image color threshold or alpha-channel (transparency) in the content in the intruding region. If neither of these are available, or the implementation does not support them, the path is defaulted to the bounding-box.

### wrap-side

| Field | Value |
|---|---|
| **Values** | `all \| start \| end \| inside \| outside \| largest \| smallest` |
| **Initial** | `shape` |
| **Applies to** | fo:region |
| **Inherited** | No |
| **Percentages** | N/A |

The "wrap-side" property indicates what strategy should be applied for the runaround.

Values have the following meanings:

- **all** -- This is the default behavior. Runaround is performed, if possible, on both sides of the intruding area.
- **start** -- The run-around is performed only in the start side of the intruding area.
- **end** -- The runaround is performed only in the end side of the intruding area.
- **inside** -- The runaround is performed only in the inside of the intruded area. The inside is the side nearer to the spread "spine". The spread spine is considered the contact line between the two pages forming the spread. If the region is not part of a spread the inside value is interpreted as nearest to the binding edge, as for text-align.
- **outside** -- The runaround is performed only in the outside of the intruded area. The outside is determined as elsewhere, e.g. text-align.
- **largest** -- The runaround is performed only in the largest area available as result of the intrusion.
- **smallest** -- The runaround is performed only in the smallest area available as result of the intrusion.

## Code Samples

No code samples in spec for this property group.

## See Also

- [fo:region](fo-region.md) -- The region FO to which these properties apply
- [fo:region-body](fo-region-body.md) -- The body region that commonly participates in wrap interactions
