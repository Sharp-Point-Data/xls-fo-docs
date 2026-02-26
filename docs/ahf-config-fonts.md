# Antenna House Configuration: Font Settings

<!-- Source: XSL-FO-Reference-74-MID.pdf pp.257–263 -->

## Overview

The `<font-settings>` element configures font selection, fallback behavior, and generic font family mappings for AH Formatter. It is a child of `<formatter-settings>` and contains optional `<script-font>` and `<font-alias>` child elements.

## Element: `<font-settings>`

**Parent:** `<formatter-settings>`

**Child elements:** `<script-font>`, `<font-alias>`

## Attributes

### `auto-fallback-font`

Specifies whether to look for a fallback font automatically when a glyph cannot be found in the font family specified by the FO. See also Font Selection in the Technical Notes of the Online Manual for more about the fallback method.

- **Applies to:** `<font-settings>`
- **Values:** `true` | `false`
- **Default:** `true`

### `barcode-text-font`

Specifies the font used when adding the text of an original code to the Linear Barcode with the Barcode Generator Option. See Linear Barcode in the Barcode Generator Option of the Online Manual.

- **Applies to:** `<font-settings>`
- **Values:** See Linear Barcode in the Barcode Generator Option of the Online Manual
- **Default:** none

### `default-font-family`

Specifies the default font family. Usually one of the generic font families: serif, sans-serif, cursive, fantasy, or monospace. See also Font Selection in the Technical Notes of the Online Manual.

- **Applies to:** `<font-settings>`
- **Values:** `serif` | `sans-serif` | `cursive` | `fantasy` | `monospace`
- **Default:** `serif`

### `emulated-italic`

Specifies whether to report an error when italic is emulated in the selected font. Values specify the error reporting level:

- `0` — No error message will be reported.
- `1` — The level 1 error message will be reported.
- `2` — The level 2 error message will be reported.
- `3` — The level 3 error message will be reported.
- `4` — The level 4 error message will be reported.

- **Applies to:** `<font-settings>`
- **Values:** `0` | `1` | `2` | `3` | `4`
- **Default:** `0`

### `emulated-small-caps`

Specifies whether to report an error when small-caps is emulated in the selected font. Values specify the error reporting level:

- `0` — No error message will be reported.
- `1` — The level 1 error message will be reported.
- `2` — The level 2 error message will be reported.
- `3` — The level 3 error message will be reported.
- `4` — The level 4 error message will be reported.

No error will be reported when `small-caps-emulation-always="true"` is specified.

- **Applies to:** `<font-settings>`
- **Values:** `0` | `1` | `2` | `3` | `4`
- **Default:** `0`

### `fallback-glyph`

Specifies whether to report when a glyph is found in a fallback font. When the glyph corresponding to the specified character in the font family is not found, and `auto-fallback-font` is specified, a fallback font will be looked for. Values specify the error reporting level:

- `0` — No error message will be reported.
- `1` — The level 1 error message will be reported.
- `2` — The level 2 error message will be reported.
- `3` — The level 3 error message will be reported.
- `4` — The level 4 error message will be reported.

- **Applies to:** `<font-settings>`
- **Values:** `0` | `1` | `2` | `3` | `4`
- **Default:** `1`

### `font-selection-mode`

Specifies the selection method of fonts:

- `5` — The setting of `font-selection-strategy` is disregarded and always considered `auto`.
- `6` — The first font that has a glyph is adopted.

See also Font Selection in the Technical Notes of the Online Manual.

- **Applies to:** `<font-settings>`
- **Values:** `5` | `6`
- **Default:** `6`

### `font-stretch-mode`

Specifies whether the information on `font-stretch` is used when selecting fonts:

- `5` — The information on `font-stretch` will not be used. The operation is the same as AH Formatter V5.
- `6` — The information on `font-stretch` will be used.

- **Applies to:** `<font-settings>`
- **Values:** `5` | `6`
- **Default:** `6`

### `missing-font`

Specifies whether to warn when a font is not found from the specified font family. Values specify the error reporting level:

- `0` — No error message will be reported.
- `1` — The level 1 error message will be reported.
- `2` — The level 2 error message will be reported.
- `3` — The level 3 error message will be reported.
- `4` — The level 4 error message will be reported.

- **Applies to:** `<font-settings>`
- **Values:** `0` | `1` | `2` | `3` | `4`
- **Default:** `1`

### `missing-glyph`

Specifies whether to warn when the glyph corresponding to the specified character is not found in the specified font family or the fallback font. Values specify the error reporting level:

- `0` — No error message will be reported.
- `1` — The level 1 error message will be reported.
- `2` — The level 2 error message will be reported.
- `3` — The level 3 error message will be reported.
- `4` — The level 4 error message will be reported.

- **Applies to:** `<font-settings>`
- **Values:** `0` | `1` | `2` | `3` | `4`
- **Default:** `1`

### `missing-glyph-all`

Usually the report on `missing-glyph` is given only once for the same character. By specifying `missing-glyph-all="true"`, the report can be given for all occurrences. Note that careless specification could cause a huge amount of errors. This setting is similarly applied to `fallback-glyph` as well.

- **Applies to:** `<font-settings>`
- **Values:** `true` | `false`
- **Default:** `false`

## Element: `<script-font>`

Specifies the script and the generic fonts to be used for each language family (e.g., for languages with the Latin alphabet). For multilingual processing, repeat this element according to the language requirements. In the default system setting, this element is set for a number of language families, for the languages with the Latin alphabet without specification of the `script` attribute.

**Parent:** `<font-settings>`

### Attributes

#### `script`

Specifies the script codes for multilingual setting. The available scripts conform to ISO 15924. However, AH Formatter V7.2 does not support all scripts. The scripts that can be specified here are scripts indicated in Scripts and Languages in the Overview of the Online Manual, excluding Hira, Kana, and Hani. For generic fonts you may omit the setting of the script or specify as `script=""`.

- **Applies to:** `<script-font>`
- **Values:** See Scripts and Languages in the Overview of the Online Manual
- **Default:** none

#### `serif`

Specifies the generic serif font when specified by the script.

- **Applies to:** `<script-font>`
- **Values:** `<family-name>`
- **Default:** none

#### `sans-serif`

Specifies the generic sans-serif font when specified by the script.

- **Applies to:** `<script-font>`
- **Values:** `<family-name>`
- **Default:** none

#### `monospace`

Specifies the generic monospace font when specified by the script.

- **Applies to:** `<script-font>`
- **Values:** `<family-name>`
- **Default:** none

#### `cursive`

Specifies the generic cursive font when specified by the script.

- **Applies to:** `<script-font>`
- **Values:** `<family-name>`
- **Default:** none

#### `fantasy`

Specifies the generic font for fantasy when specified by the script.

- **Applies to:** `<script-font>`
- **Values:** `<family-name>`
- **Default:** none

#### `fallback`

Specifies the fallback font of the script when specified by the script. Two or more fonts can be enumerated by comma-separated values.

- **Applies to:** `<script-font>`
- **Values:** `<family-name>`
- **Default:** none

## Element: `<font-alias>`

Formats the font name `src` (source) appearing in FO by replacing with `dst` (destination). This is achieved by specifying an arbitrary font name for `src` and `dst`. This makes it possible to substitute an unknown font in a document made in a different environment, without modifying the document.

Note: In the following configuration:

```xml
<font-alias src="A" dst="B"/>
<font-alias src="B" dst="C"/>
```

"A" would never be replaced with "C". Moreover, the setting for `<font-alias>` does not affect the font name in the Option file.

**Parent:** `<font-settings>`

### Attributes

#### `src`

The source font name to be replaced.

- **Applies to:** `<font-alias>`

#### `dst`

The destination font name to replace with.

- **Applies to:** `<font-alias>`
