# fo:flow-source-list

## Summary

The fo:flow-source-list is used to specify the sequence of flows to assign in a particular fo:flow-assignment. It contains one or more fo:flow-name-specifier children that identify the source flows by name.

## Content Model

```
(fo:flow-name-specifier+)
```

The fo:flow-source-list must contain one or more fo:flow-name-specifier children.

## Properties

This formatting object has no properties of its own. It serves as a structural container within fo:flow-assignment.

## Areas

The fo:flow-source-list formatting object generates no area directly. It is used by the fo:page-sequence formatting object to assign flows to regions.

## Constraints

The children of the fo:flow-source-list are a sequence of flow-name-specifiers identifying flows of the sequence. These flows must be either all fo:flow formatting objects or all fo:static-content formatting objects. It is an error if they are a mixture.

## Usage Notes

- When multiple fo:flow-name-specifier children are present, their referenced flows are treated as a single combined flow for composition purposes.
- The ordering of fo:flow-name-specifier children within the source list determines the order in which the referenced flows are concatenated.
- Each flow-name referenced must correspond to an fo:flow or fo:static-content child of the page-sequence that references the containing fo:flow-map.

## Code Samples

### Sample 1: Content model declaration

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_flow-source-list -->
```xml
(flow-name-specifier+)
```

## See Also

- fo:flow-assignment — parent container that pairs source and target lists
- fo:flow-name-specifier — specifies individual flow names within the source list
- fo:flow-target-list — the corresponding target list of regions
- fo:flow-map — top-level flow-to-region mapping object
