# Numbering

## Overview

XSL-FO 2.0 provides support for numbering that is aligned to formatting objects rather than document structure. This includes line numbers, column numbers, and region numbers, with features such as numbering only every Nth line. This numbering capability is distinct from the structural numbering available in XSLT, though it has similar features.

<!-- Source: https://www.w3.org/TR/xslfo20/#numbering -->

## Numbering Formatting Objects

The following formatting objects are provided for numbering. The `letter-value` property also applies.

### fo:number

`fo:number` creates a number sequence to be processed by the XSL-FO processor and generates a list of sequences in various areas in the XSL-FO area tree.

### fo:retrieve-number

`fo:retrieve-number` retrieves the current value of an `fo:number` sequence corresponding to the context where the `fo:retrieve-number` is located. By default, the output number format is the format set by the original `fo:number` properties. Alternatively, `fo:retrieve-number` can set its own properties to override the original `fo:number` property setting.

### decimal-format

The `decimal-format` property defines a decimal format that could be used by either `fo:number` or `fo:retrieve-number`.

## Code Samples

No code samples in spec for this section.

## See Also

- [properties-numbering.md](properties-numbering.md) -- Numbering-related properties
- [properties-number-string.md](properties-number-string.md) -- Number-to-string conversion properties
