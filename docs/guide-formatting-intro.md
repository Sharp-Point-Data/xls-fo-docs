# Introduction to Formatting

## Overview

This guide covers the fundamental concept of **formatting** in XSL-FO: the process of turning the result of an XSL transformation into a tangible form for a reader or listener. It describes the two-step architecture (tree construction followed by formatting), the key abstractions (formatting objects, areas, traits, refinement), and the conceptual procedure by which a formatter produces output.

<!-- Source: https://www.w3.org/TR/xslfo20/#fo-jc-intro -->

## The Formatting Process

Formatting is the construction of an **area tree** -- an ordered tree containing geometric information for the placement of every glyph, shape, and image in the document, together with information embodying spacing constraints and other rendering information. This rendering information is referred to as **traits**, which are to areas what properties are to formatting objects and attributes are to XML elements.

The area tree is an abstract model. A conforming formatter need not literally construct an area tree internally, so long as the resulting tangible form obeys the implied constraints. When constraints conflict to the point where it is impossible to satisfy them all, it is implementation-defined which constraints are relaxed and in what order.

## Formatting Objects, Areas, and Levels

**Formatting objects** are elements in the formatting object tree whose names are from the XSL namespace. A formatting object belongs to a class identified by its element name. The formatting behavior of each class is described in terms of:

1. What areas are created by a formatting object of that class.
2. How the traits of those areas are established.
3. How the areas are structured hierarchically with respect to areas created by other formatting objects.

Formatting objects are either **block-level** or **inline-level**, referring to the types of areas they generate:

- **Inline-areas** (e.g., glyph-areas) are collected into lines and stacked in the **inline-progression-direction**.
- **Lines** are a type of block-area, stacked in the **block-progression-direction**, which is perpendicular to the inline-progression-direction.

In Western writing systems, the block-progression-direction is "top-to-bottom" and the inline-progression-direction is "left-to-right". The specification uses relative directional terms rather than absolute ones:

| Relative Term | Direction |
|---|---|
| `before` / `after` | In the block-progression-direction |
| `start` / `end` | In the inline-progression-direction |

These relative terms are interpreted according to the value of the `writing-mode` property, making XSL-FO writing-system independent.

## Refinement

**Refinement** is the computational process that finalizes the specification of properties based on the attribute values in the XML result tree. Although the XML result tree and the formatting object tree have very similar structure, they are separate conceptual entities. Refinement involves:

- Propagating inherited values of properties (both implicitly inherited values and those with an attribute value of `inherit`).
- Evaluating expressions in property value specifications into actual values, which then determine the value of the properties.
- Converting relative numerics to absolute numerics.
- Constructing composite properties from more than one attribute.

Some of these operations (particularly evaluating expressions) depend on knowledge of the area tree. Therefore, refinement is not necessarily a straightforward sequential procedure; it may involve look-ahead, back-tracking, or control-splicing with other processes in the formatter.

## Summary of the Formatting Pipeline

Formatting proceeds by constructing an area tree (containing areas and their traits) that satisfies constraints based on information in the XML result tree (containing element nodes and their attributes). Conceptually, there are intermediate steps of constructing a formatting object tree (containing formatting objects and their properties) and refinement. These steps may proceed in an interleaved fashion during construction of the area tree.

## Conceptual Procedure

<!-- Source: https://www.w3.org/TR/xslfo20/#fo-jc-intro -->

The following is a conceptual description of how formatting could work. This conceptual procedure does not mandate any particular algorithms or data structures as long as the result obeys the implied constraints.

### Processing Model

The procedure works by processing formatting objects. Each object, while being processed, may initiate processing of other objects. The objects are hierarchically structured, but the processing is not -- processing of a given object is like a co-routine that may pass control to other processes and pick up again later where it left off. The procedure starts by initiating the processing of the `fo:root` formatting object.

### Area Creation and Return

Unless otherwise specified, processing a formatting object creates areas and returns them to its parent to be placed in the area tree. When given control, a formatting object:

1. Initiates or continues formatting of its own children (or a subset of them).
2. Supplies parameters to its children based on the traits of areas already in the area tree, possibly including areas generated by the formatting object or its ancestors.
3. Disposes of the areas returned by its formatting object children by either:
   - Returning such an area to its parent (always the case if the formatting object does not generate areas itself), or
   - Arranging the area in the area tree according to the semantics of the formatting object, which may involve changing its geometric position.
4. Terminates processing when all its children have terminated processing (if initiated) and it is finished generating areas.

Some formatting objects do not themselves generate areas; they simply return the areas returned to them by their children. Alternatively, a formatting object may continue to generate and return areas based on information discovered while formatting its own children. For example, `fo:page-sequence` continues generating pages as long as it contains a flow with unprocessed descendants.

Areas returned to `fo:root` are page-viewport-areas, placed as children of the area tree root in the order in which they are returned, with no geometrical implications.

### Ordering Guarantee

As a general rule, the order of the area tree parallels the order of the formatting object tree. If one formatting object precedes another in the depth-first traversal of the formatting object tree (with neither containing the other), then all the areas generated by the first will precede all the areas generated by the second in the depth-first traversal of the area tree, unless otherwise specified. Typical exceptions include side floats, before floats, and footnotes.

### Constraints, Not Algorithms

At the end of the procedure, the areas and their traits must satisfy constraints described in the definitions of their associated formatting objects and in the area model. Size and position of areas are subject to the placement and spacing constraints described in the area model, unless the formatting object definition indicates otherwise.

The formatting object definitions, property descriptions, and area model are **not algorithms**. The specification does not prescribe how line-breaking, word positioning, or line shifting must work. Rather, it assumes the formatter has performed these operations and describes the constraints the result must satisfy. An implementation may apply constraints at a time other than when formatting the formatting object to which the constraint applies. For example, the constraint given by the `hyphenate` property on `fo:character` would typically be used during line-building, not when processing the `fo:character` itself.

## Code Samples

No code samples in spec for this section.

## See Also

- `fo:root` -- The root formatting object where processing begins.
- `fo:page-sequence` -- Generates pages from flow content.
- `fo:block` -- A block-level formatting object.
- `fo:inline` -- An inline-level formatting object.
- `guide-area-model.md` -- The area tree model referenced throughout this section.
- `properties-writing-mode.md` -- The `writing-mode` property that determines direction interpretation.
