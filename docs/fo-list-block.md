# fo:list-block

## Summary

The `fo:list-block` formatting object is used to format a list. It generates one or more normal block-areas containing the list items. Each child `fo:list-item` provides one item in the list.

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_list-block -->

## Areas

The `fo:list-block` formatting object generates one or more normal block-areas. The `fo:list-block` returns these areas, any page-level-out-of-line areas, and any reference-level-out-of-line areas returned by the children of the `fo:list-block`.

## Constraints

- No area may have more than one normal child area returned by the same `fo:list-block` formatting object.
- The children of each normal area returned by an `fo:list-block` formatting object must be normal block-areas returned by the children of the `fo:list-block`, must be properly stacked, and must be properly ordered.

## Content Model

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_list-block -->
```xml
(list-item+)
```

In addition this formatting object may have a sequence of zero or more `fo:marker`s as its initial children.

## Properties

| Property | Inherited | Conformance Level |
|---|---|---|
| Common Accessibility Properties | N/A | Basic |
| Common Aural Properties | N/A | Extended |
| Common Border, Padding, and Background Properties | N/A | Basic |
| Common Margin Properties - Block | N/A | Basic |
| Common Relative Position Properties | N/A | Extended |
| `break-after` | no | Basic |
| `break-before` | no | Basic |
| `clear` | no | Extended |
| `id` | N/A | Basic |
| `index-class` | N/A | Extended |
| `index-key` | N/A | Extended |
| `intrusion-displace` | yes | Extended |
| `keep-together` | no | Extended |
| `keep-with-next` | no | Extended |
| `keep-with-previous` | no | Extended |
| `provisional-distance-between-starts` | yes | Basic |
| `provisional-label-separation` | yes | Basic |

## Usage Notes

- The `fo:list-block` is the top-level container for lists. It must contain one or more `fo:list-item` children.
- The `provisional-distance-between-starts` property controls the distance from the start-edge of the list-item-label to the start-edge of the list-item-body. This is typically used to set consistent indentation for list item content.
- The `provisional-label-separation` property controls the minimum gap between the end of the label and the start of the body content.
- Use `keep-together`, `keep-with-next`, and `keep-with-previous` to control page/column breaks within and around the list.
- The list-block itself does not define whether items are numbered, bulleted, or labeled; that is determined by the content placed in each `fo:list-item-label`.

## Code Samples

The following three-part example demonstrates an ordered list transformed from source XML to XSL-FO using `fo:list-block`, with `provisional-distance-between-starts` and `provisional-label-separation` controlling list layout, and `label-end()`/`body-start()` functions for label and body indentation.

Source XML ordered list:

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_conditional-table-footer-reference -->
```xml
<ol>
<item>List item 1.</item>
<item>List item 2.</item>
<item>List item 3.</item>
</ol>
```

XSLT stylesheet transforming the ordered list into `fo:list-block` with `fo:list-item` children. Uses `label-end()` and `body-start()` to set indentation, and `xsl:number` for automatic label generation:

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_conditional-table-footer-reference -->
```xml
<?xml version='1.0'?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
                xmlns:fo="http://www.w3.org/1999/XSL/Format"
                version='1.0'>

<xsl:template match="ol">
  <fo:list-block provisional-distance-between-starts="15mm"
   provisional-label-separation="5mm">
    <xsl:apply-templates/>
  </fo:list-block>
</xsl:template>

<xsl:template match="ol/item">
  <fo:list-item>
    <fo:list-item-label start-indent="5mm" end-indent="label-end()">
      <fo:block>
        <xsl:number format="a."/>
      </fo:block>
    </fo:list-item-label>
    <fo:list-item-body start-indent="body-start()">
      <fo:block>
        <xsl:apply-templates/>
      </fo:block>
    </fo:list-item-body>
  </fo:list-item>
</xsl:template>

</xsl:stylesheet>
```

Resulting XSL-FO output with `fo:list-block` containing three `fo:list-item` elements, each with a label (a., b., c.) and body:

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_conditional-table-footer-reference -->
```xml
<fo:list-block provisional-distance-between-starts="15mm"
  provisional-label-separation="5mm">

  <fo:list-item>
    <fo:list-item-label start-indent="5mm" end-indent="label-end()">
      <fo:block>a.
      </fo:block>
    </fo:list-item-label>
    <fo:list-item-body start-indent="body-start()">
      <fo:block>List item 1.
      </fo:block>
    </fo:list-item-body>
  </fo:list-item>

  <fo:list-item>
    <fo:list-item-label start-indent="5mm" end-indent="label-end()">
      <fo:block>b.
      </fo:block>
    </fo:list-item-label>
    <fo:list-item-body start-indent="body-start()">
      <fo:block>List item 2.
      </fo:block>
    </fo:list-item-body>
  </fo:list-item>

  <fo:list-item>
    <fo:list-item-label start-indent="5mm" end-indent="label-end()">
      <fo:block>c.
      </fo:block>
    </fo:list-item-label>
    <fo:list-item-body start-indent="body-start()">
      <fo:block>List item 3.
      </fo:block>
    </fo:list-item-body>
  </fo:list-item>

</fo:list-block>
```

## See Also

- `fo:list-item` -- child formatting object containing label and body for each list entry
- `fo:list-item-label` -- contains the label content (bullet, number, etc.)
- `fo:list-item-body` -- contains the body content of a list item
