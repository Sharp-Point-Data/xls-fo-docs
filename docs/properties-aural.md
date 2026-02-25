# Aural Properties

## Overview

<!-- Source: https://www.w3.org/TR/xslfo20/#common-aural-properties -->

The common aural properties control the rendering of formatting objects in aural (speech) media. These properties are taken from CSS2 and govern characteristics such as spatial sound positioning, speech rate, voice characteristics, volume, and auditory cues. They apply to most formatting objects that accept the common aural properties group.

All aural properties have media type "aural" unless otherwise noted.

## Properties

### azimuth

| Field | Value |
|---|---|
| **Values** | `<angle> \| [[ left-side \| far-left \| left \| center-left \| center \| center-right \| right \| far-right \| right-side ] \|\| behind ] \| leftwards \| rightwards \| inherit` |
| **Initial** | `center` |
| **Applies to** | all formatting objects that accept common aural properties |
| **Inherited** | Yes |
| **Percentages** | N/A |
| **Media** | aural |

<!-- Source: https://www.w3.org/TR/xslfo20/#azimuth -->

CSS2 Definition. Specifies the horizontal angle from which the sound originates.

### cue-after

| Field | Value |
|---|---|
| **Values** | `<uri-specification> \| none \| inherit` |
| **Initial** | `none` |
| **Applies to** | all formatting objects that accept common aural properties |
| **Inherited** | No |
| **Percentages** | N/A |
| **Media** | aural |

<!-- Source: https://www.w3.org/TR/xslfo20/#cue-after -->

CSS2 Definition. Specifies a sound to be played after speaking an element's content.

**XSL modifications to the CSS definition:** The \<uri\> value has been changed to a \<uri-specification\>.

### cue-before

| Field | Value |
|---|---|
| **Values** | `<uri-specification> \| none \| inherit` |
| **Initial** | `none` |
| **Applies to** | all formatting objects that accept common aural properties |
| **Inherited** | No |
| **Percentages** | N/A |
| **Media** | aural |

<!-- Source: https://www.w3.org/TR/xslfo20/#cue-before -->

CSS2 Definition. Specifies a sound to be played before speaking an element's content.

**XSL modifications to the CSS definition:** The \<uri\> value has been changed to a \<uri-specification\>.

### elevation

| Field | Value |
|---|---|
| **Values** | `<angle> \| below \| level \| above \| higher \| lower \| inherit` |
| **Initial** | `level` |
| **Applies to** | all formatting objects that accept common aural properties |
| **Inherited** | Yes |
| **Percentages** | N/A |
| **Media** | aural |

<!-- Source: https://www.w3.org/TR/xslfo20/#elevation -->

CSS2 Definition. Specifies the vertical angle from which the sound originates.

### pause-after

| Field | Value |
|---|---|
| **Values** | `<time> \| <percentage> \| inherit` |
| **Initial** | depends on user agent |
| **Applies to** | all formatting objects that accept common aural properties |
| **Inherited** | No |
| **Percentages** | see prose (CSS2 specification) |
| **Media** | aural |

<!-- Source: https://www.w3.org/TR/xslfo20/#pause-after -->

CSS2 Definition. Specifies a pause to be observed after speaking an element's content.

### pause-before

| Field | Value |
|---|---|
| **Values** | `<time> \| <percentage> \| inherit` |
| **Initial** | depends on user agent |
| **Applies to** | all formatting objects that accept common aural properties |
| **Inherited** | No |
| **Percentages** | see prose (CSS2 specification) |
| **Media** | aural |

<!-- Source: https://www.w3.org/TR/xslfo20/#pause-before -->

CSS2 Definition. Specifies a pause to be observed before speaking an element's content.

### pitch

| Field | Value |
|---|---|
| **Values** | `<frequency> \| x-low \| low \| medium \| high \| x-high \| inherit` |
| **Initial** | `medium` |
| **Applies to** | all formatting objects that accept common aural properties |
| **Inherited** | Yes |
| **Percentages** | N/A |
| **Media** | aural |

<!-- Source: https://www.w3.org/TR/xslfo20/#pitch -->

CSS2 Definition. Specifies the average pitch (a frequency) of the speaking voice.

### pitch-range

| Field | Value |
|---|---|
| **Values** | `<number> \| inherit` |
| **Initial** | `50` |
| **Applies to** | all formatting objects that accept common aural properties |
| **Inherited** | Yes |
| **Percentages** | N/A |
| **Media** | aural |

<!-- Source: https://www.w3.org/TR/xslfo20/#pitch-range -->

CSS2 Definition. Specifies variation in average pitch of the speaking voice.

### play-during

| Field | Value |
|---|---|
| **Values** | `<uri-specification> mix? repeat? \| auto \| none \| inherit` |
| **Initial** | `auto` |
| **Applies to** | all formatting objects that accept common aural properties |
| **Inherited** | No |
| **Percentages** | N/A |
| **Media** | aural |

<!-- Source: https://www.w3.org/TR/xslfo20/#play-during -->

CSS2 Definition. Specifies a sound to be played as a background while an element's content is spoken.

**XSL modifications to the CSS definition:** The \<uri\> value has been changed to a \<uri-specification\>.

### richness

| Field | Value |
|---|---|
| **Values** | `<number> \| inherit` |
| **Initial** | `50` |
| **Applies to** | all formatting objects that accept common aural properties |
| **Inherited** | Yes |
| **Percentages** | N/A |
| **Media** | aural |

<!-- Source: https://www.w3.org/TR/xslfo20/#richness -->

CSS2 Definition. Specifies the richness, or brightness, of the speaking voice.

### speak

| Field | Value |
|---|---|
| **Values** | `normal \| none \| spell-out \| inherit` |
| **Initial** | `normal` |
| **Applies to** | all formatting objects that accept common aural properties |
| **Inherited** | Yes |
| **Percentages** | N/A |
| **Media** | aural |

<!-- Source: https://www.w3.org/TR/xslfo20/#speak -->

CSS2 Definition. Specifies whether text will be rendered aurally and in what manner.

### speak-header

| Field | Value |
|---|---|
| **Values** | `once \| always \| inherit` |
| **Initial** | `once` |
| **Applies to** | all formatting objects that accept common aural properties |
| **Inherited** | Yes |
| **Percentages** | N/A |
| **Media** | aural |

<!-- Source: https://www.w3.org/TR/xslfo20/#speak-header -->

CSS2 Definition. Specifies whether table headers are spoken before every cell, or only before a cell when that cell is associated with a different header than the previous cell.

### speak-numeral

| Field | Value |
|---|---|
| **Values** | `digits \| continuous \| inherit` |
| **Initial** | `continuous` |
| **Applies to** | all formatting objects that accept common aural properties |
| **Inherited** | Yes |
| **Percentages** | N/A |
| **Media** | aural |

<!-- Source: https://www.w3.org/TR/xslfo20/#speak-numeral -->

CSS2 Definition. Specifies how numerals are spoken.

### speak-punctuation

| Field | Value |
|---|---|
| **Values** | `code \| none \| inherit` |
| **Initial** | `none` |
| **Applies to** | all formatting objects that accept common aural properties |
| **Inherited** | Yes |
| **Percentages** | N/A |
| **Media** | aural |

<!-- Source: https://www.w3.org/TR/xslfo20/#speak-punctuation -->

CSS2 Definition. Specifies how punctuation is spoken.

### speech-rate

| Field | Value |
|---|---|
| **Values** | `<number> \| x-slow \| slow \| medium \| fast \| x-fast \| faster \| slower \| inherit` |
| **Initial** | `medium` |
| **Applies to** | all formatting objects that accept common aural properties |
| **Inherited** | Yes |
| **Percentages** | N/A |
| **Media** | aural |

<!-- Source: https://www.w3.org/TR/xslfo20/#speech-rate -->

CSS2 Definition. Specifies the speaking rate.

### stress

| Field | Value |
|---|---|
| **Values** | `<number> \| inherit` |
| **Initial** | `50` |
| **Applies to** | all formatting objects that accept common aural properties |
| **Inherited** | Yes |
| **Percentages** | N/A |
| **Media** | aural |

<!-- Source: https://www.w3.org/TR/xslfo20/#stress -->

CSS2 Definition. Specifies the height of "local peaks" in the intonation contour of a voice.

### voice-family

| Field | Value |
|---|---|
| **Values** | `[[<specific-voice> \| <generic-voice> ],]* [<specific-voice> \| <generic-voice> ] \| inherit` |
| **Initial** | depends on user agent |
| **Applies to** | all formatting objects that accept common aural properties |
| **Inherited** | Yes |
| **Percentages** | N/A |
| **Media** | aural |

<!-- Source: https://www.w3.org/TR/xslfo20/#voice-family -->

CSS2 Definition. Specifies a prioritized list of voice family names. Similar in concept to `font-family` for visual media, this property allows specification of named voices or generic voice families.

### volume

| Field | Value |
|---|---|
| **Values** | `<number> \| <percentage> \| silent \| x-soft \| soft \| medium \| loud \| x-loud \| inherit` |
| **Initial** | `medium` |
| **Applies to** | all formatting objects that accept common aural properties |
| **Inherited** | Yes |
| **Percentages** | refer to inherited value |
| **Media** | aural |

<!-- Source: https://www.w3.org/TR/xslfo20/#volume -->

CSS2 Definition. Specifies the median volume of the waveform.

## Code Samples

No code samples in spec for this property group.

## See Also

- [Properties: Accessibility](properties-accessibility.md) -- Related properties for alternate renderers
