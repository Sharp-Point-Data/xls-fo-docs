# axf:ruby

## Summary

Ruby is a typographic support for pronouncing complex characters in the CJK (Chinese, Japanese, Korean) languages. Antenna House provides the typographic implementation for different Ruby types. The use of the Ruby extension is comprehensively documented with examples in the AHF Online Manual (Ruby Extension, file: `ahf:ruby.html`).

An `axf:ruby` element contains one or more pairs of `axf:ruby-base` (the base characters) followed by `axf:ruby-text` (the annotation characters).

## Properties

- **axf:ruby-align** — Alignment of ruby text relative to the base text.
- **axf:ruby-position** — Position of ruby text (e.g., above or below the base text).
- **axf:ruby-offset** — Offset distance of ruby text from the base text.
- **axf:ruby-overhang** — Controls whether ruby text can overhang adjacent base characters.
- **axf:ruby-limit-overhang** — Limits the extent of ruby overhang.
- **axf:ruby-limit-space** — Limits the space adjustment for ruby text.
- **axf:ruby-small-kana** — Controls the use of small kana in ruby text.
- **axf:ruby-font-family** — Font family for ruby text.
- **axf:ruby-font-size** — Font size for ruby text.
- **axf:ruby-minimum-font-size** — Minimum font size for ruby text.
- **axf:ruby-font-style** — Font style for ruby text (e.g., italic).
- **axf:ruby-font-weight** — Font weight for ruby text (e.g., bold).
- **axf:ruby-font-stretch** — Font stretch for ruby text.
- **axf:ruby-condense** — Controls condensing of ruby text.
- **axf:ruby-color** — Color of ruby text.

## Parent Objects

- `fo:basic-link`
- `fo:bidi-override`
- `fo:block`
- `fo:inline`

## Child Objects

- `axf:ruby-base` followed by `axf:ruby-text` (these pairs may occur repeatedly)

## Code Samples

No code sample provided in the Antenna House reference for this formatting object.

**Constructed example** (not from the Antenna House reference):

```xml
<fo:block font-size="14pt"
          xmlns:axf="http://www.antennahouse.com/names/XSL/Extensions">
  <axf:ruby axf:ruby-position="before"
            axf:ruby-align="center"
            axf:ruby-font-size="7pt">
    <axf:ruby-base>&#x6771;&#x4EAC;</axf:ruby-base>
    <axf:ruby-text>&#x3068;&#x3046;&#x304D;&#x3087;&#x3046;</axf:ruby-text>
  </axf:ruby>
</fo:block>
```

This constructed example annotates the kanji characters for "Tokyo" (&#x6771;&#x4EAC;) with their hiragana reading (&#x3068;&#x3046;&#x304D;&#x3087;&#x3046;). The ruby text is positioned before (above in horizontal writing mode) the base text, centered, at half the base font size.
