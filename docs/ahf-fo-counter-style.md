# axf:counter-style

## Summary

With AH XSL Formatter, a unique counter style can be defined using the `axf:counter-style` extension formatting object. This object does not generate an area.

<!-- Source: XSL-FO-Reference-74-MID.pdf p.295 -->

## Properties

| Property | Description |
|---|---|
| `name` | The name of the counter style being defined |
| `system` | The counter system algorithm to use |
| `negative` | Symbols to wrap around negative counter representations |
| `prefix` | A symbol prepended to the counter representation |
| `suffix` | A symbol appended to the counter representation |
| `range` | The range of counter values for which the style is defined |
| `pad` | Minimum width and padding symbol for the counter representation |
| `fallback` | The fallback counter style to use when the defined style cannot represent a value |
| `symbols` | The symbols used by the counter system |
| `additive-symbols` | The symbols and their additive weights for additive counter systems |

All properties listed above are AHF counter-style-specific extension properties.

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
  <axf:counter-style name="my-lower-alpha"
                     system="alphabetic"
                     symbols="a b c d e f g h i j k l m n o p q r s t u v w x y z"
                     suffix=") "/>
</fo:declarations>
```
