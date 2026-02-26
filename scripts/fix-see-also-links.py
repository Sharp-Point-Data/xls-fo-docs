#!/usr/bin/env python3
"""Fix See Also sections in docs/fo-*.md files to add internal project doc links."""

import os
import sys
import re
import glob
import difflib

DOCS_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "docs")


def build_doc_index():
    """Build a set of all available doc basenames (without .md)."""
    docs = set()
    for f in glob.glob(os.path.join(DOCS_DIR, "*.md")):
        docs.add(os.path.basename(f)[:-3])  # strip .md
    return docs


# Map fo:element-name -> expected doc filename (without .md)
def fo_to_doc(fo_name):
    """Convert fo:block-container to fo-block-container."""
    return fo_name.replace("fo:", "fo-", 1)


# Map property name -> possible doc filenames to search
# Properties are grouped in files like properties-font.md, properties-table.md, etc.
# We can't do a 1:1 mapping without reading each file, so we'll skip linking individual properties.


def make_link(text, doc_name):
    """Create a relative markdown link to a doc file."""
    return f"[{text}]({doc_name}.md)"


def transform_see_also_line(line, doc_index):
    """Transform a single See Also bullet line to use internal doc links."""
    if not line.startswith("- "):
        return line

    content = line[2:]

    # Strip backticks for uniform processing
    clean = content.replace("`", "")

    # Detect and split on separator
    desc = None
    ref_part = clean

    for sep in [" \u2014 ", " \u2013 ", " -- "]:
        if sep in clean:
            idx = clean.index(sep)
            ref_part = clean[:idx].strip()
            desc = clean[idx + len(sep):].strip()
            break

    # Handle comma-separated FO list
    if ", fo:" in ref_part and ref_part.startswith("fo:"):
        fo_names = [n.strip() for n in ref_part.split(",")]
        links = []
        for name in fo_names:
            doc_name = fo_to_doc(name)
            if doc_name in doc_index:
                links.append(make_link(name, doc_name))
            else:
                links.append(name)
        result = "- " + ", ".join(links)
        if desc:
            result += f" \u2014 {desc}"
        return result

    # 1. FO element: starts with fo:
    fo_match = re.match(r'^(fo:[a-z][-a-z0-9]*)(.*)$', ref_part)
    if fo_match:
        fo_name = fo_match.group(1)
        remainder = fo_match.group(2).strip()
        doc_name = fo_to_doc(fo_name)
        if doc_name in doc_index:
            result = f"- {make_link(fo_name, doc_name)}"
        else:
            result = f"- {fo_name}"
        if desc:
            result += f" \u2014 {desc}"
        elif remainder:
            result += f" {remainder}"
        return result

    # 2. Common property group: starts with "Common"
    # These map to properties-*.md files but the mapping is complex.
    # Leave as-is (no link).

    # 3. Function references: leave as-is
    # 4. Property references: leave as-is (grouped in properties-*.md, no 1:1 mapping)
    # 5. Copyfitting model, etc.: check for guide docs
    if ref_part.startswith("Copyfitting model"):
        if "guide-copyfitting" in doc_index:
            remainder = ref_part[len("Copyfitting model"):].strip()
            result = f"- {make_link('Copyfitting model', 'guide-copyfitting')}"
            if remainder:
                result += f" {remainder}"
            if desc:
                result += f" \u2014 {desc}"
            return result

    # For everything else, just normalize separators and backticks
    result = f"- {ref_part}"
    if desc:
        result += f" \u2014 {desc}"
    return result


def process_file(filepath, doc_index, dry_run=False):
    """Process a single file, fixing its See Also section."""
    with open(filepath, "r", encoding="utf-8") as f:
        original_lines = f.readlines()

    lines = [l.rstrip("\n") for l in original_lines]

    # Find See Also section
    see_also_start = None
    for i, line in enumerate(lines):
        if line.strip() == "## See Also":
            see_also_start = i
            break

    if see_also_start is None:
        return False, []

    # Transform lines after ## See Also
    new_lines = lines[:see_also_start + 1]

    changed = False
    for i in range(see_also_start + 1, len(lines)):
        line = lines[i]
        if line.startswith("## "):
            new_lines.extend(lines[i:])
            break
        if line.startswith("- "):
            new_line = transform_see_also_line(line, doc_index)
            if new_line != line:
                changed = True
            new_lines.append(new_line)
        else:
            new_lines.append(line)

    if not changed:
        return False, []

    diff = list(difflib.unified_diff(
        [l + "\n" for l in lines],
        [l + "\n" for l in new_lines],
        fromfile=os.path.basename(filepath),
        tofile=os.path.basename(filepath),
        lineterm="\n"
    ))

    if not dry_run:
        with open(filepath, "w", encoding="utf-8") as f:
            for line in new_lines:
                f.write(line + "\n")

    return changed, diff


def main():
    dry_run = "--dry-run" in sys.argv or "--diff" in sys.argv

    doc_index = build_doc_index()
    files = sorted(glob.glob(os.path.join(DOCS_DIR, "fo-*.md")))

    if not files:
        print(f"No fo-*.md files found in {DOCS_DIR}")
        sys.exit(1)

    print(f"{'DRY RUN: ' if dry_run else ''}Processing {len(files)} files (doc index: {len(doc_index)} docs)...")

    total_changed = 0
    total_linked = 0
    total_unlinked = 0

    for filepath in files:
        changed, diff = process_file(filepath, doc_index, dry_run=dry_run)
        if changed:
            total_changed += 1
            if diff:
                basename = os.path.basename(filepath)
                print(f"\n--- {basename} ---")
                for d in diff:
                    print(d, end="")

    # Count linked vs unlinked in result
    for filepath in files:
        with open(filepath, "r", encoding="utf-8") as f:
            in_sa = False
            for line in f:
                if line.strip() == "## See Also":
                    in_sa = True
                    continue
                if in_sa and line.startswith("## "):
                    break
                if in_sa and line.startswith("- "):
                    if "](" in line:
                        total_linked += 1
                    else:
                        total_unlinked += 1

    print(f"\n{'Would modify' if dry_run else 'Modified'}: {total_changed}/{len(files)} files")
    print(f"Linked: {total_linked}, Unlinked: {total_unlinked}")


if __name__ == "__main__":
    main()
