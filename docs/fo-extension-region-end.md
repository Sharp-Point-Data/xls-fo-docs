# fo:extension-region-end

## Summary

The `fo:extension-region-end` formatting object is used to define a rectangular region that extends from the `fo:region-body` along the "end" direction to contain `fo:marginalia`, if they exist. This is an XSL-FO 2.0 addition for marginalia support.

The `fo:extension-region-end` region specifies a viewport/reference pair that is located on the "end" side of the region-body. The before-edge of this region is aligned with the before-edge of the region-body and the start-edge of this region is parallel to the end-edge of the region-body, at a distance specified by the `distance` attribute.

The extent in the inline-direction of the extension-region is indicated in the `extent` attribute of the `fo:extension-region-end` declaration, while the block-dimension of the area is the same as the region-body.

The `fo:extension-region-end` also defines other properties of the region such as border, padding, background, etc.

It is an error if a marginalia is contained in a page whose `fo:simple-page-master` does not contain any `fo:extension-region-start` or `fo:extension-region-end` declarations.

## Areas

The extension-region-end specifies a viewport/reference pair that is located on the "end" side of the region-body. The before-edge of this region is aligned with the before-edge of the region-body and the start-edge of this region is parallel to the end-edge of the region-body, at a distance specified by the `distance` attribute.

## Content Model

```
Empty.
```

The `fo:extension-region-end` has no children. It is an empty element whose properties configure the region.

## Properties

| Property | Type | Inherited | Conformance Level |
|---|---|---|---|
| extent | \<length\> | No | Extended |
| distance | \<length\> | No | Extended |

The `fo:extension-region-end` also supports border, padding, and background properties as noted in the spec.

## Constraints

None.

## Usage Notes

- The `fo:extension-region-end` is declared as a child of `fo:simple-page-master`, alongside the standard region declarations (`fo:region-body`, `fo:region-before`, etc.).
- The `extent` property specifies the inline-direction size of the marginalia region.
- The `distance` property specifies the gap between the start-edge of the extension-region and the end-edge of the region-body.
- This region is specifically designed for marginalia content. Marginalia placed in the flow will be rendered in this region when it exists.
- The block-dimension of the extension-region matches the block-dimension of the region-body.

## Code Samples

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_extension-region-end -->
```xml
Empty.
```

## See Also

- `fo:simple-page-master` -- parent formatting object that contains region definitions
- `fo:extension-region-start` -- the corresponding extension region on the start side
- `fo:region-body` -- the central content region adjacent to this extension region
- `fo:region-end` -- the standard end-side region (distinct from this extension region)
- `fo:marginalia` -- the formatting object for marginalia content assigned to extension regions
