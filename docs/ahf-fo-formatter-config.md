# axf:formatter-config

## Summary

Specifies additional option setting information for Antenna House Formatter. This element does not generate an area. The `src` property can specify an external option setting file. Child elements belong to the namespace `http://www.antennahouse.com/names/XSL/Settings`.

Currently only the following child elements can be described:

- `formatter-settings`
- `pdf-settings`
- `text-settings`
- `svg-settings`
- `ps-settings`
- `mathml-settings`
- `cgm-settings`

All other elements will be disregarded. Some specifications, such as those related to initialization, are ignored.

## Remarks

Usually, the additional setting by `axf:formatter-config` never influences the formatting process of the following document. However, when settings are done by GUI, additional settings will be reflected on the default settings.

The additional option setting information by `axf:formatter-config` is not reflected in the AreaTree.

When `axf-formatter-config="false"` is specified in the Option Setting File, the contents of `axf:formatter-config` will be ignored.

## Properties

- **src** — Specifies the path to an external option setting file.

## Parent Objects

- `fo:declarations`

## Child Objects

Elements in the `http://www.antennahouse.com/names/XSL/Settings` namespace (`axs:*`), including:

- `axs:formatter-settings`
- `axs:pdf-settings`
- `axs:text-settings`
- `axs:svg-settings`
- `axs:ps-settings`
- `axs:mathml-settings`
- `axs:cgm-settings`

## Code Samples

<!-- Source: XSL-FO-Reference-74-MID.pdf p.301 -->
```xml
<fo:declarations>
   <axf:formatter-config src="add-settings.xml"
      xmlns:axs="http://www.antennahouse.com/names/XSL/Settings">
      <axs:pdf-settings pdf-version="PDF1.6" tagged-pdf="true"/>
   </axf:formatter-config>
</fo:declarations>
```

In this example, an additional option setting file, `add-settings.xml` is specified, and then PDF setting is added.
