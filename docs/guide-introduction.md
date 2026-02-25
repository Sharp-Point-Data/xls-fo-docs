# Introduction and Overview of XSL

## Overview

XSL (Extensible Stylesheet Language) is a language for expressing stylesheets. Given arbitrarily structured XML documents or data files, an XSL stylesheet expresses how that structured content should be styled, laid out, and paginated onto a presentation medium such as a browser window, a hand-held device, or physical pages in a catalog, report, pamphlet, or book.

This guide covers Chapter 1 of the W3C XSL-FO 2.0 specification: the conceptual processing model, the two-phase architecture (tree transformation and formatting), and the design rationale behind XSL's formatting object and property vocabulary.

<!-- Source: xslspec.xml line 203 -->

## Processing a Stylesheet

<!-- Source: xslspec.xml line 213 -->

An XSL **stylesheet processor** accepts a document or data in XML and an XSL stylesheet and produces the presentation of that XML source content intended by the stylesheet designer. There are two aspects of this presentation process:

1. **Tree transformation** -- constructing a result tree from the XML source tree.
2. **Formatting** -- interpreting the result tree to produce formatted results suitable for presentation on a display, on paper, in speech, or onto other media.

Formatting is performed by the **formatter**, which may simply be a rendering engine inside a browser.

Tree transformation allows the structure of the result tree to differ significantly from the source tree. For example, one could add a table-of-contents as a filtered selection of the original source, or rearrange source data into a sorted tabular presentation. During tree construction, the transformation process also adds the information necessary to format the result tree.

Formatting is enabled by including formatting semantics in the result tree, expressed through a catalog of classes of **formatting objects**. The nodes of the result tree are formatting objects. These classes denote typographic abstractions such as page, paragraph, table, and so forth. Finer control over presentation is provided by **formatting properties** such as those controlling indents, word- and letter-spacing, and widow, orphan, and hyphenation control. Together, the formatting object classes and formatting properties provide the vocabulary for expressing presentation intent.

The XSL processing model is intended to be conceptual only. An implementation is not mandated to provide tree transformation and formatting as separate processes. Implementations are free to process the source document in any way that produces the same result as the conceptual model.

### Tree Transformations

<!-- Source: xslspec.xml line 257 -->

Tree transformation constructs the result tree. In XSL, this tree is the **element and attribute tree**, with objects primarily in the "formatting object" namespace. In this tree, a formatting object is represented as an XML element, with properties represented by XML attribute-value pairs. The content of the formatting object is the content of the XML element. Tree transformation is defined in the XSLT Recommendation.

The XSL stylesheet is used in tree transformation. A stylesheet contains a set of **tree construction rules**, each with two parts:

- A **pattern** that is matched against elements in the source tree.
- A **template** that constructs a portion of the result tree.

This allows a stylesheet to be applicable to a wide class of documents that have similar source tree structures.

In some implementations of XSL/XSLT, the result of tree construction can be output as an XML document containing formatting objects and formatting properties. This capability is neither necessary for an XSL processor nor encouraged. However, there are cases where it is important, such as a server preparing input for a known client (e.g., a WAP server preparing input for a WAP-capable handheld device). To preserve accessibility, designers of Web systems should not develop architectures that require transmission of documents containing formatting objects and properties unless either the transmitter knows the client can accept them or the transmitted document contains a reference to the source document(s) used in its construction.

### Formatting

<!-- Source: xslspec.xml line 298 -->

Formatting interprets the result tree in its formatting object tree form to produce the presentation intended by the stylesheet designer.

The vocabulary of formatting objects supported by XSL -- the set of `fo:` element types -- represents the set of typographic abstractions available to the designer. Semantically, each formatting object represents a specification for a part of the pagination, layout, and styling information that will be applied to its content as a result of formatting the whole result tree. Each formatting object class represents a particular kind of formatting behavior. For example, the block formatting object class represents the breaking of paragraph content into lines. Other parts of the specification may come from other formatting objects; for example, formatting a paragraph (block formatting object) depends on both the properties on the block formatting object and the layout structure into which the block is placed by the formatter.

Properties associated with a formatting object instance control its formatting. Some properties (e.g., `color`) directly specify the formatted result. Other properties (e.g., `space-before`) only constrain the set of possible formatted results without specifying any particular one. The formatter may make choices among other possible considerations such as aesthetics.

#### Formatting Steps

Formatting consists of three steps:

**Step 1: Objectification.** The element and attribute tree obtained via XSLT transformation is "objectified." This consists of turning elements into formatting object nodes and attributes into property specifications. The result is the **formatting object tree**.

As part of objectification:
- Characters in the result tree are replaced by `fo:character` nodes.
- Characters in text nodes consisting solely of white-space characters, which are children of elements whose corresponding formatting objects do not permit `fo:character` children, are ignored.
- Other characters within elements whose formatting objects do not permit `fo:character` children are errors.
- The content of `fo:instream-foreign-object` is not objectified; instead the object points to the appropriate node in the element and attribute tree.
- Similarly, any non-XSL namespace child element of `fo:declarations` is not objectified; the object points to the appropriate node in the element and attribute tree.

**Step 2: Refinement.** The formatting object tree is refined to produce the **refined formatting object tree**. Refinement handles the mapping from properties to traits, consisting of:
1. Shorthand expansion into individual properties
2. Mapping of corresponding properties
3. Determining computed values (may include expression evaluation)
4. Handling `white-space-treatment` and `linefeed-treatment` property effects
5. Inheritance

**Step 3: Area tree construction.** The area tree is generated as described in the semantics of each formatting object. The traits applicable to each formatting object class control how areas are generated. Although every formatting property may be specified on every formatting object, for each formatting object class only a subset of properties are used to determine the traits for objects of that class.

#### The Area Tree

Formatting generates a tree of geometric areas called the **area tree**. These geometric areas are positioned on a sequence of one or more pages (a browser typically uses a single page). Each geometric area has a position on the page, a specification of what to display, and may have a background, padding, and borders. For example, formatting a single character generates an area large enough to hold the glyph used to present the character visually. Areas may be nested: the glyph may be positioned within a line, within a block, within a page.

Rendering takes the area tree (the abstract model of the presentation in terms of pages and their collections of areas) and causes a presentation to appear on the relevant medium, such as a browser window or sheets of paper. The semantics of rendering are not described in detail in the specification.

## Benefits of XSL

<!-- Source: xslspec.xml line 434 -->

Unlike HTML, element names in XML have no intrinsic presentation semantics. Without a stylesheet, a processor could not know how to render XML document content other than as an undifferentiated string of characters. XSL provides a comprehensive model and a vocabulary for writing stylesheets using XML syntax.

XSL builds on prior work on Cascading Style Sheets (CSS2) and the Document Style Semantics and Specification Language (DSSSL). While many of XSL's formatting objects and properties correspond to the common set of CSS properties, this alone would not be sufficient to accomplish all goals of XSL. In particular, XSL introduces a model for pagination and layout that extends what is currently available and can in turn be extended to page structures beyond the simple page models described in the specification.

### Paging and Scrolling

<!-- Source: xslspec.xml line 457 -->

Supporting both scrollable document windows and pagination introduces complexities to the styling of XML content. Pagination introduces arbitrary boundaries (pages or regions on pages) on the content, making concepts such as spacing control at page, region, and block boundaries extremely important. Related concepts include adjusting spaces between lines (vertical justification) and between words and letters (line justification). These do not always arise with simple scrollable document windows.

There is a correspondence between a page with multiple regions (body, header, footer, and left/right sidebars) and a Web presentation using "frames." The distribution of content into regions is basically the same in both cases, and XSL handles both analogously.

XSL was developed to give designers control over features needed for paginated documents while providing an equivalent "frame"-based structure for Web browsing. To achieve this, XSL extended the set of formatting objects and formatting properties beyond those available in either CSS2 or DSSSL. Selection of XML source components (elements, attributes, text nodes, comments, and processing instructions) is based on XSLT and XPath, providing an extremely powerful selection mechanism.

The design of the formatting object and property extensions was inspired by DSSSL, though the actual extensions do not always resemble the DSSSL constructs on which they were based. Some diverged from DSSSL to conform more closely with CSS2 or to handle cases more simply.

Extensions were made in several ways:

- **New values for existing properties.** For example, values reflecting a variety of writing-modes (top-to-bottom, bottom-to-top) rather than just left-to-right and right-to-left.
- **Splitting compound properties.** CSS2 properties expressed as one property with multiple simultaneous values were split into several properties for independent control. For example, the `white-space` property was split into four properties: `white-space-treatment` (controls how white space is processed), `linefeed-treatment` (controls how line feeds are processed), `white-space-collapse` (controls how multiple consecutive spaces are collapsed), and `wrap-option` (controls whether lines automatically wrap at boundaries such as column edges). Splitting a property makes the original CSS2 property a "shorthand" for the sub-properties it subsumes.
- **Entirely new properties.** For example, properties controlling hyphenation, including identifying the `script` and `country` of the text, and properties such as `hyphenation-character` (which varies from script to script).

Many formatting objects and properties in XSL come from the CSS2 specification, ensuring compatibility between the two.

#### Four Classes of XSL Properties

1. CSS properties by copy (unchanged from their CSS2 semantics)
2. CSS properties with extended values
3. CSS properties broken apart and/or extended
4. XSL-only properties

### Selectors and Tree Construction

<!-- Source: xslspec.xml line 539 -->

XSL uses XSLT and XPath for tree construction and pattern selection, providing a high degree of control over how portions of source content are presented and what properties are associated with those content portions, even where mixed namespaces are involved.

The patterns of XPath allow selection of a portion of a string or the Nth text node in a paragraph. This allows rules such as making all third paragraphs in procedural steps appear in bold. Properties can be associated with a content portion based on the numeric value of that content or attributes on the containing element, allowing style rules that make negative values appear in red and positive values in black. Text can be generated depending on a particular context in the source tree, or portions of the source tree may be presented multiple times with different styles.

### An Extended Page Layout Model

<!-- Source: xslspec.xml line 560 -->

XSL includes a set of formatting objects to describe both the layout structure of a page or "frame" (body size, number of columns, presence and size of headers, footers, and sidebars) and the rules by which XML source content is placed into these containers.

The layout structure is defined through one or more instances of a **simple-page-master** formatting object. This formatting object allows defining independently filled regions for the body (with multiple columns), a header, a footer, and sidebars on a page. These simple-page-masters can be used in **page sequences** that specify the order in which the various simple-page-masters are used. The page sequence also specifies how styled content fills those pages. This model allows:

- A sequence of simple-page-masters for a book chapter where page instances are automatically generated by the formatter.
- An explicit sequence of pages such as used in a magazine layout.

Styled content is assigned to various regions on a page by associating the region name with names attached to styled content in the result tree.

In addition to layout formatting objects and properties, there are properties designed for the level of control typical of paginated documents, including control over hyphenation and expanded control over text that is kept with other text in the same line, column, or on the same page.

### A Comprehensive Area Model

<!-- Source: xslspec.xml line 589 -->

The extension of properties and formatting objects -- particularly in the area of control over spacing of blocks, lines, page regions, and within lines -- necessitated an extension of the CSS2 box formatting model. The CSS2 box model is a subset of the XSL area model. The area model provides a vocabulary for describing the relationships and space-adjustment between letters, words, lines, and blocks.

The full area model is described in the Area Model chapter of the specification. A mapping of CSS2 box model terminology to XSL Area Model terminology is also provided there.

## Code Samples

No code samples in spec for this section.

## See Also

- `fo-root` -- The root formatting object of every XSL-FO document
- `fo-page-sequence` -- Controls the generation of pages and their layout
- `fo-simple-page-master` -- Defines the layout geometry of a page
- `fo-block` -- The primary block-level formatting object
- `guide-formatting` -- Introduction to XSL-FO formatting concepts (Chapter 2)
- `properties-writing-mode` -- Writing-mode properties (referenced in the Benefits section)
- `guide-area-model` -- The XSL-FO area model in detail
