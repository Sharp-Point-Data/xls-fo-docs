# fo:flow-assignment

## Summary

The fo:flow-assignment is used to specify the assignment of one sequence of flows to a sequence of regions. It is a child of fo:flow-map and contains exactly one fo:flow-source-list and one fo:flow-target-list, defining which flows map to which regions.

## Content Model

```
(fo:flow-source-list, fo:flow-target-list)
```

The fo:flow-assignment must contain exactly one fo:flow-source-list followed by exactly one fo:flow-target-list.

## Properties

This formatting object has no properties of its own. It serves as a structural container within fo:flow-map.

## Areas

The fo:flow-assignment formatting object generates no area directly. It is used by the fo:page-sequence formatting object to assign flows to regions.

## Constraints

The children of the fo:flow-assignment are a source-list and target-list containing constraints for assigning one sequence of flows to a sequence of regions.

## Usage Notes

- Each fo:flow-assignment defines one mapping group within a fo:flow-map.
- The source list identifies one or more flows (by flow-name) that are treated as a single flow for composition.
- The target list identifies one or more regions (by region-name) that receive the source content.
- A given flow-name must not appear in more than one fo:flow-assignment within the same fo:flow-map.
- A given region-name must not appear in more than one fo:flow-assignment within the same fo:flow-map.

## Code Samples

### Sample 1: Content model declaration

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_flow-assignment -->
```xml
(flow-source-list,flow-target-list)
```

## See Also

- fo:flow-map — parent container for flow-assignment objects
- fo:flow-source-list — specifies source flow names
- fo:flow-target-list — specifies target region names
- fo:flow-name-specifier — specifies individual flow names
- fo:region-name-specifier — specifies individual region names
