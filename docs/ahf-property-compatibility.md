# Antenna House: Standard Property Compatibility

Compatibility of W3C XSL-FO properties with Antenna House Formatter v7.4, based on the Antenna House XSL-FO Reference Guide.

<!-- Source: XSL-FO-Reference-74-MID.pdf pp.82–204 -->

## Support Status Summary

- **Supported**: Full conformance with the W3C XSL-FO specification
- **Extended**: Supported with Antenna House extensions beyond the W3C spec
- **Not supported**: Not implemented in Antenna House Formatter

## Property Compatibility

| Property | Support | Notes |
|---|---|---|
| absolute-position | Supported | — |
| active-state | Not supported | Used by fo:multi-case for interactive state toggling; fo:multi-case is not supported |
| alignment-adjust | Supported | — |
| alignment-baseline | Supported | — |
| allowed-height-scale | Supported | — |
| allowed-width-scale | Supported | — |
| auto-restore | Not supported | Used by fo:multi-switch for automatic state restoration; fo:multi-switch is not supported |
| background | Extended | Extended with axf:background-size, axf:background-origin, axf:background-clip |
| background-attachment | Supported | — |
| background-color | Supported | — |
| background-image | Extended | Extended with SVG support and axf:background-content-type |
| background-position | Supported | — |
| background-position-horizontal | Supported | — |
| background-position-vertical | Supported | — |
| background-repeat | Supported | — |
| baseline-shift | Supported | — |
| block-progression-dimension | Supported | — |
| border | Supported | — |
| border-after-color | Supported | — |
| border-after-precedence | Supported | — |
| border-after-style | Extended | Extended with additional border styles (double, wave) |
| border-after-width | Supported | — |
| border-before-color | Supported | — |
| border-before-precedence | Supported | — |
| border-before-style | Extended | Extended with additional border styles (double, wave) |
| border-before-width | Supported | — |
| border-bottom | Supported | — |
| border-bottom-color | Supported | — |
| border-bottom-style | Extended | Extended with additional border styles (double, wave) |
| border-bottom-width | Supported | — |
| border-collapse | Supported | — |
| border-color | Supported | — |
| border-end-color | Supported | — |
| border-end-precedence | Supported | — |
| border-end-style | Extended | Extended with additional border styles (double, wave) |
| border-end-width | Supported | — |
| border-left | Supported | — |
| border-left-color | Supported | — |
| border-left-style | Extended | Extended with additional border styles (double, wave) |
| border-left-width | Supported | — |
| border-right | Supported | — |
| border-right-color | Supported | — |
| border-right-style | Extended | Extended with additional border styles (double, wave) |
| border-right-width | Supported | — |
| border-separation | Supported | — |
| border-spacing | Supported | — |
| border-start-color | Supported | — |
| border-start-precedence | Supported | — |
| border-start-style | Extended | Extended with additional border styles (double, wave) |
| border-start-width | Supported | — |
| border-style | Extended | Extended with additional border styles (double, wave) |
| border-top | Supported | — |
| border-top-color | Supported | — |
| border-top-style | Extended | Extended with additional border styles (double, wave) |
| border-top-width | Supported | — |
| border-width | Supported | — |
| break-after | Supported | — |
| break-before | Supported | — |
| caption-side | Supported | — |
| case-name | Not supported | Used by fo:multi-case for naming interactive cases; fo:multi-case is not supported |
| case-title | Not supported | Used by fo:multi-case for case titles; fo:multi-case is not supported |
| change-bar-class | Supported | — |
| change-bar-color | Supported | — |
| change-bar-offset | Supported | — |
| change-bar-placement | Supported | — |
| change-bar-style | Supported | — |
| change-bar-width | Supported | — |
| character | Supported | — |
| clear | Supported | — |
| clip | Supported | — |
| color | Supported | — |
| color-profile-name | Supported | — |
| column-count | Extended | Extended with axf:column-fill, axf:column-rule-* properties |
| column-gap | Extended | Extended with column rule properties |
| column-number | Supported | — |
| column-width | Supported | — |
| content-height | Supported | — |
| content-type | Extended | Extended with additional media types |
| content-width | Supported | — |
| country | Supported | — |
| destination-placement-offset | Not supported | Used by fo:bookmark for scroll offset at destination; not implemented |
| direction | Supported | — |
| display-align | Extended | Extended behavior |
| dominant-baseline | Supported | — |
| empty-cells | Not supported | CSS table property for controlling display of empty table cells; not implemented |
| end-indent | Supported | — |
| ends-row | Supported | — |
| extent | Supported | — |
| external-destination | Supported | — |
| float | Supported | — |
| flow-map-name | Supported | — |
| flow-map-reference | Supported | — |
| flow-name | Supported | — |
| flow-name-reference | Supported | — |
| font | Supported | — |
| font-family | Supported | — |
| font-selection-strategy | Supported | — |
| font-size | Supported | — |
| font-size-adjust | Supported | — |
| font-stretch | Supported | — |
| font-style | Extended | Extended with oblique angle support |
| font-variant | Supported | — |
| font-weight | Supported | — |
| force-page-count | Extended | Extended with additional values |
| format | Extended | Extended with additional number formats including Kansuji |
| glyph-orientation-horizontal | Supported | — |
| glyph-orientation-vertical | Supported | — |
| grouping-separator | Supported | — |
| grouping-size | Supported | — |
| height | Supported | — |
| hyphenate | Supported | — |
| hyphenation-character | Supported | — |
| hyphenation-keep | Supported | — |
| hyphenation-ladder-count | Supported | — |
| hyphenation-push-character-count | Supported | — |
| hyphenation-remain-character-count | Supported | — |
| indicate-destination | Not supported | Used by fo:basic-link to visually indicate the destination area; not implemented |
| index-class | Supported | — |
| index-key | Supported | — |
| initial-page-number | Supported | — |
| inline-progression-dimension | Supported | — |
| internal-destination | Extended | Extended PDF link behavior |
| intrinsic-scale-value | Supported | — |
| intrusion-displace | Supported | — |
| keep-together | Supported | — |
| keep-with-next | Supported | — |
| keep-with-previous | Supported | — |
| last-line-end-indent | Supported | — |
| leader-alignment | Extended | Extended alignment options |
| leader-length | Supported | — |
| leader-pattern | Supported | — |
| leader-pattern-width | Supported | — |
| letter-spacing | Supported | — |
| letter-value | Supported | — |
| line-height | Supported | — |
| line-height-shift-adjustment | Supported | — |
| line-stacking-strategy | Supported | — |
| linefeed-treatment | Supported | — |
| margin | Supported | — |
| margin-bottom | Supported | — |
| margin-end | Supported | — |
| margin-left | Supported | — |
| margin-right | Supported | — |
| margin-start | Supported | — |
| margin-top | Supported | — |
| marker-class-name | Supported | — |
| master-name | Supported | — |
| master-reference | Supported | — |
| max-height | Supported | — |
| max-width | Supported | — |
| maximum-repeats | Supported | — |
| media-usage | Not supported | Used by fo:root for specifying the target media; not implemented |
| merge-pages-across-index-key-references | Supported | — |
| merge-ranges-across-index-key-references | Supported | — |
| merge-sequential-page-numbers | Extended | Extended behavior |
| min-height | Supported | — |
| min-width | Supported | — |
| number-columns-repeated | Supported | — |
| number-columns-spanned | Supported | — |
| number-rows-spanned | Supported | — |
| odd-or-even | Extended | Extended with blank page handling |
| orphans | Supported | — |
| overflow | Extended | Extended with axf:overflow-condense, axf:overflow-align |
| padding | Supported | — |
| padding-after | Supported | — |
| padding-before | Supported | — |
| padding-bottom | Supported | — |
| padding-end | Supported | — |
| padding-left | Supported | — |
| padding-right | Supported | — |
| padding-start | Supported | — |
| padding-top | Supported | — |
| page-break-after | Supported | — |
| page-break-before | Supported | — |
| page-break-inside | Supported | — |
| page-citation-strategy | Supported | — |
| page-height | Supported | — |
| page-number-treatment | Supported | — |
| page-position | Supported | — |
| page-width | Supported | — |
| position | Supported | — |
| precedence | Supported | — |
| provisional-distance-between-starts | Supported | — |
| provisional-label-separation | Supported | — |
| ref-id | Supported | — |
| ref-index-key | Supported | — |
| reference-orientation | Supported | — |
| region-name | Supported | — |
| region-name-reference | Supported | — |
| relative-align | Supported | — |
| relative-position | Supported | — |
| rendering-intent | Not supported | Used by fo:color-profile for specifying color rendering intent; not implemented |
| retrieve-boundary | Supported | — |
| retrieve-boundary-within-table | Supported | — |
| retrieve-class-name | Supported | — |
| retrieve-position | Supported | — |
| retrieve-position-within-table | Supported | — |
| role | Supported | — |
| rule-style | Supported | — |
| rule-thickness | Supported | — |
| scale-option | Supported | — |
| scaling | Supported | — |
| scaling-method | Not supported | Used by fo:external-graphic and fo:instream-foreign-object for image scaling algorithm; not implemented |
| score-spaces | Supported | — |
| script | Extended | Extended script handling |
| show-destination | Supported | — |
| size | Supported | — |
| source-document | Supported | — |
| space-after | Supported | — |
| space-before | Supported | — |
| space-end | Supported | — |
| space-start | Supported | — |
| span | Supported | — |
| start-indent | Supported | — |
| starting-state | Not supported | Used by fo:multi-toggle for initial display state; fo:multi-toggle is not supported |
| starts-row | Supported | — |
| suppress-at-line-break | Not supported | Used by fo:character for controlling character suppression at line breaks; not implemented |
| switch-to | Not supported | Used by fo:multi-toggle for switching between multi-case states; fo:multi-toggle is not supported |
| table-layout | Supported | — |
| table-omit-footer-at-break | Extended | Extended with conditional table footer/header |
| table-omit-header-at-break | Extended | Extended with conditional table footer/header |
| target-presentation-context | Not supported | Used by fo:basic-link for specifying the presentation context of the destination; not implemented |
| target-processing-context | Not supported | Used by fo:basic-link for specifying the processing context of the destination; not implemented |
| target-stylesheet | Not supported | Used by fo:basic-link for specifying a stylesheet for the destination; not implemented |
| text-align | Supported | — |
| text-align-last | Supported | — |
| text-altitude | Supported | — |
| text-decoration | Supported | — |
| text-depth | Supported | — |
| text-indent | Supported | — |
| text-shadow | Supported | — |
| text-transform | Extended | Extended with additional transformations |
| treat-as-word-space | Not supported | Used by fo:character to specify whether the character should be treated as a word space; not implemented |
| unicode-bidi | Supported | — |
| unicode-range | Supported | — |
| vertical-align | Supported | — |
| visibility | Supported | — |
| white-space | Supported | — |
| white-space-collapse | Supported | — |
| white-space-treatment | Supported | — |
| widows | Supported | — |
| width | Supported | — |
| word-spacing | Supported | — |
| wrap-option | Supported | — |
| writing-mode | Supported | — |
