# fo:flow-map

## Summary

The fo:flow-map is used to specify the assignment of flows to regions. It enables flexible mapping between fo:flow objects and page regions, allowing multiple flows to be directed to multiple regions within a page-sequence. When no explicit fo:flow-map is provided, an implicit flow-map is used that maps each standard flow name to its corresponding region name.

## Content Model

```
(fo:flow-assignment+)
```

The fo:flow-map must contain one or more fo:flow-assignment children. Each fo:flow-assignment defines a source list (flow names) and a target list (region names).

## Properties

| Property | Type | Initial Value | Inherited | Conformance Level |
|----------|------|---------------|-----------|-------------------|
| flow-map-name | name | N/A (required) | no | extended |

## Areas

The fo:flow-map formatting object generates no area directly. It is used by the fo:page-sequence formatting object to assign flows to regions.

Each fo:flow-assignment child of the fo:flow-map defines a source list and a target list. The source list is a sequence of flow names whose corresponding fo:flow objects (in the referring fo:page-sequence) are treated as a single fo:flow for composition purposes. The target list is a sequence of region-names which identify the region or regions on each page which are used for the source content.

This is independent of the actual sequence of pages, which is generated as it has always been generated using the fo:simple-page-master and fo:page-sequence-master objects referred to by the master-reference property of the fo:page-sequence.

For each fo:flow-assignment child of the fo:flow-map, having an fo:flow-source-list child S and an fo:flow-target-list child T, the fo:flow-map assigns each of the flows referenced by the fo:flow-name-specifier children of S to the regions referenced by the fo:region-name-specifier children of T.

## Constraints

Many of the constraints that a flow-map induces are expressed in the fo:page-sequence specification.

The children of the fo:flow-map are fo:flow-assignment objects containing parallel constraints for assigning flows to regions. It is an error for a flow-name to appear in the source list of more than one fo:flow-assignment child of a given fo:flow-map. It is also an error for a region-name to appear in the target list of more than one fo:flow-assignment child of a given fo:flow-map.

## Usage Notes

- Use fo:flow-map when you need to assign multiple flows to multiple regions on a page, such as mapping body content to one region and sidebar content to another.
- The fo:page-sequence references a flow-map via the flow-map-reference property.
- If no explicit flow-map is referenced, an implicit flow-map is used that provides one-to-one mapping of the standard region names (xsl-region-body, xsl-region-before, xsl-region-after, xsl-region-start, xsl-region-end) to their corresponding regions.

## Code Samples

### Sample 1: Implicit flow-map (default mapping)

This example shows the implicit flow-map that is used when no explicit flow-map is specified. It maps each standard flow name to its corresponding region.

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_flow-map -->
```xml
<fo:flow-map>
  <fo:flow-assignment>
    <fo:flow-source-list>
      <fo:flow-name-specifier
        flow-name-reference="xsl-region-body"/>
    </fo:flow-source-list>
    <fo:flow-target-list>
      <fo:region-name-specifier
        region-name-reference="xsl-region-body"/>
    </fo:flow-target-list>
  </fo:flow-assignment>
  <fo:flow-assignment>
    <fo:flow-source-list>
      <fo:flow-name-specifier
        flow-name-reference="xsl-region-before"/>
    </fo:flow-source-list>
    <fo:flow-target-list>
      <fo:region-name-specifier
        region-name-reference="xsl-region-before"/>
    </fo:flow-target-list>
  </fo:flow-assignment>
  <fo:flow-assignment>
    <fo:flow-source-list>
      <fo:flow-name-specifier
        flow-name-reference="xsl-region-after"/>
    </fo:flow-source-list>
    <fo:flow-target-list>
      <fo:region-name-specifier
        region-name-reference="xsl-region-after"/>
    </fo:flow-target-list>
  </fo:flow-assignment>
  <fo:flow-assignment>
    <fo:flow-source-list>
      <fo:flow-name-specifier
        flow-name-reference="xsl-region-start"/>
    </fo:flow-source-list>
    <fo:flow-target-list>
      <fo:region-name-specifier
        region-name-reference="xsl-region-start"/>
    </fo:flow-target-list>
  </fo:flow-assignment>
  <fo:flow-assignment>
    <fo:flow-source-list>
      <fo:flow-name-specifier
        flow-name-reference="xsl-region-end"/>
    </fo:flow-source-list>
    <fo:flow-target-list>
      <fo:region-name-specifier
        region-name-reference="xsl-region-end"/>
     </fo:flow-target-list>
  </fo:flow-assignment>
</fo:flow-map>
```

### Sample 2: Content model declaration

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_flow-map -->
```xml
(flow-assignment+)
```

## See Also

- [fo:flow-assignment](fo-flow-assignment.md) — defines a single source-to-target mapping within a flow-map
- [fo:flow-source-list](fo-flow-source-list.md) — specifies the source flow names in a flow-assignment
- [fo:flow-target-list](fo-flow-target-list.md) — specifies the target region names in a flow-assignment
- [fo:flow-name-specifier](fo-flow-name-specifier.md) — specifies a single flow name in a source list
- [fo:region-name-specifier](fo-region-name-specifier.md) — specifies a single region name in a target list
- [fo:page-sequence](fo-page-sequence.md) — references a flow-map via the flow-map-reference property
- flow-map-name property — names the flow-map for reference
