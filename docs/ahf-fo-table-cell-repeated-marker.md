# axf:table-cell-repeated-marker

<!-- Source: XSL-FO-Reference-74-MID.pdf p.312 -->

## Summary

Specifies the contents to be displayed in a split cell. When `axf:repeat-cell-content-at-break="true"` is specified on a table cell and that cell contains an `<axf:table-cell-repeated-marker>`, the contents of the `<axf:table-cell-repeated-marker>` are used instead of the original cell contents in the repeated (split) portion of the cell.

This is useful when a table cell spans multiple pages and you want the repeated portion to display different content (such as a "continued" indicator) rather than repeating the original cell contents verbatim.

## Content Model

```
(#PCDATA | fo:inline | fo:block)*
```

The element accepts mixed content: plain text, `fo:inline` elements, `fo:block` elements, or any combination thereof.

## Properties

None.

## Parent Objects

- `fo:table-cell`

## Code Samples

No code sample provided in the Antenna House reference for this formatting object.

**Constructed example** (not from spec):

```xml
<fo:table-cell axf:repeat-cell-content-at-break="true">
  <axf:table-cell-repeated-marker>
    <fo:block font-style="italic">(continued)</fo:block>
  </axf:table-cell-repeated-marker>
  <fo:block>This is the original cell content that may span
    multiple pages. When the cell breaks across a page boundary,
    the repeated portion of the cell will display "(continued)"
    instead of repeating this text.</fo:block>
</fo:table-cell>
```
