# XSL-FO Documentation for Context7

Developer-friendly XSL-FO documentation structured for LLM consumption via [Context7](https://context7.com). Covers the W3C XSL-FO 2.0 specification and Antenna House Formatter extensions.

XSL-FO is the W3C XML vocabulary for generating PDF and other paginated output from XML data. An XSLT stylesheet transforms XML source into an XSL-FO document, then a processor (Apache FOP, RenderX XEP, or Antenna House Formatter) renders it to PDF, PostScript, or other formats.

## Accuracy Warning

**This documentation was extracted and organized with LLM assistance.** While code samples from the source materials were preserved verbatim wherever possible, errors in extraction, summarization, or attribution may exist. This documentation is provided as-is with no guarantee of correctness.

**Do not treat this as a substitute for the authoritative sources.** Always verify against:
- The [W3C XSL-FO 2.0 specification](https://www.w3.org/TR/xslfo20/) for core FO content
- The [Antenna House Formatter documentation](https://www.antenna.co.jp/AHF/help/en/index.html) for extension content

If you find an error, please [open an issue](https://github.com/Sharp-Point-Data/xls-fo-docs/issues).

## Start Here

| If you want to... | Read this |
|--------------------|-----------|
| Understand what XSL-FO is | [Introduction and Overview](docs/guide-introduction.md) |
| Learn how formatting works | [Introduction to Formatting](docs/guide-formatting-intro.md) |
| See every FO at a glance | [Formatting Object Summary](docs/ref-fo-summary.md) |
| See every property at a glance | [Property Summary](docs/ref-property-summary.md) |
| Build a basic page | [fo:root](docs/fo-root.md) → [fo:simple-page-master](docs/fo-simple-page-master.md) → [fo:page-sequence](docs/fo-page-sequence.md) → [fo:flow](docs/fo-flow.md) → [fo:block](docs/fo-block.md) |
| Work with tables | [fo:table](docs/fo-table.md) and [Advanced Table Layouts](docs/guide-tables-advanced.md) |
| Use keeps and breaks | [Keeps and Breaks Guide](docs/guide-keeps-breaks.md) and [Keeps and Breaks Properties](docs/properties-keeps-breaks.md) |
| Browse all 216 docs | [Documentation Index](docs/README.md) |

## What's in This Repo

216 documentation files covering:

| Category | Count | Prefix | Description |
|----------|------:|--------|-------------|
| Formatting Objects | 103 | `fo-` | Every FO from the W3C spec — `fo:block`, `fo:table`, `fo:page-sequence`, etc. |
| Properties | 30 | `properties-` | W3C property groups — fonts, borders, pagination, keeps/breaks, etc. |
| Guides | 19 | `guide-` | Conceptual docs — area model, writing modes, XSLT integration, etc. |
| Reference | 4 | `ref-` | Summary tables and conformance info |
| AHF Extension FOs | 23 | `ahf-fo-` | Antenna House extension formatting objects |
| AHF Extension Properties | 25 | `ahf-properties-` | Antenna House extension property groups |
| AHF Configuration | 10 | `ahf-config-` | Antenna House Formatter configuration settings |
| AHF Functions | 1 | `ahf-functions` | Antenna House extension XPath functions |

## Data Sources

All documentation in this repo was derived from two sources.

### W3C XSL-FO 2.0 Specification

The primary source is `xslspec.xml`, the W3C XSL-FO 2.0 specification in XML form. This is the authoritative standard for XSL Formatting Objects. All `fo-*`, `properties-*`, `guide-*`, and `ref-*` files are derived from this source.

- Specification: https://www.w3.org/TR/xslfo20/
- Code samples in docs include `<!-- Source: ... -->` comments linking back to the spec section or XML line number

### Antenna House Formatter v7.4 Reference Guide

The secondary source is the Antenna House XSL-FO Reference Guide v7.4 (PDF), which documents Antenna House Formatter's proprietary extensions to the XSL-FO standard. Antenna House publishes this documentation freely on their website.

- Online docs: https://www.antenna.co.jp/AHF/help/en/index.html
- Code samples in docs include `<!-- Source: XSL-FO-Reference-74-MID.pdf p.NNN -->` comments referencing the PDF page number

## Core XSL-FO vs. Antenna House Extensions

This is the most important distinction in this repo.

### Core XSL-FO (files without `ahf-` prefix)

Standard W3C XSL-FO that works across **all** compliant processors: Apache FOP, RenderX XEP, Antenna House Formatter, and others. If you are writing XSL-FO and don't know what processor will be used, **use only core content**.

### Antenna House Extensions (files with `ahf-` prefix)

Proprietary extensions that **only work with Antenna House Formatter**. These cover features not in the W3C spec: PDF form fields, advanced float control, spread pages, CJK typography, PDF annotations, and more.

**Use the `ahf-` docs when:**
- You are targeting Antenna House Formatter specifically
- You need a feature not covered by the W3C spec (e.g., PDF forms, advanced footnote numbering, spread page masters)
- You are configuring Antenna House Formatter itself (`ahf-config-*` files)

**Do not use the `ahf-` docs when:**
- You need output to work with Apache FOP or RenderX XEP
- You are writing processor-agnostic XSL-FO
- You are unsure which processor will render the document

Antenna House extensions use a separate namespace (`xmlns:axf="http://www.antennahouse.com/names/XSL/Extensions"`) which will be ignored or cause errors in other processors. This project is not affiliated with Antenna House; the extension documentation was created from their publicly available reference materials under a usage license.

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

## Repository Layout

```
docs/
  fo-*.md                  W3C formatting objects (one file per FO)
  properties-*.md          W3C property groups
  guide-*.md               Conceptual guides and explanations
  ref-*.md                 Reference summaries
  ahf-fo-*.md              Antenna House extension FOs
  ahf-properties-*.md      Antenna House extension properties
  ahf-config-*.md          Antenna House Formatter configuration
  ahf-functions.md         Antenna House extension functions
inventory/                   Source extraction artifacts and section inventories
  sections.json              W3C spec section inventory
  samples.json               Code sample index (compact)
  samples-full.json          Code sample index (full text)
  summary.txt                Spec structure summary
  file-mapping.json          Maps spec sections to output doc files
  parsed_ext_props.json      Parsed Antenna House extension properties
  config_*.txt               Extracted AHF configuration sections
  group_*.txt                Extracted AHF property groups
  pdf_*.txt                  Extracted AHF spec content
context7.json                Context7 library configuration
```

## XSL-FO Processors

| Processor | License | Website |
|-----------|---------|---------|
| Apache FOP | Open Source (Apache 2.0) | https://xmlgraphics.apache.org/fop/ |
| Antenna House Formatter | Commercial | https://www.antennahouse.com/ |

## License

See [LICENSE](LICENSE).

---

Maintained by Sharp Point Data LTD.
