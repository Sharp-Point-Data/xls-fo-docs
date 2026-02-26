# fo:inline-container

## Summary

The fo:inline-container flow object is used to generate an inline reference-area, typically containing text blocks with a different writing-mode. It generates one or more viewport/reference pairs. The use of this flow object is not required for bi-directional text; in that case the Unicode BIDI algorithm and the fo:bidi-override are sufficient.

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_inline-container -->

## Content Model

`(%block;)+`

In addition, this formatting object may have a sequence of zero or more fo:marker elements as its initial children.

## Properties

| Property | Inherited | Conformance Level |
|----------|-----------|-------------------|
| Common Border, Padding, and Background Properties | No | Basic |
| Common Margin Properties-Inline | No | Basic |
| Common Relative Position Properties | No | Extended |
| alignment-adjust | No | Extended |
| alignment-baseline | No | Extended |
| baseline-shift | No | Extended |
| block-progression-dimension | No | Extended |
| clip | No | Extended |
| display-align | No | Extended |
| dominant-baseline | No | Extended |
| height | No | Extended |
| id | No | Basic |
| index-class | No | Extended |
| index-key | No | Extended |
| inline-progression-dimension | No | Extended |
| keep-together | Yes | Extended |
| keep-with-next | No | Extended |
| keep-with-previous | No | Extended |
| line-height | Yes | Basic |
| overflow | No | Extended |
| reference-orientation | No | Extended |
| width | No | Extended |
| writing-mode | No | Basic |

## Usage Notes

- fo:inline-container is used when you need an inline-level reference-area with a different writing-mode or reference-orientation than the surrounding context.
- All generated viewport-areas are subject to the constraints given by the block-progression-dimension and inline-progression-dimension traits.
- If the absolute-position trait is "auto", the areas have an area-class of "xsl-normal". If absolute-position is "absolute" or "fixed", there is one viewport/reference pair with an area-class of "xsl-absolute" or "xsl-fixed" respectively.
- The reference-orientation and writing-mode traits of the viewport-area and reference-area come from the fo:inline-container. These determine the orientation of the start-edge, end-edge, before-edge, and after-edge of the content-rectangle of the viewport-area, and of the padding-, border-, and content-rectangles of the reference-area.
- The reference-orientation of the reference-area is set to "0" and is therefore the same as the orientation established by the viewport-area.
- The inline-progression-dimension of the reference-area is the same as that of the viewport-area, and may not be "auto" if the inline-progression-direction is different from that of the parent.
- The block-progression-dimension of the reference-area is not constrained; the reference-area may be larger than the viewport-area, which may cause the overflow property to operate.
- When block-progression-dimension.maximum is other than "auto", overflow processing may apply. The "repeat" value of overflow can be used to generate multiple viewport/reference pairs.
- No area may have more than one normal child area returned by the same fo:inline-container.
- The children of each reference-area must be normal block-areas returned by the children of the fo:inline-container, must be properly stacked, and must be properly ordered.
- Any reference-level-out-of-line areas returned by the children are handled as described in the fo:float specification.
- Baseline table values are calculated based on the relationship between the writing-mode of the fo:inline-container and its parent:
  - **baseline**: If the block-progression-direction is parallel to the parent, the alignment-point is at the position of the dominant-baseline of the first descendant line-area. If there is no such line-area, the alignment-point is at the after-edge of the allocation rectangle. If not parallel, the alignment-point is halfway between the before-edge and after-edge of the content rectangle.
  - **before-edge**: At the before-edge of the allocation rectangle.
  - **text-before-edge**: At the closest position to the before-edge selected from two candidate edges (before/after if parallel; start/end if not).
  - **middle**: Halfway between before-edge and after-edge of the allocation rectangle.
  - **after-edge**: At the after-edge of the allocation rectangle.
  - **text-after-edge**: At the closest position to the after-edge selected from two candidate edges.
  - **ideographic**: 7/10 of the distance from before-edge to after-edge.
  - **alphabetic**: 6/10 of the distance from before-edge to after-edge.
  - **hanging**: 2/10 of the distance from before-edge to after-edge.
  - **mathematical**: 5/10 of the distance from before-edge to after-edge.

## Code Samples

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_inline-container -->
```xml
(%block;)+
```

## See Also

- [fo:inline](fo-inline.md) — for inline-level formatting without a separate reference-area
- [fo:block-container](fo-block-container.md) — the block-level counterpart for generating reference-areas
- [fo:bidi-override](fo-bidi-override.md) — for overriding bidirectional text rendering
