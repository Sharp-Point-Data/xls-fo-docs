# PDF Bookmarks in XSL-FO

## Overview

XSL-FO provides three formatting objects for generating PDF bookmarks (also known as outlines or navigation trees):

- **`fo:bookmark-tree`** — Container for the entire bookmark hierarchy; child of `fo:root`.
- **`fo:bookmark`** — An individual bookmark entry with a link destination; can nest recursively.
- **`fo:bookmark-title`** — The human-readable label displayed in the bookmark panel.

Bookmarks appear as a hierarchical navigation panel in PDF viewers, allowing readers to jump directly to sections without scrolling through pages.

## Element Hierarchy

```
fo:root
└── fo:bookmark-tree
    ├── fo:bookmark (internal-destination="chapter1-id")
    │   ├── fo:bookmark-title → "Chapter 1: Introduction"
    │   ├── fo:bookmark (internal-destination="section1-1-id")
    │   │   └── fo:bookmark-title → "1.1 Background"
    │   └── fo:bookmark (internal-destination="section1-2-id")
    │       └── fo:bookmark-title → "1.2 Scope"
    └── fo:bookmark (internal-destination="chapter2-id")
        ├── fo:bookmark-title → "Chapter 2: Methods"
        └── ...
```

## Content Models

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_bookmark-tree -->
```xml
fo:bookmark-tree: (bookmark+)
```

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_bookmark -->
```xml
fo:bookmark: (bookmark-title, bookmark*)
```

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_bookmark-title -->
```xml
fo:bookmark-title: (#PCDATA)
```

No code samples in spec for bookmark usage. The spec contains only content model declarations and prose descriptions for these formatting objects.

## Properties

### fo:bookmark-tree

No specific properties. It serves only as a structural container.

### fo:bookmark

| Property | Values | Description |
|---|---|---|
| `internal-destination` | `<idref>` | References an `id` attribute within the same document. The bookmark navigates to the element with this ID. |
| `external-destination` | `<uri-specification>` | References an external resource (URL or file). |
| `starting-state` | `show` \| `hide` | Controls whether child bookmarks are initially expanded (`show`) or collapsed (`hide`) in the PDF viewer. Default: `show`. |

One of `internal-destination` or `external-destination` should be specified. If both are present, the processor may report an error or use `internal-destination`.

### fo:bookmark-title

| Property | Values | Description |
|---|---|---|
| `color` | `<color>` | Color of the bookmark text in the navigation panel. |
| `font-style` | `normal` \| `italic` | Font style of the bookmark text. Limited to these two values. |
| `font-weight` | `normal` \| `bold` | Font weight of the bookmark text. Limited to these two values. |

## Constructed Example: Basic Hierarchical Bookmarks

**Note: This is a constructed example, not from the spec.**

```xml
<fo:root xmlns:fo="http://www.w3.org/1999/XSL/Format">

  <fo:layout-master-set>
    <fo:simple-page-master master-name="page"
        page-height="11in" page-width="8.5in" margin="1in">
      <fo:region-body/>
    </fo:simple-page-master>
  </fo:layout-master-set>

  <!-- Bookmark tree: placed as a child of fo:root, before page-sequences -->
  <fo:bookmark-tree>
    <fo:bookmark internal-destination="ch1">
      <fo:bookmark-title>Chapter 1: Introduction</fo:bookmark-title>
      <fo:bookmark internal-destination="s1-1">
        <fo:bookmark-title>1.1 Background</fo:bookmark-title>
      </fo:bookmark>
      <fo:bookmark internal-destination="s1-2">
        <fo:bookmark-title>1.2 Scope</fo:bookmark-title>
      </fo:bookmark>
    </fo:bookmark>
    <fo:bookmark internal-destination="ch2">
      <fo:bookmark-title>Chapter 2: Methods</fo:bookmark-title>
      <fo:bookmark internal-destination="s2-1">
        <fo:bookmark-title>2.1 Data Collection</fo:bookmark-title>
      </fo:bookmark>
      <fo:bookmark internal-destination="s2-2">
        <fo:bookmark-title>2.2 Analysis</fo:bookmark-title>
      </fo:bookmark>
    </fo:bookmark>
    <fo:bookmark internal-destination="ch3">
      <fo:bookmark-title>Chapter 3: Results</fo:bookmark-title>
    </fo:bookmark>
  </fo:bookmark-tree>

  <fo:page-sequence master-reference="page">
    <fo:flow flow-name="xsl-region-body">
      <fo:block id="ch1" font-size="18pt" font-weight="bold"
          space-before="24pt" space-after="12pt">
        Chapter 1: Introduction
      </fo:block>
      <fo:block id="s1-1" font-size="14pt" font-weight="bold"
          space-before="18pt" space-after="8pt">
        1.1 Background
      </fo:block>
      <fo:block>Background content here...</fo:block>
      <fo:block id="s1-2" font-size="14pt" font-weight="bold"
          space-before="18pt" space-after="8pt">
        1.2 Scope
      </fo:block>
      <fo:block>Scope content here...</fo:block>

      <fo:block id="ch2" font-size="18pt" font-weight="bold"
          space-before="24pt" space-after="12pt" break-before="page">
        Chapter 2: Methods
      </fo:block>
      <fo:block id="s2-1" font-size="14pt" font-weight="bold"
          space-before="18pt" space-after="8pt">
        2.1 Data Collection
      </fo:block>
      <fo:block>Data collection content here...</fo:block>
      <fo:block id="s2-2" font-size="14pt" font-weight="bold"
          space-before="18pt" space-after="8pt">
        2.2 Analysis
      </fo:block>
      <fo:block>Analysis content here...</fo:block>

      <fo:block id="ch3" font-size="18pt" font-weight="bold"
          space-before="24pt" space-after="12pt" break-before="page">
        Chapter 3: Results
      </fo:block>
      <fo:block>Results content here...</fo:block>
    </fo:flow>
  </fo:page-sequence>
</fo:root>
```

**Key points:**
- The `fo:bookmark-tree` is a direct child of `fo:root`, placed after `fo:layout-master-set` and before the first `fo:page-sequence`.
- Each `fo:bookmark` must contain exactly one `fo:bookmark-title` as its first child, followed by zero or more nested `fo:bookmark` children.
- The `internal-destination` value must match an `id` attribute on a formatting object in the document (typically an `fo:block` for section headings).
- Nesting `fo:bookmark` elements inside other `fo:bookmark` elements creates the hierarchy visible in PDF viewers.

## Constructed Example: Bookmarks with Styling and Collapse Control

**Note: This is a constructed example, not from the spec.**

```xml
<fo:bookmark-tree>
  <!-- Top-level: bold, expanded -->
  <fo:bookmark internal-destination="part1" starting-state="show">
    <fo:bookmark-title font-weight="bold" color="navy">
      Part I: Foundations
    </fo:bookmark-title>

    <!-- Second level: normal, initially collapsed -->
    <fo:bookmark internal-destination="ch1" starting-state="hide">
      <fo:bookmark-title>Chapter 1: Overview</fo:bookmark-title>

      <!-- Third level: italic -->
      <fo:bookmark internal-destination="s1-1">
        <fo:bookmark-title font-style="italic">1.1 History</fo:bookmark-title>
      </fo:bookmark>
      <fo:bookmark internal-destination="s1-2">
        <fo:bookmark-title font-style="italic">1.2 Current State</fo:bookmark-title>
      </fo:bookmark>
    </fo:bookmark>

    <fo:bookmark internal-destination="ch2" starting-state="hide">
      <fo:bookmark-title>Chapter 2: Theory</fo:bookmark-title>
    </fo:bookmark>
  </fo:bookmark>

  <fo:bookmark internal-destination="part2" starting-state="show">
    <fo:bookmark-title font-weight="bold" color="navy">
      Part II: Applications
    </fo:bookmark-title>

    <fo:bookmark internal-destination="ch3" starting-state="hide">
      <fo:bookmark-title>Chapter 3: Implementation</fo:bookmark-title>
    </fo:bookmark>
  </fo:bookmark>

  <!-- Appendices: external link -->
  <fo:bookmark external-destination="url('https://example.com/appendix')">
    <fo:bookmark-title font-style="italic" color="gray">
      Online Appendix (External)
    </fo:bookmark-title>
  </fo:bookmark>
</fo:bookmark-tree>
```

**Styling and state control:**
- `starting-state="show"` expands the bookmark's children in the PDF viewer by default. `starting-state="hide"` collapses them.
- A typical pattern is to expand top-level sections (`show`) while collapsing subsections (`hide`) so the reader sees the high-level structure without being overwhelmed.
- `font-weight="bold"` and `color` on `fo:bookmark-title` make top-level entries visually distinct in the bookmark panel.
- `font-style="italic"` can distinguish subsection-level entries.
- `external-destination` with `url('...')` syntax links to an external resource instead of an internal document location.

## Constructed Example: XSLT-Generated Bookmarks

**Note: This is a constructed example, not from the spec.**

When generating bookmarks from structured XML (e.g., DocBook, DITA, or custom XML), use recursive XSLT templates to build the bookmark hierarchy automatically:

```xml
<!-- XSLT template to generate fo:bookmark-tree from document structure -->
<xsl:template name="generate-bookmarks">
  <fo:bookmark-tree>
    <xsl:for-each select="//chapter">
      <fo:bookmark internal-destination="{generate-id(.)}" starting-state="hide">
        <fo:bookmark-title font-weight="bold">
          <xsl:value-of select="concat('Chapter ', position(), ': ', title)"/>
        </fo:bookmark-title>
        <xsl:for-each select="section">
          <fo:bookmark internal-destination="{generate-id(.)}">
            <fo:bookmark-title>
              <xsl:value-of select="title"/>
            </fo:bookmark-title>
            <xsl:for-each select="subsection">
              <fo:bookmark internal-destination="{generate-id(.)}">
                <fo:bookmark-title font-style="italic">
                  <xsl:value-of select="title"/>
                </fo:bookmark-title>
              </fo:bookmark>
            </xsl:for-each>
          </fo:bookmark>
        </xsl:for-each>
      </fo:bookmark>
    </xsl:for-each>
  </fo:bookmark-tree>
</xsl:template>
```

The `generate-id()` function produces unique IDs that are also used as `id` attributes on the corresponding `fo:block` elements in the document body, ensuring that `internal-destination` values resolve correctly.

## Placement Rules

1. `fo:bookmark-tree` must be a child of `fo:root`.
2. It appears after `fo:layout-master-set` (and optional `fo:declarations`) and before the first `fo:page-sequence`.
3. Only one `fo:bookmark-tree` is allowed per document.
4. The `fo:bookmark-tree` must contain at least one `fo:bookmark` child.

The complete `fo:root` content model is:
```xml
(layout-master-set, declarations?, bookmark-tree?, (page-sequence|page-sequence-wrapper)+)
```

## Limitations

- **Text only**: `fo:bookmark-title` contains only `#PCDATA` (plain text). No inline formatting objects (no `fo:inline`, `fo:external-graphic`, etc.) are allowed inside bookmark titles.
- **Styling is limited**: Only `color`, `font-style` (normal/italic), and `font-weight` (normal/bold) are supported on `fo:bookmark-title`. No font-size, font-family, or other formatting.
- **PDF viewer dependency**: The visual rendering of bookmarks (panel placement, expand/collapse behavior, styling support) depends on the PDF viewer. Not all viewers honor `color` or `font-style` on bookmarks.
- **No dynamic bookmarks**: Bookmarks are defined statically in the FO tree. There is no mechanism to generate bookmarks automatically from heading elements — this must be done at the XSLT transformation level.

## See Also

- fo:bookmark-tree — container for all bookmarks
- fo:bookmark — individual bookmark entry
- fo:bookmark-title — bookmark label text
- fo:root — parent of fo:bookmark-tree
- fo:basic-link — the general-purpose linking mechanism (fo:bookmark is a specialized form)
