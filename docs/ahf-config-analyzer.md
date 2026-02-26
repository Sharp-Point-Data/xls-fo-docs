# Antenna House Configuration: Analyzer Settings

<!-- Source: XSL-FO-Reference-74-MID.pdf pp.283-290 -->

## Overview

The `<analyzer-settings>` element configures the AH Formatter Analyzer tool for automated analysis of the Area Tree. The Analyzer detects typographic quality issues such as widows, rivers of white space, excessive hyphenation, unbalanced spreads, and repeated line beginnings or endings. Each analysis check can be individually enabled or disabled, and threshold values control the sensitivity of each check. For full details, see "Automated Analysis" in the Features section of the AH Formatter Online Manual.

## Element: `<analyzer-settings>`

**Parent:** `<formatter-config>`

**Attributes:** `analyze`, `end-blank-pages`, `end-blank-pages-limit`, `hyphen`, `hyphen-limit`, `line-start-end`, `line-start-limit`, `line-start-repeat-limit`, `line-end-limit`, `line-end-repeat-limit`, `lines-after`, `lines-before`, `page-widow`, `page-widow-limit-em`, `page-widow-limit-percent`, `paragraph-widow`, `paragraph-widow-limit-em`, `paragraph-widow-limit-percent`, `river`, `river-zone`, `unbalanced-spread`, `unbalanced-spread-limit`, `white-space`

**Child elements:** None

## Attributes

### `analyze`

Specifies whether or not to perform analysis checks.

- **Applies to:** `<analyzer-settings>`
- **Values:** `false` | `true`
- **Default:** `true`

### `end-blank-pages`

Specifies whether or not to analyze the number of blank pages at the end of the document.

- **Applies to:** `<analyzer-settings>`
- **Values:** `false` | `true`
- **Default:** `true`

### `end-blank-pages-limit`

Allowed number of blank pages at the end of document.

- **Applies to:** `<analyzer-settings>`
- **Values:** `<integer>`
- **Default:** `2`

### `hyphen`

Specifies whether or not to analyze the number of consecutive lines that end with a hyphen.

- **Applies to:** `<analyzer-settings>`
- **Values:** `false` | `true`
- **Default:** `true`

### `hyphen-limit`

Allowed number of consecutive lines that end with a hyphen.

- **Applies to:** `<analyzer-settings>`
- **Values:** `<integer>`
- **Default:** `3`

### `line-start-end`

Specifies whether or not to analyze consecutive lines that start, or that end, with the same word.

- **Applies to:** `<analyzer-settings>`
- **Values:** `false` | `true`
- **Default:** `true`

### `line-start-limit`

Maximum number of characters to compare at the start of a line.

- **Applies to:** `<analyzer-settings>`
- **Values:** `<integer>`
- **Default:** `8`

### `line-start-repeat-limit`

Allowed number of lines that start with the same word.

- **Applies to:** `<analyzer-settings>`
- **Values:** `<integer>`
- **Default:** `2`

### `line-end-limit`

Maximum number of characters to compare at the end of a line.

- **Applies to:** `<analyzer-settings>`
- **Values:** `<integer>`
- **Default:** `8`

### `line-end-repeat-limit`

Allowed number of lines that end with the same word.

- **Applies to:** `<analyzer-settings>`
- **Values:** `<integer>`
- **Default:** `2`

### `lines-after`

Specifies whether or not to analyze the number of lines after a block.

- **Applies to:** `<analyzer-settings>`
- **Values:** `false` | `true`
- **Default:** `true`

### `lines-before`

Specifies whether or not to analyze the number of lines before a block.

- **Applies to:** `<analyzer-settings>`
- **Values:** `false` | `true`
- **Default:** `true`

### `page-widow`

Specifies whether or not to analyze pages that start with a page-level widow.

- **Applies to:** `<analyzer-settings>`
- **Values:** `false` | `true`
- **Default:** `true`

### `page-widow-limit-em`

Minimum width, in `em` for the current block, of a widow line at the start of a page. If the value is `0`, this setting is ignored. A negative value is treated as `0`.

- **Applies to:** `<analyzer-settings>`
- **Values:** `<number>`
- **Default:** `2.5`

### `page-widow-limit-percent`

Minimum width, in percent of the current block width, of a widow line at the start of a page. If the value is `0`, this setting is ignored. A negative value is treated as `0`.

- **Applies to:** `<analyzer-settings>`
- **Values:** `<integer>`
- **Default:** `15`

### `paragraph-widow`

Specifies whether or not to analyze paragraphs that end with a paragraph-level widow.

- **Applies to:** `<analyzer-settings>`
- **Values:** `false` | `true`
- **Default:** `true`

### `paragraph-widow-limit-em`

Minimum width, in `em` for the current block, of a widow line at the start of a paragraph. If the value is `0`, this setting is ignored. A negative value is treated as `0`.

- **Applies to:** `<analyzer-settings>`
- **Values:** `<number>`
- **Default:** `2.5`

### `paragraph-widow-limit-percent`

Minimum width, in percent of the current block width, of a widow line at the start of a paragraph. If the value is `0`, this setting is ignored. A negative value is treated as `0`.

- **Applies to:** `<analyzer-settings>`
- **Values:** `<integer>`
- **Default:** `15`

### `river`

Either the maximum allowed cumulative width, in `em` or as an absolute length, for a river of white-space within a block or the value `none` to disable river analysis.

- **Applies to:** `<analyzer-settings>`
- **Values:** `<length>` | `<integer>em` | `none`
- **Default:** `1em`

### `river-zone`

Maximum allowed width between two non-overlapping spaces on consecutive lines for the spaces to be considered a part of the same river. This setting is ignored when `river` is `none`.

- **Applies to:** `<analyzer-settings>`
- **Values:** `<integer>`
- **Default:** `0`

### `unbalanced-spread`

Specifies whether or not to analyze unbalanced spreads.

- **Applies to:** `<analyzer-settings>`
- **Values:** `false` | `true`
- **Default:** `true`

### `unbalanced-spread-limit`

Allowed height difference, in `pt`, for an unbalanced spread. A negative value is treated as `0`.

- **Applies to:** `<analyzer-settings>`
- **Values:** `<integer>`
- **Default:** `0`

### `white-space`

Either the maximum width, in `em` or as an absolute length, for white-space between consecutive words on a line or the value `none` to disable white-space analysis.

- **Applies to:** `<analyzer-settings>`
- **Values:** `<length>` | `<integer>em` | `none`
- **Default:** `0.40em`

## Attributes Summary Table

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `analyze` | `boolean` | `true` | Master switch for all analysis checks |
| `end-blank-pages` | `boolean` | `true` | Check blank pages at end of document |
| `end-blank-pages-limit` | `integer` | `2` | Allowed trailing blank pages |
| `hyphen` | `boolean` | `true` | Check consecutive hyphenated lines |
| `hyphen-limit` | `integer` | `3` | Allowed consecutive hyphenated lines |
| `line-start-end` | `boolean` | `true` | Check repeated words at line start/end |
| `line-start-limit` | `integer` | `8` | Max characters compared at line start |
| `line-start-repeat-limit` | `integer` | `2` | Allowed lines starting with same word |
| `line-end-limit` | `integer` | `8` | Max characters compared at line end |
| `line-end-repeat-limit` | `integer` | `2` | Allowed lines ending with same word |
| `lines-after` | `boolean` | `true` | Check lines after a block |
| `lines-before` | `boolean` | `true` | Check lines before a block |
| `page-widow` | `boolean` | `true` | Check page-level widows |
| `page-widow-limit-em` | `number` | `2.5` | Min widow width in em |
| `page-widow-limit-percent` | `integer` | `15` | Min widow width in percent |
| `paragraph-widow` | `boolean` | `true` | Check paragraph-level widows |
| `paragraph-widow-limit-em` | `number` | `2.5` | Min paragraph widow width in em |
| `paragraph-widow-limit-percent` | `integer` | `15` | Min paragraph widow width in percent |
| `river` | `length/em/none` | `1em` | Max river width or `none` to disable |
| `river-zone` | `integer` | `0` | Max gap between river spaces |
| `unbalanced-spread` | `boolean` | `true` | Check unbalanced spreads |
| `unbalanced-spread-limit` | `integer` | `0` | Allowed height difference in pt |
| `white-space` | `length/em/none` | `0.40em` | Max word spacing or `none` to disable |

## Example Option Setting File

<!-- Source: XSL-FO-Reference-74-MID.pdf pp.289-290 -->

The following is an example of a complete AH Formatter option setting file showing `<formatter-settings>`, `<pdf-settings>`, and `<font-settings>` configuration:

```xml
<?xml version="1.0"?>
<formatter-config>
   <formatter-settings
      default-page-width="210mm"
      default-page-height="297mm"
      default-font-size="10pt"
      normal-line-height="1.2"
      default-color="#000000"
      border-thin-width="1pt"
      border-medium-width="3pt"
      border-thick-width="5pt"
      pxpi="96"
      default-lang=""
      default-CJK="ja"
      punctuation-trim="true"
      text-autospace="true"
      vertical-underline-side="auto"
      punctuation-spacing="0.5"
      text-autospace-width="0.25"/>
   <pdf-settings
      embed-all-fonts="false"
      error-on-embed-fault="false"
      user-password=""
      master-password=""
      no-printing="false"
      no-changing="false"
      no-content-copying="false"
      no-adding-or-changing-comments="false"
      color-compression="auto"
      color-jpeg-quality="80"
      text-and-lineart-compression="true"
      use-launch-for-local-file="true"
      rasterize-resolution="108">
      <embed-font font="Arial"/>
      <embed-font font="Courier New"/>
   </pdf-settings>
   <font-settings default-font-family="serif">
      <script-font
         serif="Times New Roman"
         sans-serif="Arial"
         monospace="Courier New"
         cursive="Times New Roman"
         fantasy="Times New Roman"/>
      <script-font
         script="Jpan"
         serif="IPAMincho"
         sans-serif="IPAGothic"
         monospace="IPAMincho"/>
      <script-font
         script="Hang"
         serif="Batang"
         sans-serif="Gulim"
         monospace="Batang"/>
   </font-settings>
</formatter-config>
```

**Note:** The example file continues beyond what is shown in the source material (p.290 is the last page captured). The `<script-font script="Hang">` element and the closing tags for `<font-settings>` and `<formatter-config>` are inferred for completeness, as the source excerpt ends mid-element. The actual values for the Korean (`Hang`) script font beyond `serif="Batang"` are constructed to complete the example.
