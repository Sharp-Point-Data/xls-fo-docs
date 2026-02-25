# Expressions and Core Function Library

## Overview

All property value specifications in attributes within an XSL stylesheet can be expressions. These expressions represent the value of the property specified. The expression is first evaluated and then the resultant value is used to determine the value of the property.

The expression language supports operations on a limited set of datatypes. These do **not** include `<angle>`, `<time>`, and `<frequency>`. Values of those datatypes must be strings in the expression language. The definition of these datatypes specifies the allowed form of these strings.

Source: [W3C XSL-FO 2.0 -- Expressions](https://www.w3.org/TR/xslfo20/#numbers)

## Property Context

Properties are evaluated against a property-specific context. This context provides:

- A list of allowed resultant types for a property value.
- Conversions from resultant expression value types to an allowed type for the property.
- The current `font-size` value.
- Conversions from relative numerics by type to absolute numerics within additive expressions.

It is not necessary that a conversion be provided for all types. If no conversion is specified, it is an error.

When a type instance (e.g., a string, a keyword, a numeric, etc.) is recognized in the expression it is evaluated against the property context. This provides the ability for specific values to be converted with the property context's specific algorithms or conversions for use in the evaluation of the expression as a whole.

For example, the "auto" enumeration token for certain properties is a calculated value. Such a token would be converted into a specific type instance via an algorithm specified in the property definition. In such a case the resulting value might be an absolute length specifying the `width` of some aspect of the formatting object.

In addition, this allows certain types like relative numerics to be resolved into absolute numerics prior to mathematical operations.

All property contexts allow conversions as specified in the Expression Value Conversions section below.

## Evaluation Order

When a set of properties is being evaluated for a specific formatting object in the formatting object tree, there is a specific order in which properties must be evaluated. The `font-size` property **must** be evaluated first before all other properties. Once `font-size` has been evaluated, all other properties may be evaluated in any order.

When `font-size` is evaluated, the current font-size for use in evaluation is the `font-size` of the parent element. Once `font-size` has been evaluated, that value is used as the current font-size for all property contexts of all property value expressions being further evaluated.

## Expression Grammar

### Basics

The top-level expression grammar is:

```
Expr          ::= AdditiveExpr
PrimaryExpr   ::= '(' Expr ')'
                 | Numeric
                 | Literal
                 | Color
                 | Keyword
                 | EnumerationToken
                 | FunctionCall
```

### Function Calls

```
FunctionCall  ::= FunctionName '(' ( Argument ( ',' Argument )* )? ')'
Argument      ::= Expr
```

### Numerics

A numeric represents all the types of numbers in an XSL expression. Some are absolute values; others are relative to some other set of values. All use a floating-point number (double-precision 64-bit IEEE 754) to represent the number-part of their definition. IEEE 754 values include a special "Not-a-Number" (NaN) value, positive and negative infinity, and positive and negative zero.

```
Numeric          ::= AbsoluteNumeric | RelativeNumeric
AbsoluteNumeric  ::= AbsoluteLength
AbsoluteLength   ::= Number AbsoluteUnitName?
RelativeNumeric  ::= Percent | RelativeLength
Percent          ::= Number '%'
RelativeLength   ::= Number RelativeUnitName
```

#### Operators

The following operators may be used with numerics:

| Operator | Description |
|----------|-------------|
| `+`      | Performs addition. |
| `-`      | Performs subtraction or negation. |
| `*`      | Performs multiplication. |
| `div`    | Performs floating-point division according to IEEE 754. |
| `mod`    | Returns the remainder from a truncating division. |

Since XML allows `-` in names, the `-` operator (when not used as a UnaryExpr negation) typically needs to be preceded by white space. For example, the expression `10pt - 2pt` means subtract 2 points from 10 points. The expression `10pt-2pt` would mean a length value of 10 with a unit of "pt-2pt".

**`mod` operator examples:**

- `5 mod 2` returns `1`
- `5 mod -2` returns `1`
- `-5 mod 2` returns `-1`
- `-5 mod -2` returns `-1`

The `mod` operator is the same as the `%` operator in Java and ECMAScript and is **not** the same as the IEEE remainder operation, which returns the remainder from a rounding division.

#### Numeric Expression Grammar

```
AdditiveExpr         ::= MultiplicativeExpr
                       | AdditiveExpr '+' MultiplicativeExpr
                       | AdditiveExpr '-' MultiplicativeExpr

MultiplicativeExpr   ::= UnaryExpr
                       | MultiplicativeExpr MultiplyOperator UnaryExpr
                       | MultiplicativeExpr 'div' UnaryExpr
                       | MultiplicativeExpr 'mod' UnaryExpr

UnaryExpr            ::= PrimaryExpr
                       | '-' UnaryExpr
```

**Operator precedence** (lowest precedence first):

1. `+`, `-`
2. `*`, `div`, `mod`

All operators are left associative. For example, `2*3 + 4 div 5` is equivalent to `(2*3) + (4 div 5)`.

If a non-numeric value is used in an AdditiveExpr and there is no property context conversion from that type into an absolute numeric value, the expression is invalid and considered an error.

## Absolute Numerics

An absolute numeric is an absolute length which is a pair consisting of a Number and a UnitName raised to a power. When an absolute length is written without a unit, the unit power is assumed to be zero. Hence, all floating point numbers are a length with a power of zero.

Each unit name has associated with it an internal ratio to some common internal unit of measure (e.g., a meter). When a value is written in a property expression, it is first converted to the internal unit of measure and then mathematical operations are performed.

Only the `mod`, addition, and subtraction operators require that the numerics on either side of the operation be absolute numerics of the same unit power. For other operations, the unit powers may be different and the result should be mathematically consistent as with the handling of powers in algebra.

A property definition may constrain an absolute length to a particular power. For example, when specifying `font-size`, the value is expected to be of power "one" -- that is, it is expected to have a single powered unit specified (e.g., `10pt`).

When the final value of a property is calculated, the resulting power of the absolute numeric must be either zero or one. If any other power is specified, the value is an error.

## Relative Numerics

Relative lengths are values that are calculated relative to some other set of values. When written as part of an expression, they are either converted via the property context into an absolute numeric or passed verbatim as the property value.

It is an error if the property context has no available conversion for the relative numeric and a conversion is required for expression evaluation (e.g., within an add operation).

### Percents

Percentages are values that are counted in 1/100 units. That is, `10%` as a percentage value is `0.10` as a floating point number. When converting to an absolute numeric, the percentage is defined in the property definition as being a percentage of some known property value. If the percentage evaluates to "auto", the complete expression evaluates to "auto".

For example, a value of "110%" on a `font-size` property would be evaluated to mean 1.1 times the current font size. Such a definition of the allowed conversion for percentages is specified on the property definition. If no conversion is specified, the resulting value is a percentage.

### Relative Lengths

A relative length is a unit-based value that is measured against the current value of the `font-size` property.

- **`em`**: The definition of "1em" is equal to the current font size. For example, a value of "1.25em" is 1.25 times the current font size.
- **`ex`**: The definition of "x-height" is the distance between the baseline and midline of an alphabet. From this comes the "ex" unit.

When an `em` measurement is used in an expression, it is converted according to the `font-size` value of the current property's context. The result of the expression is an absolute length.

## Strings

Strings are represented either as literals (quoted strings) or as an EnumerationToken. All property contexts allow conversion from enumeration tokens to strings (see Expression Value Conversions below).

## Colors

A color is a set of values used to identify a particular color from a color space. Only RGB (Red, Green, Blue) and ICC (International Color Consortium) colors are included in this Recommendation.

RGB colors are directly represented in the expression language using a hexadecimal notation (e.g., `#FF0000`). ICC colors can be specified through the `rgb-icc()` function. Colors can also be specified through the `system-color()` function or through conversion from an EnumerationToken via the property context.

## Keywords

Keywords are special tokens in the grammar that provide access to calculated values or other property values.

### inherit

The property takes the same **computed** value as the property for the formatting object's parent object.

`inherit` is not allowed as an expression mixed with operations. The same functionality is provided by the `from-parent()` function, which can be mixed with operations.

## Lexical Structure

When processing an expression, white space (ExprWhitespace) may be allowed before or after any expression token even though it is not explicitly defined as such in the grammar. In some cases, white space is necessary to make tokens lexically distinct. Essentially, white space should be treated as if it does not exist after tokenization of the expression has occurred.

### Tokenization Disambiguation Rules

The following special tokenization rules must be applied in the order specified to disambiguate the grammar:

1. If the character following an NCName (possibly after intervening ExprWhitespace) is `(`, then the token must be recognized as a FunctionName.
2. A number terminates at the first occurrence of a non-digit character other than `.`. This allows the unit token for length quantities to parse properly.
3. When an NCName immediately follows a Number, it should be recognized as a UnitName or it is an error.
4. The Keyword values take precedence over EnumerationToken.
5. If an NCName follows a Numeric, it should be recognized as an OperatorName or it is an error.

### Complete Lexical Grammar

```
ExprToken        ::= '(' | ')' | '%'
                   | Operator
                   | FunctionName
                   | EnumerationToken
                   | Number

Number           ::= FloatingPointNumber
FloatingPointNumber ::= Digits ('.' Digits?)?
                      | '.' Digits
Digits           ::= [0-9]+

Color            ::= '#' AlphaOrDigits
AlphaOrDigits    ::= [a-fA-F0-9]+

Literal          ::= '"' [^"]* '"'
                   | "'" [^']* "'"

Operator         ::= OperatorName
                   | MultiplyOperator
                   | '+' | '-'
OperatorName     ::= 'mod' | 'div'
MultiplyOperator ::= '*'

Keyword          ::= 'inherit'
FunctionName     ::= NCName
EnumerationToken ::= NCName

AbsoluteUnitName ::= 'cm' | 'mm' | 'in' | 'pt' | 'pc' | 'px'
RelativeUnitName ::= 'em' | 'ex'

ExprWhitespace   ::= S
```

## Expression Value Conversions

<!-- Source: https://www.w3.org/TR/xslfo20/#expr.value.conv -->

Values that are the result of an expression evaluation may be converted into property value types. In some instances this is a simple verification of set membership (e.g., is the value a legal country code). In other cases, the value is expected to be a simple type like an integer and must be converted.

It is not necessary that all types be allowed to be converted. If the expression value cannot be converted to the necessary type for the property value, it is an error.

### Allowed Conversions

| Type | Allowed Conversions | Constraints |
|------|-------------------|-------------|
| NCName (EnumerationToken) | Color (via `system-color()` function); Enumeration value (as defined in the property definition); To a string literal | The value may be checked against a legal set of values depending on the property. |
| AbsoluteNumeric | Integer (via the `round()` function); Color (as an RGB color value) | If converting to an RGB color value, it must be a legal color value from the color space. |
| RelativeLength | To an AbsoluteLength | (none) |

The specific conversion to be applied is property specific and can be found in the definition of each property.

Conversions of compound property values are not allowed. For example, `space-before.optimum="inherited-property-value(space-before)"` is invalid. Permitted are `space-before="inherited-property-value(space-before)"` and `space-before.optimum="inherited-property-value(space-before.optimum)"` since they do not require conversion.

## Definitions of Units of Measure

<!-- Source: https://www.w3.org/TR/xslfo20/#numbers -->

| Unit | Definition |
|------|-----------|
| `cm` | Centimeter (see ISO 31) |
| `mm` | Millimeter (see ISO 31) |
| `in` | Inch = 2.54cm |
| `pt` | Point = 1/72in |
| `pc` | Pica = 12pt |
| `px` | Pixel (see Pixels below) |
| `em` | Equal to the current font-size (see Relative Lengths above) |
| `ex` | x-height of the current font (see Relative Lengths above) |

### Pixels

<!-- Source: https://www.w3.org/TR/xslfo20/#pixels -->

XSL interprets a `px` unit to be a request for the formatter to choose a device-dependent measurement that approximates viewing one pixel on a typical computer monitor. This interpretation follows:

1. **Preferred definition**: The actual distance covered by the largest integer number of device dots (the size of a device dot is measured as the distance between dot centers) that spans a distance less-than-or-equal-to the distance specified by the CSS arc-span rule. A minimum of 1 device dot should be used. This calculation is done separately in each axis, and may have a different value in each axis.

2. **Alternative**: Implementors may instead simply pick a fixed conversion factor, treating `px` as an absolute unit of measurement (such as 1/92" or 1/72").

Pixels should not be mixed with other absolute units in expressions as they may cause undesirable effects. Particular caution should be used with inherited property values that may have been specified using pixels.

If the User Agent chooses a measurement for `px` that does not match an integer number of device dots in each axis, it may produce undesirable effects such as: moire patterns in scaled raster graphics, unrenderable overlapping areas when the renderer rounds sizes upward, large spaces when the renderer rounds sizes downward, or unreadable results including unacceptably small text/layout.

Stylesheets utilizing `px` units may not produce consistent results across different implementations or different output devices from a single implementation. Even if stylesheets are expressed entirely in `px` units the results may vary on different devices.

## Core Function Library

### Number Functions

<!-- Source: https://www.w3.org/TR/xslfo20/#expr-color-functions -->

#### floor(number) => number

The `floor` function returns the largest (closest to positive infinity) integer that is not greater than the argument. The number argument to this function must be of unit power zero.

If it is necessary to use the `floor` function for a property where a unit power of one is expected, then an expression such as `floor(1.4in div 1.0in)*1.0in` must be used. This also applies to `ceiling`, `round`, and other such functions where a unit power of zero is required.

#### ceiling(number) => number

The `ceiling` function returns the smallest (closest to negative infinity) integer that is not less than the argument. The number argument to this function must be of unit power zero.

#### round(number) => number

The `round` function returns the integer that is closest to the argument. If there are two such numbers, then the one that is closest to positive infinity is returned. The numeric argument to this function must be of unit power zero.

#### min(number, number) => number

The `min` function returns the minimum of the two numeric arguments. These arguments must have the same unit power.

#### max(number, number) => number

The `max` function returns the maximum of the two numeric arguments. These arguments must have the same unit power.

#### abs(number) => number

The `abs` function returns the absolute value of the numeric argument. That is, if the numeric argument is negative, it returns the negation of the argument.

### Color Functions

<!-- Source: https://www.w3.org/TR/xslfo20/#expr-color-functions -->

#### rgb(number, number, number) => color

The `rgb` function returns a specific color from the RGB color space. The parameters to this function must be numerics (real numbers) with a length power of zero.

#### rgb-icc(number, number, number, NCName, number, number, ...) => color

The `rgb-icc` function returns a specific color from the ICC Color Profile. The color profile is specified by the name parameter (the fourth parameter). This color profile must have been declared in the `fo:declarations` formatting object using an `fo:color-profile` formatting object.

The first three parameters specify a fallback color from the sRGB color space. This color is used when the color profile is not available. The color is specified by color values (real numbers) specified after the name parameter. These values are specific to the color profile.

#### icc-named-color(number, number, number, NCName, string) => color

The `icc-named-color` function returns a specific named color from the ICC Color profile. The color profile is specified by the name parameter (the fourth parameter). This color profile must have been declared in the `fo:declarations` formatting object using an `fo:color-profile` formatting object.

The color is specified by the last parameter. The first three parameters specify a fallback color from the sRGB color space. This color is used when the CIE LCH color space is not available.

#### system-color(NCName) => color

The `system-color` function returns a system defined color with a given name.

#### cmyk-icc-color(number, number, number, NCName, number, number, number, number) => color

The `cmyk-icc-color` function returns a specific color from the ICC Color Profile. The color profile is specified by the name parameter (the fourth parameter). This color profile must have been declared in the `fo:declarations` formatting object using an `fo:color-profile` formatting object.

The first three parameters specify a fallback color from the sRGB color space. This color is used when the color profile is not available. The color is specified by a sequence of four color values (real numbers) specified after the name parameter.

#### cie-lab-color(number, number, number, number, number, number, number) => color

The `cie-lab-color` function returns a specific color from the cartesian form of the CIE Lab color space. The "Lightness", "a", and "b" values are specified by the fourth to sixth parameters, respectively.

The first three parameters specify a fallback color from the sRGB color space. This color is used when the CIE Lab color space is not available.

#### cie-lch-color(number, number, number, number, number, number, number) => color

The `cie-lch-color` function returns a specific color from the cylindrical form of the CIELUV color space. The "Lightness", "Hue", and "Chroma" values are specified by the fourth to sixth parameters, respectively.

The first three parameters specify a fallback color from the sRGB color space. This color is used when the CIE LCH color space is not available.

#### Uncalibrated Device Color Functions

Uncalibrated device colors are sometimes useful in print workflows, for example to produce patches of known ink density used for quality control purposes.

**device-gray-color(number, number, number, number) => color**

Returns an uncalibrated gray color. The first three parameters are the sRGB fallback. The fourth parameter is the gray component.

**device-rgb-color(number, number, number, number, number, number) => color**

Returns an uncalibrated RGB color. The first three parameters are the sRGB fallback. The last three parameters are the device RGB values.

**device-cmyk-color(number, number, number, number, number, number, number) => color**

Returns an uncalibrated CMYK color. The first three parameters are the sRGB fallback. The last four parameters are the device CMYK values.

A color-managed User Agent which supports the indicated class of output device will pass the values through without color management. If the class of output device (for example, CMYK) is not supported, then the fallback sRGB color (the first three parameters) is used. As these are uncalibrated, any interpolation or compositing occurs using the fallback sRGB color value.

### Font Functions

<!-- Source: https://www.w3.org/TR/xslfo20/#expr-color-functions -->

#### system-font(NCName, NCName?) => object

The `system-font` function returns a characteristic of a system font. The first argument is the name of the system font and the second argument, which is optional, names the property that specifies the characteristic. If the second argument is omitted, then the characteristic returned is the same as the name of the property to which the expression is being assigned.

For example, the expression `system-font(heading, font-size)` returns the `font-size` characteristic for the system font named "heading". This is equivalent to the property assignment `font-size="system-font(heading)"`.

### Property Value Functions

<!-- Source: https://www.w3.org/TR/xslfo20/#expr-color-functions -->

#### inherited-property-value(NCName?) => object

The `inherited-property-value` function returns the inherited value of the property whose name matches the argument specified, or if omitted, the property for which the expression is being evaluated. It is an error if this property is not an inherited property.

The returned "inherited value" is the computed value of this property on this object's parent.

If the argument specifies a shorthand property and if the expression only consists of the `inherited-property-value` function with an argument matching the property being computed, it is interpreted as an expansion of the shorthand with each property into which the shorthand expands, each having a value of `inherited-property-value` with an argument matching the property. It is an error if arguments matching a shorthand property are used in any other way.

Similarly, if the argument specifies a property of a compound datatype and if the expression only consists of the `inherited-property-value` function with an argument matching the property being computed, it is interpreted as an expansion with each component of the compound property having a value of `inherited-property-value` with an argument matching the component. It is an error if arguments matching a property of a compound datatype are used in any other way.

#### label-end() => number

The `label-end` function returns the calculated label-end value for lists. See the definition in the `provisional-label-separation` property.

#### body-start() => number

The `body-start` function returns the calculated body-start value for lists. See the definition in the `provisional-distance-between-starts` property.

#### from-parent(NCName?) => object

The `from-parent` function returns a computed value of the property whose name matches the argument specified, or if omitted, the property for which the expression is being evaluated. The value returned is that for the parent of the formatting object for which the expression is evaluated. If there is no parent, the value returned is the initial value.

If the argument specifies a shorthand property and if the expression only consists of the `from-parent` function with an argument matching the property being computed, it is interpreted as an expansion of the shorthand with each property into which the shorthand expands, each having a value of `from-parent` with an argument matching the property. It is an error if arguments matching a shorthand property are used in any other way.

Similarly, if the argument specifies a property of a compound datatype and if the expression only consists of the `from-parent` function with an argument matching the property being computed, it is interpreted as an expansion with each component of the compound property having a value of `from-parent` with an argument matching the component. It is an error if arguments matching a property of a compound datatype are used in any other way.

#### from-nearest-specified-value(NCName?) => object

The `from-nearest-specified-value` function returns a computed value of the property whose name matches the argument specified, or if omitted, the property for which the expression is being evaluated. The value returned is that for the closest ancestor of the formatting object for which the expression is evaluated on which there is an assignment of the property in the XML result tree in the fo namespace. If there is no such ancestor, the value returned is the initial value.

If the argument specifies a shorthand property and if the expression only consists of the `from-nearest-specified-value` function with an argument matching the property being computed, it is interpreted as an expansion of the shorthand with each property into which the shorthand expands, each having a value of `from-nearest-specified-value` with an argument matching the property. It is an error if arguments matching a shorthand property are used in any other way.

Similarly, if the argument specifies a property of a compound datatype and if the expression only consists of the `from-nearest-specified-value` function with an argument matching the property being computed, it is interpreted as an expansion with each component of the compound property having a value of `from-nearest-specified-value` with an argument matching the component. It is an error if arguments matching a property of a compound datatype are used in any other way.

#### from-page-master-region(NCName?) => object

The `from-page-master-region` function returns the computed value of the property whose name matches the argument specified, or if omitted, the property for which the expression is being evaluated.

In XSL-FO this function may only be used as the value of the `writing-mode` and `reference-orientation` properties. In addition, the argument of the function **must** be omitted. If an argument is present, it is an error.

The computed value of the designated property is taken from that property on the layout formatting object being used to generate the region viewport/reference area pair.

If this function is used in an expression on a formatting object, F, that is a descendant of an `fo:page-sequence`, then the computed value is taken from the region specification that was used to generate the nearest ancestor region reference area which has as its descendants the areas returned by F.

#### from-table-column(NCName?) => object

The `from-table-column` function returns the inherited value of the property whose name matches the argument specified, or if omitted, the property for which the expression is being evaluated, from the `fo:table-column` whose `column-number` matches the column for which this expression is evaluated and whose `number-columns-spanned` also matches any span. If there is no match for `number-columns-spanned`, it is matched against a span of 1. If there is still no match, the initial value is returned.

If the argument specifies a shorthand property and if the expression only consists of the `from-table-column` function with an argument matching the property being computed, it is interpreted as an expansion of the shorthand with each property into which the shorthand expands, each having a value of `from-table-column` with an argument matching the property. It is an error if arguments matching a shorthand property are used in any other way.

Similarly, if the argument specifies a property of a compound datatype and if the expression only consists of the `from-table-column` function with an argument matching the property being computed, it is interpreted as an expansion with each component of the compound property having a value of `from-table-column` with an argument matching the component. It is an error if arguments matching a property of a compound datatype are used in any other way.

It is also an error to use this function on formatting objects that are not an `fo:table-cell` or its descendants.

#### proportional-column-width(number) => number

The `proportional-column-width` function returns N units of proportional measure where N is the argument given to this function. The column widths are first determined ignoring the proportional measures. The difference between the table-width and the sum of the column widths is the available proportional width. One unit of proportional measure is the available proportional width divided by the sum of the proportional factors.

It is an error to use this function on formatting objects other than an `fo:table-column`. It is also an error to use this function if the fixed table layout is not used.

#### merge-property-values(NCName?) => object

The `merge-property-values` function returns a value of the property whose name matches the argument, or if omitted, the property for which the expression is being evaluated. The value returned is the specified value on the last `fo:multi-property-set`, of the parent `fo:multi-properties`, that applies to the User Agent state. If there is no such value, the computed value of the parent `fo:multi-properties` is returned.

If the argument specifies a shorthand property and if the expression only consists of the `merge-property-values` function with an argument matching the property being computed, it is interpreted as an expansion of the shorthand with each property into which the shorthand expands, each having a value of `merge-property-values` with an argument matching the property. It is an error if arguments matching a shorthand property are used in any other way.

Similarly, if the argument specifies a property of a compound datatype and if the expression only consists of the `merge-property-values` function with an argument matching the property being computed, it is interpreted as an expansion with each component of the compound property having a value of `merge-property-values` with an argument matching the component. It is an error if arguments matching a property of a compound datatype are used in any other way.

The test for applicability of a User Agent state is specified using the `active-state` property.

It is an error to use this function on formatting objects other than an `fo:wrapper` that is the child of an `fo:multi-properties`.

## Code Samples

No code samples in spec for this section. (The `<eg>` tags in this range of the spec -- samples 17-20 at lines 5607, 5725, 5770, and 5774 -- are within the Property Value Functions subsection but are assigned to `guide-property-refinement.md` per the project sample inventory.)

## See Also

- `guide-datatypes.md` -- Compound datatypes and shorthand notation for property values
- `guide-property-refinement.md` -- Property value refinement process, including examples of `inherited-property-value()` and `from-page-master-region()`
- `fo-declarations.md` -- The `fo:declarations` formatting object, used for `fo:color-profile` declarations required by ICC color functions
- `fo-table-column.md` -- The `fo:table-column` formatting object, relevant to `proportional-column-width()` and `from-table-column()`
- `fo-list-block.md` -- List formatting objects, relevant to `label-end()` and `body-start()` functions
- `fo-multi-properties.md` -- Multi-properties formatting object, relevant to `merge-property-values()`
