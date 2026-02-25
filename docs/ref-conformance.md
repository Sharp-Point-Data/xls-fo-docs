# Conformance

<!-- Source: https://www.w3.org/TR/xslfo20/#conform -->

## Overview

The XSL-FO specification defines three levels of conformance that classify formatting objects and properties by implementation complexity. Conformance levels allow processors to declare partial but well-defined support for the specification. An application claims conformance to one of these levels and must implement all formatting objects and properties assigned to that level for its target medium.

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in the conformance section are interpreted as described in RFC 2119.

## Conformance Levels

The specification defines three levels, in order of completeness:

### Basic

Includes the set of formatting objects and properties needed to support a minimum level of pagination or aural rendering. This is the minimum level of conformance. A minimally conformant implementation must process as specified all the formatting objects and properties defined for the Basic level of the implementation's target medium.

### Extended

Includes everything except shorthands. It is intended for applications whose goal is to provide sophisticated pagination.

### Complete

Includes everything (all formatting objects, all properties, all shorthands).

## Conformance Requirements

1. **Level-based obligation:** An application that claims conformance to a given level must implement all the formatting objects and properties that apply to it for a given medium.

2. **Medium-specific:** Conformance applies per medium. The specification defines two media classes: **visual** and **aural**. For some formatting objects, the visual class is further subdivided into interactive and non-interactive media. An implementation conforms for its target medium and must implement the formatting objects and properties designated at its claimed level for that medium.

3. **Fallback does not constitute conformance:** The specification defines a fallback for each formatting object in the Extended and Complete levels. An implementation must not claim conformance to a given level if any of the formatting objects at that level is implemented solely as the fallback specified for that level. Correct processing of fallbacks does not constitute conformance.

4. **Implementations may exceed their level:** Implementations may choose to process formatting objects from levels or target media other than the one to which they conform.

5. **Writing-mode support:** Conforming implementations must support at least one of the `writing-mode` values defined in the specification. Although `writing-mode` is defined as a Basic property with an initial value of `lr-tb`, the specification does not impose this particular (or any other) writing-mode value on conformant applications. If an implementation does not support a `writing-mode` used in a stylesheet (whether set explicitly or relied upon via the initial value), it should display either a missing-character glyph message or some indication that the content cannot be correctly rendered.

## Where Conformance Levels Are Assigned

- **Formatting objects:** The Formatting Object Summary (Appendix A / section `FO-summary`) specifies which formatting objects belong to each conformance level, broken out by medium (visual and aural), and includes a proposed fallback treatment for Extended and Complete formatting objects.
- **Properties:** The Property Index (Appendix B / section `property-index`) specifies which properties belong to each conformance level.

## Code Samples

No code samples in spec for this section.

## See Also

- Formatting Object Summary (`FO-summary`) — conformance level assignments for each formatting object
- Property Index (`property-index`) — conformance level assignments for each property
- RFC 2119 — key word definitions for requirement levels
