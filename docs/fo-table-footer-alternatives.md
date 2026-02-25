# fo:table-footer-alternatives

## Summary

The `fo:table-footer-alternatives` formatting object provides a mechanism for selecting alternative footers for tables. This formatting object allows a user to specify different instances of a table footer depending on the different boundary conditions (page, column, and region). This also allows certain footers to be omitted at certain boundaries.

This is a new formatting object introduced in XSL-FO 2.0.

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_table-footer-alternatives -->

## Areas

The `fo:table-footer-alternatives` does not generate any areas directly. It returns the sequence of areas created by concatenating the sequences of areas returned by each of the children of the `fo:table-footer-alternatives`.

## Constraints

The order of concatenation of the sequences of areas returned by the children of the `fo:table-footer-alternatives` is the same order as the children of `fo:table-footer-alternatives` select footers according to the conditions satisfied by the `footer-position` property of those children.

## Content Model

```
(fo:conditional-table-footer-reference+)
```

## Properties

This formatting object has no directly applicable properties. The selection behavior is controlled by the `footer-position` property on the child `fo:conditional-table-footer-reference` elements.

## Usage Notes

- Use `fo:table-footer-alternatives` as a child of `fo:table-footer` to provide context-dependent footer content.
- Each child `fo:conditional-table-footer-reference` specifies footer rows to be used under specific boundary conditions (e.g., page break, column break).
- This allows tables to have different footer content on continuation pages versus the final page (e.g., "continued on next page" footers).
- The mechanism is analogous to `fo:table-header-alternatives` but for the footer section.

## Code Samples

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_table-footer-alternatives -->
```xml
(conditional-table-footer-reference
+)
```

## See Also

- `fo:table-footer` -- the parent formatting object
- `fo:conditional-table-footer-reference` -- specifies conditional footer content
- `fo:table-header-alternatives` -- the equivalent for headers
- `footer-position` property
