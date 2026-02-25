# fo:page-sequence-wrapper

## Summary

The `fo:page-sequence-wrapper` formatting object is used to specify inherited properties for a group of `fo:page-sequence` formatting objects. It acts as a transparent wrapper that passes through inherited property values to its descendants without generating any areas of its own.

## Areas

The `fo:page-sequence-wrapper` formatting object does not generate any areas. It returns the sequence of areas created by concatenating the sequences of areas returned by each of its children.

## Trait Derivation

Except for `id`, `index-class`, and `index-key`, the `fo:page-sequence-wrapper` has no properties that are directly used by it. However, it does serve as a carrier to hold inheritable properties that are utilized by its children.

## Constraints

The order of concatenation of the sequences of areas returned by the children of the `fo:page-sequence-wrapper` is the same order as the children are ordered under the `fo:page-sequence-wrapper`. An `fo:page-sequence-wrapper` that contains no `fo:page-sequence` objects as descendants returns no areas.

Because an `fo:page-sequence-wrapper` that contains no `fo:page-sequence` objects as descendants returns no areas, any `id`, `index-key`, or `index-class` property on such an `fo:page-sequence-wrapper` is ignored; the result would be as if they were not assigned on this FO. In particular, any attempt to refer to this `id` would result in the same action as if this `id` were never declared within the FO result tree.

## Content Model

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_page-sequence-wrapper -->
```xml
(layout-master-set|page-sequence|page-sequence-wrapper)*
```

The `fo:page-sequence-wrapper` may contain zero or more children, each of which is an `fo:layout-master-set`, `fo:page-sequence`, or another `fo:page-sequence-wrapper`.

## Properties

| Property | Type | Initial Value | Inherited | Conformance Level |
|---|---|---|---|---|
| id | `<id>` | see prose | no | Basic |
| index-class | `<string>` | empty string | no | Extended |
| index-key | `<string>` | none | no | Extended |

In addition to these directly-used properties, the `fo:page-sequence-wrapper` can carry any inheritable properties. These inherited properties are not consumed by the wrapper itself but are passed through to its `fo:page-sequence` children and other descendants.

## Usage Notes

The `fo:page-sequence-wrapper` provides a mechanism to set inherited properties on a group of page-sequences without affecting the document structure. This is useful when multiple page-sequences share common property values such as `language`, `country`, `font-family`, or `color`.

The wrapper can appear as a child of `fo:root` or as a child of another `fo:page-sequence-wrapper`, allowing nesting. Since it is transparent to the area tree, it has no formatting semantics beyond property inheritance.

A common use case is setting a common language or writing direction for a group of chapters:

**Note:** The following is a constructed example, not from the spec.

```xml
<!-- Constructed example: using fo:page-sequence-wrapper for shared properties -->
<fo:page-sequence-wrapper language="en" country="US">
  <fo:page-sequence master-reference="chapter-layout">
    <fo:flow flow-name="xsl-region-body">
      <fo:block>Chapter 1 content...</fo:block>
    </fo:flow>
  </fo:page-sequence>
  <fo:page-sequence master-reference="chapter-layout">
    <fo:flow flow-name="xsl-region-body">
      <fo:block>Chapter 2 content...</fo:block>
    </fo:flow>
  </fo:page-sequence>
</fo:page-sequence-wrapper>
```

## Code Samples

No code samples in spec for this formatting object. The spec section contains only the content model declaration shown above.

## See Also

- fo:root -- parent element that may contain fo:page-sequence-wrapper
- fo:page-sequence -- the primary content-bearing child
- fo:layout-master-set -- may appear as a child within the wrapper
