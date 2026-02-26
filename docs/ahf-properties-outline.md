# Antenna House Extension Properties: Outline (Bookmark) Extension Properties

<!-- Source: XSL-FO-Reference-74-MID.pdf pp.312–476 -->

Properties for controlling PDF outline (bookmark) generation from block-level formatting objects, including outline title, destination, styling (color, font style, font weight), grouping, and expansion state.

## axf:outline-color

Specifies the color which appears as a title of bookmarks. When transparent is specified, the color information is not set to PDF. This property is effective with PDF1.4 or later.

| Attribute | Value |
|---|---|
| **Applies to** | block-level formatting objects |
| **Values** | &lt;color&gt; |
| **Initial** | transparent |
| **Inherited** | no |

## axf:outline-expand

Specifies whether to display the lower hierarchy of bookmark items or not. true specifies to display the lower hierarchy in the expanded state. false specifies to display in the collapsed state.

| Attribute | Value |
|---|---|
| **Applies to** | block-level formatting objects |
| **Values** | true \| false |
| **Initial** | true |
| **Inherited** | no |

## axf:outline-external-destination

Sets the external link in the PDF bookmark. Values have the following meanings:

- **&lt;uri-specification&gt;**: Specifies the URI of the link destination.

| Attribute | Value |
|---|---|
| **Applies to** | block-level formatting objects |
| **Values** | &lt;uri-specification&gt; |
| **Initial** | empty string |
| **Inherited** | no |

## axf:outline-font-style

Specifies the font style which appears as a title of bookmarks. This property is effective with PDF1.4 or later. Values have the following meanings:

- **normal**: Specifies normal style.
- **italic**: Specifies italic.

| Attribute | Value |
|---|---|
| **Applies to** | block-level formatting objects |
| **Values** | normal \| italic |
| **Initial** | normal |
| **Inherited** | no |

## axf:outline-font-weight

Specifies the font weight which appears as a title of bookmarks. This property is effective with PDF1.4 or later. Values have the following meanings:

- **normal**: Specifies normal weight.
- **bold**: Specifies bold weight.

| Attribute | Value |
|---|---|
| **Applies to** | block-level formatting objects |
| **Values** | normal \| bold |
| **Initial** | normal |
| **Inherited** | no |

## axf:outline-group

Groups bookmark items, and outputs them collectively. If this property is omitted or specifies empty string, bookmark items are not grouped. If this specifies any string, the string is used as the name of group. The group with the same name is outputted collectively. The non-grouped bookmark is outputted as the group without the group name.

| Attribute | Value |
|---|---|
| **Applies to** | block-level formatting objects |
| **Values** | &lt;string&gt; |
| **Initial** | empty string |
| **Inherited** | no |

## axf:outline-internal-destination

Sets the internal link in the PDF bookmark. Values have the following meanings:

- **&lt;idref&gt;**: Specifies the ID of the link destination.
- **&lt;number-with-fragment&gt;**: Specifies the page number of the link destination. This string is simple numeric characters or the following string that combines numeric characters and a fragment with "#". For example: `123#zoom=50`. The page number also can be specified in the fragment: `#page=123&zoom=50`. When the page number is not specified, it is usually considered the 1st page. However, when the top position is specified, it is considered the head of the page of a block where axf:outline-internal-destination is contained. For example: `#view=fit`, `#view=fith`, `#zoom=,,0`.

| Attribute | Value |
|---|---|
| **Applies to** | block-level formatting objects |
| **Values** | &lt;idref&gt; \| &lt;number-with-fragment&gt; |
| **Initial** | empty string |
| **Inherited** | no |

## axf:outline-level

Indicates the hierarchy level of bookmark items. The value must be a non-negative integer. Initial value is 0 and it means that bookmarks should not be created. The highest level of bookmarks is 1 and it becomes 2 or more according to the hierarchy level of the bookmarks.

| Attribute | Value |
|---|---|
| **Applies to** | block-level formatting objects |
| **Values** | &lt;number&gt; |
| **Initial** | 0 |
| **Inherited** | no |

## axf:outline-title

Specifies the string which appears as a title of bookmarks. If this property is omitted or has an empty string, the text of the object to which the property is added will become the title. In other words, the following two samples create the same bookmark:

```xml
<fo:block axf:outline-level="2" axf:outline-title="1. Introduction">...
<fo:block axf:outline-level="2">1. Introduction</fo:block>
```

| Attribute | Value |
|---|---|
| **Applies to** | block-level formatting objects |
| **Values** | &lt;string&gt; |
| **Initial** | empty string |
| **Inherited** | no |
