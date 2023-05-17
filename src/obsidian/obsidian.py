from . import AutoGPTObsidian
import os
import obsidiantools.api as otools

plugin = AutoGPTObsidian()


def add_tags_to_note():
    """

    """


def create_note(title, content, tags, summary):
    """
    Create a note inside the vault with a title, content, tags, and a summary.

    Parameters:
        - title: The title of the note.
        - content: The content of the note.
        - tags: The tags of the note.
        - summary: The summary of the note.
    Returns:
        - The note created as a File object.

    """

    # Get the vault path from the config.
    vault_path = plugin.vault_path()
    parent = {"vault_path": vault_path}

    file = open(vault_path + title, 'w')
    file.write("---\n")
    file.write("tags: " + tags + "\n")
    file.write("summary: " + summary + "\n")
    file.write("---\n")
    file.write(content)

    return file


def insert(content, note):
    """
    Insert content into a note.

    Parameters:
        - content: The content to insert into the note.
        - note: The note to insert the content into.
    Returns:
        - The note with the inserted content.
    """
