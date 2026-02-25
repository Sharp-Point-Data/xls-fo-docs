# Numbering Properties

<!-- Source: https://www.w3.org/TR/xslfo20/#numbering.properties -->

## Overview

The numbering properties relate primarily to `fo:number` and control how lines, columns, footnotes, and other arbitrary objects are numbered. This group also includes the Number to String Conversion properties inherited from XSLT, which control how numeric values are formatted as strings (e.g., "1", "i", "a", "A", etc.).

The numbering system supports arbitrary object numbering through the `number-ref-id` property, which allows any formatting object (such as `fo:block`, `fo:inline`, or `fo:instream-foreign-object`) to participate in a named number series. Numbers are defined with `fo:number` and retrieved with `fo:retrieve-number`.

## Properties

### layout-level

| Field | Value |
|---|---|
| **Values** | `line \| column \| footnote \| none` |
| **Initial** | none, a value is required |
| **Applies to** | fo:number |
| **Inherited** | No |
| **Type** | Enumeration of string |

The `layout-level` property determines whether an `fo:number` is to count lines, columns, footnotes or some other type of object.

Values have the following meanings:

- **line** -- Line numbering; the `fo:number` is set under the `fo:page-sequence`, indicating that in this page sequence every line is numbered.
- **column** -- Column numbering; the `fo:number` is set under the `fo:page-sequence`, indicating that in this page sequence every column is numbered.
- **footnote** -- Footnote numbering; the `fo:number` is set under the `fo:page-sequence`, indicating that in this page sequence every footnote is numbered.
- **none** -- Expression based numbering. When this value is used, the "name" property needs to be set and `fo:retrieve-number` is used to retrieve the presentation of the number judged by the `fo:number`'s display properties. `fo:retrieve-number` uses the "value" property to provide an expression to evaluate an actual number value for this presentation. If `fo:retrieve-number` retrieves an `fo:number` whose level property is not set to "none", the expression in `fo:retrieve-number`'s property `reference-value` is used.

### reference-name

| Field | Value |
|---|---|
| **Values** | `<string>` |
| **Initial** | `none` |
| **Applies to** | fo:retrieve-number |
| **Inherited** | No |
| **Required** | Yes |
| **Type** | character |

The `reference-name` property identifies the name of the `fo:number` to which the `fo:retrieve-number` is referring.

### reference-value

| Field | Value |
|---|---|
| **Values** | `<expression>` |
| **Initial** | `value()` |
| **Applies to** | fo:retrieve-number |
| **Inherited** | No |
| **Required** | No |
| **Type** | Expression |

The `reference-value` property is an expression that can be used to generate an actual displayed value based on the retrieved value.

### number-ref-id

| Field | Value |
|---|---|
| **Values** | `<string>` |
| **Initial** | `none` |
| **Applies to** | fo:block, fo:inline, fo:instream-foreign-object, fo:table-row, fo:table-cell |
| **Inherited** | No |
| **Required** | No |
| **Type** | List of String |

The value indicates the name of an `fo:number` object that applies to the current formatting object.

If a non-leveled `fo:number` is used, the layout properties for the `fo:number` will be ignored. The user needs to use `fo:retrieve-number` to retrieve the current value of `fo:number`.

### name

| Field | Value |
|---|---|
| **Values** | `<string>` |
| **Initial** | `none` |
| **Applies to** | fo:number |
| **Inherited** | No |
| **Required** | Yes for layout-level="none", no for all other levels |
| **Type** | string |

The `name` property identifies an `fo:number` object for use with layout-level="none" or cross-references.

An `fo:number` without a name cannot be referenced. There is no imperative state for an `fo:number`, i.e. it is not a counter or a variable. Instead, it provides a reference and display properties for a number series.

### initial-value

| Field | Value |
|---|---|
| **Values** | `<expression>` |
| **Initial** | `1` |
| **Applies to** | fo:number |
| **Inherited** | No |
| **Required** | No |
| **Type** | Expression |

The `initial-value` property provides an initial value for an `fo:number` object. It is an expression, and reference could be across a page sequence boundary. For example, an `fo:number` level="line" object in the second page sequence can set the initial value to be continued from the last page sequence.

### reset-level

| Field | Value |
|---|---|
| **Values** | `block \| block-container \| column \| page \| none` |
| **Initial** | `none` |
| **Applies to** | fo:number |
| **Inherited** | No |
| **Required** | No |

The `reset-level` property determines the level at which the `fo:number`'s internal state in the FO processor needs to be reset to its reset-value. The reset-value is not necessarily the same as the initial-value.

Values have the following meanings:

- **block** -- Reset when a new `fo:block` starts; this applies to level="line" only.
- **block-container** -- Reset when a new `fo:block-container` starts; this applies to level="line" only.
- **column** -- Reset when a new column starts; this applies to level="line", level="paragraph", and level="footnote".
- **page** -- Reset when a new page starts; this applies to level="line", level="paragraph", level="column", and level="footnote".
- **none** -- Not resetting. This is the default.

### reset-value

| Field | Value |
|---|---|
| **Values** | `<expression>` |
| **Initial** | `initial-value if set, or 1 otherwise` |
| **Applies to** | fo:number |
| **Inherited** | No |
| **Required** | No |
| **Type** | Expression |

The `reset-value` property gives the value (an expression) used for an `fo:number` series when it is reset according to its reset-level.

### interval

| Field | Value |
|---|---|
| **Values** | `<expression>` |
| **Initial** | `1` |
| **Applies to** | fo:number |
| **Inherited** | No |
| **Required** | No |
| **Type** | Expression |

The `interval` property on an `fo:number` object determines the amount by which the number increases (or decreases) on each occurrence of the measured unit (lines, blocks, columns, and so forth).

### display-when

| Field | Value |
|---|---|
| **Values** | `<expression>` |
| **Initial** | `true()` |
| **Applies to** | fo:number |
| **Inherited** | No |
| **Required** | No |
| **Type** | Expression |

The `display-when` property is an expression: each number generated by the `fo:number` object is displayed only when the expression given for this property has a true or non-zero value.

For example, for a level="line" object, `value() = 1 or (value() mod 5 = 0)` indicates the number will display every 5 lines and always for the first line.

### display-position

| Field | Value |
|---|---|
| **Values** | `before \| after \| start \| end` |
| **Initial** | `start` |
| **Applies to** | fo:number |
| **Inherited** | No |
| **Required** | No |

The `display-position` property of an `fo:number` object determines where the generated areas will be placed.

Values have the following meanings:

- **before** -- Before the body of the content flow.
- **after** -- After the body of the content flow.
- **start** -- Left or right of the content flow according to the writing-direction.
- **end** -- Right or left of the content flow according to the writing-direction.

### number-align

| Field | Value |
|---|---|
| **Values** | `start \| center \| end \| decimal` |
| **Initial** | `start` |
| **Applies to** | fo:number |
| **Inherited** | No |
| **Required** | No |

The `number-align` property of an `fo:number` object determines how numbers are aligned with respect to one another.

Values have the following meanings:

- **start** -- Align the number to the start point based on the writing-direction.
- **center** -- Align the number to the center of an area large enough to contain the largest generated number.
- **end** -- Align the number to the end point based on the writing-direction.
- **decimal** -- Align the number to the decimal separator, if the increment-by value is not an integer, or to end otherwise.

### number-area-extent

| Field | Value |
|---|---|
| **Values** | `<length>` |
| **Initial** | `none` |
| **Applies to** | fo:number |
| **Inherited** | No |
| **Required** | Yes |
| **Percentages** | refer to the inline-progression-dimension of content-rectangle of parent area |

The `number-area-extent` property determines the size of the area to be extended towards the "area before", "area after", "area start" and "area end" to display the number.

### decimal-format

| Field | Value |
|---|---|
| **Values** | `<string>` |
| **Initial** | `none` |
| **Applies to** | fo:number |
| **Inherited** | No |
| **Required** | No |
| **Type** | String |

The `decimal-format` property indicates the name of the `fo:decimal-format` element that defines the format of a decimal number: decimal values in the generated `fo:number` sequence will be formatted using the properties from the named decimal-format element.

### ordinal

| Field | Value |
|---|---|
| **Values** | `<string>` |
| **Initial** | `none` |
| **Applies to** | fo:number |
| **Inherited** | No |
| **Required** | No |
| **Type** | string |

The `ordinal` property, if given a value, indicates that `fo:number` should generate ordinal rather than cardinal numbers (for example, 1st, 2nd, 3rd, 4th and so on, for English) rather than cardinal numbers (1, 2, 3, 4...).

When `ordinal` is used with the format token "w", the corresponding sequence (e.g. in English, first second third fourth ...) is generated. In some languages, ordinal numbers vary depending on the grammatical context: for example they may have different genders and may decline with the noun that they qualify. In such cases the value of the ordinal attribute may be used to indicate the variation of the ordinal number required. For inflected languages that vary the ending of the word, the preferred approach is to indicate the required ending, preceded by a hyphen. For example, in German, appropriate values are -e, -er, -es and -en.

### format

| Field | Value |
|---|---|
| **Values** | `<string>` |
| **Initial** | `1` |
| **Applies to** | fo:page-sequence, fo:page-number-citation, fo:page-number-citation-last |
| **Inherited** | No |
| **Percentages** | N/A |

This property is defined in XSLT: Number to String Conversion Attributes. It controls the format token used for number-to-string conversion (e.g., "1" for decimal, "i" for lowercase roman, "a" for lowercase alphabetic).

### letter-value

| Field | Value |
|---|---|
| **Values** | `auto \| alphabetic \| traditional \| <implementer extension>` |
| **Initial** | `auto` |
| **Applies to** | fo:page-sequence, fo:page-number-citation, fo:page-number-citation-last |
| **Inherited** | No |
| **Percentages** | N/A |

The `letter-value` property disambiguates between numbering sequences that use letters, such as Roman (i, ii, iii) and Alphabetic (i, j, k).

In many languages there are two commonly used numbering sequences that use letters. One numbering sequence assigns numeric values to letters in alphabetic sequence, and the other assigns numeric values to each letter in some other manner traditional in that language. In English, these would correspond to the numbering sequences specified by the format tokens "a" and "i". A value of "alphabetic" specifies the alphabetic sequence; a value of "traditional" specifies the other sequence. If the `letter-value` property is not specified, then it is implementation-dependent how any ambiguity is resolved.

### grouping-separator

| Field | Value |
|---|---|
| **Values** | `<character>` |
| **Initial** | `no separator` |
| **Applies to** | fo:page-sequence, fo:page-number-citation, fo:page-number-citation-last |
| **Inherited** | No |
| **Percentages** | N/A |

This property is defined in XSLT: Number to String Conversion Attributes. It specifies the character used to separate groups of digits (e.g., a comma in "1,000").

### grouping-size

| Field | Value |
|---|---|
| **Values** | `<number>` |
| **Initial** | `no grouping` |
| **Applies to** | fo:page-sequence, fo:page-number-citation, fo:page-number-citation-last |
| **Inherited** | No |
| **Percentages** | N/A |

This property is defined in XSLT: Number to String Conversion Attributes. It specifies the number of digits per group (e.g., 3 for thousands grouping).

## Code Samples

### Setting up fo:number with layout-level="none"

<!-- Source: https://www.w3.org/TR/xslfo20/#numbering.properties -->
```xml
<!-- the layout-level needs to be set as "none" -->
<fo:number name="p1" layout-level="none"/>
<fo:number name="f1" layout-level="none"/>
```

### Arbitrary object numbering with number-ref-id

<!-- Source: https://www.w3.org/TR/xslfo20/#numbering.properties -->
```xml
<fo:block number-ref-id="p1">Lorem ipsum dolor sit amet,
  consectetuer adipiscing elit, sed diam nonummy nibh euismod
  tincidunt ut laoreet dolore magna aliquam erat
  volutpat.<fo:block>

<fo:block>Ut wisi enim ad minim veniam, quis nostrud exerci
tation <fo:instream-foreign-object
number-ref-id="f1">...</fo:instreaem-foreign-object>
ullamcorper suscipit lobortis nisl ut aliquip ex ea commodo
consequat.</fo:block>

<fo:block number-ref-id="p1">Lorem ipsum dolor sit amet,
consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt
ut laoreet dolore magna aliquam erat volutpat.</fo:block>

<fo:block>Duis autem vel eum iriure dolor in hendrerit in
vulputate velit esse molestie consequat, vel illum dolore eu feugiat
nulla facilisis at vero eros et accumsan et iusto odio dignissim qui
blandit praesent luptatum zzril delenit</fo:block>

<fo:block>Lorem ipsum dolor sit amet, consectetuer adipiscing
elit, <fo:instream-foreign-object
number-ref-id="f1">...</fo:instreaem-foreign-object> sed diam
nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat
volutpat.</fo:block>

<fo:block number-ref-id="p1">Ut wisi enim ad minim veniam, quis
nostrud exerci tation ullamcorper suscipit lobortis nisl ut aliquip ex
ea commodo consequat.</fo:block>

<fo:block number-ref-id="p1">Lorem ipsum dolor sit amet,
consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt
ut laoreet dolore magna aliquam erat volutpat.</fo:block>

<fo:block>In above <fo:retrieve-number
  name="f1"/> in <fo:retrieve-number name="p1"> paragraphs,
we demonstrated the new attribute
"number-ref-id"</fo:block>
```

In the above example, the attribute "number-ref-id" is added to only four different `fo:block` objects, which means FOUR distinct paragraphs are marked, instead of SEVEN according to the total number of all `fo:block` objects.

### reference-value expression example

<!-- Source: https://www.w3.org/TR/xslfo20/#reference-value -->
```xml
if (value() - current-page-number() > 1) string(concat('Page ', value())
     else if (value() - current-page-number() = 1) 'next page'
     else if (value() = current-page-number()) 'later this page'
```

This example shows how `reference-value` can generate context-sensitive text based on the relationship between the retrieved number value and the current page number.

## See Also

- [fo-page-sequence](fo-page-sequence.md) -- The `fo:page-sequence` formatting object (uses format, letter-value, grouping properties)
- [fo-page-number-citation](fo-page-number-citation.md) -- The `fo:page-number-citation` formatting object
- [fo-page-number-citation-last](fo-page-number-citation-last.md) -- The `fo:page-number-citation-last` formatting object
