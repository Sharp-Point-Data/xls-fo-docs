# fo:bookmark-tree

## Summary

The `fo:bookmark-tree` formatting object is used to hold a list of access points within the document such as a table of contents, a list of figures or tables, etc. Each access point is called a bookmark.

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_bookmark-tree -->

## Areas

This formatting object returns the sequence of areas returned by the children of this formatting object.

## Constraints

The sequence of returned areas must be the concatenation of the sub-sequences of areas returned by each of the flow children of the `fo:bookmark-tree` formatting object in the order in which the children occur.

## Content Model

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_bookmark-tree -->
```xml
(bookmark+)
```

## Properties

This formatting object has no specific properties.

## Usage Notes

- The `fo:bookmark-tree` is a child of `fo:root` and serves as the container for all bookmarks in the document.
- Bookmarks typically appear as a hierarchical navigation panel in PDF viewers, allowing quick access to different sections of the document.
- The `fo:bookmark-tree` must contain one or more `fo:bookmark` children. Each `fo:bookmark` can in turn contain nested `fo:bookmark` children to create a hierarchical structure.

## Code Samples

No code samples in spec for this formatting object. For complete examples of `fo:bookmark-tree` usage including hierarchical bookmark structures, styling with `fo:bookmark-title` properties, `starting-state` control, and XSLT-generated bookmarks, see **guide-bookmarks**.

## See Also

- `fo:bookmark` -- child formatting object representing an individual bookmark entry
- `fo:bookmark-title` -- grandchild providing the human-readable title for a bookmark
- `fo:root` -- parent formatting object
