# Antenna House Extension Functions

Antenna House Formatter extends the standard XSL-FO function set with additional color functions. These functions provide support for CMYK, grayscale, spot colors, and CSS3-style HSL color specification.

## cmyk()

<!-- Source: XSL-FO-Reference-74-MID.pdf p.477 -->

The function `cmyk()` is equivalent to the function `rgb-icc(#CMYK,<C>,<M>,<Y>,<K>)` (see `rgb-icc()`).

**Signature:**

```
cmyk(<C>,<M>,<Y>,<K>)
```

**Arguments:**

- `<C>`,`<M>`,`<Y>`,`<K>` = %-values or numbers from 0.0 to 1.0

No code sample provided in the Antenna House reference for this function.

**Constructed example** (not from spec):

```xml
<fo:block color="cmyk(0, 0, 0, 1)">Black text using CMYK</fo:block>
<fo:block color="cmyk(1, 0, 0, 0)">Cyan text using CMYK</fo:block>
<fo:block color="cmyk(0.2, 0.8, 0, 0.1)">Custom purple using CMYK</fo:block>
```

## cmyka()

<!-- Source: XSL-FO-Reference-74-MID.pdf p.477 -->

The `cmyka()` function has 5 arguments: `cmyka(<C>,<M>,<Y>,<K>,<A>)` (see also `rgb-icc()`).

**Signature:**

```
cmyka(<C>,<M>,<Y>,<K>,<A>)
```

**Arguments:**

- `<C>`,`<M>`,`<Y>`,`<K>` = %-values or numbers from 0.0 to 1.0
- `<A>` = alpha (opacity) value

No code sample provided in the Antenna House reference for this function.

**Constructed example** (not from spec):

```xml
<fo:block color="cmyka(0, 0, 0, 1, 0.5)">Semi-transparent black text</fo:block>
<fo:block color="cmyka(1, 0, 0, 0, 0.8)">80% opaque cyan text</fo:block>
```

## hsl()

<!-- Source: XSL-FO-Reference-74-MID.pdf p.477 -->

`hsl()` is a function in CSS3 and specifies the hue saturation lightness (HSL). The 3 arguments to it are `hsl(<H>,<S>,<L>)`. `<H>` is a number without a unit of measurement. For `<S>` and `<L>` percentage values or the values from 0.0 to 1.0 are allowed.

**Signature:**

```
hsl(<H>,<S>,<L>)
```

**Arguments:**

- `<H>` = hue, a number without a unit of measurement (0-360 on the color wheel)
- `<S>` = saturation, percentage values or the values from 0.0 to 1.0
- `<L>` = lightness, percentage values or the values from 0.0 to 1.0

No code sample provided in the Antenna House reference for this function.

**Constructed example** (not from spec):

```xml
<fo:block color="hsl(0, 100%, 50%)">Red text using HSL</fo:block>
<fo:block color="hsl(120, 1.0, 0.5)">Green text using HSL with decimal values</fo:block>
<fo:block color="hsl(240, 100%, 25%)">Dark blue text using HSL</fo:block>
```

## hsla()

<!-- Source: XSL-FO-Reference-74-MID.pdf p.477 -->

`hsla()` is a function in CSS3 and specifies the hue saturation lightness (HSL) with an additional alpha value. The 4 arguments for it are `hsla(<H>,<S>,<L>,<A>)`. `<H>` is a number without a unit of measurement. For `<S>`, `<L>` and `<A>` percentage values or the values from 0.0 to 1.0 are allowed.

**Signature:**

```
hsla(<H>,<S>,<L>,<A>)
```

**Arguments:**

- `<H>` = hue, a number without a unit of measurement (0-360 on the color wheel)
- `<S>` = saturation, percentage values or the values from 0.0 to 1.0
- `<L>` = lightness, percentage values or the values from 0.0 to 1.0
- `<A>` = alpha (opacity), percentage values or the values from 0.0 to 1.0

No code sample provided in the Antenna House reference for this function.

**Constructed example** (not from spec):

```xml
<fo:block color="hsla(0, 100%, 50%, 0.5)">Semi-transparent red text</fo:block>
<fo:block color="hsla(200, 0.8, 0.4, 1.0)">Fully opaque blue text using decimal values</fo:block>
```

## rgb-icc()

<!-- Source: XSL-FO-Reference-74-MID.pdf p.478-479 -->

The extension of Antenna House concerns the color formats initiated with `#` for gray values, four-color printing (CMYK), and spot colors.

**Argument names used in the following:**

- `<R>`,`<G>`,`<B>` = %-values or integers from 0 to 255
- `<C>`,`<M>`,`<Y>`,`<K>` = %-values or numbers from 0.0 to 1.0
- `<Scale>` = %-value or 0.0 (black) to 1.0 (white)
- `<Tint>` = %-value or 0.0 (brightest value) to 1.0 (darkest value)

### Grayscale

Specify gray values. The intensity of the gray value is set with the `<Scale>` argument:

```
rgb-icc(#Grayscale,<Scale>)
```

No code sample provided in the Antenna House reference for this function.

**Constructed example** (not from spec):

```xml
<fo:block color="rgb-icc(#Grayscale, 0.5)">50% gray text</fo:block>
<fo:block color="rgb-icc(#Grayscale, 0.0)">Black text (grayscale)</fo:block>
<fo:block color="rgb-icc(#Grayscale, 1.0)">White text (grayscale)</fo:block>
```

### CMYK

Specification of four-color printing according to the CMYK format (cyan, magenta, yellow, black). If the RGB specification is missing, the RGB values are derived from the CMYK values:

```
rgb-icc(<R>,<G>,<B>,#CMYK,<C>,<M>,<Y>,<K>)
rgb-icc(#CMYK,<C>,<M>,<Y>,<K>)
```

No code sample provided in the Antenna House reference for this function.

**Constructed example** (not from spec):

```xml
<!-- With explicit RGB fallback -->
<fo:block color="rgb-icc(255, 0, 0, #CMYK, 0, 1, 1, 0)">Red text with RGB fallback and CMYK</fo:block>

<!-- Without RGB fallback (derived from CMYK) -->
<fo:block color="rgb-icc(#CMYK, 0, 0, 0, 1)">Black text using CMYK shorthand</fo:block>
```

### Spot Colors

Specification of spot colors. The color name is specified as `<Name>`, e.g. as `PANTONE 131 PC`. The tint is entered as `<Tint>`. If `<Tint>` is not specified, the tint is assumed to be 1.0. Furthermore, RGB or CMYK must be specified. If the RGB specification is missing, the RGB values are derived from the CMYK values:

**With RGB fallback:**

```
rgb-icc(<R>,<G>,<B>,#Separation,<Name>,<Tint>,<C>,<M>,<Y>,<K>)
rgb-icc(<R>,<G>,<B>,#Separation,<Name>,<Tint>)
rgb-icc(<R>,<G>,<B>,#Separation,<Name>)
```

**Without RGB fallback (derived from CMYK):**

```
rgb-icc(#Separation,<Name>,<Tint>,<C>,<M>,<Y>,<K>)
rgb-icc(#Separation,<Name>,<Tint>)
rgb-icc(#Separation,<Name>)
```

If the option "AH Formatter PANTONE" is included in the license for the AH XSL Formatter, the PANTONE colors are automatically converted to RGB or CMYK values. Then you can write the function as follows:

```
rgb-icc(#Separation, 'PANTONE 131 PC')
```

No code sample provided in the Antenna House reference for this function.

**Constructed example** (not from spec):

```xml
<!-- Spot color with RGB fallback and CMYK alternate, full tint -->
<fo:block color="rgb-icc(200, 150, 50, #Separation, 'PANTONE 131 PC', 1.0, 0, 0.35, 0.85, 0.05)">
  Spot color with RGB fallback and CMYK alternate
</fo:block>

<!-- Spot color with RGB fallback and tint only -->
<fo:block color="rgb-icc(200, 150, 50, #Separation, 'PANTONE 131 PC', 0.5)">
  Spot color at 50% tint with RGB fallback
</fo:block>

<!-- Spot color without RGB fallback, CMYK derived -->
<fo:block color="rgb-icc(#Separation, 'PANTONE 131 PC', 1.0, 0, 0.35, 0.85, 0.05)">
  Spot color with CMYK alternate, no RGB fallback
</fo:block>

<!-- PANTONE licensed shorthand -->
<fo:block color="rgb-icc(#Separation, 'PANTONE 131 PC')">
  PANTONE color using licensed auto-conversion
</fo:block>
```
