# fo:external-graphic

## Summary

The fo:external-graphic flow object is used for a graphic where the graphics data resides outside of the fo: element tree. It generates and returns one inline-level viewport-area and one reference-area containing the external graphic. The inline-level area uses the large-allocation-rectangle as defined in the area model.

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_external-graphic -->

## Content Model

`EMPTY`

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
| src | No | Basic |
| text-align | Yes | Basic |
| width | No | Basic |

## Usage Notes

- An fo:external-graphic may be placed block-level by enclosing it in an fo:block.
- A line-stacking-strategy of "max-height" or "line-height" is typically used for stacking one or more lines with fo:external-graphic content.
- The viewport size is determined by the block-progression-dimension and inline-progression-dimension traits. For values of "auto", the content size of the graphic is used.
- The content size of a graphic is determined by taking the intrinsic size of the graphic and scaling as specified by the content-height, content-width, scaling, allowed-height-scale, and allowed-width-scale traits. If one of content-height or content-width is not "auto", the same scale factor (as calculated from the specified non-auto value) is applied equally to both directions.
- Once scaled, the reference-area is aligned with respect to the viewport-area using the text-align and display-align traits. If the graphic is too large for the viewport-area, it is aligned as if it would fit and the overflow trait controls the clipping, scroll bars, etc.
- In the case when the graphics format does not specify an intrinsic size, the size is determined in an implementation-defined manner (for example, a size of 1/96" as the size of one pixel for rasterized images may be used).

## Code Samples

The following three-part example from the spec shows how fo:external-graphic is used to include an image with a caption.

### Source XML input with figure, photo, and caption elements

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_alternative-copyfit-content -->
```xml
<doc>
  <figure>
    <photo image="TH0317A.jpg"/>
    <caption>C'ieng Tamlung of C'ieng Mai</caption>
  </figure>
</doc>
```

### XSLT stylesheet using fo:external-graphic

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_alternative-copyfit-content -->
```xml
<?xml version='1.0'?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
                xmlns:fo="http://www.w3.org/1999/XSL/Format"
                version='1.0'>

<xsl:template match="figure">
  <fo:block>
    <xsl:apply-templates/>
  </fo:block>
</xsl:template>

<xsl:template match="photo">
  <fo:block text-align="center">
    <fo:external-graphic src="'url({@image})'"/>
  </fo:block>
</xsl:template>

<xsl:template match="caption">
  <fo:block space-before="3pt" text-align="center"
    start-indent="10mm" end-indent="10mm">
    <xsl:apply-templates/>
  </fo:block>
</xsl:template>

</xsl:stylesheet>
```

### Resulting XSL-FO output with fo:external-graphic

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_alternative-copyfit-content -->
```xml
<fo:block>
  <fo:block text-align="center">
    <fo:external-graphic src="'url(TH0317A.jpg)'"/>
  </fo:block>

  <fo:block space-before="3pt" text-align="center" start-indent="10mm"
    end-indent="10mm">C'ieng Tamlung of C'ieng Mai</fo:block>
</fo:block>
```

## See Also

- [fo:instream-foreign-object](fo-instream-foreign-object.md) — for inline graphics where data is embedded in the FO tree
- [fo:block](fo-block.md) — used to wrap fo:external-graphic for block-level placement
- [fo:scaling-value-citation](fo-scaling-value-citation.md) — to obtain the scale-factor applied to a cited fo:external-graphic
