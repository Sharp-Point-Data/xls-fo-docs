# Advanced Table Layouts

## Overview

XSL-FO provides comprehensive table formatting capabilities including cell spanning (merging), nested tables, header/footer styling, and per-row/per-cell background colors. This guide covers advanced table techniques beyond basic table creation, including patterns for alternating row colors, complex spanning layouts, and nested table structures.

## Cell Spanning (Merged Cells)

Cell spanning is controlled by two properties on `fo:table-cell`:

- **`number-columns-spanned`**: A positive integer specifying how many columns the cell occupies. Default is `1`. The value `0` is also valid and means the cell spans all remaining columns.
- **`number-rows-spanned`**: A positive integer specifying how many rows the cell occupies. Default is `1`. The value `0` is also valid and means the cell spans all remaining rows in the table-body, table-header, or table-footer.

No code samples in spec for cell spanning properties.

### Constructed Example: Table with Column and Row Spanning

**Note: This is a constructed example, not from the spec.**

```xml
<fo:table table-layout="fixed" width="100%" border-collapse="collapse"
    border="1pt solid black">
  <fo:table-column column-width="30%"/>
  <fo:table-column column-width="35%"/>
  <fo:table-column column-width="35%"/>

  <fo:table-header>
    <fo:table-row>
      <!-- Header cell spanning all 3 columns -->
      <fo:table-cell number-columns-spanned="3"
          padding="4pt" background-color="#2c3e50"
          border="1pt solid black">
        <fo:block color="white" font-weight="bold" text-align="center">
          Quarterly Sales Report
        </fo:block>
      </fo:table-cell>
    </fo:table-row>
    <fo:table-row>
      <fo:table-cell padding="4pt" background-color="#34495e"
          border="1pt solid black">
        <fo:block color="white" font-weight="bold">Region</fo:block>
      </fo:table-cell>
      <fo:table-cell padding="4pt" background-color="#34495e"
          border="1pt solid black">
        <fo:block color="white" font-weight="bold">Q1</fo:block>
      </fo:table-cell>
      <fo:table-cell padding="4pt" background-color="#34495e"
          border="1pt solid black">
        <fo:block color="white" font-weight="bold">Q2</fo:block>
      </fo:table-cell>
    </fo:table-row>
  </fo:table-header>

  <fo:table-body>
    <!-- Row-spanning cell: "North" spans 2 rows -->
    <fo:table-row>
      <fo:table-cell number-rows-spanned="2" padding="4pt"
          display-align="center" border="1pt solid black">
        <fo:block font-weight="bold">North</fo:block>
      </fo:table-cell>
      <fo:table-cell padding="4pt" border="1pt solid black">
        <fo:block text-align="end">$150,000</fo:block>
      </fo:table-cell>
      <fo:table-cell padding="4pt" border="1pt solid black">
        <fo:block text-align="end">$175,000</fo:block>
      </fo:table-cell>
    </fo:table-row>
    <fo:table-row>
      <!-- No first cell: occupied by the row-spanning cell above -->
      <fo:table-cell padding="4pt" border="1pt solid black">
        <fo:block text-align="end">$160,000</fo:block>
      </fo:table-cell>
      <fo:table-cell padding="4pt" border="1pt solid black">
        <fo:block text-align="end">$180,000</fo:block>
      </fo:table-cell>
    </fo:table-row>

    <fo:table-row>
      <fo:table-cell padding="4pt" border="1pt solid black">
        <fo:block font-weight="bold">South</fo:block>
      </fo:table-cell>
      <!-- Cell spanning 2 columns -->
      <fo:table-cell number-columns-spanned="2" padding="4pt"
          border="1pt solid black" text-align="center">
        <fo:block font-style="italic">Data pending</fo:block>
      </fo:table-cell>
    </fo:table-row>
  </fo:table-body>
</fo:table>
```

**Key rules for spanning:**
- When a cell spans multiple rows with `number-rows-spanned`, subsequent rows must not include a cell for the column positions occupied by the spanning cell.
- When a cell spans multiple columns with `number-columns-spanned`, no additional cells should be placed in those column positions within the same row.
- Use `display-align="center"` on row-spanning cells to vertically center content across the spanned rows.
- The `column-number` property can explicitly assign a cell to a specific column position, which is useful when spanning creates irregular grid positions.

### Constructed Example: Explicit Column Positioning with Spans

**Note: This is a constructed example, not from the spec.**

```xml
<fo:table table-layout="fixed" width="100%" border-collapse="collapse"
    border="1pt solid black">
  <fo:table-column column-width="25%"/>
  <fo:table-column column-width="25%"/>
  <fo:table-column column-width="25%"/>
  <fo:table-column column-width="25%"/>

  <fo:table-body>
    <fo:table-row>
      <fo:table-cell column-number="1" number-columns-spanned="2"
          number-rows-spanned="2" padding="4pt" border="1pt solid black"
          display-align="center">
        <fo:block text-align="center" font-weight="bold">
          Merged 2x2 Block
        </fo:block>
      </fo:table-cell>
      <fo:table-cell column-number="3" padding="4pt"
          border="1pt solid black">
        <fo:block>C3</fo:block>
      </fo:table-cell>
      <fo:table-cell column-number="4" padding="4pt"
          border="1pt solid black">
        <fo:block>C4</fo:block>
      </fo:table-cell>
    </fo:table-row>
    <fo:table-row>
      <!-- Columns 1-2 occupied by the 2x2 span above -->
      <fo:table-cell column-number="3" padding="4pt"
          border="1pt solid black">
        <fo:block>C3</fo:block>
      </fo:table-cell>
      <fo:table-cell column-number="4" padding="4pt"
          border="1pt solid black">
        <fo:block>C4</fo:block>
      </fo:table-cell>
    </fo:table-row>
  </fo:table-body>
</fo:table>
```

Using explicit `column-number` attributes makes the column assignment unambiguous, which is especially important in tables with complex spanning patterns.

## Alternating Row Colors

The XSL-FO spec does not provide a built-in mechanism for alternating row colors. This is typically achieved at the XSLT level using positional logic to apply different `background-color` values to odd and even rows.

No code samples in spec for alternating row colors.

### Constructed Example: Alternating Row Colors with XSLT

**Note: This is a constructed example, not from the spec.**

The XSLT template uses `position() mod 2` to alternate background colors:

```xml
<!-- XSLT template for generating table rows with alternating colors -->
<xsl:template match="row">
  <fo:table-row>
    <xsl:attribute name="background-color">
      <xsl:choose>
        <xsl:when test="position() mod 2 = 1">#f2f2f2</xsl:when>
        <xsl:otherwise>#ffffff</xsl:otherwise>
      </xsl:choose>
    </xsl:attribute>
    <xsl:apply-templates select="cell"/>
  </fo:table-row>
</xsl:template>
```

### Constructed Example: Complete Table with Alternating Rows and Styled Header

**Note: This is a constructed example, not from the spec.**

```xml
<fo:table table-layout="fixed" width="100%" border-collapse="collapse">
  <fo:table-column column-width="40%"/>
  <fo:table-column column-width="30%"/>
  <fo:table-column column-width="30%"/>

  <!-- Styled header row with distinct background -->
  <fo:table-header>
    <fo:table-row background-color="#2c3e50">
      <fo:table-cell padding="6pt" border="1pt solid #2c3e50">
        <fo:block color="white" font-weight="bold" font-size="10pt">
          Product
        </fo:block>
      </fo:table-cell>
      <fo:table-cell padding="6pt" border="1pt solid #2c3e50">
        <fo:block color="white" font-weight="bold" font-size="10pt">
          Price
        </fo:block>
      </fo:table-cell>
      <fo:table-cell padding="6pt" border="1pt solid #2c3e50">
        <fo:block color="white" font-weight="bold" font-size="10pt">
          Stock
        </fo:block>
      </fo:table-cell>
    </fo:table-row>
  </fo:table-header>

  <!-- Footer row with distinct styling -->
  <fo:table-footer>
    <fo:table-row background-color="#ecf0f1" border-top="2pt solid #2c3e50">
      <fo:table-cell padding="6pt">
        <fo:block font-weight="bold">Total</fo:block>
      </fo:table-cell>
      <fo:table-cell padding="6pt">
        <fo:block font-weight="bold" text-align="end">$1,250.00</fo:block>
      </fo:table-cell>
      <fo:table-cell padding="6pt">
        <fo:block font-weight="bold" text-align="end">450</fo:block>
      </fo:table-cell>
    </fo:table-row>
  </fo:table-footer>

  <fo:table-body>
    <!-- Odd row (light gray background) -->
    <fo:table-row background-color="#f9f9f9">
      <fo:table-cell padding="6pt" border-bottom="0.5pt solid #bdc3c7">
        <fo:block>Widget A</fo:block>
      </fo:table-cell>
      <fo:table-cell padding="6pt" border-bottom="0.5pt solid #bdc3c7">
        <fo:block text-align="end">$250.00</fo:block>
      </fo:table-cell>
      <fo:table-cell padding="6pt" border-bottom="0.5pt solid #bdc3c7">
        <fo:block text-align="end">150</fo:block>
      </fo:table-cell>
    </fo:table-row>

    <!-- Even row (white background) -->
    <fo:table-row background-color="#ffffff">
      <fo:table-cell padding="6pt" border-bottom="0.5pt solid #bdc3c7">
        <fo:block>Widget B</fo:block>
      </fo:table-cell>
      <fo:table-cell padding="6pt" border-bottom="0.5pt solid #bdc3c7">
        <fo:block text-align="end">$500.00</fo:block>
      </fo:table-cell>
      <fo:table-cell padding="6pt" border-bottom="0.5pt solid #bdc3c7">
        <fo:block text-align="end">200</fo:block>
      </fo:table-cell>
    </fo:table-row>

    <!-- Odd row -->
    <fo:table-row background-color="#f9f9f9">
      <fo:table-cell padding="6pt" border-bottom="0.5pt solid #bdc3c7">
        <fo:block>Widget C</fo:block>
      </fo:table-cell>
      <fo:table-cell padding="6pt" border-bottom="0.5pt solid #bdc3c7">
        <fo:block text-align="end">$500.00</fo:block>
      </fo:table-cell>
      <fo:table-cell padding="6pt" border-bottom="0.5pt solid #bdc3c7">
        <fo:block text-align="end">100</fo:block>
      </fo:table-cell>
    </fo:table-row>
  </fo:table-body>
</fo:table>
```

**Styling notes:**
- `background-color` is applied at the `fo:table-row` level. When set on a row, it fills the background of the entire row behind all cells. Cell-level `background-color` overrides the row-level value for that cell.
- Background color precedence (from highest to lowest): `fo:table-cell` > `fo:table-row` > `fo:table-body`/`fo:table-header`/`fo:table-footer` > `fo:table`.
- Only background properties (not padding or border) apply to `fo:table-row`. Padding and borders are set on individual `fo:table-cell` elements.
- Use `border-bottom` on cells (not rows) for horizontal rules between rows.

## Nested Tables

A table can be nested inside an `fo:table-cell` because the cell's content model is `(%block;)+`, which includes `fo:table`. There is no limit to nesting depth.

No code samples in spec for nested tables.

### Constructed Example: Nested Table Layout

**Note: This is a constructed example, not from the spec.**

```xml
<fo:table table-layout="fixed" width="100%" border-collapse="collapse"
    border="1pt solid black">
  <fo:table-column column-width="30%"/>
  <fo:table-column column-width="70%"/>

  <fo:table-body>
    <fo:table-row>
      <fo:table-cell padding="6pt" border="1pt solid black">
        <fo:block font-weight="bold">Department</fo:block>
      </fo:table-cell>
      <fo:table-cell padding="6pt" border="1pt solid black">
        <fo:block font-weight="bold">Employees</fo:block>
      </fo:table-cell>
    </fo:table-row>

    <fo:table-row>
      <fo:table-cell padding="6pt" border="1pt solid black"
          display-align="center">
        <fo:block>Engineering</fo:block>
      </fo:table-cell>
      <fo:table-cell padding="0pt" border="1pt solid black">
        <!-- Nested table inside the cell -->
        <fo:table table-layout="fixed" width="100%"
            border-collapse="collapse">
          <fo:table-column column-width="50%"/>
          <fo:table-column column-width="25%"/>
          <fo:table-column column-width="25%"/>
          <fo:table-body>
            <fo:table-row background-color="#ecf0f1">
              <fo:table-cell padding="4pt"
                  border-bottom="0.5pt solid #bdc3c7">
                <fo:block font-weight="bold" font-size="9pt">Name</fo:block>
              </fo:table-cell>
              <fo:table-cell padding="4pt"
                  border-bottom="0.5pt solid #bdc3c7">
                <fo:block font-weight="bold" font-size="9pt">Role</fo:block>
              </fo:table-cell>
              <fo:table-cell padding="4pt"
                  border-bottom="0.5pt solid #bdc3c7">
                <fo:block font-weight="bold" font-size="9pt">Level</fo:block>
              </fo:table-cell>
            </fo:table-row>
            <fo:table-row>
              <fo:table-cell padding="4pt"><fo:block font-size="9pt">Alice</fo:block></fo:table-cell>
              <fo:table-cell padding="4pt"><fo:block font-size="9pt">Lead</fo:block></fo:table-cell>
              <fo:table-cell padding="4pt"><fo:block font-size="9pt">Senior</fo:block></fo:table-cell>
            </fo:table-row>
            <fo:table-row>
              <fo:table-cell padding="4pt"><fo:block font-size="9pt">Bob</fo:block></fo:table-cell>
              <fo:table-cell padding="4pt"><fo:block font-size="9pt">Dev</fo:block></fo:table-cell>
              <fo:table-cell padding="4pt"><fo:block font-size="9pt">Mid</fo:block></fo:table-cell>
            </fo:table-row>
          </fo:table-body>
        </fo:table>
      </fo:table-cell>
    </fo:table-row>
  </fo:table-body>
</fo:table>
```

**Nested table considerations:**
- The nested table is a direct child block of `fo:table-cell`. Set `padding="0pt"` on the containing cell if the nested table should fill the cell completely.
- The nested table's `width="100%"` makes it fill the containing cell's content area.
- Each table (outer and nested) needs its own `fo:table-column` definitions.
- `table-layout="fixed"` is recommended for both outer and nested tables for predictable column sizing.
- Borders on nested tables are independent of the outer table's borders. Use `border-collapse="collapse"` consistently if you want seamless borders.

## Table Header/Footer Alternatives (XSL-FO 2.0)

XSL-FO 2.0 introduces `fo:table-header-alternatives` and `fo:table-footer-alternatives` for conditional header/footer content based on boundary position.

### Spec Example: Conditional Table Headers

<!-- Source: xslspec.xml line 12230 -->
```xml
<fo:table>
 <fo:table-header>
   <fo:table-header-alternatives>
     <fo:conditional-table-header-reference>
       ...
     </fo:conditional-table-header-reference>
     <fo:conditional-table-header-reference header-position="page">
       ...
     </fo:conditional-table-header-reference>
     <fo:conditional-table-header-reference header-position="column">
       ...
     </fo:conditional-table-header-reference>
     ...
   </fo:table-header-alternatives>
 </fo:table-header>
 <fo:table-footer>
   <fo:table-footer-alternatives>
   </fo:table-footer-alternatives>
 </fo:table-footer>
 <fo:table-body>
   ...
 </fo:table-body>
</fo:table>
```

The `header-position` property on `fo:conditional-table-header-reference` controls when each alternative header is used:
- No `header-position` (default): The default header used as a fallback.
- `header-position="page"`: Used when the table continues at a page break.
- `header-position="column"`: Used when the table continues at a column break.
- `header-position="region"`: Used when the table continues at a region boundary.

## Limitations and Processor Considerations

### Border Model Limitations

XSL-FO defines two border models controlled by `border-collapse` on `fo:table`:

- **`border-collapse="collapse"`**: Borders between adjacent cells merge into a single border. Border precedence rules determine which border wins when they differ. The precedence order is: table > column > row > cell (with wider borders winning over narrower ones, and certain styles winning over others).
- **`border-collapse="collapse-with-precedence"`**: Same as collapse but allows explicit precedence values via `border-before-precedence`, `border-after-precedence`, `border-start-precedence`, and `border-end-precedence`.
- **`border-collapse="separate"`**: Each cell has its own independent borders with spacing controlled by `border-separation` (the XSL-FO equivalent of CSS `border-spacing`).

### Column Width Calculation

Tables use either fixed or automatic layout:
- **`table-layout="fixed"`**: Column widths are determined by `fo:table-column` specifications. Required when using `proportional-column-width()`.
- **`table-layout="auto"`**: Column widths are calculated from content. More processor-intensive and behavior may vary between processors.

The `proportional-column-width()` function distributes remaining space proportionally:

```xml
<fo:table-column column-width="proportional-column-width(1)"/>  <!-- 1/3 -->
<fo:table-column column-width="proportional-column-width(2)"/>  <!-- 2/3 -->
```

### Known Processor Variations

Processor behavior may differ in these areas (not part of the W3C spec — based on common implementation experience):

- **Table breaking across pages**: The spec allows tables to break across pages, with `fo:table-header` and `fo:table-footer` repeated on each page. Not all processors handle `number-rows-spanned` cells that cross page boundaries identically.
- **Automatic table layout**: The algorithm for `table-layout="auto"` is not specified in detail by XSL-FO. Processors may produce different column widths for the same content.
- **Nested table borders**: When nested tables have `border-collapse="collapse"`, the border collapsing applies only within each table independently. The nested table's outer border interacts with the containing cell's padding, not with the outer table's borders.
- **number-rows-spanned="0"** (span all remaining rows): Not all processors support the value `0`. When unsupported, specify the exact number of rows to span.

## See Also

- fo:table — the table formatting object
- fo:table-cell — cell formatting object (holds `number-columns-spanned`, `number-rows-spanned`)
- fo:table-row — row formatting object (accepts `background-color`)
- fo:table-header — table header (repeated on page breaks)
- fo:table-footer — table footer
- fo:table-column — column definitions
- fo:table-body — table body container
- properties-table — comprehensive table property reference
- properties-border-padding-background — background-color and border properties
