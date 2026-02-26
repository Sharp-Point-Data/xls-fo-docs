# axf:form-field-event

## Summary

Specifies an action corresponding to an event on a form field. Both the `name` property and the `axf:action-type` property must be specified. If `axf:action-type="javascript"` is specified, the JavaScript program is processed in the content of this formatting object.

## Properties

- **name** — Specifies the event type. Accepted values (not case-sensitive):
  - `MouseUp`
  - `MouseDown`
  - `MouseEnter`
  - `MouseExit`
  - `OnFocus`
  - `OnBlur`
- **axf:action-type** — Specifies the type of action to execute (e.g., `"javascript"`).

## Parent Objects

- `axf:form-field`

## Child Objects

When `axf:action-type="javascript"` is specified, the content of `axf:form-field-event` contains the JavaScript program to be executed.

## Code Samples

No code sample provided in the Antenna House reference for this formatting object.

**Constructed example** (not from the Antenna House reference):

```xml
<axf:form-field field-type="button" field-name="myButton">
  <axf:form-field-event name="MouseUp" axf:action-type="javascript">
    app.alert("Button was clicked!");
  </axf:form-field-event>
</axf:form-field>
```

This constructed example shows a form field button with a `MouseUp` event that triggers a JavaScript alert when the button is clicked.
