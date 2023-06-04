"""
Import the `os` module to access the environment variables from the `.env` file.
"""
import os

"""
Import the obsidian module to access the obsidian plugin commands.
"""
from obsidian import _create_note, _find_note_by_title, _get_valid_tags


-- TODO - Add tests for the following functions: _get_valid_tag, _create_note, _create_notes, and _find_note_by_title 
def test_create_note() -> None:
    """
    Tests the creation of a note with `create_note()`. More specifically, this test creates a note that is titled "test_note" and has the content "This is a test note."
    Additionally, this test checks that the note is created.
    """
    # Set the vault path with the environment variable from the `.env` file.
    vault_path = os.getenv("OBSIDIAN_VAULT_PATH")
    # Attempt note creation with `create_note()` with the title "test_note" and the content "This is a test note."
    response = _create_note(title="test_note", content="This is a test note.",)
    with _find_note_by_title(title="test_note") as file:
        # Check that the note was created.
        assert file.read() == response
        file.close()
        os.remove(f"{vault_path}{os.sep}test_note.md")


def test_sync_empty() -> None:
    """ 
    Tests the sync function of the obsidian plugin with an empty vault.
    """
    working_directory = os.path.join(
        current_working_directory,
        "autogpt",
        "auto_gpt_workspace",
        git_url.split("/")[-1],
    )
