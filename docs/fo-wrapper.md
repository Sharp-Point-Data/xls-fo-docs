# fo:wrapper

## Summary

The `fo:wrapper` formatting object is used to specify inherited properties for a group of formatting objects. It acts as a "carrier" for inheritable properties that are utilized by its children, without generating any areas of its own (in most cases).

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_wrapper -->

## Areas

The `fo:wrapper` formatting object returns the sequence of areas created by concatenating the sequences of areas returned by each of the children of the `fo:wrapper`. If this sequence contains at least one normal area, or if the `id` and `index-key` properties are not specified on the `fo:wrapper`, then the `fo:wrapper` does not itself generate any areas.

If the sequence of areas returned to the `fo:wrapper` contains no normal areas, and the `id` or `index-key` property is specified on the `fo:wrapper`, then it additionally generates and returns one normal area with `inline-progression-dimension` and `block-progression-dimension` set to zero. This area is an inline-area except where this would violate the constraint (on some ancestor area) that an area's children are all block-areas or all inline-areas, but not a mixture. In that case the `fo:wrapper` must instead generate a block-area.

## Trait Derivation

Except for `id`, `index-class`, and `index-key`, the `fo:wrapper` has no properties that are directly used by it. However, it does serve as a carrier to hold inheritable properties that are utilized by its children.

## Constraints

- The order of concatenation of the sequences of areas returned by the children of the `fo:wrapper` is the same order as the children are ordered under the `fo:wrapper`.
- An `fo:wrapper` is only permitted to have children that would be permitted to be children of the parent of the `fo:wrapper`, with two exceptions:
  - An `fo:wrapper` may always have a sequence of zero or more `fo:marker`s as its initial children.
  - An `fo:wrapper` that is a child of an `fo:multi-properties` is only permitted to have children that would be permitted in place of the `fo:multi-properties`.
- This restriction applies recursively. For example an `fo:wrapper` that is a child of another `fo:wrapper` may only have children that would be permitted to be children of the parent `fo:wrapper`.

## Content Model

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_wrapper -->
```xml
(#PCDATA|%inline;|%block;)*
```

## Properties

| Property | Inherited | Conformance Level |
|---|---|---|
| `id` | N/A | Basic |
| `index-class` | N/A | Extended |
| `index-key` | N/A | Extended |

## Usage Notes

- The `fo:wrapper` is commonly used to set inheritable properties (such as `font-weight`, `font-family`, `color`, etc.) on a group of formatting objects without introducing an additional area in the area tree.
- When used within `fo:multi-properties`, the `fo:wrapper` applies merged properties via the `merge-property-values()` function to its descendants.
- The `fo:wrapper` can hold `fo:marker` children, making it useful as a point to associate index keys and markers with content.
- The content model is context-dependent: the `fo:wrapper` may only contain children that would be valid in its parent's position.
- When an `id` or `index-key` is specified but the wrapper has no content generating normal areas, a zero-sized area is generated to serve as an anchor point.

## Code Samples

The following three-part example from the spec demonstrates `fo:wrapper` used as a property inheritance carrier: the source XML, the XSLT stylesheet, and the resulting XSL-FO output.

**Source XML with emphasis and code markup elements:**

<!-- Source: xslspec.xml line 17269 -->
```xml
<doc>
<p>This is an <emph>important word</emph> in this
sentence that also refers to a <code>variable</code>.</p>
</doc>
```

**XSLT stylesheet using `fo:wrapper` to carry `font-weight` and `font-family` properties for inheritance by child text:**

<!-- Source: xslspec.xml line 17280 -->
```xml
<?xml version='1.0'?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
                xmlns:fo="http://www.w3.org/1999/XSL/Format"
                version='1.0'>

<xsl:template match="p">
  <fo:block>
    <xsl:apply-templates/>
  </fo:block>
</xsl:template>

<xsl:template match="emph">
  <fo:wrapper font-weight="bold">
    <xsl:apply-templates/>
  </fo:wrapper>
</xsl:template>

<xsl:template match="code">
  <fo:wrapper font-family="Courier">
    <xsl:apply-templates/>
  </fo:wrapper>
</xsl:template>

</xsl:stylesheet>
```

**Resulting XSL-FO output with `fo:wrapper` carrying `font-weight="bold"` and `font-family="Courier"` without generating any areas of its own:**

<!-- Source: xslspec.xml line 17307 -->
```xml
<fo:block xmlns:fo="http://www.w3.org/1999/XSL/Format">This is an
<fo:wrapper font-weight="bold">important word</fo:wrapper>
in this sentence that also refers to a
<fo:wrapper font-family="Courier">variable</fo:wrapper>.
</fo:block>
```

## See Also

- `fo:multi-properties` -- uses `fo:wrapper` as a child for applying merged property values
- `fo:marker` -- can be an initial child of `fo:wrapper`
- `fo:inline` -- an alternative for wrapping inline content with explicit area generation
