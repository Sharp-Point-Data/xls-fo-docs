# Linking

## Overview

XSL-FO provides a formatting object (`fo:basic-link`) that expresses both the formatting of link content and the semantics of following a hypertext link. Because XML, unlike HTML, has no built-in semantics, there is no built-in notion of a hypertext link -- XSL-FO must provide this explicitly. XSL-FO also provides mechanisms for changing the presentation of link targets and for altering the formatting of elements based on their active state.

<!-- Source: xslspec.xml line 647 -->

## Link Semantics in XSL-FO

In this context, "link" refers to "hypertext link" as defined in the HTML 4.01 specification, as well as some aspects of "link" as defined in XLink, where "link is a relationship between two or more resources or portions of resources, made explicit by an XLink linking element."

XSL has a formatting object that expresses the dual semantics of:

1. **Formatting the content** of the link reference (i.e., how the clickable text or inline content appears).
2. **Following the link** (i.e., the navigation behavior when the link is activated).

## Link Target Presentation

XSL provides a few mechanisms for changing the presentation of a link target that is being visited:

- **Indicating the link target** -- A mechanism that permits indicating the link target as such (e.g., highlighting or scrolling to the target).
- **Placement control** -- Allows control over the placement of the link target in the viewing area.
- **Display relationship** -- Permits some degree of control over the way the link target is displayed in relationship to the originating link anchor.

## Active State Formatting

XSL also provides a general mechanism for changing the way elements are formatted depending on their **active state**. This is particularly useful in relation to links:

- Indicating whether a given link reference has already been visited.
- Applying a given style depending on whether the mouse, for instance, is hovering over the link reference or not.

## Code Samples

No code samples in spec for this section.

## See Also

- [fo-basic-link.md](fo-basic-link.md) -- The `fo:basic-link` formatting object for creating hypertext links
- [guide-introduction.md](guide-introduction.md) -- Parent chapter: Introduction and Overview of XSL
