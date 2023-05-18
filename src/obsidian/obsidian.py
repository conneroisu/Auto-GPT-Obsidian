from . import AutoGPTObsidian
import os
import obsidiantools.api as otools

plugin = AutoGPTObsidian()

"""
Obsidian Integrations for Auto-GPT using obsidiantools.
"""

def vault_path_set() -> bool:
    """
    Check to see if the vault path is set.
    """
    return True if getvaultpath() is not None else False

def add_tags_to_note(note_path, tags):
    """
    Add tags to an existing note.

    Parameters:
        - path: The path to the note to add tags to.
        - tags: The tags to add to the note in a comma-separated string.
    Returns:
        - a string explaining the result of the operation.
    """
    exists = os.path.isfile(note_path)
    if not exists:
        return "The note specified does not exist."
    # Check to see if there are already tags in the note.
    note = open(note_path, 'r')
    note_lines = note.readlines()
    ## Check if tags: exists in the note's frontmatter
    for line in note_lines:
        if line.startswith("tags:"):
            # check if the tags are enclosed in brackets
            if line.startswith("tags: ["):
                # If they are, remove the end bracket and add the tags to the line, and add an enclosing bracket.
                line = line[:-1] + ", " + tags + "]"
                return "Tags added to note successfully in the frontmatter."
        # If the tags are in list format, add each tag to the list as new tags.
        elif line.startswith("tags:") and line[line.index() + 1].startswith("-") and not line[line.index() + 1].startswith("---")
            # insert each tag individually into the list with preceding - and a space.
            tags_list = tags.split(",").replace(" ", "")
            for tag in tags_list:
                line = line + "\n- " + tag
            return "Tags added to note successfully in the frontmatter."
            # If they are not, add the tags to the line.
        ## Check if tags:: exists in the note's content as the start of a line
        elif line.startswith("tags::"):
            # If it does, add the tags to the line.
            line = line + " " + tags
            return "Tags added to note successfully in the content via an append."
        else:
            # If it does not, add the tags to the line as tags: <tags> in the frontmatter.
            # If a frontmatter exists, add the tags to the frontmatter.
            # If a frontmatter does not exist, create a frontmatter and add the tags to it.
def create_note(title, aliases, tags, summary, content):
    """
    Create a note inside the vault with a title, content, tags, and a summary.

    Parameters:
        - title: The title of the note ending in `.md`.
        - content: The content of the note to be written in Markdown.
        - tags: The tags of the note categorizing the content of the note.
        - summary: The summary of the note.
    Returns:
        - True if the note was created successfully, False otherwise.

    """
    # Get the vault path from the config.
    vault_path = plugin.vault_path
    parent = {"vault_path": vault_path}

    file = open(vault_path + os.path.sep + title, 'w')
    file.write("---\n")
    file.write("aliases: " + aliases + "\n")
    file.write("tags: " + tags + "\n")
    file.write("summary: " + summary + "\n")
    file.write("---\n")
    file.write(content)

    file.close()

    return True

def insert(content, note):
    """
    Insert content into a note.

    Parameters:
        - content: The content to insert into the note.
        - note: The note to insert the content into.
    Returns:
        - The note with the inserted content.
    """
