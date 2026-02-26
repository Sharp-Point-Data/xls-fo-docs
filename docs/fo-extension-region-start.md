# fo:extension-region-start

## Summary

The `fo:extension-region-start` formatting object is used to define a rectangular region that extends from the `fo:region-body` along the "start" direction to contain marginalia, if they exist. This is an XSL-FO 2.0 addition for marginalia support.

The extension-region-start specifies a viewport/reference pair that is located on the "start" side of the region-body. The before-edge of the extension-region is aligned with the before-edge of the region-body, and the end-edge of this region is parallel to the start-edge of the region-body, at a distance specified by the `distance` attribute.

The extent in the inline-direction of the extension-region is indicated in the `extent` attribute of the `fo:extension-region-start` declaration, while the block-dimension of the area is the same as the region-body.

The `fo:extension-region-start` also defines other properties of the region such as border, padding, background, etc.

It is an error if a marginalia is contained in a page whose `fo:simple-page-master` does not contain any `fo:extension-region-start` or `fo:extension-region-end` declarations.

## Areas

The extension-region-start specifies a viewport/reference pair that is located on the "start" side of the region-body, meaning that the before-edge of the extension-region is aligned with the before-edge of the region-body and the end-edge of this region is parallel to the start-edge of the region-body, at a distance specified by the `distance` attribute.

## Content Model

```
Empty.
```

The `fo:extension-region-start` has no children. It is an empty element whose properties configure the region.

## Properties

| Property | Type | Inherited | Conformance Level |
|---|---|---|---|
| extent | \<length\> | No | Extended |
| distance | \<length\> | No | Extended |

The `fo:extension-region-start` also supports border, padding, and background properties as noted in the spec.

## Constraints

None.

## Usage Notes

- The `fo:extension-region-start` is declared as a child of `fo:simple-page-master`, alongside the standard region declarations (`fo:region-body`, `fo:region-before`, etc.).
- The `extent` property specifies the inline-direction size of the marginalia region.
- The `distance` property specifies the gap between the end-edge of the extension-region and the start-edge of the region-body.
- This region is specifically designed for marginalia content. Marginalia placed in the flow will be rendered in this region when it exists.
- The block-dimension of the extension-region matches the block-dimension of the region-body.

## Code Samples

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_extension-region-start -->
```xml
Empty.
```

## See Also

- [fo:simple-page-master](fo-simple-page-master.md) — parent formatting object that contains region definitions
- [fo:extension-region-end](fo-extension-region-end.md) — the corresponding extension region on the end side
- [fo:region-body](fo-region-body.md) — the central content region adjacent to this extension region
- [fo:region-start](fo-region-start.md) — the standard start-side region (distinct from this extension region)
- [fo:marginalia](fo-marginalia.md) — the formatting object for marginalia content assigned to extension regions
