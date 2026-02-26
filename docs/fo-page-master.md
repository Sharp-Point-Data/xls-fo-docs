# fo:page-master

## Summary

The `fo:page-master` is used in the generation of pages and specifies the geometry of the page. The page may be subdivided into an arbitrary number of regions, each called an `fo:region`. The region has similar behaviour to a region-body, meaning that an `fo:page-master` is formed by an arbitrary number of body-like regions. Regions are positioned absolutely into the page and have a concept of z-index.

This formatting object provides more flexibility than `fo:simple-page-master` by allowing an arbitrary number of regions with absolute positioning and z-index layering, rather than being limited to the fixed five-region model (body, before, after, start, end).

## Areas

The `fo:page-master` formatting object generates no area directly. It is used in the generation of pages by an `fo:page-sequence`.

When the `fo:page-master` is used to generate a page, a viewport/reference pair is generated, consisting of a page-viewport-area and a page-reference-area. The page-viewport-area represents the physical bounds of the output medium. The page-reference-area represents the portion of the page on which content is intended to appear; that is, the area inside the page margins.

In addition, when the `fo:page-master` is used to generate a page, viewport/reference pairs that correspond to the regions that are the children of the `fo:page-master` are also generated.

## Trait Derivation

Same as `fo:simple-page-master`.

## Constraints

Same as `fo:simple-page-master`.

## Content Model

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_page-master -->
```xml
(region)+
```

The `fo:page-master` must contain one or more `fo:region` children. Unlike `fo:simple-page-master`, which is limited to the five predefined region types, `fo:page-master` can contain any number of generic `fo:region` elements.

## Properties

| Property | Type | Initial Value | Inherited | Conformance Level |
|---|---|---|---|---|
| margin-top | `<length> \| <percentage> \| auto \| inherit` | 0pt | no | Extended |
| margin-bottom | `<length> \| <percentage> \| auto \| inherit` | 0pt | no | Extended |
| margin-left | `<length> \| <percentage> \| auto \| inherit` | 0pt | no | Extended |
| margin-right | `<length> \| <percentage> \| auto \| inherit` | 0pt | no | Extended |
| space-before | `<space> \| inherit` | 0pt | no | Extended |
| space-after | `<space> \| inherit` | 0pt | no | Extended |
| start-indent | `<length> \| <percentage> \| inherit` | 0pt | yes | Extended |
| end-indent | `<length> \| <percentage> \| inherit` | 0pt | yes | Extended |
| bleed-box | `x1 y1 x2 y2` | 0 0 0 0 | no | Extended |
| master-name | `<name>` | an empty name | no, a value is required | Extended |
| page-height | `auto \| indefinite \| <length> \| inherit` | auto | no | Extended |
| page-width | `auto \| indefinite \| <length> \| inherit` | auto | no | Extended |
| reference-orientation | `0 \| 90 \| 180 \| 270 \| -90 \| -180 \| -270 \| inherit` | 0 | no | Extended |
| trim-box | `x1 y1 x2 y2` | 0 0 0 0 | no | Extended |
| writing-mode | `lr-tb \| rl-tb \| tb-rl \| tb-lr \| ... \| inherit` | lr-tb | no | Extended |

The "Common Margin Properties-Block" group includes: `margin-top`, `margin-bottom`, `margin-left`, `margin-right`, `space-before`, `space-after`, `start-indent`, and `end-indent`.

### Key Property Details

- **master-name**: Provides an identifying name for this page-master, unique within the `fo:layout-master-set`.
- **page-height / page-width**: Specify the page dimensions. Same semantics as for `fo:simple-page-master`.
- **bleed-box**: Defines the size and position of a notional rectangle around the page in which ink might appear. The primary purpose is so that when a trimming machine cuts the printed page to size, graphics or other content can extend to the edge of the page. The values are offsets from the page-reference-area origin (x1, y1) and from the diagonally opposite corner (x2, y2).
- **trim-box**: Defines the size and position of the rectangle to which the page will be trimmed. The trim box is usually inside the bleed-box.
- **reference-orientation / writing-mode**: Same semantics as for `fo:simple-page-master`.

## Usage Notes

The `fo:page-master` provides an advanced page layout model where regions can be positioned arbitrarily on the page rather than being constrained to the before/after/start/end/body positions of `fo:simple-page-master`. Regions within `fo:page-master` are positioned absolutely and support z-index for layering.

The z-index property controls the stacking order of overlapping regions. When regions overlap:
- A region with a higher z-index appears on top of regions with lower z-index values.
- Text in lower-z-index regions is pushed away from higher-z-index regions (content avoidance).
- If regions have the same z-index, text may overlap.

The `bleed-box` and `trim-box` properties are specific to `fo:page-master` and support professional print production workflows. The bleed box defines the area where printing may extend beyond the final page edge, while the trim box defines where the page will be cut.

## Code Samples

No code samples in spec for this formatting object. The spec section contains only the content model declaration shown above.

## See Also

- [fo:layout-master-set](fo-layout-master-set.md) — parent container
- [fo:simple-page-master](fo-simple-page-master.md) — simpler page-master with fixed five-region model
- [fo:region-body](fo-region-body.md) — used with fo:simple-page-master
- [fo:page-sequence](fo-page-sequence.md) — references this master via master-reference
- [fo:page-sequence-master](fo-page-sequence-master.md) — orchestrates page-master selection
