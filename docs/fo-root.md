# fo:root

## Summary

The `fo:root` formatting object is the top node of the formatting object tree. It holds an `fo:layout-master-set`, an optional `fo:declarations`, an optional `fo:bookmark-tree`, and one or more `fo:layout-master-set`, `fo:page-sequence`, or `fo:page-sequence-wrapper` objects. An `fo:layout-master-set` holds masters used in the document. Each `fo:page-sequence` represents a sequence of pages that result from formatting the content children of the `fo:page-sequence`. An `fo:page-sequence-wrapper` can also occur as the child of `fo:root` and is used to specify inherited properties for the `fo:page-sequence` objects it wraps; it has no additional formatting semantics.

A document can contain multiple `fo:page-sequence` elements. For example, each chapter of a document could be a separate `fo:page-sequence`; this would allow chapter-specific content, such as the chapter title, to be placed within a header or footer.

## Areas

Page-viewport-areas are returned by the `fo:page-sequence` children of the `fo:root` formatting object. The `fo:root` does not generate any areas.

## Constraints

The children of the root of the area tree consist solely of, and totally of, the page-viewport-areas returned by the `fo:page-sequence` children of the `fo:root`. The set of all areas returned by the `fo:page-sequence` children is properly ordered.

It is an error if there is not at least one `fo:page-sequence` descendant of `fo:root`.

## Content Model

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_root -->
```xml
(layout-master-set,declarations?,bookmark-tree?,(layout-master-set|page-sequence|page-sequence-wrapper)+)
```

The first child must be an `fo:layout-master-set`. An optional `fo:declarations` may follow, then an optional `fo:bookmark-tree`. After these, one or more `fo:layout-master-set`, `fo:page-sequence`, or `fo:page-sequence-wrapper` children are required.

## Properties

| Property | Type | Initial Value | Inherited | Conformance Level |
|---|---|---|---|---|
| source-document | `<uri-specification> [<uri-specification>]* \| none \| inherit` | none | no | Basic |
| role | `<uri-specification> \| none \| inherit` | none | no | Basic |
| id | `<id>` | see prose | no | Basic |
| index-class | `<string>` | empty string | no | Extended |
| index-key | `<string>` | none | no | Extended |
| media-usage | `auto \| paginate \| bounded-in-one-dimension \| unbounded` | auto | no | Extended |

The "Common Accessibility Properties" group includes `source-document` and `role`.

## Usage Notes

Every XSL-FO document must have exactly one `fo:root` as the root element. It serves as the structural container for the entire document. The `fo:root` element must contain at least one `fo:layout-master-set` (which defines page layouts) and at least one descendant `fo:page-sequence` (which provides the content).

The `media-usage` property on `fo:root` controls how pages are presented: `paginate` produces a sequence of fixed-size pages (typical for print), `bounded-in-one-dimension` produces a single scrollable page per page-sequence, and `unbounded` produces pages that grow in both dimensions to fit content.

## Code Samples

No code samples in spec for this formatting object. The spec section contains only the content model declaration shown above.

## See Also

- fo:layout-master-set -- defines page masters used by the document
- fo:declarations -- global declarations including color profiles
- fo:bookmark-tree -- document bookmarks/outline
- fo:page-sequence -- generates a sequence of pages from content
- fo:page-sequence-wrapper -- groups page-sequences for inherited properties
