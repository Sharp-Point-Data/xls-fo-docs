# fo:shape-path-specifier

## Summary

The fo:shape-path-specifier is used to specify the intrusion path created from this region when intruding other regions. It defines the shape geometry that determines how content from one region intrudes into another.

## Content Model

```
EMPTY
```

This formatting object has no children.

## Properties

| Property | Type | Initial Value | Inherited | Conformance Level |
|----------|------|---------------|-----------|-------------------|
| Common Relative Position Properties | | | | extended |
| display-align | auto \| before \| center \| after | auto | yes | basic |
| height | auto \| length \| percentage | auto | no | basic |
| width | auto \| length \| percentage | auto | no | basic |

Note: The spec references a "shape-name-reference" property similar to flow-name-reference, but this property is not yet formally defined in the specification.

## Areas

The spec does not define specific area generation for this formatting object. It serves as a configuration element for intrusion path geometry.

## Usage Notes

- This formatting object is part of the shape-based intrusion model in XSL-FO 2.0.
- Use it to define the path shape when one region intrudes upon another region's content area.
- The height and width properties define the dimensions of the intrusion path.
- The display-align property controls alignment within the shape area.

## Code Samples

### Sample 1: Content model declaration

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_shape-path-specifier -->
```xml
EMPTY
```

## See Also

- [fo:shape-background-specifier](fo-shape-background-specifier.md) — specifies the background shape design
- [fo:shape-border-specifier](fo-shape-border-specifier.md) — specifies the border shape design
- Common Relative Position Properties
- display-align property
- height property
- width property
