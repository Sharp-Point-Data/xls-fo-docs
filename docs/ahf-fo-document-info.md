# axf:document-info

## Summary

The `axf:document-info` extension formatting object is an empty object that can be used in arbitrary accumulation to embed different document-related information in the PDF output. These are referred to as PDF keywords, specified with the `name` property, and written as CDATA contents or keywords in the `value` property.

<!-- Source: XSL-FO-Reference-74-MID.pdf p.296-297 -->

A distinction must be made between single and multiple PDF document output:

- **Single PDF output:** `axf:document-info` must stand as a direct child object before all other child objects in `fo:root`.
- **Multiple PDF output:** `axf:document-info` must stand as the first child object under the `fo:page-sequence` object which constitutes the PDF document. Any `axf:document-info` objects standing under `fo:root` will be ignored in this case.

### Supported PDF Keywords

**Bibliography-related keywords:**

| `name` value | Description |
|---|---|
| `document-title` | The document title |
| `subject` | The document subject |
| `author` | The document author |
| `author-title` | The author title (invalid when XMP file is referenced) |
| `description-writer` | The description writer (invalid when XMP file is referenced) |
| `keywords` | Document keywords |
| `copyright-status` | Values: `Unknown`, `Copyrighted`, or `PublicDomain` (invalid when XMP file is referenced) |
| `copyright-notice` | The copyright information as value (invalid when XMP file is referenced) |
| `copyright-info-url` | URL of the copyright information (treated as text only, does not generate access to the URL) (invalid when XMP file is referenced) |
| `xmp` | URL of an external XMP file (uri-specification of XSL) |

When an XMP file is referenced, `author-title`, `description-writer`, `copyright-status`, `copyright-notice`, and `copyright-info-url` names become invalid. Instead of referencing an XMP file, the `axf:custom-property` extension object can also be used.

**Display keywords when the document is opened:**

| `name` value | Allowed `value` values |
|---|---|
| `pagemode` | `UseNone`, `UseOutlines`, `UseThumbs`, `FullScreen`, `UseOC` |
| `pagelayout` | `SinglePage`, `OneColumn`, `TwoColumnLeft`, `TwoColumnRight`, `TwoPageLeft`, `TwoPageRight` |

**Display window related keywords:**

| `name` value | Allowed `value` values | Default |
|---|---|---|
| `hidetoolbar` | `true`, `false` | `false` |
| `hidemenubar` | `true`, `false` | `false` |
| `hidewindowui` | `true`, `false` | `false` |
| `fitwindow` | `true`, `false` | `false` |
| `centerwindow` | `true`, `false` | `false` |
| `displaydoctitle` | `true`, `false` | `false` |
| `openaction` | Special application specifications | |

**Date-related keywords:**

| `name` value | Description |
|---|---|
| `createdate` | The creation date |
| `modifydate` | The modification date |

## Properties

| Property | Description |
|---|---|
| `name` | The PDF keyword name (AHF specific) |
| `value` | The PDF keyword value (AHF specific) |

## Parent Objects

- `fo:root` (for single PDF output)
- `fo:page-sequence` (for multiple PDF output)

## Child Objects

None. This is an empty formatting object.

## Code Samples

No code sample provided in the Antenna House reference for this formatting object.

The following is a constructed example showing setting title, author, and subject (not from the reference):

<!-- Constructed example — not from reference material -->
```xml
<fo:root xmlns:fo="http://www.w3.org/1999/XSL/Format"
         xmlns:axf="http://www.antennahouse.com/names/XSL/Extensions">
  <axf:document-info name="document-title" value="Quarterly Report Q3 2025"/>
  <axf:document-info name="author" value="Jane Smith"/>
  <axf:document-info name="subject" value="Financial results for Q3"/>
  <axf:document-info name="keywords" value="finance, quarterly, report"/>
  <axf:document-info name="displaydoctitle" value="true"/>
  <axf:document-info name="pagelayout" value="SinglePage"/>
  <fo:layout-master-set>
    <!-- ... -->
  </fo:layout-master-set>
  <fo:page-sequence master-reference="default">
    <!-- ... -->
  </fo:page-sequence>
</fo:root>
```
