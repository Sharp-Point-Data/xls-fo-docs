# fo:number

## Summary

The fo:number formatting object creates a number sequence to be processed by the XSL-FO processor and generate a list of sequences in various areas in the XSL-FO area tree. This flow object does not generate an area itself.

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_number -->

## Content Model

Empty.

## Properties

| Property | Inherited | Conformance Level |
|----------|-----------|-------------------|
| reference-name | No | Extended |
| number-area-extent | No | Extended |
| level | No | Extended |
| reset-level | No | Extended |
| initial-value | No | Extended |
| interval | No | Extended |
| reset-value | No | Extended |
| display-when | No | Extended |
| display-position | No | Extended |
| number-align | No | Extended |
| text-align | Yes | Extended |
| text-decoration | No | Extended |
| font-family | Yes | Extended |
| font-size | Yes | Extended |
| font-style | Yes | Extended |
| font-weight | Yes | Extended |
| color | Yes | Extended |
| background-color | No | Extended |
| format | No | Extended |
| decimal-format | No | Extended |
| letter-value | No | Extended |
| ordinal | No | Extended |
| country | Yes | Extended |
| language | Yes | Extended |
| grouping-separator | No | Extended |
| grouping-size | No | Extended |

## Usage Notes

- fo:number defines a numbering sequence that can be referenced by fo:retrieve-number to display the current counter value at any point in the document.
- The level property controls the scope of the number sequence: "line", "footnote", "column", or "none".
- The reset-level property controls when the counter resets: "block", "block-container", "column", or "page".
- The initial-value property sets the starting value for the counter sequence.
- The interval property controls the increment between consecutive number values.
- The reset-value property specifies the value to which the counter resets.
- The display-when property is an expression that controls conditional display of the number.
- The display-position property specifies where the number appears relative to the content: "start", "end", "before", or "after".
- The number-align property controls the alignment of the number within its allocated area: "start", "end", "center", or "decimal".
- The number-area-extent property specifies the width allocated for displaying the number.
- fo:number does not generate any area itself; it establishes a counter that is rendered via fo:retrieve-number.

## Code Samples

No code samples in spec for this formatting object.

## See Also

- [fo:retrieve-number](fo-retrieve-number.md) — retrieves and displays the current value of an fo:number sequence
- [fo:page-number](fo-page-number.md) — for displaying the current page number (different mechanism)
