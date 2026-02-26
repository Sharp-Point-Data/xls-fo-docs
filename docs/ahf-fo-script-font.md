# axf:script-font

## Summary

Specifies the generic font according to the script. This element does not generate an area. The same setting of script-font in the Option Setting File can be specified. The specification of `axf:script-font` will be adopted in preference to the setting in the Option Setting File.

## Constraints

<!-- Source: XSL-FO-Reference-74-MID.pdf p.305 -->
```xml
<!ELEMENT axf:script-font EMPTY>
<!ATTLIST axf:script-font script CDATA #REQUIRED>
<!ATTLIST axf:script-font serif CDATA #IMPLIED>
<!ATTLIST axf:script-font sans-serif CDATA #IMPLIED>
<!ATTLIST axf:script-font monospace CDATA #IMPLIED>
<!ATTLIST axf:script-font cursive CDATA #IMPLIED>
<!ATTLIST axf:script-font fantasy CDATA #IMPLIED>
<!ATTLIST axf:script-font fallback CDATA #IMPLIED>
```

## Properties

| Attribute | Description | Required |
|-----------|-------------|----------|
| `script` | The script identifier (e.g., `"Latn"`, `"Jpan"`, `"Arab"`) | Required |
| `serif` | Font family name for the serif generic font for this script | Optional |
| `sans-serif` | Font family name for the sans-serif generic font for this script | Optional |
| `monospace` | Font family name for the monospace generic font for this script | Optional |
| `cursive` | Font family name for the cursive generic font for this script | Optional |
| `fantasy` | Font family name for the fantasy generic font for this script | Optional |
| `fallback` | Font family name for the fallback font for this script | Optional |

## Parent Objects

- `fo:declarations`

## Child Objects

None. This is an empty element.

## Code Samples

No code sample provided in the Antenna House reference for this formatting object.

The following is a **constructed example** (not from the reference):

```xml
<!-- Constructed example: Mapping generic font families for Japanese and Latin scripts -->
<fo:declarations>
  <axf:script-font script="Jpan"
                   serif="MS Mincho"
                   sans-serif="MS Gothic"
                   monospace="MS Gothic"/>
  <axf:script-font script="Latn"
                   serif="Times New Roman"
                   sans-serif="Arial"
                   monospace="Courier New"/>
  <axf:script-font script="Arab"
                   serif="Traditional Arabic"
                   sans-serif="Simplified Arabic"
                   fallback="Arial Unicode MS"/>
</fo:declarations>
```
