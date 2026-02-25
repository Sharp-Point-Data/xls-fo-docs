# Spaces and Conditionality

## Overview

Space resolution is one of the most complex topics in XSL-FO. When adjacent formatting objects each specify space properties (`space-before`, `space-after`, `space-start`, `space-end`), their space-specifiers interact through a set of resolution rules that determine the actual spacing. These rules account for conditionality (whether space is suppressed at the edges of reference-areas and line-areas), precedence (which space-specifier wins when multiple compete), and forcing behavior. Mastering space resolution is essential for achieving precise control over vertical and horizontal spacing in paginated output.

<!-- Source: https://www.w3.org/TR/xslfo20/#spacecond -->

## The Space-Specifier Compound Datatype

A **space-specifier** is a compound datatype with five components:

| Component | Type | Description |
|---|---|---|
| `minimum` | `<length>` | The minimum acceptable distance. May be negative (can cause overlap). |
| `optimum` | `<length>` | The preferred distance. |
| `maximum` | `<length>` | The maximum acceptable distance. May be negative. |
| `conditionality` | `discard` or `retain` | Controls whether the space is suppressed at reference-area or line-area boundaries. |
| `precedence` | `<integer>` or `force` | Controls which space-specifier prevails when multiple compete. |

The minimum must be less than or equal to the optimum, and the optimum must be less than or equal to the maximum.

A **conditional** space-specifier is one whose conditionality is `discard`. A **forcing** space-specifier is one whose precedence is `force`.

## How Space-Specifiers Interact

Space-specifiers occurring in sequence may interact with each other. The constraint imposed by a sequence of space-specifiers is computed by calculating for each space-specifier its associated **resolved space-specifier** in accordance with conditionality and precedence, as defined by the space-resolution rules below.

The constraint imposed on a distance by a sequence of resolved space-specifiers is **additive**: the distance is constrained to be no less than the sum of the resolved minimum values and no larger than the sum of the resolved maximum values.

## Space-Resolution Rules

<!-- Source: https://www.w3.org/TR/xslfo20/#area-space -->

The resolved space-specifier of a given space-specifier `S` is computed as follows.

### Determining the Relevant Subsequence

Consider the maximal inline-stacking constraint or block-stacking constraint `S''` containing the space-specifier `S` as an element of the sequence (`S''` is a sequence of space-specifiers; see the Stacking Constraints section of the area model). Define `S'` to be a subsequence of `S''` as follows:

- If `S` is the `space-before` or `space-after` of a **line-area**, then `S'` is the maximal subsequence of `S''` containing `S` such that all the space-specifiers in `S'` are traits of line-areas.
- If `S` is the `space-before` or `space-after` of a **block-area which is not a line-area**, then `S'` is the maximal subsequence of `S''` containing `S` such that all the space-specifiers in `S'` are traits of block-areas which are not line-areas.
- If `S` is the `space-start` or `space-end` of an **inline-area**, then `S'` is all of `S''`.

The resolved space-specifier of `S` is a non-conditional, forcing space-specifier computed in terms of the sequence `S'`.

### Rule 1: Conditional Suppression at Boundaries

If any of the space-specifiers in `S'` is conditional and **begins** a reference-area or line-area, then it is **suppressed** (its resolved space-specifier is zero). Further, any conditional space-specifiers which **consecutively follow** it in the sequence are also suppressed.

A space-specifier `U` **consecutively follows** a space-specifier `V` if `U` follows `V` and `U` and `V` are separated in the sequence only by conditional space-specifiers and/or space-specifiers whose computed minimum, optimum, and maximum values are zero.

Symmetrically, if a conditional space-specifier **ends** a reference-area or line-area, then it is suppressed together with any other conditional space-specifiers which **consecutively precede** it in the sequence. A space-specifier `U` **consecutively precedes** a space-specifier `V` if `U` precedes `V` and `U` and `V` are separated in the sequence only by conditional space-specifiers and/or space-specifiers whose computed minimum, optimum, and maximum values are zero.

### Rule 2: Forcing Space-Specifiers

If any of the remaining (non-suppressed) space-specifiers in `S'` is forcing (precedence is `force`), all non-forcing space-specifiers are suppressed, and the value of each forcing space-specifier is taken as its resolved value.

### Rule 3: Non-Forcing Precedence Resolution

If all of the remaining space-specifiers in `S'` are non-forcing, then the resolved space-specifier is defined in terms of those non-suppressed space-specifiers whose precedence is numerically highest, and among these, those whose optimum value is the greatest. All other space-specifiers are suppressed. If there is only one such space-specifier, its value is taken as its resolved value.

When there are two or more space-specifiers all of the same highest precedence and the same largest optimum, the resolved space-specifier of the **last** space-specifier in the sequence is derived from these spaces by:

- Taking their common optimum value as its optimum.
- Taking the greatest of their minimum values as its minimum.
- Taking the least of their maximum values as its maximum.

All other space-specifiers in the tie are suppressed.

### Rule 4: Overconstrainment Relaxing

If `S` is subject to overconstrainment relaxing, then its maximum value is set to the actual `block-progression-dimension` of the containing block-area. See the Overconstrained Space-Specifiers section below.

## Worked Example from Spec

The following example is provided in the specification to illustrate space resolution.

Suppose the sequence of space values occurring at the beginning of a reference-area is:

1. A space with value 10 points (minimum, optimum, and maximum all equal to 10pt) and conditionality `discard`.
2. A space with value 4 points and conditionality `retain`.
3. A space with value 5 points and conditionality `discard`.

All three spaces have precedence zero.

Resolution:

- The first (10pt) space is **suppressed under Rule 1** because it is conditional and begins a reference-area.
- The third (5pt) space is conditional but is not consecutively following the first (the 4pt `retain` space intervenes), so it is not suppressed by Rule 1.
- Under Rule 3, the second (4pt) space is **suppressed** because the third (5pt) space has a greater optimum at the same precedence.
- The resolved value of the third space is a non-conditional 5 points, even though it originally came from a conditional space.

## Interaction with Padding and Borders

The `padding` of a block-area does not interact with any space-specifier, except that by definition the presence of padding at the before-edge or after-edge prevents areas on either side of it from having a stacking constraint.

### Conditional Borders and Padding on Block-Areas

The `border` or `padding` at the before-edge or after-edge of a block-area `B` may be specified as conditional. If so:

- It is set to zero if its associated edge is a **leading** edge in a reference-area and the `is-first` trait of `B` is `false`.
- It is set to zero if its associated edge is a **trailing** edge in a reference-area and the `is-last` trait of `B` is `false`.

In either case, the border or padding is taken to be zero for purposes of the stacking constraint definitions.

### Conditional Borders and Padding on Inline-Areas

The `border` or `padding` at the start-edge or end-edge of an inline-area `I` may be specified as conditional. If so:

- It is set to zero if its associated edge is a **leading** edge in a line-area and the `is-first` trait of `I` is `false`.
- It is set to zero if its associated edge is a **trailing** edge in a line-area and the `is-last` trait of `I` is `false`.

In either case, the border or padding is taken to be zero for purposes of the stacking constraint definitions.

## Overconstrained Space-Specifiers

<!-- Source: https://www.w3.org/TR/xslfo20/#bpd-slack -->

When an area `P` is generated by a formatting object whose `block-progression-dimension` is `auto`, the constraints involving the before-edge and after-edge of the content-rectangle of `P`, together with the constraints between the various descendants of `P`, result in a constraint on the actual value of the block-progression-dimension.

If the `block-progression-dimension` is instead specified as a length, this might result in an **overconstrained area tree** -- for example, an incompletely-filled `fo:block` with a specified size. In that case, some constraints between `P` and its descendants should be relaxed. Those that are eligible for this treatment are said to be **subject to overconstrainment relaxing**, and are treated as described in Rule 4 above (the maximum value is set to the actual `block-progression-dimension` of the containing block-area).

The rules for determining which spaces are subject to overconstrainment relaxing depend on the `display-align` property:

- If the `display-align` value is `after` or `center` and `P` is the **first** normal area generated by the formatting object, then the `space-before` of the first normal child of `P` is subject to overconstrainment relaxing.
- If the `display-align` value is `before` or `center` and `P` is the **last** normal area generated by the formatting object, then the `space-after` of the last normal child of `P` is subject to overconstrainment relaxing.

This mechanism allows a formatter to distribute remaining space when content does not fill a fixed-size container, with the distribution controlled by the `display-align` property.

## Code Samples

No code samples in spec for this section.

## See Also

- [guide-area-model.md](guide-area-model.md) -- Area model concepts including stacking constraints and reference-areas
- [guide-datatypes.md](guide-datatypes.md) -- The `<space>` compound datatype with its minimum, optimum, maximum, conditionality, and precedence components
- [guide-keeps-breaks.md](guide-keeps-breaks.md) -- Keeps and breaks that interact with page and column boundaries where conditionality applies
- [properties-keeps-breaks.md](properties-keeps-breaks.md) -- Property definitions for keeps and breaks
