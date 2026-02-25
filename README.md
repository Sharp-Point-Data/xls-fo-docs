# XSL-FO Documentation

Developer-friendly documentation for XSL Formatting Objects (XSL-FO), the W3C XML vocabulary for generating PDF and other paginated output from XML data.

XSL-FO is used in a two-step workflow: an XSLT stylesheet transforms XML source into an XSL-FO document, then an XSL-FO processor (Apache FOP, RenderX XEP, or Antenna House) renders it to PDF.

## Quick Start

```xml
<?xml version="1.0" encoding="utf-8"?>
<fo:root xmlns:fo="http://www.w3.org/1999/XSL/Format">

  <fo:layout-master-set>
    <fo:simple-page-master master-name="A4"
        page-height="297mm" page-width="210mm"
        margin-top="20mm" margin-bottom="20mm"
        margin-left="25mm" margin-right="25mm">
      <fo:region-body margin-bottom="15mm"/>
      <fo:region-after extent="10mm"/>
    </fo:simple-page-master>
  </fo:layout-master-set>

  <fo:page-sequence master-reference="A4">
    <fo:static-content flow-name="xsl-region-after">
      <fo:block text-align="center">Page <fo:page-number/></fo:block>
    </fo:static-content>
    <fo:flow flow-name="xsl-region-body">
      <fo:block font-size="18pt" font-weight="bold">Hello, XSL-FO</fo:block>
      <fo:block font-size="12pt">Body text goes here.</fo:block>
    </fo:flow>
  </fo:page-sequence>

</fo:root>
```

Render with Apache FOP:

```bash
fop -fo myfile.fo -pdf output.pdf
```

## Documentation

| File | Contents |
|------|----------|


## Document Structure

```
fo:root
  fo:layout-master-set
    fo:simple-page-master
      fo:region-body
      fo:region-before  (header)
      fo:region-after   (footer)
      fo:region-start   (left margin)
      fo:region-end     (right margin)
    fo:page-sequence-master  (optional: alternating pages)
  fo:bookmark-tree           (optional: PDF bookmarks)
  fo:page-sequence
    fo:static-content        (headers/footers)
    fo:flow
      fo:block               (paragraphs, headings)
      fo:table               (tables)
      fo:list-block          (lists)
```

## Required Namespace

All XSL-FO elements use the namespace `http://www.w3.org/1999/XSL/Format`, declared with the `fo:` prefix:

```xml
<fo:root xmlns:fo="http://www.w3.org/1999/XSL/Format">
```

## Key Processors

| Processor | License | Website |
|-----------|---------|---------|
| Apache FOP | Open Source (Apache 2.0) | https://xmlgraphics.apache.org/fop/ |
| RenderX XEP | Commercial | https://www.renderx.com/ |
| Antenna House Formatter | Commercial | https://www.antennahouse.com/ |

## Source Specification

This documentation is based on the W3C XSL-FO 2.0 specification.
