# Antenna House Extension Properties: Suppression Properties

<!-- Source: XSL-FO-Reference-74-MID.pdf pp.312-476 -->

Properties for suppressing duplicate content in output, including duplicate footnotes, duplicate page numbers, duplicate marker contents, and folio prefix/suffix suppression.

## axf:suppress-duplicate-footnote

Specifies whether to delete footnotes duplicated in the same page. Deters the display of duplicated footnotes on the same footnote region when the same footnote is assigned to two or more places in the same page. When axf:footnote-position="column" is specified, it is effective only for the footnote in the same column.

| Attribute | Value |
|---|---|
| **Applies to** | fo:footnote |
| **Values** | true \| false |
| **Initial** | false |
| **Inherited** | yes |

## axf:suppress-duplicate-marker-contents

Specifies the removal of duplicate marker references. When inline consecutive fo:retrieve-marker refer to fo:marker with the same content, one fo:retrieve-marker is removed. For example, in the following case, text and elements between fo:retrieve-marker are also removed:

```xml
<fo:retrieve-marker/> — <fo:retrieve-marker/>
```

It does not work in the following cases:
- When fo:marker is not an inline element
- When fo:retrieve-marker is not a sibling element.

The same applies to inline consecutive fo:retrieve-marker.

| Attribute | Value |
|---|---|
| **Applies to** | all formatting objects |
| **Values** | true \| false |
| **Initial** | false |
| **Inherited** | yes |

## axf:suppress-duplicate-page-number

Specifies to delete the duplicated page numbers.

CAUTION: A similar function is provided in XSL 1.1. Use merge-*-index-key-reference.

When formatting an index, generally several fo:page-number-citation line up for one index item. In such case, when fo:page-number-citation refers to the same page number of the index, duplicate page numbers will be output using the standard property. If true is specified, when the same page number of the previous fo:page-number-citation is referred, that page number will be hidden along with the intervening elements (such as commas).

| Attribute | Value |
|---|---|
| **Applies to** | all formatting objects |
| **Values** | true \| false |
| **Initial** | false |
| **Inherited** | yes |

## axf:suppress-folio-prefix

Invalidates the prefix of page numbers. Specifies whether to invalidate the prefix set by fo:folio-prefix.

Values have the following meanings:
- `true`: Invalidates the prefix.
- `false`: Validates the prefix.

| Attribute | Value |
|---|---|
| **Applies to** | fo:page-number, fo:page-number-citation, fo:page-number-citation-last |
| **Values** | true \| false |
| **Initial** | false |
| **Inherited** | no |

## axf:suppress-folio-suffix

Invalidates the suffix of page numbers. Specifies whether to invalidate the suffix set by fo:folio-suffix.

Values have the following meanings:
- `true`: Invalidates the suffix.
- `false`: Validates the suffix.

| Attribute | Value |
|---|---|
| **Applies to** | fo:page-number, fo:page-number-citation, fo:page-number-citation-last |
| **Values** | true \| false |
| **Initial** | false |
| **Inherited** | no |

## axf:suppress-if-first-on-page

Specifies whether to suppress the block at the beginning of a page or column.

Values have the following meanings:
- `false`: Does nothing.
- `true`: Suppresses a block when it comes at the beginning of a page or column. Actually, it is hidden but exists as a block of zero size without being deleted, it's effective to refer to id, etc.
- `unless`: Suppresses a block when it comes to a place other than the beginning of a page or column. Actually, it is hidden but exists as a block of zero size without being deleted, it's effective to refer to id, etc.

| Attribute | Value |
|---|---|
| **Applies to** | fo:block, fo:block-container |
| **Values** | true \| false \| unless |
| **Initial** | false |
| **Inherited** | no |
