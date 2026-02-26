# Antenna House Extension Properties: Revision Bar Properties

<!-- Source: XSL-FO-Reference-74-MID.pdf pp.312-476 -->

Properties for displaying revision bars (change bars) in the margin to indicate modified content.

## axf:revision-bar-color

Specifies the color of the revision bar displayed in the margin.

| Attribute | Value |
|---|---|
| **Applies to** | all block-level formatting objects |
| **Values** | &lt;color&gt; |
| **Initial** | black |
| **Inherited** | no |

## axf:revision-bar-offset

Specifies the offset distance of the revision bar from the edge of the content area.

| Attribute | Value |
|---|---|
| **Applies to** | all block-level formatting objects |
| **Values** | &lt;length&gt; |
| **Initial** | 2mm |
| **Inherited** | no |

## axf:revision-bar-position

Specifies the position of the revision bar relative to the content area.

Values have the following meanings:
- `start`: The revision bar is placed on the start side.
- `end`: The revision bar is placed on the end side.
- `inside`: The revision bar is placed on the inside (binding) side.
- `outside`: The revision bar is placed on the outside (fore-edge) side.
- `both`: The revision bar is placed on both sides.
- `alternate`: The revision bar alternates sides on odd and even pages.

| Attribute | Value |
|---|---|
| **Applies to** | all block-level formatting objects |
| **Values** | start \| end \| inside \| outside \| both \| alternate |
| **Initial** | start |
| **Inherited** | no |

## axf:revision-bar-style

Specifies the line style of the revision bar.

| Attribute | Value |
|---|---|
| **Applies to** | all block-level formatting objects |
| **Values** | &lt;border-style&gt; |
| **Initial** | solid |
| **Inherited** | no |

## axf:revision-bar-width

Specifies the line width of the revision bar.

| Attribute | Value |
|---|---|
| **Applies to** | all block-level formatting objects |
| **Values** | &lt;border-width&gt; |
| **Initial** | 0.5pt |
| **Inherited** | no |
