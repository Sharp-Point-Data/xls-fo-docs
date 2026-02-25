# Dynamic Effects Properties

<!-- Source: https://www.w3.org/TR/xslfo20/#active-state -->

## Overview

The dynamic effects properties control interactive behaviors in XSL-FO documents, including link navigation, multi-case switching (show/hide), and multi-property state changes (hover, visited, active, etc.). These properties are primarily used with the dynamic effects formatting objects: `fo:basic-link`, `fo:multi-switch`, `fo:multi-case`, `fo:multi-toggle`, `fo:multi-properties`, and `fo:multi-property-set`.

Most dynamic effects properties apply to interactive media and are not inherited. They enable behaviors such as expandable/collapsible content, hyperlinks to internal and external destinations, and CSS-like pseudo-class styling for links.

## Properties

### active-state

| Field | Value |
|---|---|
| **Values** | `link \| visited \| active \| hover \| focus` |
| **Initial** | no, a value is required |
| **Applies to** | fo:multi-property-set |
| **Inherited** | No |
| **Percentages** | N/A |

The `active-state` property is used to control which of the `fo:multi-property-set`s are used to format the child flow objects within an `fo:multi-properties` formatting object. The states (or at least the events that cause the state to be entered) are defined by the DOM.

Values have the following meanings:

- **link** -- This `fo:multi-property-set` applies if there is an `fo:basic-link` descendant of the parent `fo:multi-properties` and that link has not yet been visited.
- **visited** -- This `fo:multi-property-set` applies if there is an `fo:basic-link` descendant of the parent `fo:multi-properties` and that link has been visited.
- **active** -- This `fo:multi-property-set` applies while a normal area returned by the parent `fo:multi-properties` is being activated by the user. For example, between the times the user presses the mouse button and releases it.
- **hover** -- This `fo:multi-property-set` applies while the user designates a normal area returned by the parent `fo:multi-properties` (with some pointing device), but does not activate it. For example the cursor (mouse pointer) hovers over such an area.
- **focus** -- This `fo:multi-property-set` applies while a normal area returned by the parent `fo:multi-properties` has the focus (accepts keyboard events or other forms of text input).

### auto-restore

| Field | Value |
|---|---|
| **Values** | `true \| false` |
| **Initial** | `false` |
| **Applies to** | fo:multi-switch |
| **Inherited** | Yes |
| **Percentages** | N/A |

Specifies if the initial `fo:multi-case` should be restored when the `fo:multi-switch` gets hidden by an ancestor `fo:multi-switch`.

Values have the following meanings:

- **true** -- If this `fo:multi-switch` is contained in another `fo:multi-switch`, and that `fo:multi-switch` changes the active `fo:multi-case` (hiding this `fo:multi-switch`), then this `fo:multi-switch` should restore its initial `fo:multi-case`.
- **false** -- This `fo:multi-switch` should retain its current `fo:multi-case`.

A common case of using this property with a "true" value is when several nested `fo:multi-switch` objects build an expandable/collapsible table-of-contents view. If the table-of-contents is expanded far down the hierarchy, and an (far above) ancestor is closed, one would want all subtitles to have restored to their original state when that ancestor is opened again.

### case-name

| Field | Value |
|---|---|
| **Values** | `<name>` |
| **Initial** | none, a value is required |
| **Applies to** | fo:multi-case |
| **Inherited** | No |
| **Percentages** | N/A |

Specifies a name for an `fo:multi-case`. The name must be unique among the current `fo:multi-case` siblings, i.e., in the scope of the `fo:multi-switch` object that (directly) contains them. Other instances of `fo:multi-switch` objects may use the same names for its `fo:multi-case` objects.

The purpose of this property is to allow `fo:multi-toggle` objects to select `fo:multi-case` objects to switch to.

### case-title

| Field | Value |
|---|---|
| **Values** | `<string>` |
| **Initial** | none, a value is required |
| **Applies to** | fo:multi-case |
| **Inherited** | No |
| **Percentages** | N/A |

Specifies a descriptive title for the `fo:multi-case`. The title can be displayed in a menu to represent this `fo:multi-case` when an `fo:multi-toggle` object names several `fo:multi-case` objects as allowed destinations.

### destination-placement-offset

| Field | Value |
|---|---|
| **Values** | `<length>` |
| **Initial** | `0pt` |
| **Applies to** | fo:basic-link |
| **Inherited** | No |
| **Percentages** | N/A |

The `destination-placement-offset` property specifies the distance from the beginning (top) of the page to the innermost line-area that contains the first destination area.

If the first destination area is not contained in a line-area, the `destination-placement-offset` property instead directly specifies the distance to the top of the destination area.

If the specification of `destination-placement-offset` would result in a distance longer than the distance from the start of the document, the distance from the start of the document should be used.

If the specified distance would push the first destination area below the page-area, the distance should be decreased so the whole first destination area becomes visible, if possible. If the first destination area is higher than the page, the top of the area should be aligned with the top of the page.

### external-destination

| Field | Value |
|---|---|
| **Values** | `empty string \| <uri-specification>` |
| **Initial** | `empty string` |
| **Applies to** | fo:basic-link |
| **Inherited** | No |
| **Percentages** | N/A |

Specifies the destination resource (or, when a fragment identifier is given, sub-resource).

How the destination (sub-)resource is used and/or displayed is application and implementation-dependent. In typical browsing applications, the destination resource is displayed in the browser positioned so that some rendered portion resulting from the processing of some part of the specific destination sub-resource indicated by the fragment identifier is in view.

### indicate-destination

| Field | Value |
|---|---|
| **Values** | `true \| false` |
| **Initial** | `false` |
| **Applies to** | fo:basic-link |
| **Inherited** | No |
| **Percentages** | N/A |

Values have the following meanings:

- **true** -- The areas that belong to the link target when traversed should, in a system-dependent manner, be indicated. This could be indicated in any feasible way, e.g., by reversed video, etc.
- **false** -- No special indication should be made.

### internal-destination

| Field | Value |
|---|---|
| **Values** | `empty string \| <idref>` |
| **Initial** | `empty string` |
| **Applies to** | fo:basic-link |
| **Inherited** | No |
| **Percentages** | N/A |

Specifies the destination flow object within the formatting object tree. This property allows the destination flow object node to be explicitly specified.

### show-destination

| Field | Value |
|---|---|
| **Values** | `replace \| new` |
| **Initial** | `replace` |
| **Applies to** | fo:basic-link |
| **Inherited** | No |
| **Percentages** | N/A |

Specifies where the destination resource should be displayed.

Values have the following meanings:

- **replace** -- The current document view should be replaced. However, if the destination area(s) are already available in a page/region, those areas should simply be moved/scrolled "into sight".
- **new** -- A new (additional) document view should always be opened.

### starting-state

| Field | Value |
|---|---|
| **Values** | `show \| hide` |
| **Initial** | `show` |
| **Applies to** | fo:multi-case, fo:bookmark |
| **Inherited** | No |
| **Percentages** | N/A |

Specifies how the formatting object to which it applies is initially displayed.

Values have the following meanings:

- **show** -- The content of the formatting object is a candidate for being displayed initially.
- **hide** -- The content of the formatting object is not a candidate for being displayed initially.

For details of the typical usage of this property, see the description of `fo:multi-switch` and `fo:bookmark`.

### switch-to

| Field | Value |
|---|---|
| **Values** | `xsl-preceding \| xsl-following \| xsl-any \| <name>[ <name>]*` |
| **Initial** | `xsl-any` |
| **Applies to** | fo:multi-toggle |
| **Inherited** | No |
| **Percentages** | N/A |

Specifies what `fo:multi-case` object(s) this `fo:multi-toggle` shall switch to.

If `switch-to` is a name list, the user can switch to any of the named multi-case objects. If a multi-toggle with a single name is activated, it should immediately switch to the named multi-case.

Values have the following meanings:

- **xsl-preceding** -- Activating the switch should result in the current `fo:multi-case` being replaced by its preceding sibling. The current `fo:multi-case` is the closest ancestor `fo:multi-case`. If the current `fo:multi-case` is the first sibling, xsl-preceding should switch to the last `fo:multi-case` sibling.
- **xsl-following** -- Activating the switch should result in that the current `fo:multi-case` is replaced by its next sibling. If the current `fo:multi-case` is the last sibling, xsl-following should switch to the first `fo:multi-case` sibling.
- **xsl-any** -- Activating the switch should allow the user to select any other `fo:multi-case` sibling. If there is only a single other `fo:multi-case`, the toggle should immediately switch to it (and not show that single choice to the user).
- **\<name\>** -- A name matching a `case-name` of an `fo:multi-case`.

How to actually select the multi-case from a list is system dependent.

### target-presentation-context

| Field | Value |
|---|---|
| **Values** | `use-target-processing-context \| <uri-specification>` |
| **Initial** | `use-target-processing-context` |
| **Applies to** | fo:basic-link |
| **Inherited** | No |
| **Percentages** | N/A |

Values have the following meanings:

- **use-target-processing-context** -- The context specified by the `target-processing-context` property shall be used.
- **\<uri-specification\>** -- Specifies the limited context in which the resource should be presented if the external destination is a resource of a processed structured media type for which a limited presentational context makes sense (e.g., XML, XHTML, SVG).

This property is ignored if the `external-destination` property has an empty string value or if the external destination is not of a processed structured media type for which a limited presentational context makes sense.

For example, an XML and XSL implementation may parse the XML document, but begin XSLT processing by applying templates to the node set indicated by the `target-presentation-context` property.

If this is a node other than the document root, numbering and other contextually-dependent presentation may differ between implementations. Some implementations may want to make this tradeoff for memory or performance reasons.

### target-processing-context

| Field | Value |
|---|---|
| **Values** | `document-root \| <uri-specification>` |
| **Initial** | `document-root` |
| **Applies to** | fo:basic-link |
| **Inherited** | No |
| **Percentages** | N/A |

Values have the following meanings:

- **document-root** -- The root of the document of the `external-destination` is used.
- **\<uri-specification\>** -- Specifies the root of a virtual document that the processor preparing the new presentation should process if the external destination is a resource of a processed structured media type (e.g., XML, SVG).

This property is ignored if the `external-destination` property has an empty string value or if the external destination is not of a processed structured media type.

Not all URI-specifications will be sensible roots, e.g., an XPointer that gives a string range into an XML document. If the root is not valid for the media type the processor may ignore this property.

### target-stylesheet

| Field | Value |
|---|---|
| **Values** | `use-normal-stylesheet \| <uri-specification>` |
| **Initial** | `use-normal-stylesheet` |
| **Applies to** | fo:basic-link |
| **Inherited** | No |
| **Percentages** | N/A |

Values have the following meanings:

- **use-normal-stylesheet** -- The implementation will discover stylesheets using its usual methods. For example from HTTP header information, XML stylesheet processing instructions, or XHTML style and link elements.
- **\<uri-specification\>** -- Specifies the stylesheet that shall be used for processing the resource. This stylesheet shall be used instead of any other stylesheet that otherwise would be used.

This property is ignored if the `external-destination` property has an empty string value or if the external destination is not of a media type that uses stylesheets.

In this version of XSL, only a single stylesheet URI-specification is permitted. A future version of XSL may extend the stylesheet specification.

## Code Samples

### Sample XML source document for TOC example

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_list-item-label -->
```xml
<doc>
  <chapter><title>Chapter</title>
    <p>Text</p>
    <section><title>Section</title>
    <p>Text</p>
    </section>
    <section><title>Section</title>
    <p>Text</p>
    </section>
  </chapter>
  <chapter><title>Chapter</title>
    <p>Text</p>
    <section><title>Section</title>
    <p>Text</p>
    </section>
    <section><title>Section</title>
    <p>Text</p>
    </section>
  </chapter>
</doc>
```

### XSLT stylesheet for expandable/collapsible TOC using fo:multi-switch

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_list-item-label -->
```xml
<?xml version='1.0'?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
                xmlns:fo="http://www.w3.org/1999/XSL/Format"
                version='1.0'>

<xsl:template match="doc">
  <!-- create the table of contents -->
  <xsl:apply-templates select="chapter/title" mode="toc"/>
  <!-- do the document -->
  <xsl:apply-templates/>
</xsl:template>

<xsl:template match="chapter/title" mode="toc">
  <fo:multi-switch>
    <fo:multi-case case-name="collapsed" case-title="collapsed"
    starting-state="show">
      <fo:block>
        <fo:multi-toggle switch-to="expanded">
          <fo:external-graphic href="plus-icon.gif"/>
        </fo:multi-toggle>
        <fo:basic-link internal-destination="{generate-id(.)}">
          <xsl:number level="multiple" count="chapter" format="1. "/>
          <xsl:apply-templates mode="toc"/>
        </fo:basic-link>
      </fo:block>
    </fo:multi-case>
    <fo:multi-case case-name="expanded" case-title="expanded"
    starting-state="hide">
      <fo:block>
        <fo:multi-toggle switch-to="collapsed">
          <fo:external-graphic href="minus-icon.gif"/>
        </fo:multi-toggle>
        <fo:basic-link internal-destination="{generate-id(.)}">
          <xsl:number level="multiple" count="chapter" format="1. "/>
          <xsl:apply-templates mode="toc"/>
        </fo:basic-link>
      </fo:block>
      <xsl:apply-templates select="../section/title" mode="toc"/>
    </fo:multi-case>
  </fo:multi-switch>
</xsl:template>

<xsl:template match="section/title" mode="toc">
  <fo:block start-indent="10mm">
    <fo:basic-link internal-destination="{generate-id(.)}">
      <xsl:number level="multiple" count="chapter|section" format="1.1 "/>
      <xsl:apply-templates/>
    </fo:basic-link>
  </fo:block>
</xsl:template>

<xsl:template match="chapter/title">
  <fo:block id="{generate-id(.)}">
    <xsl:number level="multiple" count="chapter" format="1. "/>
    <xsl:apply-templates/>
  </fo:block>
</xsl:template>

<xsl:template match="section/title">
  <fo:block id="{generate-id(.)}">
    <xsl:number level="multiple" count="chapter|section" format="1.1 "/>
    <xsl:apply-templates/>
  </fo:block>
</xsl:template>

<xsl:template match="p">
  <fo:block>
    <xsl:apply-templates/>
  </fo:block>
</xsl:template>

</xsl:stylesheet>
```

### XSL-FO output of the expandable/collapsible TOC

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_list-item-label -->
```xml
<fo:multi-switch>
  <fo:multi-case case-name="collapsed" case-title="collapsed" starting-state="show">
    <fo:block>
      <fo:multi-toggle switch-to="expanded">
        <fo:external-graphic href="plus-icon.gif">
        </fo:external-graphic>
      </fo:multi-toggle>
      <fo:basic-link internal-destination="N4">1. Chapter
      </fo:basic-link>
    </fo:block>
  </fo:multi-case>
  <fo:multi-case case-name="expanded" case-title="expanded" starting-state="hide">
    <fo:block>
      <fo:multi-toggle switch-to="collapsed">
        <fo:external-graphic href="minus-icon.gif">
        </fo:external-graphic>
      </fo:multi-toggle>
      <fo:basic-link internal-destination="N4">1. Chapter
      </fo:basic-link>
    </fo:block>
    <fo:block start-indent="10mm">
      <fo:basic-link internal-destination="N11">1.1 Section
      </fo:basic-link>
    </fo:block>
    <fo:block start-indent="10mm">
      <fo:basic-link internal-destination="N19">1.2 Section
      </fo:basic-link>
    </fo:block>
  </fo:multi-case>
</fo:multi-switch>
<fo:multi-switch>
  <fo:multi-case case-name="collapsed" case-title="collapsed" starting-state="show">
    <fo:block>
      <fo:multi-toggle switch-to="expanded">
        <fo:external-graphic href="plus-icon.gif">
        </fo:external-graphic>
      </fo:multi-toggle>
      <fo:basic-link internal-destination="N28">2. Chapter
      </fo:basic-link>
    </fo:block>
  </fo:multi-case>
  <fo:multi-case case-name="expanded" case-title="expanded" starting-state="hide">
    <fo:block>
      <fo:multi-toggle switch-to="collapsed">
        <fo:external-graphic href="minus-icon.gif">
        </fo:external-graphic>
      </fo:multi-toggle>
      <fo:basic-link internal-destination="N28">2. Chapter
      </fo:basic-link>
    </fo:block>
    <fo:block start-indent="10mm">
      <fo:basic-link internal-destination="N35">2.1 Section
      </fo:basic-link>
    </fo:block>
    <fo:block start-indent="10mm">
      <fo:basic-link internal-destination="N43">2.2 Section
      </fo:basic-link>
    </fo:block>
  </fo:multi-case>
</fo:multi-switch>

<fo:block id="N4">1. Chapter
</fo:block>
<fo:block>Text
</fo:block>
<fo:block id="N11">1.1 Section
</fo:block>
<fo:block>Text
</fo:block>
<fo:block id="N19">1.2 Section
</fo:block>
<fo:block>Text
</fo:block>
<fo:block id="N28">2. Chapter
</fo:block>
<fo:block>Text
</fo:block>
<fo:block id="N35">2.1 Section
</fo:block>
<fo:block>Text
</fo:block>
<fo:block id="N43">2.2 Section
</fo:block>
<fo:block>Text
</fo:block>
```

### XLink source document for link example

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_list-item-label -->
```xml
<p>Follow this <xlink:mylink xmlns:xlink="http://www.w3.org/1999/xlink"
        xlink:href="http://www.w3.org/TR"
        xlink:title="An Example"
        xlink:show="new"
        xlink:actuate="onRequest">link</xlink:mylink> to access all
TRs of the W3C.</p>
```

### XSLT stylesheet for fo:multi-properties link styling

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_list-item-label -->
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

<xsl:template match="xlink:mylink" xmlns:xlink="http://www.w3.org/1999/xlink">
    <xsl:variable name="show"><xsl:value-of select="@xlink:show"/>
    </xsl:variable>
     <fo:multi-properties text-decoration="underline">
        <fo:multi-property-set active-state="link" color="blue"/>
        <fo:multi-property-set active-state="visited" color="red"/>
        <fo:multi-property-set active-state="active" color="green"/>
        <fo:multi-property-set active-state="hover" text-decoration="blink"/>
        <fo:multi-property-set active-state="focus" color="yellow"/>
        <fo:wrapper color="merge-property-values()"
                    text-decoration="merge-property-values()">
              <fo:basic-link external-destination="http://www.w3.org/TR"
                              show-destination="{$show}">
                  <xsl:attribute name="role">
                      <xsl:value-of select="@xlink:title"/>
                  </xsl:attribute>
                  <xsl:apply-templates/>
              </fo:basic-link>
        </fo:wrapper>
      </fo:multi-properties>
</xsl:template>

</xsl:stylesheet>
```

### XSL-FO output of the multi-properties link styling

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_list-item-label -->
```xml
<fo:block>Follow this
  <fo:multi-properties text-decoration="underline">
    <fo:multi-property-set active-state="link" color="blue">
    </fo:multi-property-set>
    <fo:multi-property-set active-state="visited" color="red">
    </fo:multi-property-set>
    <fo:multi-property-set active-state="active" color="green">
    </fo:multi-property-set>
    <fo:multi-property-set active-state="hover" text-decoration="blink">
    </fo:multi-property-set>
    <fo:multi-property-set active-state="focus" color="yellow">
    </fo:multi-property-set>
    <fo:wrapper color="merge-property-values()"
      text-decoration="merge-property-values()">
      <fo:basic-link external-destination="http://www.w3.org/TR"
        show-destination="new" role="An Example">link
      </fo:basic-link>
    </fo:wrapper>
  </fo:multi-properties> to access all
TRs of the W3C.
</fo:block>
```

## See Also

- [fo-basic-link](fo-basic-link.md) -- The `fo:basic-link` formatting object
- [fo-multi-switch](fo-multi-switch.md) -- The `fo:multi-switch` formatting object
- [fo-multi-case](fo-multi-case.md) -- The `fo:multi-case` formatting object
- [fo-multi-toggle](fo-multi-toggle.md) -- The `fo:multi-toggle` formatting object
- [fo-multi-properties](fo-multi-properties.md) -- The `fo:multi-properties` formatting object
- [fo-multi-property-set](fo-multi-property-set.md) -- The `fo:multi-property-set` formatting object
