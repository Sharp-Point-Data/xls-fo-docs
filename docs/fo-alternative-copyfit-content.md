# fo:alternative-copyfit-content

## Summary

The fo:alternative-copyfit-content formatting object is intended to express alternative content for copyfit. It provides a mechanism to specify content that can be used as a substitute during the copyfitting process, allowing the formatter to choose between alternative content versions to best fill available space.

It might be a child of an fo:flow object (when copyfitting content into a region) or fo:block-container or fo:table-cell (when copyfitting content in block-containers or table cells).

## Content Model

```
(%block;)*
```

The fo:alternative-copyfit-content may contain zero or more block-level formatting objects.

## Properties

The applicable properties for this formatting object are deferred in the current specification. The spec notes that properties are likely to be resolved using a function similar to xsl:choose to select content based on formatter feedback.

## Areas

The fo:alternative-copyfit-content formatting object does not generate any areas. The fo:alternative-copyfit-content formatting object returns the areas generated and returned by its children.

## Usage Notes

- This formatting object is used in the context of the XSL-FO 2.0 copyfitting model.
- Place fo:alternative-copyfit-content as a child of fo:flow, fo:block-container, or fo:table-cell to provide alternative content that the formatter can use during copyfitting.
- The alternative content is typically a shorter or longer version of the main content, allowing the formatter to select the version that best fits the available space.
- The copyfitting mechanism works in conjunction with adjustable properties (such as line-height and word-spacing ranges) defined on the regions and blocks.
- Whether copyfit content should be allowed in static content is an open issue in the specification.

## Code Samples

### Sample 1: Content model declaration

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_alternative-copyfit-content -->
```xml
(%block;)*
```

### Sample 2: Alternative copyfit content within a flow

This example shows fo:alternative-copyfit-content used within an fo:flow. The alternative content (inside the fo:alternative-copyfit-content element) can be swapped in by the formatter during copyfitting. The blocks following the fo:alternative-copyfit-content element are the primary content.

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_alternative-copyfit-content -->
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

- [fo:flow](fo-flow.md) — parent container when copyfitting content into a region
- [fo:block-container](fo-block-container.md) — parent container when copyfitting in block-containers
- [fo:table-cell](fo-table-cell.md) — parent container when copyfitting in table cells
- [fo:block](fo-block.md) — block-level children of the alternative content
- [Copyfitting model](guide-copyfitting.md) (area model specification, copyfitting section)
- adjustable-properties — region property that enables copyfitting
- display-align — controls vertical alignment used in copyfitting
