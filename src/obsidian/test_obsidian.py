# Integration tests
from .obsidian import create_note


class TestCreateNote:
    """
    Pytest class for testing Obsidian
    """

    def test_create_note(self):
        """
        Test the creation of a note with `create_note()`.
        """
        # Create a note.
        note = create_note(
            title="test_note",
            content="This is a test note.",
            tags="test_tag",
            summary="This is a test summary.",
        )

        # Check that the note was created.
        assert note.exists()
