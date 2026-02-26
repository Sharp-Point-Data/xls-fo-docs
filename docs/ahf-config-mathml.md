# Antenna House Configuration: MathML Settings

<!-- Source: XSL-FO-Reference-74-MID.pdf pp.275–276 -->

## Overview

The `<mathml-settings>` element configures MathML rendering in AH Formatter. It controls a wide range of parameters for mathematical typesetting, including script sizing, spacing, line breaking, operator styling, fractions, roots, enclosures, tables, and font variant mappings. For additional details, see MathML Conformance in Conformance of the Online Manual.

## Element: `<mathml-settings>`

**Parent:** `<formatter-config>`

**Child elements:** `<variant-font>`, `<operator-dictionary>`

## Attributes

### Script and Size Attributes

| Attribute | Description |
|-----------|-------------|
| `mathDisplay` | Controls the display style for math rendering |
| `scriptsizemultiplier` | Multiplier applied to font size for script-level changes |
| `scriptsizemultiplierMscarries` | Script size multiplier specific to `mscarries` elements |
| `scriptminsize` | Minimum font size for scripts |
| `scriptmaxsize` | Maximum font size for scripts |

### Operator and Large Operator Attributes

| Attribute | Description |
|-----------|-------------|
| `largeopmultiplier` | Size multiplier for large operators in display mode |
| `largeopmultiplierInt` | Size multiplier for integral large operators |

### Math Size Attributes

| Attribute | Description |
|-----------|-------------|
| `mathsizeSmall` | Size value for `mathsize="small"` |
| `mathsizeBig` | Size value for `mathsize="big"` |

### Space Attributes

| Attribute | Description |
|-----------|-------------|
| `enQuad` | Width of an en quad space |
| `emQuad` | Width of an em quad space |
| `enSpace` | Width of an en space |
| `emSpace` | Width of an em space |
| `thinSpace` | Width of a thin space |
| `hairSpace` | Width of a hair space |

### Math Space Attributes

| Attribute | Description |
|-----------|-------------|
| `veryverythinmathspace` | Very very thin math space width |
| `verythinmathspace` | Very thin math space width |
| `thinmathspace` | Thin math space width |
| `mediummathspace` | Medium math space width |
| `thickmathspace` | Thick math space width |
| `verythickmathspace` | Very thick math space width |
| `veryverythickmathspace` | Very very thick math space width |

### Layout and Spacing Defaults

| Attribute | Description |
|-----------|-------------|
| `accentOffset` | Offset for accents |
| `defaultLSpace` | Default left space for operators |
| `defaultRSpace` | Default right space for operators |
| `defaultMinsize` | Default minimum size |
| `defaultLineleading` | Default line leading |
| `mathLeading` | Leading for math content |

### Line Breaking Attributes

| Attribute | Description |
|-----------|-------------|
| `linebreakingHeightAdjust` | Height adjustment for line breaking |
| `indentingnewline` | Indentation for new lines in line breaking |

### Operator and Function Spacing

| Attribute | Description |
|-----------|-------------|
| `applyFunctionSpace` | Space around the apply-function operator |
| `invisibleTimesSpace` | Space around the invisible-times operator |

### Script Alignment

| Attribute | Description |
|-----------|-------------|
| `scriptAlignMode` | Alignment mode for scripts |
| `italicSubscriptShift` | Shift for subscripts in italic context |
| `integralSubscriptShift` | Subscript shift specific to integrals |
| `integralSuperscriptShift` | Superscript shift specific to integrals |
| `integralUnderOverShift` | Under/over shift specific to integrals |

### Line Thickness Attributes

| Attribute | Description |
|-----------|-------------|
| `thinLine` | Thickness for thin lines |
| `mediumLine` | Thickness for medium lines |
| `thickLine` | Thickness for thick lines |

### Fraction Attributes

| Attribute | Description |
|-----------|-------------|
| `fracLineExtend` | Extension of the fraction line beyond content |
| `fracLineSpace` | Space around the fraction line |
| `fracLineOverGap` | Gap between the fraction line and the numerator |
| `fracLineUnderGap` | Gap between the fraction line and the denominator |

### Bevelled Fraction Attributes

| Attribute | Description |
|-----------|-------------|
| `bevelledAngle` | Angle of the bevelled fraction bar |
| `bevelledHeight` | Height of the bevelled fraction bar |

### Root Attributes

| Attribute | Description |
|-----------|-------------|
| `rootPosition1x` | X position for root point 1 |
| `rootPosition1y` | Y position for root point 1 |
| `rootPosition2x` | X position for root point 2 |
| `rootPosition2y` | Y position for root point 2 |
| `rootPosition3x` | X position for root point 3 |
| `rootPosition3y` | Y position for root point 3 |
| `rootPosition4x` | X position for root point 4 |
| `rootPosition4y` | Y position for root point 4 |
| `rootThickness1` | Line thickness for root segment 1 |
| `rootThickness2` | Line thickness for root segment 2 |
| `rootThickness3` | Line thickness for root segment 3 |
| `rootThickness4` | Line thickness for root segment 4 |
| `rootRoundRadius` | Round radius for root symbol |

### Enclosure Attributes

| Attribute | Description |
|-----------|-------------|
| `encloseLineThickness` | Line thickness for enclosure notation |
| `encloseCircle` | Circle parameters for enclosure notation |
| `roundedboxRadius` | Radius for rounded box enclosure |

### Table Attributes

| Attribute | Description |
|-----------|-------------|
| `columnspacing` | Default column spacing in `mtable` |
| `rowspacing` | Default row spacing in `mtable` |
| `framespacing` | Default frame spacing in `mtable` |
| `columnlineThickness` | Thickness of column lines in `mtable` |
| `rowlineThickness` | Thickness of row lines in `mtable` |
| `framelineThickness` | Thickness of frame lines in `mtable` |

### Character Spacing Attributes

| Attribute | Description |
|-----------|-------------|
| `charspacingTight` | Character spacing for tight setting |
| `charspacingMedium` | Character spacing for medium setting |
| `charspacingLoose` | Character spacing for loose setting |

### Multiline Attributes

| Attribute | Description |
|-----------|-------------|
| `overlapMsline` | Overlap for `msline` elements |
| `mslineOverGap` | Gap above `msline` |
| `mslineUnderGap` | Gap below `msline` |
| `crossoutThickness` | Thickness of crossout lines |

### Rendering and Behavior Attributes

| Attribute | Description |
|-----------|-------------|
| `errorColor` | Color for error display in MathML |
| `errorBackground` | Background color for error display in MathML |
| `escapingMs` | Escaping behavior for `ms` element |
| `italicizeMi` | Whether to italicize single-character `mi` elements |
| `stylisticMi` | Stylistic handling of `mi` elements |
| `substKeyboardCharacters` | Whether to substitute keyboard characters with math equivalents |
| `pseudoScripts` | Handling of pseudo-script characters |
| `inheritFontweight` | Whether to inherit font weight in math context |
| `enableOpenTypeMATH` | Whether to enable OpenType MATH table support |
| `exceptOpenTypeMATHVariants` | Exceptions for OpenType MATH variant handling |
| `mathmlSettingsMode` | Mode for MathML settings processing |

## Element: `<variant-font>`

Specifies the font corresponding to `mathvariant`. Any number of this element can be specified. See also Fonts for Math Expression in the Online Manual.

**Parent:** `<mathml-settings>`

**Child elements:** `<font-entry>`

### Attributes

#### `mathvariant`

The `mathvariant` value this font mapping applies to.

- **Applies to:** `<variant-font>`

#### `fontfamily`

The font family to use for this math variant.

- **Applies to:** `<variant-font>`

#### `center-shift`

Shift value for centering the font vertically.

- **Applies to:** `<variant-font>`

## Element: `<font-entry>`

Specifies the font that corresponds to a script or Unicode Range. This setting can change a part of fonts specified by `fontfamily` of `<variant-font>`. Any number of this element can be specified.

Either `script` or `unicode-range` must be specified. The effect is not guaranteed when both are specified.

**Parent:** `<variant-font>`

### Attributes

#### `fontfamily`

The font family to use for this font entry.

- **Applies to:** `<font-entry>`

#### `script`

The script code (ISO 15924) this font entry applies to.

- **Applies to:** `<font-entry>`

#### `unicode-range`

The Unicode range this font entry applies to.

- **Applies to:** `<font-entry>`

#### `mathvariant`

The `mathvariant` value this font entry applies to.

- **Applies to:** `<font-entry>`

#### `center-shift`

Shift value for centering the font vertically.

- **Applies to:** `<font-entry>`

## Element: `<operator-dictionary>`

The `<operator-dictionary>` element is specified in order to change the contents of the default operator dictionary. Any number of this element can be specified and is evaluated in order. See also MathML Conformance in Conformance of the Online Manual to learn more about the operator dictionary.

**Parent:** `<mathml-settings>`
