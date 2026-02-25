# fo:shape-border-specifier

## Summary

The fo:shape-border-specifier is used to specify the border shape design. It defines the shape geometry applied to the border rendering of a region.

## Content Model

```
EMPTY
```

This formatting object has no children.

## Properties

| Property | Type | Initial Value | Inherited | Conformance Level |
|----------|------|---------------|-----------|-------------------|
| Common Relative Position Properties | | | | extended |
| height | auto \| length \| percentage | auto | no | basic |
| width | auto \| length \| percentage | auto | no | basic |

Note: The spec references a "shape-name-reference" property similar to flow-name-reference, but this property is not yet formally defined in the specification.

## Areas

The spec does not define specific area generation for this formatting object. It serves as a configuration element for border shape geometry.

## Usage Notes

- This formatting object is part of the shape-based design model in XSL-FO 2.0.
- Use it to define the border shape for a region.
- The height and width properties define the dimensions of the border shape.
- Unlike fo:shape-background-specifier, the spec does not list display-align as an applicable property for this formatting object.

## Code Samples

No code samples in spec for this formatting object.

## See Also

- fo:shape-path-specifier — specifies the intrusion path shape
- fo:shape-background-specifier — specifies the background shape design
- Common Relative Position Properties
- height property
- width property
