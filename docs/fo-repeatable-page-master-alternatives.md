# fo:repeatable-page-master-alternatives

## Summary

The `fo:repeatable-page-master-alternatives` formatting object is the most complex sub-sequence-specifier. It specifies a sub-sequence consisting of repeated instances of a set of alternative page-masters. The number of repetitions may be bounded or potentially unbounded. The repetitions may also be cyclic. Which of the alternative page-masters is used at any point in the sequence depends on the evaluation of a condition on the use of the alternative.

Typical conditions include testing whether the page being generated is:

- The first or last page in a page-sequence
- Blank
- The nth page in a page-sequence or a page cycle

The full set of conditions allows different page-masters to be used for the first page, for odd and even pages, for blank pages, etc.

## Areas

The `fo:repeatable-page-master-alternatives` formatting object generates no area directly. This formatting object is used by the `fo:page-sequence` formatting object to generate pages.

## Constraints

The children of the `fo:repeatable-page-master-alternatives` are `fo:conditional-page-master-reference` elements, called alternatives.

The sub-sequence of pages mapped to this sub-sequence-specifier satisfies the constraints if:

1. The sub-sequence of pages consists of zero or more pages.
2. Each page is generated using the `fo:simple-page-master` referenced by one of the alternatives that are children of the `fo:repeatable-page-master-alternatives`.
3. The conditions on that alternative are `true`.
4. That alternative is the first alternative in the sequence of children for which all the conditions are `true`.
5. The length of the sub-sequence is less than or equal to the value of `maximum-repeats`.

Because the conditions are tested in order from the beginning of the sequence of children, the last alternative in the sequence usually has a condition that is always true and this alternative references the page-master that is used for all pages that do not receive some specialized layout.

## Content Model

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_repeatable-page-master-alternatives -->
```xml
(conditional-page-master-reference+)
```

The `fo:repeatable-page-master-alternatives` must contain one or more `fo:conditional-page-master-reference` children.

## Properties

| Property | Type | Initial Value | Inherited | Conformance Level |
|---|---|---|---|---|
| maximum-repeats | `<number> \| no-limit \| inherit` | no-limit | no | Basic |
| sequence-repeats | `<number> \| no-limit \| inherit` | no-limit | no | Extended |

### Property Details

- **maximum-repeats**: Specifies the maximum number of pages in the sub-sequence. `no-limit` means no constraint. A numeric value is an integer >= 0 specifying the maximum page count. A value of 0 means this sub-sequence-specifier will not be used.
- **sequence-repeats**: Specifies the number of pages in a cyclic sub-sequence before the cycle repeats. `no-limit` means no cycling. A numeric value specifies the cycle length. This enables cyclic page-master selection patterns (e.g., for bulk-mailed correspondence that is to be folded by a folding machine).

## Usage Notes

The `fo:repeatable-page-master-alternatives` is the most commonly used sub-sequence-specifier for book-style layouts. It allows different page layouts based on page position and parity, which is essential for professional typesetting.

The child `fo:conditional-page-master-reference` elements are evaluated in document order for each page. The first alternative whose conditions all evaluate to `true` is selected. This means more specific conditions should be listed before more general ones.

A typical pattern for book chapter layouts:

1. First alternative: `page-position="first"` -- special first-page layout (e.g., no header, chapter title at top)
2. Second alternative: `blank-or-not-blank="blank"` -- layout for forced blank pages
3. Third alternative: `odd-or-even="odd"` -- right-hand page layout
4. Fourth alternative: `odd-or-even="even"` -- left-hand page layout
5. Last alternative: no conditions (or `page-position="any"`) -- fallback for any remaining pages

When `sequence-repeats` is set to a number, the page-position conditions are evaluated relative to the cycle position rather than the absolute page-sequence position. This enables repeating patterns such as 4-page signature layouts.

## Code Samples

No code samples in spec for this formatting object. The spec section contains only the content model declaration shown above.

## See Also

- fo:page-sequence-master -- parent container
- fo:conditional-page-master-reference -- child elements specifying conditions and page-master references
- fo:single-page-master-reference -- for exactly one page with a given master
- fo:repeatable-page-master-reference -- for unconditional repeated use of a single master
- fo:simple-page-master -- the page-master referenced by the alternatives
