# fo:marker

## Summary

The `fo:marker` is used in conjunction with `fo:retrieve-marker` or `fo:retrieve-table-marker` to produce running headers or footers and dynamic table headers or footers. Typical examples include dictionary headers showing the first and last word defined on the page, headers showing the page's chapter and section titles, subtotals that give a subtotal of numbers in rows up to the last row on the current page, and table-continued captions.

The `fo:marker` has to be an initial child of its parent formatting object.

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_marker -->

## Areas

The `fo:marker` does not directly produce any area. Its children may be retrieved and formatted from within an `fo:static-content` or table header/footer, using an `fo:retrieve-marker` or an `fo:retrieve-table-marker` respectively, whose `retrieve-class-name` property value is the same as the `marker-class-name` property value of this `fo:marker`.

## Constraints

- An `fo:marker` is only permitted as the descendant of an `fo:flow`.
- Property values set on an `fo:marker` or its ancestors will not be inherited by the children of the `fo:marker` when they are retrieved by an `fo:retrieve-marker` or `fo:retrieve-table-marker`.
- It is an error if two or more `fo:marker`s that share the same parent have the same `marker-class-name` property value.
- An `fo:marker` may contain any formatting objects that are permitted as a replacement of any `fo:retrieve-marker` or `fo:retrieve-table-marker` that retrieves the `fo:marker`'s children.
- No `fo:marker` may have as a descendant any `fo:marker`, `fo:retrieve-marker`, or `fo:retrieve-table-marker`.

## Content Model

<!-- Source: https://www.w3.org/TR/xslfo20/#fo_marker -->
```xml
(#PCDATA|%inline;|%block;)*
```

## Properties

| Property | Inherited | Conformance Level |
|---|---|---|
| `marker-class-name` | no | Extended |

## Usage Notes

- The `marker-class-name` property assigns a class name to this marker. This name is used by `fo:retrieve-marker` and `fo:retrieve-table-marker` to select which marker's content to retrieve.
- Markers must be the initial children of their parent formatting object (they must come before any non-marker children).
- Each parent may have at most one marker per class name.
- The content of the marker is not formatted in place; it is only formatted when retrieved by an `fo:retrieve-marker` or `fo:retrieve-table-marker`.
- Since property values are not inherited from the marker's ancestors when retrieved, the marker's content should explicitly specify any needed properties.
- Markers cannot be nested: no `fo:marker` may contain another `fo:marker`, `fo:retrieve-marker`, or `fo:retrieve-table-marker`.

## Code Samples

The following example from the spec shows `fo:marker` used in a multi-column table layout with `fo:retrieve-table-marker` in the table footer, demonstrating how marker retrieval interacts with column breaks and page breaks.

**Complete FO example showing `fo:marker` in table body cells with `fo:retrieve-table-marker` in the footer, within a two-column `fo:region-body` layout:**

<!-- Source: xslspec.xml line 17464 -->
```xml
<fo:root xmlns:fo=http://www.w3.org/1999/XSL/Format>
  <fo:layout-master-set>
    <fo:simple-page-master master-name="page ">
      <fo:region-body region-name=" body"  column-count="2"/>
    </fo:simple-page-master>
  </fo:layout-master-set>
  <fo:page-sequence master-reference="page"
    <fo:flow flow-name=" body">
      <fo:table>
        <fo:table-column/>
        <fo:table-header>...</fo:table-header>
          <fo:table-footer>
            <fo:table-row>
              <fo:table-cell>
                <fo:block>
                  <fo:retrieve-table-marker
                    retrieve-class-name="marker-name"
                    retrieve-position-within-table="See table for values..."
                    retrieve-boundary-within-table="See table for values..."/>
                </fo:block>
              </fo:table-cell>
            </fo:table-row>
        </fo:table-footer>
        <fo:table-body>
          <fo:table-row>
            <fo:table-cell>
              <!-- cell 1 -->
              <fo:marker marker-class-name="marker-name">
                <!-- marker 1 -->
                ...
              </fo:marker>
              ...
            </fo:table-cell>
          </fo:table-row>
          <!-- and so on ... -->
          <fo:table-row>
            <fo:table-cell>
              <!-- cell 14 -->
              <fo:marker marker-class-name="marker-name">
                <!-- marker 14 -->
                ...
              </fo:marker>
              ...
            </fo:table-cell>
          </fo:table-row>
        </fo:table-body>
      </fo:table>
    </fo:flow>
  </fo:page-sequence>
</fo:root>
```

## See Also

- [fo:retrieve-marker](fo-retrieve-marker.md) — retrieves marker content for use in static-content (running headers/footers)
- [fo:retrieve-table-marker](fo-retrieve-table-marker.md) — retrieves marker content for use in table headers/footers
