# Antenna House Extension Properties: Form Field (Acroform) Properties

<!-- Source: XSL-FO-Reference-74-MID.pdf pp.312–476 -->

Properties for PDF Acroform interactive form fields including field types (text, checkbox, radio, button, list box, combo box), field appearance, validation, actions, and submit/reset behavior. These properties are primarily used with the axf:form-field extension formatting object.

## axf:action-type

This extension is used to set the behavior of an external hyperlink or form action. The goto value causes an internal link, gotor causes a link into a PDF document. launch opens the target as a file. uri opens the target as a URI (on the web). The reset and submit values can only be used for the `<axf:form-field>` extension object. reset resets a form field, submit dispatches a form field as a form action. The javascript value triggers a JavaScript action. The default value auto triggers a system specific action.

If the link does not target a local file, the action type is always URI. If the action type is unspecified or set to the default auto, the target specified by a relative addressing is treated according to the setting of use-launch-for-relative-uri in the AH XSL Formatter PDF Output Settings either as action type Open the file (for value true) or as World Wide Web link (for value false). For an absolute address, the action type is always World Wide Web link.

| Attribute | Value |
|---|---|
| **Applies to** | `<fo:basic-link>`, `<axf:form-field>`, `<axf:form-field-event>` |
| **Values** | goto \| gotor \| launch \| uri \| reset \| submit \| javascript \| auto |
| **Initial** | auto |
| **Inherited** | no |

## axf:field-button-face

This property is used to specify the label of a form field marked as a push button.

| Attribute | Value |
|---|---|
| **Applies to** | `<axf:form-field>` |
| **Values** | &lt;string&gt; |
| **Initial** | empty string |
| **Inherited** | no |

## axf:field-button-face-down

This property is used to specify the labeling of a form field marked as a push button after activation.

| Attribute | Value |
|---|---|
| **Applies to** | `<axf:form-field>` |
| **Values** | &lt;string&gt; |
| **Initial** | empty string |
| **Inherited** | no |

## axf:field-button-face-rollover

This property is used to specify the labeling of a form field marked as a push button when the cursor is moved over the form field.

| Attribute | Value |
|---|---|
| **Applies to** | `<axf:form-field>` |
| **Values** | &lt;string&gt; |
| **Initial** | empty string |
| **Inherited** | no |

## axf:field-button-icon

This property specifies the icon of a form field marked as a push button.

| Attribute | Value |
|---|---|
| **Applies to** | `<axf:form-field>` |
| **Values** | &lt;uri-specification&gt; |
| **Initial** | empty string |
| **Inherited** | no |

## axf:field-button-icon-down

This property is used to specify the icon of a form field marked as a push button after activation.

| Attribute | Value |
|---|---|
| **Applies to** | `<axf:form-field>` |
| **Values** | &lt;uri-specification&gt; |
| **Initial** | empty string |
| **Inherited** | no |

## axf:field-button-icon-rollover

This property specifies the icon of a form field marked as a push button when the cursor is moved over the form field.

| Attribute | Value |
|---|---|
| **Applies to** | `<axf:form-field>` |
| **Values** | &lt;uri-specification&gt; |
| **Initial** | empty string |
| **Inherited** | no |

## axf:field-button-layout

This property specifies where the label of a form field marked as a push button should be placed in relation to the icon. With the default value caption only the label is displayed, not the icon. With the icon value, only the icon is displayed, not the label; with the caption-below-icon value, the label is displayed below the icon, with caption-above-icon above it, with icon-caption to the right of the icon, with caption-icon to the left of the icon, with caption-over-icon overlaying the icon.

| Attribute | Value |
|---|---|
| **Applies to** | `<axf:form-field>` |
| **Values** | caption \| icon \| caption-below-icon \| caption-above-icon \| icon-caption \| caption-icon \| caption-over-icon |
| **Initial** | caption |
| **Inherited** | no |

## axf:field-checked

This property is used to specify the initial state of form fields that have checkbox or radio for the axf:field-type property. If the default value is false, the initial state is unchecked. If in axf:field-flags="Checked" is set, the setting ="true" is ignored here.

| Attribute | Value |
|---|---|
| **Applies to** | `<axf:form-field>` |
| **Values** | false \| true |
| **Initial** | false |
| **Inherited** | no |

## axf:field-checked-style

This property sets the appearance of form fields that have the checkbox or radio value for the axf:field-type property. For the default value checkmark a checkmark is displayed, for the value circle a circle, for square a square, for cross a cross and for star an asterisk.

| Attribute | Value |
|---|---|
| **Applies to** | `<axf:form-field>` |
| **Values** | checkmark \| circle \| square \| cross \| star |
| **Initial** | checkmark |
| **Inherited** | no |

## axf:field-default-text

This property is used to specify a predefined text for a form field, which can then either be adopted by the form user or overwritten with his own text.

| Attribute | Value |
|---|---|
| **Applies to** | `<axf:form-field>` |
| **Values** | &lt;string&gt; |
| **Initial** | empty string |
| **Inherited** | no |

## axf:field-description

This property is used to add a description to a form field.

| Attribute | Value |
|---|---|
| **Applies to** | `<axf:form-field>` |
| **Values** | &lt;string&gt; |
| **Initial** | empty string |
| **Inherited** | no |

## axf:field-editable

With this property one opens in form fields, which have for the property axf:field-type the value combobox, the possibility to change the displayed value. With the default value false editing is excluded. If axf:field-flags="Editable" is set, the ="true" setting is ignored here.

| Attribute | Value |
|---|---|
| **Applies to** | `<axf:form-field>` |
| **Values** | false \| true |
| **Initial** | false |
| **Inherited** | no |

## axf:field-flags

With this property the form field is given a usage identifier: With Readonly the field becomes read-only, with Required it becomes mandatory, with Hidden the field is not displayed. In this case the size is kept, backgrounds and frames are shown. In version 6.6, the following identifiers have been added: Multiline, Password, Scroll, Checked, Multiple and Editable. Multiple values must be separated by spaces.

These codes have priority over the corresponding settlements with axf:field-readonly="true", axf:field-required="true", axf:field-multiline="true", axf:field-scroll="true", axf:field-password="true", axf:field-checked="true", axf:field-multiple="true", axf:field-editable="true".

| Attribute | Value |
|---|---|
| **Applies to** | `<axf:form-field>` |
| **Values** | &lt;string&gt; |
| **Initial** | empty string |
| **Inherited** | no |

## axf:field-font-size

This property assigns a desired font size to the content of the form field. The auto value uses the font size of the environment. The default value font-size sets the value set with the font-size property.

| Attribute | Value |
|---|---|
| **Applies to** | `<axf:form-field>` |
| **Values** | font-size \| auto \| &lt;length&gt; |
| **Initial** | font-size |
| **Inherited** | no |

## axf:field-format

This property assigns a desired formatting to the form field content according to the value specified in axf:field-format-category. The exact format specification for number, percentage, date and time can be found in the AHF Online Manual. It corresponds to the JavaScript syntax. As of version 6.6, the number of digits to be displayed after the decimal point or decimal comma can be set freely.

| Attribute | Value |
|---|---|
| **Applies to** | `<axf:form-field>` |
| **Values** | auto \| [ [ &lt;string&gt; \| &lt;number&gt;] [&lt;string&gt; \| &lt;number&gt; \| true \| false]* ] |
| **Initial** | auto |
| **Inherited** | no |

## axf:field-format-category

This property assigns a format type to the form field. The formatting itself is specified with axf:field-format. If a string is specified as a default value in the text field with axf:field-default-text, the format validity is checked. Non-compliant default values are ignored.

| Attribute | Value |
|---|---|
| **Applies to** | `<axf:form-field>` |
| **Values** | none \| number \| percentage \| date \| time |
| **Initial** | none |
| **Inherited** | no |

## axf:field-lock-document

This property is used to indicate whether the document should be closed with the signature. With the default value auto the PDF reader will ask whether the document should be closed. Effective as of PDF 1.7.

| Attribute | Value |
|---|---|
| **Applies to** | `<axf:form-field>` |
| **Values** | auto \| false \| true |
| **Initial** | auto |
| **Inherited** | no |

## axf:field-maxlen

This property is used to specify the maximum number of characters allowed for input in a form field marked as a text field. If the default value is 0, or the property is not specified, or a negative number is specified, then the number of characters allowed is not restricted. If the maximum number of characters set here is exceeded in the string set with axf:field-default-text, then this string will not be output.

| Attribute | Value |
|---|---|
| **Applies to** | `<axf:form-field>` |
| **Values** | &lt;number&gt; |
| **Initial** | 0 |
| **Inherited** | no |

## axf:field-multiline

This property sets whether a form field marked as a text field allows input in a single line or in multiple lines. The default value false allows only one line. If axf:field-flags="Multiline" is set, the setting ="true" is ignored here.

| Attribute | Value |
|---|---|
| **Applies to** | `<axf:form-field>` |
| **Values** | true \| false |
| **Initial** | false |
| **Inherited** | no |

## axf:field-multiple

This property sets whether only one or a number of options can be selected for form fields that have the listbox value for the axf:field-type property. With the default value false, the choice is limited to one option in the list. If axf:field-flags="Multiple" is set, the ="true" setting is ignored here.

| Attribute | Value |
|---|---|
| **Applies to** | `<axf:form-field>` |
| **Values** | false \| true |
| **Initial** | false |
| **Inherited** | no |

## axf:field-name

This property defines the name of a form field.

| Attribute | Value |
|---|---|
| **Applies to** | `<axf:form-field>` |
| **Values** | &lt;string&gt; |
| **Initial** | none, a name must be entered as a value. |
| **Inherited** | no |

## axf:field-name-suffix-page-number

This property is used to add a page number to the form field name. It is assumed that a axf:field-name is defined. If the value is an empty string, nothing is added. This property is used with a form inside the `<fo:static-content>` if a separate form is to be generated for each page.

| Attribute | Value |
|---|---|
| **Applies to** | `<axf:form-field>` |
| **Values** | &lt;string&gt; |
| **Initial** | empty string |
| **Inherited** | no |

## axf:field-password

With this property one marks by the value true a form field marked as text field as input field for a password. Each character entered is represented by a "*" character. If axf:field-flags="Password" is set, the ="true" setting is ignored here.

| Attribute | Value |
|---|---|
| **Applies to** | `<axf:form-field>` |
| **Values** | true \| false |
| **Initial** | false |
| **Inherited** | no |

## axf:field-readonly

The true value for this property marks the form field as "read only". If axf:field-flags="ReadOnly" is set, the ="true" setting is ignored here.

| Attribute | Value |
|---|---|
| **Applies to** | `<axf:form-field>` |
| **Values** | true \| false |
| **Initial** | false |
| **Inherited** | no |

## axf:field-required

The true value for this property is used to mark the form field as "mandatory to fill". If axf:field-flags="Required" is set, the ="true" setting is ignored here.

| Attribute | Value |
|---|---|
| **Applies to** | `<axf:form-field>` |
| **Values** | true \| false |
| **Initial** | false |
| **Inherited** | no |

## axf:field-scroll

This property sets whether a form field marked as a text field gets a scroll bar or not. The default value false makes the text field not scrollable. If axf:field-flags="Scroll" is set, the setting ="true" is ignored here.

| Attribute | Value |
|---|---|
| **Applies to** | `<axf:form-field>` |
| **Values** | true \| false |
| **Initial** | false |
| **Inherited** | no |

## axf:field-selected

Specifies the first selected item in the list box, combo box.

| Attribute | Value |
|---|---|
| **Applies to** | `<axf:form-field-option>` |
| **Values** | false \| true |
| **Initial** | false |
| **Inherited** | no |

## axf:field-submit-coordinates

Specifies whether to send out the coordinates of the mouse when submitting a form field. Values have the following meanings: false does not send out the coordinates; true sends out the coordinates.

| Attribute | Value |
|---|---|
| **Applies to** | `<axf:form>` |
| **Values** | false \| true |
| **Initial** | false |
| **Inherited** | no |

## axf:field-submit-method

Specifies the way to send the information when submitting a form field. Values have the following meanings: get sends out a form as GET request; post sends out a form as POST request.

| Attribute | Value |
|---|---|
| **Applies to** | `<axf:form>` |
| **Values** | get \| post |
| **Initial** | get |
| **Inherited** | no |

## axf:field-text-align

This property sets the horizontal alignment of the content in a text field.

| Attribute | Value |
|---|---|
| **Applies to** | `<axf:form-field>` |
| **Values** | left \| center \| right |
| **Initial** | left |
| **Inherited** | no |

## axf:field-top-index

This property sets the order of options for form fields that have listbox or combobox for the axf:field-type property. With the default value 1, the first option (`<axf:form-field-option>`) in the list of options is displayed in the form field. With a higher number, options positioned further down can also be moved into the display. The setting here is overridden by the setting of axf:field-selected="true".

| Attribute | Value |
|---|---|
| **Applies to** | `<axf:form-field>` |
| **Values** | &lt;number&gt; |
| **Initial** | 1 |
| **Inherited** | no |

## axf:field-type

This property is used to set the type of a form field. The possible values: text for a text field, button for a push button to start an action, checkbox for a box to select an option, radio for a button usually placed in a group of such buttons where only one of the buttons can be selected, listbox for a list of textual alternatives defined as list items with the `<axf:form-field-option>` child extension object, combobox for a list variant, and signature for a digital signature.

The area for the digital signature must be set with width and height in the width-height ratio of the signature to be generated. The content remains empty for the signature generated in the PDF. The formatting of the signature can be set in a restricted way (font selection and font color) by the block (`<fo:block>`) enclosing the form field. In the formatting process this area is merely reserved, the signature is not generated yet, this only in the PDF generation. In the PDF browser this area is displayed to complete the signature. Clicking on this area activates the signature. The PDF must finally be saved with the signature.

| Attribute | Value |
|---|---|
| **Applies to** | `<axf:form-field>` |
| **Values** | text \| button \| checkbox \| radio \| listbox \| combobox \| signature |
| **Initial** | none, a value must be selected. |
| **Inherited** | no |

## axf:field-value

Specifies the value used when submitting a form field, etc.

| Attribute | Value |
|---|---|
| **Applies to** | `<axf:form-field>`, `<axf:form-field-option>` |
| **Values** | &lt;string&gt; |
| **Initial** | empty string |
| **Inherited** | no |
