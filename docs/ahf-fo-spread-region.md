# axf:spread-region

## Summary

This object sets the spanning area of a double page (two facing pages) within a double page template (`axf:spread-page-master`). The spread region defines an area that spans across both the left and right pages of a spread, allowing content to flow continuously across the page boundary.

## Properties

| Property | Description |
|----------|-------------|
| `absolute-position` | Absolute position of the spread region |
| `background-attachment` | Background attachment mode |
| `background-color` | Background color of the spread region |
| `background-image` | Background image for the spread region |
| `background-repeat` | Background image repeat mode |
| `background-position-horizontal` | Horizontal position of the background image |
| `background-position-vertical` | Vertical position of the background image |
| `border-before-color` | Border color on the before edge |
| `border-before-style` | Border style on the before edge |
| `border-before-width` | Border width on the before edge |
| `border-after-color` | Border color on the after edge |
| `border-after-style` | Border style on the after edge |
| `border-after-width` | Border width on the after edge |
| `border-start-color` | Border color on the start edge |
| `border-start-style` | Border style on the start edge |
| `border-start-width` | Border width on the start edge |
| `border-end-color` | Border color on the end edge |
| `border-end-style` | Border style on the end edge |
| `border-end-width` | Border width on the end edge |
| `border-top-color` | Border color on the top edge |
| `border-top-style` | Border style on the top edge |
| `border-top-width` | Border width on the top edge |
| `border-bottom-color` | Border color on the bottom edge |
| `border-bottom-style` | Border style on the bottom edge |
| `border-bottom-width` | Border width on the bottom edge |
| `border-left-color` | Border color on the left edge |
| `border-left-style` | Border style on the left edge |
| `border-left-width` | Border width on the left edge |
| `border-right-color` | Border color on the right edge |
| `border-right-style` | Border style on the right edge |
| `border-right-width` | Border width on the right edge |
| `bottom` | Bottom offset for absolute positioning |
| `end-indent` | End indent of the region |
| `height` | Height of the spread region |
| `left` | Left offset for absolute positioning |
| `margin-top` | Top margin |
| `margin-bottom` | Bottom margin |
| `margin-left` | Left margin |
| `margin-right` | Right margin |
| `overflow` | Overflow behavior for the region |
| `padding-before` | Padding on the before edge |
| `padding-after` | Padding on the after edge |
| `padding-start` | Padding on the start edge |
| `padding-end` | Padding on the end edge |
| `padding-top` | Top padding |
| `padding-bottom` | Bottom padding |
| `padding-left` | Left padding |
| `padding-right` | Right padding |
| `region-name` | Name used to target this region with `fo:flow` |
| `reference-orientation` | Reference orientation for the region |
| `right` | Right offset for absolute positioning |
| `space-before` | Space before the region |
| `space-after` | Space after the region |
| `start-indent` | Start indent of the region |
| `top` | Top offset for absolute positioning |
| `width` | Width of the spread region |

For `writing-mode`, see the notes in the description of this property.

## Parent Objects

- `axf:spread-page-master`

## Child Objects

None.

## Code Samples

No separate code sample is provided in the Antenna House reference for this formatting object. See `axf:spread-page-master` for a complete usage example that includes `axf:spread-region`.

The key usage from that example is:

<!-- Source: XSL-FO-Reference-74-MID.pdf pp.307-310 -->
```xml
<axf:spread-page-master master-name="Double-pages"
left-page-master-reference="Page-left"
right-page-master-reference="Page-right">
<axf:spread-region region-name="spread" margin-top="36pt" margin-left="36pt"
margin-right="36pt" margin-bottom="48mm"/>
</axf:spread-page-master>
```

The `region-name` attribute (here `"spread"`) is used as the `flow-name` on an `fo:flow` to direct content into the spread region:

```xml
<fo:flow flow-name="spread">
<fo:block text-align="center" font-weight="bold">
This is a Spanned Title
</fo:block>
</fo:flow>
```
