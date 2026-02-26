# fo:flow

## Summary

The `fo:flow` formatting object provides the flowing text content that is distributed into pages. The content of the `fo:flow` is a sequence of flow objects (block-level formatting objects) that are laid out into the regions of pages in the page-sequence.

## Areas

The `fo:flow` formatting object does not generate any areas. The `fo:flow` formatting object returns a sequence of areas created by concatenating the sequences of areas returned by each of the children of the `fo:flow`. The order of concatenation is the same order as the children are ordered under the `fo:flow`.

## Content Model

```
(%block;)+
```

The `fo:flow` must contain one or more block-level formatting objects. In addition, this formatting object may have a sequence of zero or more `fo:marker`s as its initial children.

## Properties

| Property | Type | Inherited | Conformance Level |
|---|---|---|---|
| id | \<id\> | No | Basic |
| index-class | \<string\> | No | Extended |
| index-key | \<string\> | No | Extended |
| flow-name | \<name\> | No | Basic |

## Constraints

The flow-map determines the assignment of the content of the `fo:flow` to a region. The `flow-name` property on the `fo:flow` identifies which region (by `region-name`) receives the flow content. When no explicit `fo:flow-map` is specified, the default mapping assigns each flow to the region whose `region-name` matches the `flow-name`.

## Usage Notes

- The `fo:flow` is a required child of `fo:page-sequence`. It contains the main flowing content of a document that is paginated across multiple pages.
- The `flow-name` property must match the `region-name` of a region defined in the page-master(s) used by the page-sequence. The most common value is "xsl-region-body", which targets the `fo:region-body`.
- Unlike `fo:static-content`, the content of `fo:flow` is distributed across pages -- it does not repeat on each page.
- Each `fo:page-sequence` must have at least one `fo:flow` child, but may have multiple `fo:flow` children when using an explicit `fo:flow-map`.
- `fo:marker` children, if present, must appear before any block-level children.
- The block-level children may include `fo:block`, `fo:block-container`, `fo:table-and-caption`, `fo:table`, `fo:list-block`, and other block-level formatting objects.

## Code Samples

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_flow -->
```xml
(%block;)+
```

## See Also

- [fo:page-sequence](fo-page-sequence.md) — parent formatting object that contains flows
- [fo:static-content](fo-static-content.md) — provides repeating content (headers, footers) that does not flow across pages
- [fo:region-body](fo-region-body.md) — the default region that receives flow content
- [fo:flow-map](fo-flow-map.md) — explicitly assigns flows to regions
- [fo:marker](fo-marker.md) — creates named content snippets that can be retrieved by fo:retrieve-marker
