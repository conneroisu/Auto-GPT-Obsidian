import os
from pathlib import Path
import pprint from pprint


from .obsidian import (
    append_note,
    create_note,
    get_notes,
    get_note,
    get_note_by_path,
    append_note,
    get_note_metadata,
    get_note_content,
    get_note_path,
    get_note_title,
    get_note_tags,
    get_note_links,
    get_note_incoming_links,
    get_note_outgoing_links,
    get_notes_by_tag,
    get_notes_by_tags,
    get_all_tags,
    get_all_notes,
    get_note_stats,
)

# Integration tests

def test_get_notes():
    """Find all notes in the vault."""