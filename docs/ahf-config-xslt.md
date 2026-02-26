# Antenna House Configuration: XSLT Settings

<!-- Source: XSL-FO-Reference-74-MID.pdf pp.278-283 -->

## Overview

The `<xslt-settings>` element configures XSLT preprocessing in AH Formatter. It controls which XSLT processor is used (the built-in MSXML on Windows or an external command-line processor), how parameters are passed to stylesheets, and allows associating specific stylesheets with XML namespaces for automatic transformation.

## Element: `<xslt-settings>`

**Parent:** `<formatter-config>`

**Attributes:** `msxml`, `msxmlver`, `command`, `param-option`

**Child elements:** `<param>`, `<stylesheet>`, `<msxml>`

## Attributes

### `msxml`

Specifies whether to use MSXML or not. If `true` is specified, MSXML is used as an XSLT Processor. Specification of `command` is disregarded at this time. If `false` is specified, the external XSLT Processor specified from `command` will be used, but when nothing is specified from `command`, it is considered that `true` is specified and MSXML is used. The version of MSXML actually used can be checked in the GUI on the XSLT page of the Format Option Setting Dialog. This setting is ignored in non-Windows environment.

- **Applies to:** `<xslt-settings>`
- **Values:** `true` | `false`
- **Default:** `true`

### `msxmlver`

Specifies the maximum version of MSXML used internally when `msxml="true"` is specified. Any version from 6 to 3 can be specified. For example, when 5 is specified, AH Formatter searches MSXML in order of MSXML5, MSXML4, MSXML3 and adopts the first found MSXML. If nothing is specified or the specified value is incorrect (such as 0), the version will be considered 6. This setting is effective only with Windows version.

- **Applies to:** `<xslt-settings>`
- **Values:** `3` | `4` | `5` | `6`
- **Default:** `0` (treated as 6)

### `command`

The command line of the External XSLT Processor is specified here. The command line strings must include at least three identifiers, `%1`, `%2` and `%3`.

- `%1`: XML document
- `%2`: XSL stylesheet
- `%3`: XSLT Output File
- `%param`: Parameter of `xsl:param`

If nothing is specified, or `@MSXML` is specified, the external processor is not used but the internal processor, MSXML is used. This setting is effective only with Windows version. It's an initial setting of XSLT Processor with all kinds of interfaces. If nothing is specified in non-Windows environment, XSLT transformation is not performed.

- **Applies to:** `<xslt-settings>`
- **Values:** a command line for the XSLT processor
- **Default:** none

### `param-option`

Specifies the parameter type of `xsl:param` given to the external XSLT Processor. The strings must include at least two identifiers, `%p` and `%v`. These values are as follows:

- `%p`: Value of `name` of `<param>`
- `%v`: Value of `value` of `<param>`

These values affect the part of `%param` in the command strings. When two or more `<param>`s are specified, they are divided by the white space and repeated.

- **Applies to:** `<xslt-settings>`
- **Values:** see above
- **Default:** none

## Child Element: `<param>`

Specifies XSLT parameters to pass to the XSLT processor.

**Parent:** `<xslt-settings>`

**Attributes:** `name`, `value`

### `name`

Specifies the parameter name of `xsl:param` for XSLT Processor.

- **Applies to:** `<param>`
- **Values:** see above
- **Default:** none

### `value`

Specifies the parameter value of `xsl:param` for XSLT Processor. When the value includes a white space, since the quotation marks will not be processed, explicitly enclose in quotation marks.

- **Applies to:** `<param>`
- **Values:** see above
- **Default:** none

## Child Element: `<stylesheet>`

Associates an XSLT stylesheet with a specific XML namespace, enabling automatic transformation without explicitly specifying a stylesheet at formatting time.

**Parent:** `<xslt-settings>`

**Attributes:** `ns`, `href`

### `ns`

Specifies the namespace of the XML document to match.

- **Applies to:** `<stylesheet>`
- **Values:** a namespace URI
- **Default:** none

### `href`

Specifies the URI of the stylesheet to apply when the namespace matches. If the XML document has the namespace specified here, it can be formatted by itself, without specifying the stylesheet. If the stylesheet is specified when formatting or the stylesheet is specified in the XML document, these are adopted and the setting here will be ignored.

- **Applies to:** `<stylesheet>`
- **Values:** a URI
- **Default:** none

#### Stylesheet Examples

<!-- Source: XSL-FO-Reference-74-MID.pdf p.281 -->

```xml
<stylesheet ns="http://www.w3.org/1999/xhtml" href="xhtml2fo.xsl"/>
<stylesheet ns="http://schemas.microsoft.com/office/word/2003/wordml"
   href="[WordMLToFO install directory]/WordMLToFO.xsl"/>
```

## Child Element: `<msxml>`

Specifies properties of MSXML when `msxml="true"` is specified. The property name is specified by `name` and the value is specified by `value`. For the moment, only `true` or `false` can be specified as `value`. That is, the property which needs the other value cannot be specified.

There are two types of properties available:

1. Properties specified by the `setProperty()` method, e.g. `setProperty("AllowXsltScript", true);`
2. Properties specified by the value directly, e.g. `resolveExternals = true;`

Names interpreted as the latter (direct value) type are:

- `preserveWhiteSpace`
- `validateOnParse`
- `resolveExternals`

In any case other than these, the value is set via the `setProperty()` method. The character string of `name` is not checked.

From MSXML6.0, `resolveExternals` became `ResolveExternals` (AH Formatter V7.2 accepts both). Also, the default value of this is `false` when `external-entity="false"` is specified.

**Parent:** `<xslt-settings>`

**Attributes:** `name`, `value`

- **Applies to:** `<msxml>`
- **Values:** see above
- **Default:** none

### Default MSXML Properties

<!-- Source: XSL-FO-Reference-74-MID.pdf p.282 -->

The following are set as default:

```xml
<msxml name="preserveWhiteSpace" value="true"/>
<msxml name="validateOnParse" value="false"/>
<msxml name="resolveExternals" value="true"/>
<msxml name="ServerHTTPRequest" value="true"/>
<msxml name="ProhibitDTD" value="false"/>>
<msxml name="AllowDocumentFunction" value="true"/>
<msxml name="AllowXsltScript" value="false"/>
```

## Complete XSLT Configuration Example

<!-- Source: XSL-FO-Reference-74-MID.pdf pp.282-283 -->

Suppose XSLT setting is as follows:

```xml
<xslt-settings command="xslt -o &#34;%3&#34; &#34;%1&#34; &#34;%2&#34;
%param" param-option="%p=%v">
   <param name="foo" value="123"/>
   <param name="bar" value="&#34;Hello, World&#34;"/>
</xslt-settings>
```

XSLT Processor executes as follows in order to transform `file.xml` and `file.xsl` into `file.fo`:

```xml
xslt -o "file.fo" "file.xml" "file.xsl" foo=123 bar="Hello, World"
```

As described in the example here, the actual file name given to `%1` or `%2` includes white space, it's necessary to enclose the file name with quotation mark, `&#34;`.
