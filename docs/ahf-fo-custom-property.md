# axf:custom-property

## Summary

The `axf:custom-property` extension formatting object specifies a custom property in PDF output. It is effective with PDF 1.4 or later. This object is invalid with PDF/A output. This object does not create an area.

<!-- Source: XSL-FO-Reference-74-MID.pdf p.295-296 -->

## Properties

| Property | Description |
|---|---|
| `name` | The name of the custom property (AHF specific) |
| `value` | The value of the custom property (AHF specific) |

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
  <axf:custom-property name="Department" value="Engineering"/>
  <axf:custom-property name="DocumentVersion" value="2.1"/>
  <axf:custom-property name="ReviewStatus" value="Approved"/>
</fo:declarations>
```
