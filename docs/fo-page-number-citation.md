# fo:page-number-citation

## Summary

The fo:page-number-citation is used to reference the page-number for the page containing the first normal area returned by the cited formatting object. It generates and returns a single normal inline-area. It may be used to provide the page-numbers in the table of contents, cross-references, and index entries.

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_page-number-citation -->

## Content Model

`EMPTY`

## Properties

| Property | Inherited | Conformance Level |
|----------|-----------|-------------------|
| Common Accessibility Properties | N/A | Basic |
| Common Aural Properties | N/A | Extended |
| Common Border, Padding, and Background Properties | No | Basic |
| Common Font Properties | Yes | Basic |
| Common Margin Properties-Inline | No | Basic |
| Common Relative Position Properties | No | Extended |
| alignment-adjust | No | Extended |
| alignment-baseline | No | Extended |
| baseline-shift | No | Extended |
| dominant-baseline | No | Extended |
| id | No | Basic |
| index-class | No | Extended |
| index-key | No | Extended |
| keep-with-next | No | Extended |
| keep-with-previous | No | Extended |
| letter-spacing | Yes | Basic |
| line-height | Yes | Basic |
| ref-id | No | Basic |
| score-spaces | Yes | Basic |
| text-altitude | No | Extended |
| text-decoration | No | Basic |
| text-depth | No | Extended |
| text-shadow | No | Extended |
| text-transform | Yes | Basic |
| visibility | Yes | Extended |
| word-spacing | Yes | Basic |
| wrap-option | Yes | Extended |

## Usage Notes

- The cited page is the page containing, as a descendant, the first normal area returned by the formatting object with an id trait matching the ref-id trait of the fo:page-number-citation (the referenced formatting object).
- The child areas of the generated inline-area are the same as the result of formatting the result-tree fragment defined in the fo:page-number specification, using the cited page as the reference-page and the fo:page-sequence that generated the cited-page as the reference-page-sequence.
- The ref-id property is required and must reference the id of another formatting object in the document.
- fo:page-number-citation is commonly used in table-of-contents entries together with fo:leader and fo:basic-link, and in cross-references within the body text.

## Code Samples

The following three-part example from the spec demonstrates how fo:page-number-citation is used for cross-references, showing the complete pipeline from source XML through XSLT to the resulting FO output.

### Source XML input with chapter references

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_alternative-copyfit-content -->
```xml
<!DOCTYPE doc SYSTEM "pgref.dtd">
<doc>
  <chapter id="x"><title>Chapter</title>
    <p>Text</p>
  </chapter>
  <chapter><title>Chapter</title>
    <p>For a description of X see <ref refid="x"/>.</p>
  </chapter>
</doc>
```

### XSLT stylesheet with fo:page-number-citation and fo:basic-link

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_alternative-copyfit-content -->
```xml
<?xml version='1.0'?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
                xmlns:fo="http://www.w3.org/1999/XSL/Format"
                version='1.0'>

<xsl:template match="doc">
  <fo:root>
    <fo:layout-master-set>
      <fo:simple-page-master master-name="page"
        page-height="297mm" page-width="210mm"
        margin-top="20mm" margin-bottom="10mm"
        margin-left="25mm" margin-right="25mm">
        <fo:region-body
          margin-top="0mm" margin-bottom="15mm"
          margin-left="0mm" margin-right="0mm"/>
        <fo:region-after extent="10mm"/>
      </fo:simple-page-master>
    </fo:layout-master-set>
    <fo:page-sequence master-reference="page">
      <fo:static-content flow-name="xsl-region-after">
        <fo:block>
          <xsl:text>Page </xsl:text>
          <fo:page-number/>
        </fo:block>
      </fo:static-content>
      <fo:flow flow-name="xsl-region-body">
        <xsl:apply-templates/>
      </fo:flow>
    </fo:page-sequence>
  </fo:root>
</xsl:template>

<xsl:template match="chapter/title">
  <fo:block id="{generate-id(.)}">
    <xsl:number level="multiple" count="chapter" format="1. "/>
    <xsl:apply-templates/>
  </fo:block>
</xsl:template>

<xsl:template match="p">
  <fo:block>
    <xsl:apply-templates/>
  </fo:block>
</xsl:template>

<xsl:template match="ref">
  <xsl:text>page </xsl:text>
  <fo:page-number-citation refid="{generate-id(id(@refid)/title)}"/>
</xsl:template>

</xsl:stylesheet>
```

### Resulting XSL-FO output

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_alternative-copyfit-content -->
```xml
<fo:root>
  <fo:layout-master-set>
    <fo:simple-page-master master-name="page"
      page-height="297mm" page-width="210mm"
      margin-top="20mm" margin-bottom="10mm"
      margin-left="25mm" margin-right="25mm">
      <fo:region-body margin-top="0mm" margin-bottom="15mm"
        margin-left="0mm" margin-right="0mm"/>
      <fo:region-after extent="10mm"/>
    </fo:simple-page-master>
  </fo:layout-master-set>
  <fo:page-sequence master-reference="page">
    <fo:static-content flow-name="xsl-region-after">
      <fo:block>Page <fo:page-number/>
      </fo:block>
    </fo:static-content>
    <fo:flow flow-name="xsl-region-body">
      <fo:block id="N5">1. Chapter</fo:block>
      <fo:block>Text</fo:block>
      <fo:block id="N13">2. Chapter</fo:block>
      <fo:block>For a description of X see page <fo:page-number-citation refid="N5"/>
      </fo:block>
    </fo:flow>
  </fo:page-sequence>
</fo:root>
```

## See Also

- fo:page-number -- for the current page number
- fo:page-number-citation-last -- for citing the last page containing areas from a formatting object
- fo:leader -- commonly used with fo:page-number-citation in TOC entries
- fo:basic-link -- for creating hyperlinks alongside page citations
