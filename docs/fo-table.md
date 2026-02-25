# fo:table

## Summary

The `fo:table` flow object is used for formatting the tabular material of a table. The `fo:table` and its child flow objects model the visual layout of a table in a "row primary" manner. A complete table may be seen as consisting of a grid of rows and columns where each cell occupies one or more grid units in the row-progression-direction and column-progression-direction.

The table content is divided into a header (optional), footer (optional), and one or more bodies. Properties specify if the headers and footers should be repeated at a break in the table. Each of these parts occupies one or more rows in the table grid.

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_table -->

## Areas

The `fo:table` formatting object generates and returns one or more normal block-areas. These areas consist of:

1. The content of the `fo:table-header` (unless omitted as specified by the `table-omit-header-at-break` property).
2. Some portion of the content of the `fo:table-body`(s).
3. The content of the `fo:table-footer` (unless omitted as specified by the `table-omit-footer-at-break` property).

In addition the `fo:table` returns any page-level-out-of-line areas, and any reference-level-out-of-line areas returned by the children of the `fo:table`.

The areas generated and returned by the `fo:table` formatting object have as children:

- Areas, with only `background`, corresponding to the table-header, table-footer, table-body, spanned columns, columns, and rows. The spanned columns (`fo:table-column` with a `number-columns-spanned` value greater than 1) are used in the same way as the "column groups" in CSS2 for determining the background.
- Areas returned by the `fo:table-cell` formatting objects.

These areas have a `z-index` controlling the rendering order determined in accordance with section 17.5.1 of the CSS2 specification.

A cell that is spanned may have a different `background` in each of the grid units it occupies.

## Trait Derivation

- The column-progression-direction and row-progression-direction are determined by the `writing-mode` trait. Columns use the inline-progression-direction, and rows use the block-progression-direction.
- The method for deriving the `border` traits for a table is specified by the `border-collapse` property.
- If `border-collapse` is "separate": the border is composed of two components. The first is placed with the inside edge coincident with the outermost table grid boundary line with the width of half the value for the `border-separation` property, filled in accordance with the `background` property of the `fo:table`. Second, outside the outermost table grid boundary line is placed, for each side of the table, a border based on a border specified on the table.
- If `border-collapse` is "collapse" or "collapse-with-precedence": the border is determined, for each segment, at the cell level. By specifying "collapse-with-precedence" and an appropriately high precedence on the border specification for the `fo:table` one may ensure that this specification is the one used on all border segments.

## Constraints

- No area may have more than one normal child area returned by the same `fo:table` formatting object.
- The content of the `fo:table-header` and `fo:table-footer`, unless omitted as specified by the `table-omit-header-at-break` and `table-omit-footer-at-break` properties, shall be repeated for each normal block-area generated and returned by the `fo:table` formatting object.
- The `inline-progression-dimension` of the content-rectangle of the table is the sum of the inline-progression-dimensions of the columns in the table grid.

### Table Layout

The method used to determine column inline-progression-dimensions is governed by the values of the `table-layout` and `inline-progression-dimension` traits:

| inline-progression-dimension | table-layout | Layout Used |
|---|---|---|
| `auto` | `auto` | Automatic table layout |
| `auto` | `fixed` | Automatic table layout |
| `<length>` or `<percentage>` | `auto` | Automatic table layout |
| `<length>` or `<percentage>` | `fixed` | Fixed table layout |

The automatic table layout and fixed table layout are defined in section 17.5.2 of the CSS2 specification.

The use of the `proportional-column-width()` function is only permitted when the fixed table layout is used. If proportional column widths are desired on a table of an unknown explicit width, the `inline-progression-dimension` cannot be specified to be "auto". Instead, the `width` must be specified as a percentage. For example, setting `table-layout="fixed"` and `inline-progression-dimension="100%"` would allow proportional column widths while simultaneously creating a table as wide as possible in the current context.

### Error Conditions

- It is an error if two or more table-cells overlap, for example because two or more table-cells attempt to span rows or columns into the same cell position within the table grid. An implementation may recover by repositioning the table-cells so that all of the content is shown.
- Table-cells must each be entirely contained both horizontally and vertically in a single table-body, table-header or table-footer. It is an error if table-cells attempt to span too far. An implementation may recover by behaving as if the table-cell spanned only as many rows or columns as are actually available.

## Content Model

```
(fo:table-column*, fo:table-header?, fo:table-footer?, fo:table-body+)
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
| `block-progression-dimension` | no | Basic |
| `border-after-precedence` | no | Basic (collapsing) |
| `border-before-precedence` | no | Basic (collapsing) |
| `border-collapse` | yes | Basic |
| `border-end-precedence` | no | Basic (collapsing) |
| `border-separation` | yes | Basic |
| `border-start-precedence` | no | Basic (collapsing) |
| `break-after` | no | Basic |
| `break-before` | no | Basic |
| `clear` | no | Extended |
| `id` | N/A | Basic |
| `index-class` | N/A | Extended |
| `index-key` | N/A | Extended |
| `inline-progression-dimension` | no | Basic |
| `intrusion-displace` | yes | Extended |
| `height` | no | Basic |
| `keep-together` | no | Extended |
| `keep-with-next` | no | Extended |
| `keep-with-previous` | no | Extended |
| `table-layout` | no | Basic |
| `table-omit-footer-at-break` | no | Basic |
| `table-omit-header-at-break` | no | Basic |
| `width` | no | Basic |
| `writing-mode` | yes | Basic |

## Usage Notes

- The `fo:table` is the primary formatting object for tabular data. It must contain at least one `fo:table-body`.
- Use `fo:table-column` children to pre-specify column widths and column-level properties (such as `background`).
- The `table-layout` property is critical: set it to `fixed` and provide an explicit `inline-progression-dimension` (or `width`) when using `proportional-column-width()`.
- Use `table-omit-header-at-break` and `table-omit-footer-at-break` to control whether headers/footers are repeated when a table breaks across pages.
- The `border-collapse` property determines the border model: "separate" uses CSS2 separate borders model, while "collapse" and "collapse-with-precedence" use the collapsing borders model.
- The result of using a percentage for the width may be unpredictable, especially when using the automatic table layout.

## Code Samples

The following three-part example demonstrates a table with proportional column widths, vertical alignment, and text alignment. It shows a CALS-style source XML, the XSLT transformation (including a utility template for converting CALS column width specifications to XSL-FO), and the resulting FO output.

Source XML with proportional column widths (`1*`, `2*+2pi`) and a fixed-width column (`72`):

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_ruby-text-container -->
```xml
<doc>
<table>
<tgroup cols="3">
<colspec colname="col1" colwidth="1*"/>
<colspec colname="col2" colwidth="2*+2pi"/>
<colspec colname="col3" colwidth="72"/>
<tbody>
<row>
<entry colnum="1" valign="top"><p>Cell 1</p></entry>
<entry colnum="2" valign="middle" align="center"><p>Cell 2</p></entry>
<entry colnum="3" align="center"><p>Cell 3</p></entry>
</row>
</tbody>
</tgroup>
</table>
</doc>
```

XSLT stylesheet that transforms the source into XSL-FO, including a `calc.column.width` named template that converts CALS column width specifications (e.g., `1*`, `2*+2pi`, `72`) into XSL-FO column widths using `proportional-column-width()`. Also maps `valign` to `display-align` and `align` to `text-align`:

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_ruby-text-container -->
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

<xsl:template match="table">
  <fo:table width="12cm" table-layout="fixed">
    <xsl:apply-templates/>
  </fo:table>
</xsl:template>

<xsl:template match="colspec">
  <fo:table-column>
    <xsl:attribute name="column-number">
      <xsl:number count="colspec"/>
    </xsl:attribute>
    <xsl:attribute name="column-width">
      <xsl:call-template name="calc.column.width">
        <xsl:with-param name="colwidth">
          <xsl:value-of select="@colwidth"/>
        </xsl:with-param>
      </xsl:call-template>
    </xsl:attribute>
  </fo:table-column>
</xsl:template>

<xsl:template match="tbody">
  <fo:table-body>
    <xsl:apply-templates/>
  </fo:table-body>
</xsl:template>

<xsl:template match="row">
  <fo:table-row>
    <xsl:apply-templates/>
  </fo:table-row>
</xsl:template>

<xsl:template match="entry">
  <fo:table-cell column-number="{@colnum}">
    <xsl:if test="@valign">
      <xsl:choose>
        <xsl:when test="@valign='middle'">
          <xsl:attribute name="display-align">center</xsl:attribute>
        </xsl:when>
        <xsl:when test="@valign='top'">
          <xsl:attribute name="display-align">before</xsl:attribute>
        </xsl:when>
        <xsl:when test="@valign='bottom'">
          <xsl:attribute name="display-align">after</xsl:attribute>
        </xsl:when>
        <xsl:otherwise>
          <xsl:attribute name="display-align">before</xsl:attribute>
        </xsl:otherwise>
      </xsl:choose>
    </xsl:if>
    <xsl:if test="@align">
      <xsl:attribute name="text-align">
        <xsl:value-of select="@align"/>
      </xsl:attribute>
    </xsl:if>
    <xsl:apply-templates/>
  </fo:table-cell>
</xsl:template>


<xsl:template name="calc.column.width">
<!-- **
     * <p>Calculate an XSL FO table column-width specification from a
     * full relative table column-width specification.</p>
     *
     * <p>Table column-widths are in the following basic
     * forms:</p>
     *
     * <ul>
     * <li><b>99.99units</b>, a fixed length-specifier.</li>
     * <li><b>99.99</b>, a fixed length-specifier without any units.</li>
     * <li><b>99.99*</b>, a relative length-specifier.</li>
     * <li><b>99.99*+99.99units</b>, a combination of both.</li>
     * </ul>
     *
     * <p>The units are points (pt), picas (pi), centimeters (cm),
     * millimeters (mm), and inches (in). These are the same units as XSL,
     * except that XSL abbreviates picas "pc" instead of "pi". If a length
     * specifier has no units, the default unit (pt) is assumed.</p>
     *
     * <p>Relative length-specifiers are represented in XSL with the
     * proportional-column-width() function.</p>
     *
     * <p>Here are some examples:</p>
     *
     * <ul>
     * <li>"36pt" becomes "36pt"</li>
     * <li>"3pi" becomes "3pc"</li>
     * <li>"36" becomes "36pt"</li>
     * <li>"3*" becomes "proportional-column-width(3)"</li>
     * <li>"3*+2pi" becomes "proportional-column-width(3)+2pc"</li>
     * <li>"1*+2" becomes "proportional-column-width(1)+2pt"</li>
     * </ul>
     *
     * @param colwidth The column width specification.
     *
     * @returns The XSL column width specification.
     * -->
  <xsl:param name="colwidth">1*</xsl:param>

  <!-- Ok, the colwidth could have any one of the following forms: -->
  <!--        1*       = proportional width -->
  <!--     1unit       = 1.0 units wide -->
  <!--         1       = 1pt wide -->
  <!--  1*+1unit       = proportional width + some fixed width -->
  <!--      1*+1       = proportional width + some fixed width -->

  <!-- If it has a proportional width, translate it to XSL -->
  <xsl:if test="contains($colwidth, '*')">
    <xsl:text>proportional-column-width(</xsl:text>
    <xsl:value-of select="substring-before($colwidth, '*')"/>
    <xsl:text>)</xsl:text>
  </xsl:if>

  <!-- Now get the non-proportional part of the specification -->
  <xsl:variable name="width-units">
    <xsl:choose>
      <xsl:when test="contains($colwidth, '*')">
        <xsl:value-of
             select="normalize-space(substring-after($colwidth, '*'))"/>
      </xsl:when>
      <xsl:otherwise>
        <xsl:value-of select="normalize-space($colwidth)"/>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:variable>

  <!-- Now the width-units could have any one of the following forms: -->
  <!--                 = <empty string> -->
  <!--     1unit       = 1.0 units wide -->
  <!--         1       = 1pt wide -->
  <!-- with an optional leading sign -->

  <!-- Get the width part by blanking out the units part and discarding -->
  <!-- white space. -->
  <xsl:variable name="width"
       select="normalize-space(translate($width-units,
                                         '+-0123456789.abcdefghijklmnopqrstuvwxyz',
                                         '+-0123456789.'))"/>

  <!-- Get the units part by blanking out the width part and discarding -->
  <!-- white space. -->
  <xsl:variable name="units"
       select="normalize-space(translate($width-units,
                                         'abcdefghijklmnopqrstuvwxyz+-0123456789.',
                                         'abcdefghijklmnopqrstuvwxyz'))"/>

  <!-- Output the width -->
  <xsl:value-of select="$width"/>

  <!-- Output the units, translated appropriately -->
  <xsl:choose>
    <xsl:when test="$units = 'pi'">pc</xsl:when>
    <xsl:when test="$units = '' and $width != ''">pt</xsl:when>
    <xsl:otherwise><xsl:value-of select="$units"/></xsl:otherwise>
  </xsl:choose>
</xsl:template>

</xsl:stylesheet>
```

Resulting XSL-FO output showing `fo:table` with `table-layout="fixed"`, `proportional-column-width()` for relative columns, and `display-align`/`text-align` for cell alignment:

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_ruby-text-container -->
```xml
<fo:table width="12cm" table-layout="fixed">
  <fo:table-column column-number="1" column-width="proportional-column-width(1)">
  </fo:table-column>
  <fo:table-column column-number="2" column-width="proportional-column-width(2)+2pc">
  </fo:table-column>
  <fo:table-column column-number="3" column-width="72pt">
  </fo:table-column>
  <fo:table-body>
    <fo:table-row>
      <fo:table-cell column-number="1" display-align="before">
        <fo:block>Cell 1
        </fo:block>
      </fo:table-cell>
      <fo:table-cell column-number="2" display-align="center" text-align="center">
        <fo:block>Cell 2
        </fo:block>
      </fo:table-cell>
      <fo:table-cell column-number="3" text-align="center">
        <fo:block>Cell 3
        </fo:block>
      </fo:table-cell>
    </fo:table-row>
  </fo:table-body>
</fo:table>
```

## See Also

- `fo:table-and-caption` -- wraps a table with a caption
- `fo:table-column` -- specifies column characteristics
- `fo:table-header` -- table header rows
- `fo:table-footer` -- table footer rows
- `fo:table-body` -- table body rows
- `fo:table-row` -- groups cells into rows
- `fo:table-cell` -- individual cell content
- `table-layout` property
- `border-collapse` property
- `proportional-column-width()` function
