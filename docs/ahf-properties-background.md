# Antenna House Extension Properties: Background Extension Properties

<!-- Source: XSL-FO-Reference-74-MID.pdf pp.312-476 -->

Extensions to the standard CSS/XSL-FO background properties, adding CSS3-style background-size, background-origin, and background-clip capabilities.

## axf:background-clip

This property specifies the display area of the image (box or content only).

| Attribute | Value |
|---|---|
| **Applies to** | `<fo:simple-page-master>`, `<fo:page-sequence>`, all formatting objects |
| **Values** | [ border-box \| padding-box \| content-box ]# |
| **Initial** | padding-box |
| **Inherited** | no |

## axf:background-content-type

Specifies the content type of a background image.

| Attribute | Value |
|---|---|
| **Applies to** | `<fo:simple-page-master>`, `<fo:page-sequence>`, all formatting objects |
| **Values** | [`<string>` \| auto]# |
| **Initial** | auto |
| **Inherited** | no |

## axf:background-image-resolution

Specifies the resolution of a background image. Values have the following meanings:

- **normal:** Depends on the default value of the system. It is the value specified as pxpi in the Option Setting File. Ignores the actual resolution of an image.
- **from-image:** Uses the actual resolution of an image. When an image does not have the resolution, it will follow the dpi specification. If nothing is specified, it is the same as normal.
- **`<dpi>`:** Specifies the resolution (dpi). Ignores the actual resolution of an image.

The resolution of a non-background image is specified by axf:image-resolution. In case of vector images, such as SVG, it is applied to numerical values with no units. from-image is ignored.

| Attribute | Value |
|---|---|
| **Applies to** | `<fo:simple-page-master>`, `<fo:page-sequence>`, all formatting objects |
| **Values** | [normal \| [ from-image \|\| `<dpi>` ]]# |
| **Initial** | from-image |
| **Inherited** | no |

## axf:background-origin

This property specifies the positioning of the original image. If this property is set, the simultaneous setting of background-attachment is contradictory.

| Attribute | Value |
|---|---|
| **Applies to** | `<fo:simple-page-master>`, `<fo:page-sequence>`, all formatting objects |
| **Values** | [ border-box \| padding-box \| content-box ]# |
| **Initial** | padding-box |
| **Inherited** | no |

## axf:background-size

See the CSS Backgrounds and Borders Module Level 3 specification for full details on background-size behavior.

| Attribute | Value |
|---|---|
| **Applies to** | `<fo:simple-page-master>`, `<fo:page-sequence>`, all formatting objects |
| **Values** | [ [ `<length>` \| `<percentage>` \| auto ]{1,2} \| cover \| contain ]# |
| **Initial** | auto |
| **Inherited** | no |
