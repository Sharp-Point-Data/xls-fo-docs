# fo:bookmark

## Summary

The `fo:bookmark` formatting object is used to identify an access point, by name, and to specify where that access point is within the current document or another external document. A given bookmark may be further subdivided into a sequence of (sub-)bookmarks to as many levels as the authors desire.

The `fo:bookmark` is a specialized form of the `fo:basic-link` with restrictions on the applicable properties and on its content model.

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_bookmark -->

## Areas

The `fo:bookmark` formatting object generates one or more normal inline-areas. The `fo:bookmark` returns these areas.

## Constraints

- One of the `external-destination` and `internal-destination` properties should be specified. If both are specified, the system may either report it as an error, or use the `internal-destination` property.
- No area may have more than one normal child area returned by the same `fo:bookmark` formatting object.
- The children of each normal area returned by an `fo:bookmark` must satisfy the constraints specified in the inline building section.
- The property `starting-state` determines whether any sub-list of bookmarks is initially displayed or is hidden. The value "show" means include the sub-list of bookmarks in the presentation of this bookmark. The value "hide" means show only this bookmark in the presentation.

## Content Model

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_bookmark -->
```xml
(bookmark-title,bookmark*)
```

## Properties

| Property | Inherited | Conformance Level |
|---|---|---|
| Common Accessibility Properties | N/A | Basic |
| `external-destination` | no | Basic |
| `internal-destination` | no | Basic |
| `starting-state` | no | Extended |

## Usage Notes

- Each `fo:bookmark` must contain exactly one `fo:bookmark-title` child (providing the human-readable label) followed by zero or more `fo:bookmark` children (providing sub-bookmarks).
- Use `internal-destination` to link to a location within the same document by specifying an `id` value. Use `external-destination` for links to external resources.
- The `starting-state` property controls the initial display of sub-bookmarks. Set to "show" to have sub-bookmarks visible by default, or "hide" to collapse them initially.
- Bookmarks create a hierarchical navigation structure that is typically rendered as a sidebar panel in PDF viewers.

## Code Samples

No code samples in spec for this formatting object. For complete examples of `fo:bookmark` usage including hierarchical nesting, `internal-destination` linking, `external-destination`, `starting-state` expand/collapse control, and XSLT-generated bookmarks, see **guide-bookmarks**.

## See Also

- [fo:bookmark-tree](fo-bookmark-tree.md) — parent formatting object containing all bookmarks
- [fo:bookmark-title](fo-bookmark-title.md) — child providing the display text of the bookmark
- [fo:basic-link](fo-basic-link.md) — general-purpose link formatting object (of which fo:bookmark is a specialized form)
