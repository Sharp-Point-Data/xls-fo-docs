# Antenna House Configuration: CGM Settings

<!-- Source: XSL-FO-Reference-74-MID.pdf p.277 -->

## Overview

The `<cgm-settings>` element configures how AH Formatter handles CGM (Computer Graphics Metafile) content. These settings control behavior for unknown or unsupported CGM elements, default graphical properties, and font fallback. For full details, see "CGM Conformance" in the Conformance section of the AH Formatter Online Manual.

## Element: `<cgm-settings>`

**Parent:** `<formatter-config>`

**Attributes:** `issue-unknown-element`, `issue-unsupported-element`, `default-line-cap`, `default-edge-cap`, `default-line-join`, `default-edge-join`, `default-mitre-limit`, `default-restricted-text-type`, `fallback-font`, `aci`

**Child elements:** None

## Attributes

| Attribute | Description |
|-----------|-------------|
| `issue-unknown-element` | Controls behavior when an unknown CGM element is encountered. |
| `issue-unsupported-element` | Controls behavior when an unsupported CGM element is encountered. |
| `default-line-cap` | Specifies the default line cap style for CGM rendering. |
| `default-edge-cap` | Specifies the default edge cap style for CGM rendering. |
| `default-line-join` | Specifies the default line join style for CGM rendering. |
| `default-edge-join` | Specifies the default edge join style for CGM rendering. |
| `default-mitre-limit` | Specifies the default mitre limit for CGM rendering. |
| `default-restricted-text-type` | Specifies the default restricted text type for CGM rendering. |
| `fallback-font` | Specifies the fallback font to use when the requested CGM font is not available. |
| `aci` | Controls ACI (Abstract Character Identifier) handling in CGM content. |

## Code Samples

No code samples in the source for this section.
