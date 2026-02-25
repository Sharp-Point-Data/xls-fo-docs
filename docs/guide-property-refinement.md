# Property Refinement / Resolution

## Overview

Property refinement is the process by which the set of properties specified on a formatting object is transformed into a set of traits that constrain the formatting result. Every formatting property may be specified on every formatting object, but for each formatting object class only a subset of properties "apply" to that class.

During refinement, properties that apply to a formatting object are converted into traits. For many traits there is a one-to-one correspondence with a property; for other traits the transformation is more complex.

The refinement process proceeds in two main steps:

1. **Obtain the effective value** of each property that applies to the formatting object. Shorthand properties are expanded into individual properties. For any property not specified on the object, the inherited or initial value is used.
2. **Transform the property set into traits.**

> Note: Although the refinement process is described as a series of steps, this is solely for the convenience of exposition and does not imply they must be implemented as separate steps. A conforming implementation must only achieve the same effect.

<!-- Source: https://www.w3.org/TR/xslfo20/#refinement -->

## Specified, Computed, and Actual Values, and Inheritance

For every property applicable to a given formatting object, three variants of the property value are distinguished:

- **Specified value**: The value placed on the formatting object during tree construction. It may not be directly usable (e.g., it may be a percentage or expression).
- **Computed value**: The result of converting the specified value into an absolute form (e.g., resolving percentages, converting relative units like `em` to absolute values, replacing keywords like "smaller" or "bolder").
- **Actual value**: The computed value after adjustment for the output medium (e.g., rounding a line width to an integral number of device pixels).

<!-- Source: https://www.w3.org/TR/xslfo20/#speccomact -->

### Specified Values

The specified value of a property is determined using the following mechanisms, in order of precedence:

1. If the tree-construction process placed the property on the formatting object, use that value. This is called "explicit specification."
2. Otherwise, if the property is inheritable, use the computed value of that property from the parent formatting object.
3. Otherwise, use the property's initial value. If there is no initial value, the property is not specified on the formatting object (this is generally an error).

The root of the result tree has no parent, so when inheritance would apply, the initial value is used instead.

### Computed Values

Specified values may be:

- **Absolute** (e.g., "red", "2mm") -- no computation needed.
- **Relative** (e.g., "auto", "2em", "12%") -- must be transformed:
  - Percentages are multiplied by a reference value (defined per property).
  - Values with relative units (`em`) are made absolute by multiplying by the appropriate font size.
  - "auto" values are computed by the formulas given with each property.
  - Certain property values ("smaller", "bolder") are replaced per their definitions.

The computed value of any property controlling a border width where the border style is "none" is forced to "0pt".

**Corresponding properties**: Some properties can be specified either relative to the writing-mode (e.g., `padding-before`) or in absolute geometric terms (e.g., `padding-top`). These are called "corresponding properties." Specifying a value for one determines computed values for both. Which relative property corresponds to which absolute property depends on the `writing-mode`. For example, with `writing-mode="lr-tb"`, `padding-start` corresponds to `padding-left`; with `writing-mode="rl-tb"`, `padding-start` corresponds to `padding-right`.

In most cases, elements inherit computed values. However, some properties' specified values may be inherited (e.g., some values of `line-height`). This is noted in the property definition.

### Actual Values

A computed value is in principle ready to be used, but a user agent may not be able to make use of the value in a given environment. For example, a user agent may only render borders with integer pixel widths and may therefore adjust the computed width. The actual value is the computed value after such adjustments.

### Inheritance

Some properties are "inheritable" (identified in the property description). Inheritable properties propagate down the formatting object tree from parent to child. At the root of the result tree, inheritable properties are given their initial value.

For a given inheritable property: if that property is explicitly present on a child, that value is used for the child and its descendants (until re-set by a lower descendant). Otherwise, the specified value for the child is the computed value of that property on the parent formatting object. Thus there is always a specified value defined for every inheritable property on every formatting object.

<!-- Source: https://www.w3.org/TR/xslfo20/#inheritance -->

## Shorthand Expansion

XSL has two kinds of shorthand properties:

1. Those originating from CSS (e.g., `border`).
2. Those arising from breaking apart and/or combining CSS properties (e.g., `page-break-inside`).

Both types are handled the same way.

> Note: Shorthands are only included in the "complete" conformance level.

**Key rules for shorthand expansion:**

- Shorthand properties do not inherit from the shorthand on the parent. Instead, the individual properties that the shorthand expands into may inherit.
- When multiple interrelated shorthand properties or a shorthand and an interrelated individual property are specified, they are processed in increasing precision:
  - `border` is less precise than `border-top`, which is less precise than `border-top-color`.
  - Individual properties are always more precise than any shorthand.
  - `border-style`, `border-color`, `border-width` are less precise than `border-top`, `border-bottom`, `border-right`, `border-left`.

**Processing steps (conceptual):**

1. Set the effective value of all properties to their initial values.
2. Process all shorthands in increasing precision:
   - If the shorthand is "inherit": set each property the shorthand covers to the computed value of the corresponding property on the parent.
   - Otherwise: determine which individual properties are to be set and replace the initial value with the computed value derived from the specified value.
3. Process all specified individual properties.
4. Carry out inheritance for any properties that were not given a value other than by step 1.

> Note: For example, if both `background` and `background-color` are specified on a formatting object, process the `background` shorthand first, then process the `background-color` property.

<!-- Source: https://www.w3.org/TR/xslfo20/#shortexpan -->

## Computing the Values of Corresponding Properties

Where there are corresponding properties (e.g., `padding-left` and `padding-start`), a computed value is determined for all corresponding properties. How the computed values are determined depends on which of the corresponding properties are specified on the object.

The correspondence mapping from absolute to relative property depends on the `writing-mode`:

- If `writing-mode` specifies a block-progression-direction of **top-to-bottom**: "top" maps to "before", "bottom" maps to "after".
- If `writing-mode` specifies a block-progression-direction of **bottom-to-top**: "top" maps to "after", "bottom" maps to "before".
- If `writing-mode` specifies a block-progression-direction of **left-to-right**: "left" maps to "before", "right" maps to "after".
- If `writing-mode` specifies a block-progression-direction of **right-to-left**: "left" maps to "after", "right" maps to "before".
- If `writing-mode` specifies an inline-progression-direction of **left-to-right**: "left" maps to "start", "right" maps to "end".
- If `writing-mode` specifies an inline-progression-direction of **right-to-left**: "left" maps to "end", "right" maps to "start".
- If `writing-mode` specifies an inline-progression-direction of **top-to-bottom**: "top" maps to "start", "bottom" maps to "end".
- If `writing-mode` specifies an inline-progression-direction of **bottom-to-top**: "top" maps to "end", "bottom" maps to "start".
- If `writing-mode` specifies an inline-progression-direction of **left-to-right for odd-numbered lines, right-to-left for even-numbered lines**: "left" maps to "start", "right" maps to "end".

> Note: `reference-orientation` is a rotation and does not influence the correspondence mapping.

<!-- Source: https://www.w3.org/TR/xslfo20/#compcorr -->

### Border and Padding Properties

The simplest class of corresponding properties are those with only two variants (absolute and relative) where the names differ only in the absolute/relative designation (e.g., `border-left-color` and `border-start-color`).

**Rules for determining computed values:**

- If the absolute variant is specified on the formatting object, its computed value sets the corresponding relative property's computed value.
- If the absolute property is not explicitly specified, the absolute property's computed value is set from the corresponding relative property's computed value.
- If the relative property is specified and the absolute property is only specified by shorthand expansion, the absolute property's computed value is set from the relative property's computed value.
- If neither is explicitly specified, inheritance or initial values apply. The initial value must be the same for all possible corresponding properties.
- If both are explicitly specified, the absolute property takes precedence, and the relative property's specified value is ignored.

The properties using this rule:

- `border-after-color`, `border-before-color`, `border-end-color`, `border-start-color`
- `border-after-style`, `border-before-style`, `border-end-style`, `border-start-style`
- `border-after-width`, `border-before-width`, `border-end-width`, `border-start-width`
- `padding-after`, `padding-before`, `padding-end`, `padding-start`

<!-- Source: https://www.w3.org/TR/xslfo20/#refine-border-padding -->

### Margin, Space, and Indent Properties

The `space-before` and `space-after` properties (block-level) and `space-start` and `space-end` properties (inline-level) are handled similarly to border/padding corresponding properties, but their corresponding absolute properties are `margin-top`, `margin-bottom`, `margin-left`, and `margin-right`.

The `.conditionality` component of any `space-before` or `space-after` determined from a margin property is set to "retain" (for CSS2 compatibility).

> Note: The computed value of a CSS2 margin in the block-progression-dimension specified as "auto" is 0pt. Any space-before or space-after determined from a margin value of "auto" is set to 0pt.

**`start-indent` and `end-indent` (block-level formatting objects):**

These correspond to various absolute margin properties but the correspondence is more complex, involving border-width and padding properties.

**When the absolute margin property is specified and the formatting object generates a reference area:**

```
start-indent = margin-corresponding + padding-corresponding + border-corresponding-width
end-indent = margin-corresponding + padding-corresponding + border-corresponding-width
```

**When the absolute margin property is specified and the formatting object does not generate a reference area:**

```
start-indent = inherited_value_of(start-indent) + margin-corresponding + padding-corresponding + border-corresponding-width
end-indent = inherited_value_of(end-indent) + margin-corresponding + padding-corresponding + border-corresponding-width
```

**When the absolute margin is not explicitly specified, or the relative property is specified and the absolute property is only from shorthand expansion:**

```
margin-corresponding = start-indent - inherited_value_of(start-indent) - padding-corresponding - border-corresponding-width
margin-corresponding = end-indent - inherited_value_of(end-indent) - padding-corresponding - border-corresponding-width
```

> Note: If `start-indent` or `end-indent` properties are not specified, their inherited value is used in these formulae.

<!-- Source: https://www.w3.org/TR/xslfo20/#refine-margin-space-indent -->

### Height and Width Properties

Based on the `writing-mode` in effect, either the `height`/`min-height`/`max-height` properties or the `width`/`min-width`/`max-width` properties are converted to the corresponding `block-progression-dimension` or `inline-progression-dimension`.

The `height` properties are absolute and indicate the dimension from "top" to "bottom"; the `width` properties indicate the dimension from "left" to "right".

**When `writing-mode` specifies a block-progression-direction of "top-to-bottom" or "bottom-to-top":**

- `height` properties map to `block-progression-dimension`
- `width` properties map to `inline-progression-dimension`

**When `writing-mode` specifies a block-progression-direction of "left-to-right" or "right-to-left":**

- `height` properties map to `inline-progression-dimension`
- `width` properties map to `block-progression-dimension`

For each dimension, the conversion proceeds as:

1. If the base property (e.g., `height`) is specified, set `.minimum`, `.optimum`, and `.maximum` to that value. If not specified, set all three to "auto".
2. If `min-height` (or `min-width`) is specified, reset `.minimum` to that value.
3. If `max-height` (or `max-width`) is specified, reset `.maximum` to that value. If `max-height`/`max-width` is "none", reset `.maximum` to "auto".

### Overconstrained Geometry

The sum of `start-indent`, `end-indent`, and the `inline-progression-dimension` of the content-rectangle of an area should equal the `inline-progression-dimension` of the content-rectangle of the closest ancestor reference-area. When the specification leads to them being different, the `end-indent` (and thus the corresponding margin) is adjusted to make the equality hold.

<!-- Source: https://www.w3.org/TR/xslfo20/#overcons_geom -->

## Simple Property to Trait Mapping

The majority of properties map into traits of the same name and simply copy the value. These are classified as "Rendering", "Formatting", "Specification", "Font selection", "Reference", and "Action" in the property table.

For example, `font-style="italic"` is refined into a `font-style` trait with a value of "italic".

Some traits have a value different from the property value (classified as "Value change"). The details for these are:

### Background-position-horizontal and Background-position-vertical Properties

A value of "top", "bottom", "left", "right", or "center" is converted to a length as specified in the property definition.

### Column-number Property

If a value has not been specified on a formatting object to which this property applies, the initial value is computed as specified in the property definition.

### Text-align Property

A value of "left" or "right" is converted to the writing-mode relative value as specified in the property definition.

### Text-align-last Property

A value of "left" or "right" is converted to the writing-mode relative value as specified in the property definition.

### z-index Property

The value is converted to an absolute value: the refined value is the specified value plus the refined value of `z-index` of the parent formatting object, if any.

### Language Property

A 2-letter ISO 639 code is converted to the corresponding 3-letter ISO 639-2 terminology code. A 3-letter ISO 639-2 bibliographic code is converted to the corresponding 3-letter terminology code. A value of "none" or "mul" is converted to "und".

## Complex Property to Trait Mapping

A small number of properties influence traits in a more complex manner.

### Word Spacing and Letter Spacing Properties

These properties may set values for the `space-start` and `space-end` traits, as described in the property definitions.

### Reference-orientation Property

The `reference-orientation` trait is copied from the `reference-orientation` property during refinement. During composition, an absolute orientation is determined.

<!-- Source: https://www.w3.org/TR/xslfo20/#refine-reference-orientation -->

### Writing-mode and Direction Properties

The `writing-mode`, `direction`, and `unicode-bidi` traits are copied from the properties of the same name during refinement. During composition, these are used in the determination of absolute orientations for the `block-progression-direction`, `inline-progression-direction`, and `shift-direction` traits.

<!-- Source: https://www.w3.org/TR/xslfo20/#refine-writing-mode -->

### Absolute-position Property

If `absolute-position` has the value "absolute" or "fixed", the values of the `left-position`, `top-position`, etc. traits are copied directly from the `left`, `top`, etc. properties. Otherwise, these traits' values are left undefined during refinement and determined during composition.

<!-- Source: https://www.w3.org/TR/xslfo20/#refine-absolute-pos -->

### Relative-position Property

If `relative-position` has the value "relative":

- The `left-offset` trait is copied from the `left` property. If `right` is specified but `left` is not, `left-offset` is set to the negative of `right`. If neither `left` nor `right` is specified, `left-offset` is 0.
- The `top-offset` trait is copied from the `top` property. If `bottom` is specified but `top` is not, `top-offset` is set to the negative of `bottom`. If neither `top` nor `bottom` is specified, `top-offset` is 0.

<!-- Source: https://www.w3.org/TR/xslfo20/#refine-relative-pos -->

### Text-decoration Property

The `text-decoration` property value provides values for the `blink` trait and a set of score and score-color traits. The "specified color" is the value of the `color` trait of the formatting object for which `text-decoration` is being refined.

Token-to-trait mapping:

| Token | Trait set to "true" | Color trait set |
|---|---|---|
| `underline` | `underline-score` | `underline-score-color` = specified color |
| `overline` | `overline-score` | `overline-score-color` = specified color |
| `line-through` | `through-score` | `through-score-color` = specified color |
| `blink` | `blink` | (none) |
| `no-underline` | `underline-score` = false | `underline-score-color` = specified color |
| `no-overline` | `overline-score` = false | `overline-score-color` = specified color |
| `no-line-through` | `through-score` = false | `through-score-color` = specified color |
| `no-blink` | `blink` = false | (none) |

<!-- Source: https://www.w3.org/TR/xslfo20/#refine-text-decoration -->

### Font Properties

Font traits on an area are indirectly derived from the combination of font properties (used to select a font) and font tables from that font.

There is no XSL mechanism to specify a particular font. Instead, a "selected font" is chosen from available fonts based on selection criteria: `font-family`, `font-style`, `font-variant`, `font-weight`, `font-stretch`, `font-size`, and (for some formatting objects) one or more characters. The `font-selection-strategy` property controls the selection algorithm.

The `nominal-font` trait is set to the selected font. If no font is selected and the "missing character" glyph is displayed, `nominal-font` is set to the font containing that glyph.

The `dominant-baseline-identifier` and `actual-baseline-table` traits are derived from the `dominant-baseline` property value, which is a compound value with three components:

1. A baseline-identifier for the dominant-baseline.
2. A baseline-table.
3. A baseline-table font-size used to scale baseline positions.

The baseline-table font-size scales the baseline positions, and the dominant-baseline position is subtracted from other baseline positions to yield the `actual-baseline-table` trait (a table of offsets from the dominant baseline).

<!-- Source: https://www.w3.org/TR/xslfo20/#fontprops -->

### Fonts and Font Data

XSL uses an abstract font model based on current font technology (OpenType). A font consists of:

- **Glyphs**: Recognizable abstract graphic symbols independent of specific design.
- **Font tables**: Information necessary to map characters to glyphs, determine glyph area sizes, and position glyph areas.

Font table characteristics include `font-weight`, font-style, etc. Geometric font characteristics are expressed in a coordinate system based on the **em box** (1 em high, 1 em wide). Points in this design space are expressed as fractional units of the em.

> Note: Most often, the (0,0) point is positioned on the left edge of the em box, but not at the bottom left corner. The Y coordinate of the bottom of a Roman capital letter is usually zero, and descenders have negative coordinate values.

XSL requires at least three font characteristics from font tables: an **ascent** (top of em box), a **descent** (bottom of em box), and a set of **baseline-tables**.

**Baselines and alignment**: The script to which a glyph belongs determines an alignment-baseline for that glyph. Within a script and a single font-size, the sequence of alignment-points defines a geometric line called a "baseline." Western/alphabetic glyphs align to the "alphabetic" baseline; certain Indic glyphs (Devanagari, Gurmukhi, Bengali) align to the "hanging" baseline; Far Eastern glyphs align to the "ideographic" baseline.

A **baseline-table** specifies positions of one or more baselines in design space coordinates. Because desired alignments depend on the dominant script, there may be different baseline tables per script. Fonts may have baseline tables for horizontal writing-modes and for vertical writing-modes.

Per-glyph font data includes (for each glyph): one width value, one alignment-baseline, and one alignment-point for horizontal writing-modes. If vertical writing-modes are supported, another set of these is required.

> Note: If font tables do not define required values, heuristics may be used to approximate them.

<!-- Source: https://www.w3.org/TR/xslfo20/#font-model -->

## Non-property Based Trait Generation

The `is-reference-area` trait is set to "true" for specific formatting objects (explicitly identified in those formatting objects' descriptions). For all other formatting objects it is set to "false".

## Property Based Transformations

### Text-transform Property

The case changes specified by `text-transform` are carried out during refinement by changing the value of the `character` property appropriately.

> Note: The use of `text-transform` is deprecated in XSL due to severe internationalization issues.

## Alignment Properties

The area alignment properties control the alignment of child areas with respect to their parent areas. The parent area is given a frame of reference through its **scaled-baseline-table**.

A scaled-baseline-table is a compound value with three components:

1. A **baseline-identifier** for the dominant-baseline.
2. A **derived baseline-table** with positions for baselines expressed in design space coordinates.
3. A **baseline-table font-size** used to scale the baseline positions.

<!-- Source: https://www.w3.org/TR/xslfo20/#alignmentproperties.intro -->

### Baseline Identifiers

The following baseline-identifiers are used in XSL-FO. Some are determined by baseline-tables in a font; others are computed from font characteristics:

- **alphabetic**: Used by most alphabetic and syllabic scripts (Western, Southern Indic, Southeast Asian non-ideographic).
- **ideographic**: Used by ideographic scripts (Chinese, Japanese, Korean, Vietnamese Chu Nom). Positioned at the bottom of the ideographic em box (not the center).
- **hanging**: Used by certain Indic scripts (Devanagari, Gurmukhi, Bengali).
- **mathematical**: Used by mathematical symbols.
- **central**: Computed baseline at the center of the em box, halfway between text-before-edge and text-after-edge.
- **middle**: Offset from the alphabetic baseline in the shift-direction by 1/2 the x-height. May be obtained from font data or computed. Lacking data, may be approximated by the "central" baseline.
- **text-before-edge**: The before-edge of the em box. Normally around or at the top of ascenders. For ideographic fonts, normally 1 em in the shift-direction from the ideographic baseline.
- **text-after-edge**: The after-edge of the em box. For fonts with descenders, normally around or at the bottom of descenders. For ideographic fonts, normally at the ideographic baseline.

Two additional computed baselines are defined only for line areas:

- **before-edge**: Determined by ignoring all inline-areas aligned to "before-edge" or "after-edge". The offset is set to the maximum extent of the before-edges of the remaining areas' allocation-rectangles (measured from the dominant-baseline toward the top of the reference-area). If all inline-areas are aligned to "before-edge" or "after-edge", the "text-before-edge" baseline offset is used.
- **after-edge**: Determined by ignoring all inline-areas aligned to "after-edge". The offset is the negative of the maximum of: (1) the maximum extent of after-edges of remaining areas' allocation-rectangles, and (2) the maximum height of allocation-rectangles of ignored areas minus the before-edge baseline offset.

### Four Alignment Properties

The alignment of a formatting object with respect to its parent is determined by three things: the scaled-baseline-table of the parent, the `alignment-baseline` of the child, and the alignment-point of the child. The four alignment properties are independent and typically only one needs to be specified:

1. **`dominant-baseline`**: The primary alignment property. A compound value with three components:
   - The dominant-baseline-identifier (default alignment-baseline for aligning two inline-areas).
   - The baseline-table (defines positions along block-progression-direction).
   - The baseline-table font-size (scaling factor).

2. **`alignment-baseline`**: The primary control on positioning an inner formatting object with respect to its parent. Initial value for non-`fo:character` is "baseline", aligning the dominant-baseline of the inner object with the dominant-baseline of the outer object.

3. **`baseline-shift`**: Does not change the baseline-table or font-size, but shifts the whole baseline-table of the parent so that an aligned inner object is repositioned. Useful for superscripts and subscripts.

4. **`alignment-adjust`**: Primarily used for objects (like some graphics) that do not belong to a particular script and have no predefined alignment point. Allows the author to assign where, on the start-edge, the alignment point lies.

## Ruby

Ruby is small-sized, supplementary text attached to a character or group of characters in the main text. This section is generally written for Japanese text, although ruby can be used with other languages and writing systems.

In Japanese, a run of ruby text is usually attached to the right of characters in vertical writing mode or immediately above them in horizontal writing mode. It indicates the reading or meaning of those characters. The annotated main text characters are called "base characters." Kana characters used as ruby to indicate how to read kanji characters is known as "furigana."

See http://www.w3.org/TR/jlreq/#en-subheading2_3_1

### Block and Line-related Properties for Ruby

The `line-stacking-annotation` property determines the line stacking method for block elements containing annotation areas such as from ruby or emphasis dots.

<!-- Source: https://www.w3.org/TR/xslfo20/#rubydef -->

## Composition

The following subsections describe areas of the composition process that are noted for future or enhanced specification.

### Improved Font Support

The XSL-FO specification aims to align with CSS, SVG, and the emerging consensus on Web fonts for downloadable font support. Future drafts are likely to contain more detailed specifications in this area.

### Force Line Justification

Allows a user to force line justification when the line length is within a certain range. For example, normally the last line of a paragraph would not be justified, but if the last line is longer than a certain threshold, a user may want to justify it anyway.

### Alignment Around Breaks

Properties to specify what the alignment should be for the "last line before a break" and the "first line after a break."

### Tabs and Tab Stops

Support for tabs and tab stops as per word processors. Compatibility with other formats, mainly word processor formats, is seen as important.

### Word and Letter Spacing

Allows users to specify the priority between word and letter spacing.

### Hyphenation and Line Breaking

Supports the specification of the number of syllables in addition to the number of characters to control hyphenation.

<!-- Source: https://www.w3.org/TR/xslfo20/#composition -->

## Formatting Properties Introduction

### Description of Property Groups

XSL formatting properties are organized as follows:

**Nine common property groups** (referenced by group name in formatting object descriptions):

1. **Common Accessibility Properties** -- support accessibility.
2. **Common Absolute Position Properties** -- control position and size of absolutely positioned areas.
3. **Common Aural Properties** -- control aural rendition of content.
4. **Common Border, Padding, and Background Properties** -- control backgrounds and borders on block-areas and inline-areas.
5. **Common Font Properties** -- control font selection on formatting objects that contain text.
6. **Common Hyphenation Properties** -- control hyphenation for line-breaking (including `language`, `script`, `country`).
7. **Common Margin Properties-Block** -- set spacing and indents around block-level objects.
8. **Common Margin Properties-Inline** -- set spacing around inline-level objects.
9. **Common Relative Position Properties** -- control relatively positioned areas.

**Additional property clusters** (referenced individually):

- Area Alignment Properties
- Area Dimension Properties
- Block and Line-related Properties
- Character Properties
- Color-related Properties
- Float-related Properties
- Keeps and Breaks Properties
- Layout-related Properties
- Leader and Rule Properties
- Properties for Dynamic Effects
- Properties for Indexing
- Properties for Markers
- Properties for Number to String Conversions
- Pagination and Layout Properties
- Table Properties
- Writing-mode-related Properties
- Miscellaneous Properties
- Shorthand Properties (complete conformance set only)

<!-- Source: https://www.w3.org/TR/xslfo20/#pr-section -->

### XSL Areas and the CSS Box Model

Property descriptions that incorporate CSS2 definitions use the following correspondence:

- CSS "boxes" correspond to XSL "areas."
- CSS "elements" correspond to XSL "formatting objects."
- A CSS "positioned element" corresponds to an XSL FO with `absolute-position` having a computed value other than "auto" and/or `relative-position` having a computed value other than "static."

> Note: Since `position` is a shorthand for `absolute-position` and `relative-position` in XSL, this is equivalent to the CSS definition.

The position and size of a box refer to the area's content-rectangle. The full correspondence table:

| CSS Box Model | XSL Area Model |
|---|---|
| top content edge | top edge of the content-rectangle |
| padding edge | padding-rectangle |
| content area | interior of the content-rectangle |
| padding area | region between content-rectangle and padding-rectangle |
| border area | region between padding-rectangle and border-rectangle |
| background | background |
| containing block | closest ancestor block-area that is not a line-area |
| caption | area generated by `fo:table-caption` |
| inline box | inline-area |
| line box | line-area |
| block box | block-area which is not a line-area |
| page box | page-area |

Box margins map to area traits in accordance with the refinement rules described above.

<!-- Source: https://www.w3.org/TR/xslfo20/#cssbox -->

### Reference Rectangle for Percentage Computations

Percentage conversions, specified on each property definition, typically reference the content-rectangle of some area. That area is determined as follows:

1. For CSS2-defined properties referring to the "containing block": the content-rectangle of the closest ancestor block-area that is not a line-area.
2. For XSL-defined properties: the property definition specifies which area's content-rectangle is used.
3. Exceptions:
   - On `fo:root`, `fo:page-sequence`, `fo:title` (and descendants of `fo:title` with no ancestor block-area): the rectangle has dimensions of the "auto" value of `page-height` and `page-width`. The `block-progression-dimension` and `inline-progression-dimension` are determined by `reference-orientation` and `writing-mode`.
   - On `fo:static-content` and `fo:flow`: the content rectangle of the region on the first page into which content is directed (normal-flow-reference-area for region-body, region-reference-area for other regions).
   - On `fo:footnote-body` and `fo:float` with area-class "xsl-before-float": the content rectangle of the footnote-reference-area and before-float-reference-area respectively.
   - On `fo:float` with area-class "xsl-side-float": the closest ancestor block-area (not a line-area) of the "xsl-anchor" area generated by the `fo:float`.
   - When `absolute-position` is "fixed": the containing block is the nearest ancestor viewport area (or user agent default).
   - When `absolute-position` is "absolute": the containing block is the nearest ancestor area with area-class different from xsl-normal or `relative-position` of "relative". For block-areas, the padding-rectangle is used. For inline-areas, a virtual rectangle spanning from the before-edge/start-edge of the first area to the after-edge/end-edge of the last area is used (this rectangle may have negative extent).
4. If the formatting object generates a sequence of areas, the first area is used for the conversion.

<!-- Source: https://www.w3.org/TR/xslfo20/#percrule -->

### Additional CSS Datatypes

The following CSS datatypes are notational shorthands used in some CSS2 property definitions (not considered XSL datatypes):

| Datatype | Expansion |
|---|---|
| `<padding-width>` | `<length>` \| `<percentage>` |
| `<border-width>` | thin \| medium \| thick \| `<length>` |
| `<border-style>` | none \| hidden \| dotted \| dashed \| solid \| double \| groove \| ridge \| inset \| outset |
| `<generic-voice>` | 'male' \| 'female' \| 'child' |
| `<specific-voice>` | values are specific instances (e.g., comedian, trinoids, carlos, lani) |
| `<margin-width>` | `<length>` \| `<percentage>` \| auto |
| `<background-color>` | shorthand component of background-color |
| `<background-image>` | shorthand component of background-image |
| `<background-repeat>` | shorthand component of background-repeat |
| `<background-attachment>` | shorthand component of background-attachment |
| `<background-position>` | shorthand component of background-position |
| `<cue-before>` | shorthand component of cue-before |
| `<cue-after>` | shorthand component of cue-after |
| `<line-height>` | shorthand component of line-height |
| `<language-country>` | `<string>`: a language and optionally a country specifier per RFC 3066 |

<!-- Source: https://www.w3.org/TR/xslfo20/#cssdatat -->

## Code Samples

### Sample: Simple Inline Alignment (Latin-Latin)

<!-- Source: https://www.w3.org/TR/xslfo20/#alignmentproperties.intro -->
```xml
<fo:inline>Apex <fo:inline>Top</fo:inline></fo:inline>
```

Two inline formatting objects (one nested inside the other) with no properties specified, so initial values apply. In horizontal writing-mode, the dominant-baseline-identifier is "alphabetic" and the baseline-table is taken from the nominal-font for the block. Both Latin glyphs are aligned on the "alphabetic" baseline. The initial value of `alignment-baseline` ("baseline") aligns the dominant-baseline of the inner object with the dominant-baseline of the outer object.

### Sample: Mixed Script Alignment (Latin-Gurmukhi)

<!-- Source: https://www.w3.org/TR/xslfo20/#alignmentproperties.intro -->
```xml
<fo:inline>Apex <fo:inline><emph>guru</emph></fo:inline></fo:inline>
```

The inner inline contains Gurmukhi glyphs (symbolized as italic Latin transliteration). The Gurmukhi glyphs are aligned to the "hanging" baseline of the inner object, while the inline formatting object itself is still aligned on the dominant ("alphabetic") baseline relative to the outer object.

### Sample: Reduced Font-size Without Baseline Reset

<!-- Source: https://www.w3.org/TR/xslfo20/#alignmentproperties.intro -->
```xml
<fo:inline>Ap<emph>guru</emph>
  <fo:inline font-size='.75em'>
    Ex<emph>ji</emph>
  </fo:inline>
</fo:inline>
```

The inner inline has a reduced font-size. The alignment of the inner formatting object does not change, nor does the alignment of glyphs inside it. Latin glyphs align to "alphabetic" and Gurmukhi glyphs to "hanging." Changing `font-size` alone does not change the baseline-table in effect.

### Sample: dominant-baseline='reset-size'

<!-- Source: https://www.w3.org/TR/xslfo20/#alignmentproperties.intro -->
```xml
<fo:inline>Ap<emph>guru</emph>
  <fo:inline font-size='.75em'
             dominant-baseline='reset-size'>
     Ex<emph>ji</emph>
  </fo:inline>
</fo:inline>
```

The `dominant-baseline='reset-size'` rescales the baseline-table of the inner inline to match its (reduced) font-size. The alignment between inner and outer objects is still on the dominant baseline, but the smaller glyphs now align with each other using the rescaled baseline-table.

### Sample: dominant-baseline='hanging' on Outer Inline

<!-- Source: https://www.w3.org/TR/xslfo20/#alignmentproperties.intro -->
```xml
<fo:inline dominant-baseline='hanging'>Ap<emph>guru</emph>
  <fo:inline font-size='.75em'
             dominant-baseline='reset-size'>
     Ex<emph>ji</emph>
  </fo:inline>
</fo:inline>
```

The "hanging" baseline becomes the dominant baseline. The initial value of `alignment-baseline` ("baseline") causes the (now dominant) "hanging" baselines to be aligned between inner and outer objects. This ensures the small Gurmukhi glyphs align with the large Gurmukhi glyphs.

### Sample: alignment-baseline='hanging' on Inner Inline

<!-- Source: https://www.w3.org/TR/xslfo20/#alignmentproperties.intro -->
```xml
<fo:inline>Ap<emph>guru</emph>
  <fo:inline font-size='.75em'
             dominant-baseline='reset-size'
             alignment-baseline='hanging'>
     Ex<emph>ji</emph>
  </fo:inline>
</fo:inline>
```

Instead of changing the dominant baseline, the inner inline is explicitly aligned on its "hanging" baseline. This achieves the same visual effect as the previous example without changing the dominant-baseline of the outer inline.

### Sample: baseline-shift='super'

<!-- Source: https://www.w3.org/TR/xslfo20/#alignmentproperties.intro -->
```xml
<fo:inline>Ap
  <fo:inline baseline-shift='super'>1<emph>ji</emph></fo:inline>
</fo:inline>
```

The `baseline-shift='super'` shifts the whole baseline-table of the parent so the inner inline is positioned at the superscript position. Because the entire set of baseline-table staff lines are shifted, it does not matter to which baseline individual glyphs align: the European number "1" aligns to "alphabetic" and the Gurmukhi syllable "ji" aligns to "hanging."

### Sample: font-size Change with baseline-shift='super'

<!-- Source: https://www.w3.org/TR/xslfo20/#alignmentproperties.intro -->
```xml
<fo:inline>Ap
  <fo:inline font-size='.75em'
             baseline-shift='super'>
    1<emph>ji</emph>
  </fo:inline>
</fo:inline>
```

Because changing the font-size on a superscript/subscript is common, this is the one case where changing `font-size` does cause the baseline-table font-size to be reset even when `dominant-baseline` has its initial value. After rescaling, the default alignment to the dominant baseline positions the superscript inline formatting object relative to the shifted baseline-table.

### Sample: inherited-property-value() Function

<!-- Source: https://www.w3.org/TR/xslfo20/#expr-color-functions -->
```xml
<fo:list-block>
  ...
  <fo:list-item color="red">
    <fo:list-item-body background-color="green">
      <fo:block background-color="inherited-property-value(color)">
      </fo:block>
    </fo:list-item-body>
  </fo:list-item>
</fo:list-block>
```

The `background-color` on the `fo:block` is assigned the value "red" because the computed (after inheritance) value of the `color` property (not `background-color`) on the parent `fo:list-item-body` is "red."

### Sample: writing-mode on Region Definition (Complete Document)

<!-- Source: https://www.w3.org/TR/xslfo20/#expr-color-functions -->
```xml
<fo:root>

<fo:layout-master-set>
  <fo:simple-page-master master-name="all-pages">
    <fo:region-body region-name="xsl-region-body" margin="0.75in"
                    writing-mode="tb-rl" />
    <fo:region-before region-name="xsl-region-before" extent="0.75in"/>
  </fo:simple-page-master>
  <fo:page-sequence-master master-name="default-sequence">
    <fo:repeatable-page-master-reference master-reference="all-pages"/>
  </fo:page-sequence-master>
</fo:layout-master-set>

<fo:page-sequence master-name="default-sequence">
  <fo:flow flow-name="xsl-region-body">
    <fo:block>
        [Content in a language which allows either
         horizontal or vertical formatting]
    </fo:block>
  </fo:flow>
</fo:page-sequence>

</fo:root>
```

This example shows a simple page layout with a single `fo:simple-page-master` having two regions. The `writing-mode="tb-rl"` on the region-body definition has no effect on the writing-mode used for content, because the writing-mode used when generating the region viewport/reference area pair comes from the computed value on the `fo:page-sequence`. Since no `writing-mode` is specified on either `fo:root` or `fo:page-sequence`, the initial value "lr-tb" is used.

### Sample: fo:page-sequence Without from-page-master-region()

<!-- Source: https://www.w3.org/TR/xslfo20/#expr-color-functions -->
```xml
<fo:page-sequence master-name="default-sequence">
```

This is the original `fo:page-sequence` line from the previous example, using the inherited `writing-mode` (which defaults to "lr-tb").

### Sample: fo:page-sequence With from-page-master-region()

<!-- Source: https://www.w3.org/TR/xslfo20/#expr-color-functions -->
```xml
<fo:page-sequence master-name="default-sequence"
                  writing-mode="from-page-master-region()">
```

When `writing-mode="from-page-master-region()"` is specified on `fo:page-sequence`, the computed value of `writing-mode` from each region definition is used when instantiating viewport/reference area pairs. For xsl-region-body, this picks up "tb-rl" from the region definition, giving the content vertical formatting. For xsl-region-before, the inherited initial value "lr-tb" is used, giving horizontal formatting.

## See Also

- `guide-area-model.md` -- Area model fundamentals and area types
- `guide-expressions.md` -- Expression language and core function library
- `guide-datatypes.md` -- Property datatypes (compound values, spaces, keeps)
- `guide-bidi.md` -- Unicode BIDI processing (refinement step for bidirectional text)
- `guide-numbering.md` -- Formatter-based numbering
- `properties-writing-mode.md` -- Writing-mode related properties
- `properties-font.md` -- Font selection properties
- `properties-alignment.md` -- Alignment properties (dominant-baseline, alignment-baseline, baseline-shift, alignment-adjust)
