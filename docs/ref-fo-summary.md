# Formatting Object Summary

<!-- Source: https://www.w3.org/TR/xslfo20/#FO-summary -->

## Overview

Quick-reference summary of all XSL-FO formatting objects, organized by category. Each table lists the conformance level for the visual and aural media classes. The spec defines two conformance levels relevant here: **basic** (minimum conformance) and **extended** (sophisticated pagination). Where a formatting object is extended, a proposed fallback treatment is specified. For a full description of conformance levels, see the [Conformance](ref-conformance.md) reference.

For certain formatting objects (see [Link and Multi FOs](#link-and-multi-fos)), the visual class is further subdivided into interactive and non-interactive media.

## Declaration and Pagination and Layout FOs

| Formatting Object | Visual | Aural |
|---|---|---|
| `fo:root` | basic | basic |
| `fo:page-sequence` | basic | basic |
| `fo:page-sequence-wrapper` | basic | basic |
| `fo:page-sequence-master` | basic | basic |
| `fo:single-page-master-reference` | basic | basic |
| `fo:repeatable-page-master-reference` | basic | basic |
| `fo:repeatable-page-master-alternatives` | extended | extended |
| `fo:conditional-page-master-reference` | extended | extended |
| `fo:layout-master-set` | basic | basic |
| `fo:simple-page-master` | basic | basic |
| `fo:region-body` | basic | basic |
| `fo:region-before` | extended | extended |
| `fo:region-after` | extended | extended |
| `fo:region-start` | extended | extended |
| `fo:region-end` | extended | extended |
| `fo:declarations` | basic | basic |
| `fo:color-profile` | extended | N/A |
| `fo:flow` | basic | basic |
| `fo:static-content` | extended | extended |
| `fo:title` | extended | extended |
| `fo:flow-map` | extended | extended |
| `fo:flow-assignment` | extended | extended |
| `fo:flow-source-list` | extended | extended |
| `fo:flow-name-specifier` | extended | extended |
| `fo:flow-target-list` | extended | extended |
| `fo:region-name-specifier` | extended | extended |

### Extended Fallbacks (Declaration and Pagination)

| Formatting Object | Visual Fallback | Aural Fallback |
|---|---|---|
| `fo:repeatable-page-master-alternatives` | Use the page-master referenced in the first `fo:conditional-page-master-reference` child | Use the page-master referenced in the first `fo:conditional-page-master-reference` child |
| `fo:conditional-page-master-reference` | Use the page-master referenced in the first `fo:conditional-page-master-reference` child | Use the page-master referenced in the first `fo:conditional-page-master-reference` child |
| `fo:region-before` | Include after content of body region is placed | Include after content of body region is spoken |
| `fo:region-after` | Include after content of body region is placed | Include after content of body region is spoken |
| `fo:region-start` | Include after content of body region is placed | Include after content of body region is spoken |
| `fo:region-end` | Include after content of body region is placed | Include after content of body region is spoken |
| `fo:color-profile` | Ignore, use the sRGB fallback of the rgb-icc function | N/A |
| `fo:static-content` | Include after content of body region is placed | Include after content of body region is spoken |
| `fo:title` | Include before content of body region is placed | Include before content of body region is spoken |
| `fo:flow-map` | Display an indication that content cannot be correctly rendered | Speak an indication that content cannot be correctly spoken |
| `fo:flow-assignment` | Ignore | Ignore |
| `fo:flow-source-list` | Ignore | Ignore |
| `fo:flow-name-specifier` | Ignore | Ignore |
| `fo:flow-target-list` | Ignore | Ignore |
| `fo:region-name-specifier` | Ignore | Ignore |

## Block FOs

| Formatting Object | Visual | Aural |
|---|---|---|
| `fo:block` | basic | basic |
| `fo:block-container` | extended | basic |

### Extended Fallbacks (Block)

| Formatting Object | Visual Fallback | Aural Fallback |
|---|---|---|
| `fo:block-container` | Display indication that content cannot be correctly rendered | N/A (basic for aural) |

## Inline FOs

| Formatting Object | Visual | Aural |
|---|---|---|
| `fo:bidi-override` | extended | basic |
| `fo:character` | basic | basic |
| `fo:initial-property-set` | extended | basic |
| `fo:external-graphic` | basic | basic |
| `fo:instream-foreign-object` | extended | extended |
| `fo:inline` | basic | basic |
| `fo:inline-container` | extended | extended |
| `fo:leader` | basic | basic |
| `fo:page-number` | basic | extended |
| `fo:page-number-citation` | extended | extended |
| `fo:page-number-citation-last` | extended | extended |
| `fo:folio-prefix` | extended | extended |
| `fo:folio-suffix` | extended | extended |
| `fo:scaling-value-citation` | extended | extended |

### Extended Fallbacks (Inline)

| Formatting Object | Visual Fallback | Aural Fallback |
|---|---|---|
| `fo:bidi-override` | Display indication that content cannot be correctly rendered | N/A (basic for aural) |
| `fo:initial-property-set` | Ignore any properties specified on this object | N/A (basic for aural) |
| `fo:instream-foreign-object` | Display an indication that content cannot be correctly rendered | Speak an indication that content cannot be correctly spoken |
| `fo:inline-container` | Display indication that content cannot be correctly rendered | Speak an indication that content cannot be correctly spoken |
| `fo:page-number` | N/A (basic for visual) | Speak an indication that content cannot be correctly spoken |
| `fo:page-number-citation` | Display an indication that content cannot be correctly rendered | Speak an indication that content cannot be correctly spoken |
| `fo:page-number-citation-last` | Display an indication that content cannot be correctly rendered | Speak an indication that content cannot be correctly spoken |
| `fo:folio-prefix` | Display an indication that content cannot be correctly rendered | Speak an indication that content cannot be correctly spoken |
| `fo:folio-suffix` | Display an indication that content cannot be correctly rendered | Speak an indication that content cannot be correctly spoken |
| `fo:scaling-value-citation` | Display indication that content cannot be correctly rendered | Speak an indication that content cannot be correctly rendered |

## Table FOs

| Formatting Object | Visual | Aural |
|---|---|---|
| `fo:table-and-caption` | basic | basic |
| `fo:table` | basic | basic |
| `fo:table-column` | basic | basic |
| `fo:table-caption` | extended | extended |
| `fo:table-header` | basic | basic |
| `fo:table-footer` | extended | extended |
| `fo:table-body` | basic | basic |
| `fo:table-row` | basic | basic |
| `fo:table-cell` | basic | basic |

### Extended Fallbacks (Table)

| Formatting Object | Visual Fallback | Aural Fallback |
|---|---|---|
| `fo:table-caption` | `caption-side="start"` becomes `"before"`; `caption-side="end"` becomes `"after"`; `caption-side="left"` becomes `"before"`; `caption-side="right"` becomes `"after"` | Same as visual |
| `fo:table-footer` | Place at end of table | Speak at end of table |

## List FOs

| Formatting Object | Visual | Aural |
|---|---|---|
| `fo:list-block` | basic | basic |
| `fo:list-item` | basic | basic |
| `fo:list-item-body` | basic | basic |
| `fo:list-item-label` | extended | basic |

### Extended Fallbacks (List)

| Formatting Object | Visual Fallback | Aural Fallback |
|---|---|---|
| `fo:list-item-label` | Labels that break across multiple lines are treated as separate blocks before list-item-body | N/A (basic for aural) |

## Link and Multi FOs

<!-- Source: https://www.w3.org/TR/xslfo20/#ConfMulti -->

For certain formatting objects in this category, the visual class is subdivided into interactive and non-interactive media. Several objects need not be implemented for extended conformance on non-interactive media.

| Formatting Object | Visual | Aural |
|---|---|---|
| `fo:basic-link` | extended | extended |
| `fo:multi-switch` | extended (need not be implemented for non-interactive media) | extended |
| `fo:multi-case` | basic (needed as wrapper for multi-switch fallback) | basic (needed as wrapper for multi-switch fallback) |
| `fo:multi-toggle` | extended (need not be implemented for non-interactive media) | extended |
| `fo:multi-properties` | extended (need not be implemented for non-interactive media) | extended |
| `fo:multi-property-set` | extended (need not be implemented for non-interactive media) | extended |

### Extended Fallbacks (Link and Multi)

| Formatting Object | Visual Fallback | Aural Fallback |
|---|---|---|
| `fo:basic-link` | Promote content to parent formatting object | Promote content to parent formatting object |
| `fo:multi-switch` | Utilize the contents of the first eligible multi-case formatting object | Utilize the contents of the first eligible multi-case formatting object |
| `fo:multi-toggle` | Promote content to parent formatting object | Promote content to parent formatting object |
| `fo:multi-properties` | Promote content to parent formatting object | Promote content to parent formatting object |
| `fo:multi-property-set` | Ignore | Ignore |

## Out-of-line FOs

| Formatting Object | Visual | Aural |
|---|---|---|
| `fo:float` | extended | extended |
| `fo:footnote` | extended | extended |
| `fo:footnote-body` | extended | extended |

### Extended Fallbacks (Out-of-line)

| Formatting Object | Visual Fallback | Aural Fallback |
|---|---|---|
| `fo:float` | Place inline | Place inline |
| `fo:footnote` | Place inline | Place inline |
| `fo:footnote-body` | Place inline | Place inline |

## Formatting Objects for Indexing

| Formatting Object | Visual | Aural |
|---|---|---|
| `fo:index-page-citation-list` | extended | extended |
| `fo:index-key-reference` | extended | extended |
| `fo:index-page-number-prefix` | extended | extended |
| `fo:index-page-number-suffix` | extended | extended |
| `fo:index-page-citation-list-separator` | extended | extended |
| `fo:index-page-citation-range-separator` | extended | extended |
| `fo:index-range-begin` | extended | extended |
| `fo:index-range-end` | extended | extended |

### Extended Fallbacks (Indexing)

| Formatting Object | Visual Fallback | Aural Fallback |
|---|---|---|
| `fo:index-page-citation-list` | Display indication that content cannot be correctly rendered | Speak an indication that content cannot be correctly rendered |
| `fo:index-key-reference` | Ignore | Ignore |
| `fo:index-page-number-prefix` | Ignore | Ignore |
| `fo:index-page-number-suffix` | Ignore | Ignore |
| `fo:index-page-citation-list-separator` | Ignore | Ignore |
| `fo:index-page-citation-range-separator` | Ignore | Ignore |
| `fo:index-range-begin` | Ignore | Ignore |
| `fo:index-range-end` | Ignore | Ignore |

## Formatting Objects for Bookmarks

| Formatting Object | Visual | Aural |
|---|---|---|
| `fo:bookmark-tree` | extended | extended |
| `fo:bookmark` | extended | extended |
| `fo:bookmark-title` | extended | extended |

### Extended Fallbacks (Bookmarks)

| Formatting Object | Visual Fallback | Aural Fallback |
|---|---|---|
| `fo:bookmark-tree` | Display an indication that content cannot be correctly rendered | Speak an indication that content cannot be correctly spoken |
| `fo:bookmark` | Ignore | Ignore |
| `fo:bookmark-title` | Ignore | Ignore |

## Other FOs

| Formatting Object | Visual | Aural |
|---|---|---|
| `fo:change-bar-begin` | extended | extended |
| `fo:change-bar-end` | extended | extended |
| `fo:wrapper` | basic | basic |
| `fo:marker` | extended | extended |
| `fo:retrieve-marker` | extended | extended |
| `fo:retrieve-table-marker` | extended | extended |

### Extended Fallbacks (Other)

| Formatting Object | Visual Fallback | Aural Fallback |
|---|---|---|
| `fo:change-bar-begin` | Ignore | Ignore |
| `fo:change-bar-end` | Ignore | Ignore |
| `fo:marker` | Ignore | Ignore |
| `fo:retrieve-marker` | Display indication that content cannot be correctly rendered | Speak an indication that content cannot be correctly rendered |
| `fo:retrieve-table-marker` | Display indication that content cannot be correctly rendered | Speak an indication that content cannot be correctly rendered |

## Quick Conformance Count

| Category | Total FOs | Basic (Visual) | Extended (Visual) |
|---|---|---|---|
| Declaration and Pagination and Layout | 26 | 13 | 13 |
| Block | 2 | 1 | 1 |
| Inline | 14 | 5 | 9 |
| Table | 9 | 6 | 3 |
| List | 4 | 3 | 1 |
| Link and Multi | 6 | 1 | 5 |
| Out-of-line | 3 | 0 | 3 |
| Indexing | 8 | 0 | 8 |
| Bookmarks | 3 | 0 | 3 |
| Other | 6 | 1 | 5 |
| **Total** | **81** | **30** | **51** |

## Code Samples

No code samples in spec for this section.

## See Also

- [Conformance](ref-conformance.md) -- conformance level definitions (basic, extended, complete)
- [fo-root](fo-root.md) -- `fo:root`
- [fo-page-sequence](fo-page-sequence.md) -- `fo:page-sequence`
- [fo-page-sequence-wrapper](fo-page-sequence-wrapper.md) -- `fo:page-sequence-wrapper`
- [fo-page-sequence-master](fo-page-sequence-master.md) -- `fo:page-sequence-master`
- [fo-single-page-master-reference](fo-single-page-master-reference.md) -- `fo:single-page-master-reference`
- [fo-repeatable-page-master-reference](fo-repeatable-page-master-reference.md) -- `fo:repeatable-page-master-reference`
- [fo-repeatable-page-master-alternatives](fo-repeatable-page-master-alternatives.md) -- `fo:repeatable-page-master-alternatives`
- [fo-conditional-page-master-reference](fo-conditional-page-master-reference.md) -- `fo:conditional-page-master-reference`
- [fo-layout-master-set](fo-layout-master-set.md) -- `fo:layout-master-set`
- [fo-simple-page-master](fo-simple-page-master.md) -- `fo:simple-page-master`
- [fo-region-body](fo-region-body.md) -- `fo:region-body`
- [fo-region-before](fo-region-before.md) -- `fo:region-before`
- [fo-region-after](fo-region-after.md) -- `fo:region-after`
- [fo-region-start](fo-region-start.md) -- `fo:region-start`
- [fo-region-end](fo-region-end.md) -- `fo:region-end`
- [fo-declarations](fo-declarations.md) -- `fo:declarations`
- [fo-color-profile](fo-color-profile.md) -- `fo:color-profile`
- [fo-flow](fo-flow.md) -- `fo:flow`
- [fo-static-content](fo-static-content.md) -- `fo:static-content`
- [fo-title](fo-title.md) -- `fo:title`
- [fo-flow-map](fo-flow-map.md) -- `fo:flow-map`
- [fo-flow-assignment](fo-flow-assignment.md) -- `fo:flow-assignment`
- [fo-flow-source-list](fo-flow-source-list.md) -- `fo:flow-source-list`
- [fo-flow-name-specifier](fo-flow-name-specifier.md) -- `fo:flow-name-specifier`
- [fo-flow-target-list](fo-flow-target-list.md) -- `fo:flow-target-list`
- [fo-region-name-specifier](fo-region-name-specifier.md) -- `fo:region-name-specifier`
- [fo-block](fo-block.md) -- `fo:block`
- [fo-block-container](fo-block-container.md) -- `fo:block-container`
- [fo-bidi-override](fo-bidi-override.md) -- `fo:bidi-override`
- [fo-character](fo-character.md) -- `fo:character`
- [fo-initial-property-set](fo-initial-property-set.md) -- `fo:initial-property-set`
- [fo-external-graphic](fo-external-graphic.md) -- `fo:external-graphic`
- [fo-instream-foreign-object](fo-instream-foreign-object.md) -- `fo:instream-foreign-object`
- [fo-inline](fo-inline.md) -- `fo:inline`
- [fo-inline-container](fo-inline-container.md) -- `fo:inline-container`
- [fo-leader](fo-leader.md) -- `fo:leader`
- [fo-page-number](fo-page-number.md) -- `fo:page-number`
- [fo-page-number-citation](fo-page-number-citation.md) -- `fo:page-number-citation`
- [fo-page-number-citation-last](fo-page-number-citation-last.md) -- `fo:page-number-citation-last`
- [fo-folio-prefix](fo-folio-prefix.md) -- `fo:folio-prefix`
- [fo-folio-suffix](fo-folio-suffix.md) -- `fo:folio-suffix`
- [fo-scaling-value-citation](fo-scaling-value-citation.md) -- `fo:scaling-value-citation`
- [fo-table-and-caption](fo-table-and-caption.md) -- `fo:table-and-caption`
- [fo-table](fo-table.md) -- `fo:table`
- [fo-table-column](fo-table-column.md) -- `fo:table-column`
- [fo-table-caption](fo-table-caption.md) -- `fo:table-caption`
- [fo-table-header](fo-table-header.md) -- `fo:table-header`
- [fo-table-footer](fo-table-footer.md) -- `fo:table-footer`
- [fo-table-body](fo-table-body.md) -- `fo:table-body`
- [fo-table-row](fo-table-row.md) -- `fo:table-row`
- [fo-table-cell](fo-table-cell.md) -- `fo:table-cell`
- [fo-list-block](fo-list-block.md) -- `fo:list-block`
- [fo-list-item](fo-list-item.md) -- `fo:list-item`
- [fo-list-item-body](fo-list-item-body.md) -- `fo:list-item-body`
- [fo-list-item-label](fo-list-item-label.md) -- `fo:list-item-label`
- [fo-basic-link](fo-basic-link.md) -- `fo:basic-link`
- [fo-multi-switch](fo-multi-switch.md) -- `fo:multi-switch`
- [fo-multi-case](fo-multi-case.md) -- `fo:multi-case`
- [fo-multi-toggle](fo-multi-toggle.md) -- `fo:multi-toggle`
- [fo-multi-properties](fo-multi-properties.md) -- `fo:multi-properties`
- [fo-multi-property-set](fo-multi-property-set.md) -- `fo:multi-property-set`
- [fo-float](fo-float.md) -- `fo:float`
- [fo-footnote](fo-footnote.md) -- `fo:footnote`
- [fo-footnote-body](fo-footnote-body.md) -- `fo:footnote-body`
- [fo-index-page-citation-list](fo-index-page-citation-list.md) -- `fo:index-page-citation-list`
- [fo-index-key-reference](fo-index-key-reference.md) -- `fo:index-key-reference`
- [fo-index-page-number-prefix](fo-index-page-number-prefix.md) -- `fo:index-page-number-prefix`
- [fo-index-page-number-suffix](fo-index-page-number-suffix.md) -- `fo:index-page-number-suffix`
- [fo-index-page-citation-list-separator](fo-index-page-citation-list-separator.md) -- `fo:index-page-citation-list-separator`
- [fo-index-page-citation-range-separator](fo-index-page-citation-range-separator.md) -- `fo:index-page-citation-range-separator`
- [fo-index-range-begin](fo-index-range-begin.md) -- `fo:index-range-begin`
- [fo-index-range-end](fo-index-range-end.md) -- `fo:index-range-end`
- [fo-bookmark-tree](fo-bookmark-tree.md) -- `fo:bookmark-tree`
- [fo-bookmark](fo-bookmark.md) -- `fo:bookmark`
- [fo-bookmark-title](fo-bookmark-title.md) -- `fo:bookmark-title`
- [fo-change-bar-begin](fo-change-bar-begin.md) -- `fo:change-bar-begin`
- [fo-change-bar-end](fo-change-bar-end.md) -- `fo:change-bar-end`
- [fo-wrapper](fo-wrapper.md) -- `fo:wrapper`
- [fo-marker](fo-marker.md) -- `fo:marker`
- [fo-retrieve-marker](fo-retrieve-marker.md) -- `fo:retrieve-marker`
- [fo-retrieve-table-marker](fo-retrieve-table-marker.md) -- `fo:retrieve-table-marker`
