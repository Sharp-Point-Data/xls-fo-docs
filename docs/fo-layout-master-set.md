# fo:layout-master-set

## Summary

The `fo:layout-master-set` is a wrapper around masters used in the document. This includes page-sequence-masters, page-masters, and flow-maps. It is a required child of `fo:root` and provides the page layout definitions that `fo:page-sequence` elements reference when generating pages.

## Areas

The `fo:layout-master-set` formatting object generates no area directly. The masters that are the children of the `fo:layout-master-set` are used by the `fo:page-sequence` to generate pages.

## Constraints

The value of the `master-name` trait on each child of the `fo:layout-master-set` must be unique within the set.

## Content Model

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_layout-master-set -->
```xml
(simple-page-master|page-sequence-master|flow-map)+
```

The `fo:layout-master-set` must contain one or more children, each of which is an `fo:simple-page-master`, `fo:page-sequence-master`, or `fo:flow-map`.

## Properties

The `fo:layout-master-set` formatting object has no properties defined in the spec. It is a structural container only.

## Usage Notes

Every XSL-FO document must contain at least one `fo:layout-master-set` as the first child of `fo:root`. This element defines all the page layouts available in the document.

The `fo:layout-master-set` serves three purposes:

1. **Page geometry definition**: Through `fo:simple-page-master` (or `fo:page-master`) children, it defines page sizes, margins, and region layout.
2. **Page selection logic**: Through `fo:page-sequence-master` children, it defines rules for selecting which page master to use for each page in a sequence (e.g., different layouts for first, odd, even, and blank pages).
3. **Flow mapping**: Through `fo:flow-map` children, it defines how flows are assigned to regions across pages.

Each master within the set must have a unique `master-name`. This name is referenced by `fo:page-sequence` elements (via `master-reference`) and by sub-sequence-specifiers within `fo:page-sequence-master` elements.

Additional `fo:layout-master-set` elements may appear later in the document (as children of `fo:root` or `fo:page-sequence-wrapper`), allowing page masters to be defined closer to where they are used.

## Code Samples

No code samples in spec for this formatting object. The spec section contains only the content model declaration shown above.

## See Also

- fo:root -- parent element that must contain at least one fo:layout-master-set
- fo:simple-page-master -- defines a page layout with predefined region structure
- fo:page-master -- defines a page layout with arbitrary regions
- fo:page-sequence-master -- defines page selection logic for a page-sequence
- fo:flow-map -- defines flow-to-region assignments
- fo:page-sequence -- references masters by name via master-reference
