# fo:retrieve-number

## Summary

The fo:retrieve-number formatting object retrieves the current value of an fo:number sequence corresponding to the context where the fo:retrieve-number resides. By default the output number format is the format set by the original fo:number properties. Alternatively, fo:retrieve-number can use its own properties to override the original fo:number property settings. It generates and returns a normal inline-level area.

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_retrieve-number -->

## Content Model

`EMPTY`

## Properties

| Property | Inherited | Conformance Level |
|----------|-----------|-------------------|
| reference-name | No | Extended |
| reference-value | No | Extended |
| format | No | Extended |
| decimal-format | No | Extended |
| letter-value | No | Extended |
| ordinal | No | Extended |
| country | Yes | Extended |
| language | Yes | Extended |
| grouping-separator | No | Extended |
| grouping-size | No | Extended |

## Usage Notes

- fo:retrieve-number is used in conjunction with fo:number. The fo:number defines a numbering sequence, and fo:retrieve-number retrieves and displays the current value of that sequence at the point where it appears.
- The reference-name property links the fo:retrieve-number to a specific fo:number sequence by matching the reference-name values.
- The number formatting properties (format, decimal-format, letter-value, ordinal, country, language, grouping-separator, grouping-size) on fo:retrieve-number can override the corresponding properties on the referenced fo:number.
- If the override properties are not specified on fo:retrieve-number, the values from the original fo:number are used.

## Code Samples

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_retrieve-number -->
```xml
EMPTY
```

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_retrieve-number -->
```xml
<fo:retrieve-number
  reference-name = string
  reference-value = [ expression ]
  format = [ string ]
  decimal-format = [ QName ]
  letter-value = [ "auto" | "alphabetic" | "traditional" | <implementater extension> ]
  ordinal = [ string ]
  country = [ "none" | country | "inherit" ]
  language = [ "none" | language | "inherit" ]
  grouping-separator = [ char ]
  grouping-size = [ number ]
/>
```

## See Also

- [fo:number](fo-number.md) — defines the numbering sequence that fo:retrieve-number references
- [fo:page-number](fo-page-number.md) — another inline-level formatting object that generates number content
