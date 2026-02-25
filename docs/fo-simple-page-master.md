# fo:simple-page-master

## Summary

The `fo:simple-page-master` is used in the generation of pages and specifies the geometry of the page. The page is subdivided into regions: one or more region-body, and up to four other regions: region-before, region-after, region-start, and region-end.

For example, if the `writing-mode` of the `fo:simple-page-master` is "lr-tb", then these regions correspond to the body of a document, the header, the footer, the left sidebar, and the right sidebar.

The simple-page-master is intended for systems that wish to provide a simple page layout facility. Future versions of the Recommendation may support more complex page layouts constructed using the `fo:page-master` formatting object.

## Areas

The `fo:simple-page-master` formatting object generates no area directly. It is used in the generation of pages by an `fo:page-sequence`.

When the `fo:simple-page-master` is used to generate a page, a viewport/reference pair is generated, consisting of a page-viewport-area and a page-reference-area. The page-viewport-area represents the physical bounds of the output medium. The page-reference-area represents the portion of the page on which content is intended to appear; that is, the area inside the page margins.

In addition, viewport/reference pairs that correspond to the regions that are the children of the `fo:simple-page-master` are also generated. The `writing-mode` of the page is used to determine the placement of the five regions on the master.

## Trait Derivation

The `reference-orientation` of the page-reference-area and `writing-mode` of the page-viewport-area are determined by the formatting object that generates the area (i.e., the `fo:page-sequence`). The `writing-mode` of the page-reference-area is set to the same value as that of the page-viewport-area. Reference-orientation does not affect the page-viewport-area and its `reference-orientation` is set to "0". Borders and padding are not allowed with a page-reference-area. The remaining traits on the page-reference-area are set according to the normal rules.

## Constraints

When a page-master is used in the generation of a page, the `block-progression-dimension` and `inline-progression-dimension` of the content-rectangle of the page-viewport-area are determined using the computed values of the `page-height` and `page-width` properties. For sheet media, these properties determine the orientation of the sheet; `page-height` is measured from "top" to "bottom". For display media, the display window is always upright.

The traits derived from the `margin-top`, `margin-bottom`, `margin-left`, and `margin-right` properties are used to indent the page-reference-area content-rectangle from the corresponding edge of the content-rectangle of the page-viewport-area.

The reference points for the page-viewport-area content-rectangle are in terms of "top", "bottom", "left", and "right" rather than "before-edge", "after-edge", "start-edge", and "end-edge" because users see the media relative to its orientation and not relative to the writing-mode currently in use.

### Page Numbering Constraints

The value of the `folio-number` trait on the first page returned by the `fo:page-sequence` is constrained to equal the value of the `initial-page-number` trait. The value on subsequent pages is one greater than the value on the immediately preceding page.

The `format`, `letter-value`, `grouping-separator`, `grouping-size`, `country`, and `language` traits are used to format the number into a string form, as specified in XSLT.

### Region Constraints

If the `block-progression-dimension` of the properly stacked region-reference-area is greater than the `block-progression-dimension` of the region-viewport-area that is its parent, then the constraints depend on values of the `overflow` trait on the region-master and the kind of flows assigned to the region:

- If all flows assigned to the region are `fo:static-content`, there is no constraint on the `block-progression-dimension` of the region-reference-area.
- If all flows are `fo:flow` and `media-usage` is `paginate` or `overflow` is `visible`, `hidden`, or `error-if-overflow`, then the region-reference-area `block-progression-dimension` is constrained to be no greater than that of the region-viewport-area.
- If `media-usage` is `bounded-in-one-dimension` or `unbounded` and `overflow` is `scroll` or `auto`, there is no constraint.

## Content Model

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_simple-page-master -->
```xml
(region-body+,region-before?,region-after?,region-start?,region-end?)
```

The `fo:simple-page-master` must contain one or more `fo:region-body` children, followed by optional `fo:region-before`, `fo:region-after`, `fo:region-start`, and `fo:region-end` children.

## Properties

| Property | Type | Initial Value | Inherited | Conformance Level |
|---|---|---|---|---|
| margin-top | `<length> \| <percentage> \| auto \| inherit` | 0pt | no | Basic |
| margin-bottom | `<length> \| <percentage> \| auto \| inherit` | 0pt | no | Basic |
| margin-left | `<length> \| <percentage> \| auto \| inherit` | 0pt | no | Basic |
| margin-right | `<length> \| <percentage> \| auto \| inherit` | 0pt | no | Basic |
| space-before | `<space> \| inherit` | 0pt | no | Basic |
| space-after | `<space> \| inherit` | 0pt | no | Basic |
| start-indent | `<length> \| <percentage> \| inherit` | 0pt | yes | Basic |
| end-indent | `<length> \| <percentage> \| inherit` | 0pt | yes | Basic |
| master-name | `<name>` | an empty name | no, a value is required | Basic |
| page-height | `auto \| indefinite \| <length> \| inherit` | auto | no | Basic |
| page-width | `auto \| indefinite \| <length> \| inherit` | auto | no | Basic |
| reference-orientation | `0 \| 90 \| 180 \| 270 \| -90 \| -180 \| -270 \| inherit` | 0 | no | Basic |
| writing-mode | `lr-tb \| rl-tb \| tb-rl \| tb-lr \| ... \| inherit` | lr-tb | no | Basic |

The "Common Margin Properties-Block" group includes: `margin-top`, `margin-bottom`, `margin-left`, `margin-right`, `space-before`, `space-after`, `start-indent`, and `end-indent`.

### Key Property Details

- **master-name**: Provides an identifying name for this page-master. This name is referenced by `fo:single-page-master-reference`, `fo:repeatable-page-master-reference`, `fo:conditional-page-master-reference`, and `fo:page-sequence` via `master-reference`. The name must be unique across all page-masters and page-sequence-masters within an `fo:layout-master-set`.
- **page-height**: Specifies the height of a page. `auto` determines the height from the medium or User Agent window. `indefinite` means the height is determined by content. A `<length>` specifies a fixed height.
- **page-width**: Specifies the width of a page. Same value semantics as `page-height`. Note: `page-width` and `page-height` may not both be set to `indefinite`.
- **margin-top/bottom/left/right**: Indent the page-reference-area from the page-viewport-area edges. These use absolute directions (top/bottom/left/right) rather than relative directions.
- **reference-orientation**: Rotation of the reference area coordinate system (in degrees counter-clockwise).
- **writing-mode**: Determines the placement of the five regions on the page and the block/inline progression directions.

## Usage Notes

The `fo:simple-page-master` is the most commonly used page-master. It defines a page with a fixed set of up to five named regions. The page dimensions are set by `page-height` and `page-width`, and the margins control the page-reference-area insets.

The spacing between the outer four regions (before, after, start, end) and each `fo:region-body` is determined by subtracting the relevant `extent` trait on each outer region from the corresponding margin property on that `fo:region-body`.

For a typical letter-size portrait document with lr-tb writing mode:
- `page-height="11in"`, `page-width="8.5in"` -- letter size
- `margin-top`, `margin-bottom`, `margin-left`, `margin-right` -- page margins
- `fo:region-body` occupies the center
- `fo:region-before` is the header area (top)
- `fo:region-after` is the footer area (bottom)
- `fo:region-start` is the left sidebar
- `fo:region-end` is the right sidebar

## Code Samples

No code samples in spec for this formatting object's own section. However, `fo:simple-page-master` appears in code samples throughout the spec:

### Page-master with region-body and region-before (writing-mode example)

<!-- Source: xslspec.xml line 5725 -->
```xml
<fo:simple-page-master master-name="all-pages">
  <fo:region-body region-name="xsl-region-body" margin="0.75in"
                  writing-mode="tb-rl" />
  <fo:region-before region-name="xsl-region-before" extent="0.75in"/>
</fo:simple-page-master>
```

### Page-master with page dimensions and region margins

<!-- Source: xslspec.xml line 10510 -->
```xml
<fo:simple-page-master master-name="page"
  page-height="297mm" page-width="210mm"
  margin-top="20mm" margin-bottom="10mm"
  margin-left="25mm" margin-right="25mm">
  <fo:region-body margin-top="0mm" margin-bottom="15mm"
    margin-left="0mm" margin-right="0mm"/>
  <fo:region-after extent="10mm"/>
</fo:simple-page-master>
```

### Page-master with all seven region types including extension regions

<!-- Source: xslspec.xml line 9395 -->
```xml
<fo:simple-page-master master-name="only"
      page-height="29.7cm"
      page-width="21cm"
      margin-top="1cm"
      margin-bottom="2cm"
      margin-left="2.5cm"
      margin-right="2.5cm">
      <fo:region-body margin-top="3cm" margin-bottom="1.5cm"
      margin-left="2cm" margin-right="2cm"/>
      <fo:extension-region-start extent="1cm" distance="0.5cm"/>
      <fo:extension-region-end extent="1cm" distance="0.5cm"/>
      <fo:region-before precedence="true" extent="3cm"/>
      <fo:region-after precedence="true" extent="1.5cm"/>
      <fo:region-start extent="1cm"/>
      <fo:region-end extent="1cm"/>
      </fo:simple-page-master>
```

For comprehensive examples of conditional page layouts with multiple page-masters, dynamic region sizing, and multi-section documents, see **guide-conditional-page-layouts**.

## See Also

- fo:layout-master-set -- parent container
- fo:region-body -- the main content region
- fo:region-before -- the before (header) region
- fo:region-after -- the after (footer) region
- fo:region-start -- the start (left in lr-tb) region
- fo:region-end -- the end (right in lr-tb) region
- fo:page-master -- alternative page-master with arbitrary region layout
- fo:page-sequence -- references this master via master-reference
- fo:page-sequence-master -- orchestrates page-master selection
