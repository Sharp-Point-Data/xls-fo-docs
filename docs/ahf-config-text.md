# Antenna House Configuration: Text Output Settings

<!-- Source: XSL-FO-Reference-74-MID.pdf p.274 -->

## Overview

The `<text-settings>` element configures plain text output for AH Formatter. It controls the character encoding and line ending style of the text output. For additional details, see TEXT Output in Output Formats of the Online Manual.

## Element: `<text-settings>`

**Parent:** `<formatter-config>`

**Child elements:** none

## Attributes

### `encoding`

Specifies the encoding of the output text. The following encodings are available (case insensitive):

| Encoding | Notes |
|----------|-------|
| `UTF-8` | System setting (default) |
| `UTF-16` | Endianness depends on the processor/OS |
| `UTF-16BE` | Big-endian UTF-16 |
| `UTF-16LE` | Little-endian UTF-16 |
| `UTF-32` | Endianness depends on the processor/OS |
| `UTF-32BE` | Big-endian UTF-32 |
| `UTF-32LE` | Little-endian UTF-32 |
| `ISO-10646-UCS-2` | UCS-2 encoding |
| `ISO-10646-UCS-4` | UCS-4 encoding |
| `ANSI_X3.4` | ASCII |
| `ISO_646.irv` | ASCII (ISO 646) |
| `ISO646-US` | ASCII (US variant) |
| `US-ASCII` | ASCII |
| `ISO_8859-1` | Latin-1 |
| `latin1` | Latin-1 |
| `Windows-31J` | Windows Japanese |
| `Shift_JIS` | Shift JIS (Japanese) |
| `EUC-JP` | Extended Unix Code for Japanese |
| `ISO-2022-JP` | ISO 2022 Japanese |

- **Applies to:** `<text-settings>`
- **Values:** See encoding table above
- **Default:** `UTF-8`

### `eol-marker`

Specifies the line feed code of the output text. The following can be specified (case insensitive):

- `CRLF` — Carriage return + line feed (Windows style)
- `LF` — Line feed only (Unix/Linux/macOS style)
- `CR` — Carriage return only (legacy Mac style)

- **Applies to:** `<text-settings>`
- **Values:** `CRLF` | `LF` | `CR`
- **Default:** `CRLF` on Windows, `LF` on other platforms
