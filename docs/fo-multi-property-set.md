# fo:multi-property-set

## Summary

The `fo:multi-property-set` auxiliary formatting object is used to specify an alternative set of formatting properties that can be used to provide an alternate presentation of the children flow objects of the `fo:wrapper` child of the parent of this `fo:multi-property-set`.

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_multi-property-set -->

## Areas

The `fo:multi-property-set` formatting object does not generate or return any areas. It simply holds a set of traits that may be accessed by expressions.

## Constraints

None.

## Content Model

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_multi-property-set -->
```xml
EMPTY
```

## Properties

| Property | Inherited | Conformance Level |
|---|---|---|
| `id` | N/A | Basic |
| `index-class` | N/A | Extended |
| `index-key` | N/A | Extended |
| `active-state` | no | Extended |

## Usage Notes

- The `active-state` property specifies which user agent state this property set applies to. Valid values include "link", "visited", "active", "hover", and "focus".
- In addition to the properties listed above, any property that the designer wants to vary by active state should be specified directly on the `fo:multi-property-set` element (e.g., `color="blue"`, `text-decoration="underline"`).
- The corresponding `fo:wrapper` sibling must use `merge-property-values()` as the value for each property that should take its value from the applicable `fo:multi-property-set`.
- Multiple `fo:multi-property-set` elements can be specified, one for each active state that needs distinct styling.

## Code Samples

No code samples in spec for this formatting object. See the "Styling an XLink Based on the Active State" example in the "Dynamic Effects: Link and Multi Formatting Objects" introduction section for a comprehensive demonstration.

## See Also

- `fo:multi-properties` -- parent formatting object that groups property sets with a wrapper
- `fo:wrapper` -- sibling formatting object that applies the merged property values
