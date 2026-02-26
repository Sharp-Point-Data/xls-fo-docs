# fo:region

## Summary

The `fo:region` formatting object is new in XSL-FO 2.0 and is used in constructing an `fo:page-master`. Each `fo:region` behaves similarly to the `fo:region-body` of XSL-FO 1.1, but is positioned absolutely within the `fo:page-master`. A region specifies a viewport/reference pair that is located at an absolute position within the `fo:page-master`. The `overflow` trait controls how much of the underlying region-reference-area is visible; that is, whether the region-reference-area is clipped by its parent region-viewport-area.

Typically, for paged media, the areas returned by the `fo:flow` formatting object in an `fo:page-sequence` are made to be descendants of a sequence of region-reference-areas that correspond to region-bodies. If the `fo:flow` flow is assigned to some other region, then the areas returned by the `fo:flow` are constrained to be descendants of region-reference-areas generated using the assigned region-master.

The `fo:region` may be divided into multiple columns. When the `column-count` trait is greater than one, the region will be subdivided into multiple columns.

The shape assignment model allows a region to point to one or more shapes that define:
- **Content path**: where the region's content is bound to wrap
- **Wrapping path**: where the region's intruded content is bound to wrap around
- **Border**: one or more shapes used to define a border beyond standard FO border capabilities or designed ad-hoc
- **Background**: one or more shapes used to define a background effect beyond standard FO background capabilities

## Areas

Same as `fo:region-body`.

## Content Model

```
(shape-name-specifier,
  shape-path-specifier?,
  shape-background-specifier*, shape-border-specifier*)
```

The `fo:region` may contain child elements that define shape references for non-rectangular content, wrapping, border, and background effects.

## Properties

| Property | Type | Inherited | Conformance Level |
|---|---|---|---|
| Common Absolute Position Properties | | No | Extended |
| Common Border, Padding, and Background Properties | | Various | Basic |
| Common Margin Properties - Block | | No | Basic |
| Common Wrap Properties | | No | Extended |
| clip | auto \| rect(...) \| inherit | No | Extended |
| column-count | \<number\> | No | Extended |
| column-gap | \<length\> \| \<percentage\> | No | Extended |
| display-align | auto \| before \| center \| after \| inherit | No | Basic |
| height | \<length\> \| \<percentage\> \| auto \| inherit | No | Basic |
| overflow | visible \| hidden \| scroll \| error-if-overflow \| auto \| paginate \| inherit | No | Basic |
| region-name | \<name\> | No | Basic |
| reference-orientation | 0 \| 90 \| 180 \| 270 \| -90 \| -180 \| -270 \| inherit | No | Extended |
| width | \<length\> \| \<percentage\> \| auto \| inherit | No | Basic |
| writing-mode | lr-tb \| rl-tb \| tb-rl \| tb-lr \| lr \| rl \| tb \| inherit | No | Basic |
| z-index | auto \| \<integer\> \| inherit | No | Extended |

## Trait Derivation

Same as `fo:region-body`.

## Constraints

Same as `fo:region-body`.

**Note:** This draft does not yet cover the interactions between non-rectangular shapes and footnotes.

## Usage Notes

- The `fo:region` is an XSL-FO 2.0 addition. It provides absolute positioning of regions within an `fo:page-master`, unlike the fixed-position regions (`fo:region-body`, `fo:region-before`, etc.) used with `fo:simple-page-master`.
- Use `absolute-position="absolute"` with `top`, `left`, `width`, and `height` to position the region within the page-master.
- Multiple `fo:region` elements may be placed within a single `fo:page-master`, each with its own `region-name` and `z-index` for layering.
- The `z-index` property controls the stacking order when regions overlap.
- Shape specifier children enable non-rectangular content areas using SVG paths defined by `fo:shape` elements in the `fo:layout-master-set`.

## Code Samples

### Sample 1: Content Model

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_region -->
```xml
(shape-name-specifier,
  shape-path-specifier?,
  shape-background-specifier*, shape-border-specifier*)
```

### Sample 2: Two Overlapping Regions

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_region -->
```xml
<fo:page-master
	       master-name="only"
	       page-height="11in" page-width="8.5in"
	       margin-top="3pt" margin-bottom="3pt"
	       margin-left="3pt" margin-right="3pt">

	       <fo:region
	        absolute-position="absolute"
	        top="0.8636in" left="1.125in"
	        width="6.75in" height="7.75in"
	        region-name="region_A"
	        z-index="0"
	        wrap="shape"
	        wrap-sides="both"
	        wrap-path="shape">
	        ... shape reference specifier(s) ...
	       </fo:region>

	      <fo:region
	        absolute-position="absolute"
	        top="1.3in" left="1.4in"
	        width="3.6in" height="5.4in"
	        region-name="region_B"
	        z-index="1">
	        ... shape reference specifier(s) ...
	       </fo:region>

	      </fo:page-master>
```

### Sample 3: Full Shape and Region Use and Re-use

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_region -->
```xml
<fo:layout-master-set>
	        <fo:shape shape-name="hexagon">
	          <svg:svg xmlns:svg="http://www.w3.org/2000/svg">
	            <svg:path d="M ... z " />
	          </svg:svg>
	        </fo:shape>

	        <fo:shape shape-name="intruder-bag">
	          <svg:svg xmlns:svg="http://www.w3.org/2000/svg">
	            <svg:path d="M ... z " />
	          </svg:svg>
	        </fo:shape>

	        <fo:shape shape-name="border-bag">
	          <svg:svg xmlns:svg="http://www.w3.org/2000/svg">
	           <svg:path d="M ... z " />
	          </svg:svg>>
	       </fo:shape>

	       <fo:shape shape-name="bag">
	        <svg:svg xmlns:svg="http://www.w3.org/2000/svg">
	        <svg:path d="M ... z " />
	       </svg:svg>
	      </fo:shape>

	      <fo:page-master
	        master-name="only"
	        page-height="11in" page-width="8.5in"
	        margin-top="3pt" margin-bottom="3pt"
	        margin-left="3pt" margin-right="3pt">

	       <fo:region
	          absolute-position="absolute"
	          top="0.8636in" left="1.125in"
	          width="10in" height="12in"
	          region-name="region_A"
	          z-index="0">

	         <fo:shape-name-specifier
	             shape-name-reference="bag"
	            width="100%" height="100%"
	            display-align="center" />

	        <fo:shape-path-specifier
	              shape-name-reference="intruder-bag"
	              width="100%" height="100%"
	              display-align="center" />

	            <fo:shape-border-specifier
	              shape-name-reference="border-bag"
	              width="100%" height="100%"
	              display-align="center" />

	            <fo:fo:shape-background-specifier
	              shape-name-reference="hexagon"
	              width="80%" height="80%"
	              relative-position="relative"
	              top="6in" left="6in" />

	            <fo:fo:shape-background-specifier
	              shape-name-reference="hexagon"
	              width="60%" height="60%"
	              relative-position="relative"
	              top="4in" left="4in" />

	            <fo:fo:shape-background-specifier
	              shape-name-reference="hexagon"
	              width="40%" height="40%"
	              relative-position="relative"
	              top="2in" left="2in" />

	            <fo:fo:shape-background-specifier
	              shape-name-reference="hexagon"
	              width="20%" height="20%"
	              relative-position="relative"
	              top="1in" left="1in" />

	          </fo:region>
	        </fo:page-master>

	      </fo:layout-master-set>
```

## See Also

- [fo:page-master](fo-page-master.md) — parent formatting object for XSL-FO 2.0 page layout
- [fo:region-body](fo-region-body.md) — XSL-FO 1.1 central content region (similar behavior)
- fo:shape — defines SVG-based shapes for use in region shape specifiers
- fo:shape-name-specifier — specifies the content shape for a region
- [fo:shape-path-specifier](fo-shape-path-specifier.md) — specifies the intrusion path for a region
- [fo:shape-border-specifier](fo-shape-border-specifier.md) — specifies a non-rectangular border shape
- [fo:shape-background-specifier](fo-shape-background-specifier.md) — specifies a non-rectangular background shape
- [fo:flow](fo-flow.md) — provides flowing content that is distributed into regions
