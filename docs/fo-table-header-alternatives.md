# fo:table-header-alternatives

## Summary

The `fo:table-header-alternatives` formatting object provides a mechanism for selecting alternative headers for tables. This formatting object allows a user to specify different instances of a table header depending on the different boundary conditions (page, column, and region). This also allows certain headers to be omitted at certain boundaries.

This is a new formatting object introduced in XSL-FO 2.0.

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_table-header-alternatives -->

## Areas

The `fo:table-header-alternatives` does not generate any areas directly. It returns the sequence of areas created by concatenating the sequences of areas returned by each of the children of the `fo:table-header-alternatives`.

## Constraints

The order of concatenation of the sequences of areas returned by the children of the `fo:table-header-alternatives` is the same order as the children of `fo:table-header-alternatives` select headers according to the conditions satisfied by the `header-position` property of those children.

## Content Model

```
(fo:conditional-table-header-reference+)
```

## Properties

This formatting object has no directly applicable properties. The selection behavior is controlled by the `header-position` property on the child `fo:conditional-table-header-reference` elements.

## Usage Notes

- Use `fo:table-header-alternatives` as a child of `fo:table-header` to provide context-dependent header content.
- Each child `fo:conditional-table-header-reference` specifies header rows to be used under specific boundary conditions (e.g., page break, column break).
- This allows tables to have a detailed header on the first occurrence and a more compact header on continuation pages.
- Multiple `fo:table-header-alternatives` elements may appear within a single `fo:table-header`, followed by the unconditional `fo:table-row` or `fo:table-cell` children.

## Code Samples

Table structure showing `fo:table-header-alternatives` with multiple `fo:conditional-table-header-reference` children, each specifying different header content for different boundary conditions (page, column):

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_ruby-text-container -->
```xml
<fo:table>
 <fo:table-header>
   <fo:table-header-alternatives>
     <fo:conditional-table-header-reference>
       ...
     </fo:conditional-table-header-reference>
     <fo:conditional-table-header-reference header-position="page">
       ...
     </fo:conditional-table-header-reference>
     <fo:conditional-table-header-reference header-position="column">
       ...
     </fo:conditional-table-header-reference>
     ...
   </fo:table-header-alternatives>
 </fo:table-header>
 <fo:table-footer>
   <fo:table-footer-alternatives>
   </fo:table-footer-alternatives>
 </fo:table-footer>
 <fo:table-body>
   ...
 </fo:table-body>
</fo:table>
```

## See Also

- [fo:table-header](fo-table-header.md) — the parent formatting object
- [fo:conditional-table-header-reference](fo-conditional-table-header-reference.md) — specifies conditional header content
- [fo:table-footer-alternatives](fo-table-footer-alternatives.md) — the equivalent for footers
- header-position property
