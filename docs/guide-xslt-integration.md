# XSL Transformation and XSLT Integration

## Overview

XSL-FO documents are typically produced by an XSLT transformation. The XSL specification defines a two-phase processing model: **tree construction** (performed by XSLT) produces a result tree of formatting objects, and **formatting** (performed by the XSL-FO processor) interprets that tree to produce paginated output. This guide covers the relationship between XSLT and XSL-FO, including tree construction, XML version compatibility, the XSL namespace, and the rules governing namespace usage.

This is essential knowledge for LLMs generating XSLT stylesheets that produce XSL-FO output.

<!-- Source: xslspec.xml line 681 -->

## Tree Construction

The Tree Construction is described in "XSL Transformations" (XSLT). The data model in XSLT is capable of representing either an XML 1.0 document or an XML 1.1 document, and it makes no distinction between the two. In principle, therefore, XSL-FO can be used with either of these XML versions; the only differences arise outside the boundary of the transformation proper, while creating the data model from textual XML (parsing).

The provisions in "XSL Transformations" form an integral part of the XSL Recommendation and are considered **normative**. Because the data model is the same whether the original document was XML 1.0 or XML 1.1, the semantics of XSLT processing do not depend on the version of XML used by the original document. There is no reason in principle why all the documents used in a single transformation must conform to the same version of XML.

## XSL Namespace

<!-- Source: https://www.w3.org/TR/xslfo20/#xsl-namespace -->

The XSL namespace has the URI:

```
http://www.w3.org/1999/XSL/Format
```

**Note:** The `1999` in the URI indicates the year in which the URI was allocated by the W3C. It does not indicate the version of XSL being used.

### Namespace Recognition

XSL processors must use the XML namespaces mechanism to recognize elements and attributes from the XSL namespace. Elements from the XSL namespace are recognized only in the stylesheet, not in the source document.

### Namespace Prefix Convention

The specification uses the prefix `fo:` for referring to elements in the XSL namespace. However, XSL stylesheets are free to use any prefix, provided that there is a namespace declaration that binds the prefix to the URI of the XSL namespace.

### Extension Rules

Implementors must not extend the XSL namespace with additional elements or attributes. Instead, any extension must be in a **separate namespace**. The expanded-name of extension elements must have a non-null namespace URI.

An element from the XSL namespace may have any attribute not from the XSL namespace, provided that the expanded-name of the attribute has a non-null namespace URI. The presence of such attributes must not change the behavior of XSL elements and functions defined in the specification. This means that an extension attribute may change the processing of an FO, but only provided that the constraints specified by XSL on that FO remain satisfied.

An XSL processor is always free to ignore such attributes, and must ignore such attributes without giving an error if it does not recognize the namespace URI. Such attributes can provide, for example, unique identifiers, optimization hints, or documentation.

### Error Conditions

It is an error for an element from the XSL namespace to have attributes with expanded-names that have null namespace URIs (i.e., attributes with unprefixed names) other than attributes defined in the specification.

### Naming Conventions

The conventions used for the names of XSL elements, attributes, and functions are:

- Names are all lowercase.
- Hyphens are used to separate words.
- Dots are used to separate names for the components of complex datatypes.
- Abbreviations are used only if they already appear in the syntax of a related language such as XML or HTML.

## Code Samples

No code samples in spec for this section.

## See Also

- [guide-introduction.md](guide-introduction.md) -- Overview of the two-phase XSL processing model (transformation + formatting)
- [fo-root.md](fo-root.md) -- The `fo:root` element, the top-level element of every XSL-FO document
- [guide-datatypes.md](guide-datatypes.md) -- Property datatypes including compound datatypes with dot-separated component names
