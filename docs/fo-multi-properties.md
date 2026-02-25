# fo:multi-properties

## Summary

The `fo:multi-properties` is used to switch between two or more property sets that are associated with a given portion of content. It can be used to give different appearances to a given portion of content, for example when a link changes from the not-yet-visited state to the visited state.

The direct children of an `fo:multi-properties` formatting object is an ordered set of `fo:multi-property-set` formatting objects followed by a single `fo:wrapper` formatting object. The properties specified on the `fo:wrapper` that have been specified with a value of `merge-property-values()` will take a value that is a merger of the value on the `fo:multi-properties` and the specified values on the `fo:multi-property-set` formatting objects that apply.

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_multi-properties -->

## Areas

The `fo:multi-properties` formatting object does not generate any areas. The `fo:multi-properties` formatting object returns the sequence of areas created by concatenating the sequences of areas returned by each of the children of the `fo:multi-properties`.

## Constraints

The order of concatenation of the sequences of areas returned by the children of the `fo:multi-properties` is the same order as the children are ordered under the `fo:multi-properties`.

## Content Model

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_multi-properties -->
```xml
(multi-property-set+,wrapper)
```

The properties that should take a merged value shall be specified with a value of `merge-property-values()`. This function, when applied on an `fo:wrapper` that is a direct child of an `fo:multi-properties`, merges the applicable property definitions on the `fo:multi-property-set` siblings.

## Properties

| Property | Inherited | Conformance Level |
|---|---|---|
| Common Accessibility Properties | N/A | Basic |

## Usage Notes

- Designers should be careful in choosing which properties they change, because many property changes could cause reflowing of the text which may not be desired. Changing properties such as `color` or `text-decoration` should not require re-flowing the text.
- The `fo:multi-properties` formatting object is commonly used to style links with different appearances for different states (link, visited, active, hover, focus).
- Each `fo:multi-property-set` child specifies an `active-state` value and the property overrides for that state.
- The `fo:wrapper` child uses `merge-property-values()` as the value for properties that should be dynamically switched based on the active state.

## Code Samples

No code samples in spec for this formatting object. See the "Styling an XLink Based on the Active State" example in the "Dynamic Effects: Link and Multi Formatting Objects" introduction section for a comprehensive demonstration.

## See Also

- `fo:multi-property-set` -- child formatting object specifying property overrides for a particular active state
- `fo:wrapper` -- child formatting object that applies merged properties to its descendants
- `fo:basic-link` -- often wrapped by `fo:multi-properties` to provide state-dependent styling
