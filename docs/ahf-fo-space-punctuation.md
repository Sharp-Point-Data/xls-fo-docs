# axf:space-after-punctuation, axf:space-before-punctuation, axf:space-between-digit-and-punctuation, axf:space-between-punctuation-and-digit

## Summary

These four extension formatting objects handle European typography spacing requirements:

- **`axf:space-after-punctuation`** -- Specifies the space inserted after a punctuation character.
- **`axf:space-before-punctuation`** -- Specifies the space inserted before a punctuation character.
- **`axf:space-between-digit-and-punctuation`** -- Specifies the space inserted between a digit (numeral) and a punctuation character.
- **`axf:space-between-punctuation-and-digit`** -- Specifies the space inserted between a punctuation character and a digit (numeral).

These specifications can alternatively be made in the external file with the option settings.

## Properties

The following properties apply to all four formatting objects:

| Property | Description |
|----------|-------------|
| `language` | The language to which this spacing rule applies (e.g., `"fr"` for French) |
| `space` | The amount of space to insert (AHF-specific values such as `"thin"`, `"1 div 3"`, `"1 div 4"`) |
| `code` | The punctuation character or character sequence to which this rule applies (AHF-specific) |

## Parent Objects

- `fo:declarations`

## Child Objects

None. These are empty elements.

## Code Samples

<!-- Source: XSL-FO-Reference-74-MID.pdf p.306 -->
```xml
<fo:declarations>
<axf:space-before-punctuation code="?" space="1 div 3" language="fr"/>
<axf:space-before-punctuation code="!" space="1 div 3" language="fr"/>
<axf:space-before-punctuation code=";" space="1 div 3" language="fr"/>
<axf:space-before-punctuation code=":" space="1 div 4" language="fr"/>
<axf:space-before-punctuation code="»" space="1 div 4" language="fr"/>
<axf:space-after-punctuation code="«" space="1 div 4" language="fr"/>
<axf:space-between-punctuation-and-digit code="+" space="thin" language="fr"/>
<axf:space-between-punctuation-and-digit code="−" space="thin" language="fr"/>
<axf:space-between-punctuation-and-digit code="±" space="thin" language="fr"/>
<axf:space-between-digit-and-punctuation code="%" space="thin" language="fr"/>
<axf:space-between-digit-and-punctuation code="°C" space="thin" language="fr"/>
<axf:space-between-digit-and-punctuation code="°F" space="thin" language="fr"/>
</fo:declarations>
```

This example shows French-language text spacing rules that follow standard French typographic conventions: inserting fractional spaces before question marks, exclamation marks, semicolons, colons, and closing guillemets; space after opening guillemets; and thin spaces between punctuation/digits for signs and units.
