# axf:output-volume-info

## Summary

Allows PDF output in separate volumes at the level of a page sequence (`fo:page-sequence`). `axf:output-volume-info` is placed directly below `fo:root` at an arbitrary position before the first `fo:page-sequence`. The object is only effective if the PDF is stored in files.

The file names are automatically formed based on the output file name.

In addition to the `axf:output-volume-info` specification in the FO, a `multivol` parameter must be set externally. When using the graphical user interface (GUI), this is done in the PDF Output Dialog.

When you want to specify the language for each PDF output in separate volume, specify the language in `fo:page-sequence` with the `language` property.

## Properties

- **format** — Controls the numbering format for volume file names.
- **axf:bookmark-include** — Specifies whether bookmarks are included in volume output.
- **axf:initial-volume-number** — Sets the initial volume number.
- **axf:document-info-include** — Specifies whether document info is included in volume output.

## Parent Objects

- `fo:root`

## Child Objects

None.

## Code Samples

No code sample provided in the Antenna House reference for this formatting object.

**Constructed example** (not from the Antenna House reference):

```xml
<fo:root xmlns:fo="http://www.w3.org/1999/XSL/Format"
         xmlns:axf="http://www.antennahouse.com/names/XSL/Extensions">
  <fo:layout-master-set>
    <fo:simple-page-master master-name="page">
      <fo:region-body/>
    </fo:simple-page-master>
  </fo:layout-master-set>

  <axf:output-volume-info format="1"
    axf:initial-volume-number="1"
    axf:bookmark-include="true"
    axf:document-info-include="true"/>

  <fo:page-sequence master-reference="page" language="en">
    <fo:flow flow-name="xsl-region-body">
      <fo:block>Volume 1 content</fo:block>
    </fo:flow>
  </fo:page-sequence>

  <fo:page-sequence master-reference="page" language="en">
    <fo:flow flow-name="xsl-region-body">
      <fo:block>Volume 2 content</fo:block>
    </fo:flow>
  </fo:page-sequence>
</fo:root>
```

This constructed example shows a document configured for multi-volume PDF output, where each `fo:page-sequence` produces a separate PDF file. The `multivol` parameter must also be set externally for this to take effect.
