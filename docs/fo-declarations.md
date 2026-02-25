# fo:declarations

## Summary

The `fo:declarations` formatting object is used to group global declarations for a stylesheet. It serves as a container for document-wide declarations such as color profiles.

## Areas

The `fo:declarations` formatting object does not generate or return any areas.

## Constraints

None.

## Content Model

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_declarations -->
```xml
(color-profile)*
```

The `fo:declarations` may contain zero or more `fo:color-profile` children. It may also have additional child elements in a non-XSL namespace. The presence of non-XSL namespace elements does not change the semantics of the XSL namespace objects and properties. The permitted structure of these non-XSL namespace elements is defined for their namespace(s).

## Properties

The `fo:declarations` formatting object has no properties defined in the spec. It is a structural container only.

## Usage Notes

The `fo:declarations` element is an optional child of `fo:root`. When present, it must appear after the first `fo:layout-master-set` and before the `fo:bookmark-tree` (if any) and any `fo:page-sequence` elements.

Its primary purpose is to hold `fo:color-profile` declarations that define ICC Color Profiles for use throughout the stylesheet. Color profiles declared here can be referenced elsewhere in the document via the `rgb-icc()` function.

The ability to include non-XSL namespace elements makes `fo:declarations` extensible for processor-specific global declarations.

## Code Samples

No code samples in spec for this formatting object. The spec section contains only the content model declaration shown above.

## See Also

- fo:root -- parent element that contains fo:declarations
- fo:color-profile -- child element for declaring ICC Color Profiles
