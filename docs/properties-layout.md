# Layout-related Properties

## Overview

<!-- Source: https://www.w3.org/TR/xslfo20/#layout-related-properties -->

The layout-related properties control clipping, overflow behavior, reference orientation, column spanning, visibility, and stacking order. These properties are not common to all formatting objects and apply primarily to formatting objects that generate reference areas, viewports, or absolutely positioned content.

## Properties

### clip

| Field | Value |
|---|---|
| **Values** | `<shape> \| auto \| inherit` |
| **Initial** | `auto` |
| **Applies to** | formatting objects with overflow other than "visible" |
| **Inherited** | No |
| **Percentages** | N/A |
| **Media** | visual |

<!-- Source: https://www.w3.org/TR/xslfo20/#clip -->

The "clip" property applies to elements that have an "overflow" property with a value other than "visible".

Values have the following meanings:

- **auto** -- The clipping region has the same size and location as the element's box(es).
- **\<shape\>** -- In CSS2, the only valid \<shape\> value is: `rect(<top>, <right>, <bottom>, <left>)` where \<top\>, \<bottom\>, \<right\>, and \<left\> specify offsets from the respective sides of the box. \<top\>, \<right\>, \<bottom\>, and \<left\> may either have a \<length\> value or "auto". Negative lengths are permitted. The value "auto" means that a given edge of the clipping region will be the same as the edge of the element's generated box (i.e., "auto" means the same as "0".)

When coordinates are rounded to pixel coordinates, care should be taken that no pixels remain visible when \<left\> + \<right\> is equal to the element's width (or \<top\> + \<bottom\> equals the element's height), and conversely that no pixels remain hidden when these values are 0.

The element's ancestors may also have clipping regions (in case their "overflow" property is not "visible"); what is rendered is the intersection of the various clipping regions.

If the clipping region exceeds the bounds of the UA's document window, content may be clipped to that window by the native operating environment.

### overflow

| Field | Value |
|---|---|
| **Values** | `visible \| hidden \| scroll \| error-if-overflow \| repeat \| auto \| inherit` |
| **Initial** | `auto` |
| **Applies to** | formatting objects that generate viewport/reference pairs |
| **Inherited** | No |
| **Percentages** | N/A |
| **Media** | visual |

<!-- Source: https://www.w3.org/TR/xslfo20/#overflow -->

This property specifies whether the content of a block-level element is clipped when it overflows the element's box (which is acting as a containing block for the content).

Values have the following meanings:

- **visible** -- This value indicates that content is not clipped, i.e., it may be rendered outside the block box.
- **hidden** -- This value indicates that the content is clipped and that no scrolling mechanism should be provided to view the content outside the clipping region; users will not have access to clipped content. The size and shape of the clipping region is specified by the "clip" property.
- **scroll** -- This value indicates that the content is clipped and that if the user agent uses a scrolling mechanism that is visible on the screen (such as a scroll bar or a panner), that mechanism should be displayed for a box whether or not any of its content is clipped. This avoids any problem with scrollbars appearing and disappearing in a dynamic environment. When this value is specified and the target medium is "print", overflowing content should be printed.
- **auto** -- The behavior of the "auto" value is user agent dependent, but should cause a scrolling mechanism to be provided for overflowing boxes.
- **error-if-overflow** -- This value implies the same semantics as the value "hidden" with the additional semantic that an error shall be indicated; implementations may recover by clipping the region.
- **repeat** -- On a formatting object which generates and returns normal viewport/reference pairs, this value specifies that additional viewport/reference pairs are to be generated so that the reference-area component of each pair is no larger than its parent viewport-area. On other formatting objects (including formatting objects whose absolute-position trait is "absolute" or "fixed"), it acts as if an overflow value of "auto" were specified.

Even if "overflow" is set to "visible", content may be clipped to a UA's document window by the native operating environment.

For print media, implementations must support "auto" and "visible", as defined in this Recommendation. Other values may be treated as if "auto" had been specified.

### reference-orientation

| Field | Value |
|---|---|
| **Values** | `0 \| 90 \| 180 \| 270 \| -90 \| -180 \| -270 \| inherit` |
| **Initial** | `0` |
| **Applies to** | formatting objects that establish a reference-area |
| **Inherited** | No |
| **Percentages** | N/A |
| **Media** | visual |

<!-- Source: https://www.w3.org/TR/xslfo20/#reference-orientation -->

The reference-orientation specifies the direction for "top" for the content-rectangle of the reference-area. This is used as the reference for deriving directions, such as the block-progression-direction, inline-progression-direction, etc. as specified by the "writing-mode" and "direction" properties, and the orientation, placement, and tiling of the background.

Values have the following meanings:

- **0** -- The reference-orientation of this reference-area has the same reference-orientation as the containing reference-area.
- **90** -- The reference-orientation of this reference-area is rotated 90 degrees counter-clockwise from the reference-orientation of the containing reference-area.
- **180** -- The reference-orientation of this reference-area is rotated 180 degrees counter-clockwise from the reference-orientation of the containing reference-area.
- **270** -- The reference-orientation of this reference-area is rotated 270 degrees counter-clockwise from the reference-orientation of the containing reference-area.
- **-90** -- Equivalent to specifying "270".
- **-180** -- Equivalent to specifying "180".
- **-270** -- Equivalent to specifying "90".

The "reference-orientation" property is applied only on formatting objects that establish a reference-area. Each value of "reference-orientation" sets the absolute direction for "top", "left", "bottom", and "right"; which is used by "writing-mode", "direction", and all positioning operations that are referenced to the reference-area or are nested within it.

The reference-orientation trait on an area is indirectly derived from the "reference-orientation" property on the formatting object that generates the area or the formatting object ancestors of that formatting object.

### span

| Field | Value |
|---|---|
| **Values** | `none \| all \| inherit` |
| **Initial** | `none` |
| **Applies to** | block-level formatting objects that are direct children of fo:flow |
| **Inherited** | No |
| **Percentages** | N/A |
| **Media** | visual |

<!-- Source: https://www.w3.org/TR/xslfo20/#span -->

Specifies if a block-level object should be placed in the current column or should span all columns of a multi-column region.

Values have the following meanings:

- **none** -- This object does not span multiple columns.
- **all** -- The areas resulting from this flow object shall span all the columns of a multi-column region.

This only has effect on areas returned by a flow; e.g. block-areas generated by fo:block children of an fo:flow. Children and further descendants of these areas take on the spanning characteristic of their parent.

### visibility

| Field | Value |
|---|---|
| **Values** | `visible \| hidden \| collapse \| inherit` |
| **Initial** | `visible` |
| **Applies to** | all formatting objects |
| **Inherited** | Yes |
| **Percentages** | N/A |
| **Media** | visual |

<!-- Source: https://www.w3.org/TR/xslfo20/#visibility -->

The "visibility" property specifies whether the boxes generated by an element are rendered. Invisible boxes still affect layout (set the "display" property to "none" to suppress box generation altogether).

Values have the following meanings:

- **visible** -- The generated box is visible.
- **hidden** -- The generated box is invisible (fully transparent), but still affects layout.
- **collapse** -- Please consult the section on dynamic row and column effects in tables. If used on elements other than rows or columns, "collapse" has the same meaning as "hidden".

This property may be used in conjunction with scripts to create dynamic effects.

XSL modification: Changed initial value to "visible" (it is "inherit" in CSS) and made it an inherited property.

### z-index

| Field | Value |
|---|---|
| **Values** | `auto \| <integer> \| inherit` |
| **Initial** | `auto` |
| **Applies to** | absolutely positioned formatting objects |
| **Inherited** | No |
| **Percentages** | N/A |
| **Media** | visual |

<!-- Source: https://www.w3.org/TR/xslfo20/#z-index -->

For a positioned box, the "z-index" property specifies:

1. The stack level of the box in the current stacking context.
2. Whether the box establishes a local stacking context.

Values have the following meanings:

- **auto** -- The stack level of the generated box in the current stacking context is the same as its parent's box. The box does not establish a new local stacking context.
- **\<integer\>** -- This integer is the stack level of the generated box in the current stacking context. The box also establishes a local stacking context in which its stack level is "0".

The default behavior of a box is to allow boxes behind it to be visible through transparent areas in its content. Each box transparently overlays the boxes below it. This behavior can be overridden by using one of the existing background properties.

## Code Samples

No code samples in spec for this property group.

## See Also

- [fo-block-container](fo-block-container.md) -- Uses reference-orientation and overflow
- [fo-region-body](fo-region-body.md) -- Uses overflow and reference-orientation
- [fo-block](fo-block.md) -- Uses span property for multi-column layouts
- [fo-inline-container](fo-inline-container.md) -- Uses clip and overflow
