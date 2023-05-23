"""
Import the `os` module to access the environment variables from the `.env` file.
"""
import os
from typing import TextIO

"""
Import the `guidance` module to access microsoft guidance a way to inference language models.
"""
import guidance

"""
Obsidian Integrations for Auto-GPT using custom API functions and obsidiantools.
"""

def _note_has_tags(title: str) -> bool: 
    """ 
    Check if a note has tags. Returns true if so. 

    Parameters: 
        - title: The title of the note. In other words, the title is the name of the note. The title is also the name of the file to be produced.
    Returns:
        - True if the note has tags, False if not.
    """

def _create_note(title: str, content: str) -> str:
    """
    Create a note inside the vault with a title, content, tags, and a summary.

    Parameters:
        - title: The title of the note. In other words, the title is the name of the note. The title is also the name of the file to be produced.
        - content: The content of the note to be written in Markdown. In other words, the content of a note is the text to be placed in the main body of the note. 
    Returns:
        - the created note content.

    """
    # Set guidance's OpenAI Model to "text-davinci-003"
    guidance.llm = guidance.llms.OpenAI("text-davinci-003")
    # Set the vault path with the environment variable from the `.env` file.
    vault_path = os.getenv("OBSIDIAN_VAULT_PATH")

    # Create the note with the title and content. Generate the tags, aliases, and summary with guidance.
    create_note_program = guidance("""The following is a note creation program in Markdown format for Obsidian MD. 
    ---
    title: {{title}} 
    aliases: {{gen 'aliases'}} 
    tags: {{gen 'tags'}}
    summary: {{gen 'summary'}}  
    --- 
    {{content}} 
    """)
    created_note_content = create_note_program(
        title=title,
        content=content
    )
    with open(f"{vault_path}{os.sep}{title}.md", "w") as file:
        file.write(created_note_content)
        file.close()

    return created_note_content


def _find_note_by_title(title: str) -> TextIO | None:
    """
    Find a note inside the vault with a title.

    Parameters:
        - title: The title of the note to find in the vault. In other words, the title is the name of the note. The title is also the name of the file to be produced.
    Returns:
        - the found file. Otherwise, returns None.
    """
    vault_path = os.getenv("OBSIDIAN_VAULT_PATH")


    if not title.endswith(".md"):
        title += ".md"

    # Find the note with the title in the vault.

    for root, dirs, files in os.walk(vault_path):
        for file in files:
            if file.endswith(".md") and file == title:
                with open(f"{vault_path}{os.sep}{title}.md", "r") as found_note:
                    return found_note
    return None
