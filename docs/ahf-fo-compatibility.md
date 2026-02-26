# Antenna House: Standard FO Compatibility

Compatibility of W3C XSL-FO formatting objects with Antenna House Formatter v7.4, based on the Antenna House XSL-FO Reference Guide.

<!-- Source: XSL-FO-Reference-74-MID.pdf pp.10–78, 292–295 -->

## Support Status Summary

- **Supported**: Full conformance with the W3C XSL-FO specification
- **Extended**: Supported with additional Antenna House extensions beyond the W3C spec
- **Not supported**: Not implemented in Antenna House Formatter

## Formatting Object Compatibility

| Formatting Object | Support | Notes |
|---|---|---|
| fo:basic-link | Supported | AHF extension properties for borders, PDF link types; AHF child: axf:ruby |
| fo:bidi-override | Supported | AHF properties: axf:auto-letter-spacing, axf:letter-spacing-side; AHF child: axf:ruby |
| fo:block | Supported | Extensive AHF extensions (annotation, outline, overflow, line numbering, typography, border, baseline grid properties); AHF child: axf:form |
| fo:block-container | Extended | Adds axf:column-count for multi-column containers, plus additional AHF extension properties |
| fo:bookmark | Supported | |
| fo:bookmark-title | Supported | |
| fo:bookmark-tree | Supported | |
| fo:change-bar-begin | Extended | Extended change bar support |
| fo:change-bar-end | Supported | |
| fo:character | Supported | AHF extension properties for typography and text handling |
| fo:color-profile | Supported | |
| fo:conditional-page-master-reference | Supported | |
| fo:declarations | Supported | AHF children: axf:counter-style, axf:custom-property, axf:font-face, axf:formatter-config, axf:hyphenation-info, axf:script-font, axf:space-after-punctuation, axf:space-before-punctuation, axf:space-between-digit-and-punctuation, axf:space-between-punctuation-and-digit |
| fo:external-graphic | Supported | AHF extension properties for borders, transforms, annotations |
| fo:float | Extended | Extended float behavior with additional placement options |
| fo:flow | Supported | AHF properties for column handling |
| fo:flow-assignment | Supported | |
| fo:flow-map | Supported | |
| fo:flow-name-specifier | Supported | |
| fo:flow-source-list | Supported | |
| fo:flow-target-list | Supported | |
| fo:folio-prefix | Supported | |
| fo:folio-suffix | Supported | |
| fo:footnote | Supported | AHF properties for footnote numbering control |
| fo:footnote-body | Extended | Extended footnote support; AHF child: axf:footnote-number-citation |
| fo:index-key-reference | Supported | |
| fo:index-page-citation-list | Supported | |
| fo:index-page-citation-list-separator | Supported | |
| fo:index-page-citation-range-separator | Supported | |
| fo:index-page-number-prefix | Supported | |
| fo:index-page-number-suffix | Supported | |
| fo:index-range-begin | Supported | |
| fo:index-range-end | Supported | |
| fo:initial-property-set | Supported | AHF extension properties for text decoration and typography |
| fo:inline | Supported | Extensive AHF extensions; AHF children: axf:footnote-number, axf:ruby |
| fo:inline-container | Supported | AHF extension properties for borders, transforms, overflow |
| fo:instream-foreign-object | Supported | AHF extension properties |
| fo:layout-master-set | Supported | AHF child: axf:spread-page-master |
| fo:leader | Supported | AHF extension properties |
| fo:list-block | Supported | Extensive AHF extensions for borders, typography, overflow |
| fo:list-item | Supported | Extensive AHF extensions |
| fo:list-item-body | Supported | |
| fo:list-item-label | Supported | |
| fo:marker | Supported | |
| fo:multi-case | Not supported | |
| fo:multi-properties | Not supported | |
| fo:multi-property-set | Not supported | |
| fo:multi-switch | Not supported | |
| fo:multi-toggle | Not supported | |
| fo:page-number | Supported | AHF extension properties for text handling |
| fo:page-number-citation | Supported | AHF extension properties |
| fo:page-number-citation-last | Supported | AHF extension properties |
| fo:page-sequence | Extended | Extended with AHF properties for footnote numbering (axf:footnote-number-reset, axf:footnote-number-format, axf:footnote-number-initial) and other extensions |
| fo:page-sequence-master | Supported | Supported with minor AHF extensions |
| fo:page-sequence-wrapper | Supported | |
| fo:region-after | Supported | AHF extension properties for background, overflow |
| fo:region-before | Supported | AHF extension properties for background, overflow |
| fo:region-body | Supported | AHF extension properties including column extensions |
| fo:region-end | Supported | AHF extension properties |
| fo:region-name-specifier | Supported | |
| fo:region-start | Supported | AHF extension properties |
| fo:repeatable-page-master-alternatives | Supported | |
| fo:repeatable-page-master-reference | Supported | |
| fo:retrieve-marker | Supported | |
| fo:retrieve-table-marker | Supported | Supported with minor AHF extensions |
| fo:root | Supported | AHF children: axf:document-info, axf:output-volume-info |
| fo:scaling-value-citation | Supported | AHF extension properties |
| fo:simple-page-master | Extended | Extended page master with additional AHF properties |
| fo:single-page-master-reference | Supported | |
| fo:static-content | Supported | AHF extension properties |
| fo:table | Supported | Extensive AHF extensions for borders, typography, overflow |
| fo:table-and-caption | Supported | AHF extension properties |
| fo:table-body | Supported | AHF extension properties |
| fo:table-caption | Supported | AHF extension properties |
| fo:table-cell | Supported | AHF extension properties; AHF child: axf:table-cell-repeated-marker |
| fo:table-column | Supported | AHF extension properties |
| fo:table-footer | Supported | AHF extension properties |
| fo:table-header | Supported | AHF extension properties |
| fo:table-row | Supported | AHF extension properties |
| fo:title | Supported | |
| fo:wrapper | Supported | |

## AHF Extension Property Groups

From section 2.2.1 of the Antenna House reference, extension properties are organized by the groups of formatting objects they apply to:

<!-- Source: XSL-FO-Reference-74-MID.pdf pp.292–295 -->

**All Formatting Objects:** axf:assumed-page-number, axf:background-clip, axf:background-content-type, axf:background-image-resolution, axf:background-origin, axf:background-size, axf:base-uri, axf:expansion-text, axf:font-feature-settings, axf:justify-nbsp, axf:overflow-limit, axf:overflow-limit-block, axf:overflow-limit-inline, axf:overprint, axf:pdftag, axf:suppress-duplicate-marker-contents, axf:suppress-duplicate-page-number, axf:text-emphasis-style, axf:text-emphasis-position, axf:text-emphasis-offset, axf:text-emphasis-skip

**All Block and Inline Level FOs:** axf:annotation-author, axf:annotation-border-style, axf:annotation-border-width, axf:annotation-border-color, axf:annotation-color, axf:annotation-contents, axf:annotation-file-attachment, axf:annotation-file-name, axf:annotation-createdate, axf:annotation-modifydate, axf:annotation-font-family, axf:annotation-flags, axf:annotation-height, axf:annotation-font-size, axf:annotation-font-style, axf:annotation-font-weight, axf:annotation-icon-name, axf:annotation-open, axf:annotation-position-horizontal, axf:annotation-position-vertical, axf:annotation-text-align, axf:annotation-text-color, axf:annotation-title, axf:annotation-type, axf:annotation-width, axf:kansuji-grouping-letter, axf:kansuji-letter, axf:kansuji-style, axf:kerning-mode, axf:layer, axf:ligature-mode, axf:normalize, axf:normalize-exclude, axf:number-transform, axf:punctuation-spacing, axf:punctuation-trim, axf:soft-hyphen-treatment, axf:text-autospace, axf:text-autospace-width, axf:text-combine-horizontal, axf:text-justify, axf:text-justify-trim, axf:text-kashida-space, axf:text-orientation, axf:text-replace, axf:text-stroke, axf:text-stroke-color, axf:text-stroke-width, axf:url-break, axf:vertical-underline-side, axf:word-break, axf:word-wrap

**Block-level FOs:** axf:baseline-block-snap, axf:baseline-grid, axf:condensed-text-align-last, axf:destination-type, axf:index-page-citation-range-f-suffix, axf:index-page-citation-range-ff-suffix, axf:keep-together-within-dimension, axf:keep-together-within-inline-dimension, axf:line-break, axf:outline-color, axf:outline-expand, axf:outline-external-destination, axf:outline-font-style, axf:outline-font-weight, axf:outline-group, axf:outline-internal-destination, axf:outline-level, axf:outline-title, axf:overflow-align, axf:overflow-condense, axf:overflow-condense-limit-font-size, axf:overflow-condense-limit-font-stretch, axf:overflow-condense-limit-line-height, axf:overflow-condense-limit-letter-spacing, axf:overflow-replace, axf:text-overflow

**Block-level FOs (descendants of fo:flow, fo:table-column):** axf:line-continued-mark, axf:line-continued-mark-color, axf:line-continued-mark-background-color, axf:line-continued-mark-font-family, axf:line-continued-mark-font-size, axf:line-continued-mark-font-style, axf:line-continued-mark-font-weight, axf:line-continued-mark-offset, axf:line-number, axf:line-number-background-color, axf:line-number-color, axf:line-number-display-align, axf:line-number-except-continued-line, axf:line-number-font-family, axf:line-number-font-size, axf:line-number-font-style, axf:line-number-font-weight, axf:line-number-offset, axf:line-number-position, axf:line-number-text-align, axf:line-number-text-decoration, axf:line-number-width

**All Objects with Borders:** axf:border-connection-form, axf:border-radius, axf:border-bottom-left-radius, axf:border-bottom-right-radius, axf:border-top-left-radius, axf:border-top-right-radius, axf:border-double-thickness, axf:border-wave-form, axf:box-shadow, axf:diagonal-border-color, axf:diagonal-border-style, axf:diagonal-border-width, axf:reverse-diagonal-border-color, axf:reverse-diagonal-border-style, axf:reverse-diagonal-border-width

**Multi-column Objects:** axf:column-fill

**Objects with Textual Content:** axf:text-line-color, axf:text-line-style, axf:text-line-width, axf:text-underline-position

**Transformable Objects:** axf:transform, axf:transform-origin

**Emphasis Objects:** axf:text-emphasis-font-family, axf:text-emphasis-font-size, axf:text-emphasis-font-style, axf:text-emphasis-font-weight, axf:text-emphasis-font-stretch, axf:text-emphasis-color

**Inline Formatting Objects:** axf:auto-letter-spacing, axf:intrude-into-punctuation, axf:letter-spacing-side
