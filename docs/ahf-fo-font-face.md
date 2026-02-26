# axf:font-face

## Summary

In AH XSL Formatter, it is possible to add fonts you want to use in the document using the `axf:font-face` extension formatting object. This object specifies an additional font. This object does not generate an area.

<!-- Source: XSL-FO-Reference-74-MID.pdf p.297 -->

## Properties

| Property | Description |
|---|---|
| `src` | The source URI of the font file |
| `font-family` | The font family name to assign to this font |
| `font-style` | The font style (e.g., normal, italic) |
| `font-weight` | The font weight (e.g., normal, bold) |
| `font-stretch` | The font stretch value |
| `unicode-range` | The range of Unicode characters covered by this font |
| `size-adjust` | Adjustment factor for font size |

## Parent Objects

- `fo:declarations`

## Child Objects

None. This is an empty formatting object.

## Code Samples

No code sample provided in the Antenna House reference for this formatting object.

The following is a constructed example (not from the reference):

<!-- Constructed example — not from reference material -->
```xml
<fo:declarations>
  <axf:font-face src="url('file:///C:/fonts/MyCustomFont-Regular.ttf')"
                 font-family="MyCustomFont"
                 font-weight="normal"
                 font-style="normal"/>
  <axf:font-face src="url('file:///C:/fonts/MyCustomFont-Bold.ttf')"
                 font-family="MyCustomFont"
                 font-weight="bold"
                 font-style="normal"/>
</fo:declarations>
```
