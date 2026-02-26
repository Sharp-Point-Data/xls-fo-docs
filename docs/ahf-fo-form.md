# axf:form

## Summary

The `axf:form` extension object serves as a container object for a form action as an Acroform in the PDF output.

**Note:** Inside an `axf:` extension object, the `axf:` extension properties omit the namespace label `axf:`.

<!-- Source: XSL-FO-Reference-74-MID.pdf p.299 -->

## Properties

| Property | Description |
|---|---|
| `external-destination` | The URI for form submission |
| `axf:field-submit-method` | The HTTP method for form submission |
| `axf:field-submit-coordinates` | Whether to include click coordinates with form submission |

## Parent Objects

- `fo:block`

## Child Objects

- `fo:block`

## Code Samples

No code sample provided in the Antenna House reference for this formatting object.

The following is a constructed example (not from the reference):

<!-- Constructed example — not from reference material -->
```xml
<fo:block>
  <axf:form external-destination="https://example.com/submit"
            field-submit-method="post">
    <fo:block>
      Name: <axf:form-field field-type="text"
                            field-name="username"
                            width="150pt"
                            height="14pt"/>
    </fo:block>
    <fo:block>
      <axf:form-field field-type="button"
                      field-button-face="Submit"
                      action-type="submit"
                      width="60pt"
                      height="20pt"/>
    </fo:block>
  </axf:form>
</fo:block>
```
