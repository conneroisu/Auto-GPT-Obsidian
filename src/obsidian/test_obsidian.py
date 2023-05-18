# Integration tests
from .obsidian import create_note, get_vault_path

MOCK_VAULT_PATH = "../test_vault/"

def test_get_vault_path():
    """
    Test the retrieval of the vault path with `get_vault_path()`.
    """
    # Get the vault path.
    vault_path = get_vault_path()

    # Check that the vault path is of type str.
    assert type(vault_path) == str
def test_create_note():
    """
    Test the creation of a note with `create_note()`.
    """
    AutoGPTObsidian.vault_path = MOCK_VAULT_PATH
    # Create a note.
    note = create_note(
        title="test_note",
        aliases="test_alias",
        content="This is a test note.",
        tags="test_tag",
        summary="This is a test summary."
    )

    # Check that the note was created.
    assert note is not None