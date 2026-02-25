# Internationalization and Writing-Modes

## Overview

XSL-FO uses a **relative frame of reference** rather than an absolute one (top, bottom, left, right) for formatting object and property descriptions. This design enables correct formatting of scripts that do not follow left-to-right, top-to-bottom conventions -- such as Far Eastern scripts that proceed top-to-bottom with lines stacking right-to-left. The `writing-mode` property controls these directions, making the entire formatting model writing-system independent.

This concept is fundamental to XSL-FO: properties like `space-before`, `space-after`, `start-indent`, and `end-indent` are all defined relative to the writing-mode, not to physical page edges.

<!-- Source: xslspec.xml line 604 -->

## Relative Directional Framework

Properties expressed in terms of a fixed, absolute frame of reference (using top, bottom, left, and right) and which apply only to a notion of words proceeding from left to right or right to left do not generalize well to scripts written in other directions. For this reason, XSL (and before it DSSSL) uses a relative frame of reference for the formatting object and property descriptions.

Just as the CSS2 frame of reference has four directions (top, bottom, left, and right), so does the XSL relative frame of reference have four directions: **before**, **after**, **start**, and **end**. These are relative to the `writing-mode` property.

| Relative Direction | Meaning |
|---|---|
| `before` | Start of the block-progression-direction |
| `after` | End of the block-progression-direction |
| `start` | Start of the inline-progression-direction |
| `end` | End of the inline-progression-direction |

## The writing-mode Property

The `writing-mode` property is a way of controlling the directions needed by a formatter to correctly place glyphs, words, lines, blocks, etc. on the page or screen. Typically, the `writing-mode` value specifies two directions:

1. The **inline-progression-direction** -- determines the direction in which words will be placed.
2. The **block-progression-direction** -- determines the direction in which blocks (and lines) are placed one after another.

The spec defines several `writing-mode` values:

| Value | Meaning |
|---|---|
| `lr-tb` | Left-to-right inline, top-to-bottom block |
| `rl-tb` | Right-to-left inline, top-to-bottom block |
| `tb-rl` | Top-to-bottom inline, right-to-left block |

In addition, the inline-progression-direction for a sequence of characters may be implicitly determined using bidirectional character types for those characters from the Unicode Character Database and the Unicode bidirectional (BIDI) algorithm.

## Additional Directions

Besides the directions that are explicit in the name of the value of the `writing-mode` property, the `writing-mode` determines other directions needed by the formatter, such as the **shift-direction** (used for subscripts and superscripts).

## Code Samples

No code samples in spec for this section.

## See Also

- [properties-writing-mode.md](properties-writing-mode.md) -- The `writing-mode` property definition and its values
- [guide-introduction.md](guide-introduction.md) -- Parent chapter: Introduction and Overview of XSL
- [guide-formatting-intro.md](guide-formatting-intro.md) -- How relative directions apply in the formatting model
- [guide-area-model.md](guide-area-model.md) -- Area model where relative directions are used for spacing and positioning
