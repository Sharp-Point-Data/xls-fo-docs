# axf:spread-page-master

## Summary

Specifies the page master of a double page (two pages displayed facing). In addition to the page area specified with a page master (`fo:simple-page-master`), an area can also be specified for such double pages in which the contents span the width of both pages.

The double page is generated only if the text flow contains enough material to fill the flow area.

## Properties

| Property | Description |
|----------|-------------|
| `end-indent` | End indent of the spread area |
| `margin-top` | Top margin of the spread area |
| `margin-bottom` | Bottom margin of the spread area |
| `margin-left` | Left margin of the spread area |
| `margin-right` | Right margin of the spread area |
| `master-name` | Name used to reference this spread page master |
| `reference-orientation` | Reference orientation for the spread |
| `space-before` | Space before the spread area |
| `space-after` | Space after the spread area |
| `start-indent` | Start indent of the spread area |
| `writing-mode` | Writing mode for the spread |

### AHF Extension Properties

| Property | Description |
|----------|-------------|
| `axf:left-page-master-reference` | References the `fo:simple-page-master` used for the left (even) page of the spread |
| `axf:right-page-master-reference` | References the `fo:simple-page-master` used for the right (odd) page of the spread |

## Parent Objects

- `fo:layout-master-set`

## Child Objects

- `axf:spread-region`

## Code Samples

<!-- Source: XSL-FO-Reference-74-MID.pdf pp.307-310 -->

The root element:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<fo:root xmlns:fo="http://www.w3.org/1999/XSL/Format"
xmlns:axf="http://www.antennahouse.com/names/XSL/Extensions">
</fo:root>
```

The layout-master-set containing simple page masters and the spread page master:

```xml
<fo:layout-master-set>
<fo:simple-page-master master-name="Title" page-width="210mm" page-height="297mm">
<fo:region-body margin="36pt" border="1pt solid black" padding="6pt"/>
<fo:region-before region-name="Header-right" extent="36pt" padding-end="36pt"
display-align="center"/>
<fo:region-after extent="36pt" padding-end="36pt" display-align="center"/>
</fo:simple-page-master>
<fo:simple-page-master master-name="Page-right" page-width="210mm"
page-height="297mm">
<fo:region-body margin="36pt" border="1pt solid black" padding="6pt"/>
<fo:region-before region-name="Header-right" extent="36pt" padding-end="36pt"
display-align="center"/>
<fo:region-after extent="36pt" padding-end="36pt" display-align="center"/>
</fo:simple-page-master>
<fo:simple-page-master master-name="Page-left" page-width="210mm"
page-height="297mm">
 <fo:region-body margin="36pt" border="1pt solid black" padding="6pt"/>
<fo:region-before region-name="Header-left" extent="36pt" padding-start="36pt"
display-align="center"/>
<fo:region-after extent="36pt" padding-start="36pt" display-align="center"/>
</fo:simple-page-master>
<!-- Page master for double pages -->
<axf:spread-page-master master-name="Double-pages"
left-page-master-reference="Page-left"
right-page-master-reference="Page-right">
<axf:spread-region region-name="spread" margin-top="36pt" margin-left="36pt"
margin-right="36pt" margin-bottom="48mm"/>
</axf:spread-page-master>
<!-- Double page sequence template -->
<fo:page-sequence-master master-name="With-double-page">
<fo:single-page-master-reference master-reference="Title"/>
<fo:repeatable-page-master-reference master-reference="Double-pages"
maximum-repeats="2"/>
<fo:repeatable-page-master-alternatives>
<fo:conditional-page-master-reference master-reference="Page-left"
odd-or-even="even"/>
<fo:conditional-page-master-reference master-reference="Page-right"
odd-or-even="odd"/>
</fo:repeatable-page-master-alternatives>
</fo:page-sequence-master>
</fo:layout-master-set>
```

The page sequence using the spread page master:

```xml
<fo:page-sequence master-reference="With-double-page"
force-page-count="end-on-even">
<fo:static-content flow-name="Header-left">
<fo:block>left page heading</fo:block>
</fo:static-content>
<fo:static-content flow-name="Header-right">
<fo:block text-align="right">right page heading</fo:block>
</fo:static-content>
<fo:static-content flow-name="xsl-region-after">
<fo:block text-align="outside"><fo:page-number/></fo:block>
</fo:static-content>
<fo:flow flow-name="spread">
<fo:block text-align="center" font-weight="bold">
This is a Spanned Title
</fo:block>
 <fo:table width="100%" border="1pt solid red" space-before="12pt"
background-color="yellow">
<fo:table-column number-columns-repeated="10"
column-width="10%" border-right="1pt solid black" />
<fo:table-header>
<fo:table-row border-bottom="1pt solid black">
<fo:table-cell number-columns-spanned="10">
<fo:block text-align="center" font-weight="bold">Table Caption</fo:block>
</fo:table-cell>
</fo:table-row>
</fo:table-header>
<fo:table-body>
<fo:table-row border-bottom="1pt solid black">
<fo:table-cell><fo:block text-align="center">Content</fo:block></fo:table-cell>
<fo:table-cell/><fo:table-cell/><fo:table-cell/><fo:table-cell/><fo:table-cell/>
<fo:table-cell/><fo:table-cell/><fo:table-cell/><fo:table-cell/>
</fo:table-row>
</fo:table-body>
</fo:table>
</fo:flow>
<fo:flow flow-name="xsl-region-body">
<fo:block text-align="center" font-weight="bold" color="red">Title</fo:block>
<fo:block background-color="silver">
<fo:block>Content Content Content Content Content Content</fo:block>
<fo:block>[More content for more pages!] </fo:block>
</fo:block>
</fo:flow>
</fo:page-sequence>
```

Note: The double page is generated only if the text flow contains enough material to fill the flow area.
