# axf:tab

## Summary

The tab character (U+0009) will be normalized to the white space (U+0020); therefore, the character normally has a meaning of just a white space. However, there are a lot of document structures that the tab character aligns the text, such as JIS X 4051:2004. AH XSL Formatter provides the extension that enables to express the tab structure.

`axf:tab` places a white space up to a tab stop position. Specify the tab stop position with `axf:tab-stops`.

**CAUTION:** A line which contains a tab will be forced to `text-align="start"`.

**CAUTION:** We cannot guarantee the best result of a tab processing in case a text requires the BIDI processing.

## Properties

| Property | Description |
|----------|-------------|
| `axf:tab-align` | Specifies the alignment of text at the tab stop position |

## Parent Objects

- `fo:block` (practically useful context)

## Child Objects

None. This is an empty/inline-level element.

## Code Samples

No code sample provided in the Antenna House reference for this formatting object.

The following is a **constructed example** (not from the reference):

```xml
<!-- Constructed example: Using axf:tab with tab stops to create aligned columns -->
<fo:block axf:tab-stops="100pt 250pt right 400pt">
  Item Description<axf:tab/>Qty<axf:tab/>Unit Price<axf:tab/>Total
</fo:block>
<fo:block axf:tab-stops="100pt 250pt right 400pt">
  Widget A<axf:tab/>10<axf:tab/>$5.00<axf:tab/>$50.00
</fo:block>
<fo:block axf:tab-stops="100pt 250pt right 400pt">
  Widget B<axf:tab/>25<axf:tab/>$3.50<axf:tab/>$87.50
</fo:block>
```

```xml
<!-- Constructed example: Right-aligned tab for a table of contents style layout -->
<fo:block axf:tab-stops="right 450pt">
  Chapter 1: Introduction<axf:tab/>1
</fo:block>
<fo:block axf:tab-stops="right 450pt">
  Chapter 2: Getting Started<axf:tab/>15
</fo:block>
<fo:block axf:tab-stops="right 450pt">
  Chapter 3: Advanced Topics<axf:tab/>42
</fo:block>
```
