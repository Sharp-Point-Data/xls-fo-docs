# Property Summary

<!-- Source: https://www.w3.org/TR/xslfo20/#property-index -->

## Overview

Comprehensive index of all XSL-FO formatting properties as defined in the W3C XSL-FO 2.0 specification. This section provides three reference tables:

1. **Property Table: Part I** -- Name, Values, Initial Value, Inherited, Percentages
2. **Property Table: Part II** -- Name, Trait Mapping, Conformance Level
3. **Properties and the FOs they apply to** -- which properties apply to which formatting objects

Total properties indexed: 272

## Trait Mapping Values

<!-- Source: https://www.w3.org/TR/xslfo20/#trmval -->

The following trait mapping values are used in Property Table: Part II to describe how each property maps to a trait:

| Trait Mapping Value | Meaning |
|---|---|
| **Rendering** | Maps directly into a rendering trait of the same name. |
| **Disappears** | There is no trait mapping. |
| **Shorthand** | A shorthand that is mapped into one or more properties. There are no traits associated with a shorthand property. The traits are associated with the individual properties. |
| **Refine** | Disappears in refinement. During refinement it sets up one or more other traits. |
| **Formatting** | Maps directly into a formatting trait of the same name. |
| **Specification** | Sub-class of formatting. It is the same as a formatting trait, but is specified on formatting objects that are referenced. |
| **See prose** | Used to calculate a formatting trait, which does not have the same name as the property. Other properties may also influence the trait value. See the property description for details. |
| **Font selection** | Property that participates in font selection. |
| **Value change** | Maps to a trait of the same name, but the value is not just copied. |
| **Reference** | An association between two names. Establishes a reference within the formatting object tree. |
| **Action** | Behavior trait. |
| **Magic** | Handled by the formatter in an implementation-defined way. There are no specific traits for this property. |

## Property Table: Part I

<!-- Source: https://www.w3.org/TR/xslfo20/#prtab1 -->

| Property | Values | Initial Value | Inherited | Percentages |
|---|---|---|---|---|
| absolute-position | auto \| absolute \| fixed \| inherit | auto | no | N/A |
| active-state | link \| visited \| active \| hover \| focus | no, a value is required | no | N/A |
| alignment-adjust | auto \| baseline \| before-edge \| text-before-edge \| middle \| central \| after-edge \| text-after-edge \| ideographic \| alphabetic \| hanging \| mathematical \| <percentage> \| <length> \| inherit | auto | no | see prose |
| alignment-baseline | auto \| baseline \| before-edge \| text-before-edge \| middle \| central \| after-edge \| text-after-edge \| ideographic \| alphabetic \| hanging \| mathematical \| inherit | auto | no | N/A |
| allowed-height-scale | [ any \| <percentage> ]* \| inherit | any | yes | intrinsic height |
| allowed-width-scale | [ any \| <percentage> ]* \| inherit | any | yes | intrinsic width |
| auto-restore | true \| false | false | yes | N/A |
| azimuth | <angle> \| [[ left-side \| far-left \| left \| center-left \| center \| center-right \| right \| far-right \| right-side ] \|\| behind ] \| leftwards \| rightwards \| inherit | center | yes | N/A |
| background | [<background-color> \|\| <background-image> \|\| <background-repeat> \|\| <background-attachment> \|\| <background-position> ]] \| inherit | not defined for shorthand properties | no | allowed on 'background-position' |
| background-attachment | scroll \| fixed \| inherit | scroll | no | N/A |
| background-color | <color> \| transparent \| inherit | transparent | no | N/A |
| background-image | <uri-specification> \| none \| inherit | none | no | N/A |
| background-position | [ [<percentage> \| <length> ]{1,2} \| [ [top \| center \| bottom] \|\| [left \| center \| right] ] ] \| inherit | 0% 0% | no | refer to the size of the box itself |
| background-position-horizontal | <percentage> \| <length> \| left \| center \| right \| inherit | 0% | no | refer to the size of the padding-rectangle |
| background-position-vertical | <percentage> \| <length> \| top \| center \| bottom \| inherit | 0% | no | refer to the size of the padding-rectangle |
| background-repeat | repeat \| repeat-x \| repeat-y \| no-repeat \| inherit | repeat | no | N/A |
| baseline-shift | baseline \| sub \| super \| <percentage> \| <length> \| inherit | baseline | no | refers to the "line-height" of the parent area |
| blank-or-not-blank | blank \| not-blank \| any \| inherit | any | no | N/A |
| block-progression-dimension | auto \| <length> \| <percentage> \| <length-range> \| inherit | auto | no | see prose |
| border | [ <border-width> \|\| <border-style> \|\| [ <color> \| transparent ] ] \| inherit | see individual properties | no | N/A |
| border-after-color | <color> \| transparent \| inherit | the value of the 'color' property | no | N/A |
| border-after-precedence | force \| <integer> \| inherit | fo:table: 6, fo:table-cell: 5, fo:table-column: 4, fo:table-row: 3, fo:table-body: 2, fo:table-header: 1, fo:table-footer: 0 | no | N/A |
| border-after-style | <border-style> \| inherit | none | no | N/A |
| border-after-width | <border-width> \| <length-conditional> \| inherit | medium | no | N/A |
| border-before-color | <color> \| transparent \| inherit | the value of the 'color' property | no | N/A |
| border-before-precedence | force \| <integer> \| inherit | fo:table: 6, fo:table-cell: 5, fo:table-column: 4, fo:table-row: 3, fo:table-body: 2, fo:table-header: 1, fo:table-footer: 0 | no | N/A |
| border-before-style | <border-style> \| inherit | none | no | N/A |
| border-before-width | <border-width> \| <length-conditional> \| inherit | medium | no | N/A |
| border-bottom | [ <border-width> \|\| <border-style> \|\| [ <color> \| transparent ] ] \| inherit | see individual properties | no | N/A |
| border-bottom-color | <color> \| transparent \| inherit | the value of the 'color' property | no | N/A |
| border-bottom-style | <border-style> \| inherit | none | no | N/A |
| border-bottom-width | <border-width> \| inherit | medium | no | N/A |
| border-collapse | collapse \| collapse-with-precedence \| separate \| inherit | collapse | yes | N/A |
| border-color | [ <color> \| transparent ]{1,4} \| inherit | see individual properties | no | N/A |
| border-end-color | <color> \| transparent \| inherit | the value of the 'color' property | no | N/A |
| border-end-precedence | force \| <integer> \| inherit | fo:table: 6, fo:table-cell: 5, fo:table-column: 4, fo:table-row: 3, fo:table-body: 2, fo:table-header: 1, fo:table-footer: 0 | no | N/A |
| border-end-style | <border-style> \| inherit | none | no | N/A |
| border-end-width | <border-width> \| <length-conditional> \| inherit | medium | no | N/A |
| border-left | [ <border-width> \|\| <border-style> \|\| [ <color> \| transparent ] ] \| inherit | see individual properties | no | N/A |
| border-left-color | <color> \| transparent \| inherit | the value of the 'color' property | no | N/A |
| border-left-style | <border-style> \| inherit | none | no | N/A |
| border-left-width | <border-width> \| inherit | medium | no | N/A |
| border-right | [ <border-width> \|\| <border-style> \|\| [ <color> \| transparent ] ] \| inherit | see individual properties | no | N/A |
| border-right-color | <color> \| transparent \| inherit | the value of the 'color' property | no | N/A |
| border-right-style | <border-style> \| inherit | none | no | N/A |
| border-right-width | <border-width> \| inherit | medium | no | N/A |
| border-separation | <length-bp-ip-direction> \| inherit | .block-progression-direction="0pt" .inline-progression-direction="0pt" | yes | N/A |
| border-spacing | <length> <length>? \| inherit | 0pt | yes | N/A |
| border-start-color | <color> \| transparent \| inherit | the value of the 'color' property | no | N/A |
| border-start-precedence | force \| <integer> \| inherit | fo:table: 6, fo:table-cell: 5, fo:table-column: 4, fo:table-row: 3, fo:table-body: 2, fo:table-header: 1, fo:table-footer: 0 | no | N/A |
| border-start-style | <border-style> \| inherit | none | no | N/A |
| border-start-width | <border-width> \| <length-conditional> \| inherit | medium | no | N/A |
| border-style | <border-style>{1,4} \| inherit | see individual properties | no | N/A |
| border-top | [ <border-width> \|\| <border-style> \|\| [ <color> \| transparent ] ] \| inherit | see individual properties | no | N/A |
| border-top-color | <color> \| transparent \| inherit | the value of the 'color' property | no | N/A |
| border-top-style | <border-style> \| inherit | none | no | N/A |
| border-top-width | <border-width> \| inherit | medium | no | N/A |
| border-width | <border-width>{1,4} \| inherit | see individual properties | no | N/A |
| bottom | <length> \| <percentage> \| auto \| inherit | auto | no | refer to height of containing block |
| break-after | auto \| column \| page \| even-page \| odd-page \| inherit | auto | no | N/A |
| break-before | auto \| column \| page \| even-page \| odd-page \| inherit | auto | no | N/A |
| caption-side | before \| after \| start \| end \| top \| bottom \| left \| right \| inherit | before | yes | N/A |
| case-name | <name> | none, a value is required | no, a value is required | N/A |
| case-title | <string> | none, a value is required | no, a value is required | N/A |
| change-bar-class | <name> | none, value required | no | N/A |
| change-bar-color | <color> | the value of the color property | yes | N/A |
| change-bar-offset | <length> | 6pt | yes | N/A |
| change-bar-placement | start \| end \| left \| right \| inside \| outside \| alternate | start | yes | N/A |
| change-bar-style | <border-style> | none | yes | N/A |
| change-bar-width | <border-width> | medium | yes | N/A |
| character | <character> | N/A, value is required | no, a value is required | N/A |
| clear | start \| end \| left \| right \| inside \| outside \| both \| none \| inherit | none | no | N/A |
| clip | <shape> \| auto \| inherit | auto | no | N/A |
| color | <color> \| inherit | depends on user agent | yes | N/A |
| color-profile-name | <name> \| inherit | N/A, value is required | no | N/A |
| column-count | <number> \| inherit | 1 | no | N/A |
| column-gap | <length> \| <percentage> \| inherit | 12.0pt | no | refer to width of the region being divided into columns. |
| column-number | <number> | see prose | no | N/A |
| column-width | <length> \| <percentage> | see prose | no | refer to width of table |
| content-height | auto \| scale-to-fit \| scale-down-to-fit \| scale-up-to-fit \| <length> \| <percentage> \| inherit | auto | no | intrinsic height |
| content-type | <string> \| auto | auto | no | N/A |
| content-width | auto \| scale-to-fit \| scale-down-to-fit \| scale-up-to-fit \| <length> \| <percentage> \| inherit | auto | no | intrinsic width |
| country | none \| <country> \| inherit | none | yes | N/A |
| cue | <cue-before> \|\| <cue-after> \| inherit | not defined for shorthand properties | no | N/A |
| cue-after | <uri-specification> \| none \| inherit | none | no | N/A |
| cue-before | <uri-specification> \| none \| inherit | none | no | N/A |
| destination-placement-offset | <length> | 0pt | no | N/A |
| direction | ltr \| rtl \| inherit | ltr | yes | N/A |
| display-align | auto \| before \| center \| after \| inherit | auto | yes | N/A |
| dominant-baseline | auto \| use-script \| no-change \| reset-size \| ideographic \| alphabetic \| hanging \| mathematical \| central \| middle \| text-after-edge \| text-before-edge \| inherit | auto | no (see prose) | N/A |
| elevation | <angle> \| below \| level \| above \| higher \| lower \| inherit | level | yes | N/A |
| empty-cells | show \| hide \| inherit | show | yes | N/A |
| end-indent | <length> \| <percentage> \| inherit | 0pt | yes | refer to inline-progression-dimension of containing reference-area |
| ends-row | true \| false | false | no | N/A |
| extent | <length> \| <percentage> \| inherit | 0.0pt | no | refer to the corresponding block-progression-dimension or inline-progression-dimension of the page-viewport-area. |
| external-destination | empty string \| <uri-specification> | empty string | no | N/A |
| float | before \| start \| end \| left \| right \| inside \| outside \| none \| inherit | none | no | N/A |
| flow-map-name | <name> | none, a value is required | no | N/A |
| flow-map-reference | <name> | see prose | no | N/A |
| flow-name | <name> | an empty name | no, a value is required | N/A |
| flow-name-reference | <name> | none, a value is required | no | N/A |
| font | [ [ <font-style> \|\| <font-variant> \|\| <font-weight> ]? <font-size> [ / <line-height>]? <font-family> ] \| caption \| icon \| menu \| message-box \| small-caption \| status-bar \| inherit | see individual properties | yes | N/A |
| font-family | [[ <family-name> \| <generic-family> ],]* [<family-name> \| <generic-family>] \| inherit | depends on user agent | yes | N/A |
| font-selection-strategy | auto \| character-by-character \| inherit | auto | yes | N/A |
| font-size | <absolute-size> \| <relative-size> \| <length> \| <percentage> \| inherit | medium | yes, the computed value is inherited | refer to parent element's font size |
| font-size-adjust | <number> \| none \| inherit | none | yes | N/A |
| font-stretch | normal \| wider \| narrower \| ultra-condensed \| extra-condensed \| condensed \| semi-condensed \| semi-expanded \| expanded \| extra-expanded \| ultra-expanded \| inherit | normal | yes | N/A |
| font-style | normal \| italic \| oblique \| backslant \| inherit | normal | yes | N/A |
| font-variant | normal \| small-caps \| inherit | normal | yes | N/A |
| font-weight | normal \| bold \| bolder \| lighter \| 100 \| 200 \| 300 \| 400 \| 500 \| 600 \| 700 \| 800 \| 900 \| inherit | normal | yes | N/A |
| force-page-count | auto \| even \| odd \| end-on-even \| end-on-odd \| no-force \| inherit | auto | no | N/A |
| format | <string> | 1 | no | N/A |
| glyph-orientation-horizontal | <angle> \| inherit | 0deg | yes | N/A |
| glyph-orientation-vertical | auto \| <angle> \| inherit | auto | yes | N/A |
| grouping-separator | <character> | no separator | no | N/A |
| grouping-size | <number> | no grouping | no | N/A |
| height | <length> \| <percentage> \| auto \| inherit | auto | no | see prose |
| hyphenate | false \| true \| inherit | false | yes | N/A |
| hyphenation-character | <character> \| inherit | The Unicode hyphen character U+2010 | yes | N/A |
| hyphenation-keep | auto \| column \| page \| inherit | auto | yes | N/A |
| hyphenation-ladder-count | no-limit \| <number> \| inherit | no-limit | yes | N/A |
| hyphenation-push-character-count | <number> \| inherit | 2 | yes | N/A |
| hyphenation-remain-character-count | <number> \| inherit | 2 | yes | N/A |
| id | <id> | see prose | no, see prose | N/A |
| index-class | <string> | empty string | no | N/A |
| index-key | <string> | none | no | N/A |
| indicate-destination | true \| false | false | no | N/A |
| initial-page-number | auto \| auto-odd \| auto-even \| <number> \| inherit | auto | no | N/A |
| inline-progression-dimension | auto \| <length> \| <percentage> \| <length-range> \| inherit | auto | no | see prose |
| internal-destination | empty string \| <idref> | empty string | no | N/A |
| intrinsic-scale-value | <percentage> \| inherit | 100% | yes | user defined |
| intrusion-displace | auto \| none \| line \| indent \| block \| inherit | auto | yes | N/A |
| keep-together | <keep> \| inherit | .within-line=auto, .within-column=auto, .within-page=auto | yes | N/A |
| keep-with-next | <keep> \| inherit | .within-line=auto, .within-column=auto, .within-page=auto | no | N/A |
| keep-with-previous | <keep> \| inherit | .within-line=auto, .within-column=auto, .within-page=auto | no | N/A |
| language | none \| <language> \| inherit | none | yes | N/A |
| last-line-end-indent | <length> \| <percentage> \| inherit | 0pt | yes | refer to inline-progression-dimension of closest ancestor block-area that is not a line-area |
| leader-alignment | none \| reference-area \| page \| inherit | none | yes | N/A |
| leader-length | <length-range> \| <percentage> \| inherit | leader-length.minimum=0pt, .optimum=12.0pt, .maximum=100% | yes | refer to the inline-progression-dimension of content-rectangle of parent area |
| leader-pattern | space \| rule \| dots \| use-content \| inherit | space | yes | N/A |
| leader-pattern-width | use-font-metrics \| <length> \| <percentage> \| inherit | use-font-metrics | yes | refer to the inline-progression-dimension of content-rectangle of parent area |
| left | <length> \| <percentage> \| auto \| inherit | auto | no | refer to width of containing block |
| letter-spacing | normal \| <length> \| <space> \| inherit | normal | yes | N/A |
| letter-value | auto \| alphabetic \| traditional | auto | no | N/A |
| linefeed-treatment | ignore \| preserve \| treat-as-space \| treat-as-zero-width-space \| inherit | treat-as-space | yes | N/A |
| line-height | normal \| <length> \| <number> \| <percentage> \| <space> \| inherit | normal | yes | refer to the font size of the element itself |
| line-height-shift-adjustment | consider-shifts \| disregard-shifts \| inherit | consider-shifts | yes | N/A |
| line-stacking-strategy | line-height \| font-height \| max-height \| inherit | max-height | yes | N/A |
| margin | <margin-width>{1,4} \| inherit | not defined for shorthand properties | no | refer to width of containing block |
| margin-bottom | <margin-width> \| inherit | 0pt | no | refer to width of containing block |
| margin-left | <margin-width> \| inherit | 0pt | no | refer to width of containing block |
| margin-right | <margin-width> \| inherit | 0pt | no | refer to width of containing block |
| margin-top | <margin-width> \| inherit | 0pt | no | refer to width of containing block |
| marker-class-name | <name> | an empty name | no, a value is required | N/A |
| master-name | <name> | an empty name | no, a value is required | N/A |
| master-reference | <name> | an empty name | no, a value is required | N/A |
| max-height | <length> \| <percentage> \| none \| inherit | none | no | refer to height of containing block |
| maximum-repeats | <number> \| no-limit \| inherit | no-limit | no | N/A |
| max-width | <length> \| <percentage> \| none \| inherit | none | no | refer to width of containing block |
| media-usage | auto \| paginate \| bounded-in-one-dimension \| unbounded | auto | no | NA |
| merge-pages-across-index-key-references | merge \| leave-separate | merge | yes | N/A |
| merge-ranges-across-index-key-references | merge \| leave-separate | merge | yes | N/A |
| merge-sequential-page-numbers | merge \| leave-separate | merge | yes | N/A |
| min-height | <length> \| <percentage> \| inherit | 0pt | no | refer to height of containing block |
| min-width | <length> \| <percentage> \| inherit | depends on UA | no | refer to width of containing block |
| number-columns-repeated | <number> | 1 | no | N/A |
| number-columns-spanned | <number> | 1 | no | N/A |
| number-rows-spanned | <number> | 1 | no | N/A |
| odd-or-even | odd \| even \| any \| inherit | any | no | N/A |
| orphans | <integer> \| inherit | 2 | yes | N/A |
| overflow | visible \| hidden \| scroll \| error-if-overflow \| repeat \| auto \| inherit | auto | no | N/A |
| padding | <padding-width>{1,4} \| inherit | not defined for shorthand properties | no | refer to width of containing block |
| padding-after | <padding-width> \| <length-conditional> \| inherit | 0pt | no | refer to width of containing block |
| padding-before | <padding-width> \| <length-conditional> \| inherit | 0pt | no | refer to width of containing block |
| padding-bottom | <padding-width> \| inherit | 0pt | no | refer to width of containing block |
| padding-end | <padding-width> \| <length-conditional> \| inherit | 0pt | no | refer to width of containing block |
| padding-left | <padding-width> \| inherit | 0pt | no | refer to width of containing block |
| padding-right | <padding-width> \| inherit | 0pt | no | refer to width of containing block |
| padding-start | <padding-width> \| <length-conditional> \| inherit | 0pt | no | refer to width of containing block |
| padding-top | <padding-width> \| inherit | 0pt | no | refer to width of containing block |
| page-break-after | auto \| always \| avoid \| left \| right \| inherit | auto | no | N/A |
| page-break-before | auto \| always \| avoid \| left \| right \| inherit | auto | no | N/A |
| page-break-inside | avoid \| auto \| inherit | auto | yes | N/A |
| page-citation-strategy | [ all \| normal \| non-blank \| inherit | all | no | N/A |
| page-height | auto \| indefinite \| <length> \| inherit | auto | no | N/A |
| page-number-treatment | link \| no-link | no-link | yes | N/A |
| page-position | only \| first \| last \| rest \| any \| inherit | any | no | N/A |
| page-width | auto \| indefinite \| <length> \| inherit | auto | no | N/A |
| pause | [<time> \| <percentage>]{1,2} \| inherit | depends on user agent | no | see descriptions of 'pause-before' and 'pause-after' |
| pause-after | <time> \| <percentage> \| inherit | depends on user agent | no | see prose |
| pause-before | <time> \| <percentage> \| inherit | depends on user agent | no | see prose |
| pitch | <frequency> \| x-low \| low \| medium \| high \| x-high \| inherit | medium | yes | N/A |
| pitch-range | <number> \| inherit | 50 | yes | N/A |
| play-during | <uri-specification> mix? repeat? \| auto \| none \| inherit | auto | no | N/A |
| position | static \| relative \| absolute \| fixed \| inherit | static | no | N/A |
| precedence | true \| false \| inherit | false | no | N/A |
| provisional-distance-between-starts | <length> \| <percentage> \| inherit | 24.0pt | yes | refer to inline-progression-dimension of closest ancestor block-area that is not a line-area |
| provisional-label-separation | <length> \| <percentage> \| inherit | 6.0pt | yes | refer to inline-progression-dimension of closest ancestor block-area that is not a line-area |
| reference-orientation | 0 \| 90 \| 180 \| 270 \| -90 \| -180 \| -270 \| inherit | 0 | no | N/A |
| ref-id | <idref> \| inherit | none, value required | no | N/A |
| ref-index-key | <string> | none, value required | no | N/A |
| region-name | xsl-region-body \| xsl-region-start \| xsl-region-end \| xsl-region-before \| xsl-region-after \| <name> | see prose | no, a value is required | N/A |
| region-name-reference | <name> | none, a value is required | no | N/A |
| relative-align | before \| baseline \| inherit | before | yes | N/A |
| relative-position | static \| relative \| inherit | static | no | N/A |
| rendering-intent | auto \| perceptual \| relative-colorimetric \| saturation \| absolute-colorimetric \| inherit | auto | no | N/A |
| retrieve-boundary | page \| page-sequence \| document | page-sequence | no | N/A |
| retrieve-boundary-within-table | table \| table-fragment \| page | table | no | N/A |
| retrieve-class-name | <name> | an empty name | no, a value is required | N/A |
| retrieve-position | first-starting-within-page \| first-including-carryover \| last-starting-within-page \| last-ending-within-page | first-starting-within-page | no | N/A |
| retrieve-position-within-table | first-starting \| first-including-carryover \| last-starting \| last-ending | first-starting | no | N/A |
| richness | <number> \| inherit | 50 | yes | N/A |
| right | <length> \| <percentage> \| auto \| inherit | auto | no | refer to width of containing block |
| role | <string> \| <uri-specification> \| none \| inherit | none | no | N/A |
| rule-style | none \| dotted \| dashed \| solid \| double \| groove \| ridge \| inherit | solid | yes | N/A |
| rule-thickness | <length> | 1.0pt | yes | N/A |
| scale-option | width \| height \| inherit | width | yes | N/A |
| scaling | uniform \| non-uniform \| inherit | uniform | no | N/A |
| scaling-method | auto \| integer-pixels \| resample-any-method \| inherit | auto | no | N/A |
| score-spaces | true \| false \| inherit | true | yes | N/A |
| script | none \| auto \| <script> \| inherit | auto | yes | N/A |
| show-destination | replace \| new | replace | no | N/A |
| size | <length>{1,2} \| auto \| landscape \| portrait \| inherit | auto | N/A [XSL:no, is optional] | N/A |
| source-document | <uri-specification> [<uri-specification>]* \| none \| inherit | none | no | N/A |
| space-after | <space> \| inherit | space.minimum=0pt, .optimum=0pt, .maximum=0pt, .conditionality=discard, .precedence=0 | no | N/A (Differs from margin-bottom in CSS) |
| space-before | <space> \| inherit | space.minimum=0pt, .optimum=0pt, .maximum=0pt, .conditionality=discard, .precedence=0 | no | N/A (Differs from margin-top in CSS) |
| space-end | <space> \| <percentage> \| inherit | space.minimum=0pt, .optimum=0pt, .maximum=0pt, .conditionality=discard, .precedence=0 | no | refer to inline-progression-dimension of closest ancestor block-area that is not a line-area |
| space-start | <space> \| <percentage> \| inherit | space.minimum=0pt, .optimum=0pt, .maximum=0pt, .conditionality=discard, .precedence=0 | no | refer to inline-progression-dimension of closest ancestor block-area that is not a line-area |
| span | none \| all \| inherit | none | no | N/A |
| speak | normal \| none \| spell-out \| inherit | normal | yes | N/A |
| speak-header | once \| always \| inherit | once | yes | N/A |
| speak-numeral | digits \| continuous \| inherit | continuous | yes | N/A |
| speak-punctuation | code \| none \| inherit | none | yes | N/A |
| speech-rate | <number> \| x-slow \| slow \| medium \| fast \| x-fast \| faster \| slower \| inherit | medium | yes | N/A |
| src | <uri-specification> \| inherit | none, value required | no | N/A |
| start-indent | <length> \| <percentage> \| inherit | 0pt | yes | refer to inline-progression-dimension of containing reference-area |
| starting-state | show \| hide | show | no | N/A |
| starts-row | true \| false | false | no | N/A |
| stress | <number> \| inherit | 50 | yes | N/A |
| suppress-at-line-break | auto \| suppress \| retain \| inherit | auto | no | N/A |
| switch-to | xsl-preceding \| xsl-following \| xsl-any \| <name>[ <name>]* | xsl-any | no | N/A |
| table-layout | auto \| fixed \| inherit | auto | no | N/A |
| table-omit-footer-at-break | true \| false | false | no | N/A |
| table-omit-header-at-break | true \| false | false | no | N/A |
| target-presentation-context | use-target-processing-context \| <uri-specification> | use-target-processing-context | no | N/A |
| target-processing-context | document-root \| <uri-specification> | document-root | no | N/A |
| target-stylesheet | use-normal-stylesheet \| <uri-specification> | use-normal-stylesheet | no | N/A |
| text-align | start \| center \| end \| justify \| inside \| outside \| left \| right \| <string> \| inherit | start | yes | N/A |
| text-align-last | relative \| start \| center \| end \| justify \| inside \| outside \| left \| right \| inherit | relative | yes | N/A |
| text-altitude | use-font-metrics \| <length> \| <percentage> \| inherit | use-font-metrics | no | refer to font's em-height |
| text-decoration | none \| [ [ underline \| no-underline] \|\| [ overline \| no-overline ] \|\| [ line-through \| no-line-through ] \|\| [ blink \| no-blink ] ] \| inherit | none | no, but see prose | N/A |
| text-depth | use-font-metrics \| <length> \| <percentage> \| inherit | use-font-metrics | no | refer to font's em-height |
| text-indent | <length> \| <percentage> \| inherit | 0pt | yes | refer to width of containing block |
| text-shadow | none \| [<color> \|\| <length> <length> <length>? ,]* [<color> \|\| <length> <length> <length>?] \| inherit | none | no, see prose | N/A |
| text-transform | capitalize \| uppercase \| lowercase \| none \| inherit | none | yes | N/A |
| top | <length> \| <percentage> \| auto \| inherit | auto | no | refer to height of containing block |
| treat-as-word-space | auto \| true \| false \| inherit | auto | no | N/A |
| unicode-bidi | normal \| embed \| bidi-override \| inherit | normal | no | N/A |
| vertical-align | baseline \| middle \| sub \| super \| text-top \| text-bottom \| <percentage> \| <length> \| top \| bottom \| inherit | baseline | no | refer to the 'line-height' of the element itself |
| visibility | visible \| hidden \| collapse \| inherit | visible | yes | N/A |
| voice-family | [[<specific-voice> \| <generic-voice> ],]* [<specific-voice> \| <generic-voice> ] \| inherit | depends on user agent | yes | N/A |
| volume | <number> \| <percentage> \| silent \| x-soft \| soft \| medium \| loud \| x-loud \| inherit | medium | yes | refer to inherited value |
| white-space | normal \| pre \| nowrap \| inherit | normal | yes | N/A |
| white-space-collapse | false \| true \| inherit | true | yes | N/A |
| white-space-treatment | ignore \| preserve \| ignore-if-before-linefeed \| ignore-if-after-linefeed \| ignore-if-surrounding-linefeed \| inherit | ignore-if-surrounding-linefeed | yes | N/A |
| widows | <integer> \| inherit | 2 | yes | N/A |
| width | <length> \| <percentage> \| auto \| inherit | auto | no | refer to width of containing block |
| word-spacing | normal \| <length> \| <space> \| inherit | normal | yes | N/A |
| wrap-option | no-wrap \| wrap \| inherit | wrap | yes | N/A |
| writing-mode | lr-tb \| rl-tb \| tb-rl \| tb-lr \| bt-lr \| bt-rl \| lr-bt \| rl-bt \| lr-alternating-rl-bt \| lr-alternating-rl-tb \| lr-inverting-rl-bt \| lr-inverting-rl-tb \| tb-lr-in-lr-pairs \| lr \| rl \| tb \| inherit | lr-tb | yes (see prose) | N/A |
| xml.lang | <language-country> \| inherit | not defined for shorthand properties | yes | N/A |
| z-index | auto \| <integer> \| inherit | auto | no | N/A |

## Property Table: Part II

<!-- Source: https://www.w3.org/TR/xslfo20/#prtab2 -->

The Trait Mapping Values are explained in the [Trait Mapping Values](#trait-mapping-values) section above.

| Property | Trait Mapping | Conformance |
|---|---|---|
| absolute-position | See prose. | Complete |
| active-state | Action | Extended.Fallback: N/A use fallback for fo:multi-properties |
| alignment-adjust | Formatting | Basic |
| alignment-baseline | Formatting | Basic |
| allowed-height-scale | Formatting | Extended.Fallback: Initial value |
| allowed-width-scale | Formatting | Extended.Fallback: Initial value |
| auto-restore | Action | Extended.Fallback: N/A use fallback for fo:multi-switch |
| azimuth | Rendering | Basic |
| background | Shorthand | Complete |
| background-attachment | Rendering | Extended.Fallback: Initial value |
| background-color | Rendering | Basic |
| background-image | Rendering | Extended.Fallback: Initial value |
| background-position | Shorthand | Complete |
| background-position-horizontal | Value change | Extended.Fallback: Initial value |
| background-position-vertical | Value change | Extended.Fallback: Initial value |
| background-repeat | Rendering | Extended.Fallback: no-repeat |
| baseline-shift | Formatting | Basic |
| blank-or-not-blank | Specification | Extended.Fallback: N/A use fallback for fo:repeatable-page-master-alternatives |
| block-progression-dimension | Formatting | Basic |
| border | Shorthand | Complete |
| border-after-color | Rendering | Basic |
| border-after-precedence | Formatting | Basic |
| border-after-style | Rendering | Basic |
| border-after-width | Formatting and Rendering | Basic |
| border-before-color | Rendering | Basic |
| border-before-precedence | Formatting | Basic |
| border-before-style | Rendering | Basic |
| border-before-width | Formatting and Rendering | Basic |
| border-bottom | Shorthand | Complete |
| border-bottom-color | Disappears | Basic |
| border-bottom-style | Disappears | Basic |
| border-bottom-width | Disappears | Basic |
| border-collapse | Formatting | Extended.Fallback: Initial value |
| border-color | Shorthand | Complete |
| border-end-color | Rendering | Basic |
| border-end-precedence | Formatting | Basic |
| border-end-style | Rendering | Basic |
| border-end-width | Formatting and Rendering | Basic |
| border-left | Shorthand | Complete |
| border-left-color | Disappears | Basic |
| border-left-style | Disappears | Basic |
| border-left-width | Disappears | Basic |
| border-right | Shorthand | Complete |
| border-right-color | Disappears | Basic |
| border-right-style | Disappears | Basic |
| border-right-width | Disappears | Basic |
| border-separation | Formatting | Extended.Fallback: Initial value |
| border-spacing | Shorthand | Complete |
| border-start-color | Rendering | Basic |
| border-start-precedence | Formatting | Basic |
| border-start-style | Rendering | Basic |
| border-start-width | Formatting and Rendering | Basic |
| border-style | Shorthand | Complete |
| border-top | Shorthand | Complete |
| border-top-color | Disappears | Basic |
| border-top-style | Disappears | Basic |
| border-top-width | Disappears | Basic |
| border-width | Shorthand | Complete |
| bottom | Formatting | Extended.Fallback: N/A due to fallback for absolute-position, relative-position |
| break-after | Formatting | Basic |
| break-before | Formatting | Basic |
| caption-side | Formatting | Complete |
| case-name | Action | Extended.Fallback: N/A use fallback for fo:multi-switch |
| case-title | Action | Extended.Fallback: N/A use fallback for fo:multi-switch |
| change-bar-class | Reference | Extended.Fallback: N/A use fallback for fo:change-bar-begin, fo:change-bar-end |
| change-bar-color | Rendering | Extended.Fallback: N/A use fallback for fo:change-bar-begin, fo:change-bar-end |
| change-bar-offset | Formatting | Extended.Fallback: N/A use fallback for fo:change-bar-begin, fo:change-bar-end |
| change-bar-placement | Formatting | Extended.Fallback: N/A use fallback for fo:change-bar-begin, fo:change-bar-end |
| change-bar-style | Rendering | Extended.Fallback: N/A use fallback for fo:change-bar-begin, fo:change-bar-end |
| change-bar-width | Rendering | Extended.Fallback: N/A use fallback for fo:change-bar-begin, fo:change-bar-end |
| character | Formatting | Basic |
| clear | Formatting | Extended.Fallback: N/A use fallback for fo:float |
| clip | Rendering | Extended.Fallback: Initial value |
| color | Rendering | Basic |
| color-profile-name | Formatting | Extended.Fallback: N/A use fallback for fo:color-profile |
| column-count | Specification | Extended.Fallback: Initial value |
| column-gap | Specification | Extended.Fallback: N/A due to fallback for column-count |
| column-number | Value change | Basic |
| column-width | Specification | Basic |
| content-height | Formatting | Extended.Fallback: Initial value |
| content-type | Formatting | Extended.Fallback: Initial value |
| content-width | Formatting | Extended.Fallback: Initial value |
| country | Formatting | Extended.Fallback: Initial value |
| cue | Shorthand | Complete |
| cue-after | Rendering | Basic |
| cue-before | Rendering | Basic |
| destination-placement-offset | Action | Extended.Fallback: N/A use fallback for fo:basic-link |
| direction | See prose. | Basic |
| display-align | Formatting | Extended.Fallback: Initial value |
| dominant-baseline | Formatting | Basic |
| elevation | Rendering | Basic |
| empty-cells | Formatting | Extended.Fallback: Initial value |
| end-indent | Formatting | Basic |
| ends-row | Formatting | Extended.Fallback: Initial value |
| extent | Specification | Extended.Fallback: N/A use fallback for fo:region-before, fo:region-after, fo:region-start, and fo:region-end |
| external-destination | Action | Extended.Fallback: N/A use fallback for fo:basic-link |
| float | Formatting | Extended.Fallback: N/A use fallback for fo:float |
| flow-map-name | Specification | Extended.Fallback: N/A use fallback for fo:flow-map |
| flow-map-reference | Specification | Extended.Fallback: N/A use fallback for fo:flow-map |
| flow-name | Reference | Basic |
| flow-name-reference | Specification | Extended.Fallback: N/A use fallback for fo:flow-map |
| font | Shorthand | Complete |
| font-family | Font selection | Basic |
| font-selection-strategy | Font selection | Complete |
| font-size | Formatting and Rendering | Basic |
| font-size-adjust | Font selection | Extended.Fallback: Initial value |
| font-stretch | Font selection | Extended.Fallback: Initial value |
| font-style | Font selection | Basic |
| font-variant | Font selection | Basic |
| font-weight | Font selection | Basic |
| force-page-count | Specification | Extended.Fallback: no-force |
| format | Formatting | Basic |
| glyph-orientation-horizontal | Formatting | Extended.Fallback: Initial value |
| glyph-orientation-vertical | Formatting | Extended.Fallback: Initial value |
| grouping-separator | Formatting | Extended.Fallback: no separator |
| grouping-size | Formatting | Extended.Fallback: no grouping |
| height | Disappears | Basic |
| hyphenate | Formatting | Extended.Fallback: Initial value |
| hyphenation-character | Formatting | Extended.Fallback: N/A due to fallback for hyphenate |
| hyphenation-keep | Formatting | Extended.Fallback: N/A due to fallback for hyphenate |
| hyphenation-ladder-count | Formatting | Extended.Fallback: N/A due to fallback for hyphenate |
| hyphenation-push-character-count | Formatting | Extended.Fallback: N/A due to fallback for hyphenate |
| hyphenation-remain-character-count | Formatting | Extended.Fallback: N/A due to fallback for hyphenate |
| id | Reference | Basic |
| index-class | Reference | Extended.Fallback: N/A use fallback for fo:index-page-citation-list |
| index-key | Reference | Extended.Fallback: N/A use fallback for fo:index-page-citation-list |
| indicate-destination | Action | Extended.Fallback: N/A use fallback for fo:basic-link |
| initial-page-number | Formatting | Basic |
| inline-progression-dimension | Formatting | Basic |
| internal-destination | Action | Extended.Fallback: N/A use fallback for fo:basic-link |
| intrinsic-scale-value | Refine | Extended.Fallback: N/A use fallback for fo:scaling-value-citation |
| intrusion-displace | Formatting | Extended.Fallback: none |
| keep-together | Formatting | Extended.Fallback: Initial value |
| keep-with-next | Formatting | Basic |
| keep-with-previous | Formatting | Basic |
| language | Value change | Extended.Fallback: Initial value |
| last-line-end-indent | Formatting | Extended.Fallback: Initial value |
| leader-alignment | Formatting | Extended.Fallback: Initial value |
| leader-length | Formatting | Basic |
| leader-pattern | Formatting | Basic |
| leader-pattern-width | Formatting | Extended.Fallback: Initial value |
| left | Formatting | Extended.Fallback: N/A due to fallback for absolute-position, relative-position |
| letter-spacing | Disappears | Extended.Fallback: Initial value |
| letter-value | Formatting | Basic |
| linefeed-treatment | Formatting | Extended.Fallback: Initial value |
| line-height | Formatting | Basic |
| line-height-shift-adjustment | Formatting | Extended.Fallback: Initial value |
| line-stacking-strategy | Formatting | Basic |
| margin | Shorthand | Complete |
| margin-bottom | Disappears | Basic |
| margin-left | Disappears | Basic |
| margin-right | Disappears | Basic |
| margin-top | Disappears | Basic |
| marker-class-name | Formatting | Extended.Fallback: N/A use fallback for fo:marker |
| master-name | Specification | Basic |
| master-reference | Specification | Basic |
| max-height | Shorthand | Complete |
| maximum-repeats | Specification | Extended.Fallback: N/A use fallback for fo:repeatable-page-master-reference and fo:repeatable-page-master-alternatives |
| max-width | Shorthand | Complete |
| media-usage | Formatting | Extended.Fallback: Initial value |
| merge-pages-across-index-key-references | Specification | Extended.Fallback: N/A use fallback for fo:index-page-citation-list |
| merge-ranges-across-index-key-references | Specification | Extended.Fallback: N/A use fallback for fo:index-page-citation-list |
| merge-sequential-page-numbers | Specification | Extended.Fallback: N/A use fallback for fo:index-page-citation-list |
| min-height | Shorthand | Complete |
| min-width | Shorthand | Complete |
| number-columns-repeated | Specification | Basic |
| number-columns-spanned | Formatting | Basic |
| number-rows-spanned | Formatting | Basic |
| odd-or-even | Specification | Extended.Fallback: N/A use fallback for fo:repeatable-page-master-alternatives |
| orphans | Formatting | Basic |
| overflow | Formatting | Basic |
| padding | Shorthand | Complete |
| padding-after | Formatting and Rendering | Basic |
| padding-before | Formatting and Rendering | Basic |
| padding-bottom | Disappears | Basic |
| padding-end | Formatting and Rendering | Basic |
| padding-left | Disappears | Basic |
| padding-right | Disappears | Basic |
| padding-start | Formatting and Rendering | Basic |
| padding-top | Disappears | Basic |
| page-break-after | Shorthand | Complete |
| page-break-before | Shorthand | Complete |
| page-break-inside | Shorthand | Complete |
| page-citation-strategy | Specification | Extended.Fallback: N/A use fallback for fo:page-number-citation-last |
| page-height | Specification | Basic |
| page-number-treatment | Action | Extended.Fallback: N/A use fallback for fo:index-page-citation-list |
| page-position | Specification | Extended.Fallback: N/A use fallback for fo:repeatable-page-master-alternatives |
| page-width | Specification | Basic |
| pause | Shorthand | Complete |
| pause-after | Rendering | Basic |
| pause-before | Rendering | Basic |
| pitch | Rendering | Basic |
| pitch-range | Rendering | Basic |
| play-during | Rendering | Basic |
| position | Shorthand | Complete |
| precedence | Specification | Extended.Fallback: N/A use fallback for fo:region-before and fo:region-after |
| provisional-distance-between-starts | Specification | Basic |
| provisional-label-separation | Specification | Basic |
| reference-orientation | See prose. | Extended.Fallback: Initial value |
| ref-id | Reference | Extended.Fallback: N/A use fallback for fo:page-number-citation |
| ref-index-key | Reference | Extended.Fallback: N/A use fallback for fo:index-page-citation-list |
| region-name | Specification | Basic |
| region-name-reference | Specification | Extended.Fallback: N/A use fallback for fo:flow-map |
| relative-align | Formatting | Extended.Fallback: Initial value |
| relative-position | See prose. | Extended.Fallback: Initial value |
| rendering-intent | Formatting | Extended.Fallback: N/A use fallback for fo:color-profile |
| retrieve-boundary | Formatting | Extended.Fallback: N/A use fallback for fo:retrieve-marker |
| retrieve-boundary-within-table | Formatting | Extended.Fallback: N/A use fallback for fo:retrieve-table-marker |
| retrieve-class-name | Formatting | Extended.Fallback: N/A use fallback for fo:retrieve-marker |
| retrieve-position | Formatting | Extended.Fallback: N/A use fallback for fo:retrieve-marker |
| retrieve-position-within-table | Formatting | Extended.Fallback: N/A use fallback for fo:retrieve-table-marker |
| richness | Rendering | Basic |
| right | Formatting | Extended.Fallback: N/A due to fallback for absolute-position, relative-position |
| role | Rendering | Basic |
| rule-style | Rendering | Basic |
| rule-thickness | Rendering | Basic |
| scale-option | Refine | Extended.Fallback: N/A use fallback for fo:scaling-value-citation |
| scaling | Formatting | Extended.Fallback: Initial value |
| scaling-method | Formatting | Extended.Fallback: Initial value |
| score-spaces | Formatting | Extended.Fallback: Initial value |
| script | Formatting | Extended.Fallback: none |
| show-destination | Action | Extended.Fallback: N/A use fallback for fo:basic-link |
| size | Shorthand | Complete |
| source-document | Rendering | Basic |
| space-after | Formatting | Basic |
| space-before | Formatting | Basic |
| space-end | Formatting | Basic |
| space-start | Formatting | Basic |
| span | Formatting | Extended.Fallback: Initial value |
| speak | Rendering | Basic |
| speak-header | Rendering | Basic |
| speak-numeral | Rendering | Basic |
| speak-punctuation | Rendering | Basic |
| speech-rate | Rendering | Basic |
| src | Reference | Basic |
| start-indent | Formatting | Basic |
| starting-state | Action | Extended.Fallback: N/A use fallback for fo:multi-switch |
| starts-row | Formatting | Extended.Fallback: Initial value |
| stress | Rendering | Basic |
| suppress-at-line-break | Formatting | Extended.Fallback: Initial value |
| switch-to | Action | Extended.Fallback: N/A use fallback for fo:multi-switch |
| table-layout | Formatting | Extended.Fallback: fixed |
| table-omit-footer-at-break | Formatting | Extended.Fallback: Initial value |
| table-omit-header-at-break | Formatting | Extended.Fallback: Initial value |
| target-presentation-context | Action | Extended.Fallback: N/A use fallback for fo:basic-link |
| target-processing-context | Action | Extended.Fallback: N/A use fallback for fo:basic-link |
| target-stylesheet | Action | Extended.Fallback: N/A use fallback for fo:basic-link |
| text-align | Value change | Basic |
| text-align-last | Value change | Extended.Fallback: Initial value |
| text-altitude | Formatting | Extended.Fallback: Initial value |
| text-decoration | See prose. | Extended.Fallback: Initial value |
| text-depth | Formatting | Extended.Fallback: Initial value |
| text-indent | Formatting | Basic |
| text-shadow | Rendering | Extended.Fallback: Initial value |
| text-transform | Refine | Extended.Fallback: Initial value |
| top | Formatting | Extended.Fallback: N/A due to fallback for absolute-position, relative-position |
| treat-as-word-space | Formatting | Extended.Fallback: Initial value |
| unicode-bidi | Formatting | Extended.Fallback: See prose |
| vertical-align | Shorthand | Complete |
| visibility | Magic | Extended.Fallback: Initial value |
| voice-family | Rendering | Basic |
| volume | Rendering | Basic |
| white-space | Shorthand | Complete |
| white-space-collapse | Formatting | Extended.Fallback: Initial value |
| white-space-treatment | Formatting | Extended.Fallback: Initial value |
| widows | Formatting | Basic |
| width | Disappears | Basic |
| word-spacing | Disappears | Extended.Fallback: Initial value |
| wrap-option | Formatting | Basic |
| writing-mode | See prose. | Basic |
| xml.lang | Shorthand | Complete |
| z-index | Value change | Extended.Fallback: N/A due to fallback for fo:block-container |

## Properties and the FOs They Apply To

<!-- Source: https://www.w3.org/TR/xslfo20/#prapply -->

For each property, the formatting objects it applies to are listed. Note that for some formatting objects there are qualifications on applicability or values permitted.

**absolute-position**: fo:block-container

**active-state**: fo:multi-property-set

**alignment-adjust**: fo:character, fo:external-graphic, fo:instream-foreign-object, fo:inline, fo:inline-container, fo:leader, fo:page-number, fo:page-number-citation, fo:page-number-citation-last, fo:scaling-value-citation, fo:basic-link

**alignment-baseline**: fo:character, fo:external-graphic, fo:instream-foreign-object, fo:inline, fo:inline-container, fo:leader, fo:page-number, fo:page-number-citation, fo:page-number-citation-last, fo:scaling-value-citation, fo:basic-link

**allowed-height-scale**: fo:external-graphic, fo:instream-foreign-object

**allowed-width-scale**: fo:external-graphic, fo:instream-foreign-object

**auto-restore**: fo:multi-switch

**azimuth**: fo:title, fo:block, fo:bidi-override, fo:character, fo:initial-property-set, fo:external-graphic, fo:instream-foreign-object, fo:inline, fo:leader, fo:page-number, fo:page-number-citation, fo:page-number-citation-last, fo:scaling-value-citation, fo:table-and-caption, fo:table, fo:table-caption, fo:table-header, fo:table-footer, fo:table-body, fo:table-row, fo:table-cell, fo:list-block, fo:list-item, fo:basic-link, fo:change-bar-begin, fo:change-bar-end

**background-attachment**: fo:region-body, fo:region-before, fo:region-after, fo:region-start, fo:region-end, fo:title, fo:block, fo:block-container, fo:character, fo:initial-property-set, fo:external-graphic, fo:instream-foreign-object, fo:inline, fo:inline-container, fo:leader, fo:page-number, fo:page-number-citation, fo:page-number-citation-last, fo:scaling-value-citation, fo:table-and-caption, fo:table, fo:table-column, fo:table-caption, fo:table-header, fo:table-footer, fo:table-body, fo:table-row, fo:table-cell, fo:list-block, fo:list-item, fo:basic-link

**background-color**: fo:region-body, fo:region-before, fo:region-after, fo:region-start, fo:region-end, fo:title, fo:block, fo:block-container, fo:character, fo:initial-property-set, fo:external-graphic, fo:instream-foreign-object, fo:inline, fo:inline-container, fo:leader, fo:page-number, fo:page-number-citation, fo:page-number-citation-last, fo:scaling-value-citation, fo:table-and-caption, fo:table, fo:table-column, fo:table-caption, fo:table-header, fo:table-footer, fo:table-body, fo:table-row, fo:table-cell, fo:list-block, fo:list-item, fo:basic-link

**background-image**: fo:region-body, fo:region-before, fo:region-after, fo:region-start, fo:region-end, fo:title, fo:block, fo:block-container, fo:character, fo:initial-property-set, fo:external-graphic, fo:instream-foreign-object, fo:inline, fo:inline-container, fo:leader, fo:page-number, fo:page-number-citation, fo:page-number-citation-last, fo:scaling-value-citation, fo:table-and-caption, fo:table, fo:table-column, fo:table-caption, fo:table-header, fo:table-footer, fo:table-body, fo:table-row, fo:table-cell, fo:list-block, fo:list-item, fo:basic-link

**background-position-horizontal**: fo:region-body, fo:region-before, fo:region-after, fo:region-start, fo:region-end, fo:title, fo:block, fo:block-container, fo:character, fo:initial-property-set, fo:external-graphic, fo:instream-foreign-object, fo:inline, fo:inline-container, fo:leader, fo:page-number, fo:page-number-citation, fo:page-number-citation-last, fo:scaling-value-citation, fo:table-and-caption, fo:table, fo:table-column, fo:table-caption, fo:table-header, fo:table-footer, fo:table-body, fo:table-row, fo:table-cell, fo:list-block, fo:list-item, fo:basic-link

**background-position-vertical**: fo:region-body, fo:region-before, fo:region-after, fo:region-start, fo:region-end, fo:title, fo:block, fo:block-container, fo:character, fo:initial-property-set, fo:external-graphic, fo:instream-foreign-object, fo:inline, fo:inline-container, fo:leader, fo:page-number, fo:page-number-citation, fo:page-number-citation-last, fo:scaling-value-citation, fo:table-and-caption, fo:table, fo:table-column, fo:table-caption, fo:table-header, fo:table-footer, fo:table-body, fo:table-row, fo:table-cell, fo:list-block, fo:list-item, fo:basic-link

**background-repeat**: fo:region-body, fo:region-before, fo:region-after, fo:region-start, fo:region-end, fo:title, fo:block, fo:block-container, fo:character, fo:initial-property-set, fo:external-graphic, fo:instream-foreign-object, fo:inline, fo:inline-container, fo:leader, fo:page-number, fo:page-number-citation, fo:page-number-citation-last, fo:scaling-value-citation, fo:table-and-caption, fo:table, fo:table-column, fo:table-caption, fo:table-header, fo:table-footer, fo:table-body, fo:table-row, fo:table-cell, fo:list-block, fo:list-item, fo:basic-link

**baseline-shift**: fo:character, fo:external-graphic, fo:instream-foreign-object, fo:inline, fo:inline-container, fo:leader, fo:page-number, fo:page-number-citation, fo:page-number-citation-last, fo:scaling-value-citation, fo:basic-link

**blank-or-not-blank**: fo:conditional-page-master-reference

**block-progression-dimension**: fo:block-container, fo:external-graphic, fo:instream-foreign-object, fo:inline, fo:inline-container, fo:table, fo:table-caption, fo:table-row, fo:table-cell

**border-after-color**: fo:region-body, fo:region-before, fo:region-after, fo:region-start, fo:region-end, fo:title, fo:block, fo:block-container, fo:character, fo:initial-property-set, fo:external-graphic, fo:instream-foreign-object, fo:inline, fo:inline-container, fo:leader, fo:page-number, fo:page-number-citation, fo:page-number-citation-last, fo:scaling-value-citation, fo:table-and-caption, fo:table, fo:table-column, fo:table-caption, fo:table-header, fo:table-footer, fo:table-body, fo:table-row, fo:table-cell, fo:list-block, fo:list-item, fo:basic-link

**border-after-precedence**: fo:table, fo:table-column, fo:table-header, fo:table-footer, fo:table-body, fo:table-row, fo:table-cell

**border-after-style**: fo:region-body, fo:region-before, fo:region-after, fo:region-start, fo:region-end, fo:title, fo:block, fo:block-container, fo:character, fo:initial-property-set, fo:external-graphic, fo:instream-foreign-object, fo:inline, fo:inline-container, fo:leader, fo:page-number, fo:page-number-citation, fo:page-number-citation-last, fo:scaling-value-citation, fo:table-and-caption, fo:table, fo:table-column, fo:table-caption, fo:table-header, fo:table-footer, fo:table-body, fo:table-row, fo:table-cell, fo:list-block, fo:list-item, fo:basic-link

**border-after-width**: fo:region-body, fo:region-before, fo:region-after, fo:region-start, fo:region-end, fo:title, fo:block, fo:block-container, fo:character, fo:initial-property-set, fo:external-graphic, fo:instream-foreign-object, fo:inline, fo:inline-container, fo:leader, fo:page-number, fo:page-number-citation, fo:page-number-citation-last, fo:scaling-value-citation, fo:table-and-caption, fo:table, fo:table-column, fo:table-caption, fo:table-header, fo:table-footer, fo:table-body, fo:table-row, fo:table-cell, fo:list-block, fo:list-item, fo:basic-link

**border-before-color**: fo:region-body, fo:region-before, fo:region-after, fo:region-start, fo:region-end, fo:title, fo:block, fo:block-container, fo:character, fo:initial-property-set, fo:external-graphic, fo:instream-foreign-object, fo:inline, fo:inline-container, fo:leader, fo:page-number, fo:page-number-citation, fo:page-number-citation-last, fo:scaling-value-citation, fo:table-and-caption, fo:table, fo:table-column, fo:table-caption, fo:table-header, fo:table-footer, fo:table-body, fo:table-row, fo:table-cell, fo:list-block, fo:list-item, fo:basic-link

**border-before-precedence**: fo:table, fo:table-column, fo:table-header, fo:table-footer, fo:table-body, fo:table-row, fo:table-cell

**border-before-style**: fo:region-body, fo:region-before, fo:region-after, fo:region-start, fo:region-end, fo:title, fo:block, fo:block-container, fo:character, fo:initial-property-set, fo:external-graphic, fo:instream-foreign-object, fo:inline, fo:inline-container, fo:leader, fo:page-number, fo:page-number-citation, fo:page-number-citation-last, fo:scaling-value-citation, fo:table-and-caption, fo:table, fo:table-column, fo:table-caption, fo:table-header, fo:table-footer, fo:table-body, fo:table-row, fo:table-cell, fo:list-block, fo:list-item, fo:basic-link

**border-before-width**: fo:region-body, fo:region-before, fo:region-after, fo:region-start, fo:region-end, fo:title, fo:block, fo:block-container, fo:character, fo:initial-property-set, fo:external-graphic, fo:instream-foreign-object, fo:inline, fo:inline-container, fo:leader, fo:page-number, fo:page-number-citation, fo:page-number-citation-last, fo:scaling-value-citation, fo:table-and-caption, fo:table, fo:table-column, fo:table-caption, fo:table-header, fo:table-footer, fo:table-body, fo:table-row, fo:table-cell, fo:list-block, fo:list-item, fo:basic-link

**border-bottom-color**: fo:region-body, fo:region-before, fo:region-after, fo:region-start, fo:region-end, fo:title, fo:block, fo:block-container, fo:character, fo:initial-property-set, fo:external-graphic, fo:instream-foreign-object, fo:inline, fo:inline-container, fo:leader, fo:page-number, fo:page-number-citation, fo:page-number-citation-last, fo:scaling-value-citation, fo:table-and-caption, fo:table, fo:table-column, fo:table-caption, fo:table-header, fo:table-footer, fo:table-body, fo:table-row, fo:table-cell, fo:list-block, fo:list-item, fo:basic-link

**border-bottom-style**: fo:region-body, fo:region-before, fo:region-after, fo:region-start, fo:region-end, fo:title, fo:block, fo:block-container, fo:character, fo:initial-property-set, fo:external-graphic, fo:instream-foreign-object, fo:inline, fo:inline-container, fo:leader, fo:page-number, fo:page-number-citation, fo:page-number-citation-last, fo:scaling-value-citation, fo:table-and-caption, fo:table, fo:table-column, fo:table-caption, fo:table-header, fo:table-footer, fo:table-body, fo:table-row, fo:table-cell, fo:list-block, fo:list-item, fo:basic-link

**border-bottom-width**: fo:region-body, fo:region-before, fo:region-after, fo:region-start, fo:region-end, fo:title, fo:block, fo:block-container, fo:character, fo:initial-property-set, fo:external-graphic, fo:instream-foreign-object, fo:inline, fo:inline-container, fo:leader, fo:page-number, fo:page-number-citation, fo:page-number-citation-last, fo:scaling-value-citation, fo:table-and-caption, fo:table, fo:table-column, fo:table-caption, fo:table-header, fo:table-footer, fo:table-body, fo:table-row, fo:table-cell, fo:list-block, fo:list-item, fo:basic-link

**border-collapse**: fo:table

**border-end-color**: fo:region-body, fo:region-before, fo:region-after, fo:region-start, fo:region-end, fo:title, fo:block, fo:block-container, fo:character, fo:initial-property-set, fo:external-graphic, fo:instream-foreign-object, fo:inline, fo:inline-container, fo:leader, fo:page-number, fo:page-number-citation, fo:page-number-citation-last, fo:scaling-value-citation, fo:table-and-caption, fo:table, fo:table-column, fo:table-caption, fo:table-header, fo:table-footer, fo:table-body, fo:table-row, fo:table-cell, fo:list-block, fo:list-item, fo:basic-link

**border-end-precedence**: fo:table, fo:table-column, fo:table-header, fo:table-footer, fo:table-body, fo:table-row, fo:table-cell

**border-end-style**: fo:region-body, fo:region-before, fo:region-after, fo:region-start, fo:region-end, fo:title, fo:block, fo:block-container, fo:character, fo:initial-property-set, fo:external-graphic, fo:instream-foreign-object, fo:inline, fo:inline-container, fo:leader, fo:page-number, fo:page-number-citation, fo:page-number-citation-last, fo:scaling-value-citation, fo:table-and-caption, fo:table, fo:table-column, fo:table-caption, fo:table-header, fo:table-footer, fo:table-body, fo:table-row, fo:table-cell, fo:list-block, fo:list-item, fo:basic-link

**border-end-width**: fo:region-body, fo:region-before, fo:region-after, fo:region-start, fo:region-end, fo:title, fo:block, fo:block-container, fo:character, fo:initial-property-set, fo:external-graphic, fo:instream-foreign-object, fo:inline, fo:inline-container, fo:leader, fo:page-number, fo:page-number-citation, fo:page-number-citation-last, fo:scaling-value-citation, fo:table-and-caption, fo:table, fo:table-column, fo:table-caption, fo:table-header, fo:table-footer, fo:table-body, fo:table-row, fo:table-cell, fo:list-block, fo:list-item, fo:basic-link

**border-left-color**: fo:region-body, fo:region-before, fo:region-after, fo:region-start, fo:region-end, fo:title, fo:block, fo:block-container, fo:character, fo:initial-property-set, fo:external-graphic, fo:instream-foreign-object, fo:inline, fo:inline-container, fo:leader, fo:page-number, fo:page-number-citation, fo:page-number-citation-last, fo:scaling-value-citation, fo:table-and-caption, fo:table, fo:table-column, fo:table-caption, fo:table-header, fo:table-footer, fo:table-body, fo:table-row, fo:table-cell, fo:list-block, fo:list-item, fo:basic-link

**border-left-style**: fo:region-body, fo:region-before, fo:region-after, fo:region-start, fo:region-end, fo:title, fo:block, fo:block-container, fo:character, fo:initial-property-set, fo:external-graphic, fo:instream-foreign-object, fo:inline, fo:inline-container, fo:leader, fo:page-number, fo:page-number-citation, fo:page-number-citation-last, fo:scaling-value-citation, fo:table-and-caption, fo:table, fo:table-column, fo:table-caption, fo:table-header, fo:table-footer, fo:table-body, fo:table-row, fo:table-cell, fo:list-block, fo:list-item, fo:basic-link

**border-left-width**: fo:region-body, fo:region-before, fo:region-after, fo:region-start, fo:region-end, fo:title, fo:block, fo:block-container, fo:character, fo:initial-property-set, fo:external-graphic, fo:instream-foreign-object, fo:inline, fo:inline-container, fo:leader, fo:page-number, fo:page-number-citation, fo:page-number-citation-last, fo:scaling-value-citation, fo:table-and-caption, fo:table, fo:table-column, fo:table-caption, fo:table-header, fo:table-footer, fo:table-body, fo:table-row, fo:table-cell, fo:list-block, fo:list-item, fo:basic-link

**border-right-color**: fo:region-body, fo:region-before, fo:region-after, fo:region-start, fo:region-end, fo:title, fo:block, fo:block-container, fo:character, fo:initial-property-set, fo:external-graphic, fo:instream-foreign-object, fo:inline, fo:inline-container, fo:leader, fo:page-number, fo:page-number-citation, fo:page-number-citation-last, fo:scaling-value-citation, fo:table-and-caption, fo:table, fo:table-column, fo:table-caption, fo:table-header, fo:table-footer, fo:table-body, fo:table-row, fo:table-cell, fo:list-block, fo:list-item, fo:basic-link

**border-right-style**: fo:region-body, fo:region-before, fo:region-after, fo:region-start, fo:region-end, fo:title, fo:block, fo:block-container, fo:character, fo:initial-property-set, fo:external-graphic, fo:instream-foreign-object, fo:inline, fo:inline-container, fo:leader, fo:page-number, fo:page-number-citation, fo:page-number-citation-last, fo:scaling-value-citation, fo:table-and-caption, fo:table, fo:table-column, fo:table-caption, fo:table-header, fo:table-footer, fo:table-body, fo:table-row, fo:table-cell, fo:list-block, fo:list-item, fo:basic-link

**border-right-width**: fo:region-body, fo:region-before, fo:region-after, fo:region-start, fo:region-end, fo:title, fo:block, fo:block-container, fo:character, fo:initial-property-set, fo:external-graphic, fo:instream-foreign-object, fo:inline, fo:inline-container, fo:leader, fo:page-number, fo:page-number-citation, fo:page-number-citation-last, fo:scaling-value-citation, fo:table-and-caption, fo:table, fo:table-column, fo:table-caption, fo:table-header, fo:table-footer, fo:table-body, fo:table-row, fo:table-cell, fo:list-block, fo:list-item, fo:basic-link

**border-separation**: fo:table

**border-start-color**: fo:region-body, fo:region-before, fo:region-after, fo:region-start, fo:region-end, fo:title, fo:block, fo:block-container, fo:character, fo:initial-property-set, fo:external-graphic, fo:instream-foreign-object, fo:inline, fo:inline-container, fo:leader, fo:page-number, fo:page-number-citation, fo:page-number-citation-last, fo:scaling-value-citation, fo:table-and-caption, fo:table, fo:table-column, fo:table-caption, fo:table-header, fo:table-footer, fo:table-body, fo:table-row, fo:table-cell, fo:list-block, fo:list-item, fo:basic-link

**border-start-precedence**: fo:table, fo:table-column, fo:table-header, fo:table-footer, fo:table-body, fo:table-row, fo:table-cell

**border-start-style**: fo:region-body, fo:region-before, fo:region-after, fo:region-start, fo:region-end, fo:title, fo:block, fo:block-container, fo:character, fo:initial-property-set, fo:external-graphic, fo:instream-foreign-object, fo:inline, fo:inline-container, fo:leader, fo:page-number, fo:page-number-citation, fo:page-number-citation-last, fo:scaling-value-citation, fo:table-and-caption, fo:table, fo:table-column, fo:table-caption, fo:table-header, fo:table-footer, fo:table-body, fo:table-row, fo:table-cell, fo:list-block, fo:list-item, fo:basic-link

**border-start-width**: fo:region-body, fo:region-before, fo:region-after, fo:region-start, fo:region-end, fo:title, fo:block, fo:block-container, fo:character, fo:initial-property-set, fo:external-graphic, fo:instream-foreign-object, fo:inline, fo:inline-container, fo:leader, fo:page-number, fo:page-number-citation, fo:page-number-citation-last, fo:scaling-value-citation, fo:table-and-caption, fo:table, fo:table-column, fo:table-caption, fo:table-header, fo:table-footer, fo:table-body, fo:table-row, fo:table-cell, fo:list-block, fo:list-item, fo:basic-link

**border-top-color**: fo:region-body, fo:region-before, fo:region-after, fo:region-start, fo:region-end, fo:title, fo:block, fo:block-container, fo:character, fo:initial-property-set, fo:external-graphic, fo:instream-foreign-object, fo:inline, fo:inline-container, fo:leader, fo:page-number, fo:page-number-citation, fo:page-number-citation-last, fo:scaling-value-citation, fo:table-and-caption, fo:table, fo:table-column, fo:table-caption, fo:table-header, fo:table-footer, fo:table-body, fo:table-row, fo:table-cell, fo:list-block, fo:list-item, fo:basic-link

**border-top-style**: fo:region-body, fo:region-before, fo:region-after, fo:region-start, fo:region-end, fo:title, fo:block, fo:block-container, fo:character, fo:initial-property-set, fo:external-graphic, fo:instream-foreign-object, fo:inline, fo:inline-container, fo:leader, fo:page-number, fo:page-number-citation, fo:page-number-citation-last, fo:scaling-value-citation, fo:table-and-caption, fo:table, fo:table-column, fo:table-caption, fo:table-header, fo:table-footer, fo:table-body, fo:table-row, fo:table-cell, fo:list-block, fo:list-item, fo:basic-link

**border-top-width**: fo:region-body, fo:region-before, fo:region-after, fo:region-start, fo:region-end, fo:title, fo:block, fo:block-container, fo:character, fo:initial-property-set, fo:external-graphic, fo:instream-foreign-object, fo:inline, fo:inline-container, fo:leader, fo:page-number, fo:page-number-citation, fo:page-number-citation-last, fo:scaling-value-citation, fo:table-and-caption, fo:table, fo:table-column, fo:table-caption, fo:table-header, fo:table-footer, fo:table-body, fo:table-row, fo:table-cell, fo:list-block, fo:list-item, fo:basic-link

**bottom**: fo:block-container, fo:block, fo:bidi-override, fo:character, fo:initial-property-set, fo:external-graphic, fo:instream-foreign-object, fo:inline, fo:inline-container, fo:leader, fo:page-number, fo:page-number-citation, fo:page-number-citation-last, fo:scaling-value-citation, fo:table-and-caption, fo:table, fo:table-caption, fo:table-header, fo:table-footer, fo:table-body, fo:table-row, fo:table-cell, fo:list-block, fo:list-item, fo:basic-link

**break-after**: fo:block, fo:block-container, fo:table-and-caption, fo:table, fo:table-row, fo:list-block, fo:list-item

**break-before**: fo:block, fo:block-container, fo:table-and-caption, fo:table, fo:table-row, fo:list-block, fo:list-item

**caption-side**: fo:table-and-caption

**case-name**: fo:multi-case

**case-title**: fo:multi-case

**change-bar-class**: fo:change-bar-begin, fo:change-bar-end

**change-bar-color**: fo:change-bar-begin

**change-bar-offset**: fo:change-bar-begin

**change-bar-placement**: fo:change-bar-begin

**change-bar-style**: fo:change-bar-begin

**change-bar-width**: fo:change-bar-begin

**character**: fo:character

**clear**: fo:block, fo:block-container, fo:table-and-caption, fo:table, fo:list-block, fo:float

**clip**: fo:region-body, fo:region-before, fo:region-after, fo:region-start, fo:region-end, fo:block-container, fo:external-graphic, fo:instream-foreign-object, fo:inline-container

**color**: fo:title, fo:block, fo:bidi-override, fo:character, fo:initial-property-set, fo:inline, fo:leader, fo:bookmark-title

**color-profile-name**: fo:color-profile

**column-count**: fo:region-body

**column-gap**: fo:region-body

**column-number**: fo:table-column, fo:table-cell

**column-width**: fo:table-column

**content-height**: fo:external-graphic, fo:instream-foreign-object

**content-type**: fo:external-graphic, fo:instream-foreign-object

**content-width**: fo:external-graphic, fo:instream-foreign-object

**country**: fo:block, fo:character

**cue-after**: fo:title, fo:block, fo:bidi-override, fo:character, fo:initial-property-set, fo:external-graphic, fo:instream-foreign-object, fo:inline, fo:leader, fo:page-number, fo:page-number-citation, fo:page-number-citation-last, fo:scaling-value-citation, fo:table-and-caption, fo:table, fo:table-caption, fo:table-header, fo:table-footer, fo:table-body, fo:table-row, fo:table-cell, fo:list-block, fo:list-item, fo:basic-link, fo:change-bar-begin, fo:change-bar-end

**cue-before**: fo:title, fo:block, fo:bidi-override, fo:character, fo:initial-property-set, fo:external-graphic, fo:instream-foreign-object, fo:inline, fo:leader, fo:page-number, fo:page-number-citation, fo:page-number-citation-last, fo:scaling-value-citation, fo:table-and-caption, fo:table, fo:table-caption, fo:table-header, fo:table-footer, fo:table-body, fo:table-row, fo:table-cell, fo:list-block, fo:list-item, fo:basic-link, fo:change-bar-begin, fo:change-bar-end

**destination-placement-offset**: fo:basic-link

**direction**: fo:bidi-override

**display-align**: fo:region-body, fo:region-before, fo:region-after, fo:region-start, fo:region-end, fo:block-container, fo:external-graphic, fo:instream-foreign-object, fo:inline-container, fo:table-cell

**dominant-baseline**: fo:character, fo:external-graphic, fo:instream-foreign-object, fo:inline, fo:inline-container, fo:leader, fo:page-number, fo:page-number-citation, fo:page-number-citation-last, fo:scaling-value-citation, fo:basic-link

**elevation**: fo:title, fo:block, fo:bidi-override, fo:character, fo:initial-property-set, fo:external-graphic, fo:instream-foreign-object, fo:inline, fo:leader, fo:page-number, fo:page-number-citation, fo:page-number-citation-last, fo:scaling-value-citation, fo:table-and-caption, fo:table, fo:table-caption, fo:table-header, fo:table-footer, fo:table-body, fo:table-row, fo:table-cell, fo:list-block, fo:list-item, fo:basic-link, fo:change-bar-begin, fo:change-bar-end

**empty-cells**: fo:table-cell

**end-indent**: fo:simple-page-master, fo:region-body, fo:block, fo:block-container, fo:table-and-caption, fo:table, fo:list-block, fo:list-item

**ends-row**: fo:table-cell

**extent**: fo:region-before, fo:region-after, fo:region-start, fo:region-end

**external-destination**: fo:basic-link, fo:bookmark

**float**: fo:float

**flow-map-name**: fo:flow-map

**flow-map-reference**: fo:page-sequence

**flow-name**: fo:flow, fo:static-content

**flow-name-reference**: fo:flow-name-specifier

**font-family**: fo:title, fo:block, fo:bidi-override, fo:character, fo:initial-property-set, fo:inline, fo:leader, fo:page-number, fo:page-number-citation, fo:page-number-citation-last, fo:scaling-value-citation

**font-selection-strategy**: fo:title, fo:block, fo:bidi-override, fo:character, fo:initial-property-set, fo:inline, fo:leader, fo:page-number, fo:page-number-citation, fo:page-number-citation-last, fo:scaling-value-citation

**font-size**: fo:title, fo:block, fo:bidi-override, fo:character, fo:initial-property-set, fo:inline, fo:leader, fo:page-number, fo:page-number-citation, fo:page-number-citation-last, fo:scaling-value-citation

**font-size-adjust**: fo:title, fo:block, fo:bidi-override, fo:character, fo:initial-property-set, fo:inline, fo:leader, fo:page-number, fo:page-number-citation, fo:page-number-citation-last, fo:scaling-value-citation

**font-stretch**: fo:title, fo:block, fo:bidi-override, fo:character, fo:initial-property-set, fo:inline, fo:leader, fo:page-number, fo:page-number-citation, fo:page-number-citation-last, fo:scaling-value-citation

**font-style**: fo:title, fo:block, fo:bidi-override, fo:character, fo:initial-property-set, fo:inline, fo:leader, fo:page-number, fo:page-number-citation, fo:page-number-citation-last, fo:scaling-value-citation

**font-variant**: fo:title, fo:block, fo:bidi-override, fo:character, fo:initial-property-set, fo:inline, fo:leader, fo:page-number, fo:page-number-citation, fo:page-number-citation-last, fo:scaling-value-citation

**font-weight**: fo:title, fo:block, fo:bidi-override, fo:character, fo:initial-property-set, fo:inline, fo:leader, fo:page-number, fo:page-number-citation, fo:page-number-citation-last, fo:scaling-value-citation

**force-page-count**: fo:page-sequence

**format**: fo:page-sequence, fo:scaling-value-citation

**glyph-orientation-horizontal**: fo:character

**glyph-orientation-vertical**: fo:character

**grouping-separator**: fo:page-sequence, fo:scaling-value-citation

**grouping-size**: fo:page-sequence, fo:scaling-value-citation

**height**: fo:block-container, fo:external-graphic, fo:instream-foreign-object, fo:inline, fo:inline-container, fo:table, fo:table-caption, fo:table-row, fo:table-cell

**hyphenate**: fo:block, fo:character

**hyphenation-character**: fo:block, fo:character

**hyphenation-keep**: fo:block

**hyphenation-ladder-count**: fo:block

**hyphenation-push-character-count**: fo:block, fo:character

**hyphenation-remain-character-count**: fo:block, fo:character

**id**: fo:root, fo:page-sequence, fo:page-sequence-wrapper, fo:flow, fo:static-content, fo:block, fo:block-container, fo:bidi-override, fo:character, fo:external-graphic, fo:instream-foreign-object, fo:inline, fo:inline-container, fo:leader, fo:page-number, fo:page-number-citation, fo:page-number-citation-last, fo:scaling-value-citation, fo:table-and-caption, fo:table, fo:table-caption, fo:table-header, fo:table-footer, fo:table-body, fo:table-row, fo:table-cell, fo:list-block, fo:list-item, fo:list-item-body, fo:list-item-label, fo:basic-link, fo:multi-switch, fo:multi-case, fo:multi-toggle, fo:multi-property-set, fo:index-range-begin, fo:float, fo:footnote, fo:footnote-body, fo:wrapper

**index-class**: fo:root, fo:page-sequence, fo:page-sequence-wrapper, fo:flow, fo:static-content, fo:block, fo:block-container, fo:bidi-override, fo:character, fo:external-graphic, fo:instream-foreign-object, fo:inline, fo:inline-container, fo:leader, fo:page-number, fo:page-number-citation, fo:page-number-citation-last, fo:scaling-value-citation, fo:table-and-caption, fo:table, fo:table-caption, fo:table-header, fo:table-footer, fo:table-body, fo:table-row, fo:table-cell, fo:list-block, fo:list-item, fo:list-item-body, fo:list-item-label, fo:basic-link, fo:multi-switch, fo:multi-case, fo:multi-toggle, fo:multi-property-set, fo:index-range-begin, fo:float, fo:footnote, fo:footnote-body, fo:wrapper

**index-key**: fo:root, fo:page-sequence, fo:page-sequence-wrapper, fo:flow, fo:static-content, fo:block, fo:block-container, fo:bidi-override, fo:character, fo:external-graphic, fo:instream-foreign-object, fo:inline, fo:inline-container, fo:leader, fo:page-number, fo:page-number-citation, fo:page-number-citation-last, fo:scaling-value-citation, fo:table-and-caption, fo:table, fo:table-caption, fo:table-header, fo:table-footer, fo:table-body, fo:table-row, fo:table-cell, fo:list-block, fo:list-item, fo:list-item-body, fo:list-item-label, fo:basic-link, fo:multi-switch, fo:multi-case, fo:multi-toggle, fo:multi-property-set, fo:index-range-begin, fo:float, fo:footnote, fo:footnote-body, fo:wrapper

**indicate-destination**: fo:basic-link

**initial-page-number**: fo:page-sequence

**inline-progression-dimension**: fo:block-container, fo:external-graphic, fo:instream-foreign-object, fo:inline, fo:inline-container, fo:table, fo:table-caption, fo:table-cell

**internal-destination**: fo:basic-link, fo:bookmark

**intrinsic-scale-value**: fo:scaling-value-citation

**intrusion-displace**: fo:block, fo:block-container, fo:table-and-caption, fo:table, fo:table-caption, fo:list-block, fo:list-item

**keep-together**: fo:block, fo:block-container, fo:inline, fo:inline-container, fo:table-and-caption, fo:table, fo:table-caption, fo:table-row, fo:list-block, fo:list-item, fo:list-item-body, fo:list-item-label, fo:basic-link

**keep-with-next**: fo:block, fo:block-container, fo:character, fo:external-graphic, fo:instream-foreign-object, fo:inline, fo:inline-container, fo:leader, fo:page-number, fo:page-number-citation, fo:page-number-citation-last, fo:scaling-value-citation, fo:table-and-caption, fo:table, fo:table-row, fo:list-block, fo:list-item, fo:basic-link

**keep-with-previous**: fo:block, fo:block-container, fo:character, fo:external-graphic, fo:instream-foreign-object, fo:inline, fo:inline-container, fo:leader, fo:page-number, fo:page-number-citation, fo:page-number-citation-last, fo:scaling-value-citation, fo:table-and-caption, fo:table, fo:table-row, fo:list-block, fo:list-item, fo:basic-link

**language**: fo:block, fo:character

**last-line-end-indent**: fo:block

**leader-alignment**: fo:leader

**leader-length**: fo:leader

**leader-pattern**: fo:leader

**leader-pattern-width**: fo:leader

**left**: fo:block-container, fo:block, fo:bidi-override, fo:character, fo:initial-property-set, fo:external-graphic, fo:instream-foreign-object, fo:inline, fo:inline-container, fo:leader, fo:page-number, fo:page-number-citation, fo:page-number-citation-last, fo:scaling-value-citation, fo:table-and-caption, fo:table, fo:table-caption, fo:table-header, fo:table-footer, fo:table-body, fo:table-row, fo:table-cell, fo:list-block, fo:list-item, fo:basic-link

**letter-spacing**: fo:bidi-override, fo:character, fo:initial-property-set, fo:leader, fo:page-number, fo:page-number-citation, fo:page-number-citation-last, fo:scaling-value-citation

**letter-value**: fo:page-sequence, fo:scaling-value-citation

**line-height**: fo:title, fo:block, fo:bidi-override, fo:character, fo:initial-property-set, fo:external-graphic, fo:instream-foreign-object, fo:inline, fo:inline-container, fo:leader, fo:page-number, fo:page-number-citation, fo:page-number-citation-last, fo:scaling-value-citation, fo:basic-link

**line-height-shift-adjustment**: fo:block

**line-stacking-strategy**: fo:block

**linefeed-treatment**: fo:block

**margin-bottom**: fo:simple-page-master, fo:region-body, fo:block, fo:block-container, fo:table-and-caption, fo:table, fo:list-block, fo:list-item, fo:title, fo:character, fo:external-graphic, fo:instream-foreign-object, fo:inline, fo:inline-container, fo:leader, fo:page-number, fo:page-number-citation, fo:page-number-citation-last, fo:scaling-value-citation, fo:basic-link

**margin-left**: fo:simple-page-master, fo:region-body, fo:block, fo:block-container, fo:table-and-caption, fo:table, fo:list-block, fo:list-item, fo:title, fo:character, fo:external-graphic, fo:instream-foreign-object, fo:inline, fo:inline-container, fo:leader, fo:page-number, fo:page-number-citation, fo:page-number-citation-last, fo:scaling-value-citation, fo:basic-link

**margin-right**: fo:simple-page-master, fo:region-body, fo:block, fo:block-container, fo:table-and-caption, fo:table, fo:list-block, fo:list-item, fo:title, fo:character, fo:external-graphic, fo:instream-foreign-object, fo:inline, fo:inline-container, fo:leader, fo:page-number, fo:page-number-citation, fo:page-number-citation-last, fo:scaling-value-citation, fo:basic-link

**margin-top**: fo:simple-page-master, fo:region-body, fo:block, fo:block-container, fo:table-and-caption, fo:table, fo:list-block, fo:list-item, fo:title, fo:character, fo:external-graphic, fo:instream-foreign-object, fo:inline, fo:inline-container, fo:leader, fo:page-number, fo:page-number-citation, fo:page-number-citation-last, fo:scaling-value-citation, fo:basic-link

**marker-class-name**: fo:marker

**master-name**: fo:page-sequence-master, fo:simple-page-master

**master-reference**: fo:page-sequence, fo:single-page-master-reference, fo:repeatable-page-master-reference, fo:conditional-page-master-reference

**maximum-repeats**: fo:repeatable-page-master-reference, fo:repeatable-page-master-alternatives

**media-usage**: fo:root

**merge-pages-across-index-key-references**: fo:index-page-citation-list

**merge-ranges-across-index-key-references**: fo:index-page-citation-list

**merge-sequential-page-numbers**: fo:index-page-citation-list

**number-columns-repeated**: fo:table-column

**number-columns-spanned**: fo:table-column, fo:table-cell

**number-rows-spanned**: fo:table-cell

**odd-or-even**: fo:conditional-page-master-reference

**orphans**: fo:block

**overflow**: fo:region-body, fo:region-before, fo:region-after, fo:region-start, fo:region-end, fo:block-container, fo:external-graphic, fo:instream-foreign-object, fo:inline-container

**padding-after**: fo:region-body, fo:region-before, fo:region-after, fo:region-start, fo:region-end, fo:title, fo:block, fo:block-container, fo:character, fo:initial-property-set, fo:external-graphic, fo:instream-foreign-object, fo:inline, fo:inline-container, fo:leader, fo:page-number, fo:page-number-citation, fo:page-number-citation-last, fo:scaling-value-citation, fo:table-and-caption, fo:table, fo:table-caption, fo:table-cell, fo:list-block, fo:list-item, fo:basic-link

**padding-before**: fo:region-body, fo:region-before, fo:region-after, fo:region-start, fo:region-end, fo:title, fo:block, fo:block-container, fo:character, fo:initial-property-set, fo:external-graphic, fo:instream-foreign-object, fo:inline, fo:inline-container, fo:leader, fo:page-number, fo:page-number-citation, fo:page-number-citation-last, fo:scaling-value-citation, fo:table-and-caption, fo:table, fo:table-caption, fo:table-cell, fo:list-block, fo:list-item, fo:basic-link

**padding-bottom**: fo:region-body, fo:region-before, fo:region-after, fo:region-start, fo:region-end, fo:title, fo:block, fo:block-container, fo:character, fo:initial-property-set, fo:external-graphic, fo:instream-foreign-object, fo:inline, fo:inline-container, fo:leader, fo:page-number, fo:page-number-citation, fo:page-number-citation-last, fo:scaling-value-citation, fo:table-and-caption, fo:table, fo:table-caption, fo:table-cell, fo:list-block, fo:list-item, fo:basic-link

**padding-end**: fo:region-body, fo:region-before, fo:region-after, fo:region-start, fo:region-end, fo:title, fo:block, fo:block-container, fo:character, fo:initial-property-set, fo:external-graphic, fo:instream-foreign-object, fo:inline, fo:inline-container, fo:leader, fo:page-number, fo:page-number-citation, fo:page-number-citation-last, fo:scaling-value-citation, fo:table-and-caption, fo:table, fo:table-caption, fo:table-cell, fo:list-block, fo:list-item, fo:basic-link

**padding-left**: fo:region-body, fo:region-before, fo:region-after, fo:region-start, fo:region-end, fo:title, fo:block, fo:block-container, fo:character, fo:initial-property-set, fo:external-graphic, fo:instream-foreign-object, fo:inline, fo:inline-container, fo:leader, fo:page-number, fo:page-number-citation, fo:page-number-citation-last, fo:scaling-value-citation, fo:table-and-caption, fo:table, fo:table-caption, fo:table-cell, fo:list-block, fo:list-item, fo:basic-link

**padding-right**: fo:region-body, fo:region-before, fo:region-after, fo:region-start, fo:region-end, fo:title, fo:block, fo:block-container, fo:character, fo:initial-property-set, fo:external-graphic, fo:instream-foreign-object, fo:inline, fo:inline-container, fo:leader, fo:page-number, fo:page-number-citation, fo:page-number-citation-last, fo:scaling-value-citation, fo:table-and-caption, fo:table, fo:table-caption, fo:table-cell, fo:list-block, fo:list-item, fo:basic-link

**padding-start**: fo:region-body, fo:region-before, fo:region-after, fo:region-start, fo:region-end, fo:title, fo:block, fo:block-container, fo:character, fo:initial-property-set, fo:external-graphic, fo:instream-foreign-object, fo:inline, fo:inline-container, fo:leader, fo:page-number, fo:page-number-citation, fo:page-number-citation-last, fo:scaling-value-citation, fo:table-and-caption, fo:table, fo:table-caption, fo:table-cell, fo:list-block, fo:list-item, fo:basic-link

**padding-top**: fo:region-body, fo:region-before, fo:region-after, fo:region-start, fo:region-end, fo:title, fo:block, fo:block-container, fo:character, fo:initial-property-set, fo:external-graphic, fo:instream-foreign-object, fo:inline, fo:inline-container, fo:leader, fo:page-number, fo:page-number-citation, fo:page-number-citation-last, fo:scaling-value-citation, fo:table-and-caption, fo:table, fo:table-caption, fo:table-cell, fo:list-block, fo:list-item, fo:basic-link

**page-citation-strategy**: fo:page-number-citation-last

**page-height**: fo:simple-page-master

**page-number-treatment**: fo:index-key-reference

**page-position**: fo:conditional-page-master-reference

**page-width**: fo:simple-page-master

**pause-after**: fo:title, fo:block, fo:bidi-override, fo:character, fo:initial-property-set, fo:external-graphic, fo:instream-foreign-object, fo:inline, fo:leader, fo:page-number, fo:page-number-citation, fo:page-number-citation-last, fo:scaling-value-citation, fo:table-and-caption, fo:table, fo:table-caption, fo:table-header, fo:table-footer, fo:table-body, fo:table-row, fo:table-cell, fo:list-block, fo:list-item, fo:basic-link, fo:change-bar-begin, fo:change-bar-end

**pause-before**: fo:title, fo:block, fo:bidi-override, fo:character, fo:initial-property-set, fo:external-graphic, fo:instream-foreign-object, fo:inline, fo:leader, fo:page-number, fo:page-number-citation, fo:page-number-citation-last, fo:scaling-value-citation, fo:table-and-caption, fo:table, fo:table-caption, fo:table-header, fo:table-footer, fo:table-body, fo:table-row, fo:table-cell, fo:list-block, fo:list-item, fo:basic-link, fo:change-bar-begin, fo:change-bar-end

**pitch**: fo:title, fo:block, fo:bidi-override, fo:character, fo:initial-property-set, fo:external-graphic, fo:instream-foreign-object, fo:inline, fo:leader, fo:page-number, fo:page-number-citation, fo:page-number-citation-last, fo:scaling-value-citation, fo:table-and-caption, fo:table, fo:table-caption, fo:table-header, fo:table-footer, fo:table-body, fo:table-row, fo:table-cell, fo:list-block, fo:list-item, fo:basic-link, fo:change-bar-begin, fo:change-bar-end

**pitch-range**: fo:title, fo:block, fo:bidi-override, fo:character, fo:initial-property-set, fo:external-graphic, fo:instream-foreign-object, fo:inline, fo:leader, fo:page-number, fo:page-number-citation, fo:page-number-citation-last, fo:scaling-value-citation, fo:table-and-caption, fo:table, fo:table-caption, fo:table-header, fo:table-footer, fo:table-body, fo:table-row, fo:table-cell, fo:list-block, fo:list-item, fo:basic-link, fo:change-bar-begin, fo:change-bar-end

**play-during**: fo:title, fo:block, fo:bidi-override, fo:character, fo:initial-property-set, fo:external-graphic, fo:instream-foreign-object, fo:inline, fo:leader, fo:page-number, fo:page-number-citation, fo:page-number-citation-last, fo:scaling-value-citation, fo:table-and-caption, fo:table, fo:table-caption, fo:table-header, fo:table-footer, fo:table-body, fo:table-row, fo:table-cell, fo:list-block, fo:list-item, fo:basic-link, fo:change-bar-begin, fo:change-bar-end

**precedence**: fo:region-before, fo:region-after

**provisional-distance-between-starts**: fo:list-block

**provisional-label-separation**: fo:list-block

**ref-id**: fo:page-number-citation, fo:page-number-citation-last, fo:scaling-value-citation, fo:index-range-end

**ref-index-key**: fo:index-key-reference

**reference-orientation**: fo:page-sequence, fo:simple-page-master, fo:region-body, fo:region-before, fo:region-after, fo:region-start, fo:region-end, fo:block-container, fo:inline-container

**region-name**: fo:region-body, fo:region-before, fo:region-after, fo:region-start, fo:region-end

**region-name-reference**: fo:region-name-specifier

**relative-align**: fo:table-cell, fo:list-item

**relative-position**: fo:block, fo:bidi-override, fo:character, fo:initial-property-set, fo:external-graphic, fo:instream-foreign-object, fo:inline, fo:inline-container, fo:leader, fo:page-number, fo:page-number-citation, fo:page-number-citation-last, fo:scaling-value-citation, fo:table-and-caption, fo:table, fo:table-caption, fo:table-header, fo:table-footer, fo:table-body, fo:table-row, fo:table-cell, fo:list-block, fo:list-item, fo:basic-link

**rendering-intent**: fo:color-profile

**retrieve-boundary**: fo:retrieve-marker

**retrieve-boundary-within-table**: fo:retrieve-table-marker

**retrieve-class-name**: fo:retrieve-marker, fo:retrieve-table-marker

**retrieve-position**: fo:retrieve-marker

**retrieve-position-within-table**: fo:retrieve-table-marker

**richness**: fo:title, fo:block, fo:bidi-override, fo:character, fo:initial-property-set, fo:external-graphic, fo:instream-foreign-object, fo:inline, fo:leader, fo:page-number, fo:page-number-citation, fo:page-number-citation-last, fo:scaling-value-citation, fo:table-and-caption, fo:table, fo:table-caption, fo:table-header, fo:table-footer, fo:table-body, fo:table-row, fo:table-cell, fo:list-block, fo:list-item, fo:basic-link, fo:change-bar-begin, fo:change-bar-end

**right**: fo:block-container, fo:block, fo:bidi-override, fo:character, fo:initial-property-set, fo:external-graphic, fo:instream-foreign-object, fo:inline, fo:inline-container, fo:leader, fo:page-number, fo:page-number-citation, fo:page-number-citation-last, fo:scaling-value-citation, fo:table-and-caption, fo:table, fo:table-caption, fo:table-header, fo:table-footer, fo:table-body, fo:table-row, fo:table-cell, fo:list-block, fo:list-item, fo:basic-link

**role**: fo:root, fo:title, fo:block, fo:initial-property-set, fo:external-graphic, fo:instream-foreign-object, fo:inline, fo:leader, fo:page-number, fo:page-number-citation, fo:page-number-citation-last, fo:scaling-value-citation, fo:table-and-caption, fo:table, fo:table-caption, fo:table-header, fo:table-footer, fo:table-body, fo:table-row, fo:table-cell, fo:list-block, fo:list-item, fo:list-item-body, fo:list-item-label, fo:basic-link, fo:multi-switch, fo:multi-case, fo:multi-toggle, fo:multi-properties, fo:bookmark, fo:bookmark-title, fo:footnote, fo:footnote-body, fo:change-bar-begin, fo:change-bar-end

**rule-style**: fo:leader

**rule-thickness**: fo:leader

**scale-option**: fo:scaling-value-citation

**scaling**: fo:external-graphic, fo:instream-foreign-object

**scaling-method**: fo:external-graphic, fo:instream-foreign-object

**score-spaces**: fo:bidi-override, fo:character, fo:initial-property-set, fo:page-number, fo:page-number-citation, fo:page-number-citation-last, fo:scaling-value-citation

**script**: fo:block, fo:character

**show-destination**: fo:basic-link

**source-document**: fo:root, fo:title, fo:block, fo:initial-property-set, fo:external-graphic, fo:instream-foreign-object, fo:inline, fo:leader, fo:page-number, fo:page-number-citation, fo:page-number-citation-last, fo:scaling-value-citation, fo:table-and-caption, fo:table, fo:table-caption, fo:table-header, fo:table-footer, fo:table-body, fo:table-row, fo:table-cell, fo:list-block, fo:list-item, fo:list-item-body, fo:list-item-label, fo:basic-link, fo:multi-switch, fo:multi-case, fo:multi-toggle, fo:multi-properties, fo:bookmark, fo:bookmark-title, fo:footnote, fo:footnote-body, fo:change-bar-begin, fo:change-bar-end

**space-after**: fo:simple-page-master, fo:region-body, fo:block, fo:block-container, fo:table-and-caption, fo:table, fo:list-block, fo:list-item

**space-before**: fo:simple-page-master, fo:region-body, fo:block, fo:block-container, fo:table-and-caption, fo:table, fo:list-block, fo:list-item

**space-end**: fo:title, fo:character, fo:external-graphic, fo:instream-foreign-object, fo:inline, fo:inline-container, fo:leader, fo:page-number, fo:page-number-citation, fo:page-number-citation-last, fo:scaling-value-citation, fo:basic-link

**space-start**: fo:title, fo:character, fo:external-graphic, fo:instream-foreign-object, fo:inline, fo:inline-container, fo:leader, fo:page-number, fo:page-number-citation, fo:page-number-citation-last, fo:scaling-value-citation, fo:basic-link

**span**: fo:block, fo:block-container

**speak**: fo:title, fo:block, fo:bidi-override, fo:character, fo:initial-property-set, fo:external-graphic, fo:instream-foreign-object, fo:inline, fo:leader, fo:page-number, fo:page-number-citation, fo:page-number-citation-last, fo:scaling-value-citation, fo:table-and-caption, fo:table, fo:table-caption, fo:table-header, fo:table-footer, fo:table-body, fo:table-row, fo:table-cell, fo:list-block, fo:list-item, fo:basic-link, fo:change-bar-begin, fo:change-bar-end

**speak-header**: fo:title, fo:block, fo:bidi-override, fo:character, fo:initial-property-set, fo:external-graphic, fo:instream-foreign-object, fo:inline, fo:leader, fo:page-number, fo:page-number-citation, fo:page-number-citation-last, fo:scaling-value-citation, fo:table-and-caption, fo:table, fo:table-caption, fo:table-header, fo:table-footer, fo:table-body, fo:table-row, fo:table-cell, fo:list-block, fo:list-item, fo:basic-link, fo:change-bar-begin, fo:change-bar-end

**speak-numeral**: fo:title, fo:block, fo:bidi-override, fo:character, fo:initial-property-set, fo:external-graphic, fo:instream-foreign-object, fo:inline, fo:leader, fo:page-number, fo:page-number-citation, fo:page-number-citation-last, fo:scaling-value-citation, fo:table-and-caption, fo:table, fo:table-caption, fo:table-header, fo:table-footer, fo:table-body, fo:table-row, fo:table-cell, fo:list-block, fo:list-item, fo:basic-link, fo:change-bar-begin, fo:change-bar-end

**speak-punctuation**: fo:title, fo:block, fo:bidi-override, fo:character, fo:initial-property-set, fo:external-graphic, fo:instream-foreign-object, fo:inline, fo:leader, fo:page-number, fo:page-number-citation, fo:page-number-citation-last, fo:scaling-value-citation, fo:table-and-caption, fo:table, fo:table-caption, fo:table-header, fo:table-footer, fo:table-body, fo:table-row, fo:table-cell, fo:list-block, fo:list-item, fo:basic-link, fo:change-bar-begin, fo:change-bar-end

**speech-rate**: fo:title, fo:block, fo:bidi-override, fo:character, fo:initial-property-set, fo:external-graphic, fo:instream-foreign-object, fo:inline, fo:leader, fo:page-number, fo:page-number-citation, fo:page-number-citation-last, fo:scaling-value-citation, fo:table-and-caption, fo:table, fo:table-caption, fo:table-header, fo:table-footer, fo:table-body, fo:table-row, fo:table-cell, fo:list-block, fo:list-item, fo:basic-link, fo:change-bar-begin, fo:change-bar-end

**src**: fo:color-profile, fo:external-graphic

**start-indent**: fo:simple-page-master, fo:region-body, fo:block, fo:block-container, fo:table-and-caption, fo:table, fo:list-block, fo:list-item

**starting-state**: fo:multi-case, fo:bookmark

**starts-row**: fo:table-cell

**stress**: fo:title, fo:block, fo:bidi-override, fo:character, fo:initial-property-set, fo:external-graphic, fo:instream-foreign-object, fo:inline, fo:leader, fo:page-number, fo:page-number-citation, fo:page-number-citation-last, fo:scaling-value-citation, fo:table-and-caption, fo:table, fo:table-caption, fo:table-header, fo:table-footer, fo:table-body, fo:table-row, fo:table-cell, fo:list-block, fo:list-item, fo:basic-link, fo:change-bar-begin, fo:change-bar-end

**suppress-at-line-break**: fo:character

**switch-to**: fo:multi-toggle

**table-layout**: fo:table

**table-omit-footer-at-break**: fo:table

**table-omit-header-at-break**: fo:table

**target-presentation-context**: fo:basic-link

**target-processing-context**: fo:basic-link

**target-stylesheet**: fo:basic-link

**text-align**: fo:block, fo:external-graphic, fo:instream-foreign-object, fo:table-and-caption

**text-align-last**: fo:block

**text-altitude**: fo:block, fo:character, fo:leader, fo:page-number, fo:page-number-citation, fo:page-number-citation-last, fo:scaling-value-citation

**text-decoration**: fo:character, fo:initial-property-set, fo:inline, fo:page-number, fo:page-number-citation, fo:page-number-citation-last, fo:scaling-value-citation

**text-depth**: fo:block, fo:character, fo:leader, fo:page-number, fo:page-number-citation, fo:page-number-citation-last, fo:scaling-value-citation

**text-indent**: fo:block

**text-shadow**: fo:character, fo:initial-property-set, fo:leader, fo:page-number, fo:page-number-citation, fo:page-number-citation-last, fo:scaling-value-citation

**text-transform**: fo:character, fo:initial-property-set, fo:page-number, fo:page-number-citation, fo:page-number-citation-last, fo:scaling-value-citation

**top**: fo:block-container, fo:block, fo:bidi-override, fo:character, fo:initial-property-set, fo:external-graphic, fo:instream-foreign-object, fo:inline, fo:inline-container, fo:leader, fo:page-number, fo:page-number-citation, fo:page-number-citation-last, fo:scaling-value-citation, fo:table-and-caption, fo:table, fo:table-caption, fo:table-header, fo:table-footer, fo:table-body, fo:table-row, fo:table-cell, fo:list-block, fo:list-item, fo:basic-link

**treat-as-word-space**: fo:character

**unicode-bidi**: fo:bidi-override

**visibility**: fo:title, fo:block, fo:character, fo:inline, fo:leader, fo:page-number, fo:page-number-citation, fo:page-number-citation-last, fo:scaling-value-citation, fo:table-column, fo:table-header, fo:table-footer, fo:table-body, fo:table-row

**voice-family**: fo:title, fo:block, fo:bidi-override, fo:character, fo:initial-property-set, fo:external-graphic, fo:instream-foreign-object, fo:inline, fo:leader, fo:page-number, fo:page-number-citation, fo:page-number-citation-last, fo:scaling-value-citation, fo:table-and-caption, fo:table, fo:table-caption, fo:table-header, fo:table-footer, fo:table-body, fo:table-row, fo:table-cell, fo:list-block, fo:list-item, fo:basic-link, fo:change-bar-begin, fo:change-bar-end

**volume**: fo:title, fo:block, fo:bidi-override, fo:character, fo:initial-property-set, fo:external-graphic, fo:instream-foreign-object, fo:inline, fo:leader, fo:page-number, fo:page-number-citation, fo:page-number-citation-last, fo:scaling-value-citation, fo:table-and-caption, fo:table, fo:table-caption, fo:table-header, fo:table-footer, fo:table-body, fo:table-row, fo:table-cell, fo:list-block, fo:list-item, fo:basic-link, fo:change-bar-begin, fo:change-bar-end

**white-space-collapse**: fo:block

**white-space-treatment**: fo:block

**widows**: fo:block

**width**: fo:block-container, fo:external-graphic, fo:instream-foreign-object, fo:inline, fo:inline-container, fo:table, fo:table-caption, fo:table-cell

**word-spacing**: fo:bidi-override, fo:character, fo:initial-property-set, fo:leader, fo:page-number, fo:page-number-citation, fo:page-number-citation-last, fo:scaling-value-citation

**wrap-option**: fo:block, fo:inline, fo:page-number, fo:page-number-citation, fo:page-number-citation-last, fo:scaling-value-citation

**writing-mode**: fo:page-sequence, fo:simple-page-master, fo:region-body, fo:region-before, fo:region-after, fo:region-start, fo:region-end, fo:block-container, fo:inline-container, fo:table

**z-index**: fo:block-container, fo:change-bar-begin

## Code Samples

No code samples in spec for this section.

## See Also

- [W3C XSL-FO 2.0 Property Summary](https://www.w3.org/TR/xslfo20/#property-index)
- properties-common-accessibility.md -- Common Accessibility Properties
- properties-common-aural.md -- Common Aural Properties
- properties-common-border-padding-background.md -- Common Border, Padding, and Background Properties
- properties-common-font.md -- Common Font Properties
- properties-common-margin.md -- Common Margin Properties
- properties-keeps-and-breaks.md -- Keeps and Breaks Properties
- properties-writing-mode.md -- Writing Mode Properties
- properties-table.md -- Table Properties
- properties-list.md -- List Properties
