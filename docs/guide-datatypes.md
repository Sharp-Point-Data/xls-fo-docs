# Property Datatypes

## Overview

XSL-FO property values use a set of defined datatypes. Some are simple (a single value like a length or integer), while others are **compound datatypes** represented as multiple attributes in the result tree. Understanding compound datatypes is essential for correctly specifying properties like `space-before`, `space-after`, `keep-together`, and `keep-with-next`, which are among the most frequently used properties in XSL-FO stylesheets.

Source: [W3C XSL-FO 2.0 -- Property Datatypes](https://www.w3.org/TR/xslfo20/#datatype)

## Compound Datatypes

Certain property values are described in terms of compound datatypes. A compound datatype (such as `<space>`) is represented in the result tree as multiple attributes. The attribute names consist of the property name, followed by a period, followed by the component name.

For example, a `space-before` property may be specified with all five sub-properties:

<!-- Source: https://www.w3.org/TR/xslfo20/#datatype -->
```xml
space-before.minimum="2.0pt"
space-before.optimum="3.0pt"
space-before.maximum="4.0pt"
space-before.precedence="0"
space-before.conditionality="discard"
```

### Shorthand for Length-Based Compound Values

A short form of compound value specification may be used in cases where the datatype has some `<length>` components and for the `<keep>` datatype.

For length-based compounds, the shorthand gives the specified `<length>` value to each of the `<length>` components and the initial value to all non-`<length>` components.

For example:

<!-- Source: https://www.w3.org/TR/xslfo20/#datatype -->
```xml
space-before="4.0pt"
```

is equivalent to:

<!-- Source: https://www.w3.org/TR/xslfo20/#datatype -->
```xml
space-before.minimum="4.0pt"
space-before.optimum="4.0pt"
space-before.maximum="4.0pt"
space-before.precedence="0"
space-before.conditionality="discard"
```

Note: Since a `<percentage>` value that is not interpreted as "auto" is a valid `<length>` value, it may be used in a short form.

### Shorthand for Keep Values

For the `<keep>` datatype, the shorthand gives the specified value to each of the components.

For example:

<!-- Source: https://www.w3.org/TR/xslfo20/#datatype -->
```xml
keep-together="always"
```

is equivalent to:

<!-- Source: https://www.w3.org/TR/xslfo20/#datatype -->
```xml
keep-together.within-line="always"
keep-together.within-column="always"
keep-together.within-page="always"
```

### Mixing Shorthand and Complete Forms

Short forms may be used together with complete forms; the complete forms have precedence over the expansion of a short form.

For example:

<!-- Source: https://www.w3.org/TR/xslfo20/#datatype -->
```xml
space-before="4.0pt"
space-before.maximum="6.0pt"
```

is equivalent to:

<!-- Source: https://www.w3.org/TR/xslfo20/#datatype -->
```xml
space-before.minimum="4.0pt"
space-before.optimum="4.0pt"
space-before.maximum="6.0pt"
space-before.precedence="0"
space-before.conditionality="discard"
```

### Inheritance and Absolute/Relative Property Interaction

Compound values of properties are inherited as a unit and not as individual components. After inheritance, any complete form specification for a component is used to set its value.

If the computed value of a corresponding relative property is set from the corresponding absolute property, the latter is used in determining all the components of the former.

For example, assuming a block-progression-direction of "top-to-bottom", in a specification of:

<!-- Source: https://www.w3.org/TR/xslfo20/#datatype -->
```xml
margin-top="10.0pt"
space-before.minimum="4.0pt"
```

the explicit setting of one of the components of the corresponding relative property (`space-before.minimum`) will have no effect, because `margin-top` (the absolute property) determines all components of `space-before` (the corresponding relative property).

## Datatype Reference

The following defines the syntax for specifying the datatypes usable in property values.

### Simple Datatypes

| Datatype | Description |
|---|---|
| `<integer>` | A signed integer value: an optional `+` or `-` character followed by a sequence of digits. A property may define additional constraints. (The `+` sign is allowed for CSS2 compatibility.) |
| `<number>` | A signed real number: an optional `+` or `-` character followed by digits, optionally followed by `.` and more digits. A property may define additional constraints. |
| `<length>` | A signed length value: a real number plus a unit qualification. A property may define additional constraints. |
| `<angle>` | An optional `+` or `-` character immediately followed by a `<number>` immediately followed by an angle unit identifier: `deg` (degrees), `grad` (grads), or `rad` (radians). Values are normalized to the range 0deg to 360deg. |
| `<percentage>` | A signed real percentage: an optional `+` or `-` character followed by digits, optionally followed by `.` and digits, followed by `%`. |
| `<time>` | A `<number>` immediately followed by a time unit identifier: `ms` (milliseconds) or `s` (seconds). |
| `<frequency>` | A `<number>` immediately followed by a frequency unit identifier: `Hz` (Hertz) or `kHz` (kilo Hertz). |

### String and Name Datatypes

| Datatype | Description |
|---|---|
| `<character>` | A single Unicode character valid per production [2] of XML or XML 1.1. For example, `c` or `&#x2202;`. |
| `<string>` | A sequence of characters. A property value of type `<string>` must be a quoted value, an NCName, or an expression that evaluates to a `<string>`; anything else (e.g., an integer) is an error. An implementation may recover by treating the unevaluated property value as a string. |
| `<name>` | A string of characters representing a name. Must conform to the definition of an NCName in XML Namespaces. |
| `<family-name>` | A string of characters identifying a font. |
| `<id>` | A string conforming to the NCName definition that is unique within the stylesheet. |
| `<idref>` | A string conforming to the NCName definition that matches an ID property value used within the stylesheet. |

### Locale Datatypes

| Datatype | Description |
|---|---|
| `<country>` | A string conforming to an ISO 3166 (parts 1, 2, and 3) country code. |
| `<language>` | A string conforming to either an ISO 639-2 3-letter terminology/bibliographic code or an ISO 639 2-letter code representing a language name. |
| `<script>` | A string conforming to an ISO 15924 script code. |

### Other Datatypes

| Datatype | Description |
|---|---|
| `<color>` | Either a keyword or a color function. Keywords: aqua, black, blue, fuchsia, gray, green, lime, maroon, navy, olive, purple, red, silver, teal, white, yellow. |
| `<uri-specification>` | `url(` optional-whitespace optional-quote IRI-reference optional-quote optional-whitespace `)`. The IRI reference conforms to RFC 3987. If the IRI contains a single quote, double quotes must be used. |
| `<shape>` | `rect(` `<top>` `<right>` `<bottom>` `<left>` `)` where each value specifies an offset from the respective side of the content rectangle. Values may be a `<length>` or `auto`. Negative lengths are permitted. `auto` is equivalent to `0pt`. |

### Compound Datatypes

| Datatype | Components | Description |
|---|---|---|
| `<space>` | minimum, optimum, maximum, precedence, conditionality | minimum/optimum/maximum are `<length>`s. precedence is either `force` or an `<integer>`. conditionality is `discard` or `retain`. If minimum > optimum, minimum is treated as optimum. If maximum < optimum, maximum is treated as optimum. |
| `<keep>` | within-line, within-column, within-page | Each component is either `auto`, `always`, or an `<integer>`. |
| `<length-range>` | minimum, optimum, maximum | Each component is a `<length>`. If minimum > optimum, treated as optimum. If maximum < optimum, treated as optimum. A property may define additional permitted values (e.g., `auto` or `<percentage>`). |
| `<length-conditional>` | length, conditionality | length is a `<length>`. conditionality is `discard` or `retain`. |
| `<length-bp-ip-direction>` | block-progression-direction, inline-progression-direction | Each component is a `<length>`. |

## See Also

- `properties-space.md` -- Space-related properties (`space-before`, `space-after`, `space-start`, `space-end`)
- `properties-keeps-and-breaks.md` -- Keep and break properties (`keep-together`, `keep-with-next`, `keep-with-previous`)
- `guide-expressions.md` -- XSL-FO expression language and value conversions
- `guide-refinement.md` -- Property value refinement, including shorthand expansion and absolute/relative property mapping
