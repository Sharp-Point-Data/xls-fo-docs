# Copyfitting

## Overview

Copyfitting is a mechanism introduced in **XSL-FO 2.0** for adjusting content to fit within a given area. It allows a formatter to automatically modify certain property values (such as `line-height`, `word-spacing`, or `space-before`) so that content fills a region, a block-container, or a table-cell exactly. Copyfitting generalizes the concept of vertical justification and extends it with prioritized adjustment strategies.

Source: [W3C XSL-FO 2.0 -- Copyfitting](https://www.w3.org/TR/xslfo20/#copyfitting)

**Note:** This is a new feature in XSL-FO 2.0 and was not available in XSL-FO 1.1. The specification notes that this subject has evolved and is currently under discussion.

## Copyfitting Summary

<!-- Source: https://www.w3.org/TR/xslfo20/#copyfitting-summary -->

Copyfitting is supported on `fo:region`, `fo:region-*` objects, `fo:block-container`, and `fo:table-cell`.

The mechanism introduces:

- A new value `justify` for the property `display-align` (already present in XSL-FO) to activate copyfitting. Although the same property is used for vertical justification, users can exploit the property `force-page-count` (along with correct definitions of page-masters and page-sequences) to avoid conflicts.
- The concept of a **list of prioritized adjustable properties**. An adjustable property is an existing XSL-FO property that the formatter is allowed to modify in order to perform copyfitting or vertical justification.
- **Range values** on existing properties to specify how (and how much) each property can be adjusted, introducing the idea of "elasticity."
- A new property `adjustable-properties` that specifies the ordered list of properties the formatter may adjust.
- New values for the property `force-page-count` to model copyfitting into a fixed number of pages or a multiple of a number.
- A new formatting object `fo:alternative-copyfit-content` to express alternative content for copyfitting.

## Basic Approach and Definitions

<!-- Source: https://www.w3.org/TR/xslfo20/#copyfitting-approach -->

Many options exist to copyfit content to a certain area. A user could add space between paragraphs, widen or narrow spaces before and after titles, images, and tables, modify the line height of paragraphs, and so on. These fine tunings and their multiplicity of combinations lead to different results, and different users may have different preferences.

Copyfitting requires two logically separated tasks:

1. **The request for copyfitting** on a given area.
2. **The definition of strategies** to perform the copyfitting.

### Activating Copyfitting

Copyfitting is enabled by setting the property `display-align` to the value `justify`. Copyfitting strategies are then expressed through "adjustable properties lists" using the `adjustable-properties` property.

Although the same approach is used for vertical justification, users can exploit the property `force-page-count` and/or the definition of page-masters and page-sequences to avoid conflicts between copyfitting and vertical justification.

### Applicable Formatting Objects

The `display-align` property applies to `fo:region`, `fo:region-*`, `fo:block-container`, and `fo:table-cell`. This makes it possible to copyfit content in a block-container or table cell, and also to copyfit the content of one flow to a single region, multiple flows to a single region, or even multiple flows to multiple regions.

### Last-Page Alignment

A `display-align-last` property is also added to specify different treatment of the last page in a copyfitted sequence, by analogy with `text-align` and `text-align-last`.

## Code Samples

No code samples in spec for this section. The copyfitting examples (6 code samples demonstrating copyfitting with flow maps, multiple regions, `display-align`, `display-align-last`, and `force-page-count`) are documented in [guide-area-model.md](guide-area-model.md).

## See Also

- [guide-area-model.md](guide-area-model.md) -- Contains copyfitting code examples and additional area model details
- [guide-rendering-model.md](guide-rendering-model.md) -- The rendering model for the area tree
- `fo-block-container` -- Block-level container that supports copyfitting via `display-align`
- `fo-table-cell` -- Table cell that supports copyfitting via `display-align`
- `fo-page-sequence` -- Page sequence with `force-page-count` for controlling page output
- `fo-flow-map` -- Flow map for assigning flows to regions (used in copyfitting examples)
- `properties-display-align.md` -- The `display-align` property that activates copyfitting
