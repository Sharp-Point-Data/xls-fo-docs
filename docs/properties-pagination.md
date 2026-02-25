# Pagination and Layout Properties

<!-- Source: https://www.w3.org/TR/xslfo20/#blank-or-not-blank -->

## Overview

The pagination and layout properties are all XSL-only properties that control how pages are created, sequenced, and laid out. They govern page master selection rules, page dimensions, region naming, flow mapping (assigning flows to regions), page numbering, column layout, and copyfitting behavior.

These properties are used on page-level formatting objects such as `fo:simple-page-master`, `fo:page-sequence-master`, `fo:repeatable-page-master-alternatives`, `fo:conditional-page-master-reference`, `fo:page-sequence`, `fo:flow`, `fo:static-content`, `fo:flow-map`, and region formatting objects (`fo:region-body`, `fo:region-before`, `fo:region-after`, `fo:region-start`, `fo:region-end`).

This is the largest group of pagination properties, covering page master selection, page geometry, flow mapping, and the new XSL-FO 2.0 copyfitting mechanism.

## Properties

### blank-or-not-blank

| Field | Value |
|---|---|
| **Values** | `blank \| not-blank \| any \| inherit` |
| **Initial** | `any` |
| **Applies to** | fo:conditional-page-master-reference |
| **Inherited** | No |
| **Percentages** | N/A |

This property forms part of a selection rule to determine if the referenced page-master is eligible for selection at this point in the page-sequence.

Values have the following meanings:

- **blank** -- This master is eligible for selection if a page must be generated (e.g., to maintain proper page parity at the start or end of the page-sequence) and there are no areas from any of the `fo:flow` flows within the containing `fo:page-sequence` to be put on that page.
- **not-blank** -- This master is eligible for selection if this page contains areas from any of the `fo:flow` flows within the containing `fo:page-sequence`.
- **any** -- This master is always eligible for selection.

### column-count

| Field | Value |
|---|---|
| **Values** | `<number> \| inherit` |
| **Initial** | `1` |
| **Applies to** | fo:region-body |
| **Inherited** | No |
| **Percentages** | N/A |

Specifies the number of columns in the region. A value of 1 indicates that this is not a multi-column region.

A positive integer. If a non-positive or non-integer value is provided, the value will be rounded to the nearest integer value greater than or equal to 1.

### column-gap

| Field | Value |
|---|---|
| **Values** | `<length> \| <percentage> \| inherit` |
| **Initial** | `12.0pt` |
| **Applies to** | fo:region-body |
| **Inherited** | No |
| **Percentages** | refer to width of the region being divided into columns |

Specifies the width of the separation between adjacent columns in a multi-column region.

Values have the following meanings:

- **\<length\>** -- This is an unsigned length. If a negative value has been specified a value of 0pt will be used.
- **\<percentage\>** -- The value is a percentage of the `inline-progression-dimension` of the content-rectangle of the region.

### extent

| Field | Value |
|---|---|
| **Values** | `<length> \| <percentage> \| inherit` |
| **Initial** | `0.0pt` |
| **Applies to** | fo:region-before, fo:region-after, fo:region-start, fo:region-end |
| **Inherited** | No |
| **Percentages** | refer to the corresponding block-progression-dimension or inline-progression-dimension of the page-viewport-area |

Specifies the `inline-progression-dimension` of the region-start or region-end or the `block-progression-dimension` of the region-before or region-after.

Values have the following meanings:

- **\<length\>** -- This is an unsigned length. If a negative value has been specified a value of 0pt will be used.
- **\<percentage\>** -- The value is a percentage of the corresponding `block-progression-dimension` or `inline-progression-dimension` of the page-viewport-area.

### flow-map-name

| Field | Value |
|---|---|
| **Values** | `<name>` |
| **Initial** | none, a value is required |
| **Applies to** | fo:flow-map |
| **Inherited** | No |
| **Percentages** | N/A |

This property provides an identifying name for an `fo:flow-map`, which is subsequently referenced as the value of the `flow-map-reference` property on an `fo:page-sequence`.

Names identify flow-maps. They may not be empty and must be unique.

### flow-map-reference

| Field | Value |
|---|---|
| **Values** | `<name>` |
| **Initial** | see prose |
| **Applies to** | fo:page-sequence |
| **Inherited** | No |
| **Percentages** | N/A |

Specifies the flow map to be used for assigning flows to regions within the page-sequence.

The name identifies a flow map; it may not be empty and must refer to a `flow-map-name` that exists within the document.

If no `flow-map-reference` is specified on a page-sequence, then the flow-map in effect is the implicit flow-map specified in the `fo:page-sequence` definition.

### flow-name

| Field | Value |
|---|---|
| **Values** | `<name>` |
| **Initial** | `an empty name` |
| **Applies to** | fo:flow, fo:static-content |
| **Inherited** | No, a value is required |
| **Percentages** | N/A |

Defines the name of the flow. Names used as identifiers must be unique within an `fo:page-sequence`.

The `flow-name` and `region-name` are used to assign the flow's content (or static-content's content) to a specific region or series of regions in the layout. In XSL this is done by specifying the name of the target region as the flow-name. (For example, text placed in the region-body would specify `flow-name="xsl-region-body"`.)

The flow-names reserved in XSL are: xsl-region-body, xsl-region-before, xsl-region-after, xsl-region-start, xsl-region-end, xsl-before-float-separator, xsl-footnote-separator.

If the name is empty or if a name-conflict is encountered, an error shall be reported. A processor may then continue processing.

### flow-name-reference

| Field | Value |
|---|---|
| **Values** | `<name>` |
| **Initial** | none, a value is required |
| **Applies to** | fo:flow-name-specifier |
| **Inherited** | No |
| **Percentages** | N/A |

Specifies a flow to be used within a sequence of flows in the flow-source-list of a particular assignment of flows to regions.

The name identifies a flow; it must not be empty and must refer to a `flow-name` that exists within the document.

### force-page-count

| Field | Value |
|---|---|
| **Values** | `auto \| even \| odd \| end-on-even \| end-on-odd \| no-force \| inherit` |
| **Initial** | `auto` |
| **Applies to** | fo:page-sequence |
| **Inherited** | No |
| **Percentages** | N/A |

Force-page-count is used to impose a constraint on the number of pages in a page-sequence. In the event that this constraint is not satisfied, an additional page will be added to the end of the sequence. This page becomes the "last" page of that sequence.

Values have the following meanings:

- **auto** -- Force the last page in this page-sequence to be an odd-page if the `initial-page-number` of the next page-sequence is even. Force it to be an even-page if the `initial-page-number` of the next page-sequence is odd. If there is no next page-sequence or if the value of its `initial-page-number` is "auto" do not force any page.
- **even** -- Force an even number of pages in this page-sequence.
- **odd** -- Force an odd number of pages in this page-sequence.
- **end-on-even** -- Force the last page in this page-sequence to be an even-page.
- **end-on-odd** -- Force the last page in this page-sequence to be an odd-page.
- **no-force** -- Do not force either an even or an odd number of pages in this page-sequence.

Whether a page is an odd-page or even-page is determined from the folio-number trait.

### initial-page-number

| Field | Value |
|---|---|
| **Values** | `auto \| auto-odd \| auto-even \| <number> \| inherit` |
| **Initial** | `auto` |
| **Applies to** | fo:page-sequence |
| **Inherited** | No |
| **Percentages** | N/A |

Sets the initial folio number to be used in this page-sequence.

Values have the following meanings:

- **auto** -- The initial folio number shall be set to 1 if no previous `fo:page-sequence` exists in the document. If a preceding page-sequence exists, the initial folio number will be one greater than the last number for that sequence.
- **auto-odd** -- A value is determined in the same manner as for "auto". If that value is an even number 1 is added.
- **auto-even** -- A value is determined in the same manner as for "auto". If that value is an odd number 1 is added.
- **\<number\>** -- A positive integer. If a non-positive or non-integer value is provided, the value will be rounded to the nearest integer value greater than or equal to 1.

### master-name

| Field | Value |
|---|---|
| **Values** | `<name>` |
| **Initial** | `an empty name` |
| **Applies to** | fo:simple-page-master, fo:page-sequence-master |
| **Inherited** | No, a value is required |
| **Percentages** | N/A |

Names identify masters, must not be empty and must be unique within an `fo:layout-master-set`.

If this property is specified on an `fo:simple-page-master`, it provides an identifying name of the master. This name is subsequently referenced as the value of properties on `fo:single-page-master-reference`, `fo:repeatable-page-master-reference`, and `fo:conditional-page-master-reference` to request the use of this master when creating a page instance. It may also be used on an `fo:page-sequence` to specify the use of this master when creating page instances.

If this property is specified on an `fo:page-sequence-master`, it provides an identifying name of the master. This name is subsequently referenced as the value of properties on the `fo:page-sequence` to request the use of this page-sequence-master when creating page instances.

A `master-name` must be unique across all page-masters and page-sequence-masters within an `fo:layout-master-set`.

### master-reference

| Field | Value |
|---|---|
| **Values** | `<name>` |
| **Initial** | `an empty name` |
| **Applies to** | fo:page-sequence, fo:single-page-master-reference, fo:repeatable-page-master-reference, fo:conditional-page-master-reference |
| **Inherited** | No, a value is required |
| **Percentages** | N/A |

The names need not be unique, but must not be empty and must refer to a `master-name` that exists within the current or a preceding `fo:layout-master-set`.

Selecting a master:

- If specified on `fo:page-sequence`, it specifies the name of the page-sequence-master or page-master to be used to create pages in the sequence.
- If specified on `fo:single-page-master-reference`, it specifies the name of the page-master to be used to create a single page instance.
- If specified on `fo:repeatable-page-master-reference`, it specifies the name of the page-master to be used in repetition until the content is exhausted or the `maximum-repeats` limit is reached.
- If specified on `fo:conditional-page-master-reference`, it specifies the name of the page-master to be used whenever this alternative is chosen.

### maximum-repeats

| Field | Value |
|---|---|
| **Values** | `<number> \| no-limit \| inherit` |
| **Initial** | `no-limit` |
| **Applies to** | fo:repeatable-page-master-reference, fo:repeatable-page-master-alternatives |
| **Inherited** | No |
| **Percentages** | N/A |

Specifies the constraint on the maximum number of pages in the sub-sequence of pages that may be generated by an `fo:page-sequence` that uses the `fo:repeatable-page-master-reference` or `fo:repeatable-page-master-alternatives` on which this property is specified.

Values have the following meanings:

- **no-limit** -- No constraint is specified.
- **\<number\>** -- The maximum number of pages in the sub-sequence. The value is an integer greater than or equal to 0. A value of 0 indicates this `master-reference` will not be used.

### media-usage

| Field | Value |
|---|---|
| **Values** | `auto \| paginate \| bounded-in-one-dimension \| unbounded` |
| **Initial** | `auto` |
| **Applies to** | fo:root |
| **Inherited** | No |
| **Percentages** | N/A |

The `media-usage` property is used to control how the selected display medium is used to present the page(s) specified by the stylesheet.

Values have the following meanings:

- **auto** -- The User Agent determines which value of `media-usage` (other than "auto") is used. The User Agent may consider the type of media on which the presentation is to be placed in making this determination.
- **paginate** -- A sequence of pages is generated from the `fo:page-sequence`s that are children of the `fo:root`.
- **bounded-in-one-dimension** -- Only one page is generated per `fo:page-sequence` descendant from the `fo:root`. Exactly one of `page-height` or `page-width` must be specified on the first page master that is used. The size of the page in the other dimension is determined by the content flowed into the page.
- **unbounded** -- Only one page is generated per `fo:page-sequence` descendant from the `fo:root`. Neither `page-height` nor `page-width` may be specified on any page master that is used. Each page extends as far as necessary to contain all the content.

### odd-or-even

| Field | Value |
|---|---|
| **Values** | `odd \| even \| any \| inherit` |
| **Initial** | `any` |
| **Applies to** | fo:conditional-page-master-reference |
| **Inherited** | No |
| **Percentages** | N/A |

This property forms part of a selection rule to determine if the referenced page-master is eligible for selection at this point in the page-sequence.

Values have the following meanings:

- **odd** -- This master is eligible for selection if the folio number is odd.
- **even** -- This master is eligible for selection if the folio number is even.
- **any** -- This master is eligible for selection regardless of whether the folio number is odd or even.

"Folio number" refers to the folio-number trait for the page to be generated.

### page-height

| Field | Value |
|---|---|
| **Values** | `auto \| indefinite \| <length> \| inherit` |
| **Initial** | `auto` |
| **Applies to** | fo:simple-page-master |
| **Inherited** | No |
| **Percentages** | N/A |

Specifies the height of a page.

Values have the following meanings:

- **auto** -- The `page-height` shall be determined, in the case of continuous media, from the size of the User Agent window, otherwise from the size of the media. If media information is not available this dimension shall be implementation-defined. A fallback to 11.0in would fit on both Letter size (8.5in by 11.0in) and A4 size pages.
- **indefinite** -- The height of the page is determined from the size of the laid-out content. `page-width` and `page-height` may not both be set to "indefinite".
- **\<length\>** -- Specifies a fixed height for the page.

### page-position

| Field | Value |
|---|---|
| **Values** | `<number> \| only \| first \| last \| rest \| any \| inherit` |
| **Initial** | `any` |
| **Applies to** | fo:conditional-page-master-reference |
| **Inherited** | No |
| **Percentages** | N/A |

This property forms part of a selection rule to determine if the referenced page-master is eligible for selection at this point in the page-sequence.

Values have the following meanings:

- **\<number\>** -- This master is eligible for selection if the value is equal to the current page number or, when the `sequence-repeats` property value is not "no-limit", at this point in the sub-sequence cycle.
- **only** -- This master is eligible for selection if this is the only page (i.e., both first and last) in the page-sequence.
- **first** -- This master is eligible for selection if this is the first page in the page-sequence.
- **last** -- This master is eligible for selection if this is the last page in the page-sequence.
- **rest** -- This master is eligible for selection if this is not the first page nor the last page in the page-sequence.
- **any** -- This master is eligible for selection regardless of page positioning within the page-sequence.

Several of these values can be true simultaneously; for example, "any" is always true and "only" is true when both "first" and "last" are true.

### page-width

| Field | Value |
|---|---|
| **Values** | `auto \| indefinite \| <length> \| inherit` |
| **Initial** | `auto` |
| **Applies to** | fo:simple-page-master |
| **Inherited** | No |
| **Percentages** | N/A |

Specifies the width of a page.

Values have the following meanings:

- **auto** -- The `page-width` shall be determined, in the case of continuous media, from the size of the User Agent window, otherwise from the size of the media. If media information is not available this dimension shall be implementation-defined. A fallback to 8.26in would fit on both 8.5x11 and A4 pages.
- **indefinite** -- The width of the page is determined from the size of the laid-out content. `page-width` and `page-height` may not both be set to "indefinite".
- **\<length\>** -- Specifies a fixed width for the page.

### precedence

| Field | Value |
|---|---|
| **Values** | `true \| false \| inherit` |
| **Initial** | `false` |
| **Applies to** | fo:region-before, fo:region-after |
| **Inherited** | No |
| **Percentages** | N/A |

Specifies which region (i.e., region-before, region-after, region-start, or region-end) takes precedence in terms of which may extend into the corners of the simple-page-master.

Values have the following meanings:

- **false** -- This region does not extend up to the start-edge and end-edge of the content-rectangle of the page-reference-area, but has its `inline-progression-dimension` reduced by the incursions of the adjacent regions.
- **true** -- The `inline-progression-dimension` of this region extends up to the start-edge and end-edge of the content-rectangle of the page-reference-area.

### region-name

| Field | Value |
|---|---|
| **Values** | `xsl-region-body \| xsl-region-start \| xsl-region-end \| xsl-region-before \| xsl-region-after \| <name>` |
| **Initial** | see prose |
| **Applies to** | fo:region-body, fo:region-before, fo:region-after, fo:region-start, fo:region-end |
| **Inherited** | No, a value is required |
| **Percentages** | N/A |

This property is used to identify a region within a simple-page-master.

The `region-name` may be used to differentiate a region that lies on a page-master for an odd page from a region that lies on a page-master for an even page. In this usage, once a name is used for a specific class of region (start, end, before, after, or body), that name may only be used for regions of the same class in any other page-master. The reserved names may only be used in the manner described above.

Reserved region-names:
- **xsl-region-body** -- Default name of `fo:region-body`. May not be used on any other class of region.
- **xsl-region-start** -- Default name of `fo:region-start`. May not be used on any other class of region.
- **xsl-region-end** -- Default name of `fo:region-end`. May not be used on any other class of region.
- **xsl-region-before** -- Default name of `fo:region-before`. May not be used on any other class of region.
- **xsl-region-after** -- Default name of `fo:region-after`. May not be used on any other class of region.
- **\<name\>** -- Names used as identifiers must be unique within a page-master.

### region-name-reference

| Field | Value |
|---|---|
| **Values** | `<name>` |
| **Initial** | none, a value is required |
| **Applies to** | fo:region-name-specifier |
| **Inherited** | No |
| **Percentages** | N/A |

Specifies a flow to be used within a sequence of regions in the flow-target-list of a particular assignment of flows to regions.

The name identifies a region; it must not be empty and must refer to a `region-name` that exists within the current or a preceding `fo:layout-master-set`.

### adjustable-properties

| Field | Value |
|---|---|
| **Values** | `<property-name-list>` |
| **Initial** | `everything` |
| **Applies to** | fo:region, fo:region-body, fo:region-before, fo:region-after, fo:region-start, fo:region-end, fo:block-container, fo:table-cell |
| **Inherited** | No |
| **Percentages** | N/A |

The `adjustable-properties` property is used to define strategies for copyfitting or vertical justification. It takes effect only if the property `display-align` is set to "copyfit" or "justify".

The value is a whitespace separated list of names (property names and/or shorthand names), possibly grouped in subsets by a single level of parenthesis. Items in the simplified value list are given decreasing priority: the first item's priority is greater than that of the second one, and so on; values between parenthesis have the same priority.

Pre-defined shorthand names:
- **inline-spacing** = word-spacing letter-spacing leader-length
- **block-spacing** = space-before space-after
- **any** = any property having a range value

### alternative-copyfit-content

The `fo:alternative-copyfit-content` formatting object is intended to express alternative content for copyfit. It might be a child of a `fo:flow` object (when copyfitting content into a region) or `fo:block-container` or `fo:table-cell` (when copyfitting content in block-containers or table cells).

The `fo:alternative-copyfit-content` formatting object does not generate any areas. It returns the areas generated and returned by its children.

## Code Samples

### Single flow mapped to a single region

<!-- Source: https://www.w3.org/TR/xslfo20/#pag-intro -->
```xml
<fo:flow flow-name="A">
  <fo:block>In the second century of
the Christian Aera, the empire of Rome ... </fo:block>
</fo:flow>
```

### Second flow mapped to a different region

<!-- Source: https://www.w3.org/TR/xslfo20/#pag-intro -->
```xml
<fo:flow flow-name="B">
  <fo:block>Quo usque tandem abutere, Catilina, patientia nostra? ...
</fo:block>
</fo:flow>
```

### Flow map E1: Two flows to two separate regions

<!-- Source: https://www.w3.org/TR/xslfo20/#pag-intro -->
```xml
<fo:flow-map flow-map-name="E1">
  <fo:flow-assignment>
    <fo:flow-source-list>
      <fo:flow-name-specifier flow-name-reference="A"/>
    </fo:flow-source-list>
    <fo:flow-target-list>
      <fo:region-name-specifier region-name-reference="R"/>
    </fo:flow-target-list>
  </fo:flow-assignment>
  <fo:flow-assignment>
    <fo:flow-source-list>
      <fo:flow-name-specifier flow-name-reference="B"/>
    </fo:flow-source-list>
    <fo:flow-target-list>
      <fo:region-name-specifier region-name-reference="S"/>
    </fo:flow-target-list>
  </fo:flow-assignment>
</fo:flow-map>
```

### Flow map E2: One flow to two regions

<!-- Source: https://www.w3.org/TR/xslfo20/#pag-intro -->
```xml
<fo:flow-map flow-map-name="E2">
  <fo:flow-assignment>
    <fo:flow-source-list>
      <fo:flow-name-specifier flow-name-reference="A"/>
    </fo:flow-source-list>
    <fo:flow-target-list>
      <fo:region-name-specifier region-name-reference="R1"/>
      <fo:region-name-specifier region-name-reference="R2"/>
    </fo:flow-target-list>
  </fo:flow-assignment>
</fo:flow-map>
```

### Flow map E3: Two flows merged into one region

<!-- Source: https://www.w3.org/TR/xslfo20/#pag-intro -->
```xml
<fo:flow-map flow-map-name="E3">
  <fo:flow-assignment>
    <fo:flow-source-list>
      <fo:flow-name-specifier flow-name-reference="A"/>
      <fo:flow-name-specifier flow-name-reference="B"/>
    </fo:flow-source-list>
    <fo:flow-target-list>
      <fo:region-name-specifier region-name-reference="R"/>
    </fo:flow-target-list>
  </fo:flow-assignment>
</fo:flow-map>
```

### Flow map E4: Two flows to two regions

<!-- Source: https://www.w3.org/TR/xslfo20/#pag-intro -->
```xml
<fo:flow-map flow-map-name="E4">
  <fo:flow-assignment>
    <fo:flow-source-list>
      <fo:flow-name-specifier flow-name-reference="A"/>
      <fo:flow-name-specifier flow-name-reference="B"/>
    </fo:flow-source-list>
    <fo:flow-target-list>
      <fo:region-name-specifier region-name-reference="R1"/>
      <fo:region-name-specifier region-name-reference="R2"/>
    </fo:flow-target-list>
  </fo:flow-assignment>
</fo:flow-map>
```

### Flow map with dependency references for multilingual parallel text

<!-- Source: https://www.w3.org/TR/xslfo20/#pag-intro -->
```xml
<fo:flow-map>
   <fo:flow-assignment>
      <fo:flow-source-list>
        <fo:flow-name-specifier
           flow-name-reference="Arabic-Flow"/>
      </fo:flow-source-list>
      <fo:flow-target-list>
         <fo:region-name-specifier
         region-name-reference="Region-Middle"/>
      </fo:flow-target-list>
   </fo:flow-assignment>
   <fo:flow-assignment flow-map-dependency-reference="Arabic-Flow">
      <fo:flow-source-list>
         <fo:flow-name-specifier
            flow-name-reference="Armenian-Flow"/>
      </fo:flow-source-list>
      <fo:flow-target-list>
         <fo:region-name-specifier
           region-name-reference="Region-Right"/>
      </fo:flow-target-list>
   </fo:flow-assignment>
   <fo:flow-assignment flow-map-dependency-reference="Arabic-Flow">
      <fo:flow-source-list>
         <fo:flow-name-specifier
          flow-name-reference="Syriac-Flow"/>
      </fo:flow-source-list>
   <fo:flow-target-list>
      <fo:region-name-specifier
        region-name-reference="Region-Left"/>
   </fo:flow-target-list>
 </fo:flow-assignment>
 </fo:flow-map>
```

### Dependent content with dependency-content-begin/end markers

<!-- Source: https://www.w3.org/TR/xslfo20/#pag-intro -->
```xml
<fo:flow flow-name="Arabic-Flow">
   …
   <fo:block dependency-content-begin="Key_A">
       And Nadan went to Haiqâr, and said to him,
       'W'allah, O my uncle! The king verily
       rejoiceth in thee for having done what he
       commanded thee.
   </fo:block>
   <fo:block>
       And now he hath sent me to thee that thou
       mayst dismiss the soldiers to their duties
       and come thyself to him with thy handsbound
       behind thee, and thy feet chained, that the
       ambassadors of Pharaoh may see this, and
       that the king may be feared by them and by
       their king'.
   </fo:block>
   <fo:block>
       And Nadan took him and went with him to the
       king.
   </fo:block>
   <fo:block dependency-content-end="Key_A">
       Then answered Haiqâr and said, 'To hear is
       to obey.'
   </fo:block>
   …
 </fo:flow>
```

### keep-with-dependent-content example

<!-- Source: https://www.w3.org/TR/xslfo20/#pag-intro -->
```xml
<fo:block keep-with-dependent-content="widows"
          dependent-content-begin="Key_A">
    Text text text …
   <fo:inline dependent-content-end="Key_A">
       Text text …
   </fo:inline>
    Text text text …
 </fo:block>
 <fo:block keep-with-dependent-content="all">
     Text text text …
     <fo:block dependent-content-begin="Key_B">
         Text text …
     </fo:inline>
     Text text text …
 </fo:block>
```

### Extension regions with page master

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_extension-region -->
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

### adjustable-properties syntax definition

<!-- Source: https://www.w3.org/TR/xslfo20/#adjustable-properties -->
```xml
prioritized-list-of-names = [<priority-group>]*
		priority-group = <property-name> | <shorthand-name> |
                ([<property-name> | <shorthand-name>]+)
```

### fo:alternative-copyfit-content content model

<!-- Source: https://www.w3.org/TR/xslfo20/#adjustable-properties -->
```xml
(%block;)*
```

### fo:alternative-copyfit-content example with copyfitting

<!-- Source: https://www.w3.org/TR/xslfo20/#adjustable-properties -->
```xml
<fo:flow flow-name="A">
 <fo:alternative-copyfit-content>
<fo:block word-spacing.minimum="1pt" word-spacing.maximum="4pt"
line-height.minimum="8pt" line-height.maximum="14pt">Crucis rosa ut
hoc sien qua non res veni.</fo:block>
<fo:block word-spacing.minimum="1pt" word-spacing.maximum="4pt"
line-height.minimum="8pt" line-height.maximum="14pt"> Etiam tristique,
nulla a pulvinar hendrerit nihil tortor urna auctor etim
domine secularia cali sed ut quotie ire in domince hoc fantus quis eius rei rei.
</fo:block>
 </fo:alternative-copyfit-content>

<fo:block word-spacing.minimum="1pt" word-spacing.maximum="4pt"
line-height.minimum="8pt" line-height.maximum="14pt">
Lorem maecenas blandit ac, neque sed ut pulvinar, lectus sagittis
sapien per risus vel.  Ligula sapien sed morbi cras tellus commodo.
Si qua ex docet dei etris crucis</fo:block>
<fo:block word-spacing.minimum="1pt" word-spacing.maximum="4pt"
line-height.minimum="8pt" line-height.maximum="14pt"> curabitur
magna nis, faucibus sed ornare sed, congue eu dui.
Pellentesque habitant morbi tristique senectus et netus et
malessecularia uada fames ac turpis egestas. </fo:block>
<fo:block word-spacing.minimum="1pt" word-spacing.maximum="4pt"
line-height.minimum="8pt" line-height.maximum="14pt"> Nunc sit amet dolor
sed sem congue mattis sed ut arcu. Mauris id magna sit amet elit aliquam.</fo:block>
<fo:block>Pellentesque habitant morbi tristique senectus et netus et malesuada
fames.</fo:block>
</fo:flow>
```

## See Also

- [fo-simple-page-master](fo-simple-page-master.md) -- The `fo:simple-page-master` formatting object
- [fo-page-sequence-master](fo-page-sequence-master.md) -- The `fo:page-sequence-master` formatting object
- [fo-page-sequence](fo-page-sequence.md) -- The `fo:page-sequence` formatting object
- [fo-flow](fo-flow.md) -- The `fo:flow` formatting object
- [fo-static-content](fo-static-content.md) -- The `fo:static-content` formatting object
- [fo-flow-map](fo-flow-map.md) -- The `fo:flow-map` formatting object
- [fo-region-body](fo-region-body.md) -- The `fo:region-body` formatting object
- [fo-region-before](fo-region-before.md) -- The `fo:region-before` formatting object
- [fo-region-after](fo-region-after.md) -- The `fo:region-after` formatting object
- [fo-conditional-page-master-reference](fo-conditional-page-master-reference.md) -- The `fo:conditional-page-master-reference` formatting object
- [fo-alternative-copyfit-content](fo-alternative-copyfit-content.md) -- The `fo:alternative-copyfit-content` formatting object
