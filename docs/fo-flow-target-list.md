# fo:flow-target-list

## Summary

The fo:flow-target-list is used to specify the sequence of regions to which flows are assigned in a particular fo:flow-assignment. It contains one or more fo:region-name-specifier children that identify the target regions by name.

## Content Model

```
(fo:region-name-specifier+)
```

The fo:flow-target-list must contain one or more fo:region-name-specifier children.

## Properties

This formatting object has no properties of its own. It serves as a structural container within fo:flow-assignment.

## Areas

The fo:flow-target-list formatting object generates no area directly. It is used by the fo:page-sequence formatting object to assign flows to regions.

## Constraints

The children of the fo:flow-target-list are a sequence of region-name-specifiers identifying regions in the sequence.

## Usage Notes

- When multiple fo:region-name-specifier children are present, the source flows are distributed across the referenced regions in the order specified.
- Each region-name referenced must correspond to a region defined in the page-master used by the page-sequence.
- A given region-name must not appear in the target list of more than one fo:flow-assignment within the same fo:flow-map.

## Code Samples

### Sample 1: Content model declaration

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_flow-target-list -->
```xml
(region-name-specifier+)
```

## See Also

- [fo:flow-assignment](fo-flow-assignment.md) — parent container that pairs source and target lists
- [fo:region-name-specifier](fo-region-name-specifier.md) — specifies individual region names within the target list
- [fo:flow-source-list](fo-flow-source-list.md) — the corresponding source list of flows
- [fo:flow-map](fo-flow-map.md) — top-level flow-to-region mapping object
