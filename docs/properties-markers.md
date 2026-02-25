# Marker Properties

## Overview

<!-- Source: https://www.w3.org/TR/xslfo20/#properties-for-markers -->

The marker properties control the behavior of fo:marker and fo:retrieve-marker (and fo:retrieve-table-marker) formatting objects. Markers provide a mechanism for running headers/footers and similar constructs, where content from the body of a document is captured and then retrieved for placement in page headers, footers, or repeated table headers. The properties in this group define how markers are named, matched, and how the retrieval scope and position preference are determined.

## Properties

### marker-class-name

| Field | Value |
|---|---|
| **Values** | `<name>` |
| **Initial** | `an empty name` |
| **Applies to** | fo:marker |
| **Inherited** | No (a value is required) |
| **Percentages** | N/A |
| **Media** | paged |

<!-- Source: https://www.w3.org/TR/xslfo20/#marker-class-name -->

This property identifies the fo:marker as being in a group with others that have the same name, each of which becomes a candidate to be retrieved by an fo:retrieve-marker or fo:retrieve-table-marker that has a "retrieve-class-name" property of the same value.

Values have the following meanings:

- **\<name\>** -- Names used as identifiers must be unique among fo:markers that are (conceptually) attached to the same area. If the name is empty or if a name-conflict is encountered, an error shall be reported. A processor may then continue processing.

### retrieve-class-name

| Field | Value |
|---|---|
| **Values** | `<name>` |
| **Initial** | `an empty name` |
| **Applies to** | fo:retrieve-marker, fo:retrieve-table-marker |
| **Inherited** | No (a value is required) |
| **Percentages** | N/A |
| **Media** | paged |

<!-- Source: https://www.w3.org/TR/xslfo20/#retrieve-class-name -->

This property constrains that the fo:marker whose children are retrieved by the fo:retrieve-marker or fo:retrieve-table-marker must have a "marker-class-name" property value that is the same as the value of this property.

Values have the following meanings:

- **\<name\>** -- A name that matches the "marker-class-name" property value of an fo:marker.

### retrieve-position

| Field | Value |
|---|---|
| **Values** | `first-starting-within-page \| first-including-carryover \| last-starting-within-page \| last-ending-within-page` |
| **Initial** | `first-starting-within-page` |
| **Applies to** | fo:retrieve-marker |
| **Inherited** | No |
| **Percentages** | N/A |
| **Media** | paged |

<!-- Source: https://www.w3.org/TR/xslfo20/#retrieve-position -->

This property specifies the preference for which fo:marker's children shall be retrieved by an fo:retrieve-marker, based on the areas returned by the parent of the fo:marker relative to the areas returned by the parents of other identically named fo:markers.

The term "containing page" means the page that contains the first area generated or returned by the children of the retrieved fo:marker.

Values have the following meanings:

- **first-starting-within-page** -- Specifies a preference for retrieving the children of an fo:marker attached to an area that is within the containing page, whose "is-first" trait is set to "true", and that precedes in the area tree (using pre-order traversal order) any other similarly constrained area that has an attached fo:marker with the same value of the "marker-class-name" property.
- **first-including-carryover** -- Specifies a preference for retrieving the children of an fo:marker attached to an area that is within the containing page and that precedes in the area tree (using pre-order traversal order) any other similarly constrained area that has an attached fo:marker with the same value of the "marker-class-name" property.
- **last-starting-within-page** -- Specifies a preference for retrieving the children of an fo:marker attached to an area that is within the containing page, whose "is-first" trait is set to "true", and that follows in the area tree (using pre-order traversal order) any other similarly constrained area that has an attached fo:marker with the same value of the "marker-class-name" property.
- **last-ending-within-page** -- Specifies a preference for retrieving the children of an fo:marker attached to an area that is within the containing page whose "is-last" trait is set to "true" and that follows in the area tree (using pre-order traversal order) any other similarly constrained area that has an attached fo:marker with the same value of the "marker-class-name" property.

### retrieve-boundary

| Field | Value |
|---|---|
| **Values** | `page \| page-sequence \| document` |
| **Initial** | `page-sequence` |
| **Applies to** | fo:retrieve-marker |
| **Inherited** | No |
| **Percentages** | N/A |
| **Media** | paged |

<!-- Source: https://www.w3.org/TR/xslfo20/#retrieve-boundary -->

The term "containing page" means the page that contains the first area generated or returned by the children of the retrieved fo:marker.

Values have the following meanings:

- **page** -- Specifies that the children of any fo:markers whose parent generated or returned a normal area within the containing page or generated non-normal area within the containing page may be retrieved by this fo:retrieve-marker.
- **page-sequence** -- Specifies that only the children of fo:markers that are descendants of any fo:flow within the containing fo:page-sequence may be retrieved by this fo:retrieve-marker.
- **document** -- Specifies that the children of any fo:marker that is a descendant of any fo:flow within the document may be retrieved by this fo:retrieve-marker.

### retrieve-position-within-table

| Field | Value |
|---|---|
| **Values** | `first-starting \| first-including-carryover \| last-starting \| last-ending` |
| **Initial** | `first-starting` |
| **Applies to** | fo:retrieve-table-marker |
| **Inherited** | No |
| **Percentages** | N/A |
| **Media** | paged |

<!-- Source: https://www.w3.org/TR/xslfo20/#retrieve-position-within-table -->

This property specifies the preference for which fo:marker's children shall be retrieved by an fo:retrieve-table-marker, based on the areas returned by the parent of the fo:marker relative to the areas returned by the parents of other identically named fo:markers.

The terms defined in the fo:retrieve-table-marker section are used here.

Values have the following meanings:

- **first-starting** -- Specifies a preference for retrieving the children of an fo:marker attached to an area that is a descendant of the primary retrieve scope area, whose "is-first" trait is set to "true", and precedes in the area tree (using pre-order traversal order) any other similarly constrained area that has an attached fo:marker with the same value of the "marker-class-name" property.
- **first-including-carryover** -- Specifies a preference for retrieving the children of an fo:marker attached to an area that is a descendant of the primary retrieve scope area, and that precedes in the area tree (using pre-order traversal order) any other similarly constrained area that has an attached fo:marker with the same value of the "marker-class-name" property.
- **last-starting** -- Specifies a preference for retrieving the children of an fo:marker attached to an area that is a descendant of a retrieve scope area, whose "is-first" trait is set to "true", and that follows in the area tree (using pre-order traversal order) any other similarly constrained area that has an attached fo:marker with the same value of the "marker-class-name" property.
- **last-ending** -- Specifies a preference for retrieving the children of an fo:marker attached to an area that is a descendant of a retrieve scope area, and whose "is-last" trait is set to "true" and that follows in the area tree (using pre-order traversal order) any other similarly constrained area that has an attached fo:marker with the same value of the "marker-class-name" property.

### retrieve-boundary-within-table

| Field | Value |
|---|---|
| **Values** | `table \| table-fragment \| page` |
| **Initial** | `table` |
| **Applies to** | fo:retrieve-table-marker |
| **Inherited** | No |
| **Percentages** | N/A |
| **Media** | paged |

<!-- Source: https://www.w3.org/TR/xslfo20/#retrieve-boundary-within-table -->

The terms defined in the fo:retrieve-table-marker section are used here.

Values have the following meanings:

- **table** -- Specifies that the retrieve scope area set is limited to the primary retrieve scope area and the retrieve scope areas that precede the primary retrieve scope area.
- **table-fragment** -- Specifies that the retrieve scope area set is limited to the primary retrieve scope area.
- **page** -- Specifies that the retrieve scope area set is limited to the primary retrieve scope area and the retrieve scope areas that both precede this primary retrieve scope and are on the same page as the primary retrieve scope area.

## Code Samples

No code samples in spec for this property group.

## See Also

- [fo-marker](fo-marker.md) -- Formatting object that defines marker content
- [fo-retrieve-marker](fo-retrieve-marker.md) -- Formatting object that retrieves marker content in static-content
- [fo-retrieve-table-marker](fo-retrieve-table-marker.md) -- Formatting object that retrieves marker content in table headers/footers
