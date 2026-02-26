# fo:shape-background-specifier

## Summary

The fo:shape-background-specifier is used to specify the background shape design. It defines the shape geometry applied to the background rendering of a region.

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

The spec does not define specific area generation for this formatting object. It serves as a configuration element for background shape geometry.

## Usage Notes

- This formatting object is part of the shape-based design model in XSL-FO 2.0.
- Use it to define the background shape for a region.
- The height and width properties define the dimensions of the background shape.
- The display-align property controls alignment within the shape area.

## Code Samples

No code samples in spec for this formatting object.

## See Also

- [fo:shape-path-specifier](fo-shape-path-specifier.md) — specifies the intrusion path shape
- [fo:shape-border-specifier](fo-shape-border-specifier.md) — specifies the border shape design
- Common Relative Position Properties
- display-align property
- height property
- width property
