# axf:hyphenation-info

## Summary

Specifies additional hyphenation information. This element does not generate an area. The `language` property is required to indicate which language this element is associated with. It is not available to do hyphenation if the specified language is originally not hyphenated.

The `src` property can optionally specify the exception dictionary. It is an additional setting to the original dictionary and effective only in this FO. There is no language dependency constraint for the file name unlike the original dictionary. It is a relative base-uri for the relative path. It is not a relative path to the environment variable of the hyphenation dictionary.

`<exceptions>` in the specified dictionary is evaluated. When multiple words of the same spelling are registered, the information on the last registered word becomes effective.

## Properties

- **src** — Specifies the path to an additional exception dictionary file (optional).
- **language** — Indicates the language this hyphenation information is associated with (required).

## Parent Objects

- `fo:declarations`

## Child Objects

Elements in the `http://www.antennahouse.com/names/XSL/Hyphenations` namespace (`axh:*`). Currently only the following can be described:

- `axh:exceptions` (and its child element `axh:hyphen`)

## Code Samples

<!-- Source: XSL-FO-Reference-74-MID.pdf p.302 -->
```xml
<fo:block axf:soft-hyphen-treatment="preserve"
   font-family="Wingdings">abcxyz</fo:block>
```

<!-- Source: XSL-FO-Reference-74-MID.pdf p.303 -->
```xml
<fo:declarations>
   <axf:hyphenation-info language="eng" src="en-add.xml"
      xmlns:axs="http://www.antennahouse.com/names/XSL/Hyphenations">
      <axh:exceptions>
      abc-defg
      </axh:exceptions>
   </axf:hyphenation-info>
</fo:declarations>
```

In this example, an additional exception dictionary, `en-add.xml` is specified for English language, and then the exception hyphenation is specified for the word spelled "abcdefg".

**Caution:** In the example above, do not use the following setting (`<hyphen/>` is disregarded):

```xml
abc<hyphen/>defg
```

Instead, make sure to specify:

```xml
abc<axh:hyphen/>defg
```
