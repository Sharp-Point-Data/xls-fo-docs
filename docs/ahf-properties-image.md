# Antenna House Extension Properties: Image Properties

<!-- Source: XSL-FO-Reference-74-MID.pdf pp.312-476 -->

Properties controlling image resolution, orientation, and preprocessing.

## axf:image-orientation

Rotates the image. Values have the following meanings:

- **from-image:** Follows the image information (such as the orientation specified in metadata).
- **none:** Does not rotate the image.
- **[ 0 | 90 | 180 | 270 ] flip?:** Rotates the image by the specified angle. If flip is specified, the image will be horizontally flipped after the rotation.

| Attribute | Value |
|---|---|
| **Applies to** | `<fo:external-graphic>`, `<fo:instream-foreign-object>` |
| **Values** | from-image \| none \| [ 0 \| 90 \| 180 \| 270 ] flip? |
| **Initial** | from-image |
| **Inherited** | yes |

## axf:image-preproc

Preprocesses the image. The following can be specified for `<string>`:

- **OSDC [params]:** The data specified to src for `<fo:external-graphic>` is converted to PDF using Office Server Document Converter (abbreviated as OSDC), and the PDF is embedded in the document. Further explanations on the application can be found in the AH Formatter Online Manual.

| Attribute | Value |
|---|---|
| **Applies to** | `<fo:external-graphic>` |
| **Values** | `<string>` |
| **Initial** | empty string |
| **Inherited** | no |

## axf:image-resolution

Specifies the resolution of an image. The resolution of a background image is specified by axf:background-image-resolution. In case of vector images, such as SVG, it is applied to numerical values with no units. from-image is ignored.

Values have the following meanings:

- **normal:** Depends on the default value of the system. It is the value specified as pxpi in the Option Setting File. Ignores the actual resolution of an image.
- **from-image:** Uses the actual resolution of an image. When an image does not have the resolution, it will follow the specification. If nothing is specified, it is the same as normal.
- **`<dpi>`:** Specifies the resolution (dpi). Ignores the actual resolution of an image. You can also use dpcm as a unit to indicate the resolution.

| Attribute | Value |
|---|---|
| **Applies to** | `<fo:external-graphic>`, `<fo:instream-foreign-object>` |
| **Values** | normal \| [ from-image \|\| `<dpi>` ] |
| **Initial** | from-image |
| **Inherited** | no |
