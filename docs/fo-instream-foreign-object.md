# fo:instream-foreign-object

## Summary

The fo:instream-foreign-object flow object is used for an inline graphic or other "generic" object where the object data resides as descendants of the fo:instream-foreign-object, typically as an XML element subtree in a non-XSL namespace. A common format is SVG. It generates and returns one inline viewport-area and one reference-area containing the instream-foreign-object.

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_instream-foreign-object -->

## Content Model

The fo:instream-foreign-object flow object has a child from a non-XSL namespace. The permitted structure of this child is that defined for that namespace.

The fo:instream-foreign-object flow object may have additional attributes in the non-XSL namespace. These, as well as the XSL-defined properties, are made available to the processor of the content of the flow object. Their semantics are defined by that namespace.

## Properties

| Property | Inherited | Conformance Level |
|----------|-----------|-------------------|
| Common Accessibility Properties | N/A | Basic |
| Common Aural Properties | N/A | Extended |
| Common Border, Padding, and Background Properties | No | Basic |
| Common Margin Properties-Inline | No | Basic |
| Common Relative Position Properties | No | Extended |
| alignment-adjust | No | Extended |
| alignment-baseline | No | Extended |
| allowed-height-scale | No | Extended |
| allowed-width-scale | No | Extended |
| baseline-shift | No | Extended |
| block-progression-dimension | No | Extended |
| clip | No | Extended |
| content-height | No | Basic |
| content-type | No | Basic |
| content-width | No | Basic |
| display-align | No | Extended |
| dominant-baseline | No | Extended |
| height | No | Basic |
| id | No | Basic |
| index-class | No | Extended |
| index-key | No | Extended |
| inline-progression-dimension | No | Extended |
| keep-with-next | No | Extended |
| keep-with-previous | No | Extended |
| line-height | Yes | Basic |
| overflow | No | Extended |
| scaling | No | Basic |
| scaling-method | No | Extended |
| text-align | Yes | Basic |
| width | No | Basic |

## Usage Notes

- The inline-level area uses the large-allocation-rectangle as defined in the area model.
- The viewport size is determined by the block-progression-dimension and inline-progression-dimension traits. For values of "auto", the content size of the instream foreign object is used.
- The content size is determined by taking the intrinsic size of the object and scaling as specified by the content-height, content-width, scaling, allowed-height-scale, and allowed-width-scale traits. If one of content-height or content-width is not "auto", the same scale factor (as calculated from the specified non-auto value) is applied equally to both directions.
- Once scaled, the reference-area is aligned with respect to the viewport-area using the text-align and display-align traits. If the object is too large for the viewport-area, it is aligned as if it would fit and the overflow trait controls the clipping, scroll bars, etc.
- In the case when the instream-foreign-object does not specify an intrinsic size, the size is determined in an implementation-defined manner.
- Unlike fo:external-graphic which references external data via the src property, fo:instream-foreign-object contains its data inline as child elements (typically SVG, MathML, or other XML namespaces).

## Code Samples

No code samples in spec for this formatting object.

## See Also

- fo:external-graphic -- for graphics where the data resides outside the FO tree
- fo:block -- used to wrap fo:instream-foreign-object for block-level placement
