#!/usr/bin/env python3
"""
Phase 2: Section & Code Sample Extraction from xslspec.xml

Produces:
  - inventory/sections.json    — Complete section inventory with line ranges
  - inventory/samples.json     — Complete code sample inventory
  - inventory/file-mapping.json — Section-to-file mapping
  - inventory/summary.txt      — Human-readable summary & verification
"""

import re
import json
import os
import html

SPEC_FILE = "xslspec.xml"
OUTPUT_DIR = "inventory"
BASE_URL = "https://www.w3.org/TR/xslfo20/"

# ── Section-to-file mapping from Phase 2 plan ──────────────────────────

# Chapter-level overrides (div1)
CHAPTER_FILE_MAP = {
    "Introduction and Overview": "guide-introduction.md",
    "XSL Transformation": "guide-xslt-integration.md",
    "Introduction to Formatting": "guide-formatting-intro.md",
    "Area Model": "guide-area-model.md",
    "Property Refinement / Resolution": "guide-property-refinement.md",
    "Formatting Objects": None,  # Each FO gets its own file
    "Formatting Properties": None,  # Each group gets its own file
    "Conformance": "ref-conformance.md",
    "Formatting Object Summary": "ref-fo-summary.md",
}

# Section-level overrides by id
SECTION_FILE_MAP_BY_ID = {
    "xsl-namespace": "guide-xslt-integration.md",
    "fo-jc-intro": "guide-formatting-intro.md",
    "area_model": "guide-area-model.md",
    "area-intro": "guide-area-model.md",
    "area-rect": "guide-area-model.md",
    "area-common": "guide-area-model.md",
    "area-geo": "guide-area-model.md",
    "area-treeorder": "guide-area-model.md",
    "area-stackcon": "guide-area-model.md",
    "spacecond": "guide-spaces-conditionality.md",
    "area-space": "guide-spaces-conditionality.md",
    "bpd-slack": "guide-spaces-conditionality.md",
    "area-block": "guide-area-model.md",
    "area-stackblock": "guide-area-model.md",
    "verticalpositioning": "guide-area-model.md",
    "intrusadjust": "guide-area-model.md",
    "area-line": "guide-area-model.md",
    "area-inline": "guide-area-model.md",
    "area-stackinline": "guide-area-model.md",
    "area-glyph": "guide-area-model.md",
    "area-font": "guide-area-model.md",
    "area-order": "guide-area-model.md",
    "area-linebuild": "guide-area-model.md",
    "area-inlinebuild": "guide-area-model.md",
    "keepbreak": "guide-keeps-breaks.md",
    "rendmodel": "guide-rendering-model.md",
    "area-tree-sample": "guide-area-model.md",
    "copyfitting": "guide-copyfitting.md",
    "refinement": "guide-property-refinement.md",
    "inheritance": "guide-property-refinement.md",
    "shortexpan": "guide-property-refinement.md",
    "compcorr": "guide-property-refinement.md",
    "refine-border-padding": "guide-property-refinement.md",
    "refine-margin-space-indent": "guide-property-refinement.md",
    "overcons_geom": "guide-property-refinement.md",
    "datatype": "guide-datatypes.md",
    "numbering": "guide-numbering.md",
    "conform": "ref-conformance.md",
    "FO-summary": "ref-fo-summary.md",
    # FO chapter structural sections
    "fo-section": "guide-formatting-objects.md",
    "define-returned-by": "guide-formatting-objects.md",
    # Property groups
    "common-aural-properties": "properties-aural.md",
    "common-font-properties": "properties-font.md",
    "common-hyphenation-properties": "properties-hyphenation.md",
    "common-margin-properties-block": "properties-margin-block.md",
    "common-margin-properties-inline": "properties-margin-inline.md",
    "common-wrap-properties": "properties-wrap.md",
    "area-alignment": "properties-alignment.md",
    "ruby": "properties-ruby.md",
    "numbering.properties": "properties-numbering.md",
    "writing-mode-related": "properties-writing-mode.md",
    # Missing property groups
    "common-accessibility-properties": "properties-accessibility.md",
    "common-absolute-position-properties": "properties-absolute-position.md",
    "common-border-padding-and-background-properties": "properties-border-padding-background.md",
    "common-relative-position-properties": "properties-relative-position.md",
    "cssbox": "guide-property-refinement.md",
    "percrule": "guide-property-refinement.md",
    "cssdatat": "guide-property-refinement.md",
    # Properties chapter top-level
    "pr-section": "guide-property-refinement.md",
    # Reference/summary chapters
    "property-index": "ref-property-summary.md",
    "trmval": "ref-property-summary.md",
    "prtab1": "ref-property-summary.md",
    "prtab2": "ref-property-summary.md",
    "prapply": "ref-property-summary.md",
    # Individual property IDs for markers (unmapped parent)
    "marker-class-name": "properties-markers.md",
    "retrieve-boundary-within-table": "properties-markers.md",
    "retrieve-class-name": "properties-markers.md",
    "retrieve-boundary": "properties-markers.md",
    "retrieve-position": "properties-markers.md",
    "retrieve-position-within-table": "properties-markers.md",
    # Individual property IDs for absolute/relative position
    "absolute-position": "properties-absolute-position.md",
    "bottom": "properties-absolute-position.md",
    "left": "properties-absolute-position.md",
    "right": "properties-absolute-position.md",
    "top": "properties-absolute-position.md",
    "relative-position": "properties-relative-position.md",
    # Individual property IDs for accessibility
    "source-document": "properties-accessibility.md",
    "role": "properties-accessibility.md",
    # Individual property IDs for border/padding/background
    "background-attachment": "properties-border-padding-background.md",
    "background-color": "properties-border-padding-background.md",
    "background-image": "properties-border-padding-background.md",
    "background-position-horizontal": "properties-border-padding-background.md",
    "background-position-vertical": "properties-border-padding-background.md",
    "background-repeat": "properties-border-padding-background.md",
    "border-after-color": "properties-border-padding-background.md",
    "border-after-style": "properties-border-padding-background.md",
    "border-after-width": "properties-border-padding-background.md",
    "border-before-color": "properties-border-padding-background.md",
    "border-before-style": "properties-border-padding-background.md",
    "border-before-width": "properties-border-padding-background.md",
    "border-bottom-color": "properties-border-padding-background.md",
    "border-bottom-style": "properties-border-padding-background.md",
    "border-bottom-width": "properties-border-padding-background.md",
    "border-end-color": "properties-border-padding-background.md",
    "border-end-style": "properties-border-padding-background.md",
    "border-end-width": "properties-border-padding-background.md",
    "border-left-color": "properties-border-padding-background.md",
    "border-left-style": "properties-border-padding-background.md",
    "border-left-width": "properties-border-padding-background.md",
    "border-right-color": "properties-border-padding-background.md",
    "border-right-style": "properties-border-padding-background.md",
    "border-right-width": "properties-border-padding-background.md",
    "border-start-color": "properties-border-padding-background.md",
    "border-start-style": "properties-border-padding-background.md",
    "border-start-width": "properties-border-padding-background.md",
    "border-top-color": "properties-border-padding-background.md",
    "border-top-style": "properties-border-padding-background.md",
    "border-top-width": "properties-border-padding-background.md",
    "padding-after": "properties-border-padding-background.md",
    "padding-before": "properties-border-padding-background.md",
    "padding-bottom": "properties-border-padding-background.md",
    "padding-end": "properties-border-padding-background.md",
    "padding-left": "properties-border-padding-background.md",
    "padding-right": "properties-border-padding-background.md",
    "padding-start": "properties-border-padding-background.md",
    "padding-top": "properties-border-padding-background.md",
}

# Section-level overrides by title keywords
SECTION_FILE_MAP_BY_TITLE = {
    "Internationalization and Writing-Modes": "guide-writing-modes.md",
    "Linking": "guide-linking.md",
    "Unicode BIDI Processing": "guide-bidi.md",
    "Expressions": "guide-expressions.md",
    "Core Function Library": "guide-expressions.md",
    "Property Datatypes": "guide-datatypes.md",
    "Area Dimension": "properties-dimension.md",
    "Block and Line-related": "properties-block-line.md",
    "Character Properties": "properties-character.md",
    "Color-related": "properties-color.md",
    "Float-related": "properties-float.md",
    "Keeps and Breaks": "properties-keeps-breaks.md",
    "Layout-related": "properties-layout.md",
    "Leader and Rule": "properties-leader.md",
    "Dynamic Effects": "properties-dynamic-effects.md",
    "Indexing": "properties-indexing.md",
    "Marker Properties": "properties-markers.md",
    "Properties for Markers": "properties-markers.md",
    "Number to String": "properties-number-string.md",
    "Pagination and Layout": "properties-pagination.md",
    "Table Properties": "properties-table.md",
    "Miscellaneous Properties": "properties-misc.md",
    "Shorthand Properties": "properties-shorthand.md",
    # FO chapter structural/intro sections
    "Introduction to Formatting Objects": "guide-formatting-objects.md",
    "Formatting Object Content": "guide-formatting-objects.md",
    "Formatting Objects Summary": "guide-formatting-objects.md",
    "Block-level Formatting Objects": "guide-formatting-objects.md",
    "Inline-level Formatting Objects": "guide-formatting-objects.md",
    "Formatting Objects for Tables": "guide-formatting-objects.md",
    "Formatting Objects for Lists": "guide-formatting-objects.md",
    "Formatting Objects for Bookmarks": "guide-formatting-objects.md",
    "Out-of-Line Formatting Objects": "guide-formatting-objects.md",
    "Out-of-line Formatting Objects": "guide-formatting-objects.md",
    "Other Formatting Objects": "guide-formatting-objects.md",
    # Properties chapter structural
    "Description of Property Groups": "guide-property-refinement.md",
    "Normative References": "ref-references.md",
    "Other References": "ref-references.md",
}

# FO name -> filename
def fo_to_filename(fo_name):
    """Convert an FO element name like 'fo:block-container' to 'fo-block-container.md'."""
    name = fo_name.replace("fo:", "").strip()
    return f"fo-{name}.md"


def parse_spec():
    """Parse xslspec.xml line by line, extracting sections and code samples."""
    with open(SPEC_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()

    sections = []       # All div1/div2/div3 sections
    samples = []        # All <eg> code samples
    section_stack = []  # Track nesting

    # Regex patterns
    re_div_open = re.compile(r'<(div[123])(\s[^>]*)?>')
    re_div_close = re.compile(r'</(div[123])>')
    re_head = re.compile(r'<head>(.*?)</head>')
    re_id = re.compile(r'id="([^"]*)"')
    re_eg_single = re.compile(r'<eg[^>]*>(.*?)</eg>')
    re_eg_open = re.compile(r'<eg[^>]*>')
    re_eg_close = re.compile(r'</eg>')

    in_eg = False
    eg_start_line = 0
    eg_content_lines = []

    # Also track head content that may span lines (rare but possible)
    in_head = False
    head_content = ""
    head_section_idx = -1

    for line_num_0, line in enumerate(lines):
        line_num = line_num_0 + 1  # 1-based

        # ── Handle <eg> blocks ──
        if in_eg:
            if re_eg_close.search(line):
                # Capture up to closing tag
                close_match = re_eg_close.search(line)
                eg_content_lines.append(line[:close_match.start()])
                raw_content = "".join(eg_content_lines)
                content = unescape_xml(raw_content)

                # Find containing section
                containing_section = None
                containing_section_id = None
                for s in reversed(sections):
                    if s["start_line"] <= eg_start_line:
                        containing_section = s
                        containing_section_id = s.get("id")
                        break

                # Walk up to find nearest id for URL
                nearest_id = None
                for s in reversed(sections):
                    if s["start_line"] <= eg_start_line and s.get("id"):
                        nearest_id = s["id"]
                        break

                samples.append({
                    "index": len(samples) + 1,
                    "start_line": eg_start_line,
                    "end_line": line_num,
                    "content": content.strip(),
                    "section_title": containing_section["title"] if containing_section else "Unknown",
                    "section_id": containing_section_id,
                    "nearest_id": nearest_id,
                    "source_link": f"{BASE_URL}#{nearest_id}" if nearest_id else f"xslspec.xml line {eg_start_line}",
                })
                in_eg = False
                eg_content_lines = []
            else:
                eg_content_lines.append(line)
            continue

        # Check for single-line <eg>...</eg>
        single_eg = re_eg_single.search(line)
        if single_eg:
            raw_content = single_eg.group(1)
            content = unescape_xml(raw_content)

            containing_section = None
            containing_section_id = None
            nearest_id = None
            for s in reversed(sections):
                if s["start_line"] <= line_num:
                    if containing_section is None:
                        containing_section = s
                        containing_section_id = s.get("id")
                    if nearest_id is None and s.get("id"):
                        nearest_id = s["id"]
                    if containing_section and nearest_id:
                        break

            samples.append({
                "index": len(samples) + 1,
                "start_line": line_num,
                "end_line": line_num,
                "content": content.strip(),
                "section_title": containing_section["title"] if containing_section else "Unknown",
                "section_id": containing_section_id,
                "nearest_id": nearest_id,
                "source_link": f"{BASE_URL}#{nearest_id}" if nearest_id else f"xslspec.xml line {line_num}",
            })
            continue

        # Check for multi-line <eg> opening
        if re_eg_open.search(line) and not re_eg_close.search(line):
            in_eg = True
            eg_start_line = line_num
            # Content after the opening tag on same line
            open_match = re_eg_open.search(line)
            eg_content_lines = [line[open_match.end():]]
            continue

        # ── Handle div open/close ──
        div_open = re_div_open.search(line)
        if div_open:
            tag = div_open.group(1)
            attrs = div_open.group(2) or ""
            level = int(tag[-1])

            # Extract id
            id_match = re_id.search(attrs)
            section_id = id_match.group(1) if id_match else None

            # Extract head - might be on same line or next lines
            head_match = re_head.search(line)
            title = ""
            if head_match:
                title = clean_text(head_match.group(1))
            # Also check next few lines for <head> if not found
            # (we'll handle this in a second pass if needed)

            section = {
                "tag": tag,
                "level": level,
                "id": section_id,
                "title": title,
                "start_line": line_num,
                "end_line": None,  # filled on close
                "parent_index": None,
            }

            # Find parent
            for i in range(len(sections) - 1, -1, -1):
                if sections[i]["level"] < level and sections[i]["end_line"] is None:
                    section["parent_index"] = i
                    break

            sections.append(section)
            section_stack.append(len(sections) - 1)

        div_close = re_div_close.search(line)
        if div_close:
            tag = div_close.group(1)
            # Close the most recent open section of this level
            for i in range(len(section_stack) - 1, -1, -1):
                idx = section_stack[i]
                if sections[idx]["tag"] == tag and sections[idx]["end_line"] is None:
                    sections[idx]["end_line"] = line_num
                    section_stack.pop(i)
                    break

        # ── Pick up <head> on lines following div open ──
        if not div_open:
            head_match = re_head.search(line)
            if head_match and sections:
                # Assign to most recent section without a title
                for s in reversed(sections):
                    if not s["title"] and s["end_line"] is None:
                        s["title"] = clean_text(head_match.group(1))
                        break

    # Second pass: assign target files
    for s in sections:
        s["target_file"] = resolve_target_file(s, sections)

    # Assign target files to samples
    for sample in samples:
        sample["target_file"] = resolve_sample_target(sample, sections)

    return sections, samples


def unescape_xml(text):
    """Unescape XML entities."""
    text = text.replace("&lt;", "<")
    text = text.replace("&gt;", ">")
    text = text.replace("&amp;", "&")
    text = text.replace("&quot;", '"')
    text = text.replace("&apos;", "'")
    return text


def clean_text(text):
    """Remove XML tags from text, keeping content."""
    text = re.sub(r'<[^>]+>', '', text)
    text = unescape_xml(text)
    return text.strip()


def resolve_target_file(section, all_sections):
    """Determine the target doc file for a section."""
    # Check by id first
    if section["id"] and section["id"] in SECTION_FILE_MAP_BY_ID:
        return SECTION_FILE_MAP_BY_ID[section["id"]]

    # Check by title keywords
    for keyword, filename in SECTION_FILE_MAP_BY_TITLE.items():
        if keyword.lower() in section["title"].lower():
            return filename

    # For FO sections (div2 under Formatting Objects chapter), detect fo: names
    if section["level"] >= 2:
        # Check if this is an FO definition
        fo_match = re.search(r'fo:[\w-]+', section["title"])
        if fo_match:
            return fo_to_filename(fo_match.group(0))

    # For individual property definitions inside property groups
    # Check if title looks like a property name (lowercase with hyphens)
    if section["level"] == 3:
        parent = get_parent(section, all_sections)
        if parent and parent.get("target_file") and parent["target_file"].startswith("properties-"):
            return parent["target_file"]

    # Fall back to chapter-level mapping
    chapter = get_chapter(section, all_sections)
    if chapter:
        title = chapter["title"]
        if title in CHAPTER_FILE_MAP:
            return CHAPTER_FILE_MAP[title]

    # Inherit from parent
    parent = get_parent(section, all_sections)
    if parent and parent.get("target_file"):
        return parent["target_file"]

    return None


def resolve_sample_target(sample, sections):
    """Determine target file for a code sample."""
    # Find the containing section and use its target file
    for s in reversed(sections):
        if s["start_line"] <= sample["start_line"] and (s["end_line"] is None or s["end_line"] >= sample["end_line"]):
            if s.get("target_file"):
                return s["target_file"]
    return None


def get_parent(section, all_sections):
    """Get parent section."""
    if section["parent_index"] is not None:
        return all_sections[section["parent_index"]]
    return None


def get_chapter(section, all_sections):
    """Get the div1 ancestor of a section."""
    current = section
    while current:
        if current["level"] == 1:
            return current
        current = get_parent(current, all_sections)
    return None


def generate_summary(sections, samples):
    """Generate human-readable summary."""
    lines = []
    lines.append("=" * 70)
    lines.append("PHASE 2 EXTRACTION SUMMARY")
    lines.append("=" * 70)
    lines.append("")

    # Section counts by level
    div1 = [s for s in sections if s["level"] == 1]
    div2 = [s for s in sections if s["level"] == 2]
    div3 = [s for s in sections if s["level"] == 3]
    lines.append(f"Sections found:  {len(sections)} total")
    lines.append(f"  div1 (chapters): {len(div1)}")
    lines.append(f"  div2 (sections): {len(div2)}")
    lines.append(f"  div3 (subsections): {len(div3)}")
    lines.append("")

    # Code samples
    lines.append(f"Code samples (<eg> tags): {len(samples)}")
    lines.append(f"  Expected: 221")
    lines.append(f"  Match: {'YES' if len(samples) == 221 else 'NO — INVESTIGATE'}")
    lines.append("")

    # Samples per chapter
    lines.append("Samples by chapter:")
    for ch in div1:
        ch_samples = [s for s in samples
                      if s["start_line"] >= ch["start_line"]
                      and (ch["end_line"] is None or s["start_line"] <= ch["end_line"])]
        lines.append(f"  {ch['title']}: {len(ch_samples)}")
    lines.append("")

    # Chapters overview
    lines.append("─" * 70)
    lines.append("CHAPTER OVERVIEW")
    lines.append("─" * 70)
    for ch in div1:
        lines.append(f"\n{ch['title']}")
        lines.append(f"  Lines: {ch['start_line']}–{ch['end_line'] or 'EOF'}")
        lines.append(f"  ID: {ch['id'] or '(none)'}")
        lines.append(f"  Target: {ch.get('target_file', 'N/A')}")
        # List div2 children
        children = [s for s in div2
                    if s["parent_index"] is not None
                    and sections[s["parent_index"]] == ch]
        if children:
            lines.append(f"  Sections ({len(children)}):")
            for child in children:
                id_str = f" [{child['id']}]" if child['id'] else ""
                target_str = f" -> {child['target_file']}" if child.get('target_file') else ""
                lines.append(f"    - {child['title']}{id_str}{target_str}")
    lines.append("")

    # Target file distribution
    lines.append("─" * 70)
    lines.append("TARGET FILE DISTRIBUTION")
    lines.append("─" * 70)
    file_counts = {}
    for s in sections:
        f = s.get("target_file", "(unmapped)")
        file_counts[f] = file_counts.get(f, 0) + 1

    sample_file_counts = {}
    for s in samples:
        f = s.get("target_file", "(unmapped)")
        sample_file_counts[f] = sample_file_counts.get(f, 0) + 1

    all_files = sorted(set(list(file_counts.keys()) + list(sample_file_counts.keys())), key=lambda x: x or "")
    for f in all_files:
        sec_count = file_counts.get(f, 0)
        samp_count = sample_file_counts.get(f, 0)
        lines.append(f"  {f or '(unmapped)'}: {sec_count} sections, {samp_count} samples")
    lines.append("")

    # Unmapped sections
    unmapped = [s for s in sections if not s.get("target_file")]
    if unmapped:
        lines.append("─" * 70)
        lines.append(f"UNMAPPED SECTIONS ({len(unmapped)})")
        lines.append("─" * 70)
        for s in unmapped:
            lines.append(f"  Line {s['start_line']}: {s['tag']} — {s['title']} [id={s.get('id', 'none')}]")
    lines.append("")

    # Unmapped samples
    unmapped_samples = [s for s in samples if not s.get("target_file")]
    if unmapped_samples:
        lines.append(f"UNMAPPED SAMPLES ({len(unmapped_samples)}):")
        for s in unmapped_samples:
            lines.append(f"  Sample #{s['index']} line {s['start_line']}: in section '{s['section_title']}'")
    lines.append("")

    # Sections with no id (for link construction)
    no_id = [s for s in sections if not s.get("id") and s["level"] <= 2]
    if no_id:
        lines.append(f"SECTIONS WITHOUT ID (div1/div2 only): {len(no_id)}")
        for s in no_id:
            lines.append(f"  Line {s['start_line']}: {s['tag']} — {s['title']}")

    return "\n".join(lines)


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    print("Parsing xslspec.xml...")
    sections, samples = parse_spec()

    # Write sections inventory
    sections_out = []
    for s in sections:
        sections_out.append({
            "tag": s["tag"],
            "level": s["level"],
            "id": s["id"],
            "title": s["title"],
            "start_line": s["start_line"],
            "end_line": s["end_line"],
            "target_file": s.get("target_file"),
        })

    with open(os.path.join(OUTPUT_DIR, "sections.json"), "w", encoding="utf-8") as f:
        json.dump(sections_out, f, indent=2, ensure_ascii=False)
    print(f"  Wrote {len(sections_out)} sections to inventory/sections.json")

    # Write samples inventory
    samples_out = []
    for s in samples:
        samples_out.append({
            "index": s["index"],
            "start_line": s["start_line"],
            "end_line": s["end_line"],
            "section_title": s["section_title"],
            "section_id": s["section_id"],
            "nearest_id": s["nearest_id"],
            "source_link": s["source_link"],
            "target_file": s.get("target_file"),
            "content_preview": s["content"][:200] + ("..." if len(s["content"]) > 200 else ""),
            "content_length": len(s["content"]),
        })

    with open(os.path.join(OUTPUT_DIR, "samples.json"), "w", encoding="utf-8") as f:
        json.dump(samples_out, f, indent=2, ensure_ascii=False)
    print(f"  Wrote {len(samples_out)} samples to inventory/samples.json")

    # Write full sample content separately (large file)
    samples_full = []
    for s in samples:
        samples_full.append({
            "index": s["index"],
            "start_line": s["start_line"],
            "end_line": s["end_line"],
            "source_link": s["source_link"],
            "target_file": s.get("target_file"),
            "content": s["content"],
        })

    with open(os.path.join(OUTPUT_DIR, "samples-full.json"), "w", encoding="utf-8") as f:
        json.dump(samples_full, f, indent=2, ensure_ascii=False)
    print(f"  Wrote full sample content to inventory/samples-full.json")

    # Write file mapping
    file_map = {}
    for s in sections:
        target = s.get("target_file")
        if target:
            if target not in file_map:
                file_map[target] = {"sections": [], "sample_count": 0}
            file_map[target]["sections"].append({
                "title": s["title"],
                "id": s["id"],
                "level": s["level"],
                "start_line": s["start_line"],
            })

    for s in samples:
        target = s.get("target_file")
        if target and target in file_map:
            file_map[target]["sample_count"] += 1

    with open(os.path.join(OUTPUT_DIR, "file-mapping.json"), "w", encoding="utf-8") as f:
        json.dump(file_map, f, indent=2, ensure_ascii=False)
    print(f"  Wrote {len(file_map)} file mappings to inventory/file-mapping.json")

    # Write summary
    summary = generate_summary(sections, samples)
    with open(os.path.join(OUTPUT_DIR, "summary.txt"), "w", encoding="utf-8") as f:
        f.write(summary)
    # Print summary (handle Windows encoding)
    try:
        print(f"\n{summary}")
    except UnicodeEncodeError:
        print(summary.encode("ascii", errors="replace").decode("ascii"))


if __name__ == "__main__":
    main()
