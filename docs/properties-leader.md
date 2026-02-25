# Leader and Rule Properties

<!-- Source: https://www.w3.org/TR/xslfo20/#leader-alignment -->

## Overview

The leader and rule properties control the appearance and behavior of `fo:leader` formatting objects. Leaders are used to fill space between content, commonly in tables of contents (dot leaders between titles and page numbers) and in forms (rule leaders for fill-in lines). These properties govern the leader's fill pattern, alignment, length, and the style/thickness of rules.

All leader and rule properties are inherited and apply exclusively to `fo:leader`.

## Properties

### leader-alignment

| Field | Value |
|---|---|
| **Values** | `none \| reference-area \| page \| inherit` |
| **Initial** | `none` |
| **Applies to** | fo:leader |
| **Inherited** | Yes |
| **Percentages** | N/A |

Specifies whether `fo:leader`s having identical content and property values shall have their patterns aligned with each other, with respect to their common reference-area or page.

For `fo:leader`s where the `leader-pattern` property is specified as "dot" or as "use-content", this property will be honored.

If the `fo:leader` is aligned, the start-edge of each cycle of the repeated pattern will be placed on the start-edge of the next cycle in the appropriate pattern-alignment grid.

Values have the following meanings:

- **none** -- Leader-pattern has no special alignment.
- **reference-area** -- Leader-pattern is aligned as if it began on the current reference-area's content-rectangle start-edge.
- **page** -- Leader-pattern is aligned as if it began on the current page's start-edge.

### leader-pattern

| Field | Value |
|---|---|
| **Values** | `space \| rule \| dots \| use-content \| inherit` |
| **Initial** | `space` |
| **Applies to** | fo:leader |
| **Inherited** | Yes |
| **Percentages** | N/A |

Provides the specification of how to fill in the leader.

If the leader is aligned, the start-edge of each cycle of each repeating pattern component will be placed on the start-edge of the next cycle in the pattern-alignment grid.

Implementations must support the "space", "rule", and "dots" values, as defined in this Recommendation. The "use-content" value may be treated as if "space" had been specified.

Values have the following meanings:

- **space** -- Leader is to be filled with blank space.
- **rule** -- Leader is to be filled with a rule. If this choice is selected, the `rule-thickness` and `rule-style` properties are used to set the leader's style.
- **dots** -- Leader is to be filled with a repeating sequence of dots. The choice of dot character is dependent on the user agent.
- **use-content** -- Leader is to be filled with a repeating pattern as specified by the children of the `fo:leader`.

### leader-pattern-width

| Field | Value |
|---|---|
| **Values** | `use-font-metrics \| <length> \| <percentage> \| inherit` |
| **Initial** | `use-font-metrics` |
| **Applies to** | fo:leader |
| **Inherited** | Yes |
| **Percentages** | refer to the inline-progression-dimension of content-rectangle of parent area |

Specifies the length of each repeat cycle in a repeating leader.

For leaders where the `leader-pattern` property is specified as "dots" or as "use-content", this property will be honored.

Values have the following meanings:

- **use-font-metrics** -- Use the width of the `leader-pattern` as determined from its font metrics.
- **\<length\>** -- Sets length for leader-pattern-repeating. The leader will have an inline-space inserted after each pattern cycle to account for any difference between the width of the pattern as determined by the font metrics and the width specified in this property. If the length specified is less than the value that would be determined via the use-font-metrics choice, the value of this property is computed as if use-font-metrics choice had been specified.

### leader-length

| Field | Value |
|---|---|
| **Values** | `<length-range> \| <percentage> \| inherit` |
| **Initial** | `leader-length.minimum=0pt, .optimum=12.0pt, .maximum=100%` |
| **Applies to** | fo:leader |
| **Inherited** | Yes |
| **Percentages** | refer to the inline-progression-dimension of content-rectangle of parent area |

Specifies the minimum, optimum, and maximum length of an `fo:leader`.

This property constrains the length of the leader to be between the minimum and maximum lengths.

Values have the following meanings:

- **\<length-range\>** -- leader-length.minimum sets the minimum length for a leader; leader-length.optimum sets the optimum length for a leader; leader-length.maximum sets the maximum length for a leader.

User agents may choose to use the value of "leader-length.optimum" to determine where to break the line, then use the minimum and maximum values during line justification.

As with all other space and formatting objects within a line area whose `inline-progression-dimension` provides minimum/optimum/maximum constraints, a leader formatting object's length-range provides further flexibility to the justification process. Though any result that satisfies the specified constraints would conform to this specification, current typographic practice would tend to make use of leader length flexibility in preference to other flexibility (e.g. word spaces) within the same line area when justifying the line. If multiple leader formatting objects occur within the same line area, current typographic practice would tend to make use of the length flexibility of all of them in some implementation defined manner (e.g. equally or proportionally to the specified leader-length.maximum values).

### rule-style

| Field | Value |
|---|---|
| **Values** | `none \| dotted \| dashed \| solid \| double \| groove \| ridge \| inherit` |
| **Initial** | `solid` |
| **Applies to** | fo:leader |
| **Inherited** | Yes |
| **Percentages** | N/A |

Specifies the style (pattern) of the rule. This property applies only if the `leader-pattern` property is specified as "rule".

Implementations must support the "none" and "solid" values, as defined in this Recommendation. Other values may be treated as if "solid" had been specified.

Values have the following meanings:

- **none** -- No rule, forces `rule-thickness` to 0.
- **dotted** -- The rule is a series of dots.
- **dashed** -- The rule is a series of short line segments.
- **solid** -- The rule is a single line segment.
- **double** -- The rule is two solid lines. The sum of the two lines and the space between them equals the value of `rule-thickness`.
- **groove** -- The rule looks as though it were carved into the canvas. (Top/left half of the rule's thickness is the color specified; the other half is white.)
- **ridge** -- The opposite of "groove", the rule looks as though it were coming out of the canvas. (Bottom/right half of the rule's thickness is the color specified; the other half is white.)

### rule-thickness

| Field | Value |
|---|---|
| **Values** | `<length>` |
| **Initial** | `1.0pt` |
| **Applies to** | fo:leader |
| **Inherited** | Yes |
| **Percentages** | N/A |

Specifies the overall thickness of the rule. This property applies only if the `leader-pattern` property is specified as "rule".

Values have the following meanings:

- **\<length\>** -- The `rule-thickness` is always perpendicular to its length-axis. The rule is thickened equally above and below the line's alignment position. This can be adjusted through the `baseline-shift` property.

## Code Samples

### Leader length value example

<!-- Source: https://www.w3.org/TR/xslfo20/#leader-length -->
```xml
leader-length.minimum="0pt"
leader-length.optimum="12pt"
leader-length.maximum="100%"
```

This example shows leader length values that would cause the leader to fill all available space within the current line area as part of the process of justifying that line area.

## See Also

- [fo-leader](fo-leader.md) -- The `fo:leader` formatting object
- [properties-hyphenation](properties-hyphenation.md) -- Hyphenation properties (related inline formatting)
