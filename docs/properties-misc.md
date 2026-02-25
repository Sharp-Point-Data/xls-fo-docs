# Miscellaneous Properties

## Overview

These properties cover a range of functionality that does not fit neatly into other property groups: unique identifiers, cross-references, external resource references, change bars, list label spacing, content type identification, visibility, stacking order, base URIs, and more.

<!-- Source: https://www.w3.org/TR/xslfo20/#change-bar-class -->

## Properties

### change-bar-class

| Field | Value |
|---|---|
| **Values** | `<name>` |
| **Initial** | none, value required |
| **Applies to** | fo:change-bar-begin, fo:change-bar-end |
| **Inherited** | No |
| **Conformance** | Extended |

<!-- Source: https://www.w3.org/TR/xslfo20/#change-bar-class -->

A name to allow pairing of `fo:change-bar-begin` and `fo:change-bar-end` elements.

This property associates a name with an `fo:change-bar-begin` or `fo:change-bar-end` element so that they can be matched to each other even if other `fo:change-bar-begin` and `fo:change-bar-end` elements are interspersed. This allows for "straddling pairs" of these elements.

### change-bar-color

| Field | Value |
|---|---|
| **Values** | `<color>` |
| **Initial** | the value of the `color` property |
| **Applies to** | fo:change-bar-begin |
| **Inherited** | Yes |
| **Conformance** | Extended |

<!-- Source: https://www.w3.org/TR/xslfo20/#change-bar-color -->

Specifies the color of the change bar.

Note: The color of any change bar is determined by the value of this property at the `fo:change-bar-begin` that starts the change bar; changes to this property after that do not affect the color of the change bar begin generated.

### change-bar-offset

| Field | Value |
|---|---|
| **Values** | `<length>` |
| **Initial** | `6pt` |
| **Applies to** | fo:change-bar-begin |
| **Inherited** | Yes |
| **Conformance** | Extended |

<!-- Source: https://www.w3.org/TR/xslfo20/#change-bar-offset -->

Gives the distance from the edge of the column area containing the text that is marked as changed to the center of the generated change bar. A positive distance is directed away from the column region and into the margin regardless of the change-bar-placement.

Note: The offset of any change bar is determined by the value of this property at the `fo:change-bar-begin` that starts the change bar; changes to this property after that do not affect the offset of the change bar begin generated.

Note: Relative lengths (i.e., percentage values and lengths with units of "em" or "ex") are not permitted for the value of this property.

### change-bar-placement

| Field | Value |
|---|---|
| **Values** | `start \| end \| left \| right \| inside \| outside \| alternate` |
| **Initial** | `start` |
| **Applies to** | fo:change-bar-begin |
| **Inherited** | Yes |
| **Conformance** | Extended |

<!-- Source: https://www.w3.org/TR/xslfo20/#change-bar-placement -->

This property determines where, relative to the column areas, the change bars will occur.

- **start** -- The change bar will be offset from the start edge of all column areas.
- **end** -- The change bar will be offset from the end edge of all column areas.
- **left** -- The change bar will be offset from the left edge of all column areas.
- **right** -- The change bar will be offset from the right edge of all column areas.
- **inside** -- If the page binding edge is on the start-edge, the change bar will be offset from the start edge of all column areas. If the binding is the end-edge, the change bar will be offset from the end edge of all column areas. If the page binding edge is on neither the start-edge nor end-edge, the change bar will be offset from the start edge of all column areas.
- **outside** -- If the page binding edge is on the start-edge, the change bar will be offset from the end edge of all column areas. If the binding is the end-edge, the change bar will be offset from the start edge of all column areas. If the page binding edge is on neither the start-edge nor end-edge, the change bar will be offset from the end edge of all column areas.
- **alternate** -- When there are exactly two columns, the change bar will be offset from the start edge of all column one areas and the end edge of all column two areas; when there are any other number of columns, this value is equivalent to "outside".

Note: The placement of any change bar is determined by the value of this property at the `fo:change-bar-begin` that starts the change bar; changes to this property after that do not affect the placement of the change bar begin generated.

### change-bar-style

| Field | Value |
|---|---|
| **Values** | `<border-style>` |
| **Initial** | `none` |
| **Applies to** | fo:change-bar-begin |
| **Inherited** | Yes |
| **Conformance** | Extended |

<!-- Source: https://www.w3.org/TR/xslfo20/#change-bar-style -->

Specifies the style of the change bar. See definition of property `border-top-style`.

Note: The style of any change bar is determined by the value of this property at the `fo:change-bar-begin` that starts the change bar; changes to this property after that do not affect the style of the change bar begin generated.

Note: Conforming implementations may interpret "dotted", "dashed", "double", "groove", "ridge", "inset", and "outset" to be "solid".

### change-bar-width

| Field | Value |
|---|---|
| **Values** | `<border-width>` |
| **Initial** | `medium` |
| **Applies to** | fo:change-bar-begin |
| **Inherited** | Yes |
| **Conformance** | Extended |

<!-- Source: https://www.w3.org/TR/xslfo20/#change-bar-width -->

Specifies the thickness of the change bar.

- **thin** -- A thin border.
- **medium** -- A medium border.
- **thick** -- A thick border.
- **\<length\>** -- The border's thickness has an explicit value. Explicit border widths cannot be negative.

Note: The thickness of any change bar is determined by the value of this property at the `fo:change-bar-begin` that starts the change bar; changes to this property after that do not affect the thickness of the change bar begin generated.

Note: Relative lengths (i.e., percentage values and lengths with units of "em" or "ex") are not permitted for the value of this property.

### content-type

| Field | Value |
|---|---|
| **Values** | `<string> \| auto` |
| **Initial** | `auto` |
| **Applies to** | fo:external-graphic, fo:instream-foreign-object |
| **Inherited** | No |
| **Conformance** | Extended |

<!-- Source: https://www.w3.org/TR/xslfo20/#content-type -->

This property specifies the content-type and may be used by a User Agent to select a rendering processor for the object.

- **auto** -- No identification of the content-type. The User Agent may determine it by "sniffing" or by other means.
- **\<string\>** -- A specification of the content-type in terms of either a mime-type or a namespace. A mime-type specification has the form "content-type:" followed by a mime content-type, e.g., `content-type="content-type:xml/svg"`. A namespace specification has the form "namespace-prefix:" followed by a declared namespace prefix, e.g., `content-type="namespace-prefix:svg"`. If the namespace prefix is null, the content-type refers to the default namespace.

### id

| Field | Value |
|---|---|
| **Values** | `<id>` |
| **Initial** | see prose |
| **Applies to** | all formatting objects |
| **Inherited** | No, see prose |
| **Conformance** | Basic |

<!-- Source: https://www.w3.org/TR/xslfo20/#id -->

An identifier unique within all objects in the result tree with the fo: namespace. It allows references to this formatting object by other objects.

The "inherit" value is not allowed on this property. The initial value of this property is a random and unique identifier. The algorithm to generate this identifier is system-dependent.

### intrinsic-scale-value

| Field | Value |
|---|---|
| **Values** | `<percentage> \| inherit` |
| **Initial** | `100%` |
| **Applies to** | fo:external-graphic, fo:instream-foreign-object |
| **Inherited** | Yes |
| **Conformance** | Extended |

<!-- Source: https://www.w3.org/TR/xslfo20/#intrinsic-scale-value -->

Specifies the scale factor that the intrinsic size corresponds to.

### page-citation-strategy

| Field | Value |
|---|---|
| **Values** | `all \| normal \| non-blank \| inherit` |
| **Initial** | `all` |
| **Applies to** | fo:page-number-citation, fo:page-number-citation-last |
| **Inherited** | No |
| **Conformance** | Extended |

<!-- Source: https://www.w3.org/TR/xslfo20/#page-citation-strategy -->

This property determines what set of page areas are considered by a page number citation formatting object.

- **all** -- The set of pages that might be cited includes the pages containing, as a descendant, any area that matches the ref-id trait of the formatting object on which this property appears plus any blank pages generated by the referenced formatting object.
- **normal** -- The set of pages that might be cited includes the pages containing, as a descendant, any normal area that matches the ref-id trait of the formatting object on which this property appears, and which is either returned to that formatting object or is a descendant of a normal area returned to that formatting object.
- **non-blank** -- The set of pages that might be cited includes the pages containing, as a descendant, any area that matches the ref-id trait of the formatting object on which this property appears. This set of pages includes pages containing as descendants out-of-line areas such as those generated by `fo:footnote` and `fo:float`.

### provisional-distance-between-starts

| Field | Value |
|---|---|
| **Values** | `<length> \| <percentage> \| inherit` |
| **Initial** | `24.0pt` |
| **Applies to** | fo:list-block |
| **Inherited** | Yes |
| **Conformance** | Basic |

<!-- Source: https://www.w3.org/TR/xslfo20/#provisional-distance-between-starts -->

Specifies the provisional distance between the start-indent of the list-item-label and the start-indent of the list-item-body. The value is not directly used during formatting, but is used in the computation of the value of the body-start function.

`body-start()` = the value of the start-indent + start-intrusion-adjustment + the value of the provisional-distance-between-starts of the closest ancestor `fo:list-block`.

If there is no ancestral `fo:list-block`, the value used for the provisional-distance-between-starts in the above formula shall be equal to `inherited-property-value(provisional-distance-between-starts)` of the FO in which the `body-start()` function is evaluated.

### provisional-label-separation

| Field | Value |
|---|---|
| **Values** | `<length> \| <percentage> \| inherit` |
| **Initial** | `6.0pt` |
| **Applies to** | fo:list-block |
| **Inherited** | Yes |
| **Conformance** | Basic |

<!-- Source: https://www.w3.org/TR/xslfo20/#provisional-label-separation -->

Specifies the provisional distance between the end of the list-item-label and the start of the list-item-body. The value is not directly used during formatting, but is used in the computation of the value of the label-end function.

`label-end()` = width of the content-rectangle of the reference-area into which the list-block is placed - (the value of the provisional-distance-between-starts + the value of the start-indent + start-intrusion-adjustment - the value of the provisional-label-separation) of the closest ancestor `fo:list-block`.

If there is no ancestral `fo:list-block`, the value used for the provisional-label-separation and provisional-distance-between-starts in the above formula shall be equal to `inherited-property-value(provisional-label-separation)` and `inherited-property-value(provisional-distance-between-starts)` respectively of the FO in which the `body-start()` function is evaluated.

### ref-id

| Field | Value |
|---|---|
| **Values** | `<idref> \| inherit` |
| **Initial** | none, value required |
| **Applies to** | fo:page-number-citation, fo:page-number-citation-last |
| **Inherited** | No |
| **Conformance** | Basic |

<!-- Source: https://www.w3.org/TR/xslfo20/#ref-id -->

Reference to the object having the specified unique identifier. The value is the "id" of an object in the formatting object tree.

### scale-option

| Field | Value |
|---|---|
| **Values** | `width \| height \| inherit` |
| **Initial** | `width` |
| **Applies to** | fo:external-graphic, fo:instream-foreign-object |
| **Inherited** | Yes |
| **Conformance** | Extended |

<!-- Source: https://www.w3.org/TR/xslfo20/#scale-option -->

Specifies whether the scale-factor applied to the width or the height of the graphic should be retrieved.

- **width** -- Requests the scale-factor applied to the width of the graphic.
- **height** -- Requests the scale-factor applied to the height of the graphic.

### score-spaces

| Field | Value |
|---|---|
| **Values** | `true \| false \| inherit` |
| **Initial** | `true` |
| **Applies to** | fo:block, fo:character, fo:inline, fo:page-number, fo:page-number-citation, fo:page-number-citation-last |
| **Inherited** | Yes |
| **Conformance** | Extended |

<!-- Source: https://www.w3.org/TR/xslfo20/#score-spaces -->

Specifies whether the text-decoration property shall be applied to spaces.

- **true** -- Text-decoration will be applied to spaces.
- **false** -- Text-decoration will not be applied to spaces.

### src

| Field | Value |
|---|---|
| **Values** | `<uri-specification> \| inherit` |
| **Initial** | none, value required |
| **Applies to** | fo:external-graphic, fo:color-profile |
| **Inherited** | No |
| **Conformance** | Basic |

<!-- Source: https://www.w3.org/TR/xslfo20/#src -->

Specifies the URI-specification to locate an external resource such as image/graphic data to be included as the content of this object, or color-profile data.

### visibility

| Field | Value |
|---|---|
| **Values** | `visible \| hidden \| collapse \| inherit` |
| **Initial** | `visible` |
| **Applies to** | all formatting objects that generate areas |
| **Inherited** | Yes |
| **Conformance** | Extended |

<!-- Source: https://www.w3.org/TR/xslfo20/#visibility -->

The "visibility" property specifies whether the boxes generated by an element are rendered. Invisible boxes still affect layout.

- **visible** -- The generated box is visible.
- **hidden** -- The generated box is invisible (fully transparent), but still affects layout.
- **collapse** -- Please consult the section on dynamic row and column effects in tables. If used on elements other than rows or columns, "collapse" has the same meaning as "hidden".

XSL modifications: Changed initial value to visible (it is "inherit" in CSS) and made it an inherited property.

### z-index

| Field | Value |
|---|---|
| **Values** | `auto \| <integer> \| inherit` |
| **Initial** | `auto` |
| **Applies to** | fo:block-container (when absolutely positioned) |
| **Inherited** | No |
| **Conformance** | Extended |

<!-- Source: https://www.w3.org/TR/xslfo20/#z-index -->

For a positioned box, the "z-index" property specifies the stack level of the box in the current stacking context, and whether the box establishes a local stacking context.

- **auto** -- The stack level of the generated box in the current stacking context is the same as its parent's box. The box does not establish a new local stacking context.
- **\<integer\>** -- This integer is the stack level of the generated box in the current stacking context. The box also establishes a local stacking context in which its stack level is "0".

### xml:base

| Field | Value |
|---|---|
| **Values** | `<legacy-extended-iri>` |
| **Initial** | None, a value is required |
| **Applies to** | all formatting objects |
| **Inherited** | Yes |
| **Conformance** | Extended |

<!-- Source: https://www.w3.org/TR/xslfo20/#xml.base -->

Specifies a base URI other than the base URI of the document or external entity in conformance with XML Base.

- **\<legacy-extended-iri\>** -- A Legacy Extended IRI (LEIRI) giving a base URI.

### output-base-uri

| Field | Value |
|---|---|
| **Values** | `empty string \| <uri-specification>` |
| **Initial** | `empty string` |
| **Applies to** | all formatting objects |
| **Inherited** | Yes |
| **Conformance** | Extended |

<!-- Source: https://www.w3.org/TR/xslfo20/#output-base-uri -->

Specifies the base URI to use with relative URIs in the rendered document.

- **empty string** -- Relative URIs in other trait values are resolved relative to the entity containing the reference.
- **\<uri-specification\>** -- A URI specification giving the base URI for resolving relative URIs in other trait values. A relative URI value for this property is resolved relative to the inherited resolved "output-base-uri" value.

## Code Samples

No code samples in spec for this property group.

## See Also

- [fo-external-graphic](fo-external-graphic.md) -- uses `src`, `content-type`, `scale-option`, `intrinsic-scale-value`
- [fo-page-number-citation](fo-page-number-citation.md) -- uses `ref-id`, `page-citation-strategy`
- [fo-list-block](fo-list-block.md) -- uses `provisional-distance-between-starts`, `provisional-label-separation`
- [fo-change-bar-begin](fo-change-bar-begin.md) -- uses change-bar-* properties
- [fo-change-bar-end](fo-change-bar-end.md) -- uses `change-bar-class`
