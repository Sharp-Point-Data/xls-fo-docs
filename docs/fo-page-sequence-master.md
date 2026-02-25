# fo:page-sequence-master

## Summary

The `fo:page-sequence-master` is used to specify the constraints on and the order in which a given set of page-masters will be used in generating a sequence of pages. Pages are automatically generated when the `fo:page-sequence-master` is used in formatting an `fo:page-sequence`.

There are several ways of specifying a potential sequence of pages: one can specify a sequence of references to particular page-masters (yielding a bounded sequence), specify a repeating sub-sequence of one or more page-masters (which can be bounded or unbounded), or intermix the two kinds of sub-sequence-specifiers.

## Areas

The `fo:page-sequence-master` formatting object generates no area directly. It is used by the `fo:page-sequence` formatting object to generate pages.

## Constraints

The children of the `fo:page-sequence-master` are a sequence of sub-sequence-specifiers. A page-sequence satisfies the constraint determined by an `fo:page-sequence-master` if:

1. It can be partitioned into a sequence of sub-sequences of pages that map one-to-one to an initial sub-sequence of the sequence of sub-sequence-specifiers that are the children of the `fo:page-sequence-master`.
2. For each sub-sequence of pages in the partition, that sub-sequence satisfies the constraints of the corresponding sub-sequence-specifier.

The sequence of sub-sequences of pages can be shorter than the sequence of sub-sequence-specifiers.

It is an error if the entire sequence of sub-sequence-specifiers children is exhausted while some areas returned by an `fo:flow` are not placed. Implementations may recover, if possible, by re-using the sub-sequence-specifier that was last used to generate a page.

## Content Model

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_page-sequence-master -->
```xml
(single-page-master-reference|repeatable-page-master-reference|repeatable-page-master-alternatives)+
```

The `fo:page-sequence-master` must contain one or more children, each of which is an `fo:single-page-master-reference`, `fo:repeatable-page-master-reference`, or `fo:repeatable-page-master-alternatives`.

## Properties

| Property | Type | Initial Value | Inherited | Conformance Level |
|---|---|---|---|---|
| master-name | `<name>` | an empty name | no, a value is required | Basic |

### Property Details

- **master-name**: Provides an identifying name for this page-sequence-master. This name is subsequently referenced as the value of `master-reference` on `fo:page-sequence` to request the use of this page-sequence-master when creating page instances. The name must be unique across all page-masters and page-sequence-masters within an `fo:layout-master-set`. It is an error if the name is empty or if a name-conflict is encountered.

## Usage Notes

The `fo:page-sequence-master` is the key mechanism for defining complex page layouts that vary across a sequence of pages. It acts as a state machine that determines which page-master to use for each successive page.

The three types of sub-sequence-specifiers provide different levels of control:

- **fo:single-page-master-reference**: Specifies exactly one page using a particular page-master. Useful for title pages or separator pages.
- **fo:repeatable-page-master-reference**: Specifies zero or more pages all using the same page-master. Useful for simple documents where all pages have the same layout.
- **fo:repeatable-page-master-alternatives**: Specifies zero or more pages where the page-master is selected conditionally based on page position (first, last, rest), parity (odd/even), or blank status. This is the most commonly used sub-sequence-specifier for book-style layouts.

Sub-sequence-specifiers are processed in order. Once a sub-sequence-specifier's conditions can no longer be satisfied (e.g., the maximum-repeats limit is reached), processing moves to the next sub-sequence-specifier. The last sub-sequence-specifier in the sequence typically uses `fo:repeatable-page-master-alternatives` with no repeat limit to handle any remaining pages.

## Code Samples

No code samples in spec for this formatting object's own section. However, `fo:page-sequence-master` appears in code samples in other spec sections:

<!-- Source: xslspec.xml line 5725 -->
```xml
<fo:page-sequence-master master-name="default-sequence">
  <fo:repeatable-page-master-reference master-reference="all-pages"/>
</fo:page-sequence-master>
```

This shows the simplest usage: a `fo:page-sequence-master` that repeats a single page-master indefinitely.

For comprehensive examples of conditional page layouts using `fo:page-sequence-master` with `fo:repeatable-page-master-alternatives`, including book chapter layouts, different first/odd/even/blank pages, and dynamic region sizing strategies, see **guide-conditional-page-layouts**.

## See Also

- fo:layout-master-set -- parent container
- fo:single-page-master-reference -- references a single page-master for one page
- fo:repeatable-page-master-reference -- references a page-master for repeated use
- fo:repeatable-page-master-alternatives -- conditional page-master selection
- fo:simple-page-master -- defines the actual page geometry
- fo:page-master -- defines arbitrary page geometry
- fo:page-sequence -- references this master via master-reference
