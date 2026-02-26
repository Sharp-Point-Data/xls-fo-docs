# Antenna House Configuration: PDF Output Settings

<!-- Source: XSL-FO-Reference-74-MID.pdf pp.264–272 -->

## Overview

The `<pdf-settings>` element configures PDF output for AH Formatter. It controls PDF version, font embedding, encryption, image compression, downsampling, tagging, annotations, EPS processing, and many other PDF-specific output options. It is a child of `<formatter-config>` and contains an optional `<embed-font>` child element.

For attributes not documented here, refer to the section "PDF Output Settings" in the AH Formatter Online Manual (file: `ahf-optset.html`).

## Element: `<pdf-settings>`

**Parent:** `<formatter-config>`

**Child elements:** `<embed-font>`

**Full attribute list:** `allow-deprecated-annotation`, `allow-embedding-lower-versions`, `allow-javascript`, `allow-nest-alt-text`, `check-tag-relationship`, `color-compression`, `color-compression-default`, `color-compression-minimum`, `color-conversion`, `color-downsampling`, `color-downsampling-above-dpi`, `color-downsampling-target-dpi`, `color-downsampling-default`, `color-downsampling-above-dpi-default`, `color-downsampling-target-dpi-default`, `color-downsampling-minimum`, `color-downsampling-above-dpi-minimum`, `color-downsampling-target-dpi-minimum`, `color-jpeg-quality`, `color-jpeg-quality-default`, `color-jpeg-quality-minimum`, `default-output-intent`, `embed-all-fonts`, `embed-font-encoding`, `embed-std-output-intent`, `embed-subset-font-percentage`, `encrypt-metadata`, `encryption-level`, `EPS-processor`, `error-on-embed-fault`, `error-on-missing-glyph`, `error-on-pdfx-fault`, `fallback-alttext`, `ghostscript`, `grayscale-compression`, `grayscale-compression-default`, `grayscale-compression-minimum`, `grayscale-downsampling`, `grayscale-downsampling-above-dpi`, `grayscale-downsampling-target-dpi`, `grayscale-downsampling-default`, `grayscale-downsampling-above-dpi-default`, `grayscale-downsampling-target-dpi-default`, `grayscale-downsampling-minimum`, `grayscale-downsampling-above-dpi-minimum`, `grayscale-downsampling-target-dpi-minimum`, `grayscale-jpeg-quality`, `grayscale-jpeg-quality-default`, `grayscale-jpeg-quality-minimum`, `gs-options`, `image-color-profile`, `import-annotation-types`, `import-tagged-pdf`, `joboptions`, `linearized`, `mediabox-origin-zero`, `monochrome-compression`, `monochrome-compression-default`, `monochrome-compression-minimum`, `monochrome-downsampling`, `monochrome-downsampling-above-dpi`, `monochrome-downsampling-target-dpi`, `monochrome-downsampling-default`, `monochrome-downsampling-above-dpi-default`, `monochrome-downsampling-target-dpi-default`, `monochrome-downsampling-minimum`, `monochrome-downsampling-above-dpi-minimum`, `monochrome-downsampling-target-dpi-minimum`, `multimedia-treatment`, `new-tagging-mode`, `no-accessibility`, `no-adding-or-changing-comments`, `no-assemble-doc`, `no-changing`, `no-content-copying`, `no-fill-form`, `object-compression`, `object-compression-default`, `object-compression-minimum`, `overprint`, `owner-password`, `page-labels`, `pages-max-kids`, `pass-through`, `pass-through-default`, `pass-through-minimum`, `pdf-version`, `printing-allowed`, `rasterize-resolution`, `real-value-limit`, `real-value-limit-modify`, `reverse-page`, `tagged-pdf`, `text-and-lineart-compression`, `text-and-lineart-compression-default`, `text-and-lineart-compression-minimum`, `transparency`, `transparency-color-space`, `use-launch-for-local-file`, `user-password`, `xmp-padding`

## Documented Attributes

### `allow-deprecated-annotation`

In PDF 2.0, some annotations (Movie, Sound) are deprecated and cannot be output. If you specify `true`, you will be able to output these in PDF 2.0.

- **Applies to:** `<pdf-settings>`
- **Values:** `false` | `true`
- **Default:** `false`

### `allow-embedding-lower-versions`

In PDF 2.0, embedding of PDF 1.X is deprecated. If you specify `true`, you will be able to embed PDF 1.X in PDF 2.0.

- **Applies to:** `<pdf-settings>`
- **Values:** `false` | `true`
- **Default:** `false`

### `embed-all-fonts`

Specifies whether or not to embed in the PDF all fonts that are embeddable:

- `false` — Only fonts specified in `<embed-font>` are embedded.
- `true` — All fonts that can be embedded will be embedded, except for the Standard 14 Fonts.
- `base14` — All fonts that can be embedded will be embedded, including the Standard 14 Fonts.

In the GUI, this can be specified by selecting the "Embed All Embeddable Fonts" option.

- **Applies to:** `<pdf-settings>`
- **Values:** `false` | `true` | `base14`
- **Default:** `true`

### `EPS-processor`

Specifies whether to output PDF after converting EPS to PDF using an external processor when outputting EPS to PDF in the formatted result. The value is case-insensitive.

- `none` — Use nothing. The same behavior as in the past.
- `distiller` — Use Adobe Distiller in environments where Adobe Distiller is installed. `acrodist.exe` is used. Effective only with the Windows version. PS support has some restrictions:
  - PS-Adobe-2.0 or later required.
  - `%%BeginProlog` and `%%EndProlog` should be included.
  - See also the `joboptions` attribute.
- `ghostscript` — Use Ghostscript in environments where Ghostscript is installed. Uses `gswin32c.exe` with the Windows version (`gswin64c.exe` with Windows 64-bit) and `gs` with non-Windows. Since the program is invoked by `fork()` etc., there is no problem with the GPL license.
  - See also the `ghostscript` attribute.

Invalid in environments where the respective processor is not installed. The PATH must be set for the program to use.

- **Applies to:** `<pdf-settings>`
- **Values:** `none` | `ghostscript` | `distiller`
- **Default:** `none`

### `ghostscript`

When converting EPS into PDF using Ghostscript, the full path to Ghostscript can be specified. For example, specify as `ghostscript="/usr/local/bin/gs"`. This allows Ghostscript to be invoked even if the PATH does not include Ghostscript. Specify `gswin32c.exe` in the Windows version (`gswin64c.exe` with Windows 64-bit).

- **Applies to:** `<pdf-settings>`
- **Values:** path to Ghostscript program
- **Default:** none

### `gs-options`

When converting EPS into PDF using Ghostscript, AH Formatter V7.2 specifies the following parameters and starts Ghostscript by default:

```
-dPDFSETTINGS=/printer
-dNOPAUSE
-dBATCH
-dSAFER
-sDEVICE=pdfwrite
-dDEVICEWIDTHPOINTS=%width
-dDEVICEHEIGHTPOINTS=%height
-dEPSFitPage
-dCompatibilityLevel=1.3
-dAutoRotatePages=/None
-q
-sOutputFile=%temp
-c
.setpdfwrite
-f
%eps
```

The following four values starting with `%` are replaced by their respective values by AH Formatter V7.2:

- `%width` — Width of EPS
- `%height` — Height of EPS
- `%eps` — Input EPS
- `%temp` — Temporary Output File

You can specify any parameter with `gs-options`. Specify multiple parameters separated by U+000A (line feed). The `gs-options` setting completely replaces the above default settings and launches Ghostscript. The setting of `-sOutputFile` is always considered to be `-sOutputFile=%temp`. If `%temp` is not included, it will be added. If `%eps` is not included, it will be added at the end. The operation is not guaranteed when invalid parameters are specified.

- **Applies to:** `<pdf-settings>`
- **Values:** Parameters separated by the character U+000A
- **Default:** none

### `import-annotation-types`

Annotations contained in the embedded PDF can be embedded directly in PDF. Specify the following character strings (case insensitive) separated by white spaces:

`All` | `Text` | `Link` | `FreeText` | `Line` | `Square` | `Circle` | `Polygon` | `PolyLine` | `Highlight` | `Underline` | `Squiggly` | `StrikeOut` | `Stamp` | `Caret` | `Ink` | `Popup` | `FileAttachment` | `Sound` | `Movie` | `Screen` | `3D` | `RichMedia` | `Other`

Specify `Other` when you embed annotations with no type written. When `All` is specified, all the annotations are embedded. In GUI, it can be specified by selecting the "Import All Annotations" option. For more details, see also PDF Embedding in PDF Output of the Online Manual.

- **Applies to:** `<pdf-settings>`
- **Values:** Space-separated list of annotation types (see above)
- **Default:** none

### `import-tagged-pdf`

Specifies whether to permit embedding tagged PDF in tagged PDF. If `true` is specified, the tagged PDF is embedded "as is" without producing an error. In GUI, you can change the setting at "Allow Importing Tagged PDF". For more details, see also PDF Embedding in PDF Output of the Online Manual.

- **Applies to:** `<pdf-settings>`
- **Values:** `false` | `true`
- **Default:** `false`

### `multimedia-treatment`

Specifies whether to embed multimedia (see Multimedia in PDF Output of the Online Manual) in PDF in case of `axf:multimedia-treatment="auto"`:

- `embed` — Embed multimedia directly.
- `absolute-link` — Use an absolute link.
- `relative-link` — Use a relative link.
- `richmedia` — Use RichMedia.
- `richmedia-windowed` — Use RichMedia in windowed mode.

- **Applies to:** `<pdf-settings>`
- **Values:** `embed` | `absolute-link` | `relative-link` | `richmedia` | `richmedia-windowed`
- **Default:** `embed`

### `new-tagging-mode`

If `true` is specified, when explicitly specifying an empty string such as `axf:pdftag="''"`, that element does not create a tag but belongs to the tag to which the parent area belongs. In addition, the Role Map is also enabled, and maps from nonstandard tag names to standard tag names are valid. Specifying `axf:pdftag="''"` on the root element has no effect since the root element does not have a parent: a Document tag is always created.

- **Applies to:** `<pdf-settings>`
- **Values:** `true` | `false`
- **Default:** `false`

### `overprint`

Specifies the overprint. Any values of `axf:overprint` other than `auto` can be specified.

- **Applies to:** `<pdf-settings>`
- **Values:** See `axf:overprint`
- **Default:** none

### `pdf-version`

Specifies the version of the PDF to create. Available values:

| Value | Description |
|-------|-------------|
| `PDF1.3` | PDF version 1.3 |
| `PDF1.4` | PDF version 1.4 |
| `PDF1.5` | PDF version 1.5 (system setting) |
| `PDF1.6` | PDF version 1.6 |
| `PDF1.7` | PDF version 1.7 (requires Adobe Acrobat Reader 8.0 or higher) |
| `PDF2.0` | Compliant with ISO 32000-2:2017 |
| `PDF/X-1a:2001`, `PDF/X-3:2002`, `PDF/X-1a:2003`, `PDF/X-2:2003`, `PDF/X-3:2003`, `PDF/X-4:2010`, `PDF/X-4p:2010` | PDF/X variants (optimized for print output, ISO 15930-7:2010) |
| `PDF/A-1a:2005`, `PDF/A-1b:2005` | PDF/A variants (optimized for archiving) |
| `PDF1.4/A-2a:2011`, `PDF1.4/A-2b:2011`, `PDF1.4/A-2u:2011`, `PDF1.4/A-3a:2012`, `PDF1.4/A-3b:2012`, `PDF1.4/A-3u:2012` | PDF/A variants based on PDF 1.4 |
| `PDF1.5/A-2a:2011`, `PDF1.5/A-2b:2011`, `PDF1.5/A-2u:2011`, `PDF1.5/A-3a:2012`, `PDF1.5/A-3b:2012`, `PDF1.5/A-3u:2012` | PDF/A variants based on PDF 1.5 |
| `PDF1.6/A-2a:2011`, `PDF1.6/A-2b:2011`, `PDF1.6/A-2u:2011`, `PDF1.6/A-3a:2012`, `PDF1.6/A-3b:2012`, `PDF1.6/A-3u:2012` | PDF/A variants based on PDF 1.6 |
| `PDF1.7/A-2a:2011`, `PDF1.7/A-2b:2011`, `PDF1.7/A-2u:2011`, `PDF1.7/A-3a:2012`, `PDF1.7/A-3b:2012`, `PDF1.7/A-3u:2012` | PDF/A variants based on PDF 1.7 |
| `PDF1.5/UA-1:2014`, `PDF1.6/UA-1:2014`, `PDF1.7/UA-1:2014` | PDF/UA (Universal Accessibility, ISO 14289-1:2014). Alternative textual descriptions can be specified with `axf:alttext`; links with `axf:annotation-contents`. |

In GUI, it can be specified by selecting the "PDF Version" option.

- **Applies to:** `<pdf-settings>`
- **Values:** See the versions above
- **Default:** `PDF1.5`

### `tagged-pdf`

Specifies whether to make a Tagged PDF file. PDF may not be able to be tagged depending on the PDF version. In this case this setting will be ignored. In GUI, it can be specified by selecting the "Tagged PDF" option.

- **Applies to:** `<pdf-settings>`
- **Values:** `true` | `false`
- **Default:** `false`

## Additional Attributes (Listed in Source)

The following attributes are listed in the source material attribute enumeration for `<pdf-settings>` but their detailed descriptions refer to the AH Formatter Online Manual (`ahf-optset.html`):

| Attribute | Category |
|-----------|----------|
| `allow-javascript` | JavaScript |
| `allow-nest-alt-text` | Accessibility |
| `check-tag-relationship` | Tagging |
| `color-compression` | Image compression (color) |
| `color-compression-default` | Image compression (color) |
| `color-compression-minimum` | Image compression (color) |
| `color-conversion` | Color management |
| `color-downsampling` | Image downsampling (color) |
| `color-downsampling-above-dpi` | Image downsampling (color) |
| `color-downsampling-target-dpi` | Image downsampling (color) |
| `color-downsampling-default` | Image downsampling (color) |
| `color-downsampling-above-dpi-default` | Image downsampling (color) |
| `color-downsampling-target-dpi-default` | Image downsampling (color) |
| `color-downsampling-minimum` | Image downsampling (color) |
| `color-downsampling-above-dpi-minimum` | Image downsampling (color) |
| `color-downsampling-target-dpi-minimum` | Image downsampling (color) |
| `color-jpeg-quality` | Image quality (color) |
| `color-jpeg-quality-default` | Image quality (color) |
| `color-jpeg-quality-minimum` | Image quality (color) |
| `default-output-intent` | PDF/X |
| `embed-font-encoding` | Font embedding |
| `embed-std-output-intent` | PDF/X |
| `embed-subset-font-percentage` | Font embedding |
| `encrypt-metadata` | Encryption |
| `encryption-level` | Encryption |
| `error-on-embed-fault` | Error handling |
| `error-on-missing-glyph` | Error handling |
| `error-on-pdfx-fault` | Error handling |
| `fallback-alttext` | Accessibility |
| `grayscale-compression` | Image compression (grayscale) |
| `grayscale-compression-default` | Image compression (grayscale) |
| `grayscale-compression-minimum` | Image compression (grayscale) |
| `grayscale-downsampling` | Image downsampling (grayscale) |
| `grayscale-downsampling-above-dpi` | Image downsampling (grayscale) |
| `grayscale-downsampling-target-dpi` | Image downsampling (grayscale) |
| `grayscale-downsampling-default` | Image downsampling (grayscale) |
| `grayscale-downsampling-above-dpi-default` | Image downsampling (grayscale) |
| `grayscale-downsampling-target-dpi-default` | Image downsampling (grayscale) |
| `grayscale-downsampling-minimum` | Image downsampling (grayscale) |
| `grayscale-downsampling-above-dpi-minimum` | Image downsampling (grayscale) |
| `grayscale-downsampling-target-dpi-minimum` | Image downsampling (grayscale) |
| `grayscale-jpeg-quality` | Image quality (grayscale) |
| `grayscale-jpeg-quality-default` | Image quality (grayscale) |
| `grayscale-jpeg-quality-minimum` | Image quality (grayscale) |
| `image-color-profile` | Color management |
| `joboptions` | Distiller |
| `linearized` | PDF structure |
| `mediabox-origin-zero` | PDF structure |
| `monochrome-compression` | Image compression (monochrome) |
| `monochrome-compression-default` | Image compression (monochrome) |
| `monochrome-compression-minimum` | Image compression (monochrome) |
| `monochrome-downsampling` | Image downsampling (monochrome) |
| `monochrome-downsampling-above-dpi` | Image downsampling (monochrome) |
| `monochrome-downsampling-target-dpi` | Image downsampling (monochrome) |
| `monochrome-downsampling-default` | Image downsampling (monochrome) |
| `monochrome-downsampling-above-dpi-default` | Image downsampling (monochrome) |
| `monochrome-downsampling-target-dpi-default` | Image downsampling (monochrome) |
| `monochrome-downsampling-minimum` | Image downsampling (monochrome) |
| `monochrome-downsampling-above-dpi-minimum` | Image downsampling (monochrome) |
| `monochrome-downsampling-target-dpi-minimum` | Image downsampling (monochrome) |
| `no-accessibility` | Security permissions |
| `no-adding-or-changing-comments` | Security permissions |
| `no-assemble-doc` | Security permissions |
| `no-changing` | Security permissions |
| `no-content-copying` | Security permissions |
| `no-fill-form` | Security permissions |
| `object-compression` | Compression |
| `object-compression-default` | Compression |
| `object-compression-minimum` | Compression |
| `owner-password` | Encryption |
| `page-labels` | PDF structure |
| `pages-max-kids` | PDF structure |
| `pass-through` | Image handling |
| `pass-through-default` | Image handling |
| `pass-through-minimum` | Image handling |
| `printing-allowed` | Security permissions |
| `rasterize-resolution` | Rendering |
| `real-value-limit` | PDF structure |
| `real-value-limit-modify` | PDF structure |
| `reverse-page` | Page ordering |
| `text-and-lineart-compression` | Compression |
| `text-and-lineart-compression-default` | Compression |
| `text-and-lineart-compression-minimum` | Compression |
| `transparency` | Rendering |
| `transparency-color-space` | Rendering |
| `use-launch-for-local-file` | Links |
| `user-password` | Encryption |
| `xmp-padding` | Metadata |

## Element: `<embed-font>`

Specifies the fonts that are embedded in the PDF. This element can be specified without limit and is effective only when `embed-all-fonts="false"` is specified. When `embed-all-fonts="false"` is specified and this element is not specified, only the glyphs of the characters that are needed in the PDF output are embedded. When this element is specified and the font indicated here is used within the formatted results, the glyph of the character currently used will be embedded. For a font that is not specified, embedding is performed only for the glyphs of the characters that are needed in the PDF output.

**Parent:** `<pdf-settings>`

### Attributes

#### `font`

The value of this attribute must be the font name of a font whose embedding is allowed. Licensed fonts may be declared as non-embeddable. The PDF generator of the AH Formatter strictly observes this restriction.

- **Applies to:** `<embed-font>`
- **Values:** `<family-name>`
- **Default:** none
