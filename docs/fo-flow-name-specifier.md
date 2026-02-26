# fo:flow-name-specifier

## Summary

The fo:flow-name-specifier is used to specify one flow in a source-list. It identifies a single fo:flow or fo:static-content by its flow-name, for use within an fo:flow-source-list.

## Content Model

```
EMPTY
```

This formatting object has no children.

## Properties

| Property | Type | Initial Value | Inherited | Conformance Level |
|----------|------|---------------|-----------|-------------------|
| flow-name-reference | name | N/A (required) | no | extended |

## Areas

The fo:flow-name-specifier formatting object generates no area directly. It is used by the fo:page-sequence formatting object to assign flows to regions.

## Constraints

The flow-name-reference property specifies the name of a flow in the source sequence.

## Usage Notes

- The flow-name-reference property value must match the flow-name property of an fo:flow or fo:static-content child of the referring fo:page-sequence.
- Multiple fo:flow-name-specifier elements within the same fo:flow-source-list cause the referenced flows to be treated as a single flow for composition purposes.
- All flows referenced within a single fo:flow-source-list must be either all fo:flow objects or all fo:static-content objects; mixing is an error.

## Code Samples

### Sample 1: Content model declaration

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_flow-name-specifier -->
```xml
EMPTY
```

## See Also

- [fo:flow-source-list](fo-flow-source-list.md) — parent container for flow-name-specifier objects
- [fo:flow-assignment](fo-flow-assignment.md) — contains the source and target lists
- [fo:flow-map](fo-flow-map.md) — top-level flow-to-region mapping object
- [fo:flow](fo-flow.md) — the flow object whose flow-name is referenced
- [fo:static-content](fo-static-content.md) — static content object whose flow-name may be referenced
- flow-name-reference property — specifies the flow name to reference
