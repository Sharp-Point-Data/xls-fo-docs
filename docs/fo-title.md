# fo:title

## Summary

The `fo:title` formatting object is used to associate a title with a given page-sequence. This title may be used by an interactive User Agent to identify the pages. For example, the content of the `fo:title` can be formatted and displayed in a "title" window or in a "tool tip".

## Areas

This formatting object returns the sequence of areas returned by the children of this formatting object.

## Content Model

```
(#PCDATA|%inline;)*
```

The `fo:title` may contain text and/or inline-level formatting objects. It accepts character data directly or any inline-level formatting objects.

An `fo:title` is not permitted to have an `fo:float`, `fo:footnote`, or `fo:marker` as a descendant.

Additionally, an `fo:title` is not permitted to have as a descendant an `fo:block-container` that generates an absolutely positioned area.

## Properties

| Property | Type | Inherited | Conformance Level |
|---|---|---|---|
| Common Accessibility Properties | | No | Basic |
| Common Aural Properties | | Various | Extended |
| Common Border, Padding, and Background Properties | | Various | Basic |
| Common Font Properties | | Yes | Basic |
| Common Margin Properties - Inline | | No | Basic |
| color | \<color\> \| inherit | Yes | Basic |
| line-height | normal \| \<length\> \| \<number\> \| \<percentage\> \| \<space\> \| inherit | Yes | Basic |
| visibility | visible \| hidden \| collapse \| inherit | No | Extended |

## Constraints

The sequence of returned areas must be the concatenation of the sub-sequences of areas returned by each of the flow children of the `fo:title` formatting object in the order in which the children occur.

## Usage Notes

- The `fo:title` is an optional child of `fo:page-sequence`. If present, it must appear before any `fo:static-content` or `fo:flow` children.
- The title content is metadata-like -- it does not appear in the normal page flow. Its presentation depends on the User Agent (e.g., it may appear in a window title bar or tooltip).
- Only inline-level content is allowed. Block-level formatting objects are not permitted as children of `fo:title`.
- The restrictions on descendants (no `fo:float`, `fo:footnote`, `fo:marker`, or absolutely positioned `fo:block-container`) exist because the title is not part of the normal page flow and these objects require a pagination context.
- Font properties, color, and line-height can be specified to control the rendering of the title content by the User Agent.

## Code Samples

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_title -->
```xml
(#PCDATA|%inline;)*
```

## See Also

- `fo:page-sequence` -- parent formatting object that contains the title
- `fo:flow` -- the main flowing content of the page-sequence
- `fo:static-content` -- repeating content for headers and footers
