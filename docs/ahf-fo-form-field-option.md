# axf:form-field-option

## Summary

Specifies the component elements of a list box or combo box form field. Each `axf:form-field-option` defines one selectable item within the list.

## Properties

- **axf:field-selected** — Indicates whether this option is initially selected.

## Parent Objects

- `axf:form-field`

## Child Objects

None. The text content of the element defines the option label.

## Code Samples

No code sample provided in the Antenna House reference for this formatting object.

**Constructed example** (not from the Antenna House reference):

```xml
<axf:form-field field-type="listbox" field-name="colorChoice">
  <axf:form-field-option axf:field-selected="true">Red</axf:form-field-option>
  <axf:form-field-option>Green</axf:form-field-option>
  <axf:form-field-option>Blue</axf:form-field-option>
</axf:form-field>
```

This constructed example shows a list box form field with three options, where "Red" is initially selected.
