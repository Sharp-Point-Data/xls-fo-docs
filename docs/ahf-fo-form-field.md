# axf:form-field

## Summary

The `axf:form-field` extension object generates an inline Acroform form field in the PDF output. The form field is inactive if `axf:form-field` does not stand inside `axf:form` and the `axf:action-type` property has the value `submit` or `reset`. All other properties also work outside `axf:form`.

**Note:** Inside an `axf:` extension object, the `axf:` extension properties omit the `axf:` namespace label.

<!-- Source: XSL-FO-Reference-74-MID.pdf p.299-300 -->

## Properties

| Property | Description |
|---|---|
| `axf:action-type` | The action type of the form field (e.g., submit, reset) |
| `axf:field-button-face` | The button face text |
| `axf:field-button-face-down` | The button face text when pressed down |
| `axf:field-button-face-rollover` | The button face text on rollover |
| `axf:field-button-icon` | The icon for the button |
| `axf:field-button-icon-down` | The icon for the button when pressed down |
| `axf:field-button-icon-rollover` | The icon for the button on rollover |
| `axf:field-button-layout` | The layout of button icon and text |
| `axf:field-checked` | Whether a checkbox or radio button is initially checked |
| `axf:field-checked-style` | The visual style for checked state |
| `axf:field-default-text` | The default text for a text field |
| `axf:field-description` | The tooltip description of the field |
| `axf:field-editable` | Whether a combo box is editable |
| `axf:field-flags` | Bit field flags for the form field |
| `axf:field-font-size` | The font size for text within the field |
| `axf:field-format` | The format string for the field value |
| `axf:field-format-category` | The format category for the field value |
| `axf:field-lock-document` | Whether editing the field locks the document |
| `axf:field-maxlen` | The maximum number of characters for a text field |
| `axf:field-multiline` | Whether the text field allows multiple lines |
| `axf:field-multiple` | Whether multiple selections are allowed in a list |
| `axf:field-name` | The name of the form field |
| `axf:field-name-suffix-page-number` | Whether to suffix the field name with the page number |
| `axf:field-password` | Whether the text field is a password field |
| `axf:field-readonly` | Whether the field is read-only |
| `axf:field-required` | Whether the field is required |
| `axf:field-scroll` | Whether the text field allows scrolling |
| `axf:field-text-align` | The text alignment within the field |
| `axf:field-top-index` | The index of the first visible item in a list |
| `axf:field-type` | The type of form field (e.g., text, button, checkbox, radio, listbox, combobox) |
| `width` | The width of the form field |
| `height` | The height of the form field |

## Parent Objects

- `fo:block`
- `axf:form`

## Child Objects

The object remains empty or contains any number of `axf:form-field-option` or/and `axf:form-field-event`.

## Code Samples

No code sample provided in the Antenna House reference for this formatting object.

The following is a constructed example (not from the reference):

<!-- Constructed example — not from reference material -->
```xml
<fo:block>
  <axf:form external-destination="https://example.com/survey"
            field-submit-method="post">
    <fo:block>
      Full Name:
      <axf:form-field field-type="text"
                      field-name="fullname"
                      field-description="Enter your full name"
                      field-required="true"
                      field-maxlen="100"
                      width="200pt"
                      height="14pt"/>
    </fo:block>
    <fo:block>
      Agree to terms:
      <axf:form-field field-type="checkbox"
                      field-name="agree"
                      field-checked="false"
                      field-checked-style="check"
                      width="10pt"
                      height="10pt"/>
    </fo:block>
    <fo:block>
      Country:
      <axf:form-field field-type="combobox"
                      field-name="country"
                      field-editable="false"
                      width="150pt"
                      height="14pt">
        <axf:form-field-option value="us" label="United States"/>
        <axf:form-field-option value="uk" label="United Kingdom"/>
        <axf:form-field-option value="de" label="Germany"/>
      </axf:form-field>
    </fo:block>
    <fo:block>
      <axf:form-field field-type="button"
                      action-type="submit"
                      field-button-face="Submit"
                      width="60pt"
                      height="20pt"/>
      <axf:form-field field-type="button"
                      action-type="reset"
                      field-button-face="Reset"
                      width="60pt"
                      height="20pt"/>
    </fo:block>
  </axf:form>
</fo:block>
```

## See Also

- `axf:form` -- container object for Acroform form actions
- `axf:form-field-option` -- child object for list/combo box options
- `axf:form-field-event` -- child object for form field events
