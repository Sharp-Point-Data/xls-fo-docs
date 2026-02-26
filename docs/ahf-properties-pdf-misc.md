# Antenna House Extension Properties: PDF and Miscellaneous Properties

<!-- Source: XSL-FO-Reference-74-MID.pdf pp.312-476 -->

Miscellaneous properties for PDF output, accessibility, document metadata, page numbering, layer control, tagged PDF support, and version requirements.

## axf:alttext

Specifies the alternate text of an image or link. Effective when outputting Tagged PDF.

| Attribute | Value |
|---|---|
| **Applies to** | fo:external-graphic, fo:instream-foreign-object, fo:basic-link |
| **Values** | &lt;string&gt; |
| **Initial** | empty string |
| **Inherited** | no |

## axf:assumed-page-number

Specifies the assumed page number. When fo:page-number-citation appears, the reference area is sometimes undecided. In evaluation of fo:page-number-citation, the temporary area is secured first, and when a page number is decided, it is adjusted to the right contents. Since the size of an area may change at this time, the formatted result is sometimes not desirable. For example, when an area becomes narrow, it seems that there is an unnecessary line break, and condition that a character will overflow if an area becomes large appears. axf:assumed-page-number gives the assumed page number at that time.

AH XSL Formatter expects the area of at least three-digit page number and formats temporarily. What is necessary will be just to specify axf:assumed-page-number="99" etc., when the page number is clearly less than that.

| Attribute | Value |
|---|---|
| **Applies to** | all formatting objects |
| **Values** | &lt;number&gt; |
| **Initial** | N/A |
| **Inherited** | yes |

## axf:base-uri

Specifies the location which becomes the base of relative URI. The axf:base-uri is applied to all relative URI in a document. When making links using fo:basic-link and specify relative URI, the location that is specified using axf:base-uri is interpreted to be base URI. If this property is omitted or this has empty string, the base location is interpreted as current XML file.

| Attribute | Value |
|---|---|
| **Applies to** | all formatting objects |
| **Values** | &lt;uri-specification&gt; |
| **Initial** | empty string |
| **Inherited** | yes |

## axf:bookmark-include

Specifies how to include bookmarks in multi separate volume.

CAUTION: It is invalid for bookmarks created by fo:bookmark. Use axf:outline-*.

Values have the following meanings:
- `first`: Adds a bookmark to the first separate volume.
- `all`: Adds bookmarks to all the separate volumes.
- `separate`: Adds each bookmark to each separate volume. Bookmarks are added to the volume where axf:outline-level="1" appears. The bookmark that goes across the volume is added to the previous volume. For that reason, the external link to the other volume may be included even though axf:bookmark-include="separate" is specified. Bookmarks grouped by axf:outline-group are attached to the last separate volume.
- `separate-group`: Same as separate, but also adds grouped bookmarks to each volume.

| Attribute | Value |
|---|---|
| **Applies to** | axf:output-volume-info |
| **Values** | first \| all \| separate \| separate-group |
| **Initial** | separate |
| **Inherited** | no |

## axf:destination-type

Specifies the way a link opens in a link destination. If nothing specified, it's accounted as axf:destination-type="xyz-top". The case sensitivity is ignored. The destination type options are described in detail in the Bookmark and Link section of the AHF Online Manual.

| Attribute | Value |
|---|---|
| **Applies to** | block level formatting objects |
| **Values** | &lt;string&gt; |
| **Initial** | empty string |
| **Inherited** | no |

## axf:display-alttext

Specifies whether to display the alternate text of an image.

Values have the following meanings:
- `false`: The alternate text is not displayed.
- `true`: The alternate text is displayed when the alternate text is specified and no image exists.
- `auto`: The value specified by display-alttext in the Option Setting File is adopted.

The alternate text is specified by axf:alttext in XSL-FO and alt in HTML. When the alternate text is displayed, the image is not displayed.

| Attribute | Value |
|---|---|
| **Applies to** | fo:external-graphic |
| **Values** | false \| true \| auto |
| **Initial** | auto |
| **Inherited** | yes |

## axf:document-info-include

Specifies how to include document information in multi separate volume.

Values have the following meanings:
- `first`: Adds document information to the first separate volume.
- `all`: Adds document information to all the separate volumes.

| Attribute | Value |
|---|---|
| **Applies to** | axf:output-volume-info |
| **Values** | first \| all |
| **Initial** | first |
| **Inherited** | no |

## axf:expansion-text

Specifies the expansion text for tags in Tagged PDF. Specifies the description for the abbreviation, etc. in Tagged PDF.

CAUTION: Effective only when generating tags called structure elements in Tagged PDF.

| Attribute | Value |
|---|---|
| **Applies to** | all formatting objects |
| **Values** | &lt;string&gt; |
| **Initial** | empty string |
| **Inherited** | no |

## axf:font-feature-settings

Controls the feature of OpenType fonts.

Values have the following meanings:
- `normal`: Does nothing.
- `<feature-tag-value>`: Specifies the tag of OpenType GSUB/GPOS with the following format: `<feature-tag-value> = <string> [ <integer> | on | off ]?`

CAUTION: Refrain from using this property if you are not familiar with the OpenType specification. Invalidating the tags required for complex script control or inadvertent settings will result in unintended results.

| Attribute | Value |
|---|---|
| **Applies to** | all elements |
| **Values** | normal \| &lt;feature-tag-value&gt;# |
| **Initial** | normal |
| **Inherited** | yes |

## axf:headers

Specifies the table header cells associated with this cell. It is the same as the headers attribute in HTML.

| Attribute | Value |
|---|---|
| **Applies to** | fo:table-cell |
| **Values** | &lt;idrefs&gt; |
| **Initial** | empty |
| **Inherited** | no |

## axf:index-page-citation-range-f-suffix

Specifies the suffix when merging 2 consecutive page numbers. It is used in the same way as fo:index-page-citation-range-separator. The content is (#PCDATA|%inline;)*. If omitted, it is considered "f.".

| Attribute | Value |
|---|---|
| **Applies to** | block level elements |
| **Values** | &lt;string&gt; |
| **Initial** | "f." |
| **Inherited** | yes |

## axf:index-page-citation-range-ff-suffix

Specifies the suffix when merging 3 consecutive page numbers. It is used in the same way as fo:index-page-citation-range-separator. The content is (#PCDATA|%inline;)*. If omitted, it is considered "ff.".

| Attribute | Value |
|---|---|
| **Applies to** | block level elements |
| **Values** | &lt;string&gt; |
| **Initial** | "ff." |
| **Inherited** | yes |

## axf:initial-volume-number

Specifies the initial volume number in multi separate volume. This value is applied for the format property and utilized for the PDF file name to output. In the following example, the file name of the separate volume is document-2.pdf, document-3.pdf, document-4.pdf, and so on:

```xml
<axf:output-volume-info initial-volume-number="2" format="-1"/>
```

| Attribute | Value |
|---|---|
| **Applies to** | axf:output-volume-info |
| **Values** | &lt;number&gt; |
| **Initial** | 1 |
| **Inherited** | no |

## axf:layer

Specifies to which layer the area is arranged.

Values have the following meanings:
- `none`: The area is arranged to no layer.
- `<layer-name>`: The area is arranged to the layer with the name specified by axf:layer-settings.

| Attribute | Value |
|---|---|
| **Applies to** | formatting object that generates area |
| **Values** | none \| &lt;layer-name&gt; |
| **Initial** | none |
| **Inherited** | yes |

## axf:layer-settings

Defines layers. The layer setting syntax is:

`<layer-setting> = <layer-name> [on | off]? [ intent [view | design] || view [on | off] || print [on | off] || export [on | off] || lang <string> preferred? || zoom <number> <number>? || locked ]?`

Values have the following meanings:
- `none`: No definition.
- `<layer-setting>`: Multiple layers can be defined by comma-separated items. What is essential for layer definition is &lt;layer-name&gt;. Other parameters are optional.
- `<layer-name>`: Specifies a name to identify the layer. on or off specifies the default state of the layer when the document is opened. If omitted, it is assumed to be on. If view, print, export are not specified, the value specified here will be referenced.
- `intent`: Specifies the intent of the layer. When view is specified, showing and hiding layers can be toggled. When design is specified, these cannot be toggled. If omitted, it is assumed to be view.
- `view`: Specifies whether to show or hide the layer. Displayed when the document is opened with on, it is hidden with off.
- `print`: Specifies whether to print the layer. It is printed by on and not printed by off.
- `export`: Specifies whether to include the layer in the exported result. It is included by on and not included by off.
- `lang`: Specifies the language of the layer. Displays the layer if the language of the PDF viewer application matches the specified lang when the document is opened. preferred also displays the layer when the language of the viewer partially matches lang.
- `zoom`: Specifies the minimum and maximum values of the magnification of the displayed layer. If only one value is specified, the minimum value is set.
- `locked`: Locks the layer and disables editing. locked is effective with PDF1.6 or later.

In PDF/X, PDF/A and PDF/UA, the settings of view, print, and export are ignored.

| Attribute | Value |
|---|---|
| **Applies to** | fo:root |
| **Values** | none \| &lt;layer-setting&gt;# |
| **Initial** | none |
| **Inherited** | no |

## axf:left-page-master-reference

Master name of the page master for the left page of a two-page spread. axf:left-page-master-reference refers to the page master that defines the page size and the non-spread regions for the left-hand page of a two-page spread.

Values have the following meanings:
- `<name>`: The name must refer to a master-name that exists within the document.

| Attribute | Value |
|---|---|
| **Applies to** | axf:spread-page-master |
| **Values** | &lt;name&gt; |
| **Initial** | N/A, a value is required |
| **Inherited** | no |

## axf:number-type

Specifies whether to output the page number or to output the column number. It can be specified to fo:page-number, etc. and the column number can be outputted instead of the page number. While format property is applied to the format of the page number, axf:column-number-format property is applied to the format of the column number. The column number is not outputted if multiple column is not specified by specifying of column-count="1" or span="all".

Values have the following meanings:
- `page`: Outputs the page number.
- `column`: Outputs the column number.
- `page-and-column`: Outputs both of the page number and the column number.

| Attribute | Value |
|---|---|
| **Applies to** | fo:page-number, fo:page-number-citation, fo:page-number-citation-last |
| **Values** | page \| column \| page-and-column |
| **Initial** | page |
| **Inherited** | no |

## axf:origin-id

Specifies the origin of the page number. ID for the origin of the page number can be specified in fo:page-number or fo:page-number-citation. The output page number is as follows:

`[ref-id page] - [origin-id page] + 1`

If the specified Page is after the ref-id page, the value becomes 0. In fo:page-number, ref-id is considered the position of fo:page-number itself.

| Attribute | Value |
|---|---|
| **Applies to** | fo:page-number, fo:page-number-citation, fo:page-number-citation-last |
| **Values** | &lt;idref&gt; |
| **Initial** | none |
| **Inherited** | no |

## axf:output-volume-break

Separates the file in multi volume. Specifies axf:output-volume-break="true" to fo:page-sequence where you want to start separating the volume. The document number increases one by one. When separating the volume, axf:output-volume-break="true" is considered to be always being specified to the first fo:page-sequence. If axf:output-volume-break="false" is specified explicitly, it is ignored.

Values have the following meanings:
- `true`: Separates the volume newly from this fo:page-sequence.
- `false`: Do not separate the volume newly from this fo:page-sequence.

| Attribute | Value |
|---|---|
| **Applies to** | fo:page-sequence |
| **Values** | true \| false |
| **Initial** | false |
| **Inherited** | no |

## axf:output-volume-filename

Specifies the document file name in multi separate volume. If nothing specified, the automatic file name using the format property is adopted. If this property is specified, the specified name is adopted. This property is effective only with the top fo:page-sequence or with the fo:page-sequence where axf:output-volume-break="true" is specified.

| Attribute | Value |
|---|---|
| **Applies to** | fo:page-sequence |
| **Values** | &lt;string&gt; |
| **Initial** | empty string |
| **Inherited** | no |

## axf:overprint

Specifies the overprint.

Values have the following meanings:
- `auto`: The setting of the overprint in the Option Setting File is adopted. If you specify overprint="k100" in the Option Setting File, even if nothing is specified in FO, black overprinting will be done on all pages.
- `<color>`: Specifies a color you want to apply the overprint. A color with alpha value cannot be specified.
- `k100`: Applies the overprint to rgb-icc(#CMYK,0,0,0,1).
- `separation`: Applies the overprint to the separation color shown rgb-icc(#Separation). The registration color is not included.
- `all`: Applies the overprint to all colors except for a color with alpha value.
- `stroke`: Applies the overprint for the line stroke.
- `paint`: Applies the overprint for the paint.
- `full`, `nonzero`: Specifies the operation in case the color ingredient is 0 when applying the overprint. When full is specified, the color ingredient is set to 0, when nonzero is specified, the color ingredient is not changed. (It is considered no color.) This setting is effective only with CMYK.
- `none`: The overprint is not applied.

| Attribute | Value |
|---|---|
| **Applies to** | all formatting objects |
| **Values** | auto \| &lt;overprint&gt;# where &lt;overprint&gt; = &lt;opcolor&gt; [[stroke \|\| paint \|\| [full \| nonzero]] \| none]? and &lt;opcolor&gt; = &lt;color&gt; \| k100 \| separation \| all |
| **Initial** | auto |
| **Inherited** | yes |

## axf:page-number-prefix

Sets the prefix of page number.

CAUTION: A similar function is provided in XSL 1.1. Use fo:folio-prefix.

Specifies the prefix for page numbers. Specified string will be outputted before the page number by fo:page-number and fo:page-number-citation. Also this string will be used as the page label in the PDF.

```xml
<fo:page-sequence axf:page-number-prefix="A-" format="i" initial-page-number="10">
   <fo:static-content ...>
      ...<fo:page-number/>...
   </fo:static-content>
   ...
</fo:page-sequence>
```

Arabic and Hebrew cannot be specified for the value of axf:page-number-prefix.

| Attribute | Value |
|---|---|
| **Applies to** | fo:page-sequence |
| **Values** | &lt;string&gt; |
| **Initial** | empty string |
| **Inherited** | no |

## axf:pdftag

Specifies the tag name of Tagged PDF. Customizes the tag name when outputting Tagged PDF. When you want to make the tag name of the relevant element "Paragraph", specify as follows:

```xml
<fo:block axf:pdftag="Paragraph">
```

When new-tagging-mode is set to true, and an empty string is specified explicitly as shown below, that element does not create a tag but belongs to the tag to which the parent area belongs.

```xml
<fo:block axf:pdftag="''">
```

| Attribute | Value |
|---|---|
| **Applies to** | all formatting objects |
| **Values** | &lt;string&gt; |
| **Initial** | empty string |
| **Inherited** | no |

## axf:physical-page-number

Gets physical page number. The value of initial-page-number property is disregarded and the physical page number that is not affected by the page-sequence is obtained. In order to obtain the total number of pages, ID is given to the last page per the following example:

```xml
<fo:page-number-citation ref-id="lastpage" axf:physical-page-number="true"/>
```

See also fo:page-number-citation-last in XSL 1.1.

| Attribute | Value |
|---|---|
| **Applies to** | fo:page-number, fo:page-number-citation, fo:page-number-citation-last |
| **Values** | true \| false |
| **Initial** | false |
| **Inherited** | no |

## axf:repeat-page-sequence-master

Specifies the repetition of the page sequence. When the value is true, if the page output reaches in the end of fo:page-sequence-master and the page which should still be outputted remains, page output repeats from the start of fo:page-sequence-master.

| Attribute | Value |
|---|---|
| **Applies to** | fo:page-sequence-master |
| **Values** | true \| false |
| **Initial** | false |
| **Inherited** | no |

## axf:require

Specifies the version of Antenna House Formatter required for formatting. You can specify the required version of Antenna House Formatter when formatting FO, HTML, etc. Formatting will not be performed if the specified version is not reached. For example, if you specify axf:require="7.4", only 7.4 or later can format. If you specify axf:require="7.4.1", only 7.4.1 or later can format. Up to four numbers can be specified.

| Attribute | Value |
|---|---|
| **Applies to** | fo:root |
| **Values** | &lt;string&gt; |
| **Initial** | empty string |
| **Inherited** | no |

## axf:right-page-master-reference

Master name of the page master for the right page of a two-page spread. axf:right-page-master-reference refers to the page master that defines the page size and the non-spread regions for the right-hand page of a two-page spread.

Values have the following meanings:
- `<name>`: The name must refer to a master-name that exists within the document.

| Attribute | Value |
|---|---|
| **Applies to** | axf:spread-page-master |
| **Values** | &lt;name&gt; |
| **Initial** | N/A, a value is required |
| **Inherited** | no |

## axf:scope

Specifies the range of cells with which this table header cell is associated. It is the same as the scope attribute in HTML.

| Attribute | Value |
|---|---|
| **Applies to** | fo:table-cell |
| **Values** | auto \| row \| col \| rowgroup \| colgroup \| both |
| **Initial** | auto |
| **Inherited** | no |
