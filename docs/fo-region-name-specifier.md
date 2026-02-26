# fo:region-name-specifier

## Summary

The fo:region-name-specifier is used to specify one region in a target-list. It identifies a single page region by its region-name, for use within an fo:flow-target-list.

## Content Model

```
EMPTY
```

This formatting object has no children.

## Properties

| Property | Type | Initial Value | Inherited | Conformance Level |
|----------|------|---------------|-----------|-------------------|
| region-name-reference | name | N/A (required) | no | extended |

## Areas

The fo:region-name-specifier formatting object generates no area directly. It is used by the fo:page-sequence formatting object to assign flows to regions.

## Constraints

The region-name-reference property specifies the name of a region in the target sequence.

## Usage Notes

- The region-name-reference property value must match the region-name of a region defined in the page-master(s) used by the page-sequence that references the containing fo:flow-map.
- Multiple fo:region-name-specifier elements within the same fo:flow-target-list cause the source content to be distributed across the referenced regions.
- A given region-name must not appear in the target list of more than one fo:flow-assignment within the same fo:flow-map.

## Code Samples

### Sample 1: Content model declaration

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_region-name-specifier -->
```xml
EMPTY
```

## See Also

- [fo:flow-target-list](fo-flow-target-list.md) — parent container for region-name-specifier objects
- [fo:flow-assignment](fo-flow-assignment.md) — contains the source and target lists
- [fo:flow-map](fo-flow-map.md) — top-level flow-to-region mapping object
- [fo:region-body](fo-region-body.md), [fo:region-before](fo-region-before.md), [fo:region-after](fo-region-after.md), [fo:region-start](fo-region-start.md), [fo:region-end](fo-region-end.md) — region definitions whose region-name is referenced
- region-name-reference property — specifies the region name to reference
