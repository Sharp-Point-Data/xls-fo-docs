# fo:static-content

## Summary

The `fo:static-content` formatting object holds a sequence or a tree of formatting objects that is to be presented in a single region or repeated in like-named regions on one or more pages in the page-sequence. Its common use is for repeating or running headers and footers. This content is repeated, in its entirety, on every page to which it is assigned.

## Areas

The `fo:static-content` formatting object does not generate any areas. The `fo:static-content` formatting object returns the sequence of areas created by concatenating the sequences of areas returned by each of the children of the `fo:static-content`. The order of concatenation is the same order as the children are ordered under the `fo:static-content`.

## Content Model

```
(%block;)+
```

The `fo:static-content` must contain one or more block-level formatting objects.

## Properties

| Property | Type | Inherited | Conformance Level |
|---|---|---|---|
| id | \<id\> | No | Basic |
| index-class | \<string\> | No | Extended |
| index-key | \<string\> | No | Extended |
| flow-name | \<name\> | No | Basic |

## Constraints

The flow-map determines the assignment of the content of the `fo:static-content` to a region.

The `fo:static-content` may be processed multiple times and thus the default ordering constraint does not apply to the `fo:static-content`. Instead, it must satisfy the constraint on a per-page basis. Specifically, if P is a page-reference-area, C is an area-class, and S is the set of all descendants of P of area-class C returned to the `fo:static-content` descendant, then S must be properly ordered.

## Usage Notes

- The `fo:static-content` is used for content that repeats on every page (or every page in a sub-sequence), such as headers, footers, and sidebar content.
- The `flow-name` property must match the `region-name` of a region defined in the page-master(s) used by the page-sequence. Common values are "xsl-region-before" for headers and "xsl-region-after" for footers.
- Unlike `fo:flow`, the content of `fo:static-content` is not paginated -- it is rendered in its entirety in the assigned region on each page.
- Multiple `fo:static-content` elements may appear in a single `fo:page-sequence`, each targeting a different region.
- All `fo:static-content` children of `fo:page-sequence` must appear before any `fo:flow` children.
- Because the content is repeated on each page, `fo:retrieve-marker` is commonly used within `fo:static-content` to display page-varying content such as running headers derived from the main flow.
- If the static content overflows the region, the `overflow` property on the region controls the behavior.

## Code Samples

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_static-content -->
```xml
(%block;)+
```

## See Also

- `fo:page-sequence` -- parent formatting object that contains static-content and flows
- `fo:flow` -- provides the main flowing content that is distributed across pages
- `fo:region-before` -- commonly used region for header static content
- `fo:region-after` -- commonly used region for footer static content
- `fo:region-start` -- start-side region that can hold static content
- `fo:region-end` -- end-side region that can hold static content
- `fo:retrieve-marker` -- retrieves marker content for use in running headers/footers
