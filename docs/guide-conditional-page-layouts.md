# Conditional Page Layouts and Dynamic Regions

## Overview

XSL-FO provides a powerful mechanism for implementing conditional page layouts where different sections of a document require different master pages. The `fo:page-sequence-master` with `fo:repeatable-page-master-alternatives` and `fo:conditional-page-master-reference` elements form a state machine that selects the appropriate page-master for each page based on its position (first, last, rest), parity (odd/even), and blank status.

This guide covers:
- Defining multiple page-masters with different region configurations
- Using conditional page-master references to select layouts per page
- Managing region-before and region-after heights across different page-masters
- Common patterns for book-style, report, and multi-section documents

## Defining Multiple Page-Masters

Each `fo:simple-page-master` defines a complete page geometry including all regions. To have different layouts for different pages, define separate page-masters and reference them conditionally.

### Spec Example: Simple Page-Master with Regions

<!-- Source: xslspec.xml line 5725 -->
```xml
<fo:root>

<fo:layout-master-set>
  <fo:simple-page-master master-name="all-pages">
    <fo:region-body region-name="xsl-region-body" margin="0.75in"
                    writing-mode="tb-rl" />
    <fo:region-before region-name="xsl-region-before" extent="0.75in"/>
  </fo:simple-page-master>
  <fo:page-sequence-master master-name="default-sequence">
    <fo:repeatable-page-master-reference master-reference="all-pages"/>
  </fo:page-sequence-master>
</fo:layout-master-set>

<fo:page-sequence master-name="default-sequence">
  <fo:flow flow-name="xsl-region-body">
    <fo:block>
        [Content in a language which allows either
         horizontal or vertical formatting]
    </fo:block>
  </fo:flow>
</fo:page-sequence>

</fo:root>
```

This shows the basic pattern: a `fo:simple-page-master` defines the page geometry with its regions, a `fo:page-sequence-master` establishes the page selection sequence, and a `fo:page-sequence` references the master by name.

### Spec Example: Page-Master with Region-Body and Region-After

<!-- Source: xslspec.xml line 10510 -->
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

This demonstrates a complete document with `fo:region-after` used for a page footer containing `fo:page-number`, and `fo:region-body` with a bottom margin to make room for the footer region.

### Spec Example: Extension Regions with Simple-Page-Master

<!-- Source: xslspec.xml line 9395 -->
```xml
<fo:simple-page-master master-name="only"
      page-height="29.7cm"
      page-width="21cm"
      margin-top="1cm"
      margin-bottom="2cm"
      margin-left="2.5cm"
      margin-right="2.5cm">
      <fo:region-body margin-top="3cm" margin-bottom="1.5cm"
      margin-left="2cm" margin-right="2cm"/>
      <fo:extension-region-start extent="1cm" distance="0.5cm"/>
      <fo:extension-region-end extent="1cm" distance="0.5cm"/>
      <fo:region-before precedence="true" extent="3cm"/>
      <fo:region-after precedence="true" extent="1.5cm"/>
      <fo:region-start extent="1cm"/>
      <fo:region-end extent="1cm"/>
      </fo:simple-page-master>
```

This shows a page-master with all seven region types including the XSL-FO 2.0 extension regions for marginalia. Note the `precedence="true"` on `fo:region-before` and `fo:region-after`, which means they extend to the full page width rather than being bounded by the side regions.

## Conditional Page-Master Selection

The `fo:conditional-page-master-reference` element selects a page-master based on three conditions that must all be true:

- **page-position**: `first` | `last` | `only` | `rest` | `any` | or a number (position in sequence or cycle)
- **odd-or-even**: `odd` | `even` | `any`
- **blank-or-not-blank**: `blank` | `not-blank` | `any`

The conditions are evaluated against each page as it is generated. Only the subset of conditions with specified values must match — unspecified conditions default to `any` (always true).

### Constructed Example: Book Chapter Layout with Different First, Odd, and Even Pages

**Note: This is a constructed example, not from the spec.**

```xml
<fo:layout-master-set>
  <!-- First page of chapter: no header, large top margin -->
  <fo:simple-page-master master-name="chapter-first"
      page-height="11in" page-width="8.5in"
      margin-top="2in" margin-bottom="1in"
      margin-left="1.25in" margin-right="1in">
    <fo:region-body margin-bottom="0.5in"/>
    <fo:region-after extent="0.4in"/>
  </fo:simple-page-master>

  <!-- Odd (recto) pages: header with chapter title on right -->
  <fo:simple-page-master master-name="chapter-odd"
      page-height="11in" page-width="8.5in"
      margin-top="1in" margin-bottom="1in"
      margin-left="1.25in" margin-right="1in">
    <fo:region-body margin-top="0.5in" margin-bottom="0.5in"/>
    <fo:region-before extent="0.4in" region-name="header-odd"/>
    <fo:region-after extent="0.4in" region-name="footer-odd"/>
  </fo:simple-page-master>

  <!-- Even (verso) pages: header with book title on left -->
  <fo:simple-page-master master-name="chapter-even"
      page-height="11in" page-width="8.5in"
      margin-top="1in" margin-bottom="1in"
      margin-left="1in" margin-right="1.25in">
    <fo:region-body margin-top="0.5in" margin-bottom="0.5in"/>
    <fo:region-before extent="0.4in" region-name="header-even"/>
    <fo:region-after extent="0.4in" region-name="footer-even"/>
  </fo:simple-page-master>

  <!-- Blank pages inserted for parity -->
  <fo:simple-page-master master-name="chapter-blank"
      page-height="11in" page-width="8.5in"
      margin-top="1in" margin-bottom="1in"
      margin-left="1in" margin-right="1in">
    <fo:region-body/>
  </fo:simple-page-master>

  <!-- Page-sequence-master with conditional selection -->
  <fo:page-sequence-master master-name="chapter-master">
    <fo:repeatable-page-master-alternatives>
      <fo:conditional-page-master-reference
          master-reference="chapter-blank"
          blank-or-not-blank="blank"/>
      <fo:conditional-page-master-reference
          master-reference="chapter-first"
          page-position="first"/>
      <fo:conditional-page-master-reference
          master-reference="chapter-even"
          odd-or-even="even"/>
      <fo:conditional-page-master-reference
          master-reference="chapter-odd"
          odd-or-even="odd"/>
    </fo:repeatable-page-master-alternatives>
  </fo:page-sequence-master>
</fo:layout-master-set>

<!-- Each chapter uses the same master with its own static content -->
<fo:page-sequence master-reference="chapter-master"
    force-page-count="even">
  <fo:static-content flow-name="header-odd">
    <fo:block text-align="end" font-size="9pt" font-style="italic">
      <fo:retrieve-marker retrieve-class-name="chapter-title"/>
    </fo:block>
  </fo:static-content>
  <fo:static-content flow-name="header-even">
    <fo:block text-align="start" font-size="9pt" font-style="italic">
      Book Title Here
    </fo:block>
  </fo:static-content>
  <fo:static-content flow-name="footer-odd">
    <fo:block text-align="end" font-size="9pt">
      <fo:page-number/>
    </fo:block>
  </fo:static-content>
  <fo:static-content flow-name="footer-even">
    <fo:block text-align="start" font-size="9pt">
      <fo:page-number/>
    </fo:block>
  </fo:static-content>
  <fo:flow flow-name="xsl-region-body">
    <fo:block>
      <fo:marker marker-class-name="chapter-title">Introduction</fo:marker>
      Chapter content here...
    </fo:block>
  </fo:flow>
</fo:page-sequence>
```

**Key points about conditional evaluation order:**
1. Conditions are evaluated in document order. The first `fo:conditional-page-master-reference` whose conditions are all true is selected.
2. Place more specific conditions before less specific ones. The `blank` condition is checked first because a blank page that is also even would incorrectly match the even-page condition otherwise.
3. `force-page-count="even"` on `fo:page-sequence` ensures each chapter ends on an even page, which may generate blank pages that the `blank-or-not-blank="blank"` condition handles.

## Managing Region Heights Dynamically

XSL-FO does not support truly dynamic region heights that adjust automatically based on content. Region dimensions (`extent` for side regions, or margins on `fo:region-body`) are fixed values set on the page-master. However, there are several strategies for handling varying region height requirements.

### Strategy 1: Multiple Page-Masters with Different Region Sizes

Define separate page-masters for each region height configuration and use conditional selection.

**Note: This is a constructed example, not from the spec.**

```xml
<fo:layout-master-set>
  <!-- Pages with a tall header (e.g., first page with logo and address block) -->
  <fo:simple-page-master master-name="page-tall-header"
      page-height="11in" page-width="8.5in"
      margin="1in">
    <fo:region-body margin-top="2in" margin-bottom="0.75in"/>
    <fo:region-before extent="1.8in" region-name="header-tall"/>
    <fo:region-after extent="0.5in"/>
  </fo:simple-page-master>

  <!-- Pages with a short header (e.g., continuation pages) -->
  <fo:simple-page-master master-name="page-short-header"
      page-height="11in" page-width="8.5in"
      margin="1in">
    <fo:region-body margin-top="0.75in" margin-bottom="0.75in"/>
    <fo:region-before extent="0.5in" region-name="header-short"/>
    <fo:region-after extent="0.5in"/>
  </fo:simple-page-master>

  <fo:page-sequence-master master-name="letter-master">
    <fo:repeatable-page-master-alternatives>
      <fo:conditional-page-master-reference
          master-reference="page-tall-header"
          page-position="first"/>
      <fo:conditional-page-master-reference
          master-reference="page-short-header"
          page-position="rest"/>
    </fo:repeatable-page-master-alternatives>
  </fo:page-sequence-master>
</fo:layout-master-set>

<fo:page-sequence master-reference="letter-master">
  <fo:static-content flow-name="header-tall">
    <fo:block space-after="12pt">
      <fo:external-graphic src="logo.png" content-height="0.75in"/>
    </fo:block>
    <fo:block font-size="10pt">Company Name</fo:block>
    <fo:block font-size="10pt">123 Main Street</fo:block>
    <fo:block font-size="10pt">City, State 12345</fo:block>
  </fo:static-content>
  <fo:static-content flow-name="header-short">
    <fo:block font-size="9pt" text-align="end" font-style="italic">
      Company Name — Page <fo:page-number/>
    </fo:block>
  </fo:static-content>
  <fo:static-content flow-name="xsl-region-after">
    <fo:block font-size="8pt" text-align="center">
      Confidential
    </fo:block>
  </fo:static-content>
  <fo:flow flow-name="xsl-region-body">
    <fo:block>Letter body content...</fo:block>
  </fo:flow>
</fo:page-sequence>
```

The `fo:region-body` margin-top must be large enough to accommodate the region-before `extent`. In the tall header case, `margin-top="2in"` accommodates `extent="1.8in"` with a small gap. The short header uses `margin-top="0.75in"` for `extent="0.5in"`.

### Strategy 2: Overflow and Clipping for Variable-Height Content

When region content may exceed the fixed region size, the `overflow` property controls behavior:

- `overflow="visible"` — Content extends beyond the region boundary (may overlap other regions).
- `overflow="hidden"` — Content is clipped at the region boundary.
- `overflow="scroll"` — Scrolling is available (relevant for interactive output, not print).
- `overflow="error-if-overflow"` — The processor reports an error if content overflows.
- `overflow="condense"` — The processor may reduce font size or spacing to fit content (XSL-FO 2.0).

**Note: This is a constructed example, not from the spec.**

```xml
<fo:simple-page-master master-name="variable-header-page"
    page-height="11in" page-width="8.5in" margin="1in">
  <fo:region-body margin-top="1.5in" margin-bottom="0.75in"/>
  <fo:region-before extent="1.25in" overflow="condense"
      display-align="after"/>
  <fo:region-after extent="0.5in"/>
</fo:simple-page-master>
```

Setting `display-align="after"` on `fo:region-before` aligns content to the bottom of the header region, so if content is shorter than the allocated space, it sits adjacent to the body region rather than floating at the top of the page.

### Strategy 3: Multiple Sections with Different Page-Sequences

Each `fo:page-sequence` can reference a different master. Use separate page-sequences for document sections that require fundamentally different layouts.

**Note: This is a constructed example, not from the spec.**

```xml
<fo:root>
  <fo:layout-master-set>
    <!-- Cover page: no headers or footers -->
    <fo:simple-page-master master-name="cover"
        page-height="11in" page-width="8.5in" margin="0in">
      <fo:region-body/>
    </fo:simple-page-master>

    <!-- TOC pages: small header, no footer -->
    <fo:simple-page-master master-name="toc-page"
        page-height="11in" page-width="8.5in" margin="1in">
      <fo:region-body margin-top="0.5in"/>
      <fo:region-before extent="0.4in"/>
    </fo:simple-page-master>

    <!-- Body pages: header and footer -->
    <fo:simple-page-master master-name="body-page"
        page-height="11in" page-width="8.5in" margin="1in">
      <fo:region-body margin-top="0.5in" margin-bottom="0.5in"/>
      <fo:region-before extent="0.4in"/>
      <fo:region-after extent="0.4in"/>
    </fo:simple-page-master>

    <!-- Landscape pages for wide tables -->
    <fo:simple-page-master master-name="landscape-page"
        page-height="8.5in" page-width="11in" margin="0.75in">
      <fo:region-body margin-top="0.5in" margin-bottom="0.5in"/>
      <fo:region-before extent="0.4in"/>
      <fo:region-after extent="0.4in"/>
    </fo:simple-page-master>
  </fo:layout-master-set>

  <!-- Section 1: Cover -->
  <fo:page-sequence master-reference="cover">
    <fo:flow flow-name="xsl-region-body">
      <fo:block-container absolute-position="fixed"
          top="4in" left="2in" width="4.5in">
        <fo:block font-size="28pt" text-align="center">
          Document Title
        </fo:block>
      </fo:block-container>
    </fo:flow>
  </fo:page-sequence>

  <!-- Section 2: Table of Contents -->
  <fo:page-sequence master-reference="toc-page"
      initial-page-number="1" format="i">
    <fo:static-content flow-name="xsl-region-before">
      <fo:block font-size="9pt" text-align="center">Table of Contents</fo:block>
    </fo:static-content>
    <fo:flow flow-name="xsl-region-body">
      <fo:block>TOC entries here...</fo:block>
    </fo:flow>
  </fo:page-sequence>

  <!-- Section 3: Body Content -->
  <fo:page-sequence master-reference="body-page"
      initial-page-number="1" format="1">
    <fo:static-content flow-name="xsl-region-before">
      <fo:block font-size="9pt" border-bottom="0.5pt solid black">
        Document Title
      </fo:block>
    </fo:static-content>
    <fo:static-content flow-name="xsl-region-after">
      <fo:block font-size="9pt" text-align="center">
        Page <fo:page-number/>
      </fo:block>
    </fo:static-content>
    <fo:flow flow-name="xsl-region-body">
      <fo:block>Body content...</fo:block>
    </fo:flow>
  </fo:page-sequence>

  <!-- Section 4: Landscape appendix -->
  <fo:page-sequence master-reference="landscape-page">
    <fo:static-content flow-name="xsl-region-before">
      <fo:block font-size="9pt">Appendix A: Data Tables</fo:block>
    </fo:static-content>
    <fo:static-content flow-name="xsl-region-after">
      <fo:block font-size="9pt" text-align="end">
        Page <fo:page-number/>
      </fo:block>
    </fo:static-content>
    <fo:flow flow-name="xsl-region-body">
      <fo:block>Wide table content...</fo:block>
    </fo:flow>
  </fo:page-sequence>
</fo:root>
```

Each `fo:page-sequence` starts a new section with independent page numbering (via `initial-page-number` and `format`), and references the appropriate page-master for its layout requirements.

## Region Sizing Rules

The relationship between region `extent` values and `fo:region-body` margins is critical:

- `fo:region-before` occupies the top of the page. Its height is set by `extent`. The `fo:region-body` must have a `margin-top` at least equal to the `extent` to prevent overlap (unless overlap is intentional).
- `fo:region-after` occupies the bottom. Its height is set by `extent`. The `fo:region-body` must have a `margin-bottom` at least equal to the `extent`.
- `fo:region-start` and `fo:region-end` occupy the left/right sides (in lr-tb writing mode). Their widths are set by `extent`.
- The `precedence` property on `fo:region-before` and `fo:region-after` controls whether header/footer regions extend to the full page width (`precedence="true"`) or are bounded by the side regions (`precedence="false"`, the default).

If `fo:region-body` margins are smaller than the corresponding region `extent` values, the regions overlap. This may be desirable for watermarks or background elements, but generally the margins should equal or exceed the extents.

## Challenges and Limitations

1. **No dynamic region sizing.** Region dimensions are fixed per page-master. You cannot make a header "auto-size" to its content. The workaround is to define multiple page-masters with different region sizes and select conditionally, or use `overflow="condense"` (XSL-FO 2.0) to allow the processor to fit variable content.

2. **Conditional evaluation is per-page, not per-content.** The `fo:conditional-page-master-reference` selects based on page position/parity/blank status, not based on the content being placed. You cannot say "use this master when the header content is tall." Content-based layout variation must be handled at the XSLT level by generating different `fo:page-sequence` elements.

3. **Static content is per-page-sequence.** All pages within a single `fo:page-sequence` share the same set of `fo:static-content` elements. To have fundamentally different header/footer content, use different `region-name` values on each page-master's regions, and provide `fo:static-content` for each name.

4. **Sub-sequence exhaustion.** If all sub-sequence-specifiers in a `fo:page-sequence-master` are exhausted while flow content remains, it is an error. The last specifier should typically use `fo:repeatable-page-master-alternatives` (unbounded) to handle any number of remaining pages.

5. **Region-name coordination.** When using multiple page-masters with conditional selection, each master can assign different `region-name` values to its regions. The `fo:static-content` in the page-sequence targets regions by `flow-name`. If a region-name has no matching static-content, that region is empty on pages using that master. The default region-names are `xsl-region-before`, `xsl-region-after`, `xsl-region-start`, `xsl-region-end`, and `xsl-region-body`.

## See Also

- fo:page-sequence-master — container for sub-sequence-specifiers
- fo:simple-page-master — defines page geometry and regions
- fo:conditional-page-master-reference — conditional page-master selection
- fo:repeatable-page-master-alternatives — repeating conditional selection
- fo:repeatable-page-master-reference — repeating unconditional selection
- fo:single-page-master-reference — single-use page-master reference
- fo:region-before, fo:region-after — header and footer regions
- fo:region-body — main content region
- fo:static-content — content placed in non-body regions
- fo:page-sequence — references a master and contains flows
